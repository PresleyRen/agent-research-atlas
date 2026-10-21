#!/usr/bin/env python3
"""Offline editable reconstruction. Native draw.io + SVG from a shared scene.

The SVG is a companion export, not a render of draw.io XML. Inkscape renders it.
Only the small source-detail panel remains raster; no whole-page image is embedded.
"""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
SRC = ROOT / "sources"
ASSETS = ROOT / "assets"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def create_scene() -> dict:
    # Coordinates were transcribed after inspecting reference.png (1000 x 540 px).
    # The feedback label moves below the line to avoid the source label/box overlap.
    return {
        "figure_id": "fig01_architecture",
        "reference": "reference.png",
        "reference_sha256": sha256(ROOT / "reference.png"),
        "canvas": {"width": 1000, "height": 540, "paper_width_mm": 180},
        "style": {"font_family": "DejaVu Sans", "font_size": 21,
                  "fill": "#eaf2ff", "stroke": "#203e63", "text": "#183153",
                  "edge": "#35445c", "stroke_width": 2.5, "edge_width": 4},
        "nodes": [
            {"id": "user_request", "label": "User request", "x": 36, "y": 81, "w": 199, "h": 64},
            {"id": "version_state", "label": "Version state", "x": 301, "y": 81, "w": 209, "h": 64},
            {"id": "router", "label": "Router", "x": 581, "y": 81, "w": 179, "h": 64},
            {"id": "clarify", "label": "Clarify", "x": 301, "y": 236, "w": 209, "h": 64},
            {"id": "retriever", "label": "Retriever", "x": 581, "y": 236, "w": 179, "h": 64},
            {"id": "answer", "label": "Answer", "x": 581, "y": 397, "w": 179, "h": 64},
        ],
        "edges": [
            {"id": "e_request_state", "source": "user_request", "target": "version_state",
             "points": [[235, 113], [301, 113]], "exit": [1, .5], "entry": [0, .5]},
            {"id": "e_state_router", "source": "version_state", "target": "router",
             "points": [[510, 113], [581, 113]], "exit": [1, .5], "entry": [0, .5]},
            {"id": "e_router_retriever", "source": "router", "target": "retriever",
             "points": [[670.5, 145], [670.5, 236]], "exit": [.5, 1], "entry": [.5, 0]},
            {"id": "e_retriever_answer", "source": "retriever", "target": "answer",
             "points": [[670.5, 300], [670.5, 397]], "exit": [.5, 1], "entry": [.5, 0]},
            {"id": "e_router_clarify", "source": "router", "target": "clarify",
             "points": [[581, 130], [551, 130], [551, 268], [510, 268]],
             "exit": [0, .765625], "entry": [1, .5]},
            {"id": "e_clarify_request", "source": "clarify", "target": "user_request",
             "points": [[301, 268], [135.5, 268], [135.5, 145]],
             "exit": [0, .5], "entry": [.5, 1]},
        ],
        "labels": [
            {"id": "feedback_label", "text": "clarification feedback", "x": 91, "y": 308,
             "w": 260, "h": 30, "anchor": "start", "font_size": 21},
            {"id": "source_detail_label", "text": "source detail", "x": 805, "y": 460,
             "w": 145, "h": 30, "anchor": "middle", "font_size": 21},
        ],
        "raster": {"id": "source_detail_image", "path": "assets/source_detail.png",
                   "crop_box_xyxy": [825, 345, 926, 446], "x": 825, "y": 345, "w": 101, "h": 101,
                   "meaning": "Unquantified visual detail copied from the supplied source, not chart data."},
        "layout_changes": ["Feedback label moved below the Clarify box to remove the overlap visible in the reference; topology and wording unchanged."],
        "native_render_status": "not_checked_no_drawio_renderer",
    }


