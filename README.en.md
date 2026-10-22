# Agent Research Atlas

**Connect literature, research questions, experiments, manuscripts and updates in a research map you can keep working from.**

[中文](README.md) · [Use the skill](skills/agent-research-atlas/SKILL.md) · [All sources](SOURCES.md) · [Coverage and complements](docs/coverage-audit.md) · [Validation](docs/validation.md) · [Extension guide](docs/EXTENDING.md)

Agent Research Atlas is a Chinese/English skill for Agent research. It guides an AI assistant through surveys and original papers, turns verified limitations and failures into traceable research gaps, and runs a Research Supervisor → Scientist → Critic loop that keeps checking prior work, data, measurement, feasibility and rival explanations before committing to a direction.

Each project keeps its own map, domain folders, sources, plans, results and decisions. Existing maps are read and reused. New evidence can update dependent conclusions and next steps. Start with a complete research cycle or request a focused task such as a closest-work review, benchmark design, Methods section, reviewer response or editable method figure.

## Quick start

Install `skills/agent-research-atlas/` as one Skill in a compatible host, or ask an assistant with search, file and code capabilities to read its `SKILL.md`. The three bundled tools require **Python 3.10+ and the standard library**. Research tasks use the host's available retrieval, full-text, experiment and drawing tools.

```text
Use agent-research-atlas to continue /path/to/my-agent-project.
My topics are intent recognition, document retrieval, routing and answering.
Read the existing map, surveys, papers and failed directions; extend Chinese
and English searches; compare the nearest work; propose a research question
and a locally feasible discriminating experiment. Update the map, domain
folders and next steps, and link actual results to manuscript claims.
```

| Current task | Example request | Deliverables |
|---|---|---|
| Orient in a field | “Map research from intent to retrieval and answering, including progress and disagreements.” | Sourced directions, comparisons and open questions |
| Choose a question | “Compare these ideas against nearest work, mechanisms and our actual resources.” | Research brief, rivals, feasibility and decision |
| Design evaluation research | “Build a benchmark separating intent ambiguity from missing knowledge.” | Construction, validity, splits, baselines, RQs and analyses |
| Run experiments | “Execute this approved plan and retain every outcome.” | Frozen plan, raw records, numerical checks and interpretation |
| Draft a paper | “Write Introduction and Methods from the evidence; keep a separate evidence map.” | Usable prose, citations and provenance |
| Revise and respond | “Review the manuscript and answer every reviewer concern.” | Located issues, revisions, coverage ledger and complete response |
| Prepare figures | “Explain the method and reconstruct the reference as editable drawio.” | Native figures, previews, captions and editing map |
| Resume or extend | “Update the old map and locate what needs improvement.” | Impacted records, review queue, owners and repair paths |

## Complete capability inventory

The host executes research protocols on the actual materials; local scripts maintain maps, records and repeatable checks. Each of these **32 capabilities** has a stable ID for locating its implementation, sources, complements and verification records.

