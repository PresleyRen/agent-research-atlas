#!/usr/bin/env python3
"""Deterministic research-evidence workflow, designed to complement Agent Research Atlas.

Public-source discovery is optional; all scientific conclusions require explicit
observations. No automatic peer-review / novelty verdict is supplied.
Python >= 3.10, standard library only.
"""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

MAX_SOURCE_BYTES = 16_000_000
MAX_PDF_BYTES = 40_000_000
VALID_DECISIONS = ('SEARCH_MORE', 'REPAIR_MEASUREMENT', 'NARROW', 'PROCEED', 'PIVOT', 'PARK', 'STOP')
GAP_STATES = ('candidate', 'open', 'partially_solved', 'solved', 'invalid_gap', 'inaccessible', 'unknown', 'parked')
HEADERS = ('limitations', 'limitation', 'future work', 'future directions', 'discussion', 'conclusion', 'conclusions', '局限性', '未来工作', '讨论')
TRIGGERS = ('however','unexplored','underexplored','yet','future','does not','did not','not address','remains','limited','limitations','may be','require','overhead','unknown','unclear', '尚未','仍然','局限','未来')

class ResearchError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def digest(content):
    return hashlib.sha256(content).hexdigest()


def read_json(path):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ResearchError('duplicate JSON key: '+key)
            out[key] = value
        return out
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(ResearchError('nonfinite JSON: '+x)))
    except (OSError, json.JSONDecodeError) as e:
        raise ResearchError('invalid JSON: '+str(e)) from e


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.is_symlink():
        raise ResearchError('refusing symlink destination')
    data=json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False)+'\n'
    # Never silently discard earlier decisions or evidence by replacing an existing record.
    if path.exists():
        raise ResearchError('destination exists: '+str(path))
    path.write_text(data,encoding='utf-8')
    return path


def safe_root(path):
    p=Path(path).expanduser().resolve()
    if not p.is_dir():
        raise ResearchError('existing project directory required')
    return p


def within(root, path):
    root = safe_root(root)
    p = Path(path)
    p = p if p.is_absolute() else root / p
    # Forbid any symlink in the project-relative path, including parents.
    try:
        rel = p.relative_to(root)
    except ValueError as e:
        raise ResearchError('file must be project-local') from e
    curr=root
    for part in rel.parts:
        if part == '..' or part in ('.',''):
            raise ResearchError('invalid path segment')
        curr=curr / part
        if curr.is_symlink():
            raise ResearchError('symlinks are not allowed in research artifacts')
    return curr


def fetch_public(url, max_bytes=MAX_SOURCE_BYTES, timeout=12):
    """Allowlisted read-only public scholarly API/ACL retrieval; never send credentials."""
    parsed=urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in {'api.crossref.org','api.openalex.org','aclanthology.org'}:
        raise ResearchError('URL is not an approved HTTPS public academic source')
    req=Request(url,headers={'User-Agent':'agent-research-atlas/1.3 (+research metadata; no crawling)'})
    try:
        with urlopen(req,timeout=timeout) as r:
            kind=r.headers.get('Content-Type','').lower()
            content=r.read(max_bytes+1)
            if len(content)>max_bytes: raise ResearchError('source too large')
            return {'url':url,'content':content,'content_type':kind,'fetched_at':now(),
                    'sha256':digest(content),'http_status':r.status}
    except (HTTPError,URLError,TimeoutError) as e:
        raise ResearchError('public source request failed: '+str(e)) from e


