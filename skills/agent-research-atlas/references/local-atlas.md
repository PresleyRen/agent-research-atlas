# Local atlas contract

Version 1.0.0 · Python 3.10+ · Standard library only

## Files and reuse

Research state belongs to a user-authorized project, separate from the skill:

```text
PROJECT/
  research-atlas.config.json       # relative location pointer
  research-atlas/
    atlas.json                    # revisioned source of truth
    MAP.md                        # generated overview
    map.html                      # offline interactive graph and index
    domains/<domain-id>/
      MAP.md                      # generated evidence/relationship view
      notes.md                    # human notes, never overwritten
    papers/ hypotheses/ claims/ explorations/ imports/
    experiments/<experiment-id>/  # plans, freezes, runs, imported results
    history/                      # prior states and views
```

`discover` scans up to 20,000 files, six levels deep, skipping symlinks, git/dependencies/cache/history/skill directories. It reports truncation. Inspect additional known locations when needed. It recognizes map-like filenames and native `atlas.json`; it does not understand arbitrary research prose or search the whole computer.

`init` is idempotent. It reuses a configured atlas or a single native atlas elsewhere through a relative pointer. Multiple atlases require `--atlas-dir`. Existing non-native maps block blind initialization: read them, then `adopt --file path/to/map.md`. Adoption retains original bytes and records path/hash as `registered_pending_semantic_import`. The host must read, extract, source and upsert the content. Unreadable formats remain pending.

After semantic import, annotate the existing import using `path`, `status: "normalized"`, `node_ids` and a note in a batch `imports` entry. This does not rewrite the original map. Local artifact paths reject traversal, absolute paths and symlink components. These tools are not security sandboxes or tamper-proof ledgers; version/back up the research project appropriately.

## Commands

```bash
python <SKILL>/scripts/atlas.py --root <PROJECT> discover
python <SKILL>/scripts/atlas.py --root <PROJECT> init --title 'Agent research'
python <SKILL>/scripts/atlas.py --root <PROJECT> adopt --file docs/existing-map.md
python <SKILL>/scripts/atlas.py --root <PROJECT> status
python <SKILL>/scripts/atlas.py --root <PROJECT> upsert --file batch.json --expected-revision 0
python <SKILL>/scripts/atlas.py --root <PROJECT> check
python <SKILL>/scripts/atlas.py --root <PROJECT> render
python <SKILL>/scripts/atlas.py --root <PROJECT> mark-stale --days 90 --as-of 2026-10-20
python <SKILL>/scripts/atlas.py queries --domain routing --focus-zh '检索前不确定性' --focus-en 'pre-retrieval uncertainty' --since 2024
```

Replace bracketed paths. Global options appear before the subcommand. `queries` plans eight bilingual rows (survey/closest work/negative evidence/evaluation), without executing searches or adding search records. Both focus translations must be supplied together. Custom graph domains are supported through `upsert`; the query planner uses seeded IDs, so author custom-domain queries through the host. `mark-stale` is an explicit policy operation; 90 days is editable, not a universal freshness interval.

## State schema

Root fields: `schema_version: 1`, `revision`, `project`, `nodes`, `edges`, `imports`. Project fields include title, scope, languages, timestamps and a synthetic flag fixed at creation.

Nodes: stable `id` (lowercase letters/numbers/underscore/hyphen; max 96 characters), `type`, `title`, `status`, `domains`, `data`, `sources`, timestamps. Additional fields are preserved.

| Type | Purpose |
|---|---|
| domain | Extensible direction; `data.coverage`: unsearched/partial/reviewed/stale. |
| paper | Sourced bibliographic record, optionally with DOI/arXiv for deduplication. |
| problem | Observed gap, contradiction, failure or unexplained phenomenon. |
| hypothesis | Mechanism, predictions, rivals, nearest work and evidence state. |
| experiment | Planned/performed experiment linked to actual records. |
| claim | Narrow research/manuscript claim with evidence and limitations. |
| decision | Continue/narrow/park/abandon/reopen/supersede with reasons. |
| exploration | Executed search with query/date/provider/scope/results/limits. |

Hypothesis and claim states are validated enumerations. Status vocabularies for paper/problem/experiment/decision/exploration are extensible; do not imply the validator restricts them all.

### Sources

