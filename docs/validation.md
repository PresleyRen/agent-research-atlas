# Validation report / 验证记录

Date: **2026-10-20**. Release candidate: **1.0.0**.

This report separates software tests, independent-context task trials, live retrieval checks and scientific effectiveness. The first three were exercised as described below; scientific discovery effectiveness and publication outcomes were not established.

本报告区分软件测试、独立上下文实际任务、真实检索通路和科研效果。前三类按下述范围执行；没有据此声称创新成功率或论文录用率。

## 1. Reproducible local tests

Executed from the repository root:

```bash
python -m unittest discover -s tests -q
```

Observed final result:

```text
Ran 60 tests in 14.795s
OK
```

| Suite | Passed | What it exercises |
|---|---:|---|
| `test_atlas.py` | 40 | Initialization/reuse/adoption, original bytes and notes, revision conflicts, additive updates, graph references, DOI/arXiv identity variants, hypothesis/claim requirements, scoped coverage, staleness, bilingual query planning, path/symlink checks, write locks, JSON ambiguity and generated HTML serialization. |
| `test_experiments.py` | 20 | Successful/failed/timeout execution, raw logs, authorization declaration, plan freeze, checksums, immutable run IDs, conservative budgets/cancellations, lock exclusion, exact-byte external imports, numeric JSON, path/symlink handling and retained incomplete attempts. |

All test inputs and executed workloads are explicitly synthetic and local. No paid services, package installs, real model inference, user datasets or web searches were performed by this unittest suite. Durations vary by machine. Source: [atlas tests](../tests/test_atlas.py), [experiment tests](../tests/test_experiments.py).

### Defects found and fixed before release

An independently written CLI suite initially passed 33/37 atlas tests and exposed four defects:

1. Unversioned arXiv PDF URLs were not deduplicated against their bare identifiers.
2. A paper with both DOI and arXiv identifiers lost its arXiv identity during deduplication.
3. Domain activity status could be confused with exploration coverage.
4. A known unsafe render destination could be rejected only after canonical state had changed.

The implementation now compares all normalized identifiers, keeps domain status separate from coverage, and preflights known output-path hazards before committing state. All four regressions pass. Three additional tests exercise adoption into an existing atlas, changed-import provenance and ambiguous/non-finite JSON rejection.

Preflight is not a multi-file database transaction: disk failure or adversarial filesystem changes after checking can still interrupt view generation. The canonical state is atomically replaced; generated views can be rebuilt. Local history is not externally attested or tamper-proof.

## 2. Skill packaging and viewer checks

- The skill-creator validator returned **`Skill is valid!`** for the completed installable directory.
- The HTML viewer's executable JavaScript passed Node's syntax check.
- HTML parsing tests verified that hostile title strings stay in the inert JSON payload and round-trip as data, rather than becoming injected HTML elements.
- Documentation links, code fences, the 14 taxonomy IDs and JSON syntax were checked.

These checks do **not** constitute a full browser-execution security audit or visual/accessibility review on every device. The viewer has no external library/CDN dependencies. Its graph limit of 140 matching nodes is explicitly announced, while the record index retains all matching records.

## 3. Independent-context task A: resume an existing local map

A fresh agent context received the Skill path and a realistic offline request to continue an existing project. It did not receive implementation answers, expected node counts or bug hints. The artificial project contained one Chinese Markdown map with:

- A reported debugging observation involving 18 hand-written inputs, without the original inputs or runnable baseline.
- A question about one clarification turn versus extra latency.
- Unknown data rights, GPU access and paid-API budget.
- A paused keyword-routing direction and a human note about annotation ambiguity.

Observed result, independently inspected by the coordinating agent:

| Check | Observed outcome |
|---|---|
| Reuse instead of blind replacement | Existing map was read, adopted, and semantically normalized with a provenance record. |
| Preserve source | Original SHA-256 stayed `4de6e26cef14b947baae1b09f40c62cc94adad729f60ba7e7bd899e97e8a17a3`; original notes and a byte backup were retained. |
| Persistent map | Revision 1, 28 nodes, 21 explicit edges; 14 domain folders and HTML/Markdown maps generated. |
| Research candidates | Three proposed hypotheses; one retrieval-related hypothesis parked pending access/resources. |
| Honest evidence state | All 14 literature domains remained unsearched; no papers or actual searches were invented. |
| Bilingual next steps | Chinese/English query plans saved as not executed, alongside resource and candidate files. |
| Failed-direction memory | Keyword-rule work remained paused with a reopening condition. |
| Final structural check | `atlas.py check` returned valid. |

