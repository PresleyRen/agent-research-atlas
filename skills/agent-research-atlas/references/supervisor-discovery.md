# Research advising: questions, literature and investment decisions

Adapted and substantially revised from [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills/tree/a20d76ef3979b804d7dbf599d577826957e0a8a9), Yuyu Luo and contributors. This file is **CC BY-NC-SA 4.0**; see `LICENSE.supervisor.md` in the skill root. Atlas-specific examples, decision routes and integration changes are identified here. Read the existing methodology and evidence contracts alongside this workbench.

## Contents

1. Route by the decision
2. Turn a topic into a research brief
3. Evaluate a candidate before investing
4. Reconsider assumptions and long-lived problems
5. Build a literature synthesis that answers the questions
6. Coordinate implementation, research and writing
7. Save decisions to the atlas

## 1. Route by the decision

| Current need | Work product | Atlas owners |
|---|---|---|
| Understand a field | Research questions, evidence matrix, conditional synthesis, open questions | C01, C03–C06 |
| Choose among ideas | Contribution route, strongest objection, resource fit, next discriminating check | C07–C13 |
| Design an evaluation resource | Benchmark dossier in `supervisor-publication.md` | C25 |
| Plan a method paper | Problem–challenge–method–evidence map in `supervisor-publication.md` | C12, C13, C26 |
| Explain actual findings | Manuscript and separate evidence map | C18, C21, C26 |

Use the user's requested deliverable and existing project stage. A request to polish one paragraph does not trigger a new literature survey or mandatory full-workflow restart. Infer routine scope from the project; ask only about a decision-changing ambiguity that the records cannot resolve.

## 2. Turn a topic into a research brief

Write the research question in a form that observations can answer. Record the decision the answer will change, the intended reader, the population or task, available information, comparison and time/compute constraints. Two or three questions are a useful starting size, not a quota. Keep an explicit change log when evidence warrants revising them.

For Agent research, distinguish adjacent questions. “Should the agent ask a clarification question?” can mean whether the intent is ambiguous, whether the answer would change an action, whether the user can provide the information, or whether asking is worth its cost. These are different mechanisms and need different observations.

Start with the reusable `assets/supervisor/research-brief.md`. Keep claims, hypotheses and unknown resources separate. Preserve dates and model/data/evaluator versions. If live search is unavailable, complete the local inventory and a search brief; record literature work as planned.

## 3. Evaluate a candidate before investing

### Establish the contribution route

Classify by the method and research claim, rather than the department name: method or system; new problem/setting; measurement/benchmark; theory; empirical finding; or another discipline-specific design. A mixed project can have a primary route and a secondary contribution.

Inspect the main dependency first: an undefined target, unavailable labels, overlapping prior work, an implementation that does not instantiate the mechanism, or an evaluator that measures the wrong construct. For each issue, name the affected claim, its evidence and the least costly check that could change the decision.

Distinguish four situations:

| Situation | Continue with |
|---|---|
| Logical impossibility or an established incompatible constraint | Reject this formulation, retain the reasoning, formulate an explicit alternative if useful |
| Valid observations contradict a specific prediction | Narrow or reject that prediction in its tested setting; record what changed |
| Measurement, implementation, comparability or precision is unresolved | Repair or investigate the issue before a scientific verdict |
| No empirical test yet, but a coherent mechanism and feasible design exist | Retain a proposed/grounded candidate and specify the next test |

Do not convert “the baseline won once” directly into a universal mechanism rejection. Equally, do not invent a favorable subgroup or new threshold to save a contradicted claim. New predictions get new versions and prospective tests. A serious issue may justify stopping the current run while leaving the broader question open.

### Compare benefits and the cost of obtaining evidence

Use effectiveness, speed, robustness, data/annotation/operating cost, and transfer breadth as lenses. Choose those that match the actual claim. State the proposed mechanism, strongest baseline, expected trade-off and observable result for each selected lens. Avoid counting the same cost reduction twice as two independent contributions.

Attach evidence to judgments. Numeric preference scores may help a user compare priorities, but do not translate them into acceptance labels or publication probabilities. Disruptive potential requires a concrete changed premise and a discriminating test, not a count of answered “yes” questions.

Compare the project's full critical path with the user's available time: data access, implementation, evaluation, writing and likely revision. Separate a problem's lasting scientific relevance from the short shelf life of a particular benchmark score or model version. Derive estimates from the project; do not inherit a universal GPU count, weekly hours, improvement percentage or deadline.

