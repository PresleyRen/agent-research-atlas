import hashlib
from io import BytesIO
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'skills/agent-research-atlas/scripts'))
import fetch_beir as f

class FakeResponse:
    def __init__(self,payload): self.stream=BytesIO(payload)
    def __enter__(self):return self
    def __exit__(self,*args):pass
    def read(self,n):return self.stream.read(n)

class BeirFetchTests(unittest.TestCase):
    def build_zip(self,extra_name=None):
        buf=BytesIO()
        with ZipFile(buf,'w') as z:
            z.writestr('scifact/corpus.jsonl','{"_id":"d","title":"x","text":"text"}\n')
            z.writestr('scifact/queries.jsonl','{"_id":"q","text":"why"}\n')
            z.writestr('scifact/qrels/test.tsv','query-id\tcorpus-id\tscore\nq\td\t1\n')
            if extra_name:z.writestr(extra_name,'BAD')
        return buf.getvalue()

    def test_pinned_source_and_checksum_and_manifest(self):
        data=self.build_zip()
        checksum=hashlib.md5(data).hexdigest()
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'scifact'
            with patch.object(f,'urlopen',return_value=FakeResponse(data)):
                path,record=f.download_scifact(dest,expected_md5=checksum)
            self.assertTrue((Path(path)/'qrels/test.tsv').is_file())
            self.assertEqual(record['archive_sha256'],hashlib.sha256(data).hexdigest())
            self.assertTrue((dest/'SOURCE.json').exists())

    def test_checksum_error_does_not_leave_partial_dataset(self):
        data=self.build_zip()
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'scifact'
            with patch.object(f,'urlopen',return_value=FakeResponse(data)):
                with self.assertRaises(ValueError):f.download_scifact(dest,expected_md5='0'*32)
            self.assertFalse(dest.exists())

    def test_zip_traversal_rejected_without_side_effects(self):
        data=self.build_zip('../outside.txt')
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'scifact'
            with patch.object(f,'urlopen',return_value=FakeResponse(data)):
                with self.assertRaisesRegex(ValueError,'unsafe zip path'):
                    f.download_scifact(dest,expected_md5=hashlib.md5(data).hexdigest())
            self.assertFalse((Path(tmp)/'outside.txt').exists())

    def test_refuses_overwrite_existing_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)/'scifact'
            dest.mkdir()
            with self.assertRaises(ValueError):f.download_scifact(dest)

if __name__=='__main__':unittest.main()
