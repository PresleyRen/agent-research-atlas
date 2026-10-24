import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/agent-research-atlas/scripts'))
import research_session as s
import research_cycle as c

class SessionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.session=s.Session(self.root)
        self.proposal={'proposal_id':'p1','primary_source_locator':'source.txt p.1','later_work_checked':True,
            'distinct_remaining_gap':'candidate not certified','gap_status':'candidate',
            'feasibility':dict.fromkeys(['data','compute','evaluation','budget'],'available'),
            'minimal_test':'test','rival_prediction':'rival'}
        self.write('source.txt','actual source')
        self.write('proposal.json',self.proposal)
        self.packet=self.session.prepare('proposal.json',['source.txt'],'scientist')['payload']
    def write(self,path,obj):
        (self.root/path).write_text(obj if isinstance(obj,str) else json.dumps(obj))
    def review(self,role='critic',**updates):
        r={'role':role,'reviewer_id':role+'-independent','proposal_id':'p1',
           'packet_sha256':self.packet['packet_sha256'],'finding':'Evidence limits claim',
           'evidence_locator':'source.txt p.1','evidence_paths':['source.txt'],
           'severity':'nonblocking'};r.update(updates)
        self.write(role+'.json',r);return self.session.submit_review(role+'.json')
    def test_missing_reviews_searches_not_proceeds(self):
        self.assertEqual(self.session.decide()['payload']['decision'],'SEARCH_MORE')
    def test_self_review_rejected(self):
        with self.assertRaisesRegex(c.ResearchError,'self-review'):self.review(reviewer_id='scientist')
    def test_reused_identity_rejected(self):
        self.review(reviewer_id='same')
        with self.assertRaisesRegex(c.ResearchError,'distinct'):self.review('supervisor',reviewer_id='same')
    def test_stale_review_rejected(self):
        with self.assertRaisesRegex(c.ResearchError,'stale'):self.review(packet_sha256='bad')
    def test_unbound_evidence_rejected(self):
        with self.assertRaisesRegex(c.ResearchError,'packet evidence'):self.review(evidence_paths=['invented.txt'])
    def test_evidence_change_rejected(self):
        self.write('source.txt','changed')
        with self.assertRaisesRegex(c.ResearchError,'changed'):self.review()
    def test_review_change_rejected(self):
        self.review();self.write('critic.json',{})
        with self.assertRaisesRegex(c.ResearchError,'changed'):self.session.decide()
    def test_blocker_pivots_and_revision_preserves_history(self):
        self.review(severity='blocking',failure_type='invalid_mechanism',resolved=False)
        self.review('supervisor')
        self.assertEqual(self.session.decide()['payload']['decision'],'PIVOT')
        self.proposal['proposal_id']='p2';self.write('revised.json',self.proposal)
        self.session.prepare('revised.json',['source.txt'],'scientist')
        self.assertEqual(len(self.session.events()),5)
        self.assertEqual(self.session.events()[0]['payload']['proposal']['proposal_id'],'p1')
    def test_missing_data_becomes_repair_not_exception(self):
        self.review();self.review('supervisor')
        self.assertEqual(self.session.decide()['payload']['decision'],'REPAIR_MEASUREMENT')
    def test_repeated_decision_rejected(self):
        self.session.decide()
        with self.assertRaisesRegex(c.ResearchError,'already'):self.session.decide()
    def test_execution_without_gate_rejected(self):
        with self.assertRaisesRegex(c.ResearchError,'PROCEED'):self.session.experiment('data')
    def test_resume_validates_chain(self):
        self.review();path=self.session.directory/'event-0001.json'
        value=json.loads(path.read_text());value['payload']['scientist_id']='forged';path.write_text(json.dumps(value))
        with self.assertRaisesRegex(c.ResearchError,'chain'):s.Session(self.root).events()
    def test_path_escape_rejected(self):
        with self.assertRaises(c.ResearchError):self.session.snapshot(['../outside'])
    def test_benchmark_does_not_attest_preregistration(self):
        source=(ROOT/'skills/agent-research-atlas/scripts/retrieval_benchmark.py').read_text()
        self.assertIn("'title_weight_chosen_before_label_analysis':'not_verified_by_runner'",source)

    def test_discovery_rejects_unbounded_sources(self):
        with self.assertRaises(c.ResearchError):self.session.discover('research topic',['x']*6)

    def test_discovery_preserves_failed_fetch_and_auditable_history(self):
        with patch.object(c,'crossref_query',side_effect=c.ResearchError('network unavailable')):
            with self.assertRaises(c.ResearchError):self.session.discover('research topic',['https://aclanthology.org/test/'])
        self.assertEqual(self.session.events()[-1]['kind'],'discovery_failure')
        failure=self.root/'research-atlas/session/discovery-0001/failure.json'
        self.assertIn('network unavailable',failure.read_text())
        with self.assertRaisesRegex(c.ResearchError,'partial discovery'):self.session.discover('research topic',['https://aclanthology.org/test/'])

    def test_followup_requires_search_decision(self):
        with self.assertRaises(c.ResearchError):self.session.search_more('new research question')

    def test_actual_followup_receipt_allows_new_proposal(self):
        self.session.decide()
        with patch.object(c,'crossref_query',return_value={'records':[],'access':'metadata'}):
            result=self.session.search_more('new research question')
        self.assertEqual(result['kind'],'followup_search')
        self.proposal['proposal_id']='p2';self.write('revised.json',self.proposal)
        self.session.prepare('revised.json',['source.txt'],'scientist')
        self.assertEqual(self.session.packet()['proposal']['proposal_id'],'p2')

    def test_revision_requires_explicit_decision(self):
        with self.assertRaises(c.ResearchError):self.session.prepare('proposal.json',['source.txt'],'scientist')

if __name__=='__main__':unittest.main()
