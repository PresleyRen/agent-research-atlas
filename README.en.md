# Agent Research Atlas

**Keep literature exploration, research questions, testable hypotheses, experiments, and manuscript claims in one persistent research map.**

[中文](README.md) · [Full skill](skills/agent-research-atlas/SKILL.md) · [Sources and attribution](SOURCES.md) · [Validation record](docs/validation.md)

Agent Research Atlas is a bilingual Chinese/English skill for Agent research. It guides an AI assistant through surveys and primary papers, a map of the field, closest-work comparisons, feasibility checks, discriminating experiments, negative results, and evidence-backed publication arguments.

Two bundled Python tools provide the local records: `atlas.py` manages the research graph, and `experiments.py` manages plans, freezes, budgets, and execution records. Both use only the Python standard library. Research state stays in a separate project directory so that later sessions can continue from previous evidence and decisions.

**The aim is to find important, feasible questions and test them carefully.** Novelty, scientific validity, and publication still require actual literature, appropriate experiments, and expert judgment. The skill does not promise SCI/SCIE journal acceptance or acceptance at a leading journal or conference, and it does not turn model-generated idea scores into acceptance probabilities.

## What it does

| Capability | Work and deliverables |
|---|---|
| Survey the field | Map problem definitions, method families, progress, disagreements, unresolved conditions, and evidence locations; verify important survey claims against primary papers. |
| Search in two languages | Use Chinese and English terminology, adjacent fields, and separate searches for surveys, closest work, counterevidence, datasets, and evaluation. Record actual queries, dates, providers, results, and access failures. |
| Check closest prior work | Compare objectives, information available at decision time, mechanisms, evaluation settings, costs, and contribution boundaries. Expand through references and later citations. |
| Discover research questions | Generate candidates from failures, contradictions, changed assumptions, measurement gaps, transferable mechanisms, and quality/cost trade-offs. A new component combination is not automatically a contribution. |
| Assess feasibility | Check actual data access, code, compute, evaluators, and budget. Preserve unknowns and choose inexpensive checks that could change the decision. |
| Choose a method | Match the question to theory, counterexamples, error analysis, comparative experiments, ablations, causal or counterfactual checks, robustness tests, statistical estimation, or measurement research. |
| Design experiments | Specify rivals, strong and simple baselines, experimental units, splits, metrics, controls, repetitions, budgets, and positive, negative, and inconclusive outcomes. |
| Run or import experiments | Execute inspected local argv commands within existing authorization, or import external results. Retain raw logs, exit codes, timeouts, failures, and cancellations. |
| Freeze plans and record provenance | Save a plan hash, timestamp, and prospective/exploratory declaration; hash explicitly listed code/data inputs and detect changes to frozen plans. |
| Connect results to claims | Link interpretations to real paper or experiment records; distinguish support, partial support, counterevidence, inconclusive results, and unresolved mechanisms. |
| Maintain a local map | Keep JSON as the source of truth and generate Markdown overviews, per-domain Mermaid views, and a filterable offline HTML graph. |
| Continue an existing project | Reuse a native atlas, or preserve a different map's original bytes and hash before the assistant reads and normalizes its content. |
| Preserve research history | Use stable IDs, revisions, conflict checks, history snapshots, and protected human notes. Retain parked ideas, refutations, failed directions, and reopening conditions. |
| Prepare publication arguments | Assemble closest-work tables, bounded contributions, protocols, real result figures/tables, claim–evidence mappings, limitations, and reproduction instructions. |
| Request independent review | Separate proposal generation from prior-work and rival-explanation review when the host provides independent agents; disclose serial self-review otherwise. |

The host assistant performs the research using the evidence it actually reads. The scripts check record structure, references, paths, and local integrity. They do not judge whether a paper is correct, a mechanism is established, or an experiment merits publication.

## Fourteen extensible seed domains

Initialization creates these **14 seed domains**, all with coverage `unsearched`. It does not invent papers, completed reviews, or progress.

| Domain ID | Research scope |
|---|---|
| `intent` | Intent understanding, multiple intents, out-of-distribution intents, open sets, and annotation ambiguity. |
| `clarification` | Clarifying questions, active information gathering, abstention, and human collaboration. |
| `routing` | Task, model, tool, and retrieval routing; calibration, uncertainty, and budgets. |
| `planning` | Task decomposition, planning, constraints, search, reflection, and replanning. |
| `ingestion-retrieval` | Document ingestion, chunking, indexing, retrieval, freshness, and access conditions. |
| `reranking-context` | Reranking, evidence selection, context compression, and long-context interference. |
| `knowledge-graphs` | Knowledge graphs, structured retrieval, GraphRAG, entities, and relations. |
| `memory` | Short- and long-term memory, updates, forgetting, versioning, and consistency across sessions. |
| `tool-use` | Tool selection and invocation, state, failure recovery, and execution feedback. |
| `answer-grounding` | Answer generation, attribution, citations, faithfulness, and uncertainty. |
| `multi-agent` | Collaboration, communication, division of work, debate, and multi-agent evaluation. |
| `evaluation` | Task success, data and evaluators, contamination, reproducibility, and out-of-distribution tests. |
| `production` | Latency, cost, reliability, observability, and feedback from deployment. |
| `safety-security` | Prompt injection, permissions, privacy, tool safety, and reliable execution. |

