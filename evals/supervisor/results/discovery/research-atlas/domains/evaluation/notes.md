# 评测、实验设计与科学有效性 / Evaluation, experimental design, and scientific validity — Research notes

2026-10-21 · partial；完整设计已写，数据与实验未完成，真实最近评测未核验。

## 当前选择

优先方向 B 的测量设计。主要对象是动作的信息增益与最终任务损失，而不是唯一 gold route。统一 agent-visible allowlist，隐藏意图/切片/family 标签留在评估端。正确性、版本约束、证据支持、出处和完成分项可审查，允许合格条件回答；成本未知时报告向量，不假造净收益。

## 来源与关键效度威胁

调试笔记 `../../../notes/comparison.md` L6/L8 记载事后信息泄漏和家族交叉，触发 `decision-repair-comparison`。资源笔记 `../../../notes/resources.md` L3 声称 64 改写，但当前物理输入无样本/文档/标签。故 H1/H2 不升级 testable，不把设计 artifact 当 run evidence。

主单位为家族/谱系连通组，改写与种子嵌套。若旧 8 家族取得，4/4 也只能 exploratory；新独立家族才能做确认性研究。现阶段不以 64 条估计窄独立置信区间，不声称已标注或已完成 split。

## 可执行设计入口

- [完整评测 dossier](../../../design/benchmark-dossier.md)：缺口、构建、有效性、诊断和发布。
- [标注与信息契约](../../../design/annotation-and-data-contract.md)：双人分阶段标注、集合答案、争议与失败。
- [分析/预算/停止计划](../../../design/analysis-and-execution.md)：E0–E4、族级配对、主对比、δ 未定、成本与冻结要求。
- [机器可读设计](../../../design/protocol.json)：execution_ready=false、无虚假 command/freeze/runs。

## 下一步

先解决 E0：取得原始案例与谱系并检验构念可判性。随后才实现评价器和强简单基线，做信息接口核验；新模型不是 benchmark 必需品。真实外部查新需之后授权，当前保留中英 not_run 计划。
