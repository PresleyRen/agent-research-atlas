# 中英检索与反证计划 / Bilingual retrieval plan

日期：2026-10-21。**状态：所有远端查询均为 `not_run`，原因是本轮明确禁止联网。没有零命中、饱和或新颖性结论。** 本地阅读收据在 `evidence-synthesis.md`。本文件只规划以后获准或获得合法本地真实论文时的工作。

## 问题边界与筛选

问题：决策前可见信息固定时，文档 QA 中如何判断澄清、追加检索、版本过滤和条件回答的任务收益与成本？纳入 dialog clarification、answer-sensitive ambiguity、preference elicitation、selective prediction、value of information、versioned/temporal retrieval 与评测有效性；排除仅按固定意图分类、没有动作或信息边界的纯分类排名，保留其作为背景的理由。发现机制重复或方法无提升的文献仍属相关，不能删作“无关”。

时间范围：基础机制不限起始年，近期竞争工作优先 2023–2026-10-21；未来实际执行时更新截止日期并保留旧计划。中文、英文分别执行，不把中文缺席误作不存在。每篇记首发/版本日期、预印本或正式发表状态、实际读到的页/节，不能凭索引或摘要声称全文已核验。

## 查询单元

| ID / 目的 | 中文 intent_query | English intent_query | 什么结果会改变选择 |
|---|---|---|---|
| Q01 定位综述 | 文档问答 澄清问题 歧义 信息需求 综述 | document question answering clarification ambiguity information need survey | 是否已有成熟构念与 taxonomy |
| Q02 最近评测 | 答案敏感 歧义 澄清 评测 数据集 反事实 | answer-sensitive ambiguity clarification benchmark counterfactual questions | 现有评测是否已隔离同样信息与动作 |
| Q03 动作价值 | 澄清 价值 信息价值 决策理论 用户成本 | clarification value of information decision theory interaction cost | 本问题是否仅为已知 VOI 的重命名 |
| Q04 相邻方法 | 选择性预测 弃答 成本敏感 主动信息获取 | selective prediction abstention cost-sensitive active information acquisition | 应比较的强基线与校准目标 |
| Q05 偏好缺口 | 偏好获取 缺失用户偏好 可辨识性 澄清 | preference elicitation unobserved user preference identifiability clarification | 什么先验/历史信息使纯检索也可识别目标 |
| Q06 版本规则 | 版本化检索 时间问答 旧版本 任务约束 确定性过滤 | versioned retrieval temporal question answering explicit version constraint deterministic filter | 简单版本规则和既有系统能否充分覆盖 |
| Q07 公平比较 | 路由 评测 意图标签 泄漏 决策前信息 | routing evaluation intent label leakage information available at decision time | 哪些已有工作已修复 oracle 比较 |
| Q08 反证/无提升 | 澄清问题 无提升 额外推理 无关回复 条件回答 | clarification no improvement extra reasoning irrelevant response conditional answer | 追问收益是否只来自计算或评分偏差 |
| Q09 用户成本 | 澄清 用户负担 不知道 拒绝回答 文档助手 | clarification user burden nonresponse refusal document assistant | 理想回复上界是否缺乏生产价值 |
| Q10 数据依赖 | 改写 家族划分 模板污染 基准泄漏 | paraphrase family split template leakage benchmark contamination | 有无可复用的分割/污染检测协议 |
| Q11 纠正与状态 | 意图修正 版本化目标 状态撤销 对话约束 | intent revision versioned goals state invalidation dialogue constraints | 后续多轮方向是否已有更简单方案 |

## 来源适配与记录格式

先以作者/会议/期刊/机构原始记录核验身份和关键机制。英文候选入口可包括 ACL Anthology、OpenReview、arXiv、DBLP、OpenAlex/Semantic Scholar；中文可包括中文期刊原站、机构库、CNKI/万方（仅现有合法访问）。这些名称仅为未来候选入口，当前均未访问，也没有假设账户/订阅可用。

对语义相关性接口以自然语言分别提交中英短语；不要把整条通用 Boolean 表达式照搬。对原生支持布尔/字段/日期的数据库先核对当时官方语法，再记录最终 `submitted_query`、接口版本、filters、分页与截断。用搜索引擎发现某数据库内容，应标 `web discovery`，不能伪装数据库内部检索。

一条实际执行记录至少包含：query_id、language、provider、operation、intent_query、submitted_query、executed_at、time_scope、status、returned_count（未知写 null）、screened_count、kept_ids、excluded_ids/reasons、cursor/truncated、raw_output_path、access_failures、read_depth。`not_run`、blocked、failed、success_empty、success_with_hits、partial 必须分开。计划中的日期不能填作实际检索时间。

## 有限预算与停止

第一轮只做 Q01–Q10 的中英定位，Q11 作为 parked 扩展；每个单元先筛一页可复核结果，记录页面大小与排序，优先深读可能完全重叠或反驳的工作，再对最接近的原始论文做一轮回溯/前向引用。这个限制是搜索工作量上限，不是论文数量要求或查全保证。提供者不可访问就记 blocked，改用获准本地或公开原始来源；不绕过授权。

停止条件：已获得足以改变“新 benchmark / 复用诊断 / 停止”的最近工作比较，或本轮访问/阅读预算用尽。薄弱分支只有在排除术语、访问和边界问题后才考虑是否为证据空白。每轮结尾保留新增工作是否改变判断；无真实检索不写“未发现先前工作”。

## 最近工作深读比较字段

每篇必须回答：测量什么构念；动作时可见信息；允许动作/轮数；数据与许可证；标签来源；独立单位与切分；强基线；主指标/分母；成本范围；负结果与用户不可回复条件；是否允许条件回答；本项目剩余差异。若已覆盖，优先复用其数据/协议并精确缩小贡献；若全文无法取得，则将关键差异标 unknown，不以摘要缺失证明其没做。

预期落盘位置为 Atlas 的 `explorations` 和 `papers` 节点，逐条注明真实来源与定位；不能用当前两个虚构 paper 充当查询结果。当前领域覆盖保持 partial/unsearched。