Web: `{"url":"https://…","access":"metadata|abstract|fulltext","accessed_at":"YYYY-MM-DD","locator":"section/page/abstract"}`.

Local: `{"path":"relative/file.md","access":"local","accessed_at":"YYYY-MM-DD","locator":"heading/lines"}`.

Metadata may omit a locator; read-text sources require one. Local evidence must exist. URL syntax is not proof of reading or bibliographic truth. Verify actual sources through the host. DOI/arXiv duplicates are rejected for explicit merging; title-only/version collisions require researcher review.

### Hypothesis gates

| State | Required fields in data |
|---|---|
| proposed | Title/scope; unresolved unknowns are allowed. |
| grounded | `problem`, `mechanism`, `prediction`, nonempty `rival_explanations`, `closest_paper_ids` referencing sourced papers. |
| testable | Grounded fields + `minimal_test`, `falsification`, `feasibility_notes`; feasibility data/compute/evaluation/budget all `available`. |
| pilot_supported / inconclusive / refuted | Testable fields + experiment `evidence_ids` with existing `artifact_path`; `review` with summary/limitations/reviewer/reviewed_at. |
| independently_supported | Empirical fields + `independence` describing independent evidence and shared dependencies. |
| parked | Preserve why blocked/deprioritized and the reopening condition. |

Workflow feasibility values: `available`, `unverified`, `unavailable`; only available passes the testable gate. They are documented researcher judgments, not automated resource verification. Artifact existence and an independence explanation are structural checks, not evidence-quality judgments. Run `experiments.py validate-record` separately for its hash checks; other trusted experiment stacks are allowed.

Every status change needs a fresh `data.status_reason`. History preserves earlier states. Reasoned downgrading/reopening is supported; this is not a one-way success ladder. Existing empirical research may be imported directly with its evidence.

### Coverage, claims and relations

Exploration `data`: `query`, `language` (zh/en/mixed), `provider`, `searched_at`, `scope`, `limitations`, `result_ids` referencing paper nodes. Empty results are valid. Add screening reasons and provider errors when appropriate.

A reviewed domain requires `last_reviewed` (YYYY-MM-DD), `search_ids` referencing exploration nodes, and `coverage_limits`. Record both language passes or the reason one is absent; the checker does not equate a single search with adequate coverage.

Edges: id/source/target/relation, optional note/provenance. Allowed relations: part_of, motivates, addresses, tests, supports, contradicts, extends, compares_with, uses, derived_from, supersedes, relates_to.

Claim states: draft/supported/partial/unsupported/withdrawn. Supported/partial require paper/experiment `evidence_ids`, `reasoning`, `limitations`. Read the evidence before assigning them. A supports edge records an interpretation; it is not a truth judgment made by the script.

## Incremental writes

Batch JSON allows nodes/edges/project and import annotations. Example candidate, **not a finding**:

```json
{"nodes":[{"id":"hyp-cost-aware-router","type":"hypothesis","title":"Could calibrated abstention improve routing under a fixed cost budget?","status":"proposed","domains":["routing","clarification"],"sources":[],"data":{"unknowns":["closest work","independent evaluation data"],"feasibility":{"data":"unverified","compute":"unverified","evaluation":"unverified","budget":"unverified"}}}],"edges":[]}
```

Writes use an exclusive lock, atomic state replacement and prior-state snapshots. Supply `--expected-revision` when combining parallel contributions. Validate the entire proposed state before writing. After an interrupted process, inspect the lock's PID and active writers before recovering a stale lock; it is never automatically removed.

Nested objects merge; lists append unique entries; unmentioned fields stay. Node types and project provenance cannot be rewritten, and no deletion command exists. Correct errors with documented withdrawn/superseded records and links. State the current interpretation explicitly; additive evidence lists should not hide supersession.

State and views are separate writes. If rendering fails, canonical state may already be committed. Inspect `status`, resolve the view error without bypassing permissions, then `render`; do not repeat the upsert blindly. Prior view contents, including human edits, are backed up before replacement. Use notes.md for persistent prose.

The HTML uses no CDN/network requests and filters all records by text/domain/type/status. It draws at most 140 matching graph nodes; the complete matching index remains visible, and the graph cap is clearly announced. Narrow filters to view remaining nodes. Refresh after regeneration; it is a snapshot, not an editor or live watcher.
