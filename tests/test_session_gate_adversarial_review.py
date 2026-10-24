"""Independent gate-bypass regressions. Inputs/outcomes here are synthetic fixtures.

Recomputed local checksums are intentionally NOT treated as authentication.
These checks require execution eligibility to be rederived from bound inputs.
"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/agent-research-atlas/scripts'))
import research_session as module
import research_cycle as cycle


def seal(event):
    event.pop('event_sha256', None)
    event['event_sha256'] = hashlib.sha256(json.dumps(event, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return event


class IndependentGateBypassTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        shutil.copytree(ROOT / 'evals/real_research_cycle/scifact_smoke', self.root / 'data')
        self.session = module.Session(self.root)

    def write(self, relative, obj):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(obj))
        return path

    def prepare(self, measurements=None):
        files = [{'role': role, 'path': path, 'sha256': hashlib.sha256((self.root / path).read_bytes()).hexdigest()}
                 for role, path in [('corpus', 'data/corpus.jsonl'), ('queries', 'data/queries.jsonl'), ('qrels', 'data/qrels/test.tsv')]]
        proposal = {'proposal_id': 'gate-review-fixture', 'primary_source_locator': 'synthetic fixture',
            'later_work_checked': True, 'distinct_remaining_gap': 'synthetic, not a scientific gap',
            'feasibility': dict.fromkeys(['data', 'compute', 'evaluation', 'budget'], 'available'),
            'minimal_test': 'gate regression', 'rival_prediction': 'invalid input must not execute',
            'required_measurements': measurements or ['retrieval_relevance'],
            'data_contract': {'measured_construct': 'retrieval', 'metric': 'nDCG@10', 'ground_truth_provenance': 'fixture only',
                'measurement_capabilities': ['retrieval_relevance'], 'files': files},
            'experiment': {'runner': 'bm25_title_weight', 'split': 'test', 'k': 10}}
        self.write('proposal.json', proposal)
        self.packet = self.session.prepare('proposal.json', [f['path'] for f in files], 'fixture-scientist')['payload']

    def review(self, role, blocking=False):
        review = {'role': role, 'reviewer_id': 'fixture-' + role, 'proposal_id': 'gate-review-fixture',
            'packet_sha256': self.packet['packet_sha256'], 'finding': 'synthetic gate finding',
            'evidence_locator': 'data/qrels/test.tsv', 'evidence_paths': ['data/qrels/test.tsv'],
            'severity': 'blocking' if blocking else 'nonblocking', 'failure_type': 'measurement', 'resolved': False}
        self.write(role + '.json', review)
        self.session.submit_review(role + '.json')

    def change_tail(self, mutate, reseal=True):
        path = sorted(self.session.directory.glob('event-*.json'))[-1]
        value = json.loads(path.read_text())
        mutate(value)
        if reseal:
            seal(value)
        path.write_text(json.dumps(value))

    def must_not_execute(self, pattern):
        with patch.object(module.benchmark, 'evaluate', return_value={'direction_decision': 'INCONCLUSIVE', 'synthetic_test_only': True}) as evaluate:
            with self.assertRaisesRegex(cycle.ResearchError, pattern):
                self.session.experiment('data')
            evaluate.assert_not_called()

    def test_raw_tail_proceed_edit_without_reviews_fails_integrity(self):
        self.prepare()
        self.assertEqual(self.session.decide()['payload']['decision'], 'SEARCH_MORE')
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'), reseal=False)
        self.must_not_execute('integrity')

    def test_resealed_tail_proceed_without_reviews_fails_recomputed_gate(self):
        self.prepare()
        self.session.decide()
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'))
        self.must_not_execute('recomputed PROCEED')

    def test_resealed_tail_proceed_with_only_one_reviewer_fails(self):
        self.prepare()
        self.review('critic')
        self.session.decide()
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'))
        self.must_not_execute('recomputed PROCEED')

    def test_resealed_failed_measurement_gate_cannot_become_proceed(self):
        self.prepare(['positional_attention'])
        self.review('critic')
        self.review('supervisor')
        self.assertEqual(self.session.decide()['payload']['decision'], 'REPAIR_MEASUREMENT')
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'))
        self.must_not_execute('recomputed PROCEED')

    def test_resealed_critic_blocker_cannot_become_proceed(self):
        self.prepare()
        self.review('critic', blocking=True)
        self.review('supervisor')
        self.assertEqual(self.session.decide()['payload']['decision'], 'REPAIR_MEASUREMENT')
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'))
        self.must_not_execute('recomputed PROCEED')

    def test_embedded_review_cannot_override_unchanged_source(self):
        self.prepare()
        self.review('supervisor')
        self.review('critic', blocking=True)
        self.change_tail(lambda e: e['payload']['review'].update(severity='nonblocking', resolved=True))
        with self.assertRaisesRegex(cycle.ResearchError, 'embedded review'):
            self.session.decide()

    def test_embedded_proposal_cannot_override_unchanged_source(self):
        self.prepare(['positional_attention'])
        def mutate(event):
            packet = event['payload']
            packet['proposal']['required_measurements'] = ['retrieval_relevance']
            packet.pop('packet_sha256')
            packet['packet_sha256'] = hashlib.sha256(json.dumps(packet, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        self.change_tail(mutate)
        self.must_not_execute('embedded proposal')

    def test_resealed_post_experiment_decision_cannot_reexecute_same_packet(self):
        self.prepare()
        self.review('critic')
        self.review('supervisor')
        self.session.decide()
        with patch.object(module.benchmark, 'evaluate', return_value={'direction_decision': 'INCONCLUSIVE', 'synthetic_test_only': True}):
            self.session.experiment('data')
        self.change_tail(lambda e: e['payload'].update(decision='PROCEED'))
        self.must_not_execute('already|executed|duplicate|completed')

    def test_injected_unbound_review_evidence_cannot_pass_effective_gate(self):
        self.prepare()
        for role in ['critic', 'supervisor']:
            review = {'role': role, 'reviewer_id': 'fixture-' + role,
                'proposal_id': 'gate-review-fixture', 'packet_sha256': self.packet['packet_sha256'],
                'finding': 'synthetic injected review', 'evidence_locator': 'unbound source',
                'evidence_paths': ['not-in-packet.txt'], 'severity': 'nonblocking'}
            self.write(role + '.json', review)
            # Deliberately exercise a restored/injected event, not submit_review validation.
            self.session.append('review', {'review': review, 'file': self.session.snapshot([role + '.json'])[0]})
        self.session.append('decision', {'packet_sha256': self.packet['packet_sha256'],
            'proposal_id': 'gate-review-fixture', 'decision': 'PROCEED'})
        self.must_not_execute('evidence|review')

    def test_valid_reviews_still_allow_bounded_execution(self):
        self.prepare()
        self.review('critic')
        self.review('supervisor')
        self.assertEqual(self.session.decide()['payload']['decision'], 'PROCEED')
        with patch.object(module.benchmark, 'evaluate', return_value={'direction_decision': 'INCONCLUSIVE', 'synthetic_test_only': True}) as evaluate:
            result = self.session.experiment('data')
            evaluate.assert_called_once()
        self.assertEqual(result['payload']['decision'], 'SEARCH_MORE')


if __name__ == '__main__':
    unittest.main()
