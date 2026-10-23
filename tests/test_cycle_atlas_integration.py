"""Integration into the v1.2 persistent research Atlas, with grounded real paper excerpts.

This test executes the ACTUAL prior Atlas CLI against newly exported paper/gap
nodes; it does not assert that an unverified candidate gap is scientifically open.
"""
from __future__ import annotations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
SCRIPTS=REPO/'skills/agent-research-atlas/scripts'
sys.path.insert(0,str(SCRIPTS))
from research_cycle import export_atlas_batch, gap_leads, digest


class AtlasInteropTests(unittest.TestCase):
    def invoke(self, root, *args):
        proc=subprocess.run([sys.executable,str(SCRIPTS/'atlas.py'),'--root',str(root),*args],
                            capture_output=True,text=True,timeout=25)
        self.assertEqual(proc.returncode,0,proc.stderr + '\n' + proc.stdout)
        return json.loads(proc.stdout)

    @unittest.skipUnless((SCRIPTS / "atlas.py").is_file(), "Requires complete Atlas repository checkout")
    def test_exported_real_excerpt_gaps_enter_atlas_as_unverified_candidates(self):
        source=REPO/'evals/real_research_cycle/papers/hsieh_2024_excerpts.txt'
        metadata=REPO/'evals/real_research_cycle/papers/hsieh_metadata.json'
        paper=json.loads(metadata.read_text(encoding='utf-8'))
        leads=gap_leads(source.read_text(encoding='utf-8').split('\f'),paper['paper_id'])
        self.assertEqual(len(leads),4)
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/'papers').mkdir()
            shutil.copyfile(source,root/'papers/hsieh.txt')
            self.invoke(root,'init','--title','Real-document limitation smoke','--synthetic')
            batch=export_atlas_batch(paper,leads,'papers/hsieh.txt','2026-10-22')
            batchfile=root/'import-batch.json'
            batchfile.write_text(json.dumps(batch,ensure_ascii=False),encoding='utf-8')
            self.invoke(root,'upsert','--file',str(batchfile),'--expected-revision','0')
            checked=self.invoke(root,'check')
            self.assertTrue(checked['valid'])
            state=json.loads((root/'research-atlas/atlas.json').read_text())
            new_gaps=[n for n in state['nodes'] if n['type']=='gap']
            self.assertEqual(len(new_gaps),4)
            self.assertEqual({n['status'] for n in new_gaps},{'candidate'})
            self.assertTrue(all(n['data']['source_kind']=='author_stated_limitation' for n in new_gaps))
            self.assertTrue(all(n['data']['later_work_checked'] is False for n in new_gaps))
            self.assertTrue(any(n['type']=='paper' and n.get('data',{}).get('doi')==paper['doi'] for n in state['nodes']))
            self.assertEqual((root/'papers/hsieh.txt').read_bytes(),source.read_bytes())
            self.assertEqual(digest(source.read_bytes()),digest((root/'papers/hsieh.txt').read_bytes()))
            # The host is free to request more literature; ingestion must not certify novelty.
            self.assertEqual(self.invoke(root,'status')['revision'],1)


if __name__=='__main__':unittest.main()
