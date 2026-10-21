#!/usr/bin/env python3
"""Targeted artifact/provenance checks. This does not simulate a draw.io renderer."""
from pathlib import Path
import base64
import csv
import hashlib
import json
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = {}
    manifest = json.loads((ROOT / "INPUT-MANIFEST.json").read_text())
    checks["input_integrity"] = []
    for f in manifest["files"]:
        p = ROOT / f["path"]
        actual = digest(p)
        passed = actual == f["sha256"] and p.stat().st_size == f["bytes"]
        checks["input_integrity"].append({"path": f["path"], "bytes": p.stat().st_size,
                                          "sha256": actual, "unchanged": passed})
        assert passed, f"Changed input: {f['path']}"
    scene = json.loads((ROOT / "sources/architecture_scene.json").read_text())
    # Independent topology inventory transcribed from inspected reference + PROJECT.md.
    expected_nodes = {"user_request": "User request", "version_state": "Version state", "router": "Router",
                      "retriever": "Retriever", "answer": "Answer", "clarify": "Clarify"}
    expected_edges = {("user_request", "version_state"), ("version_state", "router"),
                      ("router", "retriever"), ("retriever", "answer"),
                      ("router", "clarify"), ("clarify", "user_request")}
    doc = ET.parse(ROOT / "outputs/fig01_architecture.drawio")
    cells = doc.findall(".//mxCell")
    vertices = {c.get("id"): c for c in cells if c.get("vertex") == "1"}
    edges = [c for c in cells if c.get("edge") == "1"]
    assert {k: vertices[k].get("value") for k in expected_nodes} == expected_nodes
    assert {(e.get("source"), e.get("target")) for e in edges} == expected_edges
    assert len(edges) == 6
    assert all("endArrow=block;" in e.get("style") and e.get("source") in vertices and e.get("target") in vertices for e in edges)
    assert {"feedback_label", "source_detail_label"}.issubset(vertices)
    raster_cells = [c for c in vertices.values() if "shape=image;" in c.get("style", "")]
    assert len(raster_cells) == 1
    image_geometry = raster_cells[0].find("mxGeometry")
    assert image_geometry.get("width") == "101" and image_geometry.get("height") == "101"
    crop = Image.open(ROOT / "assets/source_detail.png")
    source_crop = Image.open(ROOT / "reference.png").crop(scene["raster"]["crop_box_xyxy"])
    assert crop.size == (101, 101) and crop.tobytes() == source_crop.tobytes()
    checks["drawio_structure"] = {"status": "passed", "native_modules": 6, "native_connectors": 6,
                                  "native_extra_labels": 2, "raster_regions": 1, "full_page_image": False,
                                  "expected_directed_edges": sorted([list(e) for e in expected_edges]),
                                  "native_application_render": "not_checked_renderer_unavailable"}
    ns = {"s": "http://www.w3.org/2000/svg"}
    architecture_svg = ET.parse(ROOT / "outputs/fig01_architecture.svg")
    assert len(architecture_svg.findall(".//s:image", ns)) == 1
    assert len(architecture_svg.findall(".//s:text", ns)) == 8
    svg_connectors = architecture_svg.findall(".//s:g[@id='connectors']/s:path", ns)
    assert {(e.get("data-source"), e.get("data-target")) for e in svg_connectors} == expected_edges
    assert all(e.get("marker-end") == "url(#arrow)" for e in svg_connectors)
    chart_svg = ET.parse(ROOT / "outputs/fig02_latency_accuracy.svg")
    texts = ["".join(e.itertext()) for e in chart_svg.findall(".//s:text", ns)]
    with (ROOT / "results/latency-accuracy.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        assert row["method"] in texts
        assert f"{float(row['latency_ms']):g} ms, {float(row['accuracy']) * 100:g}%" in texts
    assert len(chart_svg.findall(".//s:image", ns)) == 0
    checks["svg_editability_and_values"] = {"status": "passed", "architecture_text_elements": 8,
                                           "chart_text_elements": len(texts), "chart_raster_images": 0,
                                           "csv_rows_matched_to_visible_labels": len(rows)}
    checks["previews"] = []
    for p in sorted((ROOT / "outputs").glob("*.png")) + sorted((ROOT / "checks").glob("*render.png")):
        im = Image.open(p)
        checks["previews"].append({"path": str(p.relative_to(ROOT)), "size": list(im.size), "mode": im.mode})
    checks["scope"] = "File integrity, native structure, topology and numerical labels. Human visual observations are recorded separately in VALIDATION.md."
    (ROOT / "checks/artifact_verification.json").write_text(json.dumps(checks, indent=2, ensure_ascii=False) + "\n")
    generated = []
    for folder in ["outputs", "sources", "scripts", "assets"]:
        for p in sorted((ROOT / folder).glob("*")):
            if p.is_file():
                generated.append({"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size, "sha256": digest(p)})
    (ROOT / "checks/output_manifest.json").write_text(json.dumps({"files": generated}, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(checks, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
