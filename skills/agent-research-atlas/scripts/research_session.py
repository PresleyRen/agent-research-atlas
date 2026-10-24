#!/usr/bin/env python3
"""Bounded, resumable host-mediated research sessions with immutable evidence.

The host supplies genuinely separate Scientist/Critic/Supervisor work. This
module verifies provenance and orchestrates gates; it does not simulate minds.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import research_cycle as c
import retrieval_benchmark as benchmark


class Session:
    def __init__(self, root):
        self.root = c.safe_root(root)
        self.directory = c.within(self.root, 'research-atlas/session')
        self.directory.mkdir(parents=True, exist_ok=True)

    def events(self):
        result = []
        previous = None
        for index, path in enumerate(sorted(self.directory.glob('event-*.json')), 1):
            value = c.read_json(path)
            recorded_digest = value.get('event_sha256')
            unsigned = {key: item for key, item in value.items() if key != 'event_sha256'}
            if not recorded_digest or recorded_digest != c.digest(json.dumps(unsigned, sort_keys=True, ensure_ascii=False).encode()):
                raise c.ResearchError('event chain integrity changed or legacy unsealed event; inspect before resuming')
            if value.get('sequence') != index or value.get('previous_sha256') != previous:
                raise c.ResearchError('event chain changed or incomplete')
            payload=value['payload']
            if value['kind'] in ('proposal','discovery','discovery_failure','followup_search'): self.verify(payload['evidence'])
            elif value['kind']=='review': self.verify([payload['file']])
            elif value['kind']=='experiment': self.verify([payload['result']])
            result.append(value)
            previous = c.digest(path.read_bytes())
        return result

    def append(self, kind, payload):
        events = self.events()
        if len(events) >= 100:
            raise c.ResearchError('session event budget exhausted; review before continuing')
        previous = c.digest((self.directory / f'event-{len(events):04d}.json').read_bytes()) if events else None
        value = {'sequence': len(events)+1, 'kind': kind, 'payload': payload,
                 'previous_sha256': previous, 'created_at': c.now()}
        value['event_sha256'] = c.digest(json.dumps(value, sort_keys=True, ensure_ascii=False).encode())
        c.save_json(self.directory / f'event-{len(events)+1:04d}.json', value)
        return value

    def snapshot(self, paths):
        if not paths or len(paths) != len(set(paths)):
            raise c.ResearchError('nonempty distinct evidence paths required')
        records = []
        for path in paths:
            file = c.within(self.root, path)
            if not file.is_file():
                raise c.ResearchError('missing evidence: '+path)
            records.append({'path': path, 'sha256': c.digest(file.read_bytes())})
        return records

    def verify(self, snapshot):
        if self.snapshot([item['path'] for item in snapshot]) != snapshot:
            raise c.ResearchError('evidence changed since review packet')

    def discover(self, topic, paper_urls):
        """Run bounded public discovery/full-text reading and emit reusable citations.

        Paper selection remains explicit host judgment, not a keyword novelty score.
        """
        if not paper_urls or len(paper_urls)>5 or len(set(paper_urls))!=len(paper_urls):
            raise c.ResearchError('one to five distinct canonical paper URLs required')
        number=len([e for e in self.events() if e['kind']=='discovery'])+1
        relative=f'research-atlas/session/discovery-{number:04d}'
        folder=c.within(self.root,relative)
        if folder.exists():
            raise c.ResearchError('partial discovery exists; preserve failure and inspect before retry')
        folder.mkdir()
        outputs=[]
        try:
            search=c.crossref_query(topic,limit=12)
            c.save_json(folder/'search.json',search);outputs.append(relative+'/search.json')
            bibliography=[]
            for index,url in enumerate(paper_urls,1):
                paper=c.acl_metadata(url)
                source=c.read_paper_pages(paper['pdf_url'])
                pages=source.pop('pages')
                text='\f'.join(pages)
                path=f'{relative}/paper-{index}.txt'
                c.within(self.root,path).write_text(text,encoding='utf-8')
                leads=c.gap_leads(pages,paper['paper_id'])
                citations=[c.citation_entry(paper,
                    'Author-stated limitation candidate' if lead['source_kind']=='author_stated_limitation' else 'Project-inferred candidate from source passage; not an author-stated limitation',
                    lead['excerpt'],lead['locator'],text,
                    cannot_support='Verified unresolved gap, causality, novelty, or effectiveness of a new method',
                    source_access='fulltext',source_read_depth='fulltext_extracted') for lead in leads]
                record={'paper':paper,'source':source,'leads':leads,'citations':citations,
                    'atlas_batch':c.export_atlas_batch(paper,leads,path,c.now()[:10])}
                c.save_json(folder/f'paper-{index}.json',record)
                outputs.extend([path,f'{relative}/paper-{index}.json']);bibliography.append(paper)
            (folder/'references.bib').write_text(c.bibtex(bibliography),encoding='utf-8')
            outputs.append(relative+'/references.bib')
            return self.append('discovery',{'topic':topic,'evidence':self.snapshot(outputs),
                'selection':'explicit host-selected papers; search results retained; not exhaustive',
                'scientific_verdict':'not_assessed'})
        except Exception as exc:
            c.save_json(folder/'failure.json',{'error':str(exc),'completed_files':outputs})
            self.append('discovery_failure',{'topic':topic,'evidence':self.snapshot(outputs+[relative+'/failure.json'])})
            raise

    def search_more(self, topic):
        events=self.events()
        if not events or events[-1]['kind']!='decision' or events[-1]['payload']['decision']!='SEARCH_MORE':
            raise c.ResearchError('follow-up search requires a recorded SEARCH_MORE decision')
        path=f'research-atlas/session/search-{len(events)+1:04d}.json'
        destination=c.within(self.root,path)
        if destination.exists():
            result=c.read_json(destination)
            if result.get('query')!=topic or not isinstance(result.get('records'),list) or not result.get('response_sha256'):
                raise c.ResearchError('orphan search does not match requested topic/provenance')
        else:
            result=c.crossref_query(topic,limit=12)
            c.save_json(destination,result)
        return self.append('followup_search',{'topic':topic,'evidence':self.snapshot([path]),
            'after_proposal_id':self.packet()['proposal']['proposal_id'],
            'read_depth':'metadata','next_action':'Host reviews results and prepares a new proposal; no novelty inference.'})

    def packet(self):
        packets = [e for e in self.events() if e['kind'] == 'proposal']
        if not packets:
            raise c.ResearchError('prepare a proposal first')
        packet = packets[-1]['payload']
        unsigned = {key: value for key, value in packet.items() if key != 'packet_sha256'}
        if packet.get('packet_sha256') != c.digest(json.dumps(unsigned, sort_keys=True, ensure_ascii=False).encode()):
            raise c.ResearchError('proposal packet digest changed')
        if packet['proposal'] != c.read_json(c.within(self.root, packet['evidence'][0]['path'])):
            raise c.ResearchError('embedded proposal differs from snapshotted source')
        return packet

    def prepare(self, proposal, evidence_paths, scientist_id):
        if not isinstance(scientist_id, str) or not scientist_id.strip():
            raise c.ResearchError('Scientist identity required')
        old = self.events()
        proposals=[e for e in old if e['kind']=='proposal']
        if proposals:
            last = [e for e in old if e['kind'] not in ('discovery','discovery_failure','followup_search')][-1]
            if last['kind'] != 'decision' or last['payload']['decision'] not in ('PIVOT', 'NARROW', 'REPAIR_MEASUREMENT', 'SEARCH_MORE', 'PARK'):
                raise c.ResearchError('new proposal requires a recorded revision decision')
        value = c.read_json(c.within(self.root, proposal))
        if not value.get('proposal_id'):
            raise c.ResearchError('proposal ID required')
        if any(e['kind']=='proposal' and e['payload']['proposal']['proposal_id']==value['proposal_id'] for e in old):
            raise c.ResearchError('revised proposals need a new ID')
        paths = list(dict.fromkeys([proposal]+evidence_paths))
        packet = {'proposal': value, 'scientist_id': scientist_id,
                  'evidence': self.snapshot(paths), 'independence':'host_declared_not_cryptographically_verified'}
        packet['packet_sha256'] = c.digest(json.dumps(packet,sort_keys=True,ensure_ascii=False).encode())
        return self.append('proposal', packet)

    def submit_review(self, review_path):
        packet = self.packet()
        self.verify(packet['evidence'])
        review = c.read_json(c.within(self.root, review_path))
        role = review.get('role')
        if role not in ('critic','supervisor') or not review.get('reviewer_id'):
            raise c.ResearchError('critic/supervisor role and reviewer identity required')
        if review['reviewer_id'] == packet['scientist_id']:
            raise c.ResearchError('scientist cannot self-review')
        if review.get('packet_sha256') != packet['packet_sha256'] or review.get('proposal_id') != packet['proposal']['proposal_id']:
            raise c.ResearchError('review is stale or refers to another proposal')
        if not review.get('finding') or not review.get('evidence_locator'):
            raise c.ResearchError('review finding and source locator required')
        evidence_paths = {item['path'] for item in packet['evidence']}
        if (not isinstance(review.get('evidence_paths'), list) or not review['evidence_paths']
                    or not all(isinstance(path, str) and path for path in review['evidence_paths'])
                    or not set(review['evidence_paths']) <= evidence_paths):
            raise c.ResearchError('review must cite packet evidence files')
        existing = self.reviews(packet)
        if any(r['role']==role or r['reviewer_id']==review['reviewer_id'] for r in existing):
            raise c.ResearchError('distinct roles and reviewer identities required')
        if any(e['kind']=='decision' and e['payload'].get('packet_sha256')==packet['packet_sha256'] for e in self.events()):
            raise c.ResearchError('decision already recorded; create a revised proposal')
        return self.append('review', {'review':review,'file':self.snapshot([review_path])[0]})

    def reviews(self, packet):
        reviews=[]
        for event in self.events():
            if event['kind']=='review' and event['payload']['review']['packet_sha256']==packet['packet_sha256']:
                self.verify([event['payload']['file']])
                review = c.read_json(c.within(self.root, event['payload']['file']['path']))
                if review != event['payload']['review']:
                    raise c.ResearchError('embedded review differs from snapshotted source')
                if review.get('role') not in ('critic','supervisor') or not review.get('reviewer_id') or review['reviewer_id']==packet['scientist_id']:
                    raise c.ResearchError('review identity or role is invalid')
                if review.get('proposal_id') != packet['proposal']['proposal_id'] or review.get('packet_sha256') != packet['packet_sha256']:
                    raise c.ResearchError('review packet does not match')
                evidence_paths = {item['path'] for item in packet['evidence']}
                if not review.get('finding') or not review.get('evidence_locator'):
                    raise c.ResearchError('review finding and source locator required')
                if (not isinstance(review.get('evidence_paths'), list) or not review['evidence_paths']
                    or not all(isinstance(path, str) and path for path in review['evidence_paths'])
                    or not set(review['evidence_paths']) <= evidence_paths):
                    raise c.ResearchError('review must cite packet evidence files')
                if any(r['role']==review['role'] or r['reviewer_id']==review['reviewer_id'] for r in reviews):
                    raise c.ResearchError('distinct roles and reviewer identities required')
                reviews.append(review)
        return reviews

    def gate(self, packet, reviews):
        """Recompute eligibility from reviewed inputs, never a saved decision label."""
        decision,reason=c.decide(packet['proposal'],reviews)
        if decision=='PROCEED':
            try:
                c.validate_data_contract(self.root,packet['proposal'])
                if packet['proposal'].get('experiment',{}).get('runner')=='bm25_title_weight' and packet['proposal'].get('required_measurements')!=['retrieval_relevance']:
                    raise c.ResearchError('BM25 runner measures retrieval_relevance only, not attention or generation')
            except c.ResearchError as exc:
                decision,reason='REPAIR_MEASUREMENT',str(exc)
        return decision,reason

    def decide(self):
        packet=self.packet()
        self.verify(packet['evidence'])
        if any(e['kind']=='decision' and e['payload'].get('packet_sha256')==packet['packet_sha256'] for e in self.events()):
            raise c.ResearchError('decision already recorded')
        reviews=self.reviews(packet)
        decision,reason=self.gate(packet,reviews)
        return self.append('decision',{'packet_sha256':packet['packet_sha256'],
            'proposal_id':packet['proposal']['proposal_id'],'decision':decision,'reason':reason,
            'scientific_verdict':'not_assessed'})

    def experiment(self, data_dir):
        packet=self.packet()
        self.verify(packet['evidence'])
        reviews=self.reviews(packet)
        decision,reason=self.gate(packet,reviews)
        if decision!='PROCEED':
            raise c.ResearchError('experiment requires independently recomputed PROCEED gate: '+reason)
        events=self.events()
        previous_runs = [event for event in events if event['kind']=='experiment' and event['payload'].get('packet_sha256')==packet['packet_sha256']]
        if previous_runs and (len(previous_runs)!=1 or events[-1] is not previous_runs[0]):
            raise c.ResearchError('experiment already executed for this packet; a fresh PROCEED label cannot authorize a rerun')
        if events and events[-1]['kind']=='experiment':
            if events[-1]['payload'].get('packet_sha256') != packet['packet_sha256']:
                raise c.ResearchError('interrupted experiment packet does not match current proposal')
            result_path=events[-1]['payload']['result']['path']
            return self.append('decision',{'packet_sha256':packet['packet_sha256'],'proposal_id':packet['proposal']['proposal_id'],
                'decision':'SEARCH_MORE','reason':'Recovered completed experiment; fresh independent review required.',
                'scientific_verdict':'not_assessed','experiment_result':result_path})
        if not events or events[-1]['kind']!='decision' or events[-1]['payload']['decision']!='PROCEED':
            raise c.ResearchError('experiment requires fresh PROCEED gate')
        proposal=packet['proposal']
        c.validate_data_contract(self.root,proposal)
        data=c.within(self.root,data_dir)
        declared={item['role']:c.within(self.root,item['path']) for item in proposal['data_contract']['files']}
        if declared.get('corpus')!=data/'corpus.jsonl' or declared.get('queries')!=data/'queries.jsonl' or declared.get('qrels')!=data/'qrels/test.tsv':
            raise c.ResearchError('experiment data differ from reviewed data')
        if proposal.get('experiment',{})!={'runner':'bm25_title_weight','split':'test','k':10}:
            raise c.ResearchError('supported frozen experiment specification required')
        result=benchmark.evaluate(data,split='test',k=10)
        self.verify(packet['evidence'])
        c.validate_data_contract(self.root,proposal)
        output=f'research-atlas/session/result-{len(events)+1:04d}.json'
        output_path=c.within(self.root,output)
        if output_path.exists():
            # Explicit interrupted-write recovery: never overwrite a differing record.
            if c.read_json(output_path)!=result:
                raise c.ResearchError('orphan result differs; inspect interrupted run before retry')
        else:
            c.save_json(output_path,result)
        self.append('experiment',{'packet_sha256':packet['packet_sha256'],'result':self.snapshot([output])[0],
            'direction_decision':result['direction_decision'],'scientific_verdict':'not_assessed'})
        # Measured result determines the next *task*, never an automatic novelty claim.
        decision='SEARCH_MORE'
        return self.append('decision',{'packet_sha256':packet['packet_sha256'],'proposal_id':proposal['proposal_id'],
            'decision':decision,'reason':'Actual pilot recorded. Request fresh independent review and a new proposal; inspected test split is exploratory.',
            'scientific_verdict':'not_assessed','experiment_result':output})


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',required=True)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('search-more');p.add_argument('--topic',required=True)
    p=sub.add_parser('discover');p.add_argument('--topic',required=True);p.add_argument('--paper-urls',nargs='+',required=True)
    p=sub.add_parser('prepare'); p.add_argument('--proposal',required=True);p.add_argument('--evidence',nargs='+',required=True);p.add_argument('--scientist-id',required=True)
    p=sub.add_parser('review');p.add_argument('--file',required=True)
    sub.add_parser('decide');sub.add_parser('status')
    p=sub.add_parser('experiment');p.add_argument('--data-dir',required=True)
    args=parser.parse_args(argv); session=Session(args.root)
    try:
        if args.command=='search-more':result=session.search_more(args.topic)
        elif args.command=='discover':result=session.discover(args.topic,args.paper_urls)
        elif args.command=='prepare': result=session.prepare(args.proposal,args.evidence,args.scientist_id)
        elif args.command=='review': result=session.submit_review(args.file)
        elif args.command=='decide':result=session.decide()
        elif args.command=='experiment':result=session.experiment(args.data_dir)
        else: result={'events':session.events(),'next_action':'Resume from the last immutable event; reviews are host supplied.'}
        print(json.dumps(result,indent=2,ensure_ascii=False))
        return 0
    except (c.ResearchError,benchmark.BenchmarkError) as exc:
        print(str(exc),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
