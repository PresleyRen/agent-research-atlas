# 中英文检索计划与 provider 修订

更新：2026-10-20。**所有远端请求均未发送。** 本文及 `requests.json` 是冷计划，不是检索结果。`searched_at`、`submitted_query`、真实请求回执和命中数都没有被虚构。

## 1. 范围、日期与筛选

目标是查找意图修正、约束更新、撤销信号到执行边界的相关工作，同时检索失败、反例、简单基线和评测批评。语言为中文、英文。规划的证据截止日为 2026-10-20；未来执行时重新记录实际检索日和论文版本。

基础机制不限起始年份；“2024 年以来”仅作为独立的近期补查窗口，不作为所有请求的全局过滤器。需要回溯对话状态跟踪、信念修正、真值维护、计划修复、运行时验证、取消传播与并发控制等旧术语。

纳入依据是问题、决策时可用信息、机制或评测条件至少有直接关联；结论支持或反对候选都纳入。仅共享一个宽泛关键词、没有相关决策或约束机制的材料排除并记理由。`local-irrelevant` 属于后一种；`local-counter` 不属于后一种。[来源：`EVIDENCE-LEDGER.md` 的材料清单。]

## 2. 双语术语与消歧

| 中文表达 | 英文检索起点 | 同义词 / 相邻词与消歧 |
|---|---|---|
| 时变意图、用户改口 | dynamic user intent; intent revision | changing goals; goal revision; conversational correction；不只用 intent classification。 |
| 约束更新、有效时间 | constraint updates; temporal validity | valid time; versioned state; temporal consistency；区分收到消息和正式生效。 |
| 撤销目标、取消任务 | goal revocation; task cancellation | intent cancellation; interruptibility; plan invalidation；取消后再授权需单查。 |
| 授权撤回、过期授权 | authorization revocation; stale authorization | capability revocation; execution-time authorization；只保留与 Agent 决策/工具执行接口相关的机制。 |
| 记忆更新、旧状态 | memory updating; stale state | belief revision; truth maintenance; forgetting；训练期机器遗忘作为相邻线索，不冒充运行时撤销。 |
| 澄清噪声、标签歧义 | noisy clarification; label ambiguity | ambiguous correction; inconsistent feedback; dialogue state tracking。 |
| 动作提交、取消传播 | action commitment; cancellation propagation | execution monitoring; runtime verification; check-then-act race；区分可阻止与已发生副作用。 |
| 固定预算、强规则基线 | fixed action budget; rule-based baseline | compute-matched comparison; selective prediction; abstention；追加调用和等待都计成本。 |

## 3. 检索矩阵

这些是普通文本候选串。provider 支持什么语法，未来执行前需按实际接口确认；不把全表拼接成一条过窄的 AND 查询。中英文分别记录，不能以一方代替另一方完成。

| 单元 ID / 目的 | 中文候选查询 | English candidate query | 要留下什么 |
|---|---|---|---|
| Q01 综述与找词 | 智能体 时变意图 约束更新 综述 | language agent dynamic user intent constraint updates survey | 综述范围、截止日、原术语与基础原始工作。 |
| Q02 最相近问题 | 对话状态 用户改口 目标修正 任务约束 | dialogue state user corrections goal revision task constraints | 同问题的其他命名；各阶段能看到的信息。 |
| Q03 撤销与工具执行 | 智能体 工具调用 任务取消 授权撤销 | language agent tool use task cancellation authorization revocation | 撤销对象、作用范围、动作状态和可阻止边界。 |
| Q04 反例与复现 | 意图更新 澄清噪声 路由失效 复现 | intent revision noisy clarification routing failure replication | 原机制适用边界、负结果、失效条件；不使用 NOT failure。 |
| Q05 简单基线与替代解释 | 约束更新 规则取消 基线 固定预算 | constraint updates rule-based cancellation baseline fixed budget | 规则、最新状态、拒绝/等待是否已解释效果。 |
| Q06 相邻基础机制 | 信念修正 真值维护 目标变更 计划修复 | belief revision truth maintenance goal changes plan repair | 老方法与新术语的结构对应；不限年份。 |
| Q07 时序与竞态 | 取消传播 执行监控 动作提交 竞态 | cancellation propagation execution monitoring action commitment race | 复核与提交之间的假设、不可逆边界、延迟与并发。 |
| Q08 评测与可复现性 | 智能体 撤销 约束满足 过程评测 数据集 | agent cancellation constraint satisfaction trajectory evaluation dataset | 数据许可、标签定义、任务级依赖、评价器和代码访问深度。 |

