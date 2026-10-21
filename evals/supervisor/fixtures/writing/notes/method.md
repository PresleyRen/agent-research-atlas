# Method v0.1

Input: initial message, supplied context and document snippets with version metadata. Hidden reference labels are evaluator-only.
Actions: answer; retrieve one additional passage; or ask one targeted clarification.
Explicit version constraints pass through a deterministic version filter; clarification is limited to cases where a user response could change the answer. This was a rule-based pilot, not a learned gate.
The baseline retrieves once and answers without clarification. The two conditions did not have matched measured latency; no production workload was used.
An exploratory comparison was planned after inspecting the synthetic cases. No preregistration, independent replication, uncertainty analysis or causal mechanism study has been completed.
