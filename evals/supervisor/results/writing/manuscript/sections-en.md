# Version-Aware Routing for Versioned Document Requests: A Synthetic Exploratory Pilot

## 1. Introduction

For a document agent handling a version-specific request, selecting relevant content also requires identifying the version that the user intends. An explicit version requirement constrains which documents are eligible, whereas an implicit preference may leave the appropriate version unresolved. These situations motivate different responses: an explicit constraint can guide document filtering, while uncertainty about a preference may justify a clarification when the user's response could change the answer. The question considered here is how a routing policy can coordinate these decisions within a single version-aware representation.

We describe a rule-based policy that selects among answering, retrieving one additional passage, and asking one targeted clarification. The policy uses the initial message, supplied context, and document snippets with version metadata. Explicit version constraints are handled by a deterministic filter, and clarification is restricted to cases in which a user response could change the answer. The router and document filter share a version state. This arrangement connects evidence selection and clarification within the same design, rather than assigning each difficulty to an independent module. The comparison baseline retrieves once and then answers without clarification.

The supplied synthetic record reports an exploratory comparison on 64 hand-authored cases spanning eight case families. The version-aware policy was recorded as correct on 50 cases (78.125%), compared with 44 cases (68.75%) for the baseline, an absolute difference of 9.375 percentage points. Within this record, the version-aware policy was associated with a higher success rate. These counts describe the supplied fictional pilot artifact; they do not represent a newly executed study or validation on real business datasets.

The contribution of this account is a bounded description of the routing design and its recorded comparison. The comparison was planned after the synthetic cases had been inspected and was not preregistered. The available materials provide no uncertainty analysis, independent replication, causal mechanism study, or measured latency comparison. The aggregate difference therefore does not establish that clarification causes better reasoning, that the policy generalizes to other document agents, or that it is superior under matched latency budgets.

## 2. Methods

### 2.1. Record provenance and study scope

The source materials comprise a method specification, a draft description, and an aggregate result artifact supplied for an offline writing exercise. The artifact is explicitly synthetic and describes an exploratory comparison on one hand-authored pilot set containing 64 cases in eight case families. It does not include a production workload or three real-world datasets. According to the method specification, the exploratory comparison was planned after inspection of the synthetic cases. No preregistration or independent replication is documented, and no new experiment was performed for this revision.

### 2.2. Permitted inputs and actions

The documented policy receives the initial user message, supplied context, and document snippets carrying version metadata. Hidden reference labels are reserved for the evaluator and are excluded from the specified policy inputs. The available actions are to answer, retrieve one additional passage, or ask one targeted clarification. These are the actions described in the source specification; the provided materials do not define a complete multi-step execution protocol.

### 2.3. Routing logic and shared version state

The pilot uses a rule-based routing policy rather than a learned gate. When the request contains an explicit version constraint, that constraint is passed to a deterministic version filter. For an implicit preference, rules determine whether clarification is appropriate. Clarification is limited to cases in which a response from the user could change the answer; uncertainty alone is not the stated criterion for asking a question.

The router and document filter use a shared version state. The filter uses the explicit constraint to restrict document eligibility, while the routing rules use version-related uncertainty to assess whether a targeted clarification is relevant. The shared state thus serves two related design roles: maintaining consistency with explicit version requirements and supporting the decision to clarify an unresolved preference. This is a description of the documented design relationship, not evidence that either role independently accounts for the aggregate difference.

The materials do not specify the state schema, exact decision rules, rule precedence, handling of conflicting or missing version metadata, or behavior after an unanswered clarification. They also do not specify a default version. These details remain necessary for an executable reconstruction of the policy.

### 2.4. Baseline and comparison conditions

The baseline retrieves once and answers without clarification. Both reported accuracies use the same stated denominator of 64 cases in the supplied pilot record. The available aggregate artifact does not contain case identifiers or paired outcomes with which to verify case-by-case alignment. It also does not document model identities, prompts, retrieval implementation, hardware, or execution settings.

Latency was not measured, and the conditions were not compared under matched measured latency budgets. A retrieval call and a clarification turn cannot be assumed to have the same latency. Accordingly, the reported accuracy comparison is descriptive and does not support an efficiency claim. Comparisons with two larger models under equal latency budgets remain uncompleted; the artifact records a new-model comparison only as planned.

### 2.5. Outcome reporting and arithmetic

The reported outcome is accuracy, calculated as the number of cases recorded as correct divided by the stated total of 64. Percentages are obtained by multiplying the resulting proportions by 100. The absolute difference in percentage points is calculated as 100 times the version-aware accuracy minus 100 times the baseline accuracy. This reporting convention preserves the exact proportions in the source artifact and avoids confusing a percentage-point difference with a relative percentage change.

Only aggregate counts and accuracies are available. The source materials do not provide the correctness rubric, annotation or adjudication process, case-level predictions, family membership for individual cases, or failure-category counts. Consequently, this revision verifies the transcription and arithmetic of the supplied values but cannot independently rescore the cases, identify which cases improved or regressed, or validate the evaluator's decisions.

### 2.6. Dependence, uncertainty, and interpretation

The 64 cases belong to eight recorded families and cannot be assumed to constitute 64 independent replications. Independence between families has not been established either. No uncertainty analysis is reported, and the aggregate counts alone do not identify the pairing of outcomes or their distribution across families. We therefore report no confidence interval, significance test, or causal effect estimate. An analysis that accounts for family structure would require the corresponding case-level records and a justified treatment of dependence.

The comparison also does not isolate clarification from filtering, additional information, or other differences between the policies. It cannot attribute the recorded association to a specific component or establish an improvement in general reasoning ability. The documented input boundary for hidden reference labels is a design requirement; without execution traces or evaluator code, its implementation cannot be audited from these materials. These limits constrain the account to the stated synthetic record and the documented method, rather than a fully reproducible empirical validation.