def crossref_query(topic, limit=10, fetcher=fetch_public):
    if not isinstance(topic,str) or len(topic.strip())<4 or not (1<=limit<=25):
        raise ResearchError('topic and limit required')
    q=urlencode({'query.bibliographic':topic.strip(),'rows':limit,'select':'DOI,title,author,published,URL,is-referenced-by-count,abstract'})
    url='https://api.crossref.org/works?'+q
    result=fetcher(url)
    if not isinstance(result.get('content'),bytes): raise ResearchError('request did not return bytes')
    raw=json.loads(result['content'].decode('utf-8'))
    records=[]
    for item in raw.get('message',{}).get('items',[]):
        title=item.get('title',[''])[0] if item.get('title') else ''
        doi=str(item.get('DOI','')).lower().strip()
        if not title or not doi: continue
        authors=[]
        for a in item.get('author',[]):
            name=' '.join(filter(None,[a.get('given',''),a.get('family','')])).strip()
            if name:authors.append(name)
        dates=item.get('published',{}).get('date-parts',[])
        year=dates[0][0] if dates and dates[0] else None
        records.append({'paper_id':'doi:'+doi,'title':title,'doi':doi,'year':year,'authors':authors,
                        'url':'https://doi.org/'+doi,'citation_count':item.get('is-referenced-by-count'),
                        'abstract':item.get('abstract'), 'access':'metadata',
                        'provider':'crossref','provenance':{'query_url':url,'response_sha256':result['sha256'],'fetched_at':result['fetched_at']}})
    return {'query':topic,'source':url,'fetched_at':result['fetched_at'],'response_sha256':result['sha256'],
            'records':records,'count':len(records),'note':'Metadata is not full-text evidence; citation counts are discovery leads.'}


class MetadataHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta={}
    def handle_starttag(self,tag,attrs):
        if tag.lower() != 'meta':return
        d=dict(attrs)
        key=d.get('name') or d.get('property')
        if key and 'content' in d: self.meta.setdefault(key.lower(),[]).append(d['content'])


def acl_metadata(url, fetcher=fetch_public):
    if not re.fullmatch(r'https://aclanthology\.org/(?:[A-Za-z0-9_.-]+)/?',url):
        raise ResearchError('ACL canonical article URL required')
    result=fetcher(url)
    if 'html' not in result['content_type']:
        raise ResearchError('expected HTML document')
    parser=MetadataHTML()
    parser.feed(result['content'].decode('utf-8',errors='replace'))
    meta=parser.meta
    first=lambda name:(meta.get(name) or [''])[0]
    title=first('citation_title') or first('dc.title')
    doi=first('citation_doi')
    if not title or not doi:
        raise ResearchError('ACL page lacks title/DOI; do not invent metadata')
    date_string=first('citation_date') or first('citation_publication_date')
    year_match=re.search(r'\b(?:19|20)\d{2}\b',date_string)
    return {'paper_id':'doi:'+doi.lower(),'title':title,'doi':doi.lower(),
            'authors':meta.get('citation_author',[]),'url':url,
            'year':int(year_match.group(0)) if year_match else None,
            'bibliography_type':'inproceedings' if doi.lower().startswith('10.18653/v1/') else 'misc',
            'booktitle':first('citation_conference_title') or first('citation_book_title') or None,
            'pdf_url':first('citation_pdf_url') or url.rstrip('/')+'.pdf',
            'access':'metadata', 'metadata_provenance':{'sha256':result['sha256'],'fetched_at':result['fetched_at']}}


def pdf_to_text(pdf_bytes):
    if not pdf_bytes.startswith(b'%PDF'):
        raise ResearchError('not a PDF file')
    try:
        run=subprocess.run(['pdftotext','-raw','-','-'], input=pdf_bytes,capture_output=True,timeout=20)
    except FileNotFoundError as e:raise ResearchError('pdftotext executable required') from e
    if run.returncode:
        raise ResearchError('pdftotext failed: '+run.stderr.decode('utf-8',errors='replace')[:400])
    pages=run.stdout.decode('utf-8',errors='replace').split('\f')
    while pages and not pages[-1].strip(): pages.pop()
    if not pages:raise ResearchError('PDF had no extractable text')
    return pages


