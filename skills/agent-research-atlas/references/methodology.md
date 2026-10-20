# Research methodology / 科研方法

Reviewed: 2026-10-20

这份文档是对已审查的关键上游 SKILL.md、README 与方法论文的原创综合；不代表逐个阅读了上游仓库的全部文件，也不代表已经验证该流程能提高论文录用率。按实际问题选择方法，保留失败、反证和未完成的调查。

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
- 使用项目根参数 `--root PROJECT`；状态保存在 `PROJECT/research-atlas/atlas.json`。
- 复用已有记录和决策，再补新证据；避免每次从零搜索同一批论文。
- 本轮可以只完成一个领域切片、一个问题或一项判别实验。未探索方向保持可见。
- 输出语言跟随用户；默认用中文解释研究决策，关键术语附英文，英文论文内容使用英文。

选题时分别问“回答后有何知识价值”和“我们如何获得可信答案”。两者都需要具体理由，不能用会议名替代价值判断。[方法依据：Scientific Problem Selection](https://github.com/anthropics/life-sciences/blob/main/scientific-problem-selection/SKILL.md)。

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

设计视角可从问题优先、抽象层级、边界、简洁基线和结构类比中选择两三种；不强迫每个项目跑完所有方法。[参考：Orchestra research ideation](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/brainstorming-research-ideas/SKILL.md)。

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

## 6. Develop mechanisms and rivals

为每个值得推进的问题提出数量适当、机制不同的候选。独立构思后再比较，避免所有候选只是同一方案的改名版本。

| 候选解释 | 它预测什么 | 竞争解释预测什么 | 什么观察会削弱它 | 所需测量 |
|---|---|---|---|---|
| 方法确实修复目标机制 | 在目标失效条件下有特定变化 | 仅通用计算增量也能改善 | 等资源基线解释全部收益 | 任务结果、过程指标与预算 |
| 评测或数据存在偏差 | 改变评测方式后收益消失 | 真实机制在独立评测仍成立 | 无偏评测保留预测模式 | 独立标签、数据切分与误差 |

上表是诊断结构，不是预设实验结果。加入测量错误、信息泄漏、选择偏差、随机波动或其他领域合理解释。

区分“观察”“研究问题”“假设”“机制”“预测”“证据”。每个假设至少写明成立条件、可观察预测、可反驳结果和无法判断的结果。[参考：K-Dense hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md)。

## 7. Check nearest prior work

对候选论点逐项比较：问题设定、机制、关键信息、使用假设、训练/推理干预、任务领域和证据。

1. 搜索最相近工作，而非只找容易区分的论文；补齐方法旧称和邻近领域叫法。
2. 将核心机制拆成可检索描述，分别查问题、机制和两者结合。
3. 读最可能构成重复的原文和必要补充；列出对方已做什么、未确定什么。
4. 判断新贡献属于方法、机制解释、理论、资源、测量、复现纠错或新的边界刻画。
5. 将“精确机制重复”“部分重叠”“任务不同但机制相近”“访问不足”分别说明。
6. 找到重复后修改研究问题或停止该候选；不要隐藏威胁论文。

输出：“截至某日期，在所列来源与检索边界内，定位到 A/B/C；剩余差异为 X，尚待核验 Y。”不写“全世界没有人做过”。

这一查新结构参考 [ResearchStudio-Idea](https://arxiv.org/abs/2607.04439) 对问题与机制碰撞的审查；其论文的 idea-stage 自动评审结果不能换算成录用概率。

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

设计与样本量分开处理。[参考：K-Dense experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/experimental-design/SKILL.md)；[statistical-power](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/statistical-power/SKILL.md)。

## 10. Interpret results

先检查运行是否有效、标签与切分是否正确，再解释结果。保留原始输出、配置、版本、失败运行、排除理由和计划变更。

按主要预测与竞争预测比较结果，同时报告效应大小、不确定性、资源与失败分布。不要只记录最优随机种子、显著子集或漂亮案例。

将结果归为支持当前范围、挑战假设、无法判断或运行无效。运行失败首先是工程证据；只有与假设定义直接相关时才构成反证。

探索后发现的新模式可产生新假设，但需标明事后发现，并用未参与设计的数据或复验检验。更多同分布调参运行不自动构成独立支持。

## 11. Construct the paper argument

采用 [evidence-and-claims.md](evidence-and-claims.md) 的论点—证据契约，为每条主要结论链接结果与最相关文献。

将论文组织为：重要问题 → 现有答案的具体不足 → 要检验的主张 → 方法与公平比较 → 结果 → 可支持的解释及边界。

给严厉审稿人明确任务：找到最可能改变结论的漏洞，指出证据位置、替代解释、后果和最小修补实验。批评要可操作，不以尖刻措辞代替审查。

如果缺少决定性证据，缩小论点或补实验；保留主要负结果。论文不能比实际证据覆盖更大的任务、模型、人群或因果范围。

## 12. Decide the next action

每轮形成 `decision`：推进、修改、补查、追加判别实验、暂存或停止，并连接受影响记录。

下一步优先解决会改变决策的不确定性。资源已耗尽、问题已被近邻工作回答、结果无法区分解释或达到本轮交付范围时，保存状态并结束该轮。

对失败方向保存原因和重启条件；重新出现相同问题时先读取历史。每轮汇报已核实内容、未解决问题、剩余预算与最有信息量的下一步。

脚本只检查记录结构、引用关系和声明完整性。是否值得继续、证据是否可信、是否构成贡献仍需科研判断；任何状态都不保证 SCI、顶会或顶刊发表。
