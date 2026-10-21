# Capability lookup and extension contract

The installed skill includes `assets/capability-registry.json`: the machine-readable index of 28 capabilities, individually inspected sources/features, adoption status, complement relationships, conflict decisions, implementation locations and test references. Read it selectively with `audit.py locate`; do not load every upstream skill into a research prompt.

## Locate the weak point

```bash
python <SKILL>/scripts/audit.py locate --query '查新'
python <SKILL>/scripts/audit.py locate --query 'evaluator'
python <SKILL>/scripts/audit.py locate --query 'C20'
python <SKILL>/scripts/audit.py --root <PROJECT> project
python <SKILL>/scripts/audit.py check
```

`locate` is an explicit lexical lookup, not a research-quality ranking. It returns the matching capability, implementation paths/symbols, verification records, related source features, current limitations, complementary sources and a concrete repair route. Use a shorter symptom or ID when no match exists; an empty lookup cannot establish that a capability is unnecessary.

`project` is read only. It diagnoses explicit states such as unfinished imports, unsearched/stale directions, unresolved feasibility and pending downstream reviews. A clean report does not prove completeness, validity or novelty. Capability coverage (what this skill can do) and research coverage (what this project has actually explored) are separate.

## Before extending

1. Reproduce the actual gap using a small, representative project/task. Preserve current behavior and the evidence that shows the failure.
2. Locate the owning `Cxx` capability and its conflict contracts. Fix one owner module; reuse the shared paper/evidence/experiment schemas instead of creating a second truth store.
3. Record the source's current version and exact reading depth. Add distinctive features individually; mark each `implemented`, `protocol`, `optional`, `reference`, `deferred` or `rejected` with its limitation and remedy. A source row is not an effectiveness benchmark.
4. Add or update the implementation, evidence contract, fallback, tests and complement links together. Never clear uncertainty merely to pass a state validator.
5. Run `audit.py check --repo <REPO>` in the distribution checkout. It checks declared paths, Python symbols, IDs, dependencies and test references. Installed copies without repository tests can run `check`; the output discloses that test references were not verified.
6. Run the relevant regression and a fresh task when host reasoning behavior changes. Do not reveal the desired verdict to a forward-test assistant. Update the full README capability table and a change record, then publish only within the user's authorization.

## Compatibility rules

- Source connectors must preserve query/provider/date/language/access-depth and distinguish planned, success, empty, blocked, rate-limited and failed outcomes. Do not map a failed search to evidence of novelty.
- Use provider-specific query syntax. S2 negative recommendation seeds indicate irrelevant items, not scientific counterevidence. User authorization and paid-tool availability remain actual constraints.
- New domains are ordinary sourced domain nodes with explicit coverage. Add seed terminology separately if it should appear in `queries`; customized domains currently use a host-authored bilingual ledger.
- Optimization may change declared candidate files while immutable evaluator/ground-truth files remain pinned. Declare amendments through new experiment IDs and keep negative results.
- Schema changes need explicit migration preserving source bytes, IDs, revisions, review queues and old record meaning. Never relabel legacy runs as having guarantees added later.
- The registry is an index of reviewed declarations. A structural `check` cannot establish that a method works, a connector is authenticated or a paper is publishable.

The repository's `docs/EXTENDING.md` provides concrete extension examples and symptom-to-file mappings. It stays outside the loadable skill to keep ordinary research contexts focused.