def read_paper_pages(source, root=None):
    """source is project-local PDF/TXT or approved public ACL PDF URL; no implicit search."""
    if source.startswith('https://'):
        if not re.fullmatch(r'https://aclanthology\.org/[A-Za-z0-9_.-]+\.pdf',source):
            raise ResearchError('only canonical ACL PDF URLs are supported')
        result=fetch_public(source,max_bytes=MAX_PDF_BYTES)
        pages=pdf_to_text(result['content'])
        return {'source':source,'sha256':result['sha256'],
                'extracted_text_sha256':digest('\f'.join(pages).encode('utf-8')),
                'extraction_method':'pdftotext -raw','pages':pages,
                'read_depth':'fulltext_extracted','fetched_at':result['fetched_at']}
    if root is None:raise ResearchError('root required for local files')
    p=within(root,source)
    if not p.is_file():raise ResearchError('missing local source')
    raw=p.read_bytes()
    if len(raw)>MAX_PDF_BYTES:raise ResearchError('local paper too large')
    if p.suffix.lower()=='.pdf':pages=pdf_to_text(raw)
    elif p.suffix.lower()=='.txt':pages=raw.decode('utf-8').split('\f')
    else:raise ResearchError('supported local paper formats are PDF/TXT')
    return {'source':str(p.relative_to(root)),'sha256':digest(raw),
            'extracted_text_sha256':digest('\f'.join(pages).encode('utf-8')),
            'extraction_method':'pdftotext -raw' if p.suffix.lower()=='.pdf' else 'supplied_text_excerpt',
            'pages':pages,'read_depth':'fulltext_extracted' if p.suffix.lower()=='.pdf' else 'supplied_text_excerpt', 'fetched_at':now()}


def norm(s):
    return ' '.join(re.findall(r'\w+',s.lower(),flags=re.UNICODE))


def gap_leads(pages, paper_id, *, max_leads=20):
    """Extract candidate limitation paragraphs, not redundant overlapping line windows.

    A source PDF page number can be carried by a [SOURCE_PDF_PAGE=N] marker in
    deliberately excerpted text; raw PDFs use their actual page index.
    """
    if not isinstance(paper_id,str) or not paper_id.strip():raise ResearchError('paper ID required')
    out=[];seen=set();active=None;paragraph=[];page_number=1;start_line=1
    def flush():
        nonlocal paragraph
        if not paragraph:return
        excerpt=' '.join(paragraph).strip()
        paragraph=[]
        if len(excerpt)<18 or excerpt.lower().startswith(('while our study presents', 'several limitations are noteworthy')) or not any(t in excerpt.lower() for t in TRIGGERS):return
        key=norm(excerpt)
        if key in seen:return
        seen.add(key)
        out.append({'lead_id':f'lead-{len(out)+1:03d}','paper_id':paper_id,
                    'locator':f'p.{page_number}, line {start_line}', 'section':active,
                    'excerpt':excerpt[:550],
                    'source_kind':'author_stated_limitation' if active in ('limitations','limitation','局限性') else 'project_inference',
                    'status':'candidate','verified_open_gap':False,'requires_later_work':True})
    for actual_page,page in enumerate(pages,1):
        page_number=actual_page
        for i,line in enumerate(page.splitlines(),1):
            v=line.strip()
            match=re.fullmatch(r'\[SOURCE_PDF_PAGE=(\d+)\]',v)
            if match:
                flush()
                page_number=int(match.group(1))
                continue
            key=re.sub(r'^\s*(?:\d+(?:\.\d+)*[. ]+)?','',v.lower()).strip().rstrip(':')
            if key in HEADERS:
                flush()
                active=key
                continue
            if not v:
                flush()
                continue
            if key in ('references','ethical statement','acknowledgments','appendix','bibliography') or (re.match(r'^\d+\s+[A-Z]',v) and active):
                flush()
                active=None
                continue
            if active is None:continue
            if active in ('discussion','conclusion','conclusions','讨论') and not any(t in v.lower() for t in TRIGGERS):
                flush()
                continue
            # Topic-style subheadings within a limitation section.
            if paragraph and re.match(r'^(?:Simplification of the mechanism behind|Computational overhead\b|Positional attention bias may be beneficial\b|The root cause of attention bias is unclear\b)',v,re.I):
                flush()
            if not paragraph:start_line=i
            paragraph.append(v)
            if len(out)>=max_leads:break
        flush()
        if len(out)>=max_leads:break
    return out[:max_leads]


