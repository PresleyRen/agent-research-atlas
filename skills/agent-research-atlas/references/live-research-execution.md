# Research evidence execution / 真实文献与实验执行

**What this adds.** The Atlas supervisor/Scientist/Critic methodology can now use three standalone Python 3.10+ standard-library tools. They produce machine-readable receipts (source URL/hash/page, research decisions, dataset hashes, run metrics) for the existing Atlas. They do not replace an LLM or human for causal reasoning and do not claim novelty or publication acceptance.

## Research loop: research_cycle.py

```text
Supervisor selects one decision-changing question
    -> Scientist queries Crossref (metadata, Chinese or English terms)
    -> Scientist verifies ACL Anthology paper identity and PDF source
    -> pdftotext extracts PDF pages, section-specific candidate limitations
    -> Citation entry records actual source passage + page / DOI + BibTeX
    -> Scientist checks follow-up and contradictory work; Critic records finding
    -> Supervisor records SEARCH_MORE / REPAIR_MEASUREMENT / NARROW /
       PIVOT / PARK / STOP / PROCEED (pilot only)
    -> remaining gap/claim appended to persistent Atlas, prior decisions retained
    -> loop can resume with a bounded next task, not an unattended timer
```

Start from an **existing project root**; never write into installed Skill files. Example invocations from repo root:

```bash
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project query \
  --topic 'RAG long context positional bias' --limit 12 --output work/crossref.json
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project acl \
  --url 'https://aclanthology.org/2024.findings-acl.890/' --output work/hsieh-metadata.json
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project read \
  --paper 'https://aclanthology.org/2024.findings-acl.890.pdf' \
  --id doi:10.18653/v1/2024.findings-acl.890 --output work/hsieh-gaps.json
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project queue \
  --file research-queue.json
```

Citation extraction, export and SciFact polarity audit are CLI subcommands; call `--help` for their argument schema. Full-text PDF extraction requires the system's `pdftotext` executable, supplied by Poppler. If the extractor misses a section, compare page text to the actual PDF and save the corrected source; **never silently certify all limitations were extracted**. Search output is Crossref metadata, not proof that a research gap exists.

The bounded `queue` consumes a task list with **already supplied proposal and critic/supervisor review records**; it does not automatically create independent neural agents, search all neighboring papers, or infer a professor's private opinions. The LLM-equipped host should produce those review records with cited original sources. The code prevents a branch with missing reviews, missing measurements or blocking counterevidence from becoming an approved pilot.

## Real labeled retrieval evaluation: retrieval_benchmark.py

The evaluator reads official BEIR-format `corpus.jsonl`, `queries.jsonl`, and `qrels/test.tsv`. It runs two predetermined, simple BM25 tokenization variants: normal title (`x1`) versus title weighted twice (`x2`), retaining **all** per-query predictions and corpus/query/qrels SHA256. All 300 positive-labeled SciFact test queries are scored if the complete published archive is available.

```bash
python skills/agent-research-atlas/scripts/fetch_beir.py --dest /path/to/scifact-snapshot
python skills/agent-research-atlas/scripts/retrieval_benchmark.py \
  --data-dir /path/to/scifact-snapshot/scifact --split test --k 10 \
  --output /path/to/project/research-atlas/experiments/scifact-bm25.json
```

Run `fetch_beir.py` with an explicit data snapshot destination; it verifies the BEIR-published archive MD5 before extracting and hashes the downloaded archive, rejecting unsafe ZIP entries. The results include Recall@10, MRR@10, nDCG@10 and 95% paired-query bootstrap **exploratory** intervals. Query count less than 20 returns `INSUFFICIENT_QUERY_UNITS` rather than a false significant improvement. Variation is restricted to the stated title weighting; no qrels are read during ranking. The score cannot justify claims about generation accuracy, latent attention, causal position bias, or long-term agent planning.

## Source reproducibility: raw PDF and extracted text

A source reader stores *both* the original publisher PDF SHA256 and a separate SHA256 of the raw-order extracted text, plus the extraction method. The two authentic requests for the same Hsieh et al. paper produced different binary PDF hashes, yet `pdftotext -raw` yielded exactly identical textual output with SHA256 `01fbf8c15c880f983286852cbc0e7504a61f1f191a198a537b48d3d3f86c2ce1`. This distinction prevents a PDF binary packaging difference from being misreported as a research-content change. The journal/conference identity, DOI, page locator and read-depth remain independent checks.

Use the `Research Supervisor` decision on **real outcomes**: nDCG@10 can rise while the paired-query interval still crosses zero. Such a result is `INCONCLUSIVE`, not evidence for a proven method improvement or automatic clearance to claim SCI novelty. Preserve every failure, data provenance, baseline and exclusion decision.

## Actual study evidence and limits

