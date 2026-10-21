# 科研图稿交接

**日期：2026-10-21。完成范围：原图的可编辑重建、给定三行合成数据的论文格式散点图、实际可生成预览的检查、双语图注、编辑说明和研究地图关联。**

所有交付保存在本项目内。未联网、安装依赖、执行模型推理、购买服务或对外发布；未读取 distribution 中的 evals/results 或测试答案。制作前实际查看 `reference.png`，随后按可见内容重建。原图、原始 CSV 与说明文件均保留原字节，四项输入完整性检查通过。

## 直接交付

| 图 / 状态 | 原生或可编辑源 | 实际预览与排版文件 | 编辑与检查边界 |
|---|---|---|---|
| 图 1 架构重建；**原生预览待验证** | [fig01_architecture.drawio](outputs/fig01_architecture.drawio)、[fig01_architecture.svg](outputs/fig01_architecture.svg)、[共同场景 JSON](sources/architecture_scene.json) | [PNG](outputs/fig01_architecture.png)、[PDF](outputs/fig01_architecture.pdf)；已查看 PDF 栅格预览 | 6 个模块、6 条连线、2 个说明文字为原生对象；仅 source detail 小块为独立位图。XML/拓扑已检查；draw.io 原生渲染和交互未检查 |
| 图 2 延迟—准确率；**实际预览已检查** | [fig02_latency_accuracy.svg](outputs/fig02_latency_accuracy.svg)、[绘图代码](scripts/plot_latency_accuracy.py) | [PDF](outputs/fig02_latency_accuracy.pdf)、[300 dpi PNG](outputs/fig02_latency_accuracy.png)；另有 SVG/PDF 的实际渲染检查图 | SVG 文字、点、坐标轴均为矢量；数据与脚本保留。合成夹具不构成真实实验结果 |

补充文件：[双语图注](CAPTIONS.md)、[编辑说明](EDITING.md)、[设计说明与来源](notes/FIGURE-BRIEF.md)、[实际检查记录](VALIDATION.md)。

## 图 1 保留了什么

重建保留 `User request → Version state → Router`，`Router → Retriever → Answer` 以及 `Router → Clarify → User request`，共六条有向边。模块顺序与分支方向未改变。反馈标签移到 Clarify 下方，修复原图文字接近模块边缘的问题；这只是版式调整。未增加实验成功徽章。

右下角小方阵直接裁自 `reference.png` 的 `[825,345,926,446)` 区域，保留在 [source_detail.png](assets/source_detail.png)。它是 101 × 101 px 的独立位图视觉细节，未当作新数据、未补造数值或色标。原图没有整页嵌入 drawio。

图 1 的 SVG/PDF 与 drawio 来自同一 JSON 场景，**这些预览不是 drawio 原生导出**。当前没有 draw.io/diagrams.net 导出器，在禁止安装和联网的约束下，本轮完成了 XML、原生对象、端点方向以及伴随 SVG/PDF 的检查；原生应用显示、字体替换、图片显示及拖动后的端点吸附仍需在已有离线编辑器中确认。

## 图 2 的数值与解释

来源：[latency-accuracy.csv](results/latency-accuracy.csv) 表头和第 2–4 行；这是明确标记为 synthetic fixture 的输入。

| 方法 | 延迟（ms） | 准确率 |
|---|---:|---:|
| Single-pass | 120 | 68.75% |
| Version-aware | 180 | 78.125% |
| Always-clarify | 310 | 81.25% |

横轴延迟越低越好，纵轴准确率越高越好，因此同时改善两者的方向为**左上方**。没有按项目中“右上总是更快更好”的非正式备注挪动数据。图中直接标注三点，不拟合或连线；纵轴采用 65–86% 的显示范围，并在图内和图注中说明。不同点形配合颜色，便于在灰度打印中区分。

Version-aware 相对 Single-pass 的给定准确率高 9.375 个百分点，延迟增加 60 ms；Always-clarify 相对 Version-aware 高 3.125 个百分点，延迟增加 130 ms。这些仅为输入值的算术差异，不能推出统计显著性、机制效应、泛化收益或唯一最优方法。没有重复运行、样本分母、测量口径、任务/硬件配置与不确定性估计，因此未画误差条，也未推算样本量。

