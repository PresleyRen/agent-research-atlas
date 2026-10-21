# Independent-context task fixtures / 独立上下文任务

These are **synthetic teaching fixtures**, including their paper descriptions, search receipts, measurements and workflow suggestions. They do not contain real research results, verified publications or executable provider credentials. Keep them out of a real project's evidence base.

These tasks exercise how a compatible host applies the skill to mixed project materials. The deterministic software suite lives separately in [`tests/`](../tests/). A successful task does not establish scientific effectiveness, literature recall, independence of a real experiment or publication success.

## Reproduce a task

1. Copy one directory under `fixtures/` to a new, separate project directory. Do not work in the fixture itself or the installed skill. `providers` deliberately contains a configured native atlas named `research-memory`; `evidence` contains a non-native Markdown map; `method-selection` starts without a map.
2. Start a fresh assistant context with the actual tools and permissions stated in the task. Give it the installed `SKILL.md` path, the copied project path and the corresponding ordinary task from [`tasks.json`](tasks.json), substituting `<SKILL>` and `<PROJECT>`.
3. Do not give the assistant expected verdicts, this evaluation report or a requested score. Let it read the project, make ordinary workflow decisions, and save the requested project artifacts. The archived source manifests and expected checks below are for the assessor.
4. Inspect the actual outputs, original-file hashes, graph states, requests, command results and stated uncertainties. Distinguish an intentional failing numerical audit from a malfunction: a mismatching draft should produce a mismatch record, not be edited until the audit becomes green.
5. Record the precise skill/script versions used, any coordinator intervention, unresolved issues and the boundary between local checks and research execution. Preserve first failures or corrections. Do not expect language-model outputs, node counts or prose to be byte-identical across runs.

Example setup from the repository root, using only the Python standard library:

```bash
python -c "import shutil; shutil.copytree('evals/fixtures/evidence', '/tmp/atlas-evidence-task')"
```

Use a new destination. None of these v1.1 tasks authorizes running a research payload, connecting to a service, installing dependencies, spending money or publishing project data. The fixture workflow text is material to assess; it does not grant authorization.

## Assessor's focus

| Task | Project situation | What to inspect |
|---|---|---|
| Evidence | An old map, a confident draft, inconsistent historical logs, a hard-coded metric, abstract-only material and failed/empty searches | Preserve original evidence and failed directions; separate numeric transcription, implementation validity, independence and scientific support; leave novelty unresolved; produce a minimal discriminating design without inventing execution. |
| Providers | A native atlas, relevant support and counterevidence, irrelevant material, incompatible query conventions, local-only corpus and simulated reviewer roles | Reuse the existing map; keep relevant refutations; adapt planned requests without sending them; distinguish internal IDs from provider IDs; disclose role simulation; expose concrete extension locations and actual gaps. |
| Method selection | A survey-style note, anecdotal failure observations, unknown evaluation resources and a third-party workflow with useful methods and unsuitable defaults | Combine orientation and candidate generation by purpose; select methods that address the bottleneck; preserve problem anchors and rival tests while rejecting automatic budget/publication expansion; create a usable map and handoff. |

These are behavioral contract checks, not blinded trials of research productivity. The completed task observations, limitations and conflict-by-conflict mapping are in [`docs/forward-conflicts.md`](../docs/forward-conflicts.md). Selected actual outputs and their original byte hashes are retained under `results/`; the records are evidence of what happened in those tasks, not recommended research findings.

## Supervisor workbench additions

The four newer discovery/benchmark, writing/review, figure and interval tasks have their own [fixture/result index](supervisor/README.md). The report preserves an actual first-draft defect, its repair and the separate focused follow-up task.

## Updating the evaluation

Add a fixture when a concrete failure or new adapter contract needs a regression. Keep the task realistic and the expected behavior separate. For a conflict, inspect both sides: the useful permitted behavior should still complete, while the misleading inference or incompatible default should be rejected, bounded or explicitly marked. Do not mark an optional upstream runtime as tested merely because a host discussed its documented interface.