The skill extends beyond document RAG. Add domains for embodied agents, multimodality, reinforcement learning, formal methods, or another research area when relevant. The [domain reference](skills/agent-research-atlas/references/agent-domains.md) offers additional analytical views; these are not extra domains automatically initialized by the tool. The taxonomy organizes work and does not certify coverage of the Agent field.

## Install or load the skill

Clone the repository:

```bash
git clone https://github.com/PresleyRen/agent-research-atlas.git
cd agent-research-atlas
```

The installable skill directory is **`skills/agent-research-atlas`**, not the repository root. Load that directory using the official local-skill installation procedure for your host, such as Codex or Claude Code. Use its documented user or project skill location, compare any existing version before replacing it, and retain the adjacent `references`, `assets`, and `scripts` directories.

Managed chat environments may restrict persistent installation. Publishing this repository does not install it into every session. A host with local file access can also read the skill directly:

> Read `/absolute/path/agent-research-atlas/skills/agent-research-atlas/SKILL.md` and use it for my research project at `/absolute/path/agent-project`.

### Host capabilities and dependencies

| Capability | Requirement |
|---|---|
| Research reasoning | An AI host that can follow the skill and inspect the relevant evidence. No model or model API account is bundled. |
| Literature discovery | Actual host search, browsing, or authorized scholarly APIs. The bundled query planner does not execute searches. |
| Reading sources | Host webpage/PDF/file readers as needed. Record metadata-only or abstract-only access when full text is unavailable. |
| Persistent state | Read/write access to the user-authorized research project. A text-only chat cannot claim local file changes. |
| Local tools | Python **3.10+**. The two helpers need no `pip` packages; the experiment command you choose may have its own dependencies. |
| Independent review | Optional separate agents or reviewers. One context reviewing its own proposal is self-review. |
| Periodic updates | A separately available and authorized scheduling capability. This repository installs no background watcher or scheduler. |

Keep unpublished papers, private data, and project state in the separate research project, outside this public tool repository and the installed skill directory.

## Example research requests

### Explore a field

> Use $agent-research-atlas for Agent intent understanding, routing, document retrieval, and answer generation. First inspect my existing maps and experiments. Search Chinese and English surveys and primary papers, then map progress, disagreements, and unresolved problems. Select three candidates with explicit mechanisms, closest-work comparisons, and feasible local requirements. Propose the smallest experiments that distinguish their mechanisms from rival explanations, and save the map and sources.

### Continue an existing project

> Continue this project. Read the existing atlas, failed directions, and resource constraints first. Add relevant recent papers, check which hypotheses or plans need revision, and explain what the new evidence changes.

### Investigate a specific mechanism

> Could calibration of uncertainty before retrieval improve an Agent's routing? Find the closest methods and counterevidence first. Then assess whether my data can distinguish improved decisions from the alternative explanation that the system simply calls a stronger model more often.

### Move into experiments

> For this hypothesis, inspect the available resources and experiment code, design and freeze a comparison protocol, run within my authorized local budget, preserve failures and results, and update the claims and next decision.

The requested depth can stop at orientation, a shortlist, a feasible design, executed experiments, publication arguments, or an incremental update. The skill should not imply that later stages happened when the task or available tools only support an earlier stage.

## Atlas CLI

The commands below assume the repository root is your current working directory and `/path/to/agent-project` already exists. Use absolute script paths when running from another directory. Global options such as `--root` and `--atlas-dir` precede the subcommand.

```bash
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project discover
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project init --title 'My Agent research'
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project status
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project check
```

Read existing non-native maps before registering them with `adopt --file docs/existing-map.md`. Registration preserves the source and leaves its semantic import pending; the assistant must still read it and convert its actual content into sourced records. A single existing native atlas is reused. If several exist, inspect them and select the intended one with `--atlas-dir`.

Incremental writes use `upsert --file batch.json --expected-revision N`, where `N` is the revision you read. Unknown fields are retained, nested objects merge, and lists append unique entries. Correct or supersede evidence explicitly instead of silently deleting history. See the [local atlas contract](skills/agent-research-atlas/references/local-atlas.md) for the batch schema, state requirements, and recovery guidance.

