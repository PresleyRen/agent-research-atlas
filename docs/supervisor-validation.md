# Supervisor integration validation / 集成验证

Date: **2026-10-21**. Candidate: **v1.1.0**. This record describes observed task outputs and their actual limits; it does not certify upstream services or scientific discovery effectiveness.

## 1. What was checked

The source audit covers **12 Supervisor skills, 70 associated Markdown references and 18 Chinese handbook chapters**, plus seven supporting texts. The exact pinned commit, read manifest and adoption decisions are in [supervisor-source-audit.md](supervisor-source-audit.md). Reading coverage and behavioral execution are separate records.

The local deterministic suite ran after the main integration: **94 tests passed**, exit 0; the suite reported **18.040 seconds**, and the wrapper measured **18.192 seconds**. See [raw log](supervisor-local-tests.txt) and [command/version record](supervisor-local-test-run.json). These exercise the three local Python tools, not all prose methods or external products. The three Python implementation hashes remain unchanged from that run.

Three fresh assistant contexts completed ordinary project tasks using synthetic local materials. They received the skill, project and work request, with no expected conclusions or score sheet. The first three were explicitly told that the materials were offline synthetic fixtures, so these are not fully blinded studies. A fourth, narrow project task followed a real review finding. The coordinator inspected original files, actual deliverables, logs and input preservation. A separate read-only reviewer examined the first three task outputs; its [report](supervisor/output-review.md) and [structured findings](supervisor/output-review.json) preserve what it found and rechecked. None of this constitutes independent scientific replication.

Reusable inputs, task descriptions and actual snapshots are in [evals/supervisor](../evals/supervisor/README.md). All four input manifests, the manifests themselves, and all **254 archived files** match their recorded SHA-256 hashes; the four snapshot manifests are excluded from their own lists. Original absolute paths identify the source run; use the relative index for navigation after checkout.

## 2. Actual project tasks

| Task | Actual deliverables and observations | Remaining scope |
|---|---|---|
| [Discovery and benchmark](../evals/supervisor/results/discovery/HANDOFF.md) | A research choice, complete benchmark dossier, annotation/data contract, analysis plan, bilingual retrieval plan and continued map. Diagnosed the baseline's post-hoc `reference_intent` access, paraphrase-family split leakage and absent case rows. Chose diagnostic evaluation first, kept deterministic filtering/extra retrieval as strong baselines, and did not force a new learned model. Preserved all seven content inputs plus their manifest. Final atlas: revision 5, 40 nodes, 15 edges; three protocol-impact reviews resolved. | No real literature search, actual case acquisition, annotation, split execution, model run, experiment freeze or empirical hypothesis upgrade. `G-COVERAGE-UNSEARCHED` and `G-FEASIBILITY` remain. One analysis-rule defect was found and repaired as recorded below. |
| [Writing, polish and reviewer response](../evals/supervisor/results/writing/HANDOFF.md) | Actual English introduction and method sections, polished sentences, evidence map, edit notes, pre-submission review, concern ledger and complete responses. Corrected the draft's 96% against supplied 50/64 = 78.125%; baseline 44/64 = 68.75%; descriptive difference 9.375 percentage points. All five original concerns and twelve subitems are covered. Planned large-model/latency work remains planned. Preserved five content inputs plus manifest. Atlas: revision 4, 30 nodes, 11 edges. | This checks editorial consistency with a synthetic project, not the truth of a real scientific claim, actual reviewer acceptance or full-document publication readiness. Family dependence and exploratory analysis remain explicit. |
| [Figures and editable reconstruction](../evals/supervisor/results/figures/HANDOFF.md) | A `.drawio` source with six native modules and six directed connectors, two free labels and one selective 101×101 crop; actual SVG/PNG/PDF architecture and result-plot previews, captions, editing map, scripts and check records. Three supplied CSV rows are reflected in the plot. Latency is lower-is-better; the tradeoff direction is upper-left. No invented error bars or denominators. A plot label/footnote collision was detected and corrected before final inspection. Preserved four content inputs plus manifest. Atlas: revision 1, 21 nodes, 6 edges. | Native draw.io application opening, dragging, anchors, fonts and export were **not run**. Architecture previews were rendered from a shared scene through SVG/Inkscape; they are not claimed to be native draw.io exports. XML structure, actual preview appearance and native-application fidelity are distinct checks. |
| [Directional interval decisions](../evals/supervisor/results/intervals/HANDOFF.md) | A concise five-case decision table, revised rule, evidence notes and exact Decimal endpoint checks. Distinguished entirely above, below, across, negative and exactly touching the practical threshold; retained the original erroneous rule. Preserved three content inputs plus manifest. | Hypothetical design decisions only. No intervals were estimated, no coverage/power/causal method was tested and no empirical states were created. The narrow task appropriately did not create a whole research atlas. |

