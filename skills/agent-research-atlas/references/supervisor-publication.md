# Benchmark, manuscript and review-response workbench

Adapted and substantially revised from [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills/tree/a20d76ef3979b804d7dbf599d577826957e0a8a9), Yuyu Luo and contributors. This file is **CC BY-NC-SA 4.0**; see `LICENSE.supervisor.md`. Atlas-specific contracts connect these workflows to existing evidence, experiment and maintenance records.

## Contents

1. Select the paper's contribution
2. Design an informative benchmark (C25)
3. Align a method paper
4. Draft usable manuscript prose (C26)
5. Polish and translate without changing the science
6. Review a complete draft
7. Resolve each reviewer concern (C27)
8. Maintain reusable artifacts

## 1. Select the paper's contribution

| Main contribution | Central question | Essential product |
|---|---|---|
| Method or system | What mechanism solves a specified difficulty? | Mechanism–implementation–measurement chain |
| New problem or setting | What meaningful question was previously missing or ill-defined? | Task formulation and operational constraints |
| Benchmark or evaluation | What capability can now be measured more informatively? | Construction, validity and diagnostic evidence |
| Empirical finding | What reliable observation changes current understanding? | Comparison conditions, uncertainty and alternative explanations |
| Theory or another research paradigm | What proposition or identification claim is established? | The relevant assumptions and discipline-specific evidence |

Choose one primary route while retaining justified secondary contributions. A benchmark can make a useful contribution without a new model. A methods paper needs a mechanism argument beyond a higher aggregate score.

## 2. Design an informative benchmark (C25)

Start from `assets/supervisor/benchmark-dossier.md` and complete five linked parts.

**Evaluation gap.** Identify the capability existing evaluations miss and a concrete source-backed case illustrating it. Compare the closest benchmarks by construct, task/information, data origin, labels, metrics, diagnostic slices and cost. The number of comparisons follows the actual nearest work.

**Construction.** Choose a construction strategy for a reason: derive cases from known knowledge or constraints; apply controlled perturbations to existing cases; or generate candidates adaptively with a separate validation process. Record licenses/permissions, selection, generation versions, annotation guidelines, adjudication, quality checks, data lineage and release artifacts. Keep generated variants linked to their source case.

**Evaluation validity.** Define observable inputs and permitted actions, scoring rubrics, failure categories, difficulty axes and ambiguous-case treatment. Keep hidden evaluator labels out of the agent's decision inputs. Freeze splits at the appropriate family/document/user level before tuning; check contamination and near duplicates across splits. Validate an automated judge against suitable independently reviewed material and retain disagreements.

Synthetic or recently collected data is not automatically free of contamination; annotation agreement is not by itself ground truth. Distinguish training exposure, prompt leakage, shared source material and adaptation to the evaluation. Version the benchmark when data or scoring changes, record maintenance and retirement conditions, and revisit conclusions that depend on an earlier version.

**Empirical diagnosis.** Organize experiments by research question. Compare strong simple rules, established systems and relevant model families under declared information and budgets. Report denominators, abstentions, timeouts, failures, uncertainty and per-slice results. One clarification turn and one retrieval call are not automatically equal-cost treatments. Explain what each diagnostic finding changes about future research.

Define the effect's sign, the prespecified meaningful-effect threshold and the interval decision branches. “Excludes the threshold” alone is ambiguous: intervals entirely above and entirely below it imply different decisions. Use the directional checks in [methodology.md §10](methodology.md) and preserve an unresolved result when the interval crosses the relevant boundary.

**Companion method.** Include a companion model only when it tests a real response to the findings. Keep training/tuning and final evaluation distinct. Treat absence of a companion model as not applicable when the benchmark is the primary contribution; do not invent an algorithm merely to complete a template.

For Agent intent/routing/retrieval studies, useful axes include answer-sensitive ambiguity, explicit task-version constraints, stale evidence, permission scope, recoverable tool errors and action cancellation timing. Select axes supported by the question. A “newer” document is not always the correct document when a task targets an older version.

The dossier should produce the gap comparison, construction lineage, task/rubric definition, split and contamination plan, RQ-to-analysis table, release manifest and actual findings when available. Plans remain plans until run artifacts exist.

Choose task difficulty and model coverage to answer the evaluation question. Do not aim for a universal low accuracy range, model count or dataset count. Verify current venue-specific requirements against official guidance and apply each to its actual contribution type; dataset documentation requirements, executable-artifact requirements and analytical-paper requirements can differ.

## 3. Align a method paper

Connect the problem, prior-work limitation, proposed mechanism, implementation difficulty, design choice, observation and contribution. Inspect each link:

- Does the claimed limitation actually hold in the cited setting?
- Does the mechanism address that limitation?
- Does the difficulty arise from the mechanism, rather than being invented to justify an existing module?
- Does each design choice have a role that an ablation, counterexample or other suitable analysis can distinguish?
- Does each contribution have a corresponding section and evidence?

Use a many-to-many mapping when the system requires it. Shared modules can address several difficulties, and a difficulty may need several components. Do not force three challenges, three modules or three contributions; prioritize the contributions the evidence supports.

Retain unresolved limitations that affect interpretation. A necessary conventional component can remain part of a reproducible method without being presented as an original contribution.

## 4. Draft usable manuscript prose (C26)

Identify the requested artifact: an outline, a paragraph, a section, a full paper or a revision. Read the author's materials and the relevant original literature before writing the corresponding claims. Default to Chinese research discussion and English manuscript prose; follow an explicit language or venue request first.

