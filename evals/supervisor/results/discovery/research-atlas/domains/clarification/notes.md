# 多意图、歧义与澄清 / Multiple intents, ambiguity, and clarification — Research notes

2026-10-21 · partial；本地虚构观点已读，真实论文与用户研究未执行。

## 文献观点与适用边界

虚构研究 B §2（`../../../papers/local-counterexample.md` L5）说真正未指定版本时，澄清可能改变答案；§3 未测生产频率和容忍度。由此只能生成条件性假设，不能断言所有歧义都要追问。虚构综述 A §2 区分文档缺证据与未表明偏好，前提是偏好不在可访问记录中。

## 方案与旧决定

`hyp-information-source-value` 为 proposed，先测有效目标信息与无关/空回复对照，排除额外推理/文本长度解释。理想诚实回复轨道只测信息上界；策略问法、用户不知道/拒绝及费用另测。允许合格条件回答与合理弃答，保持多个可接受动作。

旧地图 `hyp-ask-all-lowconfidence` 继续 parked：成本不可控且未证明信息价值；本轮没有新实证使其重启。重启需要实际可获得回复、价值与成本对照，不能因为选定评测路线就恢复“全部追问”。

## 下一步

先检验 `answer_sensitive`、`robust_complete_answer_exists` 与用户可答性的标签能否可靠裁决。随后 E1 的同信息配对比较才可运行。[完整评测](../../../design/benchmark-dossier.md) · [分析计划](../../../design/analysis-and-execution.md) · [未来查新 Q02/Q03/Q08/Q09](../../../design/bilingual-retrieval-plan.md)
