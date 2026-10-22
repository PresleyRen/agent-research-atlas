# Real-source literature decision test (2026-10-22)

This fixture is built from **five identified research publications**, not invented bibliographic entries or model-generated benchmark measurements. The initial search and source reading were performed against official ACL Anthology records and, for Liu et al. (2024), the MIT Press full-text HTML. The checked research area is the use and ordering of retrieved evidence in long-context Agent/RAG applications.

## Verified primary sources

| Source | Original record and DOI | Actually read | Evidence use |
|---|---|---|---|
| Liu et al. (2024), *Lost in the Middle* | https://aclanthology.org/2024.tacl-1.9/ · `10.1162/tacl_a_00638` | publisher HTML full text, §§2.3/5 and conclusion | Positional effects in specifically tested multi-document and key-value tasks |
| Hsieh et al. (2024), *Found in the middle* | https://aclanthology.org/2024.findings-acl.890/ · `10.18653/v1/2024.findings-acl.890` | official abstract | A published mitigation; exact replication claim requires full text |
| Yu et al. (2025), *Mitigate Position Bias…* | https://aclanthology.org/2025.findings-acl.316/ · `10.18653/v1/2025.findings-acl.316` | official abstract | Another published mitigation in reported benchmark settings |
| Cuconasu et al. (2025), *Do RAG Systems Really Suffer…* | https://aclanthology.org/2025.emnlp-main.1422/ · `10.18653/v1/2025.emnlp-main.1422` | official abstract | Counterevidence to universalizing controlled position bias to all realistic retrieval pipelines |
| Du et al. (2025), *Context Length Alone Hurts…* | https://aclanthology.org/2025.findings-emnlp.1264/ · `10.18653/v1/2025.findings-emnlp.1264` | official abstract | Alternative mechanism: long input harms performance despite perfect retrieval in their experiments |

### Supervisor decision

1. Observed positional sensitivity is grounded in the first paper's tested conditions.
2. The claim “no mitigation exists” is contradicted by later published papers.
3. The claim “positional bias always dominates real-world RAG” is too broad given Cuconasu et al.'s contrasting 2025 study.
4. The claim “perfect retrieval guarantees reliable long-context answers” is contradicted by Du et al.'s reported experiments.
5. A new architecture combining routing and context placement has **not** been established as novel or feasible; no project-specific data, evaluator, compute or budget was supplied. The appropriate action is `SEARCH_MORE`, not `PROCEED` to implementation.

The source sample is deliberately limited and should **not** be presented as an exhaustive literature review, a live replication, a real Agent-inference experiment, or a proof of an unaddressed research gap. These are evidence-and-decision tests on *real publication records*; they guard against fabricated citations, false novelty, overbroad claims and premature feasibility promotion.

## Repeat the deterministic checks

```bash
python -m unittest discover -s tests -p 'test_real_literature.py' -v
```

See `agent_rag_position_bias.json` for source-level support and non-support sentences, claim decisions and bounded gap record. No full paper text or long copyrighted passages are distributed with this fixture.