Maintain a separate evidence map using `assets/supervisor/manuscript-evidence.md`: sentence or claim ID, exact wording, source/run, locator, version, observed versus planned status, supporting scope and manuscript location. This working map connects to the atlas and `audit.py values` for numerical claims.

For an introduction, plan the necessary argument internally: research object and motivation, known approaches and specific gap, goal, key difficulty, proposed response and contribution. Use a real running example when supplied and verified. Choose paragraph count and citation density to fit the argument, length and venue. A benchmark introduction emphasizes evaluation gap and design; it is not forced into a method narrative.

Write connected paragraphs that the user can use. Keep planning labels, score tables, gate reports, evidence-level labels and unresolved placeholders in working files. Deliver the requested prose first, followed by only material author decisions or missing inputs in a separate note when needed. Do not turn every precaution into a paragraph in the manuscript or README.

Match wording to actual evidence. A planned experiment may be described as planned; it cannot become “preliminary results suggest” without observations. A source's access level describes what was read, not a license to make any claim. Without an observed comparison, omit comparative success language rather than replacing a missing number with “improves over baselines.”

Search to resolve a specific citation need and verify the sentence-level support. Match in-text references to the bibliography and check identities, versions and context. Separate an independent citation check when available; give the checker the manuscript, cited sources and relevant author records without a desired verdict. Avoid mandatory reference quotas.

Organize sections by their job: introduction motivates; methods enable replication; results describe observations; discussion interprets them against alternatives; conclusion answers the question; abstract accurately compresses the finished work. Preserve justified field-specific structures instead of applying a universal section count.

## 5. Polish and translate without changing the science

For language-only work, improve grammar, flow, precision and term consistency while preserving the population, conditions, numbers, units, comparison and causal strength. Keep “associated with” distinct from “causes,” and retain scope such as “on the evaluated tasks.”

When a content change is necessary, make it reviewable in a separate before/after note or version diff. If the task explicitly includes correcting unsupported claims, perform those corrections and explain them; do not repeatedly request approval for already authorized editing. Do not quietly add a new mechanism, citation, result or example under the label of polish.

Translate Chinese drafts by recovering propositions and composing idiomatic English, not copying Chinese word order. Do not add a causal connective unless the source actually establishes causality. Keep a stable bilingual terminology list for intent, routing, retrieval, grounding and other project terms. Preserve the author's voice and use concrete facts in place of inflated adjectives and formulaic transitions.

For a long manuscript, record every processed section and unreadable element. Maintain clean final prose and separate editing notes. A language edit does not resolve a broken scientific argument; route the specific issue to the evidence or design workbench.

Use grammatical context and the requested style guide. Do not enforce arbitrary banned-word lists, a ban on clauses or multiple verbs, or one punctuation convention as a scientific quality criterion. For example, “in descending order” is already grammatical. Explain a substantive edit using the actual sentence and intended meaning.

## 6. Review a complete draft

Start with the paper's question and principal claim, then inspect methodology, measurement, comparison, reasoning, presentation and reproducibility. Select standards by research design. Record each finding as location, issue, evidence, consequence, severity and smallest adequate repair.

Record the actual files, sections, pages and figures examined. An abstract, caption or extracted text supports only the corresponding check; it does not establish that the full manuscript or rendered figures were inspected.

Prioritize issues by their actual effect. An unsupported main conclusion or contaminated test split can block the argument; a grammar error cannot be assigned that importance merely because a template labels every consistency failure critical. Check the rendered document when layout, equations or figures matter. Report actual locations and repairs, not an uncalibrated acceptance prediction.

## 7. Resolve each reviewer concern (C27)

Use `assets/supervisor/review-response.md`. Preserve every reviewer question and weakness with a stable ID and its original wording or exact locator. Split compound concerns into traceable subitems; group duplicates only when every original ID remains accounted for.

For each concern record:

1. The observable technical issue: unclear scope, missing comparison, validity, contribution, exposition, reproducibility or other specified concern.
2. The evidence already available and its location.
3. The appropriate action: explain existing evidence, correct the manuscript, perform an authorized new test, narrow the claim, acknowledge a limitation, or justify a disagreement.
4. The exact revision location and completion state.
5. The response text, when requested, tied to completed actions.

Match response length and structure to the actual concern and venue rules. Do not infer a stable reviewer personality or probability of changing their score from tone. Do not import historical cluster percentages or effect-size cutoffs as personalized forecasts. Address criticism on its technical merits.

A large standardized effect size alone establishes neither statistical significance nor that a response strategy caused a score change. Any separate study of such strategies needs its own outcome definition, dependency structure, confound analysis and validation.

Distinguish proposed experiments, running work, completed results and manuscript edits. Never say “we have added” when the action remains planned. When a requested experiment cannot be completed, explain the available evidence and the resulting scope change. Disagree directly and respectfully when the source supports it; do not invent a concession or dodge the question.

Before delivery, verify coverage of every original concern, numerical consistency, cited locations and the final word/page limit. Keep the concern ledger separate from the clean reply. A request for guidance produces a response plan; a request for a complete response produces actual usable prose based on available evidence.

## 8. Maintain reusable artifacts

Store benchmark dossiers, evidence maps and response ledgers in the project. Reference them from existing question, hypothesis, evidence, experiment and decision nodes. Use stable IDs rather than duplicating paper records. Record task type, selected workbench section and useful output paths in the handoff.

When a run, claim or manuscript premise changes, connect it to the current dependency graph so affected prose and responses enter review. Keep finished language, internal evidence records and historical versions separately identifiable. Diagnose additions with `audit.py locate --query C25`, `C26` or `C27`.