Generate a bilingual query plan without performing retrieval:

```bash
python skills/agent-research-atlas/scripts/atlas.py queries --domain routing --focus-zh '检索前不确定性' --focus-en 'pre-retrieval uncertainty' --since 2024
```

The output covers surveys, closest work, negative evidence, and evaluation in both languages, with `executed: false`. Supply both focus translations together. Custom graph domains are supported, while this built-in query planner uses the seed-domain IDs; the host can write queries for other domains.

### Files, views, and project-relative links

The default project layout is:

```text
agent-project/
  research-atlas.config.json
  research-atlas/
    atlas.json
    MAP.md
    map.html
    domains/<domain-id>/MAP.md
    domains/<domain-id>/notes.md
    papers/
    hypotheses/
    claims/
    explorations/
    imports/
    history/
    experiments/<experiment-id>/
      plan.json
      freeze.json
      runs/<run-id>/
```

`research-atlas.config.json` can point to a reused native atlas elsewhere **inside the project**. **Experiment storage remains fixed at `PROJECT/research-atlas/experiments`**, even when the native atlas is reused from a different directory. `experiment.data.artifact_path` is relative to the project root, so it can connect that atlas to a record elsewhere within the same project, for example `research-atlas/experiments/exp-routing/runs/seed-7/record.json`. Do not resolve artifact paths relative to the atlas directory. Local artifact paths must exist and may not escape the project through absolute paths, traversal, or symlink components.

Open `map.html` locally to filter by Chinese/English text, domain, type, or status and select nodes to inspect evidence and relationships. It requires no CDN or upload. The graph draws at most 140 matching nodes and displays a truncation notice; the full matching index remains available. Narrow the filters to inspect the remaining nodes.

Successful updates regenerate the views; refresh the page to see them. Store persistent human prose in `domains/<domain-id>/notes.md`. Generated views are rebuildable, and previous view contents are backed up before replacement. The HTML is a snapshot, not a live editor. Use explicit updates or `mark-stale` with a chosen review-age policy to identify material that needs revisiting.

### Evidence states

The eight record types are `domain`, `paper`, `problem`, `hypothesis`, `experiment`, `claim`, `decision`, and `exploration`.

Hypotheses progress from `proposed` to `grounded` and `testable` only with the corresponding closest-work, mechanism, prediction, rival, feasibility, minimum-test, and falsification fields. Empirical states require linked experiment artifacts and an evidence review; `independently_supported` also requires an explanation of independence and shared dependencies. Downgrading, parking, and reopening remain possible with a recorded reason.

Domains use coverage `unsearched`, `partial`, `reviewed`, or `stale`. A scoped `reviewed` pass needs a date, traceable exploration records, and coverage limitations. It does not mean an exhaustive search. Web sources record `metadata`, `abstract`, or `fulltext` access; local sources record a project-relative path, `local` access, and the location actually read.

These gates require explicit documentation. A validator cannot infer that the declared resources exist, the literature was read correctly, an experiment is independent, or a hypothesis is true. The [evidence and claims reference](skills/agent-research-atlas/references/evidence-and-claims.md) explains the review obligations.

## Experiment CLI

Write a project-specific plan using the [experiment protocol](skills/agent-research-atlas/references/experiments.md) and [example JSON](skills/agent-research-atlas/assets/experiment-plan.example.json). The example is a synthetic recording fixture; its command and explicit input files must be adapted or made available inside your selected project.

```bash
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project plan --file plan.json
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project freeze experiment-id --mode exploratory --rationale 'Initial exploration; no independent confirmation data yet.'
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project run experiment-id --run-id seed-7 --seed 7 --authorized-local
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project validate-record experiment-id
```

Replace `experiment-id` and the seed with values declared in your plan. `--file` is resolved from the invoking shell's working directory; `--root` sets the research project and the reference point for command working directories and input-file paths. The runner substitutes only the literal `{seed}` in argv elements.

Choose `prospective` only when the relevant criteria were fixed before observing the relevant outcomes; otherwise use `exploratory` and explain why. The mode is an operator declaration, and a local freeze timestamp cannot establish that no earlier outcomes were observed. Frozen plans are immutable to the helper: use a new experiment ID and record the amendment when revising a design.

Only execute inspected commands already covered by the user's authorization. `--authorized-local` attests to that existing authorization; it grants no permission. The runner uses structured argv and `shell=False`, records timeout and budget decisions, and reserves local run allowances conservatively. It is **not an operating-system sandbox** and cannot restrict a chosen program's network access, writes outside the project, or external service spending. Use suitable existing isolation when the task needs it.

