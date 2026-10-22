"""Deterministic decision tests over live-verified real scholarly metadata.

No network or model run occurs inside these tests. External source reading and
metadata verification are documented separately from these repeatable checks.
"""
from pathlib import Path
from urllib.parse import urlparse
import json
import unittest

FIXTURE = Path(__file__).resolve().parents[1] / 'evals' / 'real_literature' / 'agent_rag_position_bias.json'

class RealLiteratureDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding='utf-8'))
        cls.papers = {p['id']: p for p in cls.data['papers']}
        cls.claims = {c['id']: c for c in cls.data['claims']}

    def test_real_sources_have_unique_grounded_ids_and_dois(self):
        self.assertGreaterEqual(len(self.papers), 5)
        self.assertEqual(len(self.papers), len({p['doi'].lower() for p in self.papers.values()}))
        for paper in self.papers.values():
            self.assertTrue(paper['title'] and paper['doi'] and paper['locator'])
            self.assertEqual(urlparse(paper['url']).hostname, 'aclanthology.org')
            self.assertIn(paper['access'], {'metadata', 'abstract', 'fulltext', 'local'})
            self.assertTrue(paper['can_support'] and paper['cannot_support'])

    def test_actual_fulltext_and_abstract_depths_are_not_confused(self):
        self.assertEqual(self.papers['liu-2024-lost-middle']['access'], 'fulltext')
        for pid in ('hsieh-2024-found-middle','yu-2025-channel','cuconasu-2025-rag-position'):
            self.assertEqual(self.papers[pid]['access'], 'abstract')

    def test_no_mitigation_novelty_claim_fails_on_later_real_papers(self):
        c = self.claims['claim-no-mitigation-exists']
        self.assertEqual(c['verdict'], 'contradicted')
        self.assertGreaterEqual(len(c['conflict_ids']), 2)
        self.assertTrue(all('later_mitigation' in self.papers[p]['roles'] for p in c['conflict_ids']))

    def test_realistic_rag_counterevidence_blocks_universal_claim(self):
        c = self.claims['claim-rag-always-position-dominated']
        self.assertEqual(c['verdict'], 'unsupported_generalization')
        self.assertIn('cuconasu-2025-rag-position', c['conflict_ids'])

    def test_perfect_retrieval_counterexample_is_not_ignored(self):
        c = self.claims['claim-perfect-retrieval-guarantees-success']
        self.assertEqual(c['verdict'], 'contradicted')
        self.assertIn('du-2025-perfect-retrieval', c['conflict_ids'])

    def test_gap_requires_later_work_and_keeps_scoped_status(self):
        gap = self.data['gaps'][0]
        self.assertEqual(gap['status'], 'partially_solved')
        self.assertEqual(gap['decision'], 'SEARCH_MORE')
        self.assertTrue(set(gap['later_paper_ids']) <= set(self.papers))
        self.assertTrue(gap['unresolved_part'] and gap['reason'])
        self.assertNotEqual(gap['status'], 'open')

    def test_unverified_resources_do_not_become_testable(self):
        f = self.data['candidate_feasibility']
        self.assertTrue(any(f[k] != 'available' for k in ('data','compute','evaluation','budget')))
        self.assertNotEqual(f['allowed_status'], 'testable')
        self.assertEqual(f['decision'], 'SEARCH_MORE')

    def test_no_claim_has_broken_citation_ids(self):
        for c in self.data['claims']:
            self.assertTrue(set(c['evidence_ids'] + c['conflict_ids']) <= set(self.papers))
            if c['verdict'] == 'bounded_supported':
                self.assertGreater(len(c['evidence_ids']), 0)
                self.assertEqual(c['conflict_ids'], [])
            if c['verdict'] == 'unverified':
                self.assertEqual(c['evidence_ids'], [])

if __name__ == '__main__':
    unittest.main()