def citation_entry(paper, claim, excerpt, locator, document_text, *, cannot_support, source_access='local_excerpt', source_read_depth=None):
    if source_access not in ('fulltext','local_excerpt','abstract'):
        raise ResearchError('citation source_access must reflect what was actually read')
    if source_access == 'fulltext' and source_read_depth != 'fulltext_extracted':
        raise ResearchError('fulltext citation requires verified PDF/full-text extraction, not an excerpt')
    for key in ('paper_id','title','doi','url'):
        if not paper.get(key):raise ResearchError('paper lacks bibliographic '+key)
    if not claim or not excerpt or not locator or not cannot_support:
        raise ResearchError('claim/excerpt/locator/unsupported scope required')
    if norm(excerpt) not in norm(document_text):
        raise ResearchError('citation text not found in supplied source: cannot claim full-text support')
    return {'paper_id':paper['paper_id'],'title':paper['title'],'doi':paper['doi'],
            'authors':paper.get('authors',[]),'year':paper.get('year'), 'url':paper['url'],
            'source_access':source_access,'source_locator':locator,
            'source_text_sha256':digest(document_text.encode('utf-8')),
            'excerpt_sha256':digest(norm(excerpt).encode('utf-8')),
            'claim_can_support':claim,'cannot_support':cannot_support,
            'verification':'source_passage_matched_not_scientifically_adjudicated'}


def bibtex(entries):
    if len({p['doi'] for p in entries})!=len(entries):raise ResearchError('duplicate DOIs')
    lines=[]
    def escape(v):return str(v).replace('\\','\\textbackslash{}').replace('{','\\{').replace('}','\\}').replace('%','\\%').replace('&','\\&').replace('$','\\$')
    for index,p in enumerate(entries,1):
        if not p.get('title') or not p.get('doi'):raise ResearchError('cannot fabricate BibTeX fields')
        tag='atlas'+str(index)+'_'+re.sub(r'\W+','',p['doi'].lower())[:16]
        attrs={'title':p['title'],'doi':p['doi']}
        if p.get('booktitle') and (p.get('bibliography_type') or ('inproceedings' if str(p.get('doi','')).lower().startswith('10.18653/v1/') else 'misc'))=='inproceedings':
            attrs['booktitle']=p['booktitle']
        if p.get('year'):attrs['year']=str(p['year'])
        if p.get('authors'):attrs['author']=' and '.join(p['authors'])
        if p.get('url'):attrs['url']=p['url']
        kind=p.get('bibliography_type') or ('inproceedings' if str(p.get('doi','')).lower().startswith('10.18653/v1/') else 'misc')
        if kind not in {'article','inproceedings','book','incollection','misc'}:
            raise ResearchError('unknown bibliographic entry type; preserve as misc if uncertain')
        lines.append('@'+kind+'{'+tag+',\n'+''.join('  '+key+' = {'+escape(val)+'},\n' for key,val in attrs.items())+'}\n')
    return '\n'.join(lines)


