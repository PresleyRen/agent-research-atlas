# 意图理解与目标表示 / Intent understanding and goal representation — Research notes

2026-10-21 · partial，只完成本地合成材料的阅读和问题操作化。真实文献未检索。

## 文献观点与本项目判断

虚构综述 A §1（`../../../papers/local-review.md` L4）只指出给定例子没描述用户修正，不能据此断言整个领域没有意图修正研究。旧地图 L4 指出低置信度可能来自不同信息来源。当前将意图区分为“决策前相容意图集合”和“评估者事后知道的真实意图”，禁止用后者作为可部署路由输入。

答案敏感性不等于追问必要性：不同意图可能有不同答案，但一个完整条件式回答仍可能满足请求。rubric 分开记录相容意图、答案敏感性和无追问完整回答是否存在。[数据契约](../../../design/annotation-and-data-contract.md)

## 方案与问题

主节点：`problem-uncertainty-source`、`problem-information-action-value`、`hyp-information-source-value`。当前方案先用同一 O0 的反事实世界检查可识别信息；人工明确的标签只供 evaluator，不供 gate。多轮改口和版本化目标保留后续扩展，未伪造执行轨迹。

## 下一步

取得原案例后分两阶段标注：先只读 O0 列相容意图，再看完整材料标答案/证据。对选择性预测、偏好获取、对话状态跟踪和 intent revision 做未来中英查新。参见 [检索计划 Q04/Q05/Q11](../../../design/bilingual-retrieval-plan.md)。
