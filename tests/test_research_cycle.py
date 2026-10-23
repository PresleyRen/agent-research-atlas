import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import sys
from unittest.mock import patch
from io import BytesIO

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/agent-research-atlas/scripts'))
import research_cycle as c

class EvidenceCycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers=ROOT/'evals/real_research_cycle/papers'
        cls.hsieh=(cls.papers/'hsieh_2024_excerpts.txt').read_text()
        cls.cuconasu=(cls.papers/'cuconasu_2025_excerpts.txt').read_text()
        cls.proposal=json.loads((ROOT/'evals/real_research_cycle/project/proposal.json').read_text())
        cls.reviews=json.loads((ROOT/'evals/real_research_cycle/project/reviews.json').read_text())

    def test_extract_actual_four_distinct_limitation_paragraphs(self):
        leads=c.gap_leads(self.hsieh.split('\f'),'doi:10.18653/v1/2024.findings-acl.890')
        self.assertEqual(len(leads),4)
        self.assertTrue(all(x['locator'].startswith('p.9') for x in leads))
        for fragment in ('Simplification of the mechanism behind positional attention bias','Computational overhead','Positional attention bias may be beneficial','The root cause of attention bias is unclear'):
            self.assertEqual(sum(fragment in row['excerpt'] for row in leads),1)

    def test_extracted_gap_is_candidate_not_verified_open(self):
        leads=c.gap_leads(self.hsieh.split('\f'),'paper-a')
        self.assertEqual({x['status'] for x in leads},{'candidate'})
        self.assertTrue(all(x['requires_later_work'] and not x['verified_open_gap'] for x in leads))
        self.assertEqual({x['source_kind'] for x in leads},{'author_stated_limitation'})

    def test_without_limitation_section_does_not_fabricate_gap(self):
        leads=c.gap_leads(self.cuconasu.split('\f'),'paper-b')
        self.assertEqual(leads,[])

    def test_no_name_or_empty_page_is_safe(self):
        with self.assertRaises(c.ResearchError):c.gap_leads(['Limitations\ntext'],'')
        self.assertEqual(c.gap_leads([''],'paper'),[])

    def test_ignores_reference_after_limitation(self):
        leads=c.gap_leads(['Limitations\nOverhead is limited.\n\nReferences\nFuture work and overhead unknown'],'a')
        self.assertEqual(len(leads),1)

    def test_citation_locator_must_be_matched_to_source(self):
        p={'paper_id':'doi:10.18653/v1/2024.findings-acl.890','title':'Found in the middle','doi':'10.18653/v1/2024.findings-acl.890','url':'https://aclanthology.org/2024.findings-acl.890/','year':2024}
        quote='Specifically, we require extra O(K) model forward passes'
        obj=c.citation_entry(p,'Method requires extra passes',quote,'PDF p.9 limitations',self.hsieh,cannot_support='All settings incur identical exact overhead')
        self.assertEqual(obj['source_access'],'local_excerpt')
        self.assertEqual(obj['verification'],'source_passage_matched_not_scientifically_adjudicated')
        with self.assertRaises(c.ResearchError):c.citation_entry(p,'Unsupported universal claim','Never requires extra passes','PDF p.9',self.hsieh,cannot_support='none')

    def test_fulltext_claim_cannot_be_forged_from_short_excerpt(self):
        p={'paper_id':'p','title':'Found in the middle','doi':'10.18653/v1/2024.findings-acl.890','url':'https://aclanthology.org/2024.findings-acl.890/'}
        phrase='extra O(K) model forward passes'
        with self.assertRaisesRegex(c.ResearchError,'fulltext citation requires'):
            c.citation_entry(p,'extra overhead',phrase,'PDF p.9',self.hsieh,
                cannot_support='every model',source_access='fulltext')
        row=c.citation_entry(p,'extra overhead',phrase,'PDF p.9',self.hsieh,
            cannot_support='every model',source_access='fulltext',source_read_depth='fulltext_extracted')
        self.assertEqual(row['source_access'],'fulltext')

    def test_citation_source_depth_cannot_be_falsified(self):
        paper={'paper_id':'p','title':'Paper','doi':'10.1/test','url':'https://aclanthology.org/a'}
        with self.assertRaises(c.ResearchError):
            c.citation_entry(paper,'claim','phrase','p.1','phrase',cannot_support='nothing',source_access='verified_fulltext_without_reading')

    def test_citation_missing_scope_rejected(self):
        p={'paper_id':'a','title':'b','doi':'c','url':'https://x.org'}
        with self.assertRaises(c.ResearchError):c.citation_entry(p,'claim','same','loc','same',cannot_support='')

    def test_actual_paper_bibliography_does_not_invent_author(self):
        p={'paper_id':'paper','title':'Found in the middle','doi':'10.18653/v1/2024.findings-acl.890','url':'https://aclanthology.org/2024.findings-acl.890/'}
        b=c.bibtex([p])
        self.assertIn('10.18653/v1/2024.findings-acl.890',b)
        self.assertNotIn('author =',b)

    def test_acl_conference_paper_bibtex_not_mislabeled_journal(self):
        p={'paper_id':'doi:10.18653/v1/2024.findings-acl.890',
           'title':'Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization',
           'doi':'10.18653/v1/2024.findings-acl.890','year':2024,
           'url':'https://aclanthology.org/2024.findings-acl.890/'}
        bib=c.bibtex([p])
        self.assertTrue(bib.startswith('@inproceedings{'))
        self.assertIn('year = {2024}',bib)
        with_venue=c.bibtex([dict(p,booktitle='Findings of ACL 2024')])
        self.assertIn('booktitle = {Findings of ACL 2024}',with_venue)
        other=c.bibtex([dict(p,doi='10.1234/unknown')])
        self.assertTrue(other.startswith('@misc{'))

    def test_duplicate_doi_bibtex_rejected(self):
        p={'paper_id':'x','title':'A','doi':'10.5/a'}
        with self.assertRaises(c.ResearchError):c.bibtex([p,p])

    def test_real_2025_counterevidence_causes_pivot(self):
        action,reason=c.decide(self.proposal,self.reviews)
        self.assertEqual(action,'PIVOT')
        self.assertIn('mechanism',reason)

    def test_unconfirmed_data_after_narrowing_repairs_before_pilot(self):
        updated=copy.deepcopy(self.reviews)
        for review in updated:
            review['severity']='nonblocking'
            review['failure_type']='scope'
        self.assertEqual(c.decide(self.proposal,updated)[0],'REPAIR_MEASUREMENT')

    def test_source_absence_requires_search_more(self):
        p=copy.deepcopy(self.proposal)
        p['primary_source_locator']=''
        self.assertEqual(c.decide(p,self.reviews)[0],'SEARCH_MORE')

    def test_later_work_absence_requires_search_more(self):
        p=copy.deepcopy(self.proposal)
        p['later_work_checked']=False
        self.assertEqual(c.decide(p,self.reviews)[0],'SEARCH_MORE')

    def test_solved_gap_always_pivots(self):
        p=copy.deepcopy(self.proposal)
        p['gap_status']='solved'
        self.assertEqual(c.decide(p,self.reviews)[0],'PIVOT')

    def test_no_residual_gap_narrows(self):
        p=copy.deepcopy(self.proposal)
        p['distinct_remaining_gap']=''
        self.assertEqual(c.decide(p,self.reviews)[0],'NARROW')

    def test_data_unavailable_parks_candidate(self):
        p=copy.deepcopy(self.proposal)
        p['data']='unavailable'
        reviews=copy.deepcopy(self.reviews)
        for review in reviews: review['severity']='nonblocking'
        self.assertEqual(c.decide(p,reviews)[0],'PARK')

    def test_missing_critic_blocks_proceed(self):
        p=copy.deepcopy(self.proposal)
        p['feasibility']={k:'available' for k in ('data','compute','evaluation','budget')}
        self.assertEqual(c.decide(p,[self.reviews[0]])[0],'SEARCH_MORE')

    def test_proceed_requires_real_local_data_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            p=copy.deepcopy(self.proposal)
            p['feasibility']={k:'available' for k in ('data','compute','evaluation','budget')}
            rev=copy.deepcopy(self.reviews)
            for row in rev:row['severity']='nonblocking'
            (root/'proposal.json').write_text(json.dumps(p))
            (root/'reviews.json').write_text(json.dumps(rev))
            self.assertEqual(c.decide(p,rev)[0],'PROCEED')
            with self.assertRaises(c.ResearchError):c.run_cycle(root,'proposal.json','reviews.json')
            self.assertFalse((root/'research-atlas').exists())

    def test_data_contract_detects_tampered_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'corpus.txt').write_text('one doc')
            p={'data_contract':{'measured_construct':'retrieval evidence','metric':'recall@10','ground_truth_provenance':'official qrels',
                 'files':[{'role':'dataset','path':'corpus.txt','sha256':'0'*64},{'role':'labels','path':'corpus.txt','sha256':'0'*64}]}}
            with self.assertRaises(c.ResearchError):c.validate_data_contract(root,p)

    def test_sha_matching_but_invalid_beir_labels_still_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'qrels').mkdir()
            files=[]
            inputs={'corpus.jsonl':('{"_id":"d1","title":"Paper","text":"abstract"}\n','corpus'),
                    'queries.jsonl':('{"_id":"q1","text":"abstract"}\n','queries'),
                    'qrels/test.tsv':('query-id\tcorpus-id\tscore\nq1\tmissing-doc\t1\n','qrels')}
            for name,(text,role) in inputs.items():
                (root/name).write_text(text)
                files.append({'role':role,'path':name,'sha256':c.digest((root/name).read_bytes())})
            proposal={'required_measurements':['retrieval_relevance'], 'data_contract':{
                'measured_construct':'document retrieval','metric':'nDCG@10',
                'ground_truth_provenance':'original BEIR format',
                'measurement_capabilities':['retrieval_relevance'], 'files':files}}
            with self.assertRaisesRegex(c.ResearchError,'BEIR identifiers/labels invalid'):
                c.validate_data_contract(root,proposal)

    def test_data_contract_requires_actual_ground_truth(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'one').write_text('one')
            p={'data_contract':{'measured_construct':'retrieval','metric':'MRR','ground_truth_provenance':'official',
               'files':[{'role':'dataset','path':'one','sha256':c.digest(b'one')}]}}
            with self.assertRaises(c.ResearchError):c.validate_data_contract(root,p)

    def test_fixed_local_data_supports_only_bounded_pilot(self):
        root=ROOT/'evals/real_research_cycle'
        files=[]
        for name,role in [('scifact_smoke/corpus.jsonl','corpus'),('scifact_smoke/queries.jsonl','queries'),('scifact_smoke/qrels/test.tsv','qrels')]:
            files.append({'role':role,'path':name,'sha256':c.digest((root/name).read_bytes())})
        p={'required_measurements':['retrieval_relevance'], 'data_contract':{'measured_construct':'document retrieval','metric':'nDCG@3','ground_truth_provenance':'SciFact official example claim #123', 'measurement_capabilities':['retrieval_relevance'], 'files':files}}
        result=c.validate_data_contract(root,p)
        self.assertEqual(result['status'],'file_lineage_checked')
        self.assertEqual(result['measurement_validity'],'requires_scientific_review')

    def test_scifact_retrieval_data_cannot_claim_long_context_generation(self):
        root=ROOT/'evals/real_research_cycle'
        files=[]
        for path,role in [('scifact_smoke/corpus.jsonl','corpus'),('scifact_smoke/queries.jsonl','queries'),('scifact_smoke/qrels/test.tsv','qrels')]:
            files.append({'role':role,'path':path,'sha256':c.digest((root/path).read_bytes())})
        p={'required_measurements':['answer_quality','long_context_position'],
            'data_contract':{'measured_construct':'document retrieval','metric':'MRR@3',
              'ground_truth_provenance':'SciFact documentation', 'measurement_capabilities':['retrieval_relevance'], 'files':files}}
        with self.assertRaisesRegex(c.ResearchError,'dataset cannot measure'):
            c.validate_data_contract(root,p)

    def test_real_scifact_annotation_rejects_false_support_claim(self):
        rows=[{'id':123,'claim':'Antiretroviral therapy increases TB',
               'evidence':{'4883040':[{'label':'CONTRADICT','sentences':[0]}]}}]
        a=c.scifact_polarity_audit(rows,[{'claim_id':123,'doc_id':4883040,'asserted_relation':'SUPPORT'}])
        self.assertEqual(a['mismatches'],1)
        self.assertEqual(a['checks'][0]['status'],'contradicts_annotated_relation')
        b=c.scifact_polarity_audit(rows,[{'claim_id':'123','doc_id':'4883040','asserted_relation':'CONTRADICT'}])
        self.assertEqual(b['mismatches'],0)

    def test_real_scifact_no_annotation_is_not_support(self):
        claims=[{'id':263,'evidence':{'11328820':[{'label':'CONTRADICT','sentences':[7,9]}]}}]
        r=c.scifact_polarity_audit(claims,[{'claim_id':263,'doc_id':14853989,'asserted_relation':'SUPPORT'}])
        self.assertEqual(r['checks'][0]['status'],'no_annotated_evidence')

    def test_atlas_export_keeps_leads_as_candidates_and_stable_ids(self):
        leads=c.gap_leads(self.hsieh.split('\f'),'paper')
        paper={'title':'Found in the middle','doi':'10.18653/v1/2024.findings-acl.890',
               'url':'https://aclanthology.org/2024.findings-acl.890/'}
        a=c.export_atlas_batch(paper,leads,'papers/hsieh_2024_excerpts.txt','2026-10-22')
        b=c.export_atlas_batch(paper,leads,'papers/hsieh_2024_excerpts.txt','2026-10-22')
        self.assertEqual(a,b)
        self.assertEqual(len(a['nodes']),5)
        self.assertEqual(len(a['edges']),4)
        self.assertEqual({n['status'] for n in a['nodes'][1:]},{'candidate'})
        self.assertTrue(all(n['data']['later_work_checked'] is False for n in a['nodes'][1:]))
        self.assertTrue(all(n['sources'][0]['access']=='local' for n in a['nodes']))

    def test_atlas_export_refuses_fabricated_open_gap(self):
        leads=c.gap_leads(self.hsieh.split('\f'),'paper')
        leads[0]['status']='open';leads[0]['verified_open_gap']=True
        paper={'title':'Found in the middle','doi':'10.18653/v1/2024.findings-acl.890',
               'url':'https://aclanthology.org/2024.findings-acl.890/'}
        with self.assertRaises(c.ResearchError):
            c.export_atlas_batch(paper,leads,'papers/hsieh_2024_excerpts.txt','2026-10-22')

    def test_crossref_metadata_from_real_id_without_fabricated_fields(self):
        fixture={'message':{'items':[{'DOI':'10.18653/v1/2025.emnlp-main.1422', 'title':['Do RAG Systems Really Suffer From Positional Bias?'],
            'author':[{'given':'Florin','family':'Cuconasu'}],'published':{'date-parts':[[2025,11,1]]}, 'is-referenced-by-count':9}]}}
        def fetch(url):
            self.assertIn('api.crossref.org/works?',url)
            return {'content':json.dumps(fixture).encode(),'sha256':'a'*64,'fetched_at':'2026-10-22'}
        out=c.crossref_query('RAG position bias',3,fetcher=fetch)
        self.assertEqual(out['records'][0]['title'],fixture['message']['items'][0]['title'][0])
        self.assertEqual(out['records'][0]['access'],'metadata')
        self.assertEqual(out['records'][0]['authors'],['Florin Cuconasu'])

    def test_crossref_response_without_ids_is_not_invented(self):
        data={'message':{'items':[{'title':['Paper no DOI']} ]}}
        out=c.crossref_query('literature review',1,fetcher=lambda u:{'content':json.dumps(data).encode(),'sha256':'a','fetched_at':'2026'})
        self.assertEqual(out['records'],[])

    def test_acl_html_metadata_parser(self):
        data=b'<html><head><meta name="citation_title" content="Found in the middle"><meta name="citation_doi" content="10.18653/v1/2024.findings-acl.890"><meta name="citation_author" content="Cheng-Yu Hsieh"></head></html>'
        out=c.acl_metadata('https://aclanthology.org/2024.findings-acl.890/',fetcher=lambda u:{'content':data,'sha256':'a','fetched_at':'2026','content_type':'text/html'})
        self.assertEqual(out['doi'],'10.18653/v1/2024.findings-acl.890')
        self.assertEqual(out['authors'],['Cheng-Yu Hsieh'])

    def test_bad_acl_metadata_is_rejected_not_guessed(self):
        with self.assertRaises(c.ResearchError):c.acl_metadata('https://aclanthology.org/../../private',fetcher=lambda u:{})

    def test_public_fetch_is_allowlisted(self):
        for url in ('http://aclanthology.org/123','file:///etc/passwd','https://localhost/admin','https://example.com/secret'):
            with self.subTest(url=url):
                with self.assertRaises(c.ResearchError):c.fetch_public(url)

    def test_local_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'source.txt').write_text('text');(root/'link.txt').symlink_to(root/'source.txt')
            with self.assertRaises(c.ResearchError):c.read_paper_pages('link.txt',root)

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(c.ResearchError):c.within(tmp,'../x')

    def test_finite_cycle_preserves_prior_decisions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'proposal.json').write_text(json.dumps(self.proposal))
            (root/'reviews.json').write_text(json.dumps(self.reviews))
            a=c.run_cycle(root,'proposal.json','reviews.json')
            b=c.run_cycle(root,'proposal.json','reviews.json')
            self.assertEqual((a['result']['sequence'],b['result']['sequence']),(1,2))
            self.assertEqual(a['result']['decision'],'PIVOT')
            self.assertTrue((root/a['path']).is_file())
            self.assertNotEqual(a['path'],b['path'])

    def test_cycle_rejects_bad_paper_review_evidence(self):
        malformed=copy.deepcopy(self.reviews)
        malformed[0]['evidence_locator']=''
        with self.assertRaises(c.ResearchError):c.decide(self.proposal,malformed)

    def test_queue_pivots_then_stops_on_measurement_blocker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,content in [('first.json',self.proposal),('review1.json',self.reviews)]:
                (root/name).write_text(json.dumps(content))
            second=copy.deepcopy(self.proposal);second['proposal_id']='rag-reformulated'
            reviews=copy.deepcopy(self.reviews)
            for row in reviews:row['proposal_id']='rag-reformulated';row['severity']='nonblocking'
            (root/'second.json').write_text(json.dumps(second))
            (root/'review2.json').write_text(json.dumps(reviews))
            (root/'queue.json').write_text(json.dumps({'tasks':[{'proposal':'first.json','reviews':'review1.json'}, {'proposal':'second.json','reviews':'review2.json'}]}))
            out=c.run_queue(root,'queue.json')
            self.assertEqual(out['processed'],2)
            self.assertEqual(out['actions'][0]['result']['decision'],'PIVOT')
            self.assertEqual(out['outcome'],'REPAIR_MEASUREMENT')
            self.assertEqual(len(list((root/'research-atlas/supervision').glob('decision-*.json'))),2)

    def test_queue_budget_limit_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'q.json').write_text(json.dumps({'tasks':[{}]*21}))
            with self.assertRaises(c.ResearchError):c.run_queue(root,'q.json')

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'a.json';p.write_text('{"a":1,"a":2}')
            with self.assertRaises(c.ResearchError):c.read_json(p)

if __name__=='__main__':unittest.main()