| Capability | Work and deliverables |
|---|---|
| C01 · Scope and taxonomy | Define the question, time/language boundaries and inclusion criteria; extend 14 Agent seed domains. |
| C02 · Persistent research atlas | Discover and reuse maps; retain originals, human notes and revisions; generate JSON, Markdown/Mermaid and offline HTML views. |
| C03 · Bilingual discovery | Search across Chinese/English terminology and neighboring fields, with query, provider, date and access records. |
| C04 · Paper identity and citation expansion | Normalize DOI/arXiv identities, preserve versions and expand citation trails including relevant counterevidence. |
| C05 · Reading and extraction | Use surveys for orientation and primary papers for claims; extract problems, methods, conditions, findings, limitations and locators. |
| C06 · Evidence critique | Separate observations, source claims and inference; examine measurement, comparisons, bias and rival explanations. |
| C07 · Idea generation and transfer | Generate candidate mechanisms from failures, changed assumptions, neighboring methods, inversion and quality/cost trade-offs. |
| C08 · Problem selection | Compare objectives, risk, constraints and decision trees; select an informative next check and a reasoned continuation decision. |
| C09 · Closest-work comparison | Compare the nearest work on goals, information, mechanism, insight, domain and evaluation cost. |
| C10 · Hypotheses and rival predictions | Turn ideas into observable predictions, alternatives and falsification conditions linked to evidence and experiments. |
| C11 · Local feasibility | Check data rights, annotation, code, compute, evaluators and budget; resolve decision-changing unknowns first. |
| C12 · Method selection and implementation fidelity | Choose theory, diagnosis, comparison, intervention or measurement methods; trace inputs, operations, code and metrics. |
| C13 · Discriminating experiments | Plan simple/strong baselines, ablations, matched information/budgets, units, splits, metrics and outcome interpretations. |
| C14 · Frozen plans and amendments | Freeze prospective plans and declared input hashes; allow declared candidate changes while tracking evaluator/data drift. |
| C15 · Bounded experiment execution | Run authorized local commands with recorded reservations; preserve failures, timeouts, cancellations and raw output; import external results. |
| C16 · Provenance and numerical checks | Retain origins, versions, hashes and logs; check numerical JSON fields, locators, tolerances and exact large integers. |
| C17 · Statistical design | Define estimands and independent units before choosing power, minimum effect, precision, equivalence/noninferiority or sequential analysis. |
| C18 · Results to claims | Bound conclusions to the actual findings; distinguish implementation, measurement and mechanism issues and retain unresolved interpretations. |
| C19 · Independent critique | Separate proposal and review contexts when available; challenge candidates using actual sources and rival explanations. |
| C20 · Updates and failure memory | Preserve parked/refuted branches and reopening conditions; propagate recorded premise changes to dependent experiments, claims and prose. |
| C21 · Publication arguments and citations | Map claims to runs and figures; organize related work, methods, limitations and reproduction; check citation identity and sentence-level support. |
| C22 · Tool adapters | Connect available search, full-text/PDF, citation-context, evaluation, training and cloud tools through explicit request/result contracts. |
| C23 · Coverage and extension lookup | Locate owner files/functions, source features, complements, conflicts and tests from a symptom or C-ID; diagnose recorded project gaps. |
| C24 · Reproducible handoff | Carry scope, sources, resources, plans, actual results, failures, atlas revision and next actions into the next session. |
| C25 · Benchmark and evaluation research | Design evaluation gaps, construction, annotation/ground truth, splits/contamination, RQ-driven diagnosis, optional companion methods and maintenance. |
| C26 · Manuscript drafting and bilingual polish | Draft introductions and sections for the contribution type; keep evidence maps, terminology and change notes separate from usable prose. |
| C27 · Submission review and reviewer responses | Locate manuscript issues and account for every original concern through evidence, actions, revision locations, status and response text. |
| C28 · Scientific figures and editable reconstruction | Design motivation, method and result figures; rebuild reference text/shapes/connectors and deliver native sources, actual previews and editing maps. |
| C29 · Research supervision and direction decisions | An evidence-grounded Supervisor/PI chooses proceed, search-more, repair-measurement, narrow, pivot, park or stop. |
| C30 · Paper-level gap mining and ledger | Extract and verify limitations/gaps from original papers, Discussion/Limitations, later citations and negative evidence; track open/partial/solved/invalid/parked states. |
| C31 · Manuscript-ready citation corpus | Preserve identity, version, exact locator, what a source can/cannot support, its manuscript role and linked Atlas IDs. |
| C32 · Scientist–Critic adaptive loop | Scientist executes; Critic attacks prior work/data/measurement/baselines/mechanism; Supervisor decides whether to deepen, broaden, pivot, park or stop. |

## Text workflow map

```text
Project entry
  → C29 Research Supervisor defines the decision-changing unknown
  → C01/C02 scope + existing atlas
  → Scientist: C03 search → C04 citation graph → C05 surveys/original papers
  → C30 Gap Ledger → C31 Citation Corpus
  → C06 evidence critique + C09 closest work → C07/C08 candidate directions
  → C10 rivals → C11 data/measurement/resource feasibility → C12 method card

Supervisor gate
  ├─ invalid/already solved gap → STOP or choose another gap
  ├─ data/evaluator cannot answer claim → REPAIR MEASUREMENT / NARROW
  ├─ missing decision-changing literature → SEARCH MORE
  └─ testable → PROCEED → C13 discriminating experiment

Empirical loop
  C14 freeze → C15 execute → C16 provenance/numbers → C17 inference → C18 claim
  → C19/C32 Critic attacks prior work, data, leakage, baselines, mechanism, interpretation
  → C29 Supervisor: DEEPEN / BROADEN / PIVOT / PARK / STOP
  → return to C03–C06 when new evidence is needed

Publication
  C21 argument/citations → C26 prose + C28 figures
  → C27 submission review/responses → C24 handoff

Across stages
  C20 failure/new-evidence memory; C22 adapters; C23 extension lookup; C02 continuous map updates
```

## Research Supervisor–Scientist loop

v1.2 promotes research supervision into a first-class architecture via [research-supervision.md](skills/agent-research-atlas/references/research-supervision.md).

- **Supervisor / PI Advisor** keeps asking whether the original literature, later work, data and measurement actually justify the direction.
- **Scientist / Executor** performs the search, full-text reading, gap verification, experiments and atlas updates.
- **Critic / Reviewer** attacks nearest-work coverage, data/measurement validity, leakage, strong baselines, rival mechanisms and claim scope.

