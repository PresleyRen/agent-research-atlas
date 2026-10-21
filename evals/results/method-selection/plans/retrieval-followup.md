# 双语近邻与反证续接表

2026-10-20。**计划未执行；本轮不联网。** 当前仅有五份本地教学材料，没有核验任何真实论文的身份、摘要或全文。下列查询是研究意图，`submitted_query=null`、返回量未知；不能记成空结果或查新饱和。

## 实际覆盖收据

| 来源 → 请求 | 是否实际调用/阅读 | 状态与边界 |
|---|---|---|
| 项目文件清单 → 既有地图与研究材料 | 是；`rg --files`与`atlas.py discover`，随后读五个原文件全文 | 首次发现检查5文件，`truncated=false`，没有既有地图。 |
| 本地综述/开发/资源/共享工作流 → 分类、失败线索、约束与方法冲突 | 是；全文，来源定位见[原始材料清单](../reviews/2026-10-20/source-ledger.json) | 已完成有限本地阅读；全部synthetic，不能支持经验机制。 |
| 英文近邻/反证 → 原始论文和评测 | 否 | `not_run`；本轮禁止联网，不是0命中。 |
| 中文近邻/反证 → 原始论文和评测 | 否 | `not_run`；CNKI/万方等账号、权限也未核实。 |
| DOI/发表身份/前后向引用核验 | 否 | `not_run`；没有真实论文种子或身份记录。 |

## 最值得先查的检索单元

| ID/候选 | 中文意图查询 | English intent query | 反证/相邻领域重点 | 当前状态 |
|---|---|---|---|---|
| Q1 / C1 | 文档版本 意图歧义 问还是检索 路由 信息缺失 | versioned documents ambiguous user intent ask or retrieve routing missing information | conversational search、selective prediction、value of information；简单版本过滤是否已足够 | `not_run` |
| Q2 / C1 | 时间检索 版本适用性 目标日期 澄清 预算匹配 消融 | temporal retrieval target version clarification budget matched ablation | 决策时可用信息、语料更新与元数据故障、oracle标签泄漏 | `not_run` |
| Q3 / C2 | 澄清问题 答案不变 歧义 条件式回答 用户负担 | clarification question answer invariance ambiguity conditional answers user burden | answer-set equivalence、decision relevant uncertainty；不提问也能满足任务的反例 | `not_run` |
| Q4 / C3 | 自适应检索 停止条件 重复证据 无提升 查询改写 | adaptive retrieval stopping repeated evidence no improvement query reformulation | optimal stopping、information gain；停滞后可恢复、证据不在库、去重强基线 | `not_run` |
| Q5 / 全部 | 版本问答 澄清 评测 标签 分组泄漏 复现 数据集 | versioned question answering clarification evaluation labels grouped leakage replication benchmark | 能否构造独立家族、真值从哪里来、数据权利、真实成本 | `not_run` |

外部检索只在未来授权允许时开展。优先原始会议/期刊/作者记录与合法全文；英文可考虑ACL Anthology/OpenReview/arXiv，中文可考虑中文期刊原文与合法机构库。这里列的是候选入口，本轮没有访问，也不声称账号可用。

首次续接只扩展最可能改变C1的近邻、简单替代及反证；按真实服务适配语法，并保存最终提交的字符串、日期、时间窗、provider、访问深度、分页截断和失败类型。当前计划以2026-10-20为记录日期；未来查新应写实际截止日，保留基础工作回溯，不能只按新年份筛选。

## 候选身份与提取收据

| 候选 | 可读本地证据 | 真实最近论文身份 | 机制/方法差异提取 | 当前决定 |
|---|---|---|---|---|
| C1 | S02、S03为线索，S04限定资源 | 未覆盖 | 未覆盖 | 先做可识别性诊断设计；新颖性未解决。 |
| C2 | S02提到澄清负担；答案不变是本轮提出的边界假设 | 未覆盖 | 未覆盖 | 保留候选，不能称已有支持。 |
| C3 | S03只有重复旧片段的描述 | 未覆盖 | 未覆盖 | 暂存，先补轨迹。 |

每篇后续近邻应对齐：问题/任务、信息可见性、干预机制、评价器与真值、语料版本、预算、成本、对方已经做什么、精确差异和未知。尤其检查当前拟议差异是否只是旧方法的别名。若真实工作已完整回答，缩窄或停止相应候选；不能因为不利于候选就排除。
