#!/usr/bin/env python3
"""Render exported vector files with available offline tools; no draw.io renderer."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / "checks"
CHECKS.mkdir(exist_ok=True)
env = os.environ.copy()
for key, directory in {"INKSCAPE_PROFILE_DIR": ROOT / ".cache/inkscape",
                       "XDG_CACHE_HOME": ROOT / ".cache",
                       "XDG_DATA_HOME": ROOT / ".cache/data",
                       "XDG_CONFIG_HOME": ROOT / ".cache/config"}.items():
    directory.mkdir(parents=True, exist_ok=True)
    env[key] = str(directory)

cmds = [
    ["inkscape", str(ROOT / "outputs/fig01_architecture.svg"), "--export-type=png",
     f"--export-filename={ROOT}/outputs/fig01_architecture.png", "--export-dpi=180"],
    ["inkscape", str(ROOT / "outputs/fig01_architecture.svg"), "--export-type=pdf",
     f"--export-filename={ROOT}/outputs/fig01_architecture.pdf"],
    ["inkscape", str(ROOT / "outputs/fig02_latency_accuracy.svg"), "--export-type=png",
     f"--export-filename={CHECKS}/fig02_svg_render.png", "--export-dpi=200"],
]
records = []
for cmd in cmds:
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    records.append({"command": cmd, "returncode": r.returncode, "stdout": r.stdout, "stderr": r.stderr})
    if r.returncode:
        (CHECKS / "render_log.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
        raise SystemExit(r.returncode)

# Render the actual PDFs for inspection, rather than assuming export succeeded.
import fitz
for name in ["fig01_architecture", "fig02_latency_accuracy"]:
    path = ROOT / "outputs" / f"{name}.pdf"
    with fitz.open(path) as doc:
        if len(doc) != 1:
            raise ValueError(f"Expected one page in {path}")
        page = doc[0]
        page.get_pixmap(dpi=150, alpha=False).save(CHECKS / f"{name}_pdf_render.png")
        records.append({"operation": "PyMuPDF actual PDF rasterization", "source": str(path.relative_to(ROOT)),
                        "pages": len(doc), "page_size_pt": list(page.rect), "text": page.get_text(), "status": "success"})
(CHECKS / "render_log.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(records, ensure_ascii=False, indent=2))
