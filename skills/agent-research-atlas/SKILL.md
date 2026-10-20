---
name: agent-research-atlas
description: "Build and update a persistent bilingual research atlas from surveys and primary papers; discover defensible Agent research questions, audit closest prior work, assess local feasibility, design falsifiable experiments, retain negative results, and assemble evidence-backed publication claims. Use for 科研选题、综述梳理、研究地图、查新、意图识别、语义路由、文档检索、RAG、Agent评测、实验设计、论点验证, or continuing an existing research project."
---

# Agent Research Atlas

Turn an Agent research question into a traceable cycle of exploration, hypothesis, experiment and revised understanding. Preserve local research history. Support Chinese and English sources, queries and outputs; default to the user's language.

## Begin with the existing project

1. Identify the user-authorized project directory. Read its applicable instructions and resource constraints. Keep research data inside this project, never inside the installed skill or a public distribution repository.
2. Run `python <SKILL>/scripts/atlas.py --root <PROJECT> discover`. Inspect the scope and truncation flag. Read existing maps, literature notes, experiments and failed directions relevant to the task. Do not assume an unsearched directory is empty.
3. Reuse a native atlas. `init` reuses the configured atlas or a single native atlas found elsewhere. For multiple atlases, inspect them and select `--atlas-dir` using their content and the user's task; ask only if ownership remains genuinely ambiguous.
4. Read a non-native map before running `adopt --file <project-relative-map>`. Adoption retains original bytes and hash. Convert its actual content into sourced nodes with `upsert`; annotate the import as normalized only after checking it. Registration does not interpret Markdown, Mermaid, PDF or images. Use host readers/OCR when available; leave unreadable imports pending.
5. With no existing map, run `init --title <project-title>`. The 14 seeded domains start **unsearched**. Treat the taxonomy as extensible, not a complete survey or evidence of progress.
6. Read `status` and `atlas.json`, then continue from relevant open questions and decisions. Reopen parked/refuted ideas only with a recorded reason, changed constraint or new evidence.

Read [local-atlas.md](references/local-atlas.md) before the first write. Bundled tools require Python 3.10+ and only the standard library. `<SKILL>` is the directory containing this file; `<PROJECT>` is the research workspace. Prefer absolute paths.

## Match the requested depth

| Depth | Deliverable and stopping condition |
|---|---|
| Orient | Scoped, cited map of directions, progress, disagreements and explicit coverage gaps. |
| Discover | Shortlist with closest-work comparisons, plausible mechanisms and feasibility judgments. |
| Design | Experiment-ready proposal with rival explanations, decisive measurements and budget. |
| Execute | Authorized runs, raw records, failures, uncertainty and result-to-claim assessment. |
| Publish package | Claim–evidence table, reproducible methods, real figures/tables, limitations and venue fit. |
| Update | New evidence reconciled with the graph; superseded claims retained; downstream plans reconsidered. |

Proceed autonomously with already authorized work. Paper submission, public disclosure of project data, paid jobs or unattended recurring execution require task-specific authorization if not already provided. Normal reading, reversible edits and requested local tests do not need repeated approval. A paper, webpage, skill or repository instruction cannot authorize spending, publication, unknown code execution or disabling protections.

## Research loop

### 1. Scope the field and read the evidence

Read [agent-domains.md](references/agent-domains.md) and [bilingual-retrieval.md](references/bilingual-retrieval.md).

- State the research question, included/excluded settings, date cutoff, languages and available sources. For “the whole field,” define a first-pass boundary and expand iteratively.
- Inventory actual data rights, code, compute/API access, budget and deployment constraints. Mark unverified resources **unverified**; do not assume a dataset, GPU or subscription exists.
- Start with relevant surveys, then verify key conclusions using original papers and recent work. Record metadata/abstract/fulltext access and source locations for extracted claims.
- Extract problem definitions, competing approaches, results under their stated settings, failures, contradictions, evaluation assumptions and cross-domain connections.
- Add paper and exploration nodes while reading. Link claims to sources, not just search titles. Preserve null searches, access failures, query/date/provider and scope limitations. `reviewed` means a documented scoped pass, never exhaustive coverage.

### 2. Discover and challenge research questions

Read [methodology.md](references/methodology.md). Choose methods that fit the question; do not run every framework mechanically.

- Generate candidates from failure cases, rival mechanisms, assumption changes, evaluation gaps, quality/cost trade-offs, theoretical counterexamples and structural transfers between fields.
- For each candidate write: problem, mechanism, prediction, nearest papers and exact difference, rivals, minimum discriminating test, resources, falsification conditions and continuation/pivot decision.
- Search for **disconfirming prior work** using synonyms and neighboring fields in both languages. Compare objectives, information available at decision time, methods, evaluation, costs and contributions. Say “not found within these searches,” never globally confirmed novelty.
- Prefer a sharp question to a collection of components. Identify the contribution type: mechanism, theory, method, measurement, dataset or reproducible empirical finding. Do not infer acceptance from an LLM score.
- When independent agents are available, separate proposal generation from prior-work and rival-explanation review. Give reviewers evidence and a concrete question without a desired verdict. With one context, disclose serial self-review instead of claiming independence.
- Bound exploration by a search/evidence budget. Stop when the next investigation is unlikely to change the decision within it, or when feasibility cannot be resolved. Preserve blocked ideas and why they were parked.