- [`evals/real_research_cycle`](../../../evals/real_research_cycle/README.md) uses short, hand-verified excerpts of actual Hsieh et al. ACL 2024 Limitations (four distinct topics), a later EMNLP 2025 counter-paper, and SciFact's published sample label relations. The first extraction omitted a fourth limitation; the old version is retained for regression.
- [`tests/live_real_research_case.py`](../../../tests/live_real_research_case.py) downloads the full official SciFact ZIP and two official ACL records in network-enabled CI, then saves real measured metrics and source hashes as a downloadable Actions artifact. `evals/real_research_cycle` snippets are **not** the full SciFact benchmark.
- `python -m unittest discover -s tests -v` checks deterministic behavior on supported Python versions and Atlas integration when the whole repository is installed. **Passing tests does not establish the new hypothesis is scientifically correct or independently discovered.**

### Data/claim support gate

A feasibility check distinguishes the actual measured construct, ground-truth provenance, dataset hash and model access. A SciFact qrel can confirm **document retrieval relevance**, not a claim that a long-context LLM understood the evidence or answered it correctly. Without datasets and evaluation appropriate to the mechanism, supervisor decisions remain `SEARCH_MORE` or `REPAIR_MEASUREMENT`; no `testable` upgrade.

### Provider coverage

Crossref metadata and ACL Anthology full texts are concrete read-only retrieval paths. OpenAlex, Semantic Scholar, CNKI, Elicit, Scite and other previously documented services remain optional host integrations; do not describe those as authenticated or exhaustively tested. The current tools do not implement a general paper search service or full-paper semantic extraction for every publisher.


## Connected, resumable research sessions

`research_session.py` connects bounded discovery, original-paper reading, citation export, separately authored review, a measurement gate, actual retrieval execution and follow-up decisions. A host selects papers and supplies Scientist, Critic and Supervisor reasoning; it is not an unattended neural-agent service.

```text
Crossref discovery → explicit paper selection → ACL full text + candidate limitations
    → reusable citations/BibTeX + source hashes → Scientist proposal
    → independently authored Critic + Supervisor reviews bound to exact packet
    → measurement mismatch: REPAIR_MEASUREMENT → revised proposal (history retained)
    → PROCEED → actual frozen retrieval pilot → outcome → SEARCH_MORE
    → fresh review and another bounded proposal, or park the research direction
```

From an existing project directory, use `--root PROJECT` and these subcommands:
- `discover --topic TOPIC --paper-urls URL [URL ...]`: retain up to five explicitly selected full texts, search provenance and citation packets.
- `prepare --proposal proposal.json --evidence FILE [FILE ...] --scientist-id ID`: freeze a proposal and evidence packet.
- `review --file review.json`: accept a Critic or Supervisor record citing packet evidence and its exact `packet_sha256`.
- `decide`: persist the gate, including measurement repair and literature follow-up.
- `experiment --data-dir DATA`: execute the supported frozen BM25 title-weight pilot only after PROCEED and matching data hashes.
- `search-more --topic TOPIC`: execute a new bounded public metadata search after SEARCH_MORE; bind its receipt to the next proposal.
- `status`: revalidate event-chain and referenced evidence hashes before showing history.

Review records identify `role`, `reviewer_id`, `proposal_id`, `packet_sha256`, `finding`, `evidence_locator`, `evidence_paths`, `severity`, and any `failure_type`/`resolved`. Distinct reviewer IDs prevent accidental self-review; the host must actually use independent contexts and record their provenance. IDs alone do not prove scientific independence.

The supported benchmark measures retrieval relevance only. Its executable measurement gate rejects attention/answer-generation claims. A revised proposal uses a new ID; previous evidence and decisions remain immutable. An inconclusive pilot schedules fresh review rather than manufacturing a positive claim. Previously inspected test data remain exploratory; the runner cannot attest preregistration chronology.

Recovery: fresh status validates all referenced files; an interruption after a result is saved accepts only an identical orphan result, and an experiment event awaiting its final decision resumes without rerunning it. A partial discovery preserves a failure receipt and requires inspection rather than silently overwriting prior evidence.

### Session integrity and compatibility

Each new event includes a digest of its own canonical contents, including the final event; the previous-event hash also checks event ordering. Experiment eligibility is recomputed from the snapshotted proposal, distinct reviews and current data contract immediately before execution, including interrupted-run recovery. A saved `PROCEED` label is never authority on its own. Embedded proposal/review copies must match their source snapshots.

These local checks detect accidental edits and inconsistent files; they are not signatures, external audit anchors or protection against an actor rewriting every source and digest. Tail deletion is not externally anchored. Legacy unsealed session events fail closed and must be preserved for inspection, not silently relabeled as verified. Start a new session from reviewed source inputs rather than modifying old evidence to resume.
