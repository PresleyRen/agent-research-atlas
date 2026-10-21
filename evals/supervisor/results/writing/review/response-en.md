# Response to Reviewers

We thank the reviewers for identifying inaccuracies and limitations in the draft. We have revised the Introduction and Methods to match the supplied synthetic pilot record, clarified the shared version-state design, and preserved the distinction between an observed association and a causal claim. All section references below refer to the revised document, *Version-Aware Routing for Versioned Document Requests: A Synthetic Exploratory Pilot*. The revisions involve writing and checks of the supplied aggregate values; no additional experiment has been completed.

## R1.1

> The main accuracy in the draft does not agree with the result artifact. Please correct it and make the comparison population clear.

**Response.** We agree that the original accuracy was incorrect. We have replaced 96% with the value in the result artifact: 50 of 64 cases, or 78.125%, for the version-aware policy. The baseline was recorded as correct on 44 of 64 cases, or 68.75%. The absolute difference is therefore 9.375 percentage points. These values now appear together in Introduction, paragraph 3; Methods §2.5 explains the calculation and reporting convention.

We have also corrected the comparison population. The supplied record contains one hand-authored synthetic pilot set with 64 cases in eight case families, not three real business datasets. Introduction, paragraph 3, and Methods §2.1 now state this scope explicitly. Methods §2.4 explains that both reported rates use the stated denominator of 64, while the aggregate artifact does not supply case identifiers or paired outcomes for a case-by-case alignment check. We make no claim that these counts describe production performance.

## R1.2

> There appear to be only eight independent case families. What evidence supports the broad generalization and causal claim?

**Response.** The available evidence does not support either claim, and we have removed them. The artifact records eight case families, but it does not establish independence among those families or provide individual family membership and outcomes. We therefore do not treat the 64 cases as 64 independent replications. Methods §2.6 now makes both the within-family concern and the unresolved independence between families explicit.

The revised Introduction limits the observation to the supplied synthetic record and describes the higher recorded success rate as an association. Methods §§2.5–2.6 explain why the aggregate counts cannot identify which cases improved, estimate uncertainty while accounting for family structure, or isolate clarification from filtering and other policy differences. We have removed the claims that the method solves intent understanding for all document agents, generalizes across real business datasets, and shows that clarification necessarily improves reasoning. No confidence interval, significance test, or causal effect estimate has been added. Establishing broader applicability or a mechanism would require evidence beyond this record, including independent evaluation material and a comparison designed to distinguish the proposed explanation from alternatives.

## R2.1

> Please add two larger models under equal latency budgets, and explain whether the study was preregistered.

**Response.** The requested comparison has not been completed. The supplied result artifact marks a new-model comparison as planned and latency as not measured. The current revision uses the available offline materials; it contains no new model results and no equal-latency comparison. This part of the request therefore remains unresolved. We have revised Methods §2.4 to state the missing comparison directly and to remove any implication that the policy has demonstrated an efficiency advantage. We also state that a retrieval call and a clarification turn cannot be assumed to have equal latency.

A future comparison would need to identify the two models and their versions, define the latency budget and treatment of clarification time, and measure all conditions using a common protocol. That comparison is a proposed next step, not a completed addition to the paper.

The comparison was not preregistered. The method note states that it was planned after inspection of the synthetic cases. We now describe it as exploratory in Introduction, paragraph 4, and Methods §2.1. We have not retrospectively characterized this process as a prospective or confirmatory study. The resulting claims are limited to the descriptive association in the supplied record.

## R2.2

> The shared version-state module handles two challenges. The current structure obscures how the design works; please clarify this relationship and retain useful limitations.

**Response.** We have reorganized the method description around the shared version state. Methods §2.3 explains that the router and document filter use the same state for two related purposes: applying explicit version constraints to document eligibility and informing the clarification decision when a version preference is implicit. An explicit constraint is handled by a deterministic filter, while a targeted clarification is permitted only when a user response could change the answer. We identify the pilot as rule-based rather than describing the gate as learned.

This revision makes the shared design relationship explicit without inventing a separate module for each challenge or attributing the recorded difference to either role independently. Introduction, paragraph 2, gives the corresponding concise overview. We have retained the material limitations: incomplete implementation details in §2.3, unmeasured and unmatched latency in §2.4, missing scoring and case-level records in §2.5, and dependence, causal ambiguity, and the unverified implementation of the evaluator-only label boundary in §2.6. The revised structure therefore clarifies what the design specifies and where the supplied evidence remains incomplete.

## R3.1

> Please improve English flow without changing the original association claim.

**Response.** We have improved the sentence flow while preserving the wording “was associated with a higher success rate.” The language-only revision reads: “Across the evaluated examples, the version-aware policy was associated with a higher success rate.” In Introduction, paragraph 3, we use the more specific sentence “Within this record, the version-aware policy was associated with a higher success rate” so that the scope matches the supplied artifact. Neither revision changes the claim into a causal statement or asserts statistical significance.

The original phrase “in descending order” is grammatical and has been retained in the separate language-edit passage. Because the supplied materials contain no failure-category list or category counts, we have not added a failure-category statement or table to the manuscript. This separates the requested wording edit from an unsupported empirical addition.