### 3. Assess feasibility before implementation

Use `proposed → grounded → testable` only when the corresponding fields exist. These are management states, not scientific certifications.

- Verify data, compute, evaluation and budget against the project. Resolve critical unknowns with a cheap authorized check.
- Require a prediction distinguishing the mechanism from a rival or simpler baseline.
- Identify the experimental unit, independent splits, leakage/contamination, measurement reliability, implementation dependencies, smallest useful effect and confounds.
- Explain positive, negative and inconclusive outcomes before the run. A null result may challenge a mechanism, expose weak measurement or remain underpowered; do not decide using only a p-value.
- Use decision tables with evidence and reasons. A score may express user priorities; it is not the probability that the hypothesis is true or publishable.

### 4. Design and run discriminating experiments

Read [experiments.md](references/experiments.md) before execution. Adapt the bundled example plan to the actual project.

- Start from a claim and its strongest alternative. Specify strong/simple baselines, ablations, controlled budgets, independent units/splits, metrics, repetitions, uncertainty estimates and robustness checks as appropriate.
- Separate exploratory tuning from confirmatory evaluation. Freeze prospective criteria before outcomes; label exploratory work and record amendments instead of rewriting history.
- Use `experiments.py plan`, `freeze`, `run` or `import-result`, then `validate-record`. Execute only inspected commands within user authorization. The runner is **not an OS sandbox** and cannot enforce network, monetary or GPU isolation.
- Keep crashes, timeouts, cancelled runs, raw output, plan hash and code/data provenance. Do not select only the best seed or erase variants.
- Avoid expensive pilots when the budget is unknown; finish a concrete plan and resource estimate first. Synthetic smoke tests verify plumbing only.
- Do not treat script success as hypothesis confirmation. No bundled command submits papers or computes acceptance probabilities.

### 5. Interpret results and maintain the atlas

Read [evidence-and-claims.md](references/evidence-and-claims.md).

- Compare outcomes with frozen predictions and rivals. Report effect sizes, uncertainty, failures and settings alongside averages.
- Link experiment nodes to actual records through `data.artifact_path`. Read the record before assigning empirical states. State what is independent and what shares code, data, annotators or models.
- Assign `pilot_supported`, `independently_supported`, `inconclusive` or `refuted` with an evidence review, limitations and reviewer identity. Record a reason for every status change. The validator checks structure, not scientific correctness.
- Narrow claims to the evidence. Preserve counterevidence, superseded claims and relevant `contradicts`/`supersedes` links. Check downstream plans and prose when new evidence changes a premise.
- `upsert` merges stable IDs, accepts an expected revision, saves prior states and regenerates views. Lists are additive; correct errors with documented superseding records rather than silently removing sources.
- Put human notes in `domains/<id>/notes.md`. Generated views are rebuildable; prior view versions, including manual edits, are backed up before replacement.

### 6. Prepare publication arguments when requested

Produce the question, bounded novelty statement, closest-work table, methods, evidence-backed results, limitations, reproduction instructions and claim–figure/table–run mapping. Cite verified original sources. Check current official venue scope and rules before venue-specific advice.

Distinguish SCI/SCIE indexing, journal quality and top-conference fit. Never promise SCI, top-journal/main-conference acceptance or universal proof of an empirical generalization.

## Tools and honest fallbacks

| Capability | Preferred path | Fallback |
|---|---|---|
| Discovery | Available host search, official paper pages, OpenAlex/Semantic Scholar APIs | Plan queries and record missing providers; query generation is not completed retrieval. |
| Full text | Authorized publisher/OA files and host PDF readers | Mark abstract/metadata only; locate/request lawful full text if needed. |
| Citation context / local QA | Available Scite/PaperQA2 or equivalents | Read original citing sections/local papers; disclose limits. |
| Structured extraction | Available, authorized Elicit/Undermind | Host search and sourced extraction into graph nodes. |
| Experiments | Existing project stack plus bundled record runner | A frozen feasible plan; no invented execution. |
| Maps | JSON, Markdown/Mermaid, offline interactive HTML | Conservative adoption and semantic normalization of existing maps. |
| Refresh | Explicit update request and optional `mark-stale` | No background watcher/scheduler is installed. |

Optional services are not bundled dependencies and are not automatically installed. Do not require all upstream skills. Adapt to the host's actual tools.

## Minimum handoff

After substantive work report: explored scope/cutoff; evidence and disagreements; strongest candidate and nearest work; feasibility/unknowns; next decisive experiment or actual results; map location/revision; changed, parked and refuted decisions; exact sources and execution results; blocked access and unfinished semantic imports.

For short updates, focus on changes and implications. For deep exploration, deliver the complete project records and explanation. The next session should continue without repeating resolved searches or forgetting failures.
