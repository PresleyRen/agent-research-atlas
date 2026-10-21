# Supervisor workbench tasks / 工作台任务夹具

These are **synthetic local project materials**. Their papers, measurements and scenarios are not real research findings. Keep them separate from a real project's scientific evidence.

## Reuse

Copy one directory under `fixtures/` to a fresh project directory, start a new assistant context, and supply the skill/project paths with its ordinary task in [tasks.json](tasks.json). The task text is a reusable normalization of the original requests, not a byte-for-byte transcript of tool transport. Do not supply this assessor index, archived results or expected conclusions to the task assistant. The original three trials disclosed their offline synthetic nature; no claim of full blinding is made.

Let the assistant complete the requested work using the supplied local materials. Preserve original inputs and record the files, versions, commands, actual outputs and any coordinator repair request. Language-model prose and graph node counts need not reproduce byte-for-byte. The fourth task is intentionally narrow; building a whole research map is not required.

| Task | Inputs | Actual archived deliverables |
|---|---|---|
| Discovery / benchmark | [Fixture](fixtures/discovery/PROJECT.md): existing map, local review/counterexample, comparison, research choices and resources | [Handoff](results/discovery/HANDOFF.md), [research design](results/discovery/RESEARCH-DESIGN.md), [benchmark dossier](results/discovery/design/benchmark-dossier.md), [map](results/discovery/research-atlas/MAP.md), [retained repair record](results/discovery/worklog/coordinator-protocol-review.md) |
| Manuscript / polish / replies | [Fixture](fixtures/writing/PROJECT.md): draft, method note, pilot record and review concerns | [Handoff](results/writing/HANDOFF.md), [English sections](results/writing/manuscript/sections-en.md), [polish](results/writing/manuscript/polished-sentences-en.md), [full responses](results/writing/review/response-en.md), [concern ledger](results/writing/review/concern-ledger.md) |
| Figures / reconstruction | [Fixture](fixtures/figures/PROJECT.md): reference image, measured-value fixture and figure context | [Handoff](results/figures/HANDOFF.md), [editable source](results/figures/outputs/fig01_architecture.drawio), [architecture preview](results/figures/outputs/fig01_architecture.png), [plot preview](results/figures/outputs/fig02_latency_accuracy.png), [editing scope](results/figures/EDITING.md), [validation](results/figures/VALIDATION.md) |
| Interval interpretation | [Fixture](fixtures/intervals/PROJECT.md): five hypothetical intervals and an old rule | [Handoff](results/intervals/HANDOFF.md), [decision table](results/intervals/DECISION-TABLE.md), [revised rule](results/intervals/REVISED-RULE.md), [exact checks](results/intervals/CHECKS.json) |

Every fixture has an `INPUT-MANIFEST.json`. Each result snapshot has a `SNAPSHOT-MANIFEST.json` covering its exact files, excluding itself, Python bytecode and regenerable font caches. Absolute source-run paths in historical handoffs/logs are retained as provenance; use this relative index after checkout. The coordinator verified all four original input manifests/content files and all 254 archived files.

Files under `research-atlas/history/views/` are byte-preserved historical view caches. Their original relative links target the original map directory and do not form standalone navigable pages at the cache location. Use each project's current `research-atlas/MAP.md` or `map.html` for navigation; the historical bytes are retained for revision comparison.

## Assess the outputs

The detailed observations, initial interval defect, repaired rules, source-skill mapping and conflict coverage are in [supervisor-validation.md](../../docs/supervisor-validation.md). The separate [output review](../../docs/supervisor/output-review.md) records its read-only assessment of the first three projects.

Inspect completed deliverables as well as boundaries: a manuscript task should deliver actual prose; a reply task should cover each concern; a figure task should produce usable files. At the same time, a synthetic score cannot become a real claim, a plan cannot become an executed experiment, and native XML structure does not prove native-editor rendering. The interval task checks interpretation of given endpoints, not statistical estimation or scientific effectiveness.

The actual task runs authorized local reading, writing and checking only. They did not authorize external service calls, installation, model workloads, paid computation or publication. These task restrictions do not redefine the host's authorization for a different user project.