def decide(proposal, reviews):
    """Finite, inspectable decision policy. Human scientific judgment remains external."""
    if not isinstance(reviews,list):raise ResearchError('reviews should be a list')
    pid=proposal.get('proposal_id')
    if not pid:raise ResearchError('proposal ID required')
    review_roles={r.get('role') for r in reviews}
    if any(not r.get('finding') or not r.get('evidence_locator') or r.get('proposal_id')!=pid for r in reviews):
        raise ResearchError('review findings need matching proposal ID, evidence and locator')
    if proposal.get('gap_status') in ('solved','invalid_gap'):
        return 'PIVOT', 'The current gap has been marked resolved or invalid; preserve and select a new problem.'
    if not proposal.get('primary_source_locator'):
        return 'SEARCH_MORE', 'Primary paper text and a concrete locator have not been read.'
    if proposal.get('later_work_checked') is not True:
        return 'SEARCH_MORE', 'Later/nearest work has not been checked.'
    if not proposal.get('distinct_remaining_gap'):
        return 'NARROW', 'No distinct remaining gap after checking later work.'
    if 'critic' not in review_roles or 'supervisor' not in review_roles:
        return 'SEARCH_MORE', 'Critic and supervisor reports missing; do not self-certify.'
    unresolved=[r for r in reviews if r.get('severity')=='blocking' and r.get('resolved') is not True]
    if any(r.get('failure_type') == 'invalid_mechanism' for r in unresolved):
        return 'PIVOT', 'Blocking evidence-backed critique invalidates the current mechanism/claim.'
    if any(r.get('failure_type') in ('measurement','data_leakage') for r in unresolved):
        return 'REPAIR_MEASUREMENT', 'Critic found a blocking data/measurement problem.'
    if unresolved:
        return 'NARROW', 'A blocking scoped critique remains unresolved.'
    if proposal.get('data') == 'unavailable':
        return 'PARK', 'Required data are unavailable; preserve a concrete restart condition.'
    feasibility=proposal.get('feasibility',{})
    for key in ('data','compute','evaluation','budget'):
        if feasibility.get(key)!='available':
            return 'REPAIR_MEASUREMENT', 'Resource or evaluation capability not verified: '+key
    if not proposal.get('minimal_test') or not proposal.get('rival_prediction'):
        return 'NARROW', 'A cheaper discriminating test or rival prediction is missing.'
    return 'PROCEED', 'Eligible for a bounded pilot, not a proof of novelty or publishability.'


def run_cycle(root, proposal_file, reviews_file, *, max_cycles=1):
    root=safe_root(root)
    if max_cycles<1 or max_cycles>20:raise ResearchError('bounded 1..20 cycles required')
    proposal=read_json(within(root,proposal_file))
    reviews=read_json(within(root,reviews_file))
    decision,reason=decide(proposal,reviews)
    if decision=='PROCEED':validate_data_contract(root,proposal)
    state_dir=within(root,'research-atlas/supervision')
    state_dir.mkdir(parents=True,exist_ok=True)
    # Distinct snapshots retain prior decisions and protect against accidental overwrite.
    entries=sorted(state_dir.glob('decision-*.json'))
    sequence=len(entries)+1
    result={'sequence':sequence,'proposal_id':proposal['proposal_id'],'decision':decision,
            'reason':reason,'source_sha256':digest(within(root,proposal_file).read_bytes()),
            'review_sha256':digest(within(root,reviews_file).read_bytes()),
            'review_roles':[x['role'] for x in reviews], 'scientific_verdict':'not_assessed',
            'created_at':now(),'max_cycles':max_cycles,'next_step':{
                'PROCEED':'Design/execute a bounded pilot under the frozen proposal.',
                'SEARCH_MORE':'Return to primary/later literature with explicit queries.',
                'REPAIR_MEASUREMENT':'Check data, evaluation or blocked validity before proceeding.',
                'NARROW':'Respecify residual problem and strongest simple alternative.',
                'PIVOT':'Select another candidate while retaining the rejected direction.',
                'PARK':'Record data access restart condition and evaluate an alternative.',
                'STOP':'Conclude this branch with its evidence.'}[decision]}
    saved=save_json(state_dir / f'decision-{sequence:04d}.json',result)
    return {'result':result,'path':str(saved.relative_to(root))}



