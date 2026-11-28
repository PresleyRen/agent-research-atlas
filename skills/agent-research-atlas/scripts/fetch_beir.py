#!/usr/bin/env python3
"""Download official public BEIR SciFact archive with checksum and safe extraction."""
from __future__ import annotations
import argparse
import hashlib
from http.client import IncompleteRead
from io import BytesIO
import json
from pathlib import Path
from time import monotonic
from urllib.error import URLError
from urllib.request import Request,urlopen
from zipfile import ZipFile

SCIFACT_URL='https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/scifact.zip'
SCIFACT_MD5='5f7d1de60b170fc8027bb7898e2efca1'
SCIFACT_SHA256='536e14446a0ba56ed1398ab1055f39fe852686ecad24a6306c80c490fa8e0165'
SCIFACT_MIRROR=(
    'https://raw.githubusercontent.com/bakzalitdootvala/rag-beir-scifact/'
    '325eee3017cf7e657e3113ec1583e56232783dc3/data/scifact.zip'
)
NETWORK_ERRORS=(URLError,TimeoutError,ConnectionError,IncompleteRead)


def fetch_archive(source):
    req=Request(source,headers={'User-Agent':'Agent-Research-Atlas/1.3 (open scholarly data benchmark)'})
    deadline=monotonic()+30
    data=bytearray()
    with urlopen(req,timeout=12) as response:
        while monotonic()<deadline:
            # Read what is available so a trickling connection cannot defer the deadline check.
            block=response.read1(64*1024)
            if not block:
                if response.length not in (None,0):
                    raise IncompleteRead(bytes(data),response.length)
                return data
            data.extend(block)
            if len(data)>100_000_000:
                raise ValueError('dataset download too large')
    raise TimeoutError('SciFact archive download exceeded the time limit')


def download_scifact(dest, source=SCIFACT_URL, expected_md5=SCIFACT_MD5):
    if source!=SCIFACT_URL:raise ValueError('only pinned official SciFact source supported')
    dest=Path(dest).resolve()
    if dest.exists():raise ValueError('destination already exists; dataset snapshot immutable')
    dest.mkdir(parents=True,exist_ok=False)
    try:
        download_url=source
        source_error=None
        try:
            data=fetch_archive(source)
        except NETWORK_ERRORS as exc:
            source_error=str(exc)
            download_url=SCIFACT_MIRROR
            try:
                data=fetch_archive(download_url)
            except NETWORK_ERRORS as mirror_error:
                raise RuntimeError(f'SciFact download failed: official source: {exc}; mirror: {mirror_error}') from mirror_error
        sha256=hashlib.sha256(data).hexdigest()
        if hashlib.md5(data).hexdigest()!=expected_md5:
            raise ValueError(f'BEIR SciFact MD5 mismatch from {download_url}')
        if (expected_md5==SCIFACT_MD5 or source_error is not None) and sha256!=SCIFACT_SHA256:
            raise ValueError(f'BEIR SciFact SHA-256 mismatch from {download_url}')
        with ZipFile(BytesIO(data)) as archive:
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
        candidates=list(dest.rglob('corpus.jsonl'))
        if len(candidates)!=1:raise ValueError('dataset corpus file missing or ambiguous')
        folder=candidates[0].parent
        if not (folder/'queries.jsonl').is_file() or not (folder/'qrels'/'test.tsv').is_file():
            raise ValueError('official SciFact qrels/queries missing')
        record={'dataset':'BEIR SciFact','url':download_url,'md5':expected_md5,
                'archive_sha256':sha256,
                'corpus':str((folder/'corpus.jsonl').relative_to(dest)),
                'queries':str((folder/'queries.jsonl').relative_to(dest)),
                'qrels':str((folder/'qrels'/'test.tsv').relative_to(dest))}
        if source_error is not None:
            record['official_source_error']=source_error
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
