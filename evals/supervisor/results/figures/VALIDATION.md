# 实际检查记录

日期：2026-10-21。执行者：本地制图助手；为同一执行者的检查，不宣称独立同行审核。

## 原始材料与来源

制作前实际打开并查看 `reference.png`，完整阅读 `PROJECT.md`、`notes/figure-context.md` 与 `results/latency-accuracy.csv`。参考图为 1000 × 540 px。拓扑同时与项目说明核对；读到的表格只有三个合成数据点。

`scripts/verify_artifacts.py` 逐项核对 `INPUT-MANIFEST.json` 中四个输入的 SHA-256 与字节数。检查结果见 `checks/artifact_verification.json`。该校验保障本轮未改动原文件，不保证原始资料的外部真实性。

## 架构图

| 检查 | 实际结果 | 证据 / 边界 |
|---|---|---|
| 参考图视觉读取 | 完成 | 实际查看 supplied `reference.png`，无依赖图片文件名猜测 |
| 原生 drawio 对象 | 完成结构检查 | 6 个模块、6 条边、2 个额外文字对象、1 个 101 × 101 px 小图片；不是整图嵌入 |
| 有向拓扑 | 通过结构与 SVG 预览核对 | 六条边 source/target 和箭头标记均匹配 `notes/FIGURE-BRIEF.md` 的独立清单 |
| 小块来源 | 通过 | `assets/source_detail.png` 像素与原图 `[825,345,926,446)` 裁剪一致 |
| SVG 实际渲染 | 完成并视觉查看 | Inkscape 1.2.2 → `outputs/fig01_architecture.png` |
| PDF 实际渲染 | 完成并视觉查看 | Inkscape 导出 PDF；PyMuPDF 栅格化为 `checks/fig01_architecture_pdf_render.png` |
| 文字/对齐/截断/方向 | 伴随 SVG/PDF 中通过 | 六个模块文字清楚；箭头进入正确端点；反馈标签下移后无遮挡；小块标签完整 |
| drawio 原生应用渲染与交互 | **未完成** | 本地没有 drawio/diagrams.net 导出器或桌面应用，且禁止安装、联网；仍需在已有原生应用中打开、导出、拖动模块并复核连线 |

**准确界定：** PNG 与 PDF 是同一 JSON 场景生成的 SVG 经实际渲染所得，并非 drawio XML 通过 drawio 原生引擎生成。drawio 交付状态为“可编辑源已构建、结构已核验；原生渲染待验证”。

## 数据图

| 检查 | 实际结果 |
|---|---|
| CSV 与图中数字 | 三行方法、延迟、百分比标签逐项一致；变换为 accuracy × 100 |
| SVG 可编辑性 | 文字保留 `<text>` 元素，点/坐标轴为矢量，未包含栅格图 |
| 方向与量纲 | 延迟 ms 横轴向右增加；准确率 % 纵轴向上增加；改善方向为左上方 |
| 不确定性与分母 | 未提供，未伪造误差条、样本量、置信区间或显著性 |
| 非零纵轴 | 显示 65–86%，图内与图注均声明；散点不连接、不插值 |
| 首次预览缺陷 | 观察到横轴标题与图下注释重叠；已增大下边距并下移说明文字 |
| 修复验证 | Matplotlib 重新生成 PNG；Inkscape 实际渲染 SVG；PyMuPDF 实际渲染 PDF；三种最终预览均打开查看，未再见遮挡或截断 |
| 页面与文字边界 | 90 × 76 mm；程序检查标题、轴标签、点标注、图注边界及横轴标题与图注不重叠 |

已查看预览：`outputs/fig02_latency_accuracy.png`、`checks/fig02_svg_render.png`、`checks/fig02_latency_accuracy_pdf_render.png`。视觉结果仅反映当前版本，不自动继承给未来编辑。

## 实际执行环境与日志

- Python 3.12.14；Pillow 12.3.0；Matplotlib 3.10.8；NumPy 2.3.5；Inkscape 1.2.2；PyMuPDF 可用。
- `rebuild_architecture.py`、`plot_latency_accuracy.py`、`render_previews.py` 执行返回 0，生成对应文件。
- Inkscape 的三次最终导出返回 0，仍记录 `GtkRecentManager` 初始化警告；该警告未阻止文件生成，已通过打开实际导出复核。完整输出见 `checks/render_log.json`。
- 对源数据/图片、场景、脚本和图稿保存 SHA-256 记录；无外部网络或付费操作。
- `verify_artifacts.py` 返回 0：四个输入原文件哈希与字节数一致；六个原生模块、六条有向边、两条标签与一个独立位图小块通过结构核验；三行 CSV 与 SVG 可见文字匹配。
- `audit.py values` 返回 0：`sources/numerical_claim_ledger.json` 的六个图中数值与四个算术差值共 10 项均与 `outputs/fig02_data_ledger.json` 的指定字段精确匹配；通过记录的 SHA-256 绑定当前账本版本。结果见 `checks/numerical_audit.json`。CSV 到图中标签的检查由上述脚本单独完成，JSON 数值审计本身不验证 CSV 或实验设计。
- `atlas.py check` 返回 0：revision 1，21 个节点、6 条关系，结构有效；`status` 显示无待处理证据复核和无语义导入。`audit.py project` 仍报告 14 个领域 unsearched，与本轮不做文献研究的范围一致。结构通过不代表 drawio 原生检查完成，也不代表科学结论成立。

## 保留余项

1. 在现有离线 draw.io 应用中检查原生布局、字体替换、图片显示、箭头方向及模块拖动后的端点吸附，再导出一份原生预览并更新此记录。
2. 未给定目标期刊，未核实其最新尺寸/字体/文件要求；当前尺寸可作为排版起点。
3. 数据为明确标记的合成夹具，无真实实验设计、样本分母和不确定性。因此本轮不做科学有效性、显著性、方法优越性、创新性或录用概率判断。