图 2 尺寸为 90 × 76 mm，图 1 伴随矢量导出为 180 × 97.2 mm。没有指定期刊，尚未核对具体期刊的最新格式要求。

## 已做的实际验证

- 实际查看源图后重建；逐条核对六条连接方向。结构校验确认六个模块、六条原生边、两条标签和一个小位图。
- 使用 Inkscape 1.2.2 渲染图 1 SVG 为 PNG/PDF，打开查看。将两张实际 PDF 用 PyMuPDF 栅格化后再次查看。
- 使用 Matplotlib 3.10.8 输出图 2 PNG/SVG/PDF，并用 Inkscape 渲染 SVG 后查看。第一轮发现横轴标题与图下注释重叠，已调整下边距并重新检查，最终预览无该问题。
- 原始输入完整性检查为 4/4 通过；三行 CSV 与 SVG 中方法名、延迟及准确率文字逐项一致。
- 10 项数值审计均为 `match`：六个点值和四个差值。审计绑定数据账本哈希，仅验证数值转录，不认证测量质量。
- 图谱结构检查通过：revision 1，21 个节点、6 条关系；没有待处理语义导入或证据复核。14 个领域仍为 unsearched，本轮没有宣称完成文献查新。

日志与可回查记录：[artifact_verification.json](checks/artifact_verification.json)、[render_log.json](checks/render_log.json)、[numerical_audit.json](checks/numerical_audit.json)、[output_manifest.json](checks/output_manifest.json)、[atlas_check.json](checks/atlas_check.json)、[atlas_audit.json](checks/atlas_audit.json)。Inkscape 的 GtkRecentManager 警告原样记录，三次导出均返回 0，实际文件已打开验证。

实际查看过的最终预览位置：

1. `outputs/fig01_architecture.png`
2. `checks/fig01_architecture_pdf_render.png`
3. `outputs/fig02_latency_accuracy.png`
4. `checks/fig02_svg_render.png`
5. `checks/fig02_latency_accuracy_pdf_render.png`

## 复现与研究地图

从项目脚本依次运行：

```bash
python scripts/rebuild_architecture.py
python scripts/plot_latency_accuracy.py
python scripts/render_previews.py
python scripts/verify_artifacts.py
```

命令的绝对路径版本、文件编辑关系与覆盖规则见 [EDITING.md](EDITING.md)。四个脚本只使用已有本地工具，未包含安装/网络逻辑。

研究地图主文件为 [atlas.json](research-atlas/atlas.json)，当前 revision **1**；阅读入口为 [MAP.md](research-atlas/MAP.md) 与离线 [map.html](research-atlas/map.html)。主要节点关系：

| 记录 | 依赖与状态 |
|---|---|
| `figure-architecture` | 使用 `claim-reference-topology`；产物已生成，原生预览待验证 |
| `figure-latency-accuracy` | 使用 `claim-fixture-tradeoff`、`fixture-latency-accuracy`、`decision-axis-semantics`；本轮预览已检查 |
| `claim-reference-topology`、`claim-fixture-tradeoff` | 均保持 `draft`，未宣称真实实验支持 |
| `fixture-latency-accuracy` | 明确记录为给定合成夹具，未执行研究实验 |
| `decision-native-review-pending` | 保留 drawio 原生应用检查待办；与证据维护队列是否为空是不同事项 |

本轮没有新的文献候选、最近工作比较、科学 refuted/parked 假设或实验结论；这些不在制图任务范围内。已采纳的设计决定是按原始量纲作图，已修复的是数据图脚注布局，明确未完成的是 drawio 原生应用验证。

## 下一步

在已有离线 draw.io 应用中打开源文件，检查文字可编辑、模块可拖动、六条箭头方向及端点吸附、小图块显示，然后导出一份原生预览并更新 `VALIDATION.md` 和地图待办状态。若转为真实论文结果，应先提供可追溯的独立实验记录、样本分母、延迟口径和重复测量，再更新数据图与图注；本轮没有进行该研究实验。
