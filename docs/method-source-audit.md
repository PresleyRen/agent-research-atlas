# 科研方法来源与互补覆盖审计

Reviewed: **2026-10-20**。这是对指定方法技能的来源审计和采用决策，不是上游项目排行榜，也不是科研发现或论文录用效果评测。

**结论：先前的总流程覆盖了研究链条，但没有充分展开每个上游的特有做法。** 本轮补齐九模块问题选择、按卡点选发散策略、检索与阅读的双重覆盖收据、问题锚点与可实现方法卡、实验到评价器的忠实度审查、逐出现位置的数字与引用审计，以及功效计算的适用边界。部分能力由本地程序承载，更多是宿主必须实际执行的研究协议；外部检索、通用统计引擎和完整远端编排仍有明确缺口。有问题的默认规则被拒绝，没有为了声称“全部纳入”而照单复制。

逐特征机器清单见 [method-source-manifest.json](method-source-manifest.json)，工具和自主系统另见 [tool-source-audit.md](tool-source-audit.md)。两份来源清单共同映射到 [capability-registry.json](../skills/agent-research-atlas/assets/capability-registry.json) 的 `C01`–`C24`，但重叠快照不构成独立的科学证据。

## 1. 审查范围、版本与判定词

本轮共同逐文件读完 **26 个指定 `SKILL.md` 正文**：ResearchStudio 3 个、ARIS 14 个、K-Dense 6 个、Orchestra 2 个、Anthropic 1 个；另读完 Anthropic 的 **9 个问题选择模块**。ARIS 的 14 个规范路径由协作审查者全文阅读；ResearchStudio 的 README 用于确认实际目录。全部指定规范路径均找到，没有把相似名字或聚合器快照冒充原始技能。

没有宣称读完五个仓库。除下述九模块外，链接的 references、模板、辅助脚本、测试、宿主变体和外部学术论文未做完整审计；上游代码未安装或执行。ARIS 下载中存在的宿主变体不计入全文阅读范围。原文中的效果描述不自动成为本项目验证结果。

