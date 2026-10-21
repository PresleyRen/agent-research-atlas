# 论文证据与主张映射

日期：2026-10-21。所有来源均为本项目本地文件，实际阅读全文；没有外部文献检索。数值来源版本由 `INPUT-MANIFEST.json` 及 `source-integrity.json` 的 SHA-256 标识。新稿版本由 `verification.json` 的文件哈希标识。

## 1. 来源登记

| 来源 ID | 路径及版本 | 实际读取位置 | 能证明什么 / 不能证明什么 |
|---|---|---|---|
| S0 | `PROJECT.md`，输入原件 | 全文两段 | 材料明确是合成离线技能记录及授权边界；不是真实研究执行证据 |
| S1 | `draft-zh.md`，输入原件 | 中文段落 1–2；英文两句 | 作者原始主张、共享状态描述和待润色句子；其中数值及泛化/因果不可直接采用 |
| S2 | `notes/method.md`，Method v0.1 | Input、Actions、Explicit version constraints、baseline、exploratory comparison 五段 | 文档中声明的方法与限制；不是代码级实现、标签隔离或运行溯源的验证 |
| S3 | `results/pilot.json`，输入原件 | 全部 JSON 字段 | 汇总虚构记录中的数量、准确率和未完成状态；不能提供逐例标签、家族分布、时间、显著性或机制 |
| S4 | `reviews.md`，输入原件 | R1.1–R3.1 与 Old response memo | 所有实际给出的合成评审问题及旧建议；旧建议不是依据充分的科研结论 |
| D1 | `records/calculations.json`，本次派生记录 | `/derived`，`/formulas` | 从 S3 复算的确定性算术；不是新实验、统计分析或原始观测 |

S3 SHA-256：`f253003352caed0ffbb5f05cd240f30e14bf231a37fa107941a31becf320ae32`。原件完整性核查见 `records/source-integrity.json`；没有因纠错而重写 S1 或 S3。

## 2. 句级证据表

表中“记录”表示输入叙述或合成 JSON 有该内容，不表示现实执行。引号中为新版正文精确片段；P 表示该节普通正文段落，从 1 开始，不把标题计入。

