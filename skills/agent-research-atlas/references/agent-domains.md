# Agent domains / Agent 研究领域目录

Reviewed: 2026-10-20

这是一份可扩展的研究地图起点，不是宣称当前 Agent 研究只有这些方向的分类定论。方法部分综合已审查的关键上游技能；目录和例子为原创组织，未宣称通读全部上游仓库，也未逐领域完成最新文献综述。

## Contents

1. [Map contract](#1-map-contract)
2. [Domain catalog](#2-domain-catalog)
3. [Interface questions](#3-interface-questions)
4. [Select the evidence and method](#4-select-the-evidence-and-method)
5. [Domain record template](#5-domain-record-template)
6. [Search vocabulary](#6-search-vocabulary)
7. [Illustrative research slices](#7-illustrative-research-slices)
8. [Measure the right thing](#8-measure-the-right-thing)
9. [Extend the map](#9-extend-the-map)

## 1. Map contract

项目状态位于 `PROJECT/research-atlas/atlas.json`，所有项目操作使用 `--root PROJECT`。将领域保存为 `domain`，将每轮检索和覆盖边界保存为 `exploration`。

领域记录使用 `status=active`，覆盖状态位于 `data.coverage`。标记 `reviewed` 时需要 `data.last_reviewed`（`YYYY-MM-DD`）及可追溯的 `exploration`。

- 从用户当前问题选择相关方向，再展开必要的依赖；不必一次填满目录。
- 为实际创建的领域设置 `unsearched`、`partial`、`reviewed` 或 `stale`。
- 新建领域默认没有最新综述证据；不能因为目录自带描述便标成 `reviewed`。
- 每个 `reviewed` 必须能解释审查问题、检索来源、时间窗、访问缺口和截止日期。
- 同一论文可关联多个领域；同一个研究问题也可能位于模块之间。
- 一个方向有进展不意味着其兄弟方向已完成。保持未探索和已过时方向可见。
- 不把领域覆盖率、论文数量或状态数量当作创新能力或科学可信度。

接入旧地图时先保留原文件，通过 `adopt` 建立来源引用，再由宿主读取内容并增量转换。脚本不会自动理解任意 Markdown、笔记或自由文本，也不会仅因导入就将方向标为已审查。

目录采用问题和机制组织；框架名称作为实现或基线属性，不以框架品牌划分独立科学领域。此组织参考 [Orchestra 的问题发现方法](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/brainstorming-research-ideas/SKILL.md)。

## 2. Domain catalog

下列“可研究问题”都是搜索与诊断入口，**不是已经核验的新颖研究点**。

程序初始化的领域与 `queries --domain` 可接受的种子 ID 以 `assets/agent-taxonomy.json` 为准。下表是更细的扩展视角，不是初始化清单；建议键需明确加入项目，或映射到已有种子，不能假设它们都能直接传给内置查询命令。

| 建议领域键 | 中文 / English | 核心对象 | 可研究的问题入口 |
|---|---|---|---|
| foundations | 基础机制 / LLM foundations | token、embedding、概率、解码、上下文、状态 | 模型能力、表示或上下文如何限制上层行为？ |
| intent-understanding | 意图理解 / Intent understanding | 单意图、多意图、否定、修正、条件与指代 | 用户改口后哪个目标仍有效，何时需要澄清？ |
| routing | 路由与策略选择 / Routing and policy selection | 分类、规则、学习路由、模型/工具/工作流选择 | 错路由如何发现和恢复，路由置信度是否可校准？ |
| planning-feedback | 规划与反馈 / Planning and feedback | ReAct、plan-and-execute、混合策略、重规划 | 何时值得规划，观测变化何时应使旧计划失效？ |
| retrieval-ingestion | 数据准备与索引 / Ingestion and indexing | 解析、分块、索引、更新、去重、元数据 | 信息在进入检索库之前是否丢失或失去版本语境？ |
| retrieval-selection | 检索与上下文选择 / Retrieval and context selection | 稀疏/稠密/混合检索、过滤、重排、上下文装配 | 召回正确证据后为何仍无法支持答案？ |
| agentic-rag | 自主检索 / Agentic RAG | 查询分解、多跳检索、迭代检索、停止 | 下一次检索是否有预期信息收益，何时应停止？ |
| knowledge-graphs | 知识图谱与本体 / Knowledge graphs and ontology | 实体对齐、关系抽取、约束、溯源、图查询 | 模式符合是否掩盖事实错误，冲突证据如何保留？ |
| answer-generation | 回答与证据归因 / Answer generation and attribution | 综合、引用、冲突处理、拒答、不确定性 | 答案是否被检索证据支持，缺证据时怎样表达？ |
| tools-recovery | 工具与失败恢复 / Tool use and recovery | API、前置条件、幂等、重试、补偿、状态对账 | 超时后动作是否实际完成，恢复会否重复执行？ |
| long-term-memory | 长期记忆 / Long-term memory | 情景、语义、程序记忆，写入、读取、更新、遗忘 | 旧记忆何时应撤销，错误如何积累或被纠正？ |
| multi-agent | 多 Agent 协作 / Multi-agent collaboration | 分工、通信、调度、协调、竞争、证据共享 | 收益来自独立信息、计算增量还是协作机制？ |
| safety-permissions | 安全与权限 / Safety and permissions | 指令边界、提示注入、访问控制、工具授权 | 模型理解正确时，运行时是否仍可能越权？ |
| evaluation | 评测与有效性 / Evaluation and validity | 数据集、指标、标注、LLM judge、污染、回归 | 评测分数是否测到了想研究的能力？ |
| efficiency | 效率与资源分配 / Efficiency and resource allocation | token、时延、费用、缓存、批处理、测试时计算 | 在质量约束下何时追加计算才值得？ |
| observability | 可观测性与复现 / Observability and reproducibility | trace、事件日志、checkpoint、版本与环境 | 能否定位失败、复现轨迹并从中断恢复？ |
| human-collaboration | 人机协作 / Human-agent collaboration | 澄清、纠正、接管、偏好与可用性 | 何时打断用户有价值，接管后状态是否一致？ |
| multimodal-interaction | 多模态与实时交互 / Multimodal and real-time interaction | 语音、图像、流式输入、打断、时间对齐 | 输入未完整时何时可行动，取消信号如何传播？ |
| adaptation-learning | 自适应与学习 / Adaptation and learning | prompt优化、数据选择、反馈、RL、迁移 | 学到的是一般策略还是对评测分布的适配？ |

这些领域可继续拆分。例如检索可扩展为权限、版本、时间、规模、语言、文档类型和多跳问题；多 Agent 可扩展为通信拓扑、证据独立性、资源预算和动态成员。

对“本体约束有效”“记忆有帮助”等宽泛描述，使用 [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md) 的对象区分，改写成有边界的候选假设。

## 3. Interface questions

沿信息和状态的变化检查模块接口。只评单模块准确率可能看不到组合失效。

| 接口 | 需要追踪的对象 | 可区分的失败原因 | 建议诊断 |
|---|---|---|---|
| 输入 → 意图 | 目标、否定、时间、条件、指代 | 理解错误、信息缺失、过早承诺 | 对照澄清条件与用户修正序列 |
| 意图 → 路由/规划 | 有效目标、依赖、优先级、约束 | 路由错误、计划漏约束、条件次序错误 | 保持意图标签正确，单独干预计划 |
| 检索 → 回答 | 证据片段、出处、版本、权限 | 证据未召回、装配丢失、生成未利用 | 逐层使用 oracle 输入定位瓶颈 |
| 本体 → 图谱 → 回答 | 实体、关系、证据、冲突状态 | 语法合规但事实错、对齐错、证据脱落 | 同时测约束满足与事实/溯源质量 |
| 计划 → 工具 → 状态 | 前置条件、动作ID、返回值、真实后果 | 请求失败、响应丢失、动作已完成 | 可控超时与状态对账，不只重试次数 |
| 记忆 → 当前决策 | 来源、时间、作用范围、撤销信息 | 旧事实、错范围、偏好冲突 | 设计明确更新和撤销的任务序列 |
| Agent → Agent | 原始证据、推论、置信度、角色 | 重复同一错误、压缩失真、假共识 | 隔离证据来源并匹配总计算预算 |
| 权限 → 检索/工具 | 主体、资源、动作、授权时点 | 未授权召回、过期授权、执行层漏查 | 在授权沙箱中测访问决策与实际动作 |
| 人类纠正 → 执行 | 撤销目标、已提交动作、待处理任务 | 界面确认但后台未取消 | 检查取消到达各层的状态与时间 |

Oracle 诊断是用已知正确的中间输入替换某层输出，以确定错误来自哪里；不要把 oracle 结果报告为部署时可实现的性能。

## 4. Select the evidence and method

| 研究目的 | 主要证据 | 合适方法 | 关键比较条件 |
|---|---|---|---|
| 理解路由何时失效 | 意图标签、轨迹、置信度和恢复结果 | 错误分类、干预、校准 | 同任务、同模型、相同可用信息 |
| 比较检索策略 | 相关性标签、证据集合和答案 | 分层评测、配对比较 | 相同语料版本、权限与上下文预算 |
| 解释记忆增益 | 写入/读取记录和后续行为 | 更新/撤销干预、消融 | 控制上下文长度和额外提示信息 |
| 证明协作机制有贡献 | 消息、独立证据和任务结果 | 计算匹配基线、通信消融 | 单 Agent、多采样、投票等适当基线 |
| 测试工具恢复可靠性 | 实际后果和可控故障 | 故障注入、状态机属性检查 | 区分请求状态、响应状态与外部状态 |
| 提出形式保证 | 明确定义、假设和系统语义 | 反例搜索、证明或模型检查 | 清楚写保证成立的环境假设 |
| 判断用户交互价值 | 实际用户任务与反馈 | 用户研究或任务对照 | 适当同意、代表性和测量有效性 |
| 比较资源效率 | 质量、失败率、成本、延迟分布 | 预算扫描、约束下比较 | 包含调参、重试、检索和通信成本 |

按问题选择方法，不将每篇论文强行改造成“提出新模型”。失败机制、评测失真、边界条件、资源和理论结果也可形成贡献候选；仍需查新和证据。[方法参考：Scientific Problem Selection](https://github.com/anthropics/life-sciences/blob/main/scientific-problem-selection/SKILL.md)。

## 5. Domain record template

以下是阅读和写作模板；实际保存时遵循工具提供的 schema，不把模板字段假装成程序已经支持的参数。

```text
Domain ID / 领域ID：
Name and synonyms / 名称与中英文同义词：
Question boundary / 本次要审查的具体问题：
Parent and related domains / 上级与关联领域：
Inputs, outputs, state / 输入、输出、持续状态：
Methods and assumptions / 方法家族及其假设：
Evidence / 论文ID、访问级别、章节/表格/代码位置：
Tasks and datasets / 任务、数据版本和标签：
Known findings / 已有研究支持的结论：
Disagreements and unknowns / 分歧与待核实项：
Candidate problems / 关联问题ID：
Coverage / unsearched | partial | reviewed | stale：
Search boundary and date / 检索来源、检索式、截止日期：
Next check / 最能改变判断的下一项检查：
```

## 6. Search vocabulary

从术语组合开始，随着真实论文用词更新检索式。不要固定一个术语后只反复搜索相同结果。

| 中文意图 | 英文检索词起点 | 必须补的相邻概念 |
|---|---|---|
| 多意图和改口 | multi-intent, intent revision, conversational correction | task constraints, dependency, dialogue state |
| 路由恢复 | routing error, policy selection, recovery | calibration, selective prediction, fallback |
| 规划失效 | replanning, plan repair, execution monitoring | changing environment, partial observability |
| 新旧证据冲突 | temporal RAG, versioned retrieval, conflicting evidence | provenance, valid time, document updates |
| 证据没被用到 | context utilization, evidence attribution | retrieval failure, reranking, context selection |
| 图谱真实性 | knowledge graph construction, ontology constraints | entity resolution, provenance, contradiction |
| 记忆撤销 | memory update, forgetting, belief revision | temporal consistency, deletion, stale memory |
| 多 Agent 真正收益 | multi-agent coordination, communication | compute-matched baseline, diversity, correlated errors |
| 工具重复动作 | idempotency, ambiguous timeout, compensation | distributed transactions, exactly-once assumptions |
| 评测污染 | benchmark contamination, data leakage | test-set reuse, judge bias, adaptive overfitting |

用 [ResearchStudio-Idea](https://arxiv.org/abs/2607.04439) 的机制查新思路，分别检索问题描述、机制描述和两者组合；上表本身不是完成查新的证明。

## 7. Illustrative research slices

以下三个例子只展示如何缩小问题；都需要独立查新，不预设它们未被解决。

### A. 修改条件之后的任务执行

- 场景：用户先提出任务，随后修正其中一个条件；系统继续执行旧计划。
- 问题候选：理解标签正确后，失败是否仍来自计划和执行状态未同步？
- 竞争解释：意图误判、更新未传播、工具已提交、取消到达太晚。
- 最小诊断：在可控任务中记录每层状态与时间；分开替换正确意图、正确计划和正确取消信号。
- 不能推断：单个示例成功便说明系统能处理所有多意图任务。

### B. 检索到正确版本后仍回答旧内容

- 场景：证据集合含有效新版本，但答案采用旧规则。
- 问题候选：错误来自排序、上下文组织、版本理解还是生成倾向？
- 竞争解释：新版本不适用、标签错、授权过滤正确排除了部分证据、上下文被截断。
- 最小诊断：固定问题、适用日期和权限，控制旧/新证据的内容与位置，分层测量。
- 不能推断：加入日期提示的改进自动构成新的检索算法贡献。

### C. 多 Agent 增益是否来自更多计算

- 场景：协作系统比单 Agent 获得更高分，但使用更多调用和 token。
- 问题候选：独立信息交换是否在相同资源下仍有增益？
- 竞争解释：总计算量、更多候选答案、更长上下文、评审偏好或任务分配本身。
- 最小诊断：匹配合理资源范围，加入单 Agent 多采样基线并干预通信内容与证据独立性。
- 不能推断：移除通信后分数下降就已经排除了所有替代解释。

## 8. Measure the right thing

- 意图准确率不能替代任务成功率；同时检查约束满足、错误恢复和澄清代价。
- Recall@K 的分母来自已定义的相关证据集合；不把返回的 K 条当成全部相关项。
- 若任务需要多个联合证据，额外测联合证据覆盖；平均单条相关性可能掩盖缺失关键证据。
- 回答正确性、证据忠实性、引用准确性和拒答适当性分别测量。
- 工具返回成功码不等于外部目标状态正确；使用实际状态或可验证环境判定。
- 多 Agent 的共识率不等于真值；记录共同来源和相关错误。
- 延迟报告分布和测量范围；费用包括检索、重试、通信、评审与失败调用。
- 用户级、任务级、文档级依赖应体现在分析中；明确独立评测单位。
- 若使用 LLM judge，验证其与合适参考标签的一致性并分析偏差，不默认其评分为客观真值。

分析原则参考 [K-Dense scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md)。

## 9. Extend the map

出现新方向时新增 `domain`，写出它解决的独立问题、与已有领域的关系、同义词和需要的证据。仅工具名称不同而机制相同的，优先归入现有方法家族。

对外部学科任务增加其测量、数据、实验和审查要求；不要把 NLP benchmark 的规则视作生物实验、医疗或用户研究的充分条件。

每轮结束更新实际查过的切片和下一项检查。可以承诺保存可追溯进展，不能承诺固定轮数覆盖所有领域、找到必然成立的研究点或保证发表。
