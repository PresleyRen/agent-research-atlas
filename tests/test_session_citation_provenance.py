"""Preserve extraction evidence class in generated citation claims."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/agent-research-atlas/scripts'))
import research_session as module

class CitationProvenanceTests(unittest.TestCase):
    def test_project_inference_is_not_relabeled_author_limitation(self):
        with tempfile.TemporaryDirectory() as directory:
            leads=[{'source_kind':'project_inference','excerpt':'source passage','locator':'p.1'},
                   {'source_kind':'author_stated_limitation','excerpt':'source passage','locator':'p.1'}]
            with patch.object(module.c,'crossref_query',return_value={'records':[]}), \
                 patch.object(module.c,'acl_metadata',return_value={'paper_id':'paper','pdf_url':'url'}), \
                 patch.object(module.c,'read_paper_pages',return_value={'pages':['source passage']}), \
                 patch.object(module.c,'gap_leads',return_value=leads), \
                 patch.object(module.c,'citation_entry',return_value={}) as cite, \
                 patch.object(module.c,'export_atlas_batch',return_value={}), \
                 patch.object(module.c,'bibtex',return_value=''):
                module.Session(directory).discover('topic',['url'])
                self.assertIn('Project-inferred',cite.call_args_list[0].args[1])
                self.assertIn('not an author-stated',cite.call_args_list[0].args[1])
                self.assertEqual(cite.call_args_list[1].args[1],'Author-stated limitation candidate')