def validate_data_contract(root, proposal):
    """Check declared local data lineage; substantive validity remains under review."""
    contract=proposal.get('data_contract')
    if not isinstance(contract,dict):
        raise ResearchError('pilot requires data_contract with source files and intended measurement')
    if not contract.get('measured_construct') or not contract.get('metric') or not contract.get('ground_truth_provenance'):
        raise ResearchError('construct, metric, and ground-truth provenance required')
    required=proposal.get('required_measurements')
    available=contract.get('measurement_capabilities')
    if not isinstance(required,list) or not required or not isinstance(available,list):
        raise ResearchError('pilot requires required_measurements and dataset measurement_capabilities')
    if not all(isinstance(x,str) and x.strip() for x in required+available):
        raise ResearchError('measurement capability labels must be nonempty')
    missing=sorted(set(required)-set(available))
    if missing:
        raise ResearchError('dataset cannot measure the required scientific claim: '+', '.join(missing))
    files=contract.get('files')
    if not isinstance(files,list) or not files:
        raise ResearchError('pilot requires checked project-local data artifacts')
    roles=set()
    for entry in files:
        if not isinstance(entry,dict) or entry.get('role') not in {'corpus','queries','qrels','labels','evaluation','dataset'}:
            raise ResearchError('data artifact roles must be explicit')
        roles.add(entry['role'])
        file=within(root,entry.get('path',''))
        if not file.is_file() or not entry.get('sha256') or digest(file.read_bytes())!=entry['sha256']:
            raise ResearchError('data file missing or changed: '+entry.get('path',''))
    if not (('qrels' in roles and 'queries' in roles and 'corpus' in roles) or ('labels' in roles and 'dataset' in roles)):
        raise ResearchError('data contract requires source data and evaluation labels')
    parsed = None
    if {'qrels', 'queries', 'corpus'} <= roles:
        # Claims of BEIR-format retrieval support require genuine IDs and positive
        # relevance judgments, not only a checksum of arbitrary files.
        by_role={entry['role']:within(root,entry['path']) for entry in files}
        corpus_dir=by_role['corpus'].parent
        if (by_role['corpus'].name!='corpus.jsonl'
                or by_role['queries']!=corpus_dir/'queries.jsonl'
                or by_role['qrels']!=corpus_dir/'qrels'/'test.tsv'):
            raise ResearchError('BEIR data layout does not match declared roles')
        try:
            from retrieval_benchmark import load_beir, BenchmarkError
            loaded=load_beir(corpus_dir,split='test')
        except (BenchmarkError, ValueError, KeyError) as e:
            raise ResearchError('BEIR identifiers/labels invalid: '+str(e)) from e
        provenance=loaded[3]
        parsed={'labeled_queries':provenance['labeled_positive_queries'],
                'corpus_docs':provenance['corpus_docs'],
                'labels_have_matching_documents':True}
    return {'status':'file_lineage_checked','roles':sorted(roles), 'measurement_capabilities':available,
            'retrieval_ground_truth_check':parsed,'measurement_validity':'requires_scientific_review'}


def run_queue(root, file):
    """Finite queue of previously prepared proposals, not fake autonomous researcher execution."""
    root=safe_root(root)
    spec=read_json(within(root,file))
    tasks=spec.get('tasks')
    if not isinstance(tasks,list) or not tasks or len(tasks)>20:
        raise ResearchError('bounded nonempty queue of <=20 tasks required')
    decisions=[]
    for task in tasks:
        if not isinstance(task,dict) or not task.get('proposal') or not task.get('reviews'):
            raise ResearchError('each task requires a proposal/reviews pair')
        proposal=read_json(within(root,task['proposal']))
        reviews=read_json(within(root,task['reviews']))
        decision,_=decide(proposal,reviews)
        if decision=='PROCEED':validate_data_contract(root,proposal)
        decision_record=run_cycle(root,task['proposal'],task['reviews'])
        decisions.append(decision_record)
        if decision in ('PROCEED','STOP','SEARCH_MORE','REPAIR_MEASUREMENT'):
            break  # A scientist action is needed before another supervisor verdict.
    return {'processed':len(decisions),'total_tasks':len(tasks),'actions':decisions,
            'outcome':decisions[-1]['result']['decision'],'unexamined_tasks':len(tasks)-len(decisions),
            'scientific_verdict':'not_assessed'}

