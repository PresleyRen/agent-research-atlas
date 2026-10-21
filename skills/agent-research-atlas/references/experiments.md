# Experiment planning and execution records

Use `scripts/experiments.py` when an idea has been narrowed enough to name a hypothesis, a rival explanation, data, a baseline, an observable metric, and an explicit execution budget. It uses Python 3.10+ and the standard library. The helper makes no network calls and installs no software. A command you authorize and supply in a plan can have its own dependencies, network access, costs, and effects.

The tool checks schema and local record integrity. It does not decide whether the hypothesis is true, whether a design is scientifically adequate, whether an implementation matches the proposed mechanism, whether an idea is novel, or whether a paper is publishable. `scientific_verdict` is always `not_assessed`. Execution status `succeeded` means that the direct child process exited with code 0.

## Commands

Run from the repository root, or replace script and input paths with the corresponding paths in your installation. `--root` must name an existing project directory and precede the subcommand. It is the destination and the reference point for plan `cwd` and `input_files`; it does not change how your shell resolves `--file`.

```bash
python3 skills/agent-research-atlas/scripts/experiments.py --root . plan \
  --file skills/agent-research-atlas/assets/experiment-plan.example.json

python3 skills/agent-research-atlas/scripts/experiments.py --root . freeze \
  synthetic-routing-demo --mode exploratory \
  --rationale 'This hand-authored synthetic fixture already existed; it demonstrates recording only.'

# Run only after this exact local command and its scope have been authorized.
python3 skills/agent-research-atlas/scripts/experiments.py --root . run \
  synthetic-routing-demo --run-id seed-7 --seed 7 --authorized-local

python3 skills/agent-research-atlas/scripts/experiments.py --root . validate-record \
  synthetic-routing-demo
```

The example requires `examples/tiny_agent_experiment.py` in the selected project. The skill template alone does not include that repository example. Replace the command and explicit input files for a real study. The example uses `python3` from PATH; select the correct interpreter before freezing. Tests use `sys.executable` so that the interpreter is unambiguous in each temporary test environment. An absolute interpreter path can be less portable when the project is moved.

`plan` validates and writes a new `plan.json`. It never replaces an existing experiment directory. A plan can be edited manually before its first freeze. After freeze, any byte change, including formatting, makes subsequent execution and validation fail. Preserve the old experiment and create a new experiment ID when revising a frozen design. Carry forward the reason for that revision and any already observed results.

`run --seed N` accepts only a seed in the frozen plan. It replaces the literal `{seed}` substring in argv elements; no other interpolation or variable expansion occurs. The command executes with `shell=False` and no inherited stdin. Raw stdout and stderr go to separate files; neither is automatically interpreted as a measurement. No generated draft, inferred score, or model prediction is represented as an observed result.

## Plan schema, version 1

The JSON root is an object. Unknown fields and duplicate JSON keys are rejected. JSON NaN, Infinity, and values such as `1e999` are rejected. Required fields are:

| Field | Format and purpose |
|---|---|
| `schema_version` | Integer `1`. |
| `experiment_id` | 1–64 ASCII letters, digits, `_`, or `-`; begins with a letter or digit. No path separators. |
| `title` | Nonempty study title. Include `SYNTHETIC` for fixtures. |
| `hypothesis` | Nonempty, specific hypothesis text. The script cannot determine whether it is actually falsifiable. |
| `rival_explanation` | A plausible alternative reason for the expected observation. |
| `primary_metric` | Object with `name`, `direction` (`maximize` or `minimize`), and `unit`. Metric names begin with an ASCII letter and contain letters, digits, `_`, `.`, or `-`, up to 80 characters. |
| `experimental_unit` | What constitutes one unit of analysis; state nesting/dependence where relevant. |
| `data_split` | Object with nonempty `development`, `evaluation`, and `leakage_controls` descriptions. |
| `controls` | Nonempty list of control-condition descriptions. |
| `baselines` | Nonempty list of comparison methods. |
| `seeds` | Nonempty list of unique, nonnegative integers. |
| `budget` | Object with positive integer `max_runs`, positive finite `max_run_seconds`, and positive finite `max_total_seconds`. Per-run timeout may not exceed the total. |
| `decision_thresholds` | Object with nonempty `success`, `failure`, and `inconclusive` text. Describe substantive thresholds, uncertainty, and what would change your mind; they are recorded without automatic evaluation. |
| `command` | Object with nonempty string list `argv`, relative project `cwd`, and `input_files`, a list of explicit relative files to hash. The list may be empty if no file inputs exist. |
| `synthetic` | Explicit boolean. `true` means fixture/simulation data; never present it as real study evidence. |
| `notes` | Optional nonempty text. |

No automatic default is supplied for the hypothesis, rival, split, controls, baselines, decision criteria, or budget. Passing schema validation shows that declared fields have accepted shapes. It does not show that the command is installed or executable, that controls are sufficient, or that the design supports causal interpretation.