The coordinator independently ran `atlas.py check` on the archived discovery, writing and figure maps; all returned exit 0 and `valid=true`. This verifies recorded structure and local source paths. It does not certify the scientific interpretation.

Archived `history/views/` files retain their original bytes and map-relative links. Those cached pages are revision evidence, not standalone navigation pages at their cache path; use the current maps linked in the task index. Packaging checks count current-document links separately from these historical links.

The writing task's corrected numerical ledger reports **11/11 matches**. Its separate audit of the original 96% claim intentionally returns **exit 3 / mismatch**, and that failing evidence is retained. The figure task reports **10/10 JSON numerical matches** and separately compares the three CSV records with SVG labels. Numerical agreement is not a substitute for measurement validity.

## 3. A real defect, retained and repaired

The discovery draft initially said that a primary effect interval which “excludes the pre-specified δ” challenges superiority. This was directionally wrong: an interval entirely **above** a positive practical threshold also excludes it. The independent output review identified the problem, the coordinator requested a focused correction, and the author preserved the original bytes before revising the plan.

| Record | SHA-256 |
|---|---|
| [Original analysis backup](../evals/supervisor/results/discovery/worklog/analysis-before-interval-review.md) | `3aa81d73b5371c6b490fc6cad68d1c999a9f58eba2618600fba44a194415be69` |
| [Revised analysis](../evals/supervisor/results/discovery/design/analysis-and-execution.md) | `f38e8fb57169aa5967bcad3b9839e184ca4b3a7a61fa99413eb0de110be8e3a6` |

The revised rule defines the effect sign first. For positive benefit Δ and a strict goal Δ > δ, lower bound L > δ supports the scoped practical-superiority prediction; upper bound U < δ challenges achieving that threshold, but may still allow a smaller positive improvement; U < 0 supports an unfavorable comparison in the stated setting. Crossing or touching δ does not establish strict superiority. Mechanism refutation, equivalence and causal inference require their own evidence.

The skill's [methodology §10](../skills/agent-research-atlas/references/methodology.md), publication workbench and benchmark template now carry this contract. The discovery map recorded the change to E1 and queued dependent hypothesis, analysis and priority decisions for actual review. The history and completed reviews remain in the snapshot; no research run or scientific-status upgrade was manufactured.

The fresh narrow task then used δ = 0.02 and five supplied hypothetical intervals:

| Case | Interval | Observed interpretation |
|---|---|---|
| A | [0.03, 0.05] | Entirely above δ: supports the strict target within scope. |
| B | [0.005, 0.015] | Positive but below δ: permits a smaller improvement, does not meet the target. |
| C | [0.01, 0.035] | Positive and crosses δ: target unresolved, no automatic resource expansion. |
| D | [−0.04, −0.01] | Entirely negative: challenges the current favorable-comparison prediction. |
| E | [0.02, 0.05] | Touches δ exactly: L = δ does not satisfy strict L > δ. |

The coordinator read the actual [decision table](../evals/supervisor/results/intervals/DECISION-TABLE.md), [revised rule](../evals/supervisor/results/intervals/REVISED-RULE.md) and [checks](../evals/supervisor/results/intervals/CHECKS.json). All five interpretations match the defined sign and strict threshold. This is a focused interpretation regression, not validation of a statistical estimation engine.

## 4. Conflict coverage

Each entry records a selected concrete behavior. It does not turn every sentence in that conflict contract into a tested implementation.