The coordinating agent separately reviewed the one-turn clarification proposal. That review tightened the single primary metric and clarified that “always clarify” is a cost-curve reference, not a matched-budget comparison. This was a logic review, **not** literature verification, empirical support or blinded peer review.

## 4. Independent-context task B: run a bounded local experiment

A second fresh agent context received the Skill path, a project containing the hand-authored [tiny synthetic experiment](../examples/tiny_agent_experiment.py), and a request for exactly seeds 7 and 13. The budget was two runs, at most 3 seconds each, 6 seconds reserved in total. It was instructed to inspect the code and operate offline, with no installations or paid services.

The agent inspected the source, recorded and froze an **exploratory** plan, ran the two authorized payloads, preserved logs, interpreted the results, and updated the atlas.

| Seed | Direct process status | Fixture accuracy | Synthetic constant-label baseline | Runner elapsed seconds |
|---|---|---:|---:|---:|
| 7 | succeeded, exit 0 | 1.0 | 0.18333333333333332 | 0.03595322199998918 |
| 13 | succeeded, exit 0 | 1.0 | 0.31666666666666665 | 0.03523815999960789 |

**The accuracy of 1.0 is hard-coded in the fixture.** It is not a measured Agent routing result. The agent identified this from the code and explicitly rejected the claim of perfect real-world routing. The fixture also prints a fixed elapsed value; the table uses the runner's independently recorded local elapsed time instead.

Observed record details:

- Freeze time: `2026-10-20T03:09:39.975182Z`.
- Frozen plan SHA-256: `012326144ba46426518be71275e748415103af8a1be4cd1ca47e3d7e1ad70874`.
- Exactly two payload runs; full 3+3-second reservations consumed, without refunding unused time or running a third trial.
- `validate-record` returned `integrity_checked`, no incomplete attempts, and `scientific_verdict: not_assessed`.
- Final atlas: revision 2, 24 nodes, 12 explicit edges; final `check` returned valid.
- A process-completion claim was supported; a perfect-real-routing claim was unsupported; the real research hypothesis remained proposed.
- All 14 literature domains remained unsearched. Eight bilingual query rows were planned, not executed.

This tested plan→freeze→run→logs→interpretation→map maintenance. It did not test a real model, independent scientific replication, causal mechanism or research novelty. The coordinator subsequently inspected both raw run records and re-ran their integrity validation.

During development, the coordinating agent patched `atlas.py` after the experiment runs to fix atlas regressions. The trial recorded this tool-version boundary; the payload and experiment recorder were unchanged. Final map checks used the updated atlas tool. No historical experiment record was rewritten to conceal the change.

## 5. Live Chinese/English retrieval smoke

[retrieval-smoke.md](retrieval-smoke.md) records exact live queries, successfully opened original Chinese/English paper records and failed access. One Chinese journal record and two English conference records were opened at metadata/abstract depth. The report explicitly retains article-page timeouts and untested database-native searches.

This verifies those narrow retrieval routes. It does not measure comprehensive recall, full-text claim accuracy, access to paid providers, freshness across all Agent subfields or successful hypothesis discovery.

## 6. CI and reproducibility

The repository includes [a GitHub Actions workflow](../.github/workflows/tests.yml) for the same deterministic suite on Python 3.10, 3.12 and 3.13. The local outcome above is an observed result. The presence of a workflow is not evidence that a particular remote run passed; inspect the repository's Actions page for live results.

To repeat a forward task, create a separate project containing your own nonsensitive map or a copy of the synthetic example, give a fresh compatible host the Skill path and a normal user task, and inspect its artifacts. Outputs from a language-model-driven task are not expected to be byte-identical. Keep the test budget and the distinction between proposed, observed and supported explicit.

## What remains unproven

No test here establishes complete literature coverage, correct scientific reasoning on every problem, autonomous general research ability, improved publication success, SCI indexing or acceptance by a leading journal/conference. No commercial literature service was installed or authenticated. A local runner does not provide operating-system isolation or enforce cloud charges. These are material limits, not hidden assumptions.
