# Research methodology / 科研方法

Reviewed: 2026-10-20

这份文档是对已审查上游方法技能的原创综合。本轮逐项核对 26 个指定 SKILL 正文，并另读 Anthropic 的 9 份问题选择模块；不代表读完这些仓库、运行过其全部辅助程序，或验证了论文录用率。仓库 `docs/method-source-audit.md` 与 `docs/method-source-manifest.json` 记录固定版本、逐项采用与缺口。以下是宿主需要实际执行的研究协议，不能仅靠生成表格宣布完成。

## Contents

1. [Scope](#1-scope)
2. [Choose a research mode](#2-choose-a-research-mode)
3. [Search and synthesize](#3-search-and-synthesize)
4. [Build the domain map](#4-build-the-domain-map)
5. [Extract a research problem](#5-extract-a-research-problem)
6. [Develop mechanisms and rivals](#6-develop-mechanisms-and-rivals)
7. [Check nearest prior work](#7-check-nearest-prior-work)
8. [Assess feasibility](#8-assess-feasibility)
9. [Design discriminating experiments](#9-design-discriminating-experiments)
10. [Interpret results](#10-interpret-results)
11. [Construct the paper argument](#11-construct-the-paper-argument)
12. [Decide the next action](#12-decide-the-next-action)

## 1. Scope

先确定这次要回答的研究问题、资源约束和交付物，再决定探索深度。用户已有明确范围时直接推进，不重新要求其批准同一项工作。

- 记录研究对象、目标人群或任务、可用数据、基线、模型/API、算力、时间与费用边界。
- 区分真实约束、暂定假设和未知信息；不要把“没有提到 GPU”写成“没有 GPU”。
- 使用项目根参数 `--root PROJECT`；默认状态在 `PROJECT/research-atlas/atlas.json`，已有原生图可由配置指向项目内其他目录。实验工具仍固定使用 `PROJECT/research-atlas/experiments`，`artifact_path` 以项目根解析。
- 复用已有记录和决策，再补新证据；避免每次从零搜索同一批论文。
- 本轮可以只完成一个领域切片、一个问题或一项判别实验。未探索方向保持可见。
- 输出语言跟随用户；默认用中文解释研究决策，关键术语附英文，英文论文内容使用英文。

选题时分别问“回答后有何知识价值”和“我们如何获得可信答案”。两者都需要具体理由，不能用会议名替代价值判断。[方法依据：Scientific Problem Selection](https://github.com/anthropics/life-sciences/blob/main/scientific-problem-selection/SKILL.md)。

保留用户原始任务，并写 `problem anchor`：瓶颈、目标、非目标、不可变资源边界和当前成功条件。主题起步先定位文献；已有代码起步则先读基线、评测接口、失败记录，区分新研究问题与实现错误。修改锚点要记录理由及受影响计划，不能靠增加模块悄悄换题。

## 2. Choose a research mode

| 眼前的问题 | 优先方法 | 最小可审查产物 | 不应推成的结论 |
|---|---|---|---|
| 不知道领域有什么 | 范围综述、概念和方法分类 | 有检索边界的领域图 | 已覆盖所有研究 |
| 读了很多仍找不到点 | 失效分析、假设拆解、目标矛盾 | 有证据的问题记录 | 组合两个术语就是创新 |
| 有想法但不知道是否重复 | 最近工作对比、机制查新 | 最相近论文及差异矩阵 | 未搜到即无人做过 |
| 现象出现但原因不明 | 竞争解释、干预与负对照 | 可区分预测矩阵 | 相关性就是机制 |
| 新方法是否实用 | 强基线、匹配资源的比较 | 质量、成本、延迟与失败分布 | 更大计算量就是方法优势 |
| 系统在哪些情况下失效 | 压力测试、分布外和边界测试 | 失败条件与复现步骤 | 极端例子代表常见风险 |
| 要提出理论命题 | 定义、假设、反例、形式推导 | 明确适用条件的命题与证明 | 有限实验证明一般定理 |
| 已有结果但不会形成论文 | 结果到论点映射、范围校准 | 论点—证据—限制关系 | 先写结论再挑结果 |

按卡点选两三种视角，记录选择理由及产生的不同预测，不强迫项目跑完所有框架：

| 卡点 | 可选策略 | 应留下的产物 |
|---|---|---|
| 有工具但没有问题 | 问题优先／能力优先；利益相关者轮换 | 真实需要、使用条件与受益／受损对象 |
| 问题过泛或只剩案例 | 抽象上移、具体化、横向迁移 | 一般命题、边界实例与两者关系 |
| 两目标似乎冲突 | 取舍核验、对立假设并置、重定义目标 | 冲突来自物理限制、设定还是方法的证据 |
| 思路都来自同一领域 | 概念交叉矩阵、结构类比 | 对象／关系映射、失配处、可检验迁移预测 |
| 旧方法被放弃 | 条件变化、近期可用能力 | 原失败前提、实际变化和新的最小检查 |
| 机制不清楚 | 失效分析、边界探测 | 失效分层、原因与竞争解释 |
| 方案越写越复杂 | 简单基线、组件拆分与重组 | 每个组件生产／消费什么，移除损失什么能力 |
| 被表述或默认假设困住 | 换目标／形式／粒度／时间尺度；否定与反演 | 保留的问题锚点、新假设与查新义务 |
| 约束很多或没有抓手 | 硬／软／隐含约束分类，放松、收紧或替换软约束 | 固定／可调整清单；用户授权和预算不随之放松 |
| 难以解释贡献 | 两句问题与机制说明、外行可读改写 | 清楚的价值与预测，不凭流畅性判定可发表 |

这些策略覆盖 Orchestra 的十种选题视角与八类创造性操作；它们是生成线索的工具，类比、组合或通过“两句测试”都不构成创新验证。[选题原文](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/brainstorming-research-ideas/SKILL.md)；[创造性操作原文](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/creative-thinking-for-research/SKILL.md)。

领域定位可以先读综述；在已知范围内生成候选时，先独立写下机制，再看他人提案与新增文献，随后重开一轮。保存异议、未入选候选和评分依据。未入选不等于被反驳，同一上下文扮演多种角色不等于独立评审。[参考：scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/scientific-brainstorming/SKILL.md)。

## 3. Search and synthesize

1. 从研究问题写关键词、同义词、旧术语和相邻领域术语；同时搜索支持与挑战。
2. 以综述定位领域，再回到主要方法论文、评测论文、公开代码与原始实验。
3. 对 AI/CS 优先使用适合问题的 arXiv、ACL Anthology、OpenReview、DBLP、Semantic Scholar 等；记录实际用过的来源，不虚列数据库。
4. 同时覆盖奠基工作、最近竞争工作、负结果、复现、评测批评和邻近领域。
5. 沿关键论文的参考文献和后续引用追踪；对多个标题或版本合并身份，保留版本差异。
6. 记录搜索日期、检索式、时间窗、筛选规则、访问限制和未能取得全文的论文。
7. 对“它没做 X”查正文和补充材料；只读摘要时将其标成待全文确认。
8. 搜索收敛后产出综合判断，不仅逐篇摘要：共同假设、冲突证据、未测试条件、可靠结论。

每个论文网络来源按实际访问级别记录 `metadata`、`abstract` 或 `fulltext`；本地来源使用 `local`，并用项目相对路径和 `locator` 说明实际读取范围。找到 PDF 链接或本地文件不等于读过全文。[参考：K-Dense literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/literature-review/SKILL.md)。

另保留两张覆盖收据：`来源 → 请求 → 是否调用 → 成功有结果／成功空集／失败／未运行`；`候选 ID → 身份核实 → 可读证据 → 提取完成／未覆盖 → 排除理由`。核对分配与完成的 ID，解析失败不能消失成“不相关”；模型记忆仅是待验证线索。区分检索记录、论文报告和底层研究／共享数据，避免同一证据多次计数。系统综述另需适用的筛选计数与独立资格审查，不能把普通范围探索称为完成系统综述。[参考：research-lit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/research-lit/SKILL.md)。

建议的综合表：

| Paper ID | 问题与方法 | 关键假设 | 数据/任务/预算 | 主要结果位置 | 作者限制与我们发现的限制 | 可复现资产 |
|---|---|---|---|---|---|---|
| 填实际 ID | 用具体机制表述 | 写可被违反的条件 | 未报告则写未报告 | 节、表、图或代码位置 | 分开标记两类限制 | URL、版本及访问状态 |

## 4. Build the domain map

用 [agent-domains.md](agent-domains.md) 作为可扩展起点，为本轮相关 `domain` 建立问题、方法、数据、基线和评测关系。

- `unsearched`：尚未完成针对该方向的检索。
- `partial`：已有证据，但关键来源、竞争方法或任务边界仍不完整。
- `reviewed`：已完成记录的范围与截止日期内的审查；需有可追溯 `exploration` 和 `data.last_reviewed` 日期，不是该领域全部知识已掌握。
- `stale`：已出现影响判断的新来源、版本或环境变化，需要重查。

领域覆盖与假设证据是两个轴。方向 `reviewed` 不意味着其中的想法成立；有一个成功实验也不能把全领域标为 `reviewed`。

工具中领域记录的 `status` 使用 `active`，覆盖状态放在 `data.coverage`；不要把 `reviewed` 填入领域 `status`。

在 `exploration` 中记录本轮访问的领域、检索边界、得到的结论和下一步。范围改变时保留原边界与改变理由。

## 5. Extract a research problem

从实际观察或文献证据写问题，分清工程故障、已知限制、未知机制和可推广的研究问题。

```text
Problem / 问题：在什么条件下，哪个系统出现什么失败？
Evidence / 证据：对应论文、数据、日志及具体位置是什么？
Consequence / 影响：谁受到影响，损失或知识缺口是什么？
Current explanation / 已有解释：最近工作如何处理或解释它？
Unresolved part / 未解决部分：差异在哪里，依据是什么？
Boundary / 边界：在哪些条件下它不是问题，或已被解决？
```

若只有“可能会发生”的推测，将它记录为待检查的候选问题；先做文献核验或最小诊断，再描述为已观察到的现象。

优先检查：常用评测未覆盖的条件、方法依赖的隐含前提、不同论文结论冲突、模块接口传错信息、简单方法被弱实现造成的假优势。

方法组合需要说明新增的作用机制和新预测。不要以换应用名、模块数量或复杂度代替贡献。[参考：Orchestra creative-thinking-for-research](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/creative-thinking-for-research/SKILL.md)。

### Problem-selection modules / 九模块选择台

需要战略选题或转向时按需使用下表。每行填写实际产物与证据位置；不套用固定周数、论文数或将主观风险分换算成成功概率。

| 模块 | 执行动作 | 可审查产物 |
|---|---|---|
| 1. 直觉启发 | 在干预、测量、理论／计算中找逻辑或工具机会；试系统化、技术限制、缺失能力、动态过程、新坐标、平台、预期现象缺席 | 问题候选及用过的启发；“没搜到论文”不算现象缺席 |
| 2. 风险与假设 | 分科学前提与技术前提，标依赖、已有证据、检验成本与得到答案的时间 | 风险表及最早有价值的 go／pivot／stop 检查 |
| 3. 价值函数 | 知识研究看学习深度与适用范围；工具看新增能力与使用条件；应用看收益及受影响对象 | 与贡献类型匹配的价值轴、依据与对照，不强求统一总分 |
| 4. 参数策略 | 区分必须保持与可变的方法／任务条件，列改变条件和代价 | 固定／浮动表；不能解除权限、预算或已冻结比较条件 |
| 5. 决策树 | 在实施与战略评估间切换，事先写观察将触发哪个动作 | 观察／阈值／下一步／资源的分支表 |
| 6. 逆境预案 | 为负结果、重复工作、资源失效及技术失败准备修复、替代和停止路径 | 失败预案及仍可获得的信息；不保证每条分支都能发表 |
| 7. 问题反演 | 解除软约束、换可比较目标、问现有结果能回答什么 | 转向理由、新问题及沿用证据范围；事后问题标 exploratory |
| 8. 整合沟通 | 合并问题、风险、计划与证据，针对读者调整解释 | 一页交接、短讲提纲与技术记录；改写不暗增机制或保证 |
| 9. 总体编排 | 根据已有产物选择入口，对实际缺口回环，检查变更的下游影响 | 阶段／输入版本／输出路径／审查者／未完成项／下一动作 |

本轮已读 [Scientific Problem Selection](https://github.com/anthropics/life-sciences/blob/e96556b637b56d6cc3a5ad33987009be9e60aa5c/scientific-problem-selection/SKILL.md) 及其九份 `references/01…09` 全文；迁移的是上述方法，生物学例子、固定时间表、主观概率分档与长期成功承诺不直接移植。原始 Cell 方法论文为 Michael A. Fischbach 独著，上游的合著归因错误不沿用。

## 6. Develop mechanisms and rivals

为每个值得推进的问题提出数量适当、机制不同的候选。独立构思后再比较，避免所有候选只是同一方案的改名版本。

| 候选解释 | 它预测什么 | 竞争解释预测什么 | 什么观察会削弱它 | 所需测量 |
|---|---|---|---|---|
| 方法确实修复目标机制 | 在目标失效条件下有特定变化 | 仅通用计算增量也能改善 | 等资源基线解释全部收益 | 任务结果、过程指标与预算 |
| 评测或数据存在偏差 | 改变评测方式后收益消失 | 真实机制在独立评测仍成立 | 无偏评测保留预测模式 | 独立标签、数据切分与误差 |

上表是诊断结构，不是预设实验结果。加入测量错误、信息泄漏、选择偏差、随机波动或其他领域合理解释。

区分“观察”“研究问题”“假设”“机制”“预测”“证据”。每个假设至少写明成立条件、可观察预测、可反驳结果和无法判断的结果。[参考：K-Dense hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md)。

标明目标属于描述、关联、预测、因果还是机制。因果目标需定义人群／系统、干预、对照、结果、时间和识别假设；每个构念说明操作化、校准、可靠性和测量限制。便利代理不自动等于构念，零假设被拒绝不自动排除所有竞争机制。

准备实现时增加方法卡：输入／输出、内部表示、学习信号或目标、训练步骤（不训练则说明）、推理信息流、已有与新增组件、评价器与真值来源、最简单替代方案。每个关键操作必须有可执行定义；将未证命题、待调参数与未定义核心操作分开。每轮修订对照 problem anchor，记录接受或拒绝评审建议的证据理由。[参考：research-refine](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/research-refine/SKILL.md)。

## 7. Check nearest prior work

对候选论点逐项比较：问题设定、机制、关键信息、使用假设、训练/推理干预、任务领域和证据。

1. 搜索最相近工作，而非只找容易区分的论文；补齐方法旧称和邻近领域叫法。
2. 将核心机制拆成可检索描述，分别查问题、机制和两者结合。
3. 读最可能构成重复的原文和必要补充；列出对方已做什么、未确定什么。
4. 判断新贡献属于方法、机制解释、理论、资源、测量、复现纠错或新的边界刻画。
5. 将“精确机制重复”“部分重叠”“任务不同但机制相近”“访问不足”分别说明。
6. 找到重复后修改研究问题或停止该候选；不要隐藏威胁论文。

输出：“截至某日期，在所列来源与检索边界内，定位到 A/B/C；剩余差异为 X，尚待核验 Y。”不写“全世界没有人做过”。

用问题设定、核心机制、关键洞见、应用范围四轴核对最近工作，优先深读机制相近和摘要含糊的候选。分别搜原问题、宽领域和机制签名，写清已定位差异与预期收益；收益尚未测量时只能写预测。四轴计数不能替代专家判断，零返回或全部访问失败不得判为“最高新颖”。[采用并修正：scoop-check](https://github.com/microsoft/ResearchStudio/blob/063f10088af49909e1a4a7ea8d29efe19633f34e/ResearchStudio-Idea/skills/scoop_check/SKILL.md)。

## 8. Assess feasibility

| 约束 | 必须核实的事实 | 可行性不足时的动作 |
|---|---|---|
| 数据与标签 | 获取方式、任务适配、权限、标注误差 | 缩小问题或使用适配的公开数据 |
| 基线与代码 | 可运行版本、依赖、评测接口 | 先复现最小基线并记录偏差 |
| 算力与 API | 实际硬件、模型限制、费用与速率 | 估算代表性运行，再设预算 |
| 信号强度 | 目标效应、噪声和独立评测单位 | 设计更有判别力的测试 |
| 依赖假设 | 哪个未经验证前提决定成败 | 先检查最关键、最便宜的前提 |
| 研究价值 | 成功、无效或反证分别能学到什么 | 重构成可回答、有信息量的问题 |

分别报告影响、技术可行性、证据成熟度和剩余风险。可以给有理由的推进优先级；不要用一个总分决定科学真假。

假设的 `data.feasibility` 分别记录 `data`、`compute`、`evaluation`、`budget`，值为 `available`、`unverified` 或 `unavailable`；在 `feasibility_notes` 写依据。四项均有可用依据并有最小实验和可推翻条件，才可进入工具中的 `testable` 状态。

## 9. Design discriminating experiments

在查看目标结果前写方案；已有数据被看过的范围必须记录。以下是研究说明模板，不是 CLI 的 JSON schema：

```text
Hypothesis IDs / 目标假设：
Primary prediction / 主要预测与适用条件：
Rival explanations / 竞争解释：
Experimental unit / 独立实验单位：
Intervention and controls / 干预、强基线、负对照：
Fixed factors / 固定模型、数据、提示、工具、预算：
Metrics and uncertainty / 主指标、过程指标、不确定性：
Data separation / 探索集、开发集、未触碰评测集：
Decision rules / 支持、反证、无法判断、停止条件：
Budget and artifacts / 费用、运行上限、配置和原始结果路径：
```

- 性能论点需要公平比较；机制论点还需能区分替代解释的干预和过程测量。
- 调参公平包括信息、计算和选择机会；同时报告天然成本与可比较预算下的结果。
- 多个样本来自同一任务、用户或文档时保留层级；重复生成不能自动当作独立新任务。
- 匹配比较可使用配对分析；复杂依赖考虑分层或聚类，不机械套用独立样本检验。
- 不规定所有研究都必须有某个固定样本数或随机种子数；说明精度、功效或稳定性依据。
- 合成诊断集用于隔离因素，真实任务用于检验迁移；不要互相冒充。

安排分配与运行顺序时明确随机化、分块和独立重复；配对、交叉、聚类或分层设计保留相应依赖与携带效应。多因素可选全／部分因子、筛选或响应面设计，但需核对可估计性、混杂／别名和实际参数边界；本技能未打包 DOE 排程引擎。

设计与样本量分开处理。[参考：K-Dense experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/experimental-design/SKILL.md)；[statistical-power](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/statistical-power/SKILL.md)。

先选研究目标、独立单位、设计与分析，再决定样本依据：

| 推断目标 | 所需依据 | 不能套用的捷径 |
|---|---|---|
| 检出有意义效应 | SESOI、变异／基线率、检验、α、功效与敏感性范围 | 无依据的 d=0.5 或固定种子数 |
| 固定预算／样本 | MDE 或可达到的估计精度 | 用已观测效应算“事后功效”证明充分 |
| 估计精度 | 目标区间宽度与符合单位依赖的区间方法 | 把显著性当精度 |
| 等效／非劣 | 有理由的界值与匹配分析 | 不显著即等效，或直接套优效检验功效 |
| 序贯／多重比较 | 预定查看／停止与多重性方案 | 反复看结果至显著才停 |

复杂聚类、配对、多层或失败过程可以按合理数据生成假设做功效模拟；必须使用计划中的分析、先检查零效应下的错误率，报告拟合失败与 Monte Carlo 不确定性，另列效应与模型假设的不确定性。模拟次数按估计误差和预算决定。需要专业计算时调用合适统计工具；本地记录器没有通用功效或统计推断引擎。[适用范围原文](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/statistical-power/SKILL.md)。

给每个实验块写 `问题 → 预测／竞争预测 → 比较 → 指标 → 优先级／依赖 → 预算 → 计划图表`。组件删除／替换、参数敏感性和设计替代分开；删组件若同时改变信息或计算，要解释混杂。[参考：ablation-planner](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/ablation-planner/SKILL.md)。

实质执行前检查 `方法卡 → 计划 → 实际代码 → metric 调用 → reference labels` 的对应，先做授权范围内的廉价 sanity 检查；确认运行脚本真的实现比较，而非输出常量或只读取已有答案。冻结、预算、运行与导入的实际命令依 [experiments.md](experiments.md)，不把一份写好的实验方案叫已执行。[参考：experiment-bridge](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/experiment-bridge/SKILL.md)。

## 10. Interpret results

先检查运行是否有效、标签与切分是否正确，再解释结果。保留原始输出、配置、版本、失败运行、排除理由和计划变更。

按主要预测与竞争预测比较结果，同时报告效应大小、不确定性、资源与失败分布。不要只记录最优随机种子、显著子集或漂亮案例。

**把区间判决写成有方向的条件。** 先定义效应的正负、比较对象、预先规定的界值以及有效区间方法。例如正向收益 `Δ = 基线损失 − 候选损失`，实际优越性要求 `Δ > δ`、`δ > 0`，区间为 `[L,U]`：

- `L > δ`：整个区间在目标收益以上；在该设计与区间方法的适用范围内支持达到预定实际效果。
- `U < δ`：整个区间低于目标；限制“达到该最小效果”的主张，不能直接宣布整个机制无效。若仍为正向区间，可以有较小改善。
- `L ≤ δ ≤ U`：区间包含界值，不能区分是否超过它；等于界值的端点也不满足严格的 `L > δ`。
- `U < 0`：区间整体为负，支持该比较方向的不利结果；先确认有效性，再限制对应的正向预测。

不能只写“区间排除δ”：完全高于δ和完全低于δ都会排除它，决策恰好不同。上述分支表达区间相对阈值的位置，不验证区间算法、样本独立性或因果识别。等效需要核对预定的两侧界值；非劣按其有方向的单侧界值处理，不复用这张优越性表。设计时用位于阈值上方、下方、跨越、负向和恰好碰界的示例检查规则。

将结果归为支持当前范围、挑战假设、无法判断或运行无效。运行失败首先是工程证据；只有与假设定义直接相关时才构成反证。

探索后发现的新模式可产生新假设，但需标明事后发现，并用未参与设计的数据或复验检验。更多同分布调参运行不自动构成独立支持。

## 11. Construct the paper argument

采用 [evidence-and-claims.md](evidence-and-claims.md) 的论点—证据契约，为每条主要结论链接结果与最相关文献。

将论文组织为：重要问题 → 现有答案的具体不足 → 要检验的主张 → 方法与公平比较 → 结果 → 可支持的解释及边界。

给严厉审稿人明确任务：找到最可能改变结论的漏洞，指出证据位置、替代解释、后果和最小修补实验。批评要可操作，不以尖刻措辞代替审查。

如果缺少决定性证据，缩小论点或补实验；保留主要负结果。论文不能比实际证据覆盖更大的任务、模型、人群或因果范围。

### Audit workbench / 逐项审计台

先冻结审计对象清单：稿件、计划、代码、结果、引用来源的路径／版本／哈希，以及审查者和实际读取范围。分别执行以下检查，不让一种通过替代另一种：

| 检查层 | 逐项动作 | 必须留下的证据 |
|---|---|---|
| 运行完整性 | 查看计划、退出状态、失败与原始日志；运行适用的结构／哈希检查 | 验证报告与未完成 attempt；不推出科学正确 |
| 实现忠实度 | 追踪GT来源、预测依赖归一化、metric函数实际调用、评价范围／类型 | 文件与代码位置、数据链及尚未解释的偏差 |
| 数字／论文论点 | 每个数字或比较定位到文件＋字段，核对单位、舍入、best/mean/median、样本／run数、配置及相对差计算 | claim occurrence → 原值／计算 → 显示值 → 匹配／不符／缺失／无法解析 |
| 引用语境 | 每个 citation occurrence 检查来源存在、元数据身份、相邻句是否由实际读到的段落支持 | 稿件位置、引用键、来源位置、支持／部分／矛盾／未核实及修正动作 |

数值机械核对只能确认指定字段与计算关系；上下文、因果、机制和范围仍由研究者解释。找不到字段、不能解析与虚构是不同结论。哈希通过不表示论文中的 1.0 是实际准确率，DOI 存在不表示它支持引用句。[result-to-claim](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/result-to-claim/SKILL.md)；[experiment-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/experiment-audit/SKILL.md)。

结构化 JSON 数值可用 `python <SKILL>/scripts/audit.py --root <PROJECT> values --ledger values.json` 按显式 JSON Pointer 与容差核对，并可核对预期 SHA-256。它不自动抽取稿件数字、不计算任意聚合或相对改进、不解释 stdout；这些仍要真实读取并记录计算过程。

问题报告统一记录 `对象／位置、观察、对论点的后果、不确定性、严重性、最小修复、复查结果`。保持反驳标准一致；未报告某步骤不等于确认它没做。发现实质证据缺陷后可以继续探索和修复，相关肯定论点保持未支持或缩小范围，不得仅凭其他检查 PASS 升级。[paper-claim-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/paper-claim-audit/SKILL.md)；[citation-audit](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/43a5daf6f8a2db7b87b48cb51d45c6ddb3c9a6d3/skills/citation-audit/SKILL.md)。

报告完整性、单项结果的偏倚风险与一组证据的确定性是不同问题。GRADE、RoB 等只在适用研究类型、结果单位和版本明确时采用；不把医学证据层级或清单分数机械套到 Agent benchmark。[参考：scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/593377bb048752abb0152deab9fbb1083a6087df/skills/scientific-critical-thinking/SKILL.md)。

核心机制、数据、指标、稿件主张或来源改变时，将相关审计标为待复查，重新读取变更影响；标题微调只需相应呈现检查。保留旧输入、审查和修改理由，不复用不匹配版本的好评。阶段完成应有实际文件与评审记录，标题或 `done` 不能代替证据。[参考：idea-spark](https://github.com/microsoft/ResearchStudio/blob/063f10088af49909e1a4a7ea8d29efe19633f34e/ResearchStudio-Idea/skills/idea_spark/SKILL.md)。

## 12. Decide the next action

每轮形成 `decision`：推进、修改、补查、追加判别实验、暂存或停止，并连接受影响记录。

下一步优先解决会改变决策的不确定性。资源已耗尽、问题已被近邻工作回答、结果无法区分解释或达到本轮交付范围时，保存状态并结束该轮。

对失败方向保存原因和重启条件；重新出现相同问题时先读取历史。每轮汇报已核实内容、未解决问题、剩余预算与最有信息量的下一步。

续接时优先读失败／冲突／未测试的当前链，再读一般背景；报告实际产物路径、图谱 revision、审计覆盖版本和缺口。定期复查只是方法建议，不自动创建日程或后台执行。需要复现时给实际命令、环境／输入版本、预算和预期记录形状，独立执行者应能从这些文件开始。

脚本只检查记录结构、引用关系和声明完整性。是否值得继续、证据是否可信、是否构成贡献仍需科研判断；任何状态都不保证 SCI、顶会或顶刊发表。
