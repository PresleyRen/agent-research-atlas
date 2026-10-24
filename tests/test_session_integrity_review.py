"""Independent adversarial coordinator tests; mocked experiment outcomes are synthetic."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'skills/agent-research-atlas/scripts'))
import research_session as session_module
import research_cycle


class IndependentSessionIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        shutil.copytree(REPO / 'evals/real_research_cycle/scifact_smoke', self.root / 'data')
        self.session = session_module.Session(self.root)
        inputs = []
        for role, relative in [('corpus', 'data/corpus.jsonl'), ('queries', 'data/queries.jsonl'), ('qrels', 'data/qrels/test.tsv')]:
            inputs.append({'role': role, 'path': relative, 'sha256': hashlib.sha256((self.root / relative).read_bytes()).hexdigest()})
        proposal = {'proposal_id': 'synthetic-integrity-proposal', 'primary_source_locator': 'fixture only',
            'later_work_checked': True, 'distinct_remaining_gap': 'synthetic gate fixture',
            'feasibility': dict.fromkeys(['data', 'compute', 'evaluation', 'budget'], 'available'),
            'minimal_test': 'mock experiment for crash recovery', 'rival_prediction': 'not a science claim',
            'required_measurements': ['retrieval_relevance'],
            'data_contract': {'measured_construct': 'retrieval', 'metric': 'nDCG@10', 'ground_truth_provenance': 'fixture',
                'measurement_capabilities': ['retrieval_relevance'], 'files': inputs},
            'experiment': {'runner': 'bm25_title_weight', 'split': 'test', 'k': 10}}
        self.write('proposal.json', proposal)
        packet = self.session.prepare('proposal.json', [x['path'] for x in inputs], 'scientist-fixture')['payload']
        for role in ['critic', 'supervisor']:
            review = {'role': role, 'reviewer_id': role + '-fixture', 'proposal_id': proposal['proposal_id'],
                'packet_sha256': packet['packet_sha256'], 'finding': 'synthetic fixture, not independent scientific review',
                'evidence_locator': 'data/qrels/test.tsv', 'evidence_paths': ['data/qrels/test.tsv'], 'severity': 'nonblocking'}
            self.write(role + '.json', review)
            self.session.submit_review(role + '.json')
        self.assertEqual(self.session.decide()['payload']['decision'], 'PROCEED')
        self.fake_result = {'direction_decision': 'INCONCLUSIVE', 'scientific_verdict': 'not_assessed', 'synthetic_test_only': True}

    def write(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value))

    def run_mocked(self):
        with patch.object(session_module.benchmark, 'evaluate', return_value=self.fake_result):
            return self.session.experiment('data')

    def test_modified_experiment_result_is_detected_on_status(self):
        self.run_mocked()
        record = next(x for x in self.session.events() if x['kind'] == 'experiment')
        self.write(record['payload']['result']['path'], {'tampered': True})
        with self.assertRaisesRegex(research_cycle.ResearchError, 'changed'):
            session_module.Session(self.root).events()

    def test_matching_orphan_result_is_recovered_without_overwriting(self):
        relative = 'research-atlas/session/result-0005.json'
        self.write(relative, self.fake_result)
        original = (self.root / relative).read_bytes()
        self.assertEqual(self.run_mocked()['payload']['decision'], 'SEARCH_MORE')
        self.assertEqual((self.root / relative).read_bytes(), original)
        self.assertEqual(len([e for e in self.session.events() if e['kind'] == 'experiment']), 1)

    def test_differing_orphan_result_requires_inspection(self):
        relative = 'research-atlas/session/result-0005.json'
        self.write(relative, {'different': True})
        original = (self.root / relative).read_bytes()
        with self.assertRaisesRegex(research_cycle.ResearchError, 'orphan result differs'):
            self.run_mocked()
        self.assertEqual((self.root / relative).read_bytes(), original)
        self.assertEqual(len(self.session.events()), 4)

    def test_recovery_after_experiment_event_does_not_rerun(self):
        original_append = self.session.append
        def fail_decision(kind, payload):
            if kind == 'decision':
                raise RuntimeError('synthetic interruption after experiment event')
            return original_append(kind, payload)
        with patch.object(self.session, 'append', side_effect=fail_decision):
            with self.assertRaisesRegex(RuntimeError, 'synthetic interruption'):
                self.run_mocked()
        self.assertEqual(self.session.events()[-1]['kind'], 'experiment')
        with patch.object(session_module.benchmark, 'evaluate', side_effect=AssertionError('must not rerun')):
            recovered = session_module.Session(self.root).experiment('data')
        self.assertEqual(recovered['payload']['decision'], 'SEARCH_MORE')
        self.assertEqual(len(self.session.events()), 6)

    def test_matching_orphan_followup_search_resumes_without_network(self):
        self.run_mocked()
        relative = 'research-atlas/session/search-0007.json'
        receipt = {'query': 'synthetic topic', 'records': [], 'response_sha256': 'synthetic-provenance'}
        self.write(relative, receipt)
        original = (self.root / relative).read_bytes()
        with patch.object(session_module.c, 'crossref_query', side_effect=AssertionError('must not refetch')):
            event = self.session.search_more('synthetic topic')
        self.assertEqual(event['kind'], 'followup_search')
        self.assertEqual((self.root / relative).read_bytes(), original)
        self.assertEqual(len(self.session.events()), 7)

    def test_mismatched_orphan_followup_search_is_not_overwritten(self):
        self.run_mocked()
        relative = 'research-atlas/session/search-0007.json'
        self.write(relative, {'query': 'other topic', 'records': [], 'response_sha256': 'synthetic-provenance'})
        original = (self.root / relative).read_bytes()
        with patch.object(session_module.c, 'crossref_query', side_effect=AssertionError('must not refetch')):
            with self.assertRaisesRegex(research_cycle.ResearchError, 'orphan search'):
                self.session.search_more('synthetic topic')
        self.assertEqual((self.root / relative).read_bytes(), original)
        self.assertEqual(len(self.session.events()), 6)

    def test_repeated_completed_experiment_is_rejected(self):
        self.run_mocked()
        with self.assertRaisesRegex(research_cycle.ResearchError, 'PROCEED'):
            self.run_mocked()


if __name__ == '__main__':
    unittest.main()