| Claim ID | 新稿精确措辞或片段 | 来源与 locator | 状态、支持范围及未决解释 | 位置 |
|---|---|---|---|---|
| C01 | “The question considered here is how a routing policy can coordinate these decisions within a single version-aware representation.” | S1 中文第 2 段；S2 显式过滤/条件澄清段 | 作者问题的概念重述；未完成最近工作/新颖性检索 | Introduction P1 |
| C02 | “We describe a rule-based policy that selects among answering, retrieving one additional passage, and asking one targeted clarification.” | S2 Actions 与 rule-based 声明 | 方法记录；不是 learned gate | Introduction P2；Methods §§2.2–2.3 |
| C03 | “The policy uses the initial message, supplied context, and document snippets with version metadata.” | S2 Input | 声明输入边界；无代码验证 | Introduction P2 |
| C04 | “The router and document filter share a version state.” | S1 中文第 2 段末句 | 原始设计说明；状态 schema 未给 | Introduction P2；Methods §2.3 |
| C05 | “The comparison baseline retrieves once and then answers without clarification.” | S2 baseline 段 | 记录中的对照；未给模型/提示/执行配置 | Introduction P2；Methods §2.4 |
| C06 | “The supplied synthetic record reports an exploratory comparison on 64 hand-authored cases spanning eight case families.” | S0 第 1 段；S3 `/design`、`/n_cases`、`/n_case_families`、`/datasets/0` | 合成记录描述；不保证家族独立 | Introduction P3；Methods §2.1 |
| C07 | “The version-aware policy was recorded as correct on 50 cases (78.125%), compared with 44 cases (68.75%) for the baseline, an absolute difference of 9.375 percentage points.” | S3 `/version_aware/correct`、`/version_aware/accuracy`、`/baseline/correct`、`/baseline/accuracy`；D1 `/derived` | 精确转录与计算；无检验、CI 或独立推断 | Introduction P3；Response R1.1 |
| C08 | “Within this record, the version-aware policy was associated with a higher success rate.” | S1 英文句 1；S3 两条件准确率 | 仅为给定记录中的描述性比较，保留关联强度 | Introduction P3；polished-sentences 使用版；Response R3.1 |
| C09 | “The comparison was planned after the synthetic cases had been inspected and was not preregistered.” | S2 exploratory comparison 段 | 来源明确陈述；不能事后改写为前瞻设计 | Introduction P4；Methods §2.1；Response R2.1 |
| C10 | “The available materials provide no uncertainty analysis, independent replication, causal mechanism study, or measured latency comparison.” | S2 最后两段；S3 `/uncertainty_analysis`、`/latency` | 截至本地输入所提供的证据；没有新补充实验 | Introduction P4 |
| C11 | “Hidden reference labels are reserved for the evaluator and are excluded from the specified policy inputs.” | S2 Input 第二句 | 设计要求；Methods §2.6 明确实际实现尚不可审计 | Methods §2.2 P1 |
| C12 | “Clarification is limited to cases in which a response from the user could change the answer; uncertainty alone is not the stated criterion for asking a question.” | S2 Explicit version constraints 段 | 对条件的逻辑解释；不添加训练、阈值或程序次序 | Methods §2.3 P1 |
| C13 | “The shared state thus serves two related design roles: maintaining consistency with explicit version requirements and supporting the decision to clarify an unresolved preference.” | S1 中文第 2 段；S2 显式过滤/条件澄清段 | 跨材料整合后的设计解释；无独立组件效应证据 | Methods §2.3 P2；Response R2.2 |
| C14 | “These details remain necessary for an executable reconstruction of the policy.” | 全部输入未包含 schema、完整规则、程序；本次项目清单 | 作者对缺失字段的复现判断；不声称已读不存在的实现 | Methods §2.3 P3 |
| C15 | “Both reported accuracies use the same stated denominator of 64 cases in the supplied pilot record.” | S3 `/n_cases` 和两条件 counts/rates | 分母声明可核算；缺少案例 ID，未独立检查逐例对齐 | Methods §2.4 P1 |
| C16 | “Latency was not measured, and the conditions were not compared under matched measured latency budgets.” | S2 baseline 段；S3 `/latency` | 原始限制，不能用调用次数代替时间 | Methods §2.4 P2 |
| C17 | “Comparisons with two larger models under equal latency budgets remain uncompleted; the artifact records a new-model comparison only as planned.” | S4 R2.1；S3 `/new_model_comparison`；S0 无模型运行授权 | requested but not executed；没有具体模型身份或额外成绩 | Methods §2.4 P2；Response R2.1 |
| C18 | “The reported outcome is accuracy, calculated as the number of cases recorded as correct divided by the stated total of 64.” | S3 counts/rates/n；D1 formulas | 由字段值及恰好相符的算术可确认；评分标准不可确认 | Methods §2.5 P1 |
| C19 | “Only aggregate counts and accuracies are available.” | 项目 discovery 与全量输入；S3 | 指可用于重新评分/统计的结果粒度；不表示没有文字方法说明 | Methods §2.5 P2 |
| C20 | “The 64 cases belong to eight recorded families and cannot be assumed to constitute 64 independent replications.” | S3 `/n_cases`、`/n_case_families`；S4 R1.2 | 依赖风险判断；家族间独立性同样未证实 | Methods §2.6 P1；Response R1.2 |
| C21 | “We therefore report no confidence interval, significance test, or causal effect estimate.” | S2 无不确定性/因果研究；S3 aggregate only | 本次写作决定；未使用错误独立性假设生成 CI | Methods §2.6 P1 |
| C22 | “The comparison also does not isolate clarification from filtering, additional information, or other differences between the policies.” | S2 两条件行为与不同预算限制；缺少消融/逐例记录 | 基于已知设计的替代解释，未声称任何替代解释已被证实 | Methods §2.6 P2 |
| C23 | “We list the failure categories in descending order.” | S1 英文句 2 | 仅语言编辑示例，原句正确；缺少类别和频次，所以排除正文经验主张 | polished-sentences-en，语言示例；Response R3.1 |

## 3. 撤回与保留的历史主张

| 历史 ID | 原文 | 当前判断 | 后续关系 |
|---|---|---|---|
| OLD01 | “准确率为 96%” | 被提供的结果 JSON 明确否定，撤回 | 新 C07 替代；原稿不删除 |
| OLD02 | “在三个真实业务数据集上验证…泛化” | 与 `/datasets` 及 PROJECT 的合成声明矛盾，撤回 | C06/C10 取代该范围描述 |
| OLD03 | “解决了所有文档 Agent 的意图理解问题” | 无支持，撤回；不是证明算法普遍无效 | 限定问题 C01 与范围 C06 保留 |
| OLD04 | “证明澄清必然提高推理能力” | 无因果/机制支持，撤回；不能宣称反向因果结论成立 | 描述性 C08 保留；C22 记录替代解释 |

## 4. 引用和独立性检查的实际范围

没有提供外部书目，未联网验证最近工作；不存在可宣称已独立核验的论文引文。上述表逐句匹配输入材料，并且明确区分来源声明、可复算数值和本次解释。初次审查为串行自审；协调者随后另行读过两节英文稿及完整回复并对照输入，报告未发现新增实测或漏答原意见。团队共享任务背景和材料，这一编辑复读不构成独立证据来源、独立科学复验或盲审。`audit.py values` 只核查指定 JSON 数值的转录，不核查科学真实性、独立性或方法有效性。
