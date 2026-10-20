#!/usr/bin/env python3
"""Local experiment records for Agent Research Atlas (Python 3.10+, stdlib).

This records declared plans and execution evidence. It is not a scientific judge,
an execution sandbox, an independent attestation service, or a publication tool.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import shutil
import signal
import stat
import subprocess
import sys
import time
from typing import Any


SCHEMA_VERSION = 1
SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}\Z")
METRIC_ID = re.compile(r"[A-Za-z][A-Za-z0-9_.-]{0,79}\Z")
JSON_LIMIT = 4 * 1024 * 1024
LABEL = "Integrity checks do not establish scientific validity or publication readiness."


class RecordError(Exception):
    """A plan, path, budget, or integrity condition was not satisfied."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise RecordError(f"Duplicate JSON key: {key}")
        value[key] = item
    return value


def _bad_constant(value: str) -> None:
    raise RecordError(f"Non-finite JSON number is not allowed: {value}")


def finite_tree(value: Any) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise RecordError("NaN and Infinity are not allowed")
    if isinstance(value, dict):
        for child in value.values():
            finite_tree(child)
    elif isinstance(value, list):
        for child in value:
            finite_tree(child)


def parse_json(data: bytes) -> Any:
    if len(data) > JSON_LIMIT:
        raise RecordError("JSON input exceeds the 4 MiB metadata limit")
    try:
        value = json.loads(data, object_pairs_hook=_pairs,
                           parse_constant=_bad_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RecordError(f"Invalid UTF-8 JSON: {exc}") from exc
    finite_tree(value)
    return value


def safe_id(value: str) -> str:
    if not isinstance(value, str) or not SAFE_ID.fullmatch(value):
        raise RecordError("IDs must be 1–64 ASCII letters, digits, underscores or hyphens; start with a letter or digit")
    return value


def relative_parts(value: str, *, allow_dot: bool = False) -> tuple[str, ...]:
    if not isinstance(value, str) or not value or "\x00" in value or "\\" in value:
        raise RecordError("Paths must be nonempty relative POSIX paths without NUL or backslash")
    posix = PurePosixPath(value)
    if posix.is_absolute() or PureWindowsPath(value).drive or ".." in posix.parts:
        raise RecordError(f"Path must stay inside the selected project: {value}")
    if not posix.parts:
        if allow_dot and value == ".":
            return ()
        raise RecordError("A file path cannot be '.'")
    return posix.parts


def no_symlinks(path: Path) -> None:
    """Reject every existing symlink component, including a dangling symlink."""
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        try:
            mode = os.lstat(current).st_mode
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(mode):
            raise RecordError(f"Symlinks are not accepted in record or input paths: {current}")


class Project:
    def __init__(self, root: str | Path):
        supplied = Path(root).expanduser().absolute()
        no_symlinks(supplied)
        if not supplied.is_dir():
            raise RecordError(f"Project root must already be a directory: {supplied}")
        self.root = supplied.resolve()

    def path(self, *parts: str) -> Path:
        path = self.root
        for part in parts:
            path = path.joinpath(*relative_parts(part, allow_dot=True))
        no_symlinks(path)
        if not path.resolve().is_relative_to(self.root):
            raise RecordError("Resolved path escapes the selected project")
        return path

    def mkdir(self, *parts: str, exclusive: bool = False) -> Path:
        path = self.path(*parts)
        current = self.root
        components = path.relative_to(self.root).parts
        for index, part in enumerate(components):
            current /= part
            try:
                current.mkdir()
            except FileExistsError:
                no_symlinks(current)
                if not current.is_dir() or (exclusive and index == len(components) - 1):
                    raise RecordError(f"Path already exists or is not a directory: {current}")
        return self.path(*parts)

    def experiment(self, experiment_id: str) -> Path:
        return self.path("research-atlas", "experiments", safe_id(experiment_id))


def read_bytes(path: Path, *, limit: int | None = JSON_LIMIT) -> bytes:
    path = path.absolute()
    no_symlinks(path)
    if not stat.S_ISREG(os.lstat(path).st_mode):
        raise RecordError(f"Expected a regular file: {path}")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise RecordError(f"Expected a regular file: {path}")
        data = stream.read() if limit is None else stream.read(limit + 1)
    if limit is not None and len(data) > limit:
        raise RecordError(f"Metadata file exceeds {limit} bytes: {path}")
    return data


def open_new(path: Path):
    no_symlinks(path.absolute())
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    return os.fdopen(os.open(path, flags, 0o600), "wb")


def write_new(path: Path, data: bytes) -> None:
    with open_new(path) as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def write_record(path: Path, value: Any) -> None:
    data = json_bytes(value)
    write_new(path, data)
    write_new(path.with_suffix(path.suffix + ".sha256"), (digest(data) + "\n").encode())


def checked_record(path: Path) -> dict[str, Any]:
    data = read_bytes(path)
    expected = read_bytes(path.with_suffix(path.suffix + ".sha256")).decode().strip()
    if digest(data) != expected:
        raise RecordError(f"Record checksum mismatch: {path.name}")
    value = parse_json(data)
    if not isinstance(value, dict):
        raise RecordError(f"Expected a JSON object: {path.name}")
    return value


@contextlib.contextmanager
def project_lock(project: Project):
    project.mkdir("research-atlas", "experiments")
    lock = project.path("research-atlas", "experiments", "execution.lock")
    try:
        write_new(lock, json_bytes({"pid": os.getpid(), "created_at": utc_now()}))
    except FileExistsError as exc:
        raise RecordError("Another operation holds execution.lock. Inspect a stale lock and its process before manually removing it.") from exc
    try:
        yield
    finally:
        no_symlinks(lock)
        lock.unlink()


def object_fields(value: Any, fields: set[str], label: str,
                  optional: set[str] | None = None) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RecordError(f"{label} must be an object")
    missing = fields - value.keys()
    extra = value.keys() - fields - (optional or set())
    if missing or extra:
        raise RecordError(f"{label}: missing={sorted(missing)}, unsupported={sorted(extra)}")
    return value


def nonempty(value: Any, label: str) -> None:
    if not isinstance(value, str) or not value.strip() or "\x00" in value:
        raise RecordError(f"{label} must be nonempty text without NUL")


def number(value: Any, label: str, *, positive: bool = False) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RecordError(f"{label} must be a finite number")
    try:
        valid = math.isfinite(value) and (value > 0 if positive else value >= 0)
    except OverflowError:
        valid = False
    if not valid:
        raise RecordError(f"{label} must be finite and {'positive' if positive else 'nonnegative'}")


def text_list(value: Any, label: str) -> None:
    if not isinstance(value, list) or not value:
        raise RecordError(f"{label} must be a nonempty list")
    for item in value:
        nonempty(item, label)


def validate_plan(plan: Any) -> dict[str, Any]:
    fields = {"schema_version", "experiment_id", "title", "hypothesis", "rival_explanation",
              "primary_metric", "experimental_unit", "data_split", "controls", "baselines",
              "seeds", "budget", "decision_thresholds", "command", "synthetic"}
    object_fields(plan, fields, "plan", {"notes"})
    if type(plan["schema_version"]) is not int or plan["schema_version"] != SCHEMA_VERSION:
        raise RecordError("Unsupported plan schema_version (expected integer 1)")
    safe_id(plan["experiment_id"])
    for key in ("title", "hypothesis", "rival_explanation", "experimental_unit"):
        nonempty(plan[key], key)
    if "notes" in plan:
        nonempty(plan["notes"], "notes")
    if type(plan["synthetic"]) is not bool:
        raise RecordError("synthetic must be an explicit boolean")
    metric = object_fields(plan["primary_metric"], {"name", "direction", "unit"}, "primary_metric")
    if not isinstance(metric["name"], str) or not METRIC_ID.fullmatch(metric["name"]):
        raise RecordError("primary_metric.name must be a short ASCII metric identifier")
    nonempty(metric["unit"], "primary_metric.unit")
    if metric["direction"] not in ("maximize", "minimize"):
        raise RecordError("primary_metric.direction must be maximize or minimize")
    split = object_fields(plan["data_split"], {"development", "evaluation", "leakage_controls"}, "data_split")
    for key, value in split.items():
        nonempty(value, f"data_split.{key}")
    for key in ("controls", "baselines"):
        text_list(plan[key], key)
    seeds = plan["seeds"]
    if not isinstance(seeds, list) or not seeds or any(type(seed) is not int or seed < 0 for seed in seeds):
        raise RecordError("seeds must be a nonempty list of nonnegative integers")
    if len(set(seeds)) != len(seeds):
        raise RecordError("seeds must be unique")
    budget = object_fields(plan["budget"], {"max_runs", "max_run_seconds", "max_total_seconds"}, "budget")
    if type(budget["max_runs"]) is not int or budget["max_runs"] < 1:
        raise RecordError("budget.max_runs must be a positive integer")
    for key in ("max_run_seconds", "max_total_seconds"):
        number(budget[key], f"budget.{key}", positive=True)
    if budget["max_run_seconds"] > budget["max_total_seconds"]:
        raise RecordError("Per-run budget cannot exceed total local execution budget")
    criteria = object_fields(plan["decision_thresholds"], {"success", "failure", "inconclusive"}, "decision_thresholds")
    for key, value in criteria.items():
        nonempty(value, f"decision_thresholds.{key}")
    command = object_fields(plan["command"], {"argv", "cwd", "input_files"}, "command")
    text_list(command["argv"], "command.argv")
    relative_parts(command["cwd"], allow_dot=True)
    inputs = command["input_files"]
    if not isinstance(inputs, list) or any(not isinstance(item, str) for item in inputs):
        raise RecordError("command.input_files must be a list of explicit relative paths")
    if len(inputs) != len(set(inputs)):
        raise RecordError("command.input_files must not contain duplicates")
    for item in inputs:
        relative_parts(item)
    finite_tree(plan)
    return plan


def load_plan(project: Project, experiment_id: str) -> tuple[dict[str, Any], bytes]:
    path = project.experiment(experiment_id) / "plan.json"
    data = read_bytes(path)
    plan = validate_plan(parse_json(data))
    if plan["experiment_id"] != experiment_id:
        raise RecordError("Plan experiment_id differs from its directory")
    return plan, data


def load_frozen(project: Project, experiment_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    plan, data = load_plan(project, experiment_id)
    frozen = checked_record(project.experiment(experiment_id) / "freeze.json")
    if frozen.get("schema_version") != SCHEMA_VERSION or frozen.get("plan_sha256") != digest(data):
        raise RecordError("Frozen plan has changed or its schema is unsupported")
    if frozen.get("experiment_id") != experiment_id or frozen.get("mode") not in ("prospective", "exploratory"):
        raise RecordError("Invalid freeze identity or mode")
    if frozen.get("synthetic") is not plan["synthetic"]:
        raise RecordError("Frozen synthetic label differs from plan")
    return plan, frozen


def save_plan(project: Project, source: str) -> dict[str, Any]:
    plan = validate_plan(parse_json(read_bytes(Path(source).expanduser().absolute())))
    directory = project.mkdir("research-atlas", "experiments", plan["experiment_id"], exclusive=True)
    write_new(directory / "plan.json", json_bytes(plan))
    return {"status": "plan_recorded", "experiment_id": plan["experiment_id"],
            "synthetic": plan["synthetic"], "note": "Schema checks only; feasibility and scientific validity are untested."}


def freeze_plan(project: Project, experiment_id: str, mode: str, rationale: str) -> dict[str, Any]:
    nonempty(rationale, "rationale")
    if mode not in ("prospective", "exploratory"):
        raise RecordError("mode must be prospective or exploratory")
    plan, data = load_plan(project, experiment_id)
    frozen = {"schema_version": SCHEMA_VERSION, "experiment_id": experiment_id,
              "created_at": utc_now(), "plan_sha256": digest(data), "mode": mode,
              "mode_is_operator_declaration": True, "rationale": rationale,
              "synthetic": plan["synthetic"]}
    write_record(project.experiment(experiment_id) / "freeze.json", frozen)
    return {"status": "frozen", **frozen,
            "note": "Local freeze records timing; it does not independently prove no earlier observations existed."}


def hash_file(path: Path) -> dict[str, Any]:
    no_symlinks(path.absolute())
    if not stat.S_ISREG(os.lstat(path).st_mode):
        raise RecordError(f"Expected a regular file: {path}")
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    hasher = hashlib.sha256()
    with os.fdopen(fd, "rb") as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise RecordError(f"Expected a regular file: {path}")
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
        after = os.fstat(stream.fileno())
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise RecordError(f"File changed while hashing: {path}")
    return {"sha256": hasher.hexdigest(), "bytes": after.st_size}


def git_provenance(project: Project) -> dict[str, Any]:
    executable = shutil.which("git")
    if not executable:
        return {"available": False, "reason": "git_not_found"}
    base = [executable, "--no-optional-locks", "-c", "core.fsmonitor=false"]
    try:
        head = subprocess.run(base + ["rev-parse", "HEAD"], cwd=project.root,
                              capture_output=True, timeout=3, check=False)
        if head.returncode:
            return {"available": False, "reason": "no_readable_git_HEAD"}
        state = subprocess.run(base + ["status", "--porcelain=v1", "--untracked-files=no"],
                               cwd=project.root, capture_output=True, timeout=3, check=False)
        return {"available": True, "head": head.stdout.decode().strip(),
                "tracked_files_dirty": bool(state.stdout) if state.returncode == 0 else None,
                "tracked_status_sha256": digest(state.stdout) if state.returncode == 0 else None,
                "scope": "HEAD and tracked-file status; untracked inputs are covered only if explicitly declared."}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "reason": type(exc).__name__}


def run_directories(project: Project, experiment_id: str) -> list[Path]:
    directory = project.path("research-atlas", "experiments", experiment_id, "runs")
    if not directory.exists():
        return []
    result = []
    for child in sorted(directory.iterdir()):
        safe_id(child.name)
        no_symlinks(child)
        if not child.is_dir():
            raise RecordError(f"Unexpected non-directory in runs: {child.name}")
        result.append(child)
    return result


def prior_reservations(project: Project, experiment_id: str) -> tuple[int, float]:
    count, seconds = 0, 0.0
    for directory in run_directories(project, experiment_id):
        attempt = checked_record(directory / "attempt.json")
        if attempt.get("budget_reserved", {}).get("run_slot") is True:
            count += 1
            reserved = attempt["budget_reserved"]["seconds"]
            number(reserved, "reserved seconds")
            seconds += reserved
    return count, seconds


def new_attempt(project: Project, experiment_id: str, run_id: str,
                frozen: dict[str, Any], kind: str, reserved: float = 0.0,
                run_slot: bool = False, **extra: Any) -> tuple[Path, dict[str, Any]]:
    safe_id(run_id)
    directory = project.mkdir("research-atlas", "experiments", experiment_id, "runs", run_id, exclusive=True)
    attempt = {"schema_version": SCHEMA_VERSION, "experiment_id": experiment_id,
               "run_id": run_id, "kind": kind, "created_at": utc_now(),
               "plan_sha256": frozen["plan_sha256"], "mode": frozen["mode"],
               "synthetic": frozen["synthetic"],
               "budget_reserved": {"run_slot": run_slot, "seconds": reserved}, **extra}
    write_record(directory / "attempt.json", attempt)
    return directory, attempt


def finish_record(directory: Path, attempt: dict[str, Any], status: str,
                  files: list[str], **extra: Any) -> dict[str, Any]:
    manifest = {name: hash_file(directory / name) for name in files}
    record = {**attempt, "status": status, "finished_at": utc_now(),
              "attempt_sha256": hash_file(directory / "attempt.json")["sha256"],
              "files": manifest, "scientific_verdict": "not_assessed", **extra}
    write_record(directory / "record.json", record)
    return record


def terminate_process(process: subprocess.Popen) -> None:
    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            process.kill()
    except ProcessLookupError:
        pass
    process.wait()


def run_local(project: Project, experiment_id: str, run_id: str, *, authorized: bool,
              timeout_seconds: float | None = None, seed: int | None = None) -> dict[str, Any]:
    if not authorized:
        raise RecordError("run requires --authorized-local to attest that this exact local execution is already authorized; the flag is not a sandbox or permission grant")
    plan, frozen = load_frozen(project, experiment_id)
    validate_records(project, experiment_id, allow_incomplete=True)
    chosen_seed = plan["seeds"][0] if seed is None else seed
    if chosen_seed not in plan["seeds"] or type(chosen_seed) is not int:
        raise RecordError("Run seed must be one of the frozen plan seeds")
    budget = plan["budget"]
    requested = budget["max_run_seconds"] if timeout_seconds is None else timeout_seconds
    number(requested, "timeout_seconds", positive=True)
    prior_count, prior_seconds = prior_reservations(project, experiment_id)
    reason = None
    if requested > budget["max_run_seconds"]:
        reason = "requested_timeout_exceeds_per_run_budget"
    elif prior_count >= budget["max_runs"]:
        reason = "local_run_count_budget_exhausted"
    elif requested > budget["max_total_seconds"] - prior_seconds:
        reason = "reserved_local_time_budget_exhausted"
    argv = [item.replace("{seed}", str(chosen_seed)) for item in plan["command"]["argv"]]
    directory, attempt = new_attempt(project, experiment_id, run_id, frozen, "local",
                                     reserved=0.0 if reason else requested, run_slot=not bool(reason),
                                     argv=argv, cwd=plan["command"]["cwd"], seed=chosen_seed,
                                     timeout_seconds=requested,
                                     authorization="operator_attests_existing_local_authorization")
    if reason:
        return finish_record(directory, attempt, "cancelled", [], reason=reason,
                             exit_code=None, elapsed_seconds=0.0)
    started = time.monotonic()
    status, exit_code, error = "launch_failed", None, None
    process: subprocess.Popen | None = None
    provenance: dict[str, Any] = {}
    with open_new(directory / "stdout.txt") as stdout, open_new(directory / "stderr.txt") as stderr:
        try:
            cwd = project.path(plan["command"]["cwd"])
            if not cwd.is_dir():
                raise RecordError("command.cwd is not a directory")
            provenance["declared_inputs"] = {name: hash_file(project.path(name))
                                              for name in plan["command"]["input_files"]}
            provenance["git"] = git_provenance(project)
            provenance["executable_resolved"] = shutil.which(argv[0])
            process = subprocess.Popen(argv, cwd=cwd, stdin=subprocess.DEVNULL,
                                       stdout=stdout, stderr=stderr, shell=False,
                                       start_new_session=(os.name == "posix"))
            try:
                exit_code = process.wait(timeout=requested)
                status = "succeeded" if exit_code == 0 else "failed"
            except subprocess.TimeoutExpired:
                terminate_process(process)
                exit_code, status = process.returncode, "timed_out"
            except KeyboardInterrupt:
                terminate_process(process)
                exit_code, status = process.returncode, "interrupted"
        except (OSError, RecordError, ValueError) as exc:
            error = {"type": type(exc).__name__, "message": str(exc)}
            if process is not None and process.poll() is None:
                terminate_process(process)
        finally:
            # A normally exited launcher may leave background workers behind.
            # On POSIX, close this run's process group before hashing its logs.
            if process is not None and os.name == "posix":
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            stdout.flush()
            stderr.flush()
            os.fsync(stdout.fileno())
            os.fsync(stderr.fileno())
    return finish_record(directory, attempt, status, ["stdout.txt", "stderr.txt"],
                         exit_code=exit_code, elapsed_seconds=time.monotonic() - started,
                         provenance=provenance, error=error)


def validate_result(result: Any, plan: dict[str, Any]) -> dict[str, Any]:
    object_fields(result, {"schema_version", "synthetic", "status", "metrics", "elapsed_seconds", "notes"}, "external result")
    if type(result["schema_version"]) is not int or result["schema_version"] != SCHEMA_VERSION:
        raise RecordError("Unsupported external result schema")
    if type(result["synthetic"]) is not bool or result["synthetic"] is not plan["synthetic"]:
        raise RecordError("External result and plan must have the same explicit synthetic label")
    if result["status"] not in ("succeeded", "failed", "timed_out", "cancelled", "interrupted", "launch_failed"):
        raise RecordError("Invalid external execution status")
    if not isinstance(result["metrics"], dict):
        raise RecordError("metrics must be an object of finite numeric measurements")
    for key, value in result["metrics"].items():
        if not METRIC_ID.fullmatch(key):
            raise RecordError("Invalid metric identifier")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise RecordError("Metric values must be finite numbers")
        try:
            finite = math.isfinite(value)
        except OverflowError:
            finite = False
        if not finite:
            raise RecordError("Metric values must be finite numbers")
    if result["status"] == "succeeded" and plan["primary_metric"]["name"] not in result["metrics"]:
        raise RecordError("A successful external result must contain the planned primary metric")
    number(result["elapsed_seconds"], "elapsed_seconds")
    nonempty(result["notes"], "notes")
    return result


def import_result(project: Project, experiment_id: str, run_id: str,
                  source: str, origin: str) -> dict[str, Any]:
    nonempty(origin, "origin")
    plan, frozen = load_frozen(project, experiment_id)
    validate_records(project, experiment_id, allow_incomplete=True)
    source_path = Path(source).expanduser().absolute()
    data = read_bytes(source_path)
    result = validate_result(parse_json(data), plan)
    directory, attempt = new_attempt(project, experiment_id, run_id, frozen, "import",
                                     origin=origin, source_path=str(source_path),
                                     source_sha256=digest(data),
                                     source_authenticity="operator_supplied_not_independently_verified")
    write_new(directory / "imported-result.json", data)
    return finish_record(directory, attempt, "imported", ["imported-result.json"],
                         external_status=result["status"], metrics=result["metrics"],
                         elapsed_seconds=result["elapsed_seconds"],
                         external_budget_compliance="not_assessed", notes=result["notes"])


def validate_records(project: Project, experiment_id: str, *, allow_incomplete: bool = False) -> dict[str, Any]:
    plan, frozen = load_frozen(project, experiment_id)
    summaries, incomplete = [], []
    for directory in run_directories(project, experiment_id):
        attempt = checked_record(directory / "attempt.json")
        if (attempt.get("schema_version") != SCHEMA_VERSION
                or attempt.get("run_id") != directory.name
                or attempt.get("experiment_id") != experiment_id
                or attempt.get("plan_sha256") != frozen["plan_sha256"]
                or attempt.get("synthetic") is not plan["synthetic"]):
            raise RecordError(f"Attempt identity or frozen plan mismatch: {directory.name}")
        no_symlinks(directory / "record.json")
        if not (directory / "record.json").exists():
            incomplete.append(directory.name)
            continue
        record = checked_record(directory / "record.json")
        if any(record.get(key) != value for key, value in attempt.items()):
            raise RecordError(f"Final record differs from reserved attempt: {directory.name}")
        if record.get("attempt_sha256") != hash_file(directory / "attempt.json")["sha256"]:
            raise RecordError(f"Attempt checksum changed: {directory.name}")
        files = record.get("files")
        if not isinstance(files, dict):
            raise RecordError("Missing file manifest")
        for name, metadata in files.items():
            parts = relative_parts(name)
            if len(parts) != 1:
                raise RecordError("Record artifacts must be direct files in the run directory")
            if hash_file(directory / name) != metadata:
                raise RecordError(f"Artifact checksum mismatch: {directory.name}/{name}")
        if record.get("kind") == "import":
            data = read_bytes(directory / "imported-result.json")
            result = validate_result(parse_json(data), plan)
            if digest(data) != record.get("source_sha256") or result["metrics"] != record.get("metrics"):
                raise RecordError(f"Imported result differs from its source record: {directory.name}")
            if result["status"] != record.get("external_status"):
                raise RecordError("Imported execution status changed")
        summaries.append({"run_id": directory.name, "status": record.get("status"),
                          "synthetic": record["synthetic"]})
    if incomplete and not allow_incomplete:
        raise RecordError(f"Incomplete attempts retained (inspect, do not delete): {', '.join(incomplete)}")
    return {"status": "integrity_checked", "experiment_id": experiment_id,
            "mode": frozen["mode"], "synthetic": plan["synthetic"], "runs": summaries,
            "incomplete_attempts": incomplete, "scientific_verdict": "not_assessed", "note": LABEL}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--root", required=True, help="Existing project directory; all records stay beneath it")
    commands = result.add_subparsers(dest="action", required=True)
    plan = commands.add_parser("plan", help="Validate schema and record a new plan; never overwrite")
    plan.add_argument("--file", required=True)
    freeze = commands.add_parser("freeze", help="Freeze exact plan bytes and declared study mode once")
    freeze.add_argument("experiment_id")
    freeze.add_argument("--mode", choices=("prospective", "exploratory"), required=True)
    freeze.add_argument("--rationale", required=True)
    run = commands.add_parser("run", help="Execute the frozen argv under an already authorized local scope")
    run.add_argument("experiment_id")
    run.add_argument("--run-id", required=True)
    run.add_argument("--authorized-local", action="store_true")
    run.add_argument("--timeout-seconds", type=float)
    run.add_argument("--seed", type=int)
    imported = commands.add_parser("import-result", help="Preserve an externally supplied result and its origin")
    imported.add_argument("experiment_id")
    imported.add_argument("--run-id", required=True)
    imported.add_argument("--file", required=True)
    imported.add_argument("--origin", required=True)
    verify = commands.add_parser("validate-record", help="Check local record integrity, not scientific validity")
    verify.add_argument("experiment_id")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        project = Project(args.root)
        with project_lock(project):
            if args.action == "plan":
                result = save_plan(project, args.file)
            elif args.action == "freeze":
                result = freeze_plan(project, args.experiment_id, args.mode, args.rationale)
            elif args.action == "run":
                result = run_local(project, args.experiment_id, args.run_id,
                                   authorized=args.authorized_local,
                                   timeout_seconds=args.timeout_seconds, seed=args.seed)
            elif args.action == "import-result":
                result = import_result(project, args.experiment_id, args.run_id, args.file, args.origin)
            else:
                result = validate_records(project, args.experiment_id)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
        if args.action == "run" and result["status"] != "succeeded":
            return 3 if result["status"] == "cancelled" else 4
        return 0
    except (RecordError, OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