Raw stdout and stderr, execution outcomes, frozen-plan hashes, and hashes of explicitly declared input files remain available. `succeeded` means the direct child exited with code 0. `scientific_verdict` remains `not_assessed`; stdout is not automatically interpreted as measurements or proof of a hypothesis. Independently inspect the implementation, evaluator, results, alternatives, and uncertainty.

Use `import-result` for actual results produced by a cluster or another experiment framework. It retains source bytes and provenance, including failed results. Importing a local result again does not create independent evidence, and external runs are not retroactively constrained by the helper's local budget. See the protocol for the accepted JSON shape, incomplete attempts, locks, and exit codes.

## Choose methods to fit the question

| Research situation | Useful methods | Main question |
|---|---|---|
| The literature is fragmented | Scoping review, comparison matrices, citation expansion | Which conclusions share a setting, and which are only superficially similar? |
| No clear research opportunity | Failure analysis, assumption audit, contradiction and trade-off analysis | Which unresolved condition matters and has a testable mechanism? |
| A proposal may only swap components | Closest-work comparison, simple baselines, mechanism ablations | What causes the difference, and what is the contribution beyond tuning? |
| Results appear promising | Paired comparisons, effect sizes and intervals, repetitions, matched budgets | Is the difference stable, and could confounding or evaluator bias explain it? |
| A mechanism is claimed | Competing predictions, interventions, counterfactuals, suitable causal design | Which observations rule out the strongest alternative? |
| Broad generality is claimed | Distribution shifts, stress tests, stratified failures | Under which tasks, datasets, models, or resource limits does it fail? |
| The contribution is theoretical | Precise definitions and assumptions, derivations, proof checks, counterexamples | Under what explicit conditions does the result hold? |
| The contribution is data or evaluation | Annotation agreement, measurement validity, contamination audits | What is measured, and does it reflect actual task success? |

The [methodology reference](skills/agent-research-atlas/references/methodology.md) connects these choices to concrete records and decision points. Domain expertise, statistical tools, formal proof tools, or physical experiments may still be required. The skill should identify missing capabilities rather than claim universal methodological competence.

## Retrieval sources and optional services

Use actual host search and official paper records, including arXiv, ACL Anthology, OpenReview, DBLP, OpenAlex, Semantic Scholar, and Crossref. Chinese-language coverage can use relevant journals, ChinaXiv, and CNKI/Wanfang when access is available. Search neighboring terminology from information retrieval, dialogue, decision-making, and planning where it changes coverage.

Undermind, Elicit, Scite, and PaperQA2 are optional additions. They are **not installed, authenticated, or integrated by this repository**, and users do not need subscriptions to every service. Respect source access conditions. A metadata match is not full-text reading, and proximity in a citation graph does not validate a mechanism. See [bilingual retrieval](skills/agent-research-atlas/references/bilingual-retrieval.md) and the inspected-source details in [SOURCES.md](SOURCES.md).

## Testing and limitations

Run the local test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests exercise atlas reuse, preservation of original files and notes, revision conflicts, record requirements, identity deduplication, path handling, HTML data escaping, frozen-plan integrity, budgets, result imports, and retained failures/timeouts. See the [validation record](docs/validation.md) for executed commands, actual results, independent-context workflow checks, and unresolved limits. This README does not substitute a predicted test outcome for that record.

The [retrieval smoke record](docs/retrieval-smoke.md) documents a limited real Chinese/English search, the original paper records that were opened, reading depth, and access failures. It is not an evaluation of field-wide recall. Experiment fixtures are explicitly **SYNTHETIC** and do not establish performance on real Agent models or private research data.

The software and workflow checks do not establish that candidate ideas are novel, all relevant literature is covered, scientific conclusions are correct, research productivity improves, or a venue will accept a paper. Local hashes check recorded consistency; they are not external attestations, complete source snapshots, or protection against an owner rewriting checksums or deleting entire histories. Version and back up research projects, and use independent evaluation where the scientific claim requires it.

## Design sources and license

This original implementation draws on selected materials from [ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio), [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep), [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills), [Orchestra AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs), [Anthropic scientific-problem-selection](https://github.com/anthropics/life-sciences/blob/main/scientific-problem-selection/SKILL.md), and [AIRAS](https://github.com/airas-org/airas).

The source audit records the particular files or documentation inspected, their reading depth, adaptations, limitations, and original scientific references in [SOURCES.md](SOURCES.md). It does not claim that every file in those repositories was read or that their full systems were reproduced. No upstream collection must be installed to use this skill, and upstream files are not vendored here.

Original code and documentation are available under the [MIT License](LICENSE). Linked papers, datasets, products, and upstream skills retain their own licenses. The researcher controls the research direction, resource budget, and scope of disclosure.