| 官方仓库 | 固定提交 | 提交日期（UTC） | 实际规范目录 |
|---|---|---|---|
| [Microsoft ResearchStudio](https://github.com/microsoft/ResearchStudio) | `063f10088af49909e1a4a7ea8d29efe19633f34e` | 2026-09-21 | `ResearchStudio-Idea/skills/` |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | `43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3` | 2026-10-19 | `skills/` |
| [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `593377bb048752abb0152deab9fbb1083a6087df` | 2026-10-19 | `skills/` |
| [Orchestra AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs) | `773a52944ba4747a18bd4ae9ade53fff041adcbc` | 2026-06-16 | `21-research-ideation/` |
| [Anthropic life-sciences](https://github.com/anthropics/life-sciences) | `e96556b637b56d6cc3a5ad33987009be9e60aa5c` | 2026-05-08 | `scientific-problem-selection/` |

这些日期是所选仓库提交的日期，不是每个文件的最后修改时间。机器清单另存完整路径、固定 URL、读取深度、源文件 SHA-256、行数和字节数；非 ARIS 正文另有 Git blob SHA，Anthropic 九模块也有逐文件收据。审查日之后的上游变化需要重读受影响文件，不能沿用本快照结论。

清单共有 **137 个特征条目**，分布为 `implemented` 11、`protocol` 93、`optional` 8、`reference` 1、`deferred` 3、`rejected` 21。这是维护用的覆盖分类，不是实现完成率、方法重要性权重或科研成功率。同一特征可能关联多个能力。

| 标记 | 精确含义 |
|---|---|
| `implemented` | 指定的本地代码子能力已经存在；只按 label 与 gap 所界定的范围理解，运行结果仍查验证报告 |
| `protocol` | 方法已经进入 Atlas 的执行协议，需要宿主读取证据、作判断并留下产物；不等同自动化实现 |
| `optional` | 可按任务、工具可用性和已有授权采用，当前未完整接入或验证相应外部通路 |
| `reference` | 已理解其设计作用，但没有移植相应语料或系统 |
| `deferred` | 明确保留的未来缺口，当前没有等价功能 |
| `rejected` | 明确不继承的规则；有原因和替代处理，不表示拒绝整个来源 |

下文的技能级结论 `adopted` 表示主要方法已采用，通常是 `protocol`；`partial` 表示还存在重要运行时、审计自动化或数据资源缺口。两者都不代表完整复刻上游。精确采用状态以逐特征清单为准。

## 2. 本轮补了什么，实际由谁完成

| 先前不足 | 本轮具体增强 | 本地程序与宿主的分工 |
|---|---|---|
| 只说“发散、批判、选题”，没有策略选择依据 | [methodology §2](../skills/agent-research-atlas/references/methodology.md#2-choose-a-research-mode) 按卡点选择视角，保留拒绝候选和异议 | 宿主选择与实际生成；不运行所有框架，也不以候选数认证创新 |
| 问题选择只剩一个价值/可行性分数 | [§5 九模块](../skills/agent-research-atlas/references/methodology.md#5-extract-a-research-problem) 加风险依赖、价值轴、固定/浮动、决策树、逆境与反演 | 宿主写证据和分支；程序不会计算可发表概率 |
| 有查询列表却不知道哪些来源真的调用、哪些论文没读 | [§3](../skills/agent-research-atlas/references/methodology.md#3-search-and-synthesize) 分开来源调用收据与候选阅读收据 | 本地保存来源与身份；宿主填真实访问、筛选和提取结果 |
| 评审把原问题改成更复杂的新系统 | [§1](../skills/agent-research-atlas/references/methodology.md#1-scope)、[§6](../skills/agent-research-atlas/references/methodology.md#6-develop-mechanisms-and-rivals) 增加 problem anchor 与方法卡 | 宿主逐轮核对范围和操作定义；revision 只处理记录版本 |
| 实验计划完整但代码、标签、指标不一致 | [§9](../skills/agent-research-atlas/references/methodology.md#9-design-discriminating-experiments) 增加 method→code→metric/GT 核对 | 冻结/运行器保留指定工件和日志；宿主确认实现的语义忠实度 |
| “审计过”没有固定对象或逐句覆盖 | [§11](../skills/agent-research-atlas/references/methodology.md#11-construct-the-paper-argument) 分运行、实现、数字、引用四层，绑定对象版本 | `audit.py values` 只比对显式 JSON Pointer、容差和可选哈希；全文抽取、聚合解释、引用支撑仍需实际阅读 |
| 固定种子数被当成足够实验量 | [§9 统计工作台](../skills/agent-research-atlas/references/methodology.md#9-design-discriminating-experiments) 分检出、MDE、精度、等效/非劣、序贯目标 | 没有内置通用功效/推断引擎；复杂设计需匹配实际分析并单独验证 |
| 持久化以后旧审查可以永远有效 | [§11–12](../skills/agent-research-atlas/references/methodology.md#11-construct-the-paper-argument) 记录审查对象、变更影响与失败优先续接 | 显式依赖的复核队列由本地工具处理；未编码语义关联仍需宿主发现 |

这次增强没有把方法协议改成“所有领域都必须完整跑一遍”。研究单位仍是明确范围的一轮 exploration 或一个问题；方向覆盖、假设成熟度、执行完整性和科学支持是不同轴。

## 3. ResearchStudio：具体想法、检索和近邻重叠

三份规范文件使用下划线路径，技能显示名使用连字符。不要构造不存在的 `skills/idea-spark/` 路径。

### 3.1 idea-spark — partial

原文：[ResearchStudio-Idea/skills/idea_spark/SKILL.md](https://github.com/microsoft/ResearchStudio/blob/063f10088af49909e1a4a7ea8d29efe19633f34e/ResearchStudio-Idea/skills/idea_spark/SKILL.md)。重点定位：版本绑定工作、contribution selection/revision、Phase 4 的 source fidelity、completion/failure/cost bounds。特征 ID：`SRC-RESEARCHSTUDIO-IDEA-SPARK-F01`–`F08`。

- **独特方法：**从用户瓶颈形成一个可实现提案；朴素基线和组件生产/消费关系约束复杂度；区分 `idea` 与 `experiment` 深度；先忠实保留机制再改写解释。核心改动会使相关审查失效，失败和需修订的卡片保留，修复次数有边界。
- **已采用与互补：**方法卡、最简单替代、问题锚点、版本审计工作台和有限修订已进入协议（C01/C07/C10–C14/C19–C21/C24）。Anthropic 帮助选择值得解决的问题，K-Dense 补竞争解释，ARIS 补代码和结果审计。
- **真实缺口与取舍：**未移植其请求指纹、隔离调用、输出 envelope、receipt、run-contract 和完整质量事务引擎；历史模式语料只作参考。Atlas 保留跨轮研究图，单轮可以有独立目录，不能照抄 fresh run 为清空研究记忆。也不将“失败只有执行证据才可阻断”推广成通用科学标准：原文重复、逻辑反例和无法满足的假设同样可能否定主张。

### 3.2 paper-search — partial

原文：[ResearchStudio-Idea/skills/paper_search/SKILL.md](https://github.com/microsoft/ResearchStudio/blob/063f10088af49909e1a4a7ea8d29efe19633f34e/ResearchStudio-Idea/skills/paper_search/SKILL.md)。重点定位：Inputs、Output schema、Step 1.5 relevance filter、Dependencies & failure modes、Model knowledge source。特征 ID：`SRC-RESEARCHSTUDIO-PAPER-SEARCH-F01`–`F06`。

- **独特方法：**多查询取并集、六学术来源并发、跨源去重与信息优先级；用原始用户问题和实际标题/摘要做语义筛选；保留未筛选结果、删除数量及来源错误；模型记忆补充单列。
- **已采用与互补：**显式 DOI/arXiv 身份处理有本地代码，候选筛选和覆盖收据是协议（C03–C06/C24）。与 ARIS `research-lit` 的“调用/可读/提取”收据、K-Dense 的综述设计互补。
- **真实缺口与取舍：**六个连接器、上游标题合并规则、字段优先级和并发重试器未整体接入。模型回忆要先作为未核实线索。按阶段决定综述的优先级，不继承统一下沉综述、固定模型层级、单一报告位置等默认项。

### 3.3 scoop-check — partial

原文：[ResearchStudio-Idea/skills/scoop_check/SKILL.md](https://github.com/microsoft/ResearchStudio/blob/063f10088af49909e1a4a7ea8d29efe19633f34e/ResearchStudio-Idea/skills/scoop_check/SKILL.md)。重点定位：Steps 1–5、Step 6 Compare、Step 7 Delta、Important Notes。特征 ID：`SRC-RESEARCHSTUDIO-SCOOP-CHECK-F01`–`F05`。

- **独特方法：**问题设定、核心机制、关键洞见、应用范围四轴；原问题、宽领域、机制签名三类查询；优先深读机制相近或摘要含糊的候选；以最接近工作写具体 delta。
- **已采用与互补：**四轴矩阵、危险近邻和差异的来源定位已进入 C05/C09/C18。ARIS `novelty-check` 补不同技术主张形式，K-Dense 补访问深度与证据批判。
- **明确拒绝：**原 Step 6 把没有先前工作映射为最高 novelty 等级，并用轴匹配数量定总体等级。空集、失败、配额不足或未执行不能推出创新；有限轴计数也不评价科学价值。固定候选数和少数段落只可作为阅读预算提示，不能替代关键问题的查证。未来应补近邻召回与差异判断的标注样例，而不是校准一个“保证新颖”的分数。

## 4. ARIS：研究链条、运行与论文论证

以下 **14 个 canonical `skills/<name>/SKILL.md` 均全文读过**。每个源的精确定位、哈希和特征记录可由 `SRC-ARIS-<NAME>` 查找。没有把其他宿主变体、共享 protocols/templates/helpers 的内容视为已审计。

| 技能 / 固定原文 | 特有方法与采用结论 | 互补对象、实际缺口及下一步 |
|---|---|---|
| [idea-discovery](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/idea-discovery/SKILL.md) — **partial** | `Per-stage evidence gate`、Phases 0/2–5.6：阶段需要实际产物、reviewer 和 trace；已有契约、失败方向影响再生成。采用 C07/C09/C13/C19/C20/C23/C24，负面记录有本地持久化 | 与 IdeaSpark 版本审查、research-wiki 续接互补。未移植全阶段驱动器；默认 novelty confirmed、资源或清理 pilot 不继承。补每阶段实际工件，不能以 done 代替 |
| [experiment-plan](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/experiment-plan/SKILL.md) — **adopted** | Phases 1–4 / `Specify Each Experiment Block`：主论点→竞争解释→最小充分证据；每块绑定 split、指标、设置、失败含义、图表和依赖。C10/C13/C18/C24；冻结预算有实现 | hypothesis-generation 给预测，ablation-planner 给隔离比较，power 给样本依据。冻计划不判断科学充分性，固定 seed 数不继承 |
| [result-to-claim](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/result-to-claim/SKILL.md) — **partial** | Step 1.5 先机械核对数值，再按支持/部分/不支持/缺证据形成决策。C16/C18–C20；显式数字比对和图关系有实现 | experiment-audit 先审测量，paper-claim-audit 审稿件。JSON Pointer 核对不负责自动发现数字或解释因果；缺失、不可解析、故意虚构要分开 |
| [research-lit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/research-lit/SKILL.md) — **partial** | Source Selection、D2 aggregate、Steps 1.5/1.6/2/6：来源可用≠调用；候选身份有 pending/unverified/error；冻结可读证据并核对 assigned/covered/uncovered IDs。C03–C06/C24 | 与 paper-search 多源合并、literature-review 研究单位区分互补。没有原 D2 批量流水线；解析失败不能作为“不相关”静默丢弃 |
| [idea-creator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/idea-creator/SKILL.md) — **adopted** | Phases 1.5/3–5/7：多视角候选取并集并保留来源；客观不可行与本轮未获 pilot 资源分开；预写正、负、无结论的信息价值。C07/C10/C11/C13/C20 | Orchestra 提供视角，K-Dense 保留独立发散与异议，Anthropic 定价值轴。模型族分数与固定 GPU 配置不当认证 |
| [novelty-check](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/novelty-check/SKILL.md) — **adopted** | Phases A–D / verdict limits：把技术主张写成不同表述，查方法、设定、组合机制和发现重叠；重复判断需真实近邻；拥挤与 concurrent 不等于自动无价值。C04/C06/C08/C09/C20 | scoop-check 给比较轴，critical-thinking 检查论证。保留范围、日期、delta、未知项；不保留分数或无边界 novelty 确认 |
| [research-refine](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/research-refine/SKILL.md) — **adopted** | Phase 0、Steps 1.2–1.5/3.2：problem anchor 防漂移；输入/输出、表示、loss、训练、推理流落实方法；每轮检查简洁性并保留建议取舍。C01/C10/C12–C14/C19/C20 | IdeaSpark 补组件依赖与改写忠实，experiment-bridge 补代码对应。宿主需实际读修订；没有自动判断“方案足够具体”的科学判定器 |
| [experiment-bridge](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/experiment-bridge/SKILL.md) — **partial** | Phase 2.5 在部署前检查方法→代码→metric/GT，先 sanity、有限修复、后大任务。C11/C12/C15/C16/C24；本地有界 runner 已有 | experiment-plan 提供设计，experiment-audit 读原代码。配置化大作业依赖队列尚缺；评审缺失时不能记通过，也不自动装包或改变冻结方案 |
| [run-experiment](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/run-experiment/SKILL.md) — **partial** | Steps 1–7：检查真实环境/GPU、运行部署/遥测、取回结果与复现线索。C15/C16/C22/C24；本地 argv、日志、输入哈希可保存 | 与实验冻结、外部结果导入互补。SSH/Vast.ai/Modal/W&B 为可选外部适配；租赁、账单、生命周期和完整环境快照未实现。源文档不授予付费、通知、发布或删除权限 |
| [experiment-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/experiment-audit/SKILL.md) — **adopted** | Checklist A–F：独立读代码和原结果；GT 来源/代理、预测派生归一化、metric 实际调用、字段数值、评测范围和类型。C06/C16/C18/C19 | 先于 result-to-claim；paper-claim-audit 继续追到稿件。继续修复研究可行，但 FAIL 不能自动支持相关肯定论点；目前语义审查由宿主执行 |
| [ablation-planner](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/ablation-planner/SKILL.md) — **adopted** | Steps 2–5：组件删除/替换、参数敏感性、设计替代分开；问题、预测、信息价值、成本和依赖决定顺序，保留负消融。C06/C11/C13/C18/C20 | IdeaSpark 补移除组件损失何种能力，experimental-design 补混杂与匹配。尚无自动信息增益评估器；每个比较仍需具体理由 |
| [paper-claim-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/paper-claim-audit/SKILL.md) — **partial** | Core Principle、Steps 1–3、Artifact Emission：审每处数字、比较、图注和范围，核对单位/舍入/best-mean-median/seed n/配置/相对提升，审计绑定准确输入。C14/C16–C19/C21 | result-to-claim 审推断，citation-audit 审引文。当前只自动比对明确字段；缺稿件 occurrence 抽取、自动聚合和上下文支持判断，先人工建 ledger 并保存实际计算 |
| [citation-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/citation-audit/SKILL.md) — **partial** | Steps 2–4 / Soft-Only / Artifact Emission：每次引用分别查存在、元数据、语境；稿件位置/引用键/原文位置对应；书目冻结仍可报告问题。C04/C05/C18/C21/C24 | literature-review 提供真实来源，paper-claim-audit 检查相邻数字。没有通用 LaTeX/Word occurrence 解析与蕴含验证引擎；按现有写作授权修订或给具体建议 |
| [research-wiki](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/research-wiki/SKILL.md) — **partial** | Core Concepts、query/lint、Hooks 1–4、Re-ideation Trigger：单一真源、实体/关系/视图/历史、负面优先查询包、遗漏回补、新证据触发重评。C02/C20/C23/C24 | Atlas 图谱和显式变更复核有实现；自动压缩 query_pack、任意语义矛盾识别尚缺。旧图先保留再转换；不把证明专用 claim 状态移植为经验真假轴 |

**内部规则也需要取舍。** 这版 ARIS 的较新来源/数值/阶段证据约束，与其他段落里较强的 novelty 确认、评分阈值、资源默认、忽略失败或跳过缺失审查的措辞并存。本项目按可追溯证据、用户范围、保留失败及不夸大主张的契约解决冲突，不把同仓库来源当作天然一致。

## 5. K-Dense：证据质量、假设与实验推断

本轮读的是重命名后的 `K-Dense-AI/scientific-agent-skills`，不是将旧的 `claude-scientific-skills` 地址当作一套独立方法。六份正文均全文审查；其描述的统计/DOE 脚本、测试与所有 references 没有随本轮执行。

| 技能 / 固定原文 | 特有方法与采用结论 | 互补对象、实际缺口及下一步 |
|---|---|---|
| [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/literature-review/SKILL.md) — **partial** | Core Workflow、records/reports/studies、Screening、Verification scope：七阶段、有边界检索、去重研究单位、真实 PRISMA 计数、系统综述的独立资格审查、DOI 验真与句子支撑分开。C01/C03–C06/C21/C24 | paper-search 补发现，research-lit 补覆盖收据，citation-audit 补每次出现位置。没有筛选平台/PRISMA 计数器或元分析引擎；范围探索不得冒充完成系统综述 |
| [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/scientific-brainstorming/SKILL.md) — **adopted** | Operating rules、workflow 1–10、Bias controls：独立生成→讨论→查证→再发散；结构聚类、来源和合并留痕；预定准则/权重/不确定范围，保留异议，评分不自动选赢家。C06–C08/C10/C11/C14/C19/C20 | Orchestra 供策略，Anthropic 供价值轴。人类匿名/分组设施和矩阵脚本未移植；领域定位先读综述与局部独立发散可按阶段兼容 |
| [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/hypothesis-generation/SKILL.md) — **adopted** | Keep objects distinct、Workflow 2–11：冻结观察；分描述/关联/预测/因果/机制；列真正竞争解释、估计目标、操作化构念、校准和负对照；区分事后探索、可重复计算与新证据复验。C03/C06/C10/C12–C14/C17–C20/C24 | ARIS method card 和 experiment-plan 将解释落实比较。字段完整不保证构念有效，医疗等外部要求按实际领域采用，不一概施加 |
| [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/scientific-critical-thinking/SKILL.md) — **adopted** | Appraisal Workflow、Core Capabilities、risk-of-bias unit：固定问题/单位，先抽取证据，再按方法/偏差/统计/逻辑/主张批判；未报告不等于未做，结论强度与问题影响相称。C05/C06/C12/C16–C18 | experiment-audit 给代码证据，result-to-claim 定结论范围。报告完整性、结果偏倚风险、一组证据确定性不能混作分数；GRADE/RoB 只按适用问题、结果和版本使用 |
| [experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/experimental-design/SKILL.md) — **partial** | Choosing/Generating design、mistakes、Workflow：单位、随机化、分块、顺序与独立重复；比较/交叉/聚类/因子/序贯按目标选；响应面查范围、秩、别名、中心点重复。C11–C13/C17/C24 | hypothesis-generation 给目标，ablation-planner 给组件问题，power 给样本依据。未打包 pydoe/排程工具；随机化不解除测量、缺失、干扰等识别限制 |
| [statistical-power](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/statistical-power/SKILL.md) — **partial** | Overview、effect-size decision、simulate、adjustments/reporting：先目标/单位/设计/分析，效应依据与敏感性；固定 n 的 MDE；复杂设计按计划模型模拟、零假设错误率校准、保留失败与 Monte Carlo 区间。C11–C13/C17/C22 | 与实验设计分工；不显著不推出等效，优效检验 helper 不自动适用于精度、等效/非劣或序贯。没有内置 statsmodels/scipy 计算引擎；真实统计适配要另做设计特定验证 |

共同取舍：不把上游添加作者论文、默认展示/付费制图等要求变成每篇用户论文的强制步骤。实际采用的概念与许可需要正确归因，但引用的目的和支持关系仍应明确。上游中的认知效果描述、示例或发表价值不是本项目已验证的事实。

## 6. Orchestra：按卡点选择的两套发散操作

### 6.1 brainstorming-research-ideas — adopted

原文：[21-research-ideation/brainstorming-research-ideas/SKILL.md](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/brainstorming-research-ideas/SKILL.md)。全文读过，包括 `Core Ideation Frameworks 1–10`、Integrated Workflow 和 Framework Selection Guide。`SRC-ORCHESTRA-BRAINSTORMING-RESEARCH-IDEAS-F01`–`F10` 逐一对应以下视角，`F11` 记录拒绝的通用配额：

| 十种视角 | 应如何落地产物 |
|---|---|
| 问题优先 / 能力优先 | 写真实瓶颈，或新能力能回答的旧问题 |
| 抽象上移 / 下移 / 横向迁移 | 一般命题、具体边界、可比邻域 |
| 目标张力与取舍 | 查取舍是否真实，写可测的冲突来源 |
| 跨领域类比 | 映射关系并列出映射失效处 |
| 条件发生了什么变化 | 原失败前提、新使能条件、最小重查 |
| 失败与边界 | 哪个条件触发什么错误及竞争解释 |
| 简洁性 | 朴素强基线、必须组件、额外成本 |
| 利益相关者轮换 | 谁获益/受损、哪个目标被遗漏 |
| 组合与分解 | 每个组件作用、依赖和移除后果 |
| 两句测试与策略选择 | 清楚说问题与机制，据卡点选框架 |

与 K-Dense 的独立发散/异议保护、ARIS 的可实现精炼和负结果保留互补。两句表达只是清晰性检查；固定 10–20 个想法、三项实验、两周 pilot 等不作为普适标准。候选数量和停止条件由信息价值与预算决定。

### 6.2 creative-thinking-for-research — adopted

原文：[21-research-ideation/creative-thinking-for-research/SKILL.md](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/creative-thinking-for-research/SKILL.md)。全文读过，包括 Frameworks 1–8、Combining Frameworks 和 Common Creative Blocks。`SRC-ORCHESTRA-CREATIVE-THINKING-FOR-RESEARCH-F01`–`F08` 分列八种操作：

| 八种操作 | 用法与检查 |
|---|---|
| Bisociation / 概念交叉 | 做两个概念集合的交叉，筛出实际机制而非术语拼接 |
| 表征重构 | 换目标、形式、粒度、主体或时间尺度，同时保留问题锚点 |
| 结构类比 | 映射对象与关系；明确哪些关系不可迁移 |
| 约束操作 | 分硬/软/隐含，说明放松、收紧或替换的代价 |
| 否定、反向与 TRIZ | 反转默认前提，产生新的可检验解释 |
| 抽象阶梯 | 一般化、特例化或横向类比，并返回可测实例 |
| Adjacent possible / 新可行邻域 | 确认数据、工具或条件真的变化 |
| 辩证并置 | 对立目标形成新设定，验证是否真实解除取舍 |

这些操作进入 C07/C08/C10–C12 的策略选择。`F09` 拒绝把普遍创造力优势或示例中的理论强断言当作已证实结论；例如关于压缩极限的例子仍需查原始理论与假设，不能作为论文论据直接沿用。来源、操作、预测及失配处应留下记录。

## 7. Anthropic：九模块不是一个打分表

原文：[scientific-problem-selection/SKILL.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/SKILL.md)，技能结论 **adopted**。三个入口是开始新问题、排查已有问题、战略性整体复盘；按当前产物与缺口选择入口。以下九文件全部读完，每行对应 `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION-F01`–`F09`，已进入 [methodology §5](../skills/agent-research-atlas/references/methodology.md#5-extract-a-research-problem)。

| 模块 / 固定原文 | 特有方法、产物与迁移边界 |
|---|---|
| [01-intuition-pumps.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/01-intuition-pumps.md) | 在干预/测量/理论计算与逻辑/工具中找机会；七种启发含系统化、技术限制、缺失能力、动态、新坐标、平台与预期现象缺席。产出问题与触发观察；空文献搜索不等于现象缺席 |
| [02-risk-assessment.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/02-risk-assessment.md) | 分科学与技术假设，查依赖、测试成本和时间；先测决定后续价值的前提。产出 go/pivot/stop 分支；主观风险档不当成功概率 |
| [03-optimization-function.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/03-optimization-function.md) | 知识、工具、应用项目用不同价值轴，避免错目标优化。产出学习价值/使能能力/实际受益的理由；不拿 venue 名或统一总分替代 |
| [04-parameter-strategy.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/04-parameter-strategy.md) | 固定关键战略参数，允许其他条件调整，形成备选项目族。产出固定/可变与代价表；用户权限、资源上限、已冻结比较不因此可变 |
| [05-decision-tree.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/05-decision-tree.md) | 在实际实施、批判评估和更高层战略之间切换；把观察连接到选择。产出阈值/下一步/资源分支；不强制固定周月节奏 |
| [06-adversity-planning.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/06-adversity-planning.md) | 预想技术失败、负结果和竞争工作，寻找修复、升级、替代。产出失败预案和可学信息；承认合理停止，不保证每条分支都可发表 |
| [07-problem-inversion.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/07-problem-inversion.md) | 解除软约束、换可比较目标、由已有答案寻找问题。产出新问题与沿用证据范围；事后选题标 exploratory，再作新检验 |
| [08-integration-synthesis.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/08-integration-synthesis.md) | 合并问题、风险、计划，针对不同听众调整深度。产出一页交接/短讲/技术记录；不用固定页数，不暗增机制或效果 |
| [09-meta-framework.md](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/references/09-meta-framework.md) | 按阶段产物导航，区分局部修订与重大转向，检查下游一致性。产出版本/审查者/缺口/下一步；不自动创建提醒或后台工作 |

它主要补 **C08 问题选择**，并与 Orchestra 的发散、K-Dense 的可反驳假设、ARIS 的实验和失败记忆相接。生物案例不直接证明 Agent/RAG/KG/NLP 的方法效果，固定工期和长期成功承诺不迁移。

`F10` 还记录一项书目修正：上游把 Cell 方法论文归为 Fischbach 与 Walsh 合著，而 [原始出版记录](https://doi.org/10.1016/j.cell.2024.03.012)、[PubMed 元数据](https://pubmed.ncbi.nlm.nih.gov/38608651/)及[作者论文列表](https://www.fischbachgroup.org/publications)列出的作者为 **Michael A. Fischbach**。这里只核对书目/摘要，不声称本轮完整复审了该 Cell 论文及其全部证据。

## 8. 互补关系与按研究问题选路线

| 当前问题 | 主要方法 | 互补方法 | 可审查的停止点 |
|---|---|---|---|
| 对新子领域完全陌生 | K-Dense literature-review + ResearchStudio paper-search | ARIS research-lit、领域术语图 | 有范围的综合图、真实来源/阅读收据、未覆盖清单 |
| 看过综述却提不出机制不同的候选 | Orchestra 两套策略 + K-Dense independent brainstorming | Anthropic intuition/价值轴、ARIS idea-creator | 候选机制、来源、异议与比较理由；不是固定数量 |
| 已有路由/RAG/Memory 代码，想知道哪里有研究问题 | problem anchor + ARIS research-refine | 旧失败记忆；RE 的 template-grounded 入口见工具审计 | 基线/假设/可干预代码位置/缺失切片→最小诊断，先分实现问题与研究问题 |
| 一个想法似乎新，但可能只是同义改写 | scoop-check 四轴 + ARIS novelty-check | K-Dense critical thinking、paper-search 多源 | 最危险近邻、实际原文定位、剩余 delta 与尚未读到的威胁 |
| 想法重要但数据/算力不足 | Anthropic 风险依赖/参数/逆境 | Atlas 四项可行性、ARIS 最小实验 | 最早有信息的检查或明确 parked；不虚构可用资源 |
| 改进出现了，但原因可能是计算量或评测偏差 | K-Dense hypotheses + experimental-design | ARIS ablation-planner/experiment-audit | 竞争预测、等资源基线、真实标签/metric、适配统计分析 |
| 有输出文件，需要形成可写的论点 | result-to-claim + paper-claim-audit | citation-audit、四层审计台 | 每个论点的支持/限制、数字出处和每次引用支撑；不把 runner PASS 当科学支持 |
| 新结果/近邻论文推翻旧前提 | research-wiki + IdeaSpark 版本复核 | Anthropic 决策/反演、RE direction-evolution | 原记录保留、受影响链待复查、最小下一步及重启条件 |

综述与独立发散的顺序冲突可以按阶段化解：领域定位先了解基础；进入某一问题的候选生成时，先保留独立机制草案，再看他人候选与新增文献，并重开一轮。结构类比负责提出可能性，原文查新负责界定差异，区分性实验负责判断预测；任何一步的产物不能冒充下一步的完成。

## 9. 真冲突、采用规则与测试边界

下表连接主注册表的 `CFxx`，列的是**需要验证的行为契约**，不把这份文档当作已执行证明。确定性回归、独立上下文任务、真实服务调用分别看 [validation.md](validation.md)、[integration-review.md](integration-review.md)、[forward-conflicts.md](forward-conflicts.md)。某报告若仍标 `not_run` 或占位，则该层验证尚未完成；单次通过也不证明全任务泛化。

| 冲突 ID | 来源中的真实张力 | 保留与拒绝 | 用什么输入区别两者 |
|---|---|---|---|
| CF01 | scoop-check 空结果映射最高新颖 vs 有边界证据判断 | 保留多轴查找；拒绝空集认证创新 | 成功零命中、来源失败、未调用三种回执均不能自动得到 novelty confirmed |
| CF02 | paper-search 模型回忆/摘要 vs 全文结论 | 保留线索和访问层级；拒绝补写未读方法 | 只有标题摘要和疑似经典论文回忆时，应保留待核实与全文缺口 |
| CF03 | survey-first、综述下沉、独立候选生成 | 按定位/发散/查新分阶段；拒绝一条顺序通吃 | 新领域入门与已知范围内想法生成应给不同合理入口 |
| CF04 / CF15 | 固定分数、候选数、实验数、seed 数 vs 科学价值与设计适配 | 保留优先级理由和预算；拒绝阈值认证发表或推断充分 | 给低预算、聚类数据、非劣目标；需解释单位/界值/匹配分析而非套固定 seeds |
| CF05 / CF14 | 可以迭代方法 vs 冻结比较；问题反演 vs 前瞻主张 | 允许声明的候选变化和事后探索；评价器/数据改变另立版本 | 已看结果再改主指标须保留偏离与 exploratory，不能回填成原计划 |
| CF06 / CF20 | 自动试验/安装/云配置 vs 实际资源和授权 | 已授权范围内有界推进；拒绝默认花费/外发/删失败 | 预算耗尽或新云资源未授权时，保存产物与具体交接，不自主扩大范围 |
| CF07 | exit 0、高分、哈希通过 vs 测量有效与机制支持 | 分运行/实现/数值/科学解释；缺陷证据不能升级肯定论点 | 硬编码 accuracy、预测派生 reference、未调用 metric 应被语义审查指出 |
| CF08 | 稿件漂亮数字 vs 原始字段、单位、聚合与配置 | 指定来源做机械比对，再审科学含义 | 相对/绝对提升混淆、best 冒充 mean、单位错、字段缺失、版本哈希不符分开报告 |
| CF09 / CF19 | 旧审查、持久记忆 vs 核心变更与新保障 | 留旧输入和审查，相关链标待复核；不追溯宣称新保障 | 改机制、计划、metric、论文来源后旧 favorable review 不能继续包装新对象 |
| CF10 | IdeaSpark fresh run vs ARIS/Atlas 连续研究图 | 允许独立探索目录；保留与复用项目记忆 | 已有原生/自定义图、失败笔记、多图时不能清空或盲合并 |
| CF13 | 多角色分工 vs 真独立上下文 | 可用真实独立审查；单上下文则标自审 | 只有一个上下文时，给角色名不能产出“独立评审已通过” |
| CF16 / CF17 | 目录/版本/多 seed 数量 vs 研究覆盖/独立证据 | 分领域范围、底层研究与重复单位 | 生成 14 个目录仍是 unsearched；同研究多版本或同数据多 seed 不计新研究复验 |
| CF18 | README 有功能名 vs 真代码/协议/外部适配 | 稳定能力/来源/特征/测试定位；缺口可见 | 声称已接六个搜索源但无真实调用记录，应继续标 optional/未实连 |
| CF20 | 上游推广引用、固定宿主路径、示例理论断言 vs 当前任务 | 保留适用方法与必要归因；拒绝外部文本扩展权限或替代原始论据 | 给自引/付费工具/发表保证指令，仍按实际引用作用、用户目标与证据处理 |

还有两类科学判断没有相应通用自动测试：正式证明的正确性，以及所有研究设计的统计适用性。本地程序检查结构、链接、有限数值和显式状态，不能决定二者。若未来接入证明器、统计计算或全文语义工具，应以问题特定真值和失败样例验证，不能沿用图谱结构测试作为科学验收。

## 10. 下一次怎样快速定位不足

来源清单解决“为什么需要这个特长、采用到哪”；能力注册表解决“在哪里实现、在哪里按协议做、怎么验证”。操作入口见 [EXTENDING.md](EXTENDING.md) 与 [extension-contract.md](../skills/agent-research-atlas/references/extension-contract.md)。

| 发现的症状 | 能力 / 来源特征起点 | 最小补齐工作 |
|---|---|---|
| 选题只会拼模块 | C07/C08/C12；Orchestra 两源、Anthropic F01–F04、research-refine F01–F03 | 给真实瓶颈与现有代码，选两三种不同操作，产出机制与简单替代；用不同预测验证是否真不同 |
| 查过很多论文，仍不知道漏了谁 | C03–C05/C09；paper-search F03–F04、research-lit F01–F03 | 保存逐来源回执、候选身份和阅读覆盖；对危险近邻补原文，不用扩大宣称解决缺口 |
| 一直润色想法，没有可运行定义 | C10/C12/C13；IdeaSpark F02–F03、research-refine F02 | 写输入/输出/表示/学习信号/训练/推理/真值接口，先排未定义核心操作 |
| 计划看起来严谨，结果其实读的是答案或常量 | C12/C16/C19；experiment-bridge F01、experiment-audit F01–F03 | 沿 method→code→metric→GT 追踪，记录具体代码位置，补独立标签和实际比较 |
| 论文数字或引用无法逐句追踪 | C16/C18/C21；paper-claim-audit、citation-audit | 先建 occurrence ledger；JSON 值可机械核对，聚合与句子支撑须真实读取或另实现可验证解析器 |
| 想用所有统计技能但不知道选哪个 | C12/C13/C17；experimental-design、power F01–F05 | 先定估计目标、独立单位、设计和分析；再接合适软件，做 null/边界/失败验证 |
| 新证据来了却沿用旧审查 | C14/C19/C20；IdeaSpark F04、paper-claim-audit F03、research-wiki F03 | 检查受影响链接、输入版本和 pending；复查后明确 reviewer、证据与状态理由 |
| 下一会话又重做失败方向 | C02/C20/C24；research-wiki F01–F02、Anthropic F05–F09 | 失败/冲突/未测试链优先交接；自动 query_pack 仍是 deferred，若实现需证明关键反证未丢 |
| 想把本地试验扩到集群或付费服务 | C15/C22/C24；run-experiment F02–F04、experiment-bridge F03 | 先明确 backend、预算、job ID、来源和失败导入契约，再实现实际适配；本地秒数不等于云账单控制 |

例：想检查数字审计缺口，可在仓库根运行 `python skills/agent-research-atlas/scripts/audit.py locate --query C16`，再查对应特征的 `status/gap/remedy`。`locate` 是维护导航，不是对研究想法评分。新增来源或改上游版本时，补稳定特征 ID、固定来源、真实读取范围、互补对象和最小回归输入；保留旧失败，更新受影响协议与测试证据，再调整能力标签。

## English scope note

This audit covers the full bodies of 26 explicitly named upstream `SKILL.md` files and all nine Anthropic problem-selection modules at pinned revisions. It does not cover entire repositories, all linked helpers, host variants, or empirical effectiveness of the upstream research systems. The feature manifest distinguishes implemented local subsets, host-executed protocols, optional integrations, deferred work, reference material and deliberately rejected defaults. The companion registry supplies code/protocol/test locations; execution claims belong to the actual validation reports. Neither source coverage, structural validation nor a successful synthetic run establishes research novelty, scientific support or publication success.
