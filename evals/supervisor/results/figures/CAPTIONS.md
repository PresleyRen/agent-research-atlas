# 可用图注

以下文字对应本地已生成的图稿。实际投稿时，合成数据标记必须保留，除非以具有完整测量记录的真实数据重新绘图并重新审核。

## 图 1 / Figure 1

**中文：** 参考架构的可编辑重建。用户请求依次经过版本状态（Version state）与路由器（Router）；检索分支经 Retriever 输出 Answer，澄清分支经 Clarify 返回用户请求入口，形成反馈回路。模块与箭头保留所提供参考图的连接关系；右下角彩色方阵为原图局部视觉细节，不表示本研究的新测量结果。为避免遮挡，澄清反馈说明文字移至模块下方。

**English:** Editable reconstruction of the supplied architecture. A user request passes through Version state to Router. The retrieval branch proceeds through Retriever to Answer, while the clarification branch passes through Clarify and returns to the user-request entry point. Modules and arrows preserve the reference topology. The colored panel at the lower right reproduces a visual detail from the source image and does not represent a new measurement. The clarification-feedback label is moved below the module to avoid overlap.

**来源：** `reference.png` 全图；`PROJECT.md` 架构说明。对应 `outputs/fig01_architecture.*`；地图节点 `claim-reference-topology`、`figure-architecture`。该图表达可见拓扑，不支持性能或因果结论。

## 图 2 / Figure 2

**中文：** 三种方法的延迟—准确率关系（合成数据）。各点直接对应给定 CSV 中的一行：Single-pass 为 120 ms、68.75%，Version-aware 为 180 ms、78.125%，Always-clarify 为 310 ms、81.25%。横轴延迟越低越好，纵轴准确率越高越好，因此同时改善两项指标的方向为左上方。纵轴显示范围为 65–86%。由于未提供重复运行、样本分母或不确定性估计，图中未绘制误差条；这些点仅用于说明给定数值的权衡，不构成统计显著性或真实实验有效性的证据。

**English:** Latency–accuracy trade-off for three methods using synthetic fixtures. Each point directly represents one supplied CSV row: Single-pass, 120 ms and 68.75%; Version-aware, 180 ms and 78.125%; and Always-clarify, 310 ms and 81.25%. Lower latency and higher accuracy are desirable, so simultaneous improvement is toward the upper left. The accuracy axis spans 65–86%. No repeated runs, sample denominators, or uncertainty estimates were supplied; error bars are therefore omitted. The points describe the supplied values and do not establish statistical significance or empirical effectiveness.

**来源：** `results/latency-accuracy.csv` 表头及第 2–4 行；`notes/figure-context.md` 第 3 行。对应 `outputs/fig02_latency_accuracy.*`；地图节点 `fixture-latency-accuracy`、`claim-fixture-tradeoff`、`figure-latency-accuracy`。