New reusable artifacts are the [Gap Ledger](skills/agent-research-atlas/assets/supervision/gap-ledger.md), [Citation Corpus](skills/agent-research-atlas/assets/supervision/citation-corpus.md) and [Mentor Panel](skills/agent-research-atlas/assets/supervision/mentor-panel.md). `gap` is now a first-class Atlas node with candidate/open/partially_solved/solved/invalid_gap/inaccessible/unknown/parked states. See the [v1.2 source audit](docs/supervision-source-audit.md).

## Supervisor-Skills integration

The collection associated with the user's “鸭博士” reference is indexed by its official name, **[HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)**. We read all **12 SKILL.md bodies, their Markdown references and 18 Chinese handbook chapters** at the pinned revision, then connected selected methods to the existing atlas and evidence chain. See the [integration/source audit](docs/supervisor-source-audit.md) for files, decisions and reading records.

| Skill | Incorporated strengths | Capability |
|---|---|---|
| `idea-evaluator` | Contribution type, early risks, five benefit lenses, premise changes and resource fit | C07–C11 |
| `deep-research` | Question-driven multi-perspective discovery, search blind spots, conditional synthesis and citation checks | C03–C06/C09 |
| `vibe-research-workflow` | Research/coding/figure/writing coordination, method cards and continuity | C12/C15/C24 |
| `tech-paper-template` | Problem–limitation–mechanism–implementation–contribution alignment | C12/C21/C26 |
| `intro-drafter` | Contribution-specific introductions, running examples and usable paragraphs | C26 |
| `paper-writer` | Section/full-manuscript drafting with separate evidence maps and citation review | C21/C26 |
| `benchmark-paper-template` | Evaluation gap, construction, validity, diagnostic findings and optional companion methods | C25 |
| `paper-polish` | Meaning-preserving polish, Chinese-to-English rewriting and terminology consistency | C26 |
| `pre-submission-reviewer` | Paradigm-specific review of arguments, measurement, comparisons, presentation and reproduction | C19/C21/C27 |
| `rebuttal-guidance` | Concern decomposition, evidence/action/revision mapping and complete responses | C27 |
| `figure-designer` | Purpose-driven figure design, data/encoding, captions and reproducible plots | C28 |
| `drawio-reconstruction` | Per-object reference reconstruction, native text/connectors, mixed media and visual handoff | C28 |

Workbenches: [research advising and deep discovery](skills/agent-research-atlas/references/supervisor-discovery.md), [benchmark/manuscript/reviewer response](skills/agent-research-atlas/references/supervisor-publication.md), and [scientific figures/reconstruction](skills/agent-research-atlas/references/supervisor-figures.md). Five [project templates](skills/agent-research-atlas/assets/supervisor) cover the research brief, benchmark dossier, manuscript evidence, response ledger and figure handoff.

## How sources complement one another

| Source group | Strength | Connection to Atlas |
|---|---|---|
| ResearchStudio | Idea generation, paper search and closest-work overlap | Preserve candidates and compare their exact difference against neighboring work |
| ARIS | Literature, planning, implementation bridges, experiments, ablation and claim/citation review | Connect questions to code, raw results and manuscript claims |
| K-Dense | Literature reviews, hypotheses, critical thinking, design and power | Add appropriate research designs and statistical goals |
| Orchestra / Anthropic / Research-Equality | Creative operations, problem choice, risk, decision trees and research loops | Choose methods for the present bottleneck and retain branch decisions |
| Supervisor-Skills | Research advising, benchmarks, drafting, polish, responses and figures | Turn exploration and experiments into complete research/writing deliverables |
| Chinese/English discovery and citation services | Identity, full text, citation graphs, context and extraction | Share paper IDs and provenance across providers |
| Hugging Face / autonomous research systems | Data, evaluation, training, logs, cloud jobs and execution patterns | Adapt to the available environment and return versions, outputs and resource records |
| Atlas local tools | Maps, frozen inputs, run records, dependency updates and audits | Provide persistent project state for the combined workflow |

The integrated contracts resolve disagreements through the research design: check measurement and comparability before interpreting a negative result; let benchmarks center on measurement contributions; allow many-to-many method mappings; separate usable prose from evidence work files; address each actual review concern; and choose figure encodings from the quantities being shown. The complete [296-feature and 28-conflict audit](docs/coverage-audit.md) records adoption, complements and repair routes.

## Research areas and bilingual sources

Seed areas include intent/goals, ambiguity/clarification, routing, planning, document ingestion/retrieval, RAG/answering, tools, memory, multi-agent coordination, evaluation, reliability/safety, efficiency, and data/adaptation. Extend the taxonomy for embodied agents, multimodality, human-agent collaboration, reinforcement learning or formal verification. Each domain records what was actually explored.