def main(argv=None):
    ap=argparse.ArgumentParser(description='Bounded research evidence and supervision runner')
    ap.add_argument('--root',required=True)
    sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('help')
    p=sub.add_parser('query');p.add_argument('--topic',required=True);p.add_argument('--limit',type=int,default=10);p.add_argument('--output',required=True)
    p=sub.add_parser('read');p.add_argument('--paper',required=True);p.add_argument('--id',required=True);p.add_argument('--output',required=True)
    p=sub.add_parser('cycle');p.add_argument('--proposal',required=True);p.add_argument('--reviews',required=True);p.add_argument('--max-cycles',type=int,default=1)
    p=sub.add_parser('queue');p.add_argument('--file',required=True)
    p=sub.add_parser('acl');p.add_argument('--url',required=True);p.add_argument('--output',required=True)
    p=sub.add_parser('citation');p.add_argument('--paper',required=True);p.add_argument('--source',required=True);p.add_argument('--claim',required=True);p.add_argument('--excerpt',required=True);p.add_argument('--locator',required=True);p.add_argument('--cannot-support',required=True);p.add_argument('--access',choices=('fulltext','local_excerpt','abstract'),default='local_excerpt');p.add_argument('--output',required=True);p.add_argument('--bib-output',required=True)
    p=sub.add_parser('export');p.add_argument('--paper',required=True);p.add_argument('--leads',required=True);p.add_argument('--excerpt',required=True);p.add_argument('--as-of',required=True);p.add_argument('--output',required=True)
    p=sub.add_parser('polarity');p.add_argument('--claims',required=True);p.add_argument('--assertions',required=True);p.add_argument('--output',required=True)
    args=ap.parse_args(argv)
    try:
        root=safe_root(args.root)
        if args.cmd=='help':out={'commands':['query','acl','read','citation','export','polarity','cycle','queue'],'scientific_verdict':'not_assessed'}
        elif args.cmd=='query':
            out=crossref_query(args.topic,args.limit)
            save_json(within(root,args.output),out)
        elif args.cmd=='read':
            paper=read_paper_pages(args.paper,root)
            out={'paper_id':args.id,'source':paper['source'],'sha256':paper['sha256'],
                 'read_depth':paper['read_depth'],'page_count':len(paper['pages']),
                 'leads':gap_leads(paper['pages'],args.id)}
            save_json(within(root,args.output),out)
        elif args.cmd=='cycle':out=run_cycle(root,args.proposal,args.reviews,max_cycles=args.max_cycles)
        elif args.cmd=='queue':out=run_queue(root,args.file)
        elif args.cmd=='acl':
            out=acl_metadata(args.url)
            save_json(within(root,args.output),out)
        elif args.cmd=='citation':
            source=read_paper_pages(args.source,root)
            paper=read_json(within(root,args.paper))
            content='\n'.join(source['pages'])
            out=citation_entry(paper,args.claim,args.excerpt,args.locator,content,
                               cannot_support=args.cannot_support,source_access=args.access,
                               source_read_depth=source['read_depth'])
            outfile=within(root,args.output)
            bibfile=within(root,args.bib_output)
            if outfile==bibfile or outfile.exists() or bibfile.exists():
                raise ResearchError('citation outputs must be two distinct new files')
            source_bib=bibtex([paper])
            save_json(outfile,out)
            bibfile.parent.mkdir(parents=True,exist_ok=True)
            bibfile.write_text(source_bib,encoding='utf-8')
        elif args.cmd=='export':
            out=export_atlas_batch(read_json(within(root,args.paper)),
                read_json(within(root,args.leads))['leads'],args.excerpt,args.as_of)
            save_json(within(root,args.output),out)
        elif args.cmd=='polarity':
            claims=[json.loads(line) for line in within(root,args.claims).read_text().splitlines() if line.strip()]
            out=scifact_polarity_audit(claims,read_json(within(root,args.assertions)))
            save_json(within(root,args.output),out)
        print(json.dumps(out,ensure_ascii=False,indent=2))
    except (ResearchError,OSError,ValueError,subprocess.TimeoutExpired) as e:
        print(json.dumps({'error':str(e)},ensure_ascii=False),file=sys.stderr)
        return 2
    return 0



# Extensions below are defined as callable library functions. CLI registration is
# kept inside main(), so imports never cause network or file mutations.

