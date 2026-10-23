#!/usr/bin/env python3
"""Download official public BEIR SciFact archive with checksum and safe extraction."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
from urllib.request import Request,urlopen
from zipfile import ZipFile

SCIFACT_URL='https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip'
SCIFACT_MD5='5f7d1de60b170fc8027bb7898e2efca1'


def download_scifact(dest, source=SCIFACT_URL, expected_md5=SCIFACT_MD5):
    if source!=SCIFACT_URL:raise ValueError('only pinned official SciFact source supported')
    dest=Path(dest).resolve()
    if dest.exists():raise ValueError('destination already exists; dataset snapshot immutable')
    dest.mkdir(parents=True,exist_ok=False)
    try:
        req=Request(source,headers={'User-Agent':'Agent-Research-Atlas/1.3 (open scholarly data benchmark)'})
        with urlopen(req,timeout=60) as response:
            with tempfile.NamedTemporaryFile(dir=dest,delete=False,suffix='.zip') as tmp:
                zip_path=Path(tmp.name)
                total=0
                while True:
                    block=response.read(1<<20)
                    if not block:break
                    total+=len(block)
                    if total>100_000_000:raise ValueError('dataset download too large')
                    tmp.write(block)
        data=zip_path.read_bytes()
        if hashlib.md5(data).hexdigest()!=expected_md5:
            raise ValueError('official BEIR SciFact checksum mismatch')
        with ZipFile(zip_path) as archive:
            total_plain=0
            for info in archive.infolist():
                name=info.filename
                rel=Path(name)
                if rel.is_absolute() or '..' in rel.parts or str(rel).startswith(('/','\\')):
                    raise ValueError('unsafe zip path')
                # Refuse non-regular files and symlinks.
                mode=(info.external_attr>>16)&0o170000
                if mode not in (0,0o100000,0o040000):raise ValueError('unsafe zip entry')
                total_plain+=info.file_size
                if total_plain>150_000_000:raise ValueError('zip bomb detected')
            archive.extractall(dest)
        zip_path.unlink()
        candidates=list(dest.rglob('corpus.jsonl'))
        if len(candidates)!=1:raise ValueError('dataset corpus file missing or ambiguous')
        folder=candidates[0].parent
        if not (folder/'queries.jsonl').is_file() or not (folder/'qrels'/'test.tsv').is_file():
            raise ValueError('official SciFact qrels/queries missing')
        record={'dataset':'BEIR SciFact','url':source,'md5':expected_md5,
                'archive_sha256':hashlib.sha256(data).hexdigest(),
                'corpus':str((folder/'corpus.jsonl').relative_to(dest)),
                'queries':str((folder/'queries.jsonl').relative_to(dest)),
                'qrels':str((folder/'qrels'/'test.tsv').relative_to(dest))}
        (dest/'SOURCE.json').write_text(json.dumps(record,indent=2)+'\n')
        return str(folder),record
    except Exception:
        import shutil
        shutil.rmtree(dest,ignore_errors=True)
        raise

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--dest',required=True)
    args=p.parse_args()
    folder,record=download_scifact(args.dest)
    print(json.dumps({'data_dir':folder,**record},indent=2))
