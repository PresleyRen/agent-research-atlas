#!/usr/bin/env python3
"""Reproducible BEIR-format BM25 comparison; genuine qrels required.

No trained model, no claim to measure answer generation. Retains per-query metrics,
input hashes, and invalid/equivocal results rather than cherry-picking.
"""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
import csv
import hashlib
import json
from math import log, log2
from pathlib import Path
import random
import re
import statistics
import sys

class BenchmarkError(ValueError):pass

def sha256(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def terms(value):return re.findall(r"[a-z0-9]+",value.lower())

def load_jsonl(path, fields):
    records={}
    with Path(path).open(encoding='utf-8') as handle:
        for line,raw in enumerate(handle,1):
            if not raw.strip():continue
            try:item=json.loads(raw)
            except json.JSONDecodeError as e:raise BenchmarkError(f'{path}:{line} invalid json') from e
            key=str(item.get('_id',''))
            if not key or key in records or not all(isinstance(item.get(k,''),str) for k in fields):
                raise BenchmarkError(f'{path}:{line} missing/duplicate id or field')
            records[key]=item
    if not records:raise BenchmarkError('empty JSONL: '+str(path))
    return records


def load_beir(root,split='test'):
    root=Path(root)
    files=(root/'corpus.jsonl',root/'queries.jsonl',root/'qrels'/f'{split}.tsv')
    if any(not f.is_file() for f in files):raise BenchmarkError('BEIR corpus.jsonl, queries.jsonl, qrels/<split>.tsv required')
    corpus=load_jsonl(files[0],('title','text'))
    queries=load_jsonl(files[1],('text',))
    qrels=defaultdict(dict)
    with files[2].open(encoding='utf-8') as f:
        reader=csv.reader(f,delimiter='\t')
        head=next(reader,None)
        if not head or [x.strip().lower() for x in head] not in (['query-id','corpus-id','score'],['query_id','doc_id','score']):
            raise BenchmarkError('unexpected qrels TSV header')
        for line,row in enumerate(reader,2):
            if len(row)!=3:raise BenchmarkError(f'invalid qrel at line {line}')
            q,d,score=row
            if not q or not d or q not in queries or d not in corpus:raise BenchmarkError(f'unknown qrel ids at line {line}')
            if d in qrels[q]:raise BenchmarkError(f'duplicate qrel at line {line}')
            try:value=float(score)
            except ValueError as e:raise BenchmarkError('non-numeric qrel score') from e
            if value < 0 or value > 100:raise BenchmarkError('out of range qrel')
            qrels[q][d]=value
    gold={q:{d:v for d,v in docs.items() if v>0} for q,docs in qrels.items()}
    gold={q:v for q,v in gold.items() if v}
    if not gold:raise BenchmarkError('no labeled positive queries')
    return corpus, queries, gold, {'corpus_sha256':sha256(files[0]),'queries_sha256':sha256(files[1]),
       'qrels_sha256':sha256(files[2]),'corpus_docs':len(corpus),'all_queries':len(queries),
       'labeled_positive_queries':len(gold),'unlabeled_queries_excluded':len(queries)-len(gold),
       'source':'BEIR-format local files','split':split}

class BM25:
    def __init__(self,corpus, title_weight=1, k1=1.5,b=0.75):
        if title_weight not in (1,2):raise BenchmarkError('title_weight only fixed 1 or 2, not a searched hyperparameter')
        self.total=len(corpus);self.b=b;self.k1=k1
        self.tf={};self.post=defaultdict(list);self.length={};self.title_weight=title_weight
        for docid,record in corpus.items():
            # Predefined title duplication; no labels accessed during indexing/ranking.
            tokens=terms((record.get('title','')+' ')*title_weight+record.get('text',''))
            freq=Counter(tokens);self.length[docid]=len(tokens)
            for term,n in freq.items():self.post[term].append((docid,n))
        self.avgdl=sum(self.length.values())/self.total
        if not self.avgdl:raise BenchmarkError('empty tokenized corpus')

    def rank(self,query,k=10):
        scores=defaultdict(float)
        for word in set(terms(query)):
            postings=self.post.get(word,[])
            df=len(postings)
            if not df:continue
            idf=log(1+(self.total-df+0.5)/(df+0.5))
            for docid,tf in postings:
                denom=tf+self.k1*(1-self.b+self.b*self.length[docid]/self.avgdl)
                scores[docid]+=idf*tf*(self.k1+1)/denom
        return sorted(scores,key=lambda d:(-scores[d],d))[:k]


def per_query(gold,ranked,k):
    found=gold.intersection(ranked[:k]);recall=len(found)/len(gold)
    first=next((i+1 for i,d in enumerate(ranked[:k]) if d in gold),None)
    mrr=1/first if first else 0.0
    dcg=sum(1/log2(i+2) for i,d in enumerate(ranked[:k]) if d in gold)
    ideal=sum(1/log2(i+2) for i in range(min(len(gold),k)))
    return {'recall':recall,'mrr':mrr,'ndcg':dcg/ideal if ideal else 0.0}


def bootstrap_diff(per_case, metric, n_boot=1500, seed=2026):
    diffs=[x['variant'][metric]-x['baseline'][metric] for x in per_case]
    observed=statistics.mean(diffs)
    if len(diffs)<20:
        return {'delta':observed,'ci_95':None,'unit_count':len(diffs),'status':'insufficient_units_for_interval'}
    rng=random.Random(seed)
    values=[]
    for _ in range(n_boot):
        values.append(sum(rng.choices(diffs,k=len(diffs)))/len(diffs))
    values.sort()
    return {'delta':observed,'ci_95':[values[int(0.025*n_boot)],values[min(len(values)-1,int(0.975*n_boot))]],
            'unit_count':len(diffs),'status':'paired_query_bootstrap_exploratory'}


def direction_decision(ndcg_interval):
    '''A comparison is inconclusive when the paired interval spans no difference.'''
    if ndcg_interval['unit_count'] < 20 or ndcg_interval['ci_95'] is None:
        return 'INSUFFICIENT_QUERY_UNITS'
    low,high=ndcg_interval['ci_95']
    if low > 0:
        return 'FOLLOWUP_EXPERIMENT'  # Not scientific validation or a confirmatory trial.
    if high < 0:
        return 'KEEP_BASELINE'
    return 'INCONCLUSIVE'  # Positive point estimate alone is insufficient.

def evaluate(data_dir,split='test',k=10, max_queries=None):
    if not 1<=k<=100:raise BenchmarkError('k must be 1..100')
    corpus,queries,gold,provenance=load_beir(data_dir,split)
    ids=sorted(gold)
    # Study subset must be chosen without consulting text/labels; report subset rather than full claims.
    if max_queries is not None:
        if max_queries<1:raise BenchmarkError('max_queries must be positive')
        ids=ids[:max_queries]
    base=BM25(corpus,title_weight=1)
    var=BM25(corpus,title_weight=2)
    results=[]
    for q in ids:
        pred_a=base.rank(queries[q]['text'],k)
        pred_b=var.rank(queries[q]['text'],k)
        results.append({'query_id':q,'baseline':per_query(set(gold[q]),pred_a,k),
                        'variant':per_query(set(gold[q]),pred_b,k),
                        'baseline_top_ids':pred_a[:k], 'variant_top_ids':pred_b[:k]})
    means={kind:{metric:statistics.mean(x[kind][metric] for x in results) for metric in ('recall','mrr','ndcg')} for kind in ('baseline','variant')}
    diffs={metric:bootstrap_diff(results,metric) for metric in ('recall','mrr','ndcg')}
    recommend=direction_decision(diffs['ndcg'])
    # Scientific significance and publishable novelty are never inferred from this exploratory interval.
    cases={'better':sum(r['variant']['ndcg']>r['baseline']['ndcg'] for r in results),
           'worse':sum(r['variant']['ndcg']<r['baseline']['ndcg'] for r in results),
           'unchanged':sum(r['variant']['ndcg']==r['baseline']['ndcg'] for r in results)}
    return {'dataset':'BEIR-format retrieval, not generative RAG','source_files':provenance,
            'protocol':{'split':split,'k':k,'baseline':'BM25 all text title x1','variant':'BM25 title x2',
                        'k1':1.5,'b':0.75,'tokenizer':'regex lowercase ASCII tokens','selection':'sorted qrel-positive ids',
                        'title_weight_chosen_before_label_analysis':True},
            'evaluation_queries':len(ids),'means':means,'differences':diffs,
            'direction_decision':recommend,'query_outcomes_ndcg':cases,
            'scientific_verdict':'not_assessed','per_query':results,
            'limits':'Exploratory lexical retrieval comparison only. Full SciFact scores require official complete corpus and qrels; not LLM answer quality.'}


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument('--data-dir',required=True)
    p.add_argument('--split',default='test')
    p.add_argument('--k',type=int,default=10)
    p.add_argument('--max-queries',type=int)
    p.add_argument('--output',required=True)
    args=p.parse_args(argv)
    try:
        output=Path(args.output)
        if output.exists():raise BenchmarkError('output exists; do not overwrite raw experiment evidence')
        result=evaluate(args.data_dir,args.split,args.k,args.max_queries)
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
        print(json.dumps({'output':str(output),'queries':result['evaluation_queries'],
                          'means':result['means'],'differences':result['differences'],'decision':result['direction_decision']},indent=2))
        return 0
    except (OSError,ValueError) as e:
        print(json.dumps({'error':str(e)}),file=sys.stderr)
        return 2

if __name__=='__main__':raise SystemExit(main())
