# Existing local pilot note

This is a fictional measurement note for the skill trial, not scientific evidence.
A simple baseline obtains 62/64 correct and the proposed clarification router 51/64 on a debug set. Colleague suggestion: because the simple method wins, abandon the entire research problem immediately.

Baseline reads `row["reference_intent"]` before choosing a route. That field is populated by the dataset annotator after all user context is known. Router receives only the initial user message and document snippets. This was convenient during debugging. No comparable held-out experiment has been run.

The 64 debug rows are paraphrases of 8 case families; case relatives currently occur on both sides of an informal train/test split. No latency or financial cost was measured.
