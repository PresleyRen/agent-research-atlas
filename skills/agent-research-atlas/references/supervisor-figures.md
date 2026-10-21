# Scientific figures and editable reconstruction (C28)

Adapted and substantially revised from Supervisor-Skills `figure-designer` and the separately MIT-licensed `drawio-reconstruction` documentation at [commit a20d76e](https://github.com/HKUSTDial/Supervisor-Skills/tree/a20d76ef3979b804d7dbf599d577826957e0a8a9). Attribution: Yuyu Luo and contributors; the drawio subdirectory's license credits VCG-Bench Authors (2026). This combined workbench is **CC BY-NC-SA 4.0**; see `LICENSE.supervisor.md`. The upstream drawing runtime is an optional integration.

## Start with the figure's job

Use `assets/supervisor/figure-brief.md`. State the reader's question, the scientific proposition, source data/diagram, reading order, intended medium and editable deliverable.

| Figure | What it should explain | Inspect first |
|---|---|---|
| Motivating example | A concrete failure or need that the study addresses | Source case, comparison conditions, visible observations |
| Method overview | How information and control flow implement the mechanism | Inputs, outputs, module roles, state, arrows and boundaries |
| Experimental result | What the measurement shows and under which conditions | Raw records, aggregation, denominator, uncertainty, units and axes |
| Reference reconstruction | The visible topology and appearance of an existing figure | Objects, text, groups, connectors, geometry and ambiguous regions |

A paper overview and a research-history map serve different purposes. Keep the persistent atlas as the project record; derive a concise paper figure from its selected claims and mechanisms.

## Design from evidence

Choose comparisons and encodings that answer the reader's question. Keep labels, notation, units, colors and module names consistent with the manuscript and code. Explain conditions and uncertainty in the caption when needed. Use current official venue specifications for dimensions, fonts and export requirements.

For results, derive points and error bars from actual records and the declared analysis. Record data and plotting-code versions. Choose axes according to the encoded quantity: bar lengths usually require a meaningful common baseline; line/scatter plots may need a restricted range to expose relevant variation. Explain transformations, breaks and unusual scales. Do not impose nonzero or zero axes universally.

State whether each axis is to be minimized or maximized. For latency on the horizontal axis and accuracy on the vertical axis, the desirable direction is toward lower latency and higher accuracy. Do not move the preferred method, reverse quantities or declare the upper-right corner universally best.

Use vector elements for text, connectors and geometric diagrams when possible. Raster photographs, heatmaps and source-detail crops can remain appropriate within a mixed figure. Preserve an editable source file and render a preview at the intended reading size.

## Reconstruct a reference into editable objects

1. Inspect the supplied image or PDF with an available reader. Inventory labels, nodes, groups, connectors, arrow direction, ordering and uncertain text before drafting.
2. Plan the layer/group structure and coordinate system. Build native text, shapes and connectors for the parts whose structure can be recovered.
3. Represent complex visual detail with an attributed crop only when native reconstruction would obscure the intended content or is impractical. Keep it separate from editable logical elements.
4. Export a rendered preview through an available supported renderer and compare it with the reference: content, every connector's endpoints/direction and route, text, alignment, clipping, contrast and readability. Correct observed errors.
5. Deliver the native file, preview and a short editing map: which components are native editable objects, which regions are raster crops, and which ambiguities remain. For a batch, retain per-case status and paths rather than reporting only the successful cases. An incomplete or needs-fix reconstruction remains in that state until the missing check or repair is actually completed.

An image embedded inside a `.drawio` file is not by itself an editable reconstruction. Inspect the native objects and connectors. Conversely, a valid XML file alone does not establish correct rendering or faithful topology. If a renderer is unavailable, deliver the source and state which visual check remains; do not invent a preview.

Use an existing drawing skill or the separately licensed upstream implementation when the host provides it. Review its dependencies and actual file interfaces before use. The research workflow chooses the figure's purpose and validates its claim; it does not require a specific commercial drawing service.

## Preserve meaning across visuals

Reconstruct the source as observed. Put a proposed scientific or layout correction in a separate version when it changes topology or meaning. Do not silently reverse an arrow, add a result, infer a missing mechanism or remove a difficult label to make the picture cleaner.

Connect figure IDs to manuscript claims and source/run IDs. Revisit the figure when those dependencies change. For extension work, locate C28 and separately inspect whether the missing part is scientific design, native-object construction, export or visual review.
