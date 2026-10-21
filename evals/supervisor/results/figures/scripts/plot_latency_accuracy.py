#!/usr/bin/env python3
"""Plot supplied synthetic fixture; never infer uncertainty or experimental runs."""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> None:
    source = ROOT / "results" / "latency-accuracy.csv"
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    with source.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 3:
        raise ValueError("Plot design expects the supplied three-method fixture; review layout for changed data.")
    for r in rows:
        r["latency_ms"] = float(r["latency_ms"])
        r["accuracy"] = float(r["accuracy"])
        if not (r["latency_ms"] >= 0 and 0 <= r["accuracy"] <= 1):
            raise ValueError("Invalid latency or accuracy.")
        r["accuracy_pct"] = r["accuracy"] * 100
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 7.5,
                         "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7,
                         "svg.fonttype": "none", "svg.hashsalt": "agent-figure-fixture-v1",
                         "pdf.fonttype": 42, "ps.fonttype": 42, "axes.linewidth": .7,
                         "savefig.facecolor": "white"})
    # 90 x 76 mm, suitable for a common single-column width. No venue was supplied.
    fig, ax = plt.subplots(figsize=(90 / 25.4, 76 / 25.4))
    fig.subplots_adjust(left=.18, right=.96, bottom=.29, top=.89)
    ax.set_xlim(0, 350)
    ax.set_ylim(65, 86)
    ax.set_xticks([0, 50, 100, 150, 200, 250, 300, 350])
    ax.set_yticks([65, 70, 75, 80, 85])
    ax.set_xlabel("Latency (ms; lower is better)", labelpad=5)
    ax.set_ylabel("Accuracy (%; higher is better)", labelpad=5)
    ax.grid(True, color="#dce1e6", linewidth=.55, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(length=3, width=.65, color="#485663")
    styles = [("#0072B2", "o", (0, 10), "center", "bottom"),
              ("#D55E00", "s", (0, -13), "center", "top"),
              ("#009E73", "^", (-3, 11), "right", "bottom")]
    annotations = []
    for row, (color, marker, offset, ha, va) in zip(rows, styles):
        ax.scatter(row["latency_ms"], row["accuracy_pct"], s=37, marker=marker, color=color,
                   edgecolor="white", linewidth=.65, zorder=3)
        text = f"{row['method']}\n{row['latency_ms']:g} ms, {row['accuracy_pct']:g}%"
        a = ax.annotate(text, xy=(row["latency_ms"], row["accuracy_pct"]), xytext=offset,
                        textcoords="offset points", ha=ha, va=va, fontsize=7.15, linespacing=1.3,
                        color="#1d2b37", zorder=4)
        annotations.append(a)
    fig.text(.18, .965, "Latency–accuracy trade-off", ha="left", va="top", fontsize=9, weight="bold")
    fig.text(.18, .08, "Synthetic fixtures; no repeated runs or uncertainty supplied.",
             ha="left", va="center", fontsize=6.2, color="#54616b")
    fig.text(.18, .035, "Y-axis shown from 65%; each marker is one supplied value.",
             ha="left", va="center", fontsize=6.2, color="#54616b")
    # Verify actual text extents fit the page before export.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    fb = fig.bbox
    clipped = []
    for t in [*annotations, *fig.texts, ax.xaxis.label, ax.yaxis.label]:
        bb = t.get_window_extent(renderer)
        if bb.x0 < fb.x0 or bb.y0 < fb.y0 or bb.x1 > fb.x1 or bb.y1 > fb.y1:
            clipped.append(t.get_text())
    if clipped:
        raise RuntimeError(f"Text outside figure: {clipped}")
    xlabel_bb = ax.xaxis.label.get_window_extent(renderer)
    footer_bbs = [t.get_window_extent(renderer) for t in fig.texts[1:]]
    if any(xlabel_bb.overlaps(bb) for bb in footer_bbs):
        raise RuntimeError("X-axis label overlaps a figure note.")
    metadata = {"Title": "Latency–accuracy trade-off (synthetic fixtures)",
                "Subject": "No repetitions or uncertainty estimates were supplied; descriptive plot only.",
                "Creator": "plot_latency_accuracy.py with Matplotlib"}
    fig.savefig(out / "fig02_latency_accuracy.svg", metadata={"Title": metadata["Title"], "Description": metadata["Subject"], "Date": None})
    fig.savefig(out / "fig02_latency_accuracy.pdf", metadata={**metadata, "CreationDate": None, "ModDate": None})
    fig.savefig(out / "fig02_latency_accuracy.png", dpi=300, metadata={"Description": metadata["Subject"]})
    plt.close(fig)
    ledger = {"figure_id": "fig02_latency_accuracy", "source": str(source.relative_to(ROOT)),
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "synthetic": True,
              "rows": rows, "uncertainty": "not supplied; no error bars drawn",
              "aggregation": "none; each row plotted once", "denominator": "not supplied",
              "axes": {"x": "latency_ms", "x_range": [0, 350], "x_better": "lower", "x_scale": "linear",
                       "y": "accuracy * 100", "y_range": [65, 86], "y_better": "higher", "y_scale": "linear"},
              "page_mm": [90, 76], "text_extent_check": "passed", "matplotlib_version": matplotlib.__version__,
              "derived_differences": {"version_minus_single_latency_ms": rows[1]["latency_ms"] - rows[0]["latency_ms"],
                                      "version_minus_single_accuracy_pp": rows[1]["accuracy_pct"] - rows[0]["accuracy_pct"],
                                      "always_minus_version_latency_ms": rows[2]["latency_ms"] - rows[1]["latency_ms"],
                                      "always_minus_version_accuracy_pp": rows[2]["accuracy_pct"] - rows[1]["accuracy_pct"]}}
    (out / "fig02_data_ledger.json").write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(ledger, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
