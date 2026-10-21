"""Read-only numerical audits and machine-readable extension contract checks."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / 'skills/agent-research-atlas'
sys.path.insert(0, str(SKILL / 'scripts'))
import audit
from atlas import Atlas, AtlasError


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='atlas-audit-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'metrics.json').write_text('{"metrics":{"accuracy":0.75},"slices":[1,2],"a/b":{"x~y":3}}')

    def ledger(self, **kwargs):
        return {'schema_version': 1, 'claims': [{'id': 'value-a', 'artifact_path': 'metrics.json',
                    'pointer': '/metrics/accuracy', 'reported_value': 0.75, **kwargs}]}

    def test_cf_reported_number_must_match_exact_source_field(self):
        result = audit.audit_values(self.root, self.ledger(reported_value=0.95))
        self.assertFalse(result['all_values_match'])
        self.assertEqual(result['claims'][0]['status'], 'mismatch')
        self.assertEqual(result['claims'][0]['observed_value'], 0.75)
        self.assertEqual(result['scientific_verdict'], 'not_assessed')
        self.assertEqual(audit.audit_values(self.root, self.ledger())['claims'][0]['status'], 'match')

    def test_missing_file_locator_parse_and_type_are_distinct(self):
        (self.root / 'invalid.json').write_text('{invalid')
        variants = [('missing_file', {'artifact_path': 'missing.json'}),
                    ('missing_locator', {'pointer': '/metrics/f1'}),
                    ('unparseable', {'artifact_path': 'invalid.json'}),
                    ('non_numeric', {'pointer': '/metrics'})]
        for status, values in variants:
            with self.subTest(status=status):
                self.assertEqual(audit.audit_values(self.root, self.ledger(**values))['claims'][0]['status'], status)

    def test_value_identity_is_not_overridden_by_a_matching_number(self):
        result = audit.audit_values(self.root, self.ledger(expected_sha256='0' * 64))
        self.assertEqual(result['claims'][0]['status'], 'version_mismatch')
        self.assertEqual(result['claims'][0]['value_status'], 'match')
        self.assertFalse(result['all_values_match'])

    def test_json_pointer_escapes_arrays_and_explicit_tolerance(self):
        for pointer, value in [('/a~1b/x~0y', 3), ('/slices/1', 2), ('/metrics/accuracy', 0.7501)]:
            with self.subTest(pointer=pointer):
                result = audit.audit_values(self.root, self.ledger(pointer=pointer, reported_value=value, abs_tol=0.001))
                self.assertTrue(result['all_values_match'])
        for pointer in ['bad', '/bad~3', '/bad~']:
            with self.assertRaises(AtlasError):
                audit.audit_values(self.root, self.ledger(pointer=pointer))

    def test_value_audit_is_read_only_and_rejects_ambiguous_numeric_data(self):
        original = {path.name: path.read_bytes() for path in self.root.iterdir()}
        audit.audit_values(self.root, self.ledger())
        self.assertEqual(original, {path.name: path.read_bytes() for path in self.root.iterdir()})
        for raw in ['{"metrics":{"accuracy":NaN}}', '{"metrics":{"accuracy":1e999}}',
                    '{"metrics":{"accuracy":0.75,"accuracy":0.99}}']:
            (self.root / 'bad.json').write_text(raw)
            self.assertEqual(audit.audit_values(self.root, self.ledger(artifact_path='bad.json'))['claims'][0]['status'], 'unparseable')
        for value in [True, float('nan'), float('inf')]:
            with self.assertRaises(AtlasError):
                audit.audit_values(self.root, self.ledger(reported_value=value))

    def test_paths_do_not_escape_project_or_accept_windows_drive_spelling(self):
        for path in ['../metrics.json', str(self.root / 'metrics.json'), 'C:\\metrics.json']:
            with self.assertRaises(AtlasError):
                audit.audit_values(self.root, self.ledger(artifact_path=path))
        if hasattr(Path, 'symlink_to'):
            (self.root / 'linked.json').symlink_to(self.root / 'metrics.json')
            with self.assertRaises(AtlasError):
                audit.audit_values(self.root, self.ledger(artifact_path='linked.json'))

    def registry(self):
        return {'schema_version': 1, 'capabilities': [{'id': 'C01', 'name': '查新 Novelty', 'description': 'bounded search',
                 'limits': 'No automatic scientific verification', 'remedy': 'Read closest primary work',
                 'keywords': ['novelty', '查新'], 'symptoms': ['空搜索'], 'depends_on': [],
                 'implementation': [{'path': 'scripts/audit.py', 'symbol': 'audit_values'}],
                 'tests': [{'path': 'tests/test_audit.py', 'symbol': 'AuditTests.test_cf_reported_number_must_match_exact_source_field', 'kind': 'conflict'}]}],
                 'sources': [{'id': 'SRC-ONE', 'name': 'SYNTHETIC source', 'url': 'https://example.org/fixture',
                   'read_depth': 'synthetic fixture', 'revision': 'synthetic', 'features': [{'id': 'F01', 'label': 'limited query',
                   'capabilities': ['C01'], 'status': 'protocol', 'gap': 'not a live provider', 'remedy': 'use available host tools', 'complements': []}]}],
                 'conflicts': [{'id': 'CF01', 'tension': 'empty search vs novelty', 'retain': 'trace the scope', 'reject': 'global confirmation',
                   'reason': 'no result does not prove no prior work', 'extension_rule': 'retain null-result case', 'capabilities': ['C01'],
                   'tests': [{'path': 'tests/test_audit.py', 'symbol': 'AuditTests.test_registry_rejects_broken_feature_mapping_or_source', 'kind': 'conflict'}]}]}

    def test_registry_checks_real_paths_symbols_and_capability_graph(self):
        registry = self.registry()
        self.assertTrue(audit.check_registry(registry, repo=REPO)['valid'])
        for change in ('path', 'symbol', 'cycle'):
            broken = copy.deepcopy(registry)
            if change == 'path':
                broken['capabilities'][0]['implementation'][0]['path'] = 'scripts/missing.py'
            elif change == 'symbol':
                broken['capabilities'][0]['tests'][0]['symbol'] = 'AuditTests.nonexistent'
            else:
                broken['capabilities'][0]['depends_on'] = ['C01']
            with self.subTest(change=change), self.assertRaises(AtlasError):
                audit.check_registry(broken, repo=REPO)

    def test_registry_rejects_broken_feature_mapping_or_source(self):
        for field, value in [('capabilities', ['unknown']), ('status', 'certified'), ('complements', ['missing'])]:
            broken = self.registry()
            broken['sources'][0]['features'][0][field] = value
            with self.subTest(field=field), self.assertRaises(AtlasError):
                audit.check_registry(broken, repo=REPO)
        broken = self.registry()
        broken['sources'].append(copy.deepcopy(broken['sources'][0]))
        with self.assertRaises(AtlasError):
            audit.check_registry(broken, repo=REPO)

    def test_bilingual_lookup_locates_extension_without_inventing_match(self):
        for query in ['查新', 'novelty', 'C01', '空搜索']:
            result = audit.locate(self.registry(), query)
            self.assertEqual(result['matches'][0]['id'], 'C01')
            self.assertEqual(result['matches'][0]['sources'][0]['id'], 'SRC-ONE')
            self.assertEqual(result['matches'][0]['conflicts'], ['CF01'])
        self.assertEqual(audit.locate(self.registry(), 'unrelatedxyz')['matches'], [])

    def test_project_diagnostics_expose_unexplored_not_completed(self):
        missing = audit.project_gaps(self.root)
        self.assertEqual(missing['issues'][0]['code'], 'G-MAP')
        Atlas(self.root).init('SYNTHETIC diagnostic project', synthetic=True)
        report = audit.project_gaps(self.root)
        issue = next(item for item in report['issues'] if item['code'] == 'G-COVERAGE-UNSEARCHED')
        self.assertEqual(len(issue['node_ids']), 14)
        self.assertEqual(report['scientific_verdict'], 'not_assessed')


if __name__ == '__main__':
    unittest.main()
