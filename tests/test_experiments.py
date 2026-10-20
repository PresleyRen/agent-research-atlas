"""Meaningful integrity and execution tests using only the synthetic fixture."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "skills/agent-research-atlas/scripts/experiments.py"
EXAMPLE = REPO / "skills/agent-research-atlas/assets/experiment-plan.example.json"
SPEC = importlib.util.spec_from_file_location("atlas_experiments", SCRIPT)
EXPERIMENTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPERIMENTS)


class ExperimentRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="atlas-experiment-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()
        (self.root / "examples").mkdir()
        shutil.copyfile(REPO / "examples/tiny_agent_experiment.py",
                        self.root / "examples/tiny_agent_experiment.py")
        self.plan = json.loads(EXAMPLE.read_text())
        self.plan["experiment_id"] = "test-fixture"
        self.plan["command"]["argv"][0] = sys.executable
        self.plan_path = self.root / "input-plan.json"

    @property
    def directory(self):
        return self.root / "research-atlas/experiments/test-fixture"

    def command(self, *args):
        return [sys.executable, str(SCRIPT), "--root", str(self.root), *args]

    def call(self, *args, expected=0):
        completed = subprocess.run(self.command(*args), capture_output=True, text=True, timeout=15)
        self.assertEqual(completed.returncode, expected, completed.stdout + completed.stderr)
        return json.loads(completed.stdout if completed.stdout else completed.stderr)

    def prepare(self, mode="success", *, budget=None):
        self.plan["command"]["argv"] += ["--mode", mode]
        if budget:
            self.plan["budget"] = budget
        self.plan_path.write_text(json.dumps(self.plan))
        self.call("plan", "--file", str(self.plan_path))
        self.call("freeze", "test-fixture", "--mode", "exploratory", "--rationale",
                  "Synthetic fixture developed before this test; no scientific prospective claim.")

    def run_fixture(self, run_id="run-one", *extra, expected=0):
        return self.call("run", "test-fixture", "--run-id", run_id,
                         "--authorized-local", *extra, expected=expected)

    def test_success_preserves_raw_logs_and_synthetic_label(self):
        self.prepare()
        result = self.run_fixture("seed-eleven", "--seed", "11")
        run = self.directory / "runs/seed-eleven"
        raw = json.loads((run / "stdout.txt").read_text())
        self.assertTrue(raw["synthetic"])
        self.assertTrue(result["synthetic"])
        self.assertEqual(result["scientific_verdict"], "not_assessed")
        self.assertEqual(result["seed"], 11)
        self.assertEqual(result["exit_code"], 0)
        self.assertIn("examples/tiny_agent_experiment.py", result["provenance"]["declared_inputs"])
        self.assertEqual(self.call("validate-record", "test-fixture")["status"], "integrity_checked")

    def test_nonzero_exit_and_stderr_are_retained(self):
        self.prepare("fail")
        result = self.run_fixture(expected=4)
        run = self.directory / "runs/run-one"
        self.assertEqual((result["status"], result["exit_code"]), ("failed", 7))
        self.assertIn("SYNTHETIC", (run / "stdout.txt").read_text())
        self.assertIn("preserve this stderr", (run / "stderr.txt").read_text())
        self.assertEqual(self.call("validate-record", "test-fixture")["runs"][0]["status"], "failed")

    def test_timeout_kills_fixture_and_retains_partial_stdout(self):
        self.prepare("timeout", budget={"max_runs": 2, "max_run_seconds": 0.25, "max_total_seconds": 0.5})
        result = self.run_fixture(expected=4)
        self.assertEqual(result["status"], "timed_out")
        self.assertIsNotNone(result["exit_code"])
        self.assertIn("SYNTHETIC waiting", (self.directory / "runs/run-one/stdout.txt").read_text())
        self.assertLess(result["elapsed_seconds"], 4)
        self.call("validate-record", "test-fixture")

    def test_no_implicit_execution_authorization(self):
        self.prepare()
        result = self.call("run", "test-fixture", "--run-id", "unauthorized", expected=2)
        self.assertIn("already authorized", result["error"])
        self.assertFalse((self.directory / "runs/unauthorized").exists())

    def test_frozen_plan_edit_is_detected_before_execution(self):
        self.prepare()
        path = self.directory / "plan.json"
        content = json.loads(path.read_text())
        content["hypothesis"] += " CHANGED"
        path.write_text(json.dumps(content))
        self.assertIn("Frozen plan has changed", self.run_fixture(expected=2)["error"])
        self.assertFalse((self.directory / "runs").exists())

    def test_freeze_and_run_ids_cannot_be_overwritten(self):
        self.prepare()
        frozen = (self.directory / "freeze.json").read_bytes()
        self.call("freeze", "test-fixture", "--mode", "prospective", "--rationale", "Changed claim", expected=2)
        self.assertEqual(frozen, (self.directory / "freeze.json").read_bytes())
        self.run_fixture()
        original = (self.directory / "runs/run-one/record.json").read_bytes()
        self.run_fixture(expected=2)
        self.assertEqual(original, (self.directory / "runs/run-one/record.json").read_bytes())

    def test_plan_command_does_not_replace_existing_plan(self):
        self.prepare()
        original = (self.directory / "plan.json").read_bytes()
        self.call("plan", "--file", str(self.plan_path), expected=2)
        self.assertEqual(original, (self.directory / "plan.json").read_bytes())

    def test_failed_attempt_spends_budget_and_cancellation_is_preserved(self):
        self.prepare("fail", budget={"max_runs": 1, "max_run_seconds": 1, "max_total_seconds": 1})
        self.run_fixture("failure", expected=4)
        cancelled = self.run_fixture("cancelled", expected=3)
        self.assertEqual(cancelled["reason"], "local_run_count_budget_exhausted")
        self.assertFalse(cancelled["budget_reserved"]["run_slot"])
        self.assertFalse((self.directory / "runs/cancelled/stdout.txt").exists())
        report = self.call("validate-record", "test-fixture")
        self.assertEqual({run["status"] for run in report["runs"]}, {"cancelled", "failed"})

    def test_total_budget_is_conservative_and_per_run_override_is_bounded(self):
        self.prepare(budget={"max_runs": 4, "max_run_seconds": 2, "max_total_seconds": 3})
        self.run_fixture("first")
        exhausted = self.run_fixture("too-much-total", expected=3)
        self.assertEqual(exhausted["reason"], "reserved_local_time_budget_exhausted")
        too_long = self.run_fixture("too-long", "--timeout-seconds", "3", expected=3)
        self.assertEqual(too_long["reason"], "requested_timeout_exceeds_per_run_budget")
        self.run_fixture("shorter", "--timeout-seconds", "1")
        self.call("validate-record", "test-fixture")

    def test_hash_tamper_is_detected_and_not_silently_repaired(self):
        self.prepare()
        self.run_fixture()
        output = self.directory / "runs/run-one/stdout.txt"
        output.write_bytes(output.read_bytes() + b"tampered\n")
        result = self.call("validate-record", "test-fixture", expected=2)
        self.assertIn("Artifact checksum mismatch", result["error"])
        self.run_fixture("next", expected=2)
        self.assertTrue(output.read_bytes().endswith(b"tampered\n"))

    def test_record_and_freeze_checksums_are_verified(self):
        self.prepare()
        self.run_fixture()
        record = self.directory / "runs/run-one/record.json"
        record.write_bytes(record.read_bytes() + b" ")
        self.assertIn("checksum mismatch", self.call("validate-record", "test-fixture", expected=2)["error"])

    def test_import_keeps_source_bytes_and_does_not_invent_a_verdict(self):
        self.prepare()
        self.run_fixture()
        source = self.directory / "runs/run-one/stdout.txt"
        result = self.call("import-result", "test-fixture", "--run-id", "external-copy",
                           "--file", str(source), "--origin", "Local SYNTHETIC demo stdout")
        imported = self.directory / "runs/external-copy/imported-result.json"
        self.assertEqual(source.read_bytes(), imported.read_bytes())
        self.assertEqual(result["external_status"], "succeeded")
        self.assertEqual(result["scientific_verdict"], "not_assessed")
        self.assertEqual(result["source_authenticity"], "operator_supplied_not_independently_verified")
        self.call("validate-record", "test-fixture")

    def test_failed_external_result_with_no_metric_is_retained(self):
        self.prepare()
        source = self.root / "external-failure.json"
        source.write_text(json.dumps({"schema_version": 1, "synthetic": True,
                                     "status": "failed", "metrics": {}, "elapsed_seconds": 12,
                                     "notes": "SYNTHETIC external failure record"}))
        result = self.call("import-result", "test-fixture", "--run-id", "external-failure",
                           "--file", str(source), "--origin", "Synthetic outside-run fixture")
        self.assertEqual(result["external_status"], "failed")
        self.assertEqual(result["external_budget_compliance"], "not_assessed")
        self.call("validate-record", "test-fixture")

    def test_nonfinite_numbers_duplicate_keys_and_wrong_synthetic_labels_rejected(self):
        for data in (b'{"x":NaN}', b'{"x":Infinity}', b'{"x":1e999}', b'{"x":1,"x":2}'):
            with self.subTest(data=data), self.assertRaises(EXPERIMENTS.RecordError):
                EXPERIMENTS.parse_json(data)
        self.prepare()
        source = self.root / "bad-result.json"
        for value in (float("nan"), float("inf")):
            source.write_text(json.dumps({"schema_version": 1, "synthetic": True, "status": "succeeded",
                                         "metrics": {"accuracy": value}, "elapsed_seconds": 0, "notes": "SYNTHETIC"}))
            self.call("import-result", "test-fixture", "--run-id", "bad",
                      "--file", str(source), "--origin", "Synthetic invalid result", expected=2)
        self.assertFalse((self.directory / "runs/bad").exists())
        result = {"schema_version": 1, "synthetic": False, "status": "succeeded",
                  "metrics": {"accuracy": 1}, "elapsed_seconds": 0, "notes": "Mislabeled fixture"}
        with self.assertRaises(EXPERIMENTS.RecordError):
            EXPERIMENTS.validate_result(result, self.plan)

    def test_path_traversal_and_external_cwd_are_rejected(self):
        for value in ("../escape", "/tmp/escape", "C:\\escape", "name/child", ".."):
            with self.subTest(value=value), self.assertRaises(EXPERIMENTS.RecordError):
                EXPERIMENTS.safe_id(value)
        for value in ("../escape", "/tmp", "C:\\escape", "ok/../outside"):
            candidate = json.loads(json.dumps(self.plan))
            candidate["command"]["cwd"] = value
            with self.subTest(value=value), self.assertRaises(EXPERIMENTS.RecordError):
                EXPERIMENTS.validate_plan(candidate)

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_artifact_directory_symlink_cannot_escape_project(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.root / "research-atlas").symlink_to(outside, target_is_directory=True)
        self.plan_path.write_text(json.dumps(self.plan))
        self.call("plan", "--file", str(self.plan_path), expected=2)
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_nested_run_symlink_and_cwd_symlink_are_rejected(self):
        self.prepare()
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.directory / "runs").symlink_to(outside, target_is_directory=True)
        self.run_fixture(expected=2)
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_input_symlink_is_a_retained_launch_failure(self):
        self.prepare()
        original = self.root / "examples/tiny_agent_experiment.py"
        outside = Path(self.temp.name) / "outside-fixture.py"
        original.rename(outside)
        original.symlink_to(outside)
        result = self.run_fixture(expected=4)
        self.assertEqual(result["status"], "launch_failed")
        self.assertIn("Symlinks", result["error"]["message"])
        self.call("validate-record", "test-fixture")

    def test_concurrent_execution_cannot_bypass_budget_lock(self):
        self.prepare("timeout", budget={"max_runs": 1, "max_run_seconds": 0.6, "max_total_seconds": 0.6})
        process = subprocess.Popen(self.command("run", "test-fixture", "--run-id", "first",
                                                "--authorized-local"), stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        try:
            lock = self.root / "research-atlas/experiments/execution.lock"
            deadline = time.monotonic() + 5
            while not lock.exists() and process.poll() is None and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertTrue(lock.exists())
            result = self.run_fixture("concurrent", expected=2)
            self.assertIn("holds execution.lock", result["error"])
            stdout, stderr = process.communicate(timeout=8)
            self.assertEqual(process.returncode, 4, stdout + stderr)
            self.assertFalse((self.directory / "runs/concurrent").exists())
            self.run_fixture("after", expected=3)
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()

    def test_incomplete_attempt_is_retained_and_keeps_reservation(self):
        self.prepare(budget={"max_runs": 1, "max_run_seconds": 1, "max_total_seconds": 1})
        project = EXPERIMENTS.Project(self.root)
        _, frozen = EXPERIMENTS.load_frozen(project, "test-fixture")
        directory, _ = EXPERIMENTS.new_attempt(project, "test-fixture", "incomplete", frozen,
                                              "local", reserved=1, run_slot=True)
        self.call("validate-record", "test-fixture", expected=2)
        result = self.run_fixture("after-incomplete", expected=3)
        self.assertEqual(result["reason"], "local_run_count_budget_exhausted")
        self.assertTrue((directory / "attempt.json").is_file())
        self.assertFalse((directory / "record.json").exists())


if __name__ == "__main__":
    unittest.main()
