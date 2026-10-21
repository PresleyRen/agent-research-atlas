# 图稿设计说明

日期：2026-10-21。范围：用户授权项目内的原图重建和三行合成数据绘图。未联网、安装依赖、调用模型推理、购买服务或对外发布。所有输入保留原文件；该任务不涉及文献查新或方法优越性验证。

## 图 1：架构图可编辑重建

**读者问题：** 请求如何经过版本状态与路由，以及澄清如何返回请求入口？图示仅表达 `reference.png` 的可见结构，不能作为机制有效性的实验凭据。

**来源与版本：** `reference.png`，1000 × 540 px；原文件 SHA-256 为 `03eba4db7c14e85b31d9b5ae0bd963e07abf35d81552e165bf1cc53ec75b7055`。同时核对 `PROJECT.md` 第 5 行描述。用户提供的项目材料标注为 synthetic fixture；未核验外部图片权属或原论文出处。

**实际观察的元素：** User request、Version state、Router、Retriever、Answer、Clarify 六个圆角模块；六条箭头；clarification feedback 与 source detail 两条说明文字；右下角彩色小方阵。没有成功徽章或可提取的热图数值。

**结构清单：**

| 连线 ID | 起点 | 终点 | 方向与走向 |
|---|---|---|---|
| e_request_state | User request | Version state | 从左向右 |
| e_state_router | Version state | Router | 从左向右 |
| e_router_retriever | Router | Retriever | 自上向下 |
| e_retriever_answer | Retriever | Answer | 自上向下 |
| e_router_clarify | Router | Clarify | 从 Router 左侧折向下，再向左进入 Clarify |
| e_clarify_request | Clarify | User request | 从 Clarify 左侧向左，再向上进入 User request |

**重建策略：** 同一 `sources/architecture_scene.json` 生成原生 `.drawio` 与伴随 SVG。模块、标签和连线分别位于可编辑图层；右下角仅裁剪原图 `[825,345,926,446)` 的 101 × 101 px 小块，保存在 `assets/source_detail.png` 并独立嵌入。没有把整页图片封装为 drawio。

**版式调整：** 原图 feedback 文字与 Clarify 左下边缘接近/重叠，重建时移到该模块下方。保留原文、模块顺序、所有连线及方向；未改变拓扑，没有另行加入科学重设计。字体采用本地 DejaVu Sans。画布保持原图 1000:540 比例，伴随 SVG/PDF 宽度为 180 mm，高度为 97.2 mm，适合宽栏查看；不宣称匹配某个未给定期刊的格式。

**检查边界：** 已实际查看参考图、Inkscape 渲染的 SVG 预览和 PDF 的实际栅格预览。`.drawio` 已做 XML、原生对象和有向端点检查；当前无 draw.io 原生应用/导出器，未宣称完成原生渲染及拖动连线交互检查。

## 图 2：延迟—准确率散点图

**读者问题：** 给定三种方法各处于什么延迟和准确率位置？依据仅为 `results/latency-accuracy.csv` 的三行合成夹具。

| CSV 行 | 方法 | 延迟（ms，越低越好） | accuracy 原值 | 图中准确率（%，越高越好） |
|---|---|---:|---:|---:|
| 2 | Single-pass | 120 | 0.6875 | 68.75 |
| 3 | Version-aware | 180 | 0.78125 | 78.125 |
| 4 | Always-clarify | 310 | 0.8125 | 81.25 |

原 CSV SHA-256：`ed5f2384042cb46ec7c3989ddc2a5faa0ea1e2bd38fc3a0a210d3e0f4b446cef`。直接读取每行，纵轴唯一变换为 accuracy × 100；不重算均值，不假定样本量，不从小数位数推断分母，不做平滑或插值。没有重复运行、原始样本、误差估计、任务设置、硬件或延迟统计口径，因此不添加误差条或显著性标记。

**编码与量纲：** 横轴为线性延迟 0–350 ms；纵轴为线性准确率 65–86%，非零起点在图内和图注中明示。散点的受限纵轴用于区分数值，不表达柱长比率。低延迟高准确率对应左上方，右移意味着更慢，不能为了偏好方法而移动数据或把右上角称为总体最优。各方法用不同点形和颜色，并直接标注名称、延迟和准确率；不连接点以暗示连续关系。

**格式：** 90 × 76 mm；SVG 保留文字对象，PDF 嵌入 TrueType 字体，PNG 为 300 dpi；代码为 `scripts/plot_latency_accuracy.py`。这是可复用的论文图形格式，合成数据本身不构成真实实验结果。

**已观察到的结果：** 在这三行数据中，Version-aware 相对 Single-pass 的准确率高 9.375 个百分点且延迟高 60 ms；Always-clarify 相对 Version-aware 的准确率高 3.125 个百分点且延迟高 130 ms。差值仅为算术描述，不能据此推出显著性、因果机制、泛化收益或唯一最优方案。

## 研究地图连接

`research-atlas/atlas.json` 为项目记录；`research-atlas/MAP.md` 与 `research-atlas/map.html` 为可读视图。图 1 → `claim-reference-topology`；图 2 → `claim-fixture-tradeoff` → `fixture-latency-accuracy`。交付记录为 `figure-architecture` 与 `figure-latency-accuracy`。所有科研断言保持 draft；14 个领域保留 unsearched，不把制图完成当成文献综述或科学支持。

本说明采用 agent-research-atlas C28 图稿工作台的字段结构，已改写为本项目的实际观察与约束。工作台归属、上游作者与 CC BY-NC-SA 4.0 见已安装技能的 `LICENSE.supervisor.md`；项目输入的外部许可未另行核实。
