# 文档摄入、索引与检索 / Document ingestion, indexing, and retrieval — Research notes

2026-10-21 · partial；仅当前合成材料的范围。

## 保留人工提醒

**旧版任务里的旧文档不一定错误。保留这条提醒。** 原出处：`../../../research-map.md` L6，节点 `claim-old-document-valid`。不能以“最新版本”替代任务所需版本。

## 观点、反例与方案

虚构研究 B §1 提供确定性版本过滤这一强简单替代；§2 说明真正未指定版本才可能需要用户信息。虚构综述 A §2 说额外检索有时补证据，未测普遍收益。当前将初始证据足够、缺失但语料可得、语料不可得、冲突分开，不给全部低置信度一律检索。

`hyp-explicit-version-rule` 为 proposed。输入必须来自消息、公开时间和适用范围；“去年”时间锚点未知时返回 unknown，不能从金标补齐。规则过滤后仍错，分别定位解析、召回/筛选和生成利用，不直接归因路由器弱。

## 下一步

取得真实文档快照、版本有效期与目标约束；构建明确旧/新版本、未知参考日期、旧文档正确的负对照，运行计划 E2。检查共享文档使家族是否真正独立。[评测设计](../../../design/benchmark-dossier.md) · [标注规范](../../../design/annotation-and-data-contract.md) · [未来查新 Q06](../../../design/bilingual-retrieval-plan.md)
