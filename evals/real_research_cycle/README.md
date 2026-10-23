# Real academic source → gap → claim → limited decision checks

**Observed test date:** 2026-10-22. This folder contains small, attributed, **actual-publication** and **official-dataset-documentation** examples; it does not contain fabricated scientific results. Local regression details and live CI are in `docs/v1.3-validation.md`.

## Public original sources

- Hsieh et al. (ACL Findings 2024), [*Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization*](https://aclanthology.org/2024.findings-acl.890/), DOI: `10.18653/v1/2024.findings-acl.890`. We read the actual PDF's **Limitations on PDF page 9 (printed page 14990)**, and retain four author-stated concerns: simplifying the mechanism; computational overhead O(K) forward passes; circumstances in which positional bias is helpful; and the still unclear root cause. See `papers/hsieh_2024_excerpts.txt` (short, attributed excerpts) and `leads_hsieh.json` (candidates, not verified open gaps).
- Cuconasu et al. (EMNLP 2025), [*Do RAG Systems Really Suffer From Positional Bias?*](https://aclanthology.org/2025.emnlp-main.1422/), DOI: `10.18653/v1/2025.emnlp-main.1422`. Abstract/conclusion excerpts challenge universal claims that reordering is necessarily useful in realistic RAG retrieval scenarios. A contrary paper is not sufficient to prove the original controlled finding invalid; it narrows the correct claim.
- Official [SciFact documentation](https://github.com/allenai/scifact/blob/master/doc/data.md) and [BEIR benchmark documentation](https://github.com/beir-cellar/beir). Claim #123 is contradicted by evidence doc `4883040`, while claim #263's cited doc `14853989` is *not annotated* as supporting/refuting evidence, although other cited docs have CONTRADICT annotations. This distinguishes paper citation from supporting evidence.

## Observed local outputs

| Artifact | Real observation | Scientific interpretation |
|---|---|---|
| `leads_hsieh.json` | Four distinct limitation candidates, each with PDF page locator | Neither model novelty nor a verified open gap is established |
| `atlas-upsert-hsieh.json` | One real-paper Atlas node and four first-class candidate gap nodes | Can import to native Atlas; old three-lead version retained in `history/` |
| `manuscript/citation-hsieh.json` and `.bib` | Exact excerpt and input SHA256, DOI and original author metadata, can/cannot support boundaries | Manuscript reference packet, not broad factual certification |
| `project/research-atlas/supervision/decision-0001.json` | Contradictory 2025 evidence triggers **PIVOT** from universal reordering claim | A negative decision, not a new publishable direction |
| `.../decision-0002.json` | Narrower hypothesis triggers **REPAIR_MEASUREMENT** | Additional generation/latency measurements still required |
| `scifact_smoke/polarity_results.json` | One false SUPPORT versus annotated CONTRADICT is detected; another assertion is correct; a cited paper without annotated rationale remains unresolved | Annotation-consistency demonstration only |
| `scifact_smoke/` | One official *documented* labeled query in a small mixed corpus | Real evidence example, **not** a scientific retrieval performance evaluation or complete SciFact corpus |

## Genuine errors uncovered, retained and fixed

1. First section extractor emitted duplicate overlapping limitation windows. It was revised to separate paragraphs/headings.
2. Its first reviewed excerpt captured only three limitation topics. The **original official PDF actually lists four**. The source fixture and extractor were corrected; previous outputs remain in `history/`.
3. First Supervisor decision implementation prioritized missing data instead of a stronger documented contrary mechanism; the blocking critic evidence now triggers PIVOT before implementation.
4. A real SciFact documented statement about antiretroviral therapy had its evidence polarity inverted by an intentionally wrong assertion. The audit detected contradiction rather than calling the cited study supportive.
5. A single qrel-positive question yielded perfect top-k retrieval for both variants in the smoke corpus, but the evaluator correctly reports **insufficient independent query units** instead of claiming success.

The actual **complete** BEIR SciFact archive contains ~5K scientific abstracts and **300 test queries** and is downloaded by a separate versioned integration test; only those network-enabled outputs qualify as full retrieval benchmark results. We do not claim any position-bias LLM generation experiment, time-to-solve metric, professor validation or journal acceptance.

## Repeat tests

```bash
python -m unittest discover -s tests -v
python tests/live_real_research_case.py --output-dir /tmp/atlas-real-scifact
```

The second command requires external network access plus `pdftotext`; normal offline unit tests don't. Preserve the resulting files and their hashes; if the official archive cannot be fetched or its checksum changes, the live test must fail visibly.
