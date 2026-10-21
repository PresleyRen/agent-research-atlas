# 路由、模型选择与策略选择 / Routing, model selection, and strategy selection — Research notes

2026-10-21 · partial；只有合成项目材料与研究设计，没有有效路由性能实证。

## 已读比较及其后果

`../../../notes/comparison.md` L4–8 报告 62/64 与 51/64，但基线读取事后 `reference_intent`，路由器没有；8 家族改写又跨非正式分割。原数字保留，不能判定方法胜负、统计显著或据此整体弃题。当前未取得代码/逐例输出，未执行复算。

## 候选与状态

方向 A（`hyp-learned-gate`）训练暂缓；方向 B 的评测设计优先；方向 C（`hyp-retrieve-all-lowconfidence`）作为一般主线暂停，但一次额外检索 B2 仍是必要基线。简单规则 B4 只依公开版本、可见证据与任务要求，不能读 evaluator 的切片标签。完整 intent oracle 单列诊断，不参加部署排名。

未入选不表示 refuted。学习门控重启需同信息协议、独立家族上的规则残余失败、数据和运行资源落实。旧模板的固定新模型/15 模型/9% 上限没有本项目依据，决定不采用。

## 下一步

逐段追踪输入投影→路由依赖→环境返回→metric 调用；先排掉隐藏标签和预算差异。selective prediction、value of information 尚未真实检索。[选题设计](../../../RESEARCH-DESIGN.md) · [查新计划](../../../design/bilingual-retrieval-plan.md)
