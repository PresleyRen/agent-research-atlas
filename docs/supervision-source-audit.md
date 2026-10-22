# Supervision-loop source audit / 导师—研究员闭环来源审查

Date: **2026-10-22**. Candidate: **v1.2.0**.

This audit records four newly added public skill sources and the exact behaviors Agent Research Atlas adopts. The goal is not to import whole workflows; it is to close the loop from original literature to a feasible research direction, adversarial review, pivot decisions, and manuscript-reusable evidence.

## Sources

| Source | Pinned revision / file | Why it was selected | Adoption |
|---|---|---|---|
| K-Dense Scientific Agent Skills · research-lookup | `593377bb...` · blob `a337950...` | Large active skill library; manuscript-ready verified reference packets; support/contradict evidence and limitations/gaps | Partial protocol; no fixed paper quota or paid backend requirement |
| KalarisLabs research-agent-skills · autoresearch | `f73da6a...` · blob `a84d2d8...` | Literature bootstrap plus experiment inner loop / synthesis outer loop; explicit return to literature and pivot | Partial protocol; no “never stop” or unattended recurring execution |
| 45ck research-literature-review-skills · gap-finder | `235522d...` · blob `592591b...` | Traceable source→theme→gap output and explicit contradictions/weak-evidence surfacing | Partial protocol; Atlas adds later-work and feasibility verification |
| MentorForge · research-mentor-distiller | `14de3bc...` · blob `73a3430...` | Evidence-grounded mentor models distilled from public papers; direct/inferred/speculative evidence levels | Partial protocol; no impersonation or private-professor claims |

Repository popularity is context, not scientific evidence. At audit time K-Dense Scientific Agent Skills reported roughly 53.6k stars; the others were much smaller. Atlas adopts methods based on fit and inspectable behavior, not star count.

## What was missing in v1.1

v1.1 already had survey-first orientation, full-text extraction contracts, closest-work checking, hypotheses, feasibility, experiments, evidence audits and Supervisor-Skills. Four structural gaps remained:

1. **No first-class paper-level gap record.** Limitations could be written into problem/hypothesis notes, but there was no stable object for open/partial/solved/invalid gaps.
2. **No explicit supervisor–scientist–critic control loop.** Roles existed, but the main architecture did not force a direction decision after evidence/experiment review.
3. **No manuscript-ready citation corpus contract.** Paper nodes and claim evidence existed, but not a reusable “can support / cannot support / locator / writing role” sidecar.
4. **No evidence-grounded professor/lab lens.** Generic supervisor/reviewer roles existed, but not a disciplined way to derive mentor heuristics from repeated public research signals.

## Adopted behavior

### C29 · Research supervision
The Supervisor owns direction decisions, not execution. It asks for the decision-changing question, evidence sufficiency, data/measurement fit, strongest objection and cheapest next check. Decisions are `PROCEED / SEARCH MORE / REPAIR MEASUREMENT / NARROW / PIVOT / PARK / STOP`.

Mentor profiles may be derived from public papers, talks and lab materials, but must distinguish direct evidence, recurring inference and speculative extension. Agreement among mentor agents is not a truth signal.

### C30 · Paper-level gap mining
Atlas now supports `gap` nodes. A gap records one of four provenance kinds: `author_stated_limitation`, `observed_limitation`, `project_inference`, or `search_absence`. Reviewed gaps can become `open`, `partially_solved`, `solved`, `invalid_gap`, `inaccessible`, `unknown` or `parked`.

Author-stated/observed gaps need paper/experiment evidence. Partially solved gaps require later-paper references. Solved/invalid gaps require a resolution record. This prevents a Future Work sentence or empty search from silently becoming an “innovation”.

### C31 · Manuscript-ready citation corpus
Each reusable source stores identity, version, actual read locator, manuscript role, the exact claim it can support, what it cannot support, project paraphrase and linked Atlas IDs. This is complementary to paper nodes and external bibliography managers; it does not create a second literature database.

### C32 · Scientist–Critic adaptive loop
The Scientist executes the assigned search/read/experiment task; the Critic attacks nearest-work, data, measurement, baseline and interpretation; the Supervisor selects the next action. Failed directions remain in the atlas with restart conditions. Surprising results can return the project to literature rather than forcing another random experiment.

## Conflicts retained and rejected

- **CF29:** retain inner/outer-loop reflection; reject autonomous “never stop” behavior.
- **CF30:** retain survey/foundational/influence/frontier/critical anchors; reject high citation, Future Work language or zero search hits as gap proof.
- **CF31:** retain evidence-grounded mentor heuristics; reject professor impersonation or majority-vote scientific verdicts.
- **CF32:** retain verified reusable reference packets; reject DOI existence or bibliography size as claim support.

## Verification scope

Deterministic tests check:
- grounded gap nodes and invalid ungrounded gap rejection;
- partially solved gaps cannot omit later papers;
- Supervisor decision vocabulary exists;
- loop contains Scientist/Critic/Supervisor and pivot-to-literature behavior;
- citation corpus requires both support and non-support fields;
- mentor panel retains evidence levels;
- registry contains 32 capabilities, 81 sources, 312 features and 32 conflict contracts.

These tests verify state/contract behavior. They do not validate scientific novelty, actual professor judgment, literature completeness, model results or publication success.