End with a specific decision: proceed to the named check; revise the formulation; park pending a named resource; or abandon this version for a stated reason. Keep the current atlas hypothesis state consistent with that decision.

## 4. Reconsider assumptions and long-lived problems

For a promising shift, write a short premise history:

1. Which assumption does the current approach rely on?
2. Why was it reasonable when adopted?
3. What observable condition has changed?
4. What simpler alternative becomes possible?
5. Which case would show that the new alternative fails?

Use this for adjacent-field transfers, neglected problems, changing technology constraints and questions with lasting impact. Find the original work that supports the premise history. A story about a historical breakthrough is a search lead, not evidence that the present analogy works.

Verify that the strongest current neighboring methods still depend on the premise; an obsolete assumption alone is not a present research gap. For a long-lived blocked problem, record the current obstacle, an observable unlocking condition and the minimal check that new evidence would trigger. Reuse the existing problem, parked-candidate and decision records; no fixed-length idea inventory or background schedule is required.

Describe observed failures with their sampling scope, denominator and frequency, and describe their consequences separately. A rare but consequential failure can justify research. Do not impose universal failure-rate or publication-age thresholds.

An Agent example is replacing a one-shot intent label with a versioned intent state. Check whether cancellation, delayed tool execution and superseded constraints create a failure that a simpler deterministic version check already solves before adding a learned gate. This is an illustrative research question, not an established result.

## 5. Build a literature synthesis that answers the questions

### Search perspectives

Choose complementary perspectives: prevailing methods; critical or negative findings; neighboring fields; measurement/evaluation challenges; and deployment conditions. Reuse the existing bilingual query ledger and provider-specific syntax. When separate contexts are available, give each perspective a focused question and shared inclusion criteria. Otherwise perform a clearly labelled serial review.

After merging verified candidates, check missing high-frequency references, sparse branches, excluded hits and unexpected terminology. A thin branch may reflect an unsuitable query, access trouble, a narrow field or a real evidence shortage. Record the reason; do not label every empty cell a research gap or pad it to a paper quota.

### Synthesize by a useful axis

Choose a primary organizing axis that helps answer the research questions, such as decision stage, available information, adaptation mechanism or evaluation setting. Give branches operational definitions. Allow cross-links and overlapping tags when methods span several axes; a research graph does not need forced mutually exclusive leaves.

Build an evidence matrix with each source's identity, read depth, relevant claim, method, setting, comparator, measurement, result, limitations and exact locator. A metadata hit establishes an identity; an abstract supports what it actually says; full-text access alone does not make every possible claim valid.

Write comparisons within connected prose. Explain disagreements using differences in task, data, information, budget, model version, implementation or metric. Preserve unresolved disagreement rather than averaging incompatible findings. Each synthesis conclusion should point back to the sources that support and challenge it.

### Stop according to the research decision

Use the agreed coverage and resource budget. Extend searches when a specific missing item could change the conclusion. Deliver the answered research questions, conditional findings, uncovered areas and next useful search. Do not run an unbounded “all gates clear” loop.

For a requested full survey, use a coherent report with research questions, scope/method, taxonomy, comparisons, open problems and answers to the questions. For a short decision brief, lead with the decision and develop the evidence. Format serves the user's requested document.

## 6. Coordinate implementation, research and writing

Keep a shared project anchor describing the question, current design, constraints and actual state. Give coding work a method card with inputs, operations, outputs and the evaluator that uses them. Break implementation into observable intermediate products; inspect code, outputs and provenance before attributing success to a scientific mechanism.

Use task roles when useful: literature scout, implementation engineer, evaluator, manuscript author and critic. Role labels within one context do not create independent evidence. Reuse existing authorization for local work and record run budgets through the experiment tools.

Use prototypes for learning and reusable experiments for claims. Preserve failed approaches and the reason for changing direction. Select a workflow based on the bottleneck, not a requirement that humans write every line or that AI generate every artifact.

## 7. Save decisions to the atlas

Store briefs and working tables in the authorized project. Reuse paper IDs and evidence records; do not start a second disconnected literature database. Add question/hypothesis/decision nodes with links to the work products and dependencies. Mark explored scope from actual reading, not from completed templates.

When a question, metric or premise changes, update its record so the existing impact and pending-review mechanism reaches dependent experiments and prose. After the actual review, resolve each item with the current revision and a reason. Keep rejected versions available to the next session.
