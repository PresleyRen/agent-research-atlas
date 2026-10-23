import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/agent-research-atlas/scripts'))
import retrieval_benchmark as b

class RetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=ROOT/'evals/real_research_cycle/scifact_smoke'

    def test_real_scifact_claim_123_has_genuine_gold_relation(self):
        corpus,queries,qrels,p=b.load_beir(self.data)
        self.assertIn('123',queries)
        self.assertIn('4883040',qrels['123'])
        self.assertIn('Antiretroviral therapy',corpus['4883040']['text'])
        self.assertIn('reduction',corpus['4883040']['text'])
        self.assertEqual(p['labeled_positive_queries'],1)

    def test_real_scifact_demo_no_fake_statistical_confidence(self):
        r=b.evaluate(self.data,k=3)
        self.assertEqual(r['evaluation_queries'],1)
        self.assertEqual(r['direction_decision'],'INSUFFICIENT_QUERY_UNITS')
        self.assertEqual(r['differences']['ndcg']['status'],'insufficient_units_for_interval')
        self.assertIsNone(r['differences']['ndcg']['ci_95'])
        self.assertEqual(r['scientific_verdict'],'not_assessed')

    def test_bm25_scores_depend_on_content_not_gold(self):
        corpus,queries,qrels,p=b.load_beir(self.data)
        engine=b.BM25(corpus,title_weight=1)
        ranks=engine.rank(queries['123']['text'],3)
        self.assertEqual(ranks[0],'4883040')
        self.assertEqual(b.per_query(set(qrels['123']),ranks,3)['recall'],1.0)

    def test_metrics_correct_for_partial_relevance(self):
        p=b.per_query({'a','b'},['c','b','a'],3)
        self.assertEqual(p['recall'],1)
        self.assertAlmostEqual(p['mrr'],0.5)
        self.assertLess(p['ndcg'],1)

    def test_empty_retriever_yields_zero_without_hiding_failures(self):
        p=b.per_query({'a'},[],3)
        self.assertEqual(p,{'recall':0.0,'mrr':0.0,'ndcg':0.0})

    def test_paired_bootstrap_interval_requires_20_independent_queries(self):
        sample=[{'baseline':{'mrr':0.1},'variant':{'mrr':0.2}}]*19
        self.assertIsNone(b.bootstrap_diff(sample,'mrr')['ci_95'])
        sample.append({'baseline':{'mrr':0.0},'variant':{'mrr':0.2}})
        self.assertIsNotNone(b.bootstrap_diff(sample,'mrr')['ci_95'])
        self.assertAlmostEqual(b.bootstrap_diff(sample,'mrr')['delta'],0.105)

    def test_every_ranked_id_kept_for_independent_metric_audit(self):
        result=b.evaluate(self.data,k=3)
        row=result['per_query'][0]
        corpus,queries,labels,meta=b.load_beir(self.data)
        self.assertLessEqual(len(row['baseline_top_ids']),min(3,len(corpus)))
        self.assertLessEqual(len(row['variant_top_ids']),min(3,len(corpus)))
        self.assertGreater(len(row['baseline_top_ids']),0)
        self.assertEqual(len(row['baseline_top_ids']),len(set(row['baseline_top_ids'])))

    def test_scifact_source_file_hashes_are_reproducible(self):
        out=b.evaluate(self.data,k=3)
        for name,key in [('corpus.jsonl','corpus_sha256'),('queries.jsonl','queries_sha256'),('qrels/test.tsv','qrels_sha256')]:
            self.assertEqual(out['source_files'][key],b.sha256(self.data/name))

    def test_does_not_accept_qrels_with_unknown_doc(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            shutil.copytree(self.data,dest/'data')
            (dest/'data/qrels/test.tsv').write_text('query-id\tcorpus-id\tscore\n123\tmissing\t1\n')
            with self.assertRaises(b.BenchmarkError):b.load_beir(dest/'data')

    def test_does_not_accept_duplicate_qrels(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            shutil.copytree(self.data,dest/'data')
            (dest/'data/qrels/test.tsv').write_text('query-id\tcorpus-id\tscore\n123\t4883040\t1\n123\t4883040\t1\n')
            with self.assertRaises(b.BenchmarkError):b.load_beir(dest/'data')

    def test_no_ground_truth_yields_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            shutil.copytree(self.data,dest/'data')
            (dest/'data/qrels/test.tsv').write_text('query-id\tcorpus-id\tscore\n123\t4883040\t0\n')
            with self.assertRaises(b.BenchmarkError):b.load_beir(dest/'data')

    def test_benchmark_cannot_overwrite_previous_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'r.json'
            p.write_text('existing')
            rc=b.main(['--data-dir',str(self.data),'--k','3','--output',str(p)])
            self.assertEqual(rc,2)
            self.assertEqual(p.read_text(),'existing')

    def test_metric_mean_is_bounded(self):
        r=b.evaluate(self.data,k=3)
        for v in r['means'].values():
            self.assertTrue(all(0<=x<=1 for x in v.values()))

    def test_unexpected_title_weight_fails(self):
        corpus,_,_,_=b.load_beir(self.data)
        with self.assertRaises(b.BenchmarkError):b.BM25(corpus,title_weight=999)

if __name__=='__main__':unittest.main()