Queries include Chinese and English terminology, acronyms and neighboring-field vocabulary. Applicable sources include host search, OpenAlex, Semantic Scholar, Crossref, arXiv, DBLP, OpenReview, ACL Anthology, ChinaXiv, Chinese journals, CNKI and Wanfang. Full-text and account routes depend on available access. Scite, Elicit, Undermind and PaperQA can support citation context, extraction and local-paper QA through adapters. See the [bilingual retrieval protocol](skills/agent-research-atlas/references/bilingual-retrieval.md).

## Local maps and tools

A project typically holds `atlas.json` and history; overview/domain views; human `domains/<id>/notes.md`; source/query records; hypotheses and decisions; frozen experiments and results; and benchmark/manuscript/response/figure work files. JSON is the maintained state; Markdown/Mermaid and offline HTML are reading views. Writes regenerate views, and recorded premise changes create downstream review items.

```bash
# From the repository; replace the project path with the actual workspace.
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project discover
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project init --title "Agent research"
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project status
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project queries --domain routing --focus-zh "意图歧义" --focus-en "intent ambiguity"
python skills/agent-research-atlas/scripts/audit.py --root /path/to/project project
```

Command and record details: [atlas](skills/agent-research-atlas/references/local-atlas.md), [experiments](skills/agent-research-atlas/references/experiments.md), [evidence and claims](skills/agent-research-atlas/references/evidence-and-claims.md).

## Locate a gap and extend it

```bash
python skills/agent-research-atlas/scripts/audit.py locate --query "C25"
python skills/agent-research-atlas/scripts/audit.py locate --query "polish"
python skills/agent-research-atlas/scripts/audit.py locate --query "drawio"
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

| Gap | Owner | Typical repair |
|---|---|---|
| Literature coverage or Chinese terminology | C01/C03/C05 | Extend vocabulary/providers; verify actual search receipts and source locators |
| Weak mechanism or nearest-work comparison | C07–C10 | Add premise history, strongest neighboring work and rival predictions |
| Unclear experiment or statistical conditions | C11–C17 | Specify resources, independent units, information/cost and analysis |
| Benchmark construction or validity | C25 | Add construct, lineage, ground truth, splits, contamination and diagnosis |
| Draft/polish changes scientific meaning | C26 | Check the exact sentence's sources, numbers, scope and causal strength |
| Missing reviewer response or revision | C27 | Map each original concern to evidence, action, location and status |
| Uneditable or visually incorrect figure | C28 | Check native objects, connectors, rendering, data and editing scope separately |
| New evidence changes an old claim | C20/C23 | Follow dependency paths, update records and perform the actual review |
| A paper states a limitation but it may not be a real open problem | C30 | Build a Gap Ledger entry and verify later work, boundaries, data signal and minimum discriminating test |
| Need ongoing supervisor-style direction control | C29/C32 | Supervisor task → Scientist execution → Critic attack → Supervisor decision |
| References are found but not reusable during writing | C31 | Store identity, locator, support/non-support scope and manuscript role |
| Want research guidance inspired by real professors/labs | C29 | Distill only repeated public research signals with direct/inference/speculative evidence levels |

Extend through **symptom → C-ID → owner file → source feature/conflict → minimal repair → regression task**. The registry maps **81 sources, 312 features, 32 capabilities and 32 conflict contracts**. The [extension guide](docs/EXTENDING.md) covers providers, methods, backends and workbenches.

## Validation and reuse

The [real-publication literature fixture](evals/real_literature/README.md) tests five published sources, competing follow-up findings, and whether a proposed direction is prematurely declared novel or feasible.


```bash
python -m unittest discover -s tests -v
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

The deterministic suite contains **109 tests** (101 original + 8 real-publication evidence checks) for map reuse, identities, states/provenance, frozen inputs, budgets/failure records, dependency updates, numbers and extension references. Independent-context project tasks retain their actual artifacts and conflict decisions. See the [validation overview](docs/validation.md), [earlier tasks](docs/forward-conflicts.md), [Supervisor integration tasks](docs/supervisor-validation.md) and [reusable fixtures](evals/README.md) for executed scope and outcomes.

The project supports careful question selection, testing and writing. Novelty, scientific validity and publication judgments depend on real literature, experiments and peer review. SCI/SCIE and venue-specific fit are checked against current rules for the requested submission.

## License and attribution

Atlas core code and original protocols use [MIT](LICENSE). Three Supervisor-derived workbenches and five templates use **CC BY-NC-SA 4.0**, with credit to Yuyu Luo and contributors and an explanation of the adaptation. See the [license scope and third-party notices](THIRD_PARTY_NOTICES.md). All inspected sources, revisions and adoption locations are in [SOURCES](SOURCES.md).