| Conflict | Useful behavior retained | Misleading default constrained | Evidence / boundary |
|---|---|---|---|
| CF21 | Early comparison, validity review, narrower decision and unlock conditions | One unfair baseline loss permanently kills an idea; directionless threshold rule | Discovery diagnoses information/split problems and selects a feasible evaluation route. Initial interval defect repaired, then five-case task checked. No real negative experiment interpreted. |
| CF22 | Complete benchmark design and diagnostic research questions | Mandatory new model, fixed model/dataset counts, low-accuracy quota | Discovery dossier uses construct/lineage/splits/measurement; keeps companion model optional. No benchmark was actually collected. |
| CF23 | Traceable contribution narrative and usable prose | Forced six paragraphs, three modules and one-to-one mapping | Actual four-paragraph introduction and two-role shared-state method; benchmark route selected on its own contribution. |
| CF24 | Clean manuscript plus separate evidence records | Plans become preliminary results; unsupported scope/cause survives into prose | Writing removes unsupported 96%, three-real-dataset and universal-causal statements while delivering full sections. No fabricated external citations. |
| CF25 | Original concern IDs, technical evidence, actual actions and complete replies | Reviewer personality/score prediction; unperformed experiments called complete | All five concerns/twelve subitems retained; larger-model and latency work remain unperformed. No real reviewer or venue submission. |
| CF26 | Meaning-preserving polish and authorized factual corrections | “associated with” becomes “causes”; correct “in descending order” altered by a rigid rule | Supplied sentences and manuscript edited with explicit scientific-change notes. This is a selected sentence/task check, not broad translation accuracy. |
| CF27 | Readable, data-faithful tradeoff plot | “Upper right is always best,” invented error bars or obligatory zero/nonzero axes | Actual three-row latency/accuracy plot, correct direction, explicit zoomed accuracy range and rendered previews. No measurement uncertainty estimated. |
| CF28 | Native objects, selective raster detail and real preview files | Whole-image embedding described as editable; XML parse called full visual validation | Six modules/six connectors inspected; root reviewed reference and rendered PNGs. Native draw.io application verification remains unrun. |

## 5. Mapping the twelve source skills to observed work

| Source skill | Selected task evidence |
|---|---|
| idea-evaluator | Discovery: risk/benefit comparison, premise validity, choice and unlock conditions. |
| deep-research | Discovery: synthesis of supplied local materials, rival explanations and bilingual planned retrieval. Live retrieval not exercised. |
| vibe-research-workflow | Discovery: research brief, contribution choice, minimal discriminating work, map and handoff. |
| tech-paper-template | Writing: problem/mechanism/implementation/evidence structure matching the actual two-role method. |
| intro-drafter | Writing: actual English introduction, bounded claims and research motivation. |
| paper-writer | Writing: usable introduction and methods plus separate evidence notes. Other paper sections not drafted. |
| benchmark-paper-template | Discovery: complete benchmark dossier without fixed quotas or mandatory new model. |
| paper-polish | Writing: corrected prose and sentences, preserved association language and valid grammar. |
| pre-submission-reviewer | Writing: located issues based on actual available sections and records. No full manuscript/venue compliance audit. |
| figure-designer | Figures: data plot, scientific labels, axis direction, captions and actual render inspection. |
| drawio-reconstruction | Figures: native editable objects, connections and selective crop. Native editor runtime not exercised. |
| rebuttal-guidance | Writing: concern ledger, actual revisions, remaining work and full technical replies. |

All twelve have a selected task observation or explicit execution boundary. The **74 source features** remain individually classified in the registry; this table does not claim 74 separate passing behavioral tests or twelve upstream runtimes executed.

## 6. Version boundaries and unrun work

The first three tasks began before the directional-interval addition to `methodology.md`. Their reading records preserve the source hashes they actually saw. The discovery author received one explicit coordinator repair request, preserved its first draft, and updated the project. The fourth task used the repaired methodology. The deterministic run predates later registry verification metadata and these prose refinements; its original version record has not been rewritten to match final bytes. Final packaging/index checks are recorded separately in [supervisor-packaging-check.json](supervisor-packaging-check.json).

No upstream helper code was executed or bundled. No paid/provider account, model inference, training, live Chinese/English literature search, real annotation study, citation-completeness evaluation, benchmark experiment or publication submission occurred in these four trials. Native draw.io application checks, full manuscript compilation, statistical estimators and real research novelty remain unrun. Earlier narrow retrieval observations are kept in the [historical validation record](validation.md), rather than presented as new tests.

Remote CI and release status must be read from the exact published commit and its Actions runs. A local log, existing workflow file or prospective release name does not establish remote execution or publication.