def write_drawio(scene: dict, png_bytes: bytes) -> None:
    s = scene["style"]
    mxfile = ET.Element("mxfile", {"host": "offline-editable-reconstruction", "type": "device"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": "fig01", "name": "Reference reconstruction"})
    model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1000", "dy": "540", "grid": "1", "gridSize": "10", "guides": "1",
        "tooltips": "1", "connect": "1", "arrows": "1", "fold": "1", "page": "1",
        "pageScale": "1", "pageWidth": "1000", "pageHeight": "540", "background": "#ffffff",
        "math": "0", "shadow": "0"})
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    for layer, label in [("1", "01 Connectors"), ("layer_modules", "02 Modules"),
                         ("layer_labels", "03 Labels"), ("layer_detail", "04 Source detail (raster)")]:
        ET.SubElement(root, "mxCell", {"id": layer, "value": label, "parent": "0"})
    for e in scene["edges"]:
        ex, ey = e["exit"]
        ix, iy = e["entry"]
        style = (f"edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=0;"
                 f"strokeColor={s['edge']};strokeWidth={s['edge_width']};endArrow=block;endFill=1;endSize=10;"
                 f"exitX={ex};exitY={ey};exitDx=0;exitDy=0;exitPerimeter=0;"
                 f"entryX={ix};entryY={iy};entryDx=0;entryDy=0;entryPerimeter=0;")
        c = ET.SubElement(root, "mxCell", {"id": e["id"], "value": "", "edge": "1", "parent": "1",
                                         "source": e["source"], "target": e["target"], "style": style})
        geo = ET.SubElement(c, "mxGeometry", {"relative": "1", "as": "geometry"})
        if len(e["points"]) > 2:
            waypoints = ET.SubElement(geo, "Array", {"as": "points"})
            for x, y in e["points"][1:-1]:
                ET.SubElement(waypoints, "mxPoint", {"x": str(x), "y": str(y)})
    for n in scene["nodes"]:
        style = (f"rounded=1;arcSize=16;whiteSpace=wrap;html=0;fillColor={s['fill']};"
                 f"strokeColor={s['stroke']};strokeWidth={s['stroke_width']};fontColor={s['text']};"
                 f"fontFamily={s['font_family']};fontSize={s['font_size']};align=center;verticalAlign=middle;")
        c = ET.SubElement(root, "mxCell", {"id": n["id"], "value": n["label"], "vertex": "1",
                                         "parent": "layer_modules", "style": style})
        ET.SubElement(c, "mxGeometry", {"x": str(n["x"]), "y": str(n["y"]),
                                       "width": str(n["w"]), "height": str(n["h"]), "as": "geometry"})
    for l in scene["labels"]:
        align = "left" if l["anchor"] == "start" else "center"
        style = (f"text;html=0;strokeColor=none;fillColor=none;align={align};verticalAlign=middle;"
                 f"whiteSpace=wrap;rounded=0;fontFamily={s['font_family']};fontSize={l['font_size']};"
                 f"fontColor={s['edge']};spacing=0;")
        c = ET.SubElement(root, "mxCell", {"id": l["id"], "value": l["text"], "vertex": "1",
                                         "parent": "layer_labels", "style": style})
        ET.SubElement(c, "mxGeometry", {"x": str(l["x"]), "y": str(l["y"]),
                                       "width": str(l["w"]), "height": str(l["h"]), "as": "geometry"})
    r = scene["raster"]
    # draw.io uses image/png,<base64> (without ;base64) inside mxCell style strings.
    data_uri = "data:image/png," + base64.b64encode(png_bytes).decode("ascii")
    c = ET.SubElement(root, "mxCell", {"id": r["id"], "value": "", "vertex": "1", "parent": "layer_detail",
                                     "style": f"shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;image={data_uri};"})
    ET.SubElement(c, "mxGeometry", {"x": str(r["x"]), "y": str(r["y"]),
                                   "width": str(r["w"]), "height": str(r["h"]), "as": "geometry"})
    ET.indent(mxfile)
    ET.ElementTree(mxfile).write(OUT / "fig01_architecture.drawio", encoding="utf-8", xml_declaration=True)