初次获准实际检索时，建议优先 Q01、Q02、Q04、Q06 的中英两路，然后按命中术语推进 Q03、Q05、Q07、Q08。每条查询先筛最多 20 条、至多 2 页；这是待采用的工作预算，不是结果上限即完整覆盖。可对至多两篇已核验近邻各做一次参考文献与被引扩展，每个方向最多筛 10 条。限流、空集、无权、语法失败分别停止并记账，不盲重试。

## 4. 原三条请求的修正

| 原请求 | 发现的问题 | 当前计划中的修正 |
|---|---|---|
| S2 relevance：`agent AND routing NOT failure` | 本地技能规定 relevance 使用普通文本；通用 Boolean 不可直接套用。排除 failure 还会损失反证。 | 把上表普通文本分阶段发送；保留明确的失败/噪声/复现查询；bulk 是另一接口，未核验其语法，不当作替代接口已接好。 |
| S2 recommendations：`positivePaperIds:[local-support]`、`negativePaperIds:[local-counter]` | 把相关反例当无关负种子；所有 local-* 又都是合成内部 ID，不能视为真实 S2 ID。 | 只保存相关种子角色示例：support 与 counter 都属于正相关方向；irrelevant 才是无关示例。真正请求体留空、`sendable:false`；取得真实且核验的论文 ID 后才能生成。 |
| Elicit keyword：`query:agent routing` + `filters.year_min:2024` | 本地协议说明 keyword 与 corpus 原生语法相关，不能混 filters；过早设置近年下界漏基础工作。 | 默认改为 semantic 自然语言问题；本轮不设 provider 日期参数，年份要求放在本地筛选计划，基础回溯不限年份。若未来选 keyword，必须另核验 corpus 原生语法并去掉 filters，不能假设 MCP 与 REST 字段相同。 |

接口规则的依据是本地 `references/bilingual-retrieval.md`“按来源适配查询”和 `SRC-S2-F01/F02`、`SRC-ELICIT-F01` 快照；本轮没有访问现网文档，也没有验证当前 endpoint、配额或账号能力。保存的版本说明与能力定位见 `CAPABILITY-GAPS.md`。

Elicit semantic 的双语问题草案：

- 中文：哪些研究检验了用户修正目标或撤销任务后，智能体如何更新约束并停止待执行工具动作？请同时找简单规则基线、澄清带噪声时的失败和无改进结果。
- English: Which studies test how agents update constraints and stop pending tool actions after users revise goals or cancel tasks? Include simple rule-based baselines, failures with noisy clarification, and no-improvement results.

## 5. 工具接续顺序与回执

本轮直接读三份本地材料即可完成账本；没有调用 PaperQA2。将来 PaperQA2 即便可用，其本地 `SearchPapers` 也只覆盖明确导入的 corpus，不代表全球查新，且包可安装不代表模型调用免费。[本地依据：`references/bilingual-retrieval.md`“可选工具”与 `SRC-PAPERQA-F01/F03`。]

若下一轮获得实际公开检索授权，先使用当时可用的公开检索与原始论文页；S2、OpenAlex 等接口按实际权限与版本再启用。中文期刊、机构库、ChinaXiv 等公开入口可补语言覆盖；CNKI/万方库内查询若没有已授权访问就保留未覆盖，不能把搜索引擎发现写作已搜数据库。

每次真实请求至少保存：请求 ID、provider、endpoint/version、operation/mode、语言、研究意图、实际提交串与参数、日期/起止时间、scope、授权和成本边界、分页/截断、warnings/effective settings、原始回执路径、候选与保留 ID、实际阅读深度和来源定位。使用 `planned / succeeded / empty / blocked / rate_limited / failed`；必要时另标部分结果。未执行时 `submitted_query` 和结果数为 `null`，不以空数组表示“查无论文”。

两张覆盖收据分别记录：来源→请求→是否调用→真实状态；候选 ID→身份核实→读取范围→提取/排除/未覆盖。真实近邻仍为空，支持与反驳的外部检索均未完成。达到约定预算可以结束该轮，但只有真实增量记录才能支持“在本范围内趋于饱和”的描述。
