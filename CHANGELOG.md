# Changelog

## 1.3.0 — 2026-10-23

### Executable evidence cycle and real-source validation

- Add `research_cycle.py` for real Crossref/ACL metadata, official ACL PDF extraction, author-stated limitation candidates, citation/BibTeX evidence (ACL as `@inproceedings`), source and extracted-text checksums, evidence-limited Supervisor decisions, and bounded project queues.
- Add `fetch_beir.py` for checksum-pinned official BEIR SciFact ZIP retrieval, safe extraction and stable provenance.
- Add `retrieval_benchmark.py` for full BEIR relevance evaluation: 5,183 documents, 300 official held-out test queries, two declared BM25 variants, Recall/MRR/nDCG, complete ranked IDs, source hashes, paired bootstrap and data/claim measurement gates.
- Add a live network-and-PDF acceptance workflow, archived raw artifacts, real-literature/citation project examples, and 4 additional test files plus integration.
- Preserve two original live PDF failures, correct two-column interleaving and wrapped heading detection, and rerun against the authentic 14-page ACL document; now extracts four candidate limitations on page 9.
- Preserve the real outcome: baseline nDCG@10 0.664451 vs title-weighted 0.672688, paired interval [-0.003330, +0.019695], interpreted **INCONCLUSIVE** rather than claiming publication-level improvement. Independently verify 1,800 metric values.
- Record both original-PDF SHA256 and extracted-text SHA256 because source PDFs were binary-different but extracted to identical text. Distinguish test-set exploration from independent confirmation.
- Extend existing C03/C04/C05/C11/C13/C16/C22/C29/C30/C31/C32 capability owner locations and tests without inflating the capability count. Keep the optional provider inventory and Supervisor roles.

## 1.2.0 — 2026-10-22

### Supervisor–Scientist research loop

- Add C29–C32: evidence-grounded research supervision, paper-level gap mining, manuscript-ready citation corpus, and Scientist–Critic adaptive research loops.
- Add a Research Supervision workbench plus Gap Ledger, Citation Corpus and Mentor Panel templates. Supervisor decisions explicitly support proceed, search-more, repair-measurement, narrow, pivot, park and stop.
- Add first-class `gap` atlas nodes with provenance kinds and candidate/open/partially-solved/solved/invalid/inaccessible/unknown/parked states. Source-grounded gaps require paper/experiment evidence; partial/solved states require later/resolution records.
- Add unresolved-gap diagnosis to `audit.py project`, so continued projects surface research-direction work rather than silently treating a map as complete.

### New source integrations

- Add K-Dense `research-lookup` for manuscript-ready evidence packets and claim-support boundaries.
- Add KalarisLabs `autoresearch` for literature/experiment inner loops, synthesis outer loops and evidence-driven pivots; explicitly reject its unbounded “never stop” behavior.
- Add 45ck `gap-finder` for source→theme→gap traceability and explicit weak/contradictory evidence.
- Add MentorForge `research-mentor-distiller` for evidence-grounded professor/lab methodology lenses, while rejecting impersonation or majority-vote scientific truth.
- Expand the maintained registry to 81 sources, 312 source features, 32 capabilities and 32 conflict contracts.

### Validation

- Add gap-state tests plus supervision/citation/mentor contract tests and eight real-publication claim/gap checks; deterministic suite target becomes 109 tests.
- Document the new source reading scope, adopted/rejected behaviors, and extension routes. Fix bilingual Supervisor evidence assertion and disable GitHub Actions matrix fail-fast so failures are visible per Python version. No upstream paid search backend, recurring autonomous loop or real professor distillation runtime is claimed as executed.

## 1.1.0 — 2026-10-21

### Coverage and maintainability

- Audit 77 named source entries and 296 distinctive features; identify 28 capabilities and 28 conflict contracts with exact implementation/test locations, complement links, limitations and repair routes.
- Expand the read scope to 48 named SKILL.md bodies, the nine Anthropic problem-selection modules, and all 70 Supervisor Markdown references plus 18 Chinese handbook chapters; preserve pinned revisions and distinguish host protocols, local implementation, optional integrations and intentionally rejected rules.
- Add `audit.py coverage`, `locate`, `project` and `check --repo` for read-only capability lookup, recorded project gaps and extension-reference validation.
- Document all 28 capabilities, explicit text workflow maps, source complementarity and practical extension examples in the Chinese/English READMEs and audit guides.

### Supervisor-Skills integration

- Add three adapted workbenches and five project templates for research advising, benchmark/evaluation design, manuscript drafting and bilingual polish, submission review, reviewer responses, scientific figures and editable reconstruction.
- Map all 12 Supervisor skills and 74 distinctive features at pinned commit a20d76e. Record source reading manifests, original review proposals and final adoption decisions.
- Add C25–C28 and CF21–CF28; preserve flexible contribution routes, valid negative-result interpretation, clean prose plus separate evidence, concern-based replies and data-faithful figures.
- Keep the Atlas core MIT license and separately mark Supervisor-derived methods/templates CC BY-NC-SA 4.0 with attribution. No upstream drawing runtime is vendored.
- Rewrite both READMEs around capabilities, practical deliverables, the full text workflow and symptom-to-owner extension routes.

### Research correctness and conflict fixes

- Add a JSON Pointer numerical ledger audit with source hashes, explicit tolerances, distinct missing/unparseable/mismatch statuses and precise integer comparison.
- Freeze declared input hashes; allow explicitly mutable candidate files while detecting immutable evaluator/data drift before and after execution. Keep legacy freezes labelled `legacy_unpinned`.
- Add dependency impact and persistent pending-review queues, including experiment/hypothesis coupling, changed/removed evidence links, cyclic graphs and explicit review resolutions. Show pending warnings in all generated map views.
- Strengthen problem selection, strategy choice, problem/method anchors, implementation fidelity, statistical-design limits, occurrence-level claim/citation audits and negative-result continuation.
- Correct strict schema-version checks for atlas/freeze/attempt/final records and reject malformed maintenance triggers before writes.

### Validation

- Expand the deterministic suite from 60 to 94 tests, including independent integration review and specific before-fix failures.
- Add reusable synthetic fixtures and three independent-context evidence, retrieval-continuation and method-selection tasks. Record their observations separately from upstream service integration and scientific validity.
- Add three Supervisor project tasks for discovery/benchmark, writing/review, and figures/reconstruction, plus a focused five-scenario interval interpretation task; archive actual outputs and remaining runtime checks separately.
- Preserve an independently detected interval-direction defect and its repair: distinguish bounds above/below/across a practical threshold, negative effects and exact equality; update protocol dependencies without inventing empirical results.
- Extend CI to compile all three scripts and validate registry paths, symbols, capabilities and references on Python 3.10, 3.12 and 3.13.

## 1.0.0 — 2026-10-20

- Add a bilingual Agent research workflow from literature maps to falsifiable hypotheses, experiments and evidence-backed manuscript claims.
- Add fourteen extensible seed domains and Chinese/English terminology.
- Add local atlas discovery/adoption, stable graph IDs, incremental updates, revision checks, history and preserved human notes.
- Generate Markdown/Mermaid views and an offline interactive HTML map.
- Add frozen experiment plans, bounded local execution, imported results, failure records and integrity verification.
- Include methodology references, provenance audit, reproducible tests and clearly labelled synthetic examples.
- Document search, interpretation, local security, resource and publication limitations.
