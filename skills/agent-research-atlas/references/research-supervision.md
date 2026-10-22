# Research supervision loop / 科研导师—研究员闭环

This workbench coordinates evidence-grounded supervision, execution and criticism for research exploration. It integrates useful patterns from Agent Research Atlas, Supervisor-Skills, Kalaris autoresearch, K-Dense evidence lookup, gap-analysis skills, and MentorForge-style evidence-grounded mentor distillation. It does not impersonate real professors or treat model opinions as evidence.

## Roles

### Research Supervisor / PI Advisor
Owns research direction, evidence sufficiency, decision gates and next-task selection. It should repeatedly ask:
- What exact problem is being claimed?
- Which original papers establish the current state?
- Which limitation is author-stated versus project-inferred?
- Has later work already solved the limitation?
- What evidence would falsify the proposed extension?
- Does the available data actually measure the claimed construct?
- Is the cheapest discriminating check cheaper than implementing the full idea?
- What would make us pivot, park or stop?

The Supervisor does not replace literature or experiments with a score. It issues concrete tasks to the Scientist and records proceed / revise / search-more / experiment / pivot / park / stop decisions.

### Research Scientist / Executor
Performs the assigned evidence work: search, read full text when available, extract evidence, maintain the gap ledger and citation corpus, implement experiments, inspect raw data and update the atlas. The Scientist must preserve negative findings and failed searches.

### Research Critic / Reviewer
Attacks the strongest current candidate from a different task context when possible. It checks nearest prior work, data validity, measurement validity, leakage, unfair baselines, alternative mechanisms, claim strength and missing citations. A role label inside one context is not independent evidence; record that limitation.

### Specialist pool
Invoke only when needed: literature scout, citation checker, statistician, benchmark designer, implementation engineer, data/evaluation auditor, paper reviewer, figure designer, venue/journal checker, or an evidence-grounded mentor profile.

## Core cycle

```text
Field / project state
  -> Supervisor defines the decision-changing question
  -> Scientist reads surveys + anchor papers + recent/critical work
  -> Gap Ledger records what is solved / unresolved / uncertain
  -> Citation Corpus stores manuscript-reusable evidence with locators
  -> Supervisor evaluates value, feasibility and evidence sufficiency
      -> not feasible / invalid gap: pivot, narrow or search another branch
      -> plausible but uncertain: assign cheapest discriminating check
      -> testable: Scientist designs/runs controlled experiment
  -> Critic reviews literature, data, design and interpretation
  -> Supervisor decides proceed / revise / broaden / deepen / pivot / park / stop
  -> update atlas and repeat
```

## 1. Literature before opinion

Use a layered anchor set rather than a citation-count shortcut:

1. **Survey anchors** — current reviews/tutorials to establish terminology and method families.
2. **Foundational anchors** — papers that define the task, mechanism, dataset or evaluation regime.
3. **Influence anchors** — frequently cited or repeatedly referenced papers, used to understand the field's trajectory; citation frequency is not quality proof.
4. **Frontier anchors** — strongest recent work and nearest mechanisms, typically including the last 1–3 years when relevant.
5. **Critical anchors** — negative results, replications, benchmark critiques, failure analyses and competing interpretations.

For each important claim, go back to the original source. Metadata identifies a paper; an abstract supports only what it states; “paper exists” is not claim support. Record exact locators for full-text statements.

## 2. Paper-level gap mining

For every candidate limitation or opportunity create a Gap Ledger entry.

Distinguish:
- **author-stated limitation** — explicitly stated in limitations/discussion/future work;
- **observed limitation** — supported by actual results, errors or code behavior;
- **project inference** — a reasoned interpretation not directly claimed by the authors;
- **search absence** — no matching work found under recorded searches; never a certified gap.

For a claimed gap, answer:
1. What exact capability/condition is unresolved?
2. Which source and locator support that statement?
3. What did the source actually solve?
4. What assumption or measurement boundary creates the remaining limitation?
5. Which later papers cite/extend/challenge it?
6. Is the gap open, partially solved, solved, invalid, inaccessible, or unknown?
7. Why does the remaining part matter?
8. What extension mechanism is plausible?
9. What simpler alternative may already solve it?
10. What observation would make the extension unnecessary or false?

Do not convert every Future Work sentence into a research direction. Later literature, practical importance and feasibility must be checked.

## 3. Build a manuscript-ready Citation Corpus

Every paper likely to be used later should be saved once with reusable evidence:

- stable paper ID, DOI/arXiv/version;
- bibliographic metadata;
- access level and exact locator;
- role: background / foundational / closest work / gap evidence / mechanism / method precedent / benchmark / counterevidence / limitation;
- exact claim it can support;
- what it **cannot** support;
- short project paraphrase;
- related gap / hypothesis / experiment / manuscript claim IDs;
- citation status: verified identity / text checked / reusable / stale.

A citation corpus is not a pile of BibTeX. A paper enters the manuscript-ready pool only after identity and relevant text are checked. Re-read stale or version-changed sources before reuse.

## 4. Multi-angle validation

A promising direction should survive several different lenses. Use only applicable lenses and record disagreements.

| Lens | Question |
|---|---|
| Literature | Is the exact unresolved part supported by original and recent work? |
| Mentor/PI | Is the question important, sharp and capable of teaching something if negative? |
| Critic/reviewer | What is the strongest novelty, validity or interpretation attack? |
| Data | Does the available data contain the signal needed to answer the claim? |
| Measurement | Does the evaluator measure the construct rather than a convenient proxy? |
| Method | Does the proposed intervention instantiate the claimed mechanism? |
| Baseline | Could a simpler or equal-budget method explain the gain? |
| Statistics | Are unit, dependence, uncertainty and decision thresholds appropriate? |
| Resources | Can the decisive test be run with actual code/data/compute/budget? |
| Publication argument | If the result succeeds or fails, is there a bounded contribution that can be defended? |

Agreement between agents is not evidence by itself. The final decision cites the sources, data or experiments that caused the agreement.

## 5. Evidence-grounded mentor panel

When useful, derive mentor perspectives from public evidence rather than generic “professor personas.” A mentor profile may be based on a researcher, lab or research community and should distinguish:

- direct public evidence;
- recurring strong inference across multiple papers/years;
- speculative extension.

Extract repeated signals from representative papers: problem framing, contribution type, evaluation taste, favored baselines, failure analysis, methodological patterns, claim strength and unresolved boundaries. Never state that the profile reproduces a real person's private opinion or review decision.

Use multiple mentor profiles only when they contribute distinct lenses (for example measurement-first, systems-first, theory-first). The Supervisor synthesizes disagreement instead of voting by majority.

## 6. Feasibility and data-support gate

Before marking a direction testable, check:
- data availability, legal/ethical access and lineage;
- target label or ground-truth origin;
- whether the data contain the variable needed to distinguish hypotheses;
- train/dev/test family leakage and contamination;
- sample/experimental unit and dependence;
- evaluator implementation and validity;
- code/baseline availability;
- compute/API/cost budget;
- minimum discriminating experiment;
- explicit falsification and pivot rule.

A plausible idea with unsuitable data remains grounded/proposed, not testable. If the data can only establish association, do not write a causal research question.

## 7. Supervisor decision contract

At each major checkpoint produce one decision with evidence:

- **PROCEED** — gap remains, mechanism is distinct, decisive test is feasible.
- **SEARCH MORE** — specific missing literature could change novelty or mechanism judgment.
- **REPAIR MEASUREMENT** — current data/evaluator cannot answer the question.
- **NARROW** — evidence supports a smaller scope than the original claim.
- **PIVOT** — core assumption fails or another question has higher information value.
- **PARK** — worthwhile but blocked by a named resource/condition; store restart trigger.
- **STOP** — duplicate, invalid, infeasible, or low-information after recorded checks.

A failed direction is retained with the reason, sources and restart condition. Do not erase it and rediscover it later.

## 8. Scientist–Critic handoff

The Scientist hands the Critic:
- problem anchor;
- current Gap Ledger entries;
- closest-work matrix;
- Citation Corpus subset;
- data/measurement contract;
- experiment plan or actual result;
- explicit strongest current claim.

The Critic returns:
- strongest potentially fatal issue;
- evidence/location;
- alternative explanation;
- consequence for the claim;
- minimum repair/check;
- whether the issue changes novelty, feasibility, measurement, mechanism or only presentation.

The Supervisor then chooses the next action. Reviewer output does not directly mutate scientific status.

## 9. Persistence

Reuse Atlas paper, problem, hypothesis, experiment, claim and decision IDs. Gap and mentor/citation files are project working records linked to those IDs; do not create a disconnected literature database.

Recommended project files:
- `research-atlas/work/gap-ledger.md`
- `research-atlas/work/citation-corpus.md`
- `research-atlas/work/mentor-panel.md`

Use the templates in `assets/supervision/`. Store full bibliographic managers (BibTeX/Zotero/etc.) as additional views if desired, but keep the Atlas IDs and evidence locators as the shared key.
