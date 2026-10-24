#!/usr/bin/env python3
"""Online, bounded real-source integration acceptance for Atlas v1.3.

Run only in user-authorized CI; downloads open BEIR SciFact and two ACL papers.
Outputs include input hashes and bounded, reproducible measurements. Does not
claim novel research, LLM answer accuracy, or professor judgement.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import sys

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'skills/agent-research-atlas/scripts'))
import fetch_beir as fetch
import research_cycle as cycle
import retrieval_benchmark as bench


def check(output):
    assert output['evaluation_queries']==300, f"Expected all 300 official SciFact test queries, got {output['evaluation_queries']}"
    assert output['source_files']['corpus_docs']==5183, f"Expected all 5,183 official documents, got {output['source_files']['corpus_docs']}"
    assert output['differences']['ndcg']['unit_count']==300
    assert output['differences']['ndcg']['ci_95'] is not None
    assert output['scientific_verdict']=='not_assessed'
    assert len(output['per_query'])==300
    assert 0<=output['means']['baseline']['ndcg']<=1
    assert 0<=output['means']['variant']['ndcg']<=1


def run_online(outdir):
    outdir=Path(outdir).resolve()
    outdir.mkdir(parents=True,exist_ok=True)
    data_dir,manifest=fetch.download_scifact(outdir/'scifact')
    score=bench.evaluate(data_dir,split='test',k=10)
    check(score)
    # Independently verify all 300 stored rankings against original qrels.
    corpus,queries,qrels,_=bench.load_beir(data_dir,split='test')
    for row in score['per_query']:
        gold=set(qrels[row['query_id']])
        for variant,rank_key in [('baseline','baseline_top_ids'),('variant','variant_top_ids')]:
            ranking=row[rank_key]
            assert len(ranking)<=10 and len(set(ranking))==len(ranking)
            matches=[rank in gold for rank in ranking]
            independently_computed_recall=sum(matches)/len(gold)
            independently_computed_mrr=next((1/(i+1) for i,match in enumerate(matches) if match),0.0)
            independently_computed_dcg=sum((1/math.log2(i+2)) for i,match in enumerate(matches) if match)
            ideal=sum(1/math.log2(i+2) for i in range(min(10,len(gold))))
            independently_computed_ndcg=independently_computed_dcg/ideal
            for metric,value in [('recall',independently_computed_recall),('mrr',independently_computed_mrr),('ndcg',independently_computed_ndcg)]:
                assert abs(value-row[variant][metric])<1e-12,(row['query_id'],variant,metric)
    inputs=[{'role':role,'path':str(path.relative_to(outdir)),'sha256':bench.sha256(path)}
            for role,path in [('corpus',Path(data_dir)/'corpus.jsonl'),('queries',Path(data_dir)/'queries.jsonl'),('qrels',Path(data_dir)/'qrels/test.tsv')]]
    contract={'required_measurements':['retrieval_relevance'],
             'data_contract':{'measured_construct':'document retrieval evidence relevance',
                 'metric':'nDCG@10','ground_truth_provenance':'official BEIR SciFact test qrels',
                 'measurement_capabilities':['retrieval_relevance'],'files':inputs}}
    data_audit=cycle.validate_data_contract(outdir,contract)
    assert data_audit['retrieval_ground_truth_check']['labeled_queries']==300
    assert data_audit['retrieval_ground_truth_check']['corpus_docs']==5183
    (outdir/'scifact-full-results.json').write_text(json.dumps(score,indent=2,ensure_ascii=False)+'\n')
    result={'data_contract':data_audit,'independent_metric_checks':300*2*3,
            'dataset':'BEIR SciFact official test','download_manifest':manifest,'qrels_metric':score['means'],
            'difference':score['differences']['ndcg'], 'decision':score['direction_decision'],
            'model_inference':'not_run','scientific_verdict':'not_assessed'}

    url='https://aclanthology.org/2024.findings-acl.890/'
    paper=cycle.acl_metadata(url)
    assert 'Found in the middle' in paper['title']
    assert paper['doi']=='10.18653/v1/2024.findings-acl.890'
    pdf=cycle.fetch_public(paper['pdf_url'],max_bytes=cycle.MAX_PDF_BYTES)
    # Preserve exact original bytes and actual page extraction for independent
    # inspection even if limitation-mining later fails its live assertion.
    (outdir/'hsieh-source.pdf').write_bytes(pdf['content'])
    pages=cycle.pdf_to_text(pdf['content'])
    (outdir/'hsieh-extracted-pages.txt').write_text('\f'.join(pages),encoding='utf-8')
    source={'pages':pages,'sha256':pdf['sha256'],
            'extracted_text_sha256':cycle.digest('\f'.join(pages).encode('utf-8')),
            'extraction_method':'pdftotext -raw','read_depth':'fulltext_extracted'}
    assert len(source['pages'])>=8
    leads=cycle.gap_leads(source['pages'],paper['paper_id'])
    (outdir/'hsieh-gap-candidates.json').write_text(json.dumps(leads,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    # Full PDF is read and limitation paragraphs are returned as *candidates*.
    expected=['Simplification of the mechanism behind','Computational overhead',
              'Positional attention bias may be beneficial', 'The root cause of attention bias is unclear']
    assert len(leads)==4, f'Expected four nonduplicated author limitations, found {len(leads)}'
    for heading in expected:
        assert sum(heading in x['excerpt'] for x in leads)==1, f'PDF limitation missing or duplicated: {heading}'
    assert all(x['locator'].startswith('p.9') for x in leads)
    assert all(x['status']=='candidate' and not x['verified_open_gap'] for x in leads)
    result['acl_fulltext']={'paper':paper['title'],'doi':paper['doi'],
                            'pdf_sha256':source['sha256'],
                            'extracted_text_sha256':source['extracted_text_sha256'],
                            'extraction_method':source['extraction_method'],
                            'extraction_environment':cycle.extraction_environment(),
                            'page_count':len(source['pages']), 'extracted_candidate_count':len(leads),
                            'limit_first_3':leads[:3], 'actual_text_depth':source['read_depth']}
    (outdir/'acl-paper-audit.json').write_text(json.dumps(result['acl_fulltext'],indent=2)+'\n')

    contrary=cycle.acl_metadata('https://aclanthology.org/2025.emnlp-main.1422/')
    assert contrary['doi']=='10.18653/v1/2025.emnlp-main.1422'
    result['counter_paper']={'paper':contrary['title'],'doi':contrary['doi'],'access':'metadata',
                             'scientific_role':'contrary publication, requires claim-scoped review'}
    (outdir/'online-summary.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--output-dir',required=True)
    args=p.parse_args()
    print(json.dumps(run_online(args.output_dir),indent=2,ensure_ascii=False))