Keep API credentials out of argv, plan notes, and logs. Environment variables are inherited by the authorized command but are not dumped into the record by this helper.

## Freeze and study mode

`freeze` writes `freeze.json` and its checksum using exclusive creation. It records the exact plan SHA-256, a UTC timestamp, the synthetic label, and one of two explicitly selected modes:

- **`prospective`**: the operator declares that the relevant hypothesis, comparison, and criteria were fixed before observing the relevant outcomes.
- **`exploratory`**: the plan follows some exploration or outcome observation. Exploratory work can inform a later independently evaluated study.

These are operator declarations. A local timestamp does not establish that no earlier experiments occurred, prove a dataset remained unseen, or replace an independently maintained preregistration service. Predictions and proposed thresholds belong in the plan; they are not results. A tool cannot make a study prospective merely by setting this flag.

## Budgets and authorization

`--authorized-local` is an operator attestation that the exact command, directory, resources, and effects already fall within user authorization. It is not a permission grant, an allowlist, a sandbox, or a security review. `shell=False` prevents implicit shell parsing; an explicitly chosen executable can still do anything permitted by the operating system. Do not treat structured argv as a reason to run unfamiliar code without review.

Local execution is constrained by the frozen budget:

1. Every admitted local attempt reserves one run slot and its full timeout before execution starts.
2. A smaller `--timeout-seconds` can be supplied. A larger one than `max_run_seconds` is cancelled without executing the command.
3. Reserved time is conservative: unused time is not refunded. Failures, launch failures, timeouts, and incomplete attempts retain their reservation.
4. A budget rejection creates an immutable `cancelled` run record explaining the reason. It reserves no additional execution time.
5. A project-wide lock created with exclusive file creation serializes CLI operations, including budget checks and reservations, so two cooperating CLI processes cannot simultaneously spend the same remaining allowance.

The timeout bounds the direct child process's allowed wall-clock execution. File hashing, git metadata reads, process launch/termination, and record I/O add overhead; this is not a hard whole-program real-time deadline or a billing meter. No cloud-spend accounting is implemented. On POSIX the child runs in a new process group, which is killed on timeout or after its direct child exits, including any remaining group workers. On other platforms only the direct child's termination is provided. A child that escapes the group, hostile code, or a hostile concurrent filesystem writer requires operating-system isolation beyond this helper.

If the helper itself is terminated, an `attempt.json` may remain without a final `record.json`. Validation reports it as incomplete. Its reserved budget remains spent; the next run does not erase or reuse it. A process killed before it releases `execution.lock` can leave a stale lock. Inspect the lock, its process, and partial attempt before manually removing that lock; there is no automatic stale-lock deletion or silent repair.

The CLI exits `0` for a completed recording/validation operation or an exit-0 local command, `2` for an input/path/integrity/lock error, `3` for a recorded budget cancellation, and `4` for a preserved local execution failure, timeout, interruption, or launch failure. A successful import means the source was recorded; inspect `external_status` to see its reported execution outcome.

## Files and provenance

All generated project contents are under:

```text
research-atlas/experiments/<experiment_id>/
  plan.json
  freeze.json
  freeze.json.sha256
  runs/<run_id>/
    attempt.json
    attempt.json.sha256
    stdout.txt                 (local attempts that reached launch preparation)
    stderr.txt                 (local attempts that reached launch preparation)
    imported-result.json       (imports only)
    record.json                (absent if the helper was interrupted before finalization)
    record.json.sha256
```

The shared lock is `research-atlas/experiments/execution.lock`. Run IDs use the same safe identifier rules as experiment IDs and cannot be reused by the helper. Existing frozen records, logs, failed runs, and imported source files are never overwritten or automatically deleted.

Local records include argv after seed substitution, project-relative cwd, timeout, seed, exit status, elapsed time, the frozen plan hash, and log hashes. `command.input_files` are individually hashed immediately before execution. No whole-project or dataset scan is performed. List code, data manifests, split files, and evaluation configuration deliberately. The hashes describe those declared files at that time; files are not snapshotted, and undeclared files, dependencies, live APIs, database contents, and changes occurring during execution are not covered.

When git is available, records include HEAD, whether tracked files are dirty, and a hash of tracked-file status. This does not snapshot a dirty working tree or cover undeclared untracked files. No remote git operation occurs. Changing the current source after a run does not invalidate historical log integrity; reproduce using the corresponding source version and declared-input hashes.

Project-relative cwd and input paths reject absolute paths, traversal, and symlink components. Every accessed record path is checked, with no-follow/exclusive file opens where supported. The selected root itself must not contain symlink components. These checks prevent ordinary path escapes; they are not a complete defense against an adversarial process racing directory changes.

## Import an externally measured result

Use imports for an actual external run, including failed or inconclusive runs. Identify where the bytes came from with `--origin`; keep source provenance detailed enough for another researcher to locate the original run. The tool checks syntax, hashes, and declared labels, not whether a measurement was honestly obtained.

Required external JSON shape:

```json
{
  "schema_version": 1,
  "synthetic": true,
  "status": "succeeded",
  "metrics": {"accuracy": 1.0},
  "elapsed_seconds": 0.0,
  "notes": "SYNTHETIC example format only; not a real scientific result."
}
```

Metric values must be finite numbers; signed values are allowed for differences or other signed measurements. A `succeeded` result must contain the frozen primary metric. The other allowed statuses are `failed`, `timed_out`, `cancelled`, `interrupted`, and `launch_failed`; those may contain an empty metrics object. The explicit `synthetic` boolean must match the plan. Imported bytes are copied exactly and hashed. Original source path and operator-supplied origin remain in the record. The helper cannot retroactively enforce execution budgets for external work, and imports do not consume local execution reservations.

The repository's synthetic example prints this format. To preserve that synthetic stdout as a separate imported record:

```bash
python3 skills/agent-research-atlas/scripts/experiments.py --root . import-result \
  synthetic-routing-demo --run-id imported-seed-7 \
  --file research-atlas/experiments/synthetic-routing-demo/runs/seed-7/stdout.txt \
  --origin 'SYNTHETIC local fixture stdout from seed-7; no external benchmark'
```

This creates another view of the same observation, not an independent replication. Do not count the local record and its import twice in an analysis.

## What validate-record establishes

It rechecks the plan schema and frozen hash, record checksums, attempt identity and linkage, preserved artifact hashes, imported metrics/status and source hash, and incomplete attempts. It neither reparses local stdout into experimental measurements nor evaluates decision thresholds. Errors are reported without rewriting evidence.

The records are ordinary local files, not a trusted append-only database. An owner able to edit both a record and its checksum, remove whole run directories, or rewrite all local history can defeat these checks. Independent storage, signed attestations, repository protections, execution isolation, an independent evaluator, and a review of leakage and implementation fidelity are separate capabilities. Do not advertise this helper as cryptographic proof of provenance, comprehensive tamper resistance, or scientific verification.

Before making a scientific claim, review the mechanism, strongest prior work, matched baselines, data independence, hidden confounders, implementation, appropriate uncertainty analysis, and all retained failure evidence. Use these records as auditable inputs to that review.

## Verification performed in this repository

`tests/test_experiments.py` runs only the hand-authored synthetic fixture in temporary local projects. It checks successful capture, nonzero failures, partial output on timeout, existing authorization attestation, freeze/run immutability, plan and artifact tampering, conservative budgets, cancellation records, concurrent lock exclusion, source-preserving imports, failed external imports, invalid numeric JSON, path traversal, symlink rejection, and retained incomplete attempts. These are software integrity tests; they are not evidence that a research hypothesis or scientific workflow is effective.

## v1.1 frozen inputs and controlled optimization

A new freeze records SHA-256 and byte length for every `command.input_files` entry. All listed files are immutable by default. Include the evaluator, metric implementation, ground truth/split manifest, prompts/configuration and other comparison-critical files explicitly; undeclared dependencies are outside this check. A changed immutable file before launch produces a retained `launch_failed` attempt and consumes the reserved local attempt budget. Fix the mismatch by creating a new experiment ID with an explained amendment, not by editing the freeze record.

Optimization can change an explicitly declared candidate implementation:

```json
{
  "argv": ["python", "train.py", "--seed", "{seed}"],
  "cwd": ".",
  "input_files": ["train.py", "evaluate.py", "split.json"],
  "mutable_input_files": ["train.py"]
}
```

`mutable_input_files` is optional, defaults to `[]`, and must be a unique subset of `input_files`. Keep evaluators, held-out labels, metric definitions and comparison budgets outside this mutable set. The runner checks the declared policy, not a file's scientific role. Review the method-to-code mapping before execution; a user can mislabel an evaluator as a candidate, which syntax alone cannot detect.

Each launched run records input hashes before and after execution. If an immutable input changes during a run that exited 0, the record preserves `exit_code: 0`, reports `status: failed` and names `immutable_inputs_changed_during_run`. Failure, timeout and launch errors remain visible. A hash before/after check cannot detect a temporary edit that was restored between observations, undeclared files, an altered runtime/environment or external services. Use a real isolated evaluator and the project's container/CI controls when the comparison requires stronger protection.

Old v1.0 freezes remain readable and are explicitly reported as `legacy_unpinned`. Historical validation checks recorded artifacts rather than requiring today's source files to match an old run. Do not re-label old runs as having the new freeze-time guarantee. New confirmatory comparisons should use a new experiment ID and an explicit current freeze.

## Numeric statements need a separate audit

`validate-record` verifies recorded bytes and identities. Before putting measurements into a result-to-claim table, use `audit.py values` with the numerical ledger in [evidence-and-claims.md](evidence-and-claims.md). It distinguishes a number mismatch, missing file, missing JSON locator, unparseable source, non-numeric value and changed source version. A matching number does not establish that the evaluator measures the intended construct or that a causal claim follows.