def write_svg(scene: dict, png_bytes: bytes) -> None:
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    q = lambda tag: f"{{{ns}}}{tag}"
    svg = ET.Element(q("svg"), {"width": "180mm", "height": "97.2mm", "viewBox": "0 0 1000 540",
                              "version": "1.1", "role": "img", "aria-labelledby": "title desc"})
    ET.SubElement(svg, q("title"), {"id": "title"}).text = "Editable reconstruction of the supplied agent architecture"
    ET.SubElement(svg, q("desc"), {"id": "desc"}).text = (
        "User request to Version state to Router. Router to Retriever to Answer. "
        "Router to Clarify to User request. Small source detail is a raster crop, not measured data. "
        "Companion SVG generated from the same scene as draw.io; not a native draw.io export.")
    defs = ET.SubElement(svg, q("defs"))
    s = scene["style"]
    marker = ET.SubElement(defs, q("marker"), {"id": "arrow", "viewBox": "0 0 10 8", "refX": "10", "refY": "4",
                                            "markerWidth": "10", "markerHeight": "8", "markerUnits": "userSpaceOnUse", "orient": "auto"})
    ET.SubElement(marker, q("path"), {"d": "M 0 0 L 10 4 L 0 8 z", "fill": s["edge"]})
    ET.SubElement(svg, q("rect"), {"id": "background", "width": "1000", "height": "540", "fill": "#ffffff"})
    edge_group = ET.SubElement(svg, q("g"), {"id": "connectors", "fill": "none", "stroke": s["edge"],
                                           "stroke-width": str(s["edge_width"]), "stroke-linejoin": "round"})
    for e in scene["edges"]:
        d = "M " + " L ".join(f"{x},{y}" for x, y in e["points"])
        ET.SubElement(edge_group, q("path"), {"id": e["id"], "d": d, "marker-end": "url(#arrow)",
                                             "data-source": e["source"], "data-target": e["target"]})
    modules = ET.SubElement(svg, q("g"), {"id": "modules", "font-family": s["font_family"],
                                         "font-size": str(s["font_size"]), "fill": s["text"]})
    for n in scene["nodes"]:
        g = ET.SubElement(modules, q("g"), {"id": n["id"]})
        ET.SubElement(g, q("rect"), {"x": str(n["x"]), "y": str(n["y"]), "width": str(n["w"]), "height": str(n["h"]),
                                    "rx": "12", "fill": s["fill"], "stroke": s["stroke"], "stroke-width": str(s["stroke_width"])})
        ET.SubElement(g, q("text"), {"x": str(n["x"] + n["w"] / 2), "y": str(n["y"] + n["h"] / 2 + 7.4),
                                    "text-anchor": "middle"}).text = n["label"]
    labels = ET.SubElement(svg, q("g"), {"id": "labels", "font-family": s["font_family"], "fill": s["edge"]})
    for l in scene["labels"]:
        x = l["x"] if l["anchor"] == "start" else l["x"] + l["w"] / 2
        ET.SubElement(labels, q("text"), {"id": l["id"], "x": str(x), "y": str(l["y"] + l["h"] / 2 + 7.4),
                                         "text-anchor": l["anchor"], "font-size": str(l["font_size"])}).text = l["text"]
    r = scene["raster"]
    ET.SubElement(svg, q("image"), {"id": r["id"], "x": str(r["x"]), "y": str(r["y"]), "width": str(r["w"]), "height": str(r["h"]),
                                   "preserveAspectRatio": "none", "{http://www.w3.org/1999/xlink}href": "data:image/png;base64," + base64.b64encode(png_bytes).decode("ascii")})
    ET.indent(svg)
    ET.ElementTree(svg).write(OUT / "fig01_architecture.svg", encoding="utf-8", xml_declaration=True)


def main() -> None:
    for path in (OUT, SRC, ASSETS):
        path.mkdir(parents=True, exist_ok=True)
    scene_path = SRC / "architecture_scene.json"
    # Existing scene is authoritative for reproducible coordinate/label edits.
    scene = json.loads(scene_path.read_text()) if scene_path.exists() else create_scene()
    if sha256(ROOT / scene["reference"]) != scene["reference_sha256"]:
        raise RuntimeError("Reference changed; re-inspect before rebuilding.")
    Image.open(ROOT / scene["reference"]).crop(scene["raster"]["crop_box_xyxy"]).save(ROOT / scene["raster"]["path"])
    png_bytes = (ROOT / scene["raster"]["path"]).read_bytes()
    scene["raster"]["sha256"] = sha256(ROOT / scene["raster"]["path"])
    scene_path.write_text(json.dumps(scene, indent=2, ensure_ascii=False) + "\n")
    write_drawio(scene, png_bytes)
    write_svg(scene, png_bytes)
    print(json.dumps({"native_modules": len(scene["nodes"]), "native_connectors": len(scene["edges"]),
                      "native_extra_labels": len(scene["labels"]), "raster_regions": 1,
                      "drawio_native_render": "not performed; renderer unavailable"}, indent=2))


if __name__ == "__main__":
    main()