def scifact_polarity_audit(claim_records, asserted):
    """Use actual SciFact annotation polarity instead of DOI/citation existence.

    Each asserted row: {'claim_id': int/str, 'doc_id': int/str,
                        'asserted_relation': 'SUPPORT'|'CONTRADICT'}.
    An ambiguous multi-label gold entry is unresolved, not forced to one label.
    """
    claims={}
    for item in claim_records:
        cid=str(item.get('id',''))
        if not cid or cid in claims:raise ResearchError('invalid/duplicate SciFact claim id')
        if not isinstance(item.get('evidence'),dict):raise ResearchError('claim evidence must be a document map')
        claims[cid]=item
    output=[]
    for row in asserted:
        claim_id=str(row.get('claim_id',''))
        doc_id=str(row.get('doc_id',''))
        relation=row.get('asserted_relation')
        if relation not in ('SUPPORT','CONTRADICT'):
            raise ResearchError('asserted_relation must be SUPPORT or CONTRADICT')
        if claim_id not in claims:
            output.append({'claim_id':claim_id,'doc_id':doc_id,'asserted_relation':relation,'status':'unknown_claim'})
            continue
        gold_rows=claims[claim_id]['evidence'].get(doc_id,[])
        labels={x.get('label') for x in gold_rows}
        if not labels:
            status='no_annotated_evidence'
        elif not labels <= {'SUPPORT','CONTRADICT'} or len(labels)!=1:
            status='mixed_or_invalid_gold'
        elif relation in labels:
            status='matches_annotated_relation'
        else:
            status='contradicts_annotated_relation'
        output.append({'claim_id':claim_id,'doc_id':doc_id,'asserted_relation':relation,
                       'gold_relations':sorted(str(v) for v in labels),'status':status,
                       'annotation_source':'SciFact expert-labeled evidence (if using official files)'})
    return {'checks':output,'checked':len(output),
            'mismatches':sum(x['status']=='contradicts_annotated_relation' for x in output),
            'scientific_verdict':'annotation_consistency_only'}


def export_atlas_batch(paper,leads,local_excerpt_path,as_of):
    """Create Atlas-compatible import nodes; no claim of a confirmed open gap."""
    from datetime import date
    try:date.fromisoformat(as_of)
    except (TypeError,ValueError) as e:raise ResearchError('as_of must be YYYY-MM-DD') from e
    if not paper.get('title') or not paper.get('doi') or not paper.get('url'):
        raise ResearchError('verified paper title/DOI/URL required for Atlas export')
    if not local_excerpt_path or Path(local_excerpt_path).is_absolute() or '..' in Path(local_excerpt_path).parts:
        raise ResearchError('project-relative local excerpt required')
    doi=str(paper['doi']).lower().removeprefix('https://doi.org/')
    canonical='paper_'+digest(doi.encode())[:16]
    source={'access':'local','path':local_excerpt_path,'locator':'read excerpt; individual PDF-page locators in gap nodes',
            'accessed_at':as_of}
    nodes=[{'id':canonical,'type':'paper','title':paper['title'],'domains':[],'sources':[source],
            'data':{'doi':doi,'url':paper['url'],'read_depth':'supplied_text_excerpt'}}]
    edges=[]
    for row in leads:
        if row.get('status') != 'candidate' or row.get('verified_open_gap') is not False:
            raise ResearchError('only candidate leads may be exported without later-work verification')
        lid='gap_'+digest((doi+'|'+row['locator']+'|'+row['excerpt']).encode('utf-8'))[:16]
        nodes.append({'id':lid,'type':'gap','title':row['excerpt'][:95],'domains':[],
                      'status':'candidate','sources':[{'access':'local','path':local_excerpt_path,
                      'locator':row['locator'],'accessed_at':as_of}],
                      'data':{'source_kind':row['source_kind'],'evidence_ids':[canonical],
                      'source_locator':row['locator'],'unresolved_part':'pending later-work verification',
                      'review_reason':'candidate lead, not assessed as open',
                      'later_work_checked':False}})
        edges.append({'id':'edge_'+digest((canonical+lid).encode())[:16], 'source':canonical,'target':lid,'relation':'motivates'})
    return {'nodes':nodes,'edges':edges}

if __name__=='__main__':raise SystemExit(main())
