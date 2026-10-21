# Supervisor-Skills 正文审查 A：选题、深度调研与科研协作

**结论：优先集成能改变下一步研究决定的细节，不叠加评分框架或自我认证。** 最值得补齐的是活前提审计、实践失败形式化、从排除池反查检索盲区、按条件处理文献冲突，以及长期问题的解锁记录。Atlas已有证据、可行性、反证、冻结与持久化契约保持共同底座。

固定上游版本：`a20d76ef3979b804d7dbf599d577826957e0a8a9`。全文读取3个技能主文件、23个references、6个指定手册，共32份Markdown；另读根LICENSE。没有运行上游脚本、安装、发布或修改Atlas主仓库。

## 1. 阅读与集成边界

对照Atlas主SKILL、方法/证据/双语检索/扩展协议、实验记录相关章节，以及C01–C24、全部冲突契约和相关来源条目。不是重新读完Atlas背后的65个上游来源；没有推测C25–C28。

根LICENSE为CC BY-NC-SA 4.0，署名Yuyu Luo（methodology）和贡献者；Vibe手册分享人李伯岩。部分SKILL frontmatter却标CC-BY-4.0。候选方法改编按较严格根许可单独标 **CC BY-NC-SA 4.0**、归因并注明修改；不据不一致的frontmatter改为MIT，现有核心MIT内容未被本组改动。

**优先级：** 先做IE05/IE06/DR02/DR04，它们能直接形成新问题或区分实验；再补IE02/IE03/IE04的投入判断；最后按需加长期问题、实现/图形/写作交接。每个工作单必须指出它改变哪个决定，已解决的问题不为了填表重新调查。

## 2. 逐技能对照

所有建议均为 `review_only_not_applied`。`proposed_status` 是未来registry建议采用方式，不能表述为本组已经实现或证实有效。

### idea-evaluator

该技能及全部references共12份，已全文读。

#### SUP-A-IE01 · 按贡献与实际方法选择评价标准

**映射 / 建议状态：** C08, C12, C21 / `protocol`。

**改变的决定：** 同一个 Agent 课题可以需要公平算法比较、行为测量或形式证明，评价标准不可混用。

**现有互补与缺口：** 已有贡献类型与方法路由；可加简短入口，防止把 Agent 用户研究、理论、测量和算法全部按效果增益打分。

**补齐：** 声明主贡献、实际研究方法和所需证据；混合项目的子论点分别路由。

**保留：** 按方法和核心贡献分类，而非部门名称。

**拒绝或收紧：** 不把五维评分、是否有外部商业受益者或是否发明新算法作为所有研究的准入条件。

**落地步骤：**

1. 复用 problem anchor，说明贡献类型。
2. 列证据要求与最危险替代解释，选择适用方法。

**产物：** contribution_type / method_family / evidence_needed 说明；不是现有 schema 新必填字段。

**现有归属：** `references/methodology.md §2/5/6`；`references/evidence-and-claims.md §5/8`

**互补来源：** `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION`, `SRC-KDENSE-HYPOTHESIS-GENERATION`

**精确上游定位：**

- [skills/idea-evaluator/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/SKILL.md)，§ Step 1: First impression（标题行 58）。
- [skills/idea-evaluator/references/domain-evaluation-frameworks.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/domain-evaluation-frameworks.md)，§ 5. Choosing the framework（标题行 147）。
- [handbook/01_Preliminary/1.1_如何评价一篇论文的质量.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/01_Preliminary/1.1_%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E4%B8%80%E7%AF%87%E8%AE%BA%E6%96%87%E7%9A%84%E8%B4%A8%E9%87%8F.md)，§ 从审稿的角度来评价（标题行 13）。

#### SUP-A-IE02 · 投入前检查阻断项，负结果先做有效性分诊

**映射 / 建议状态：** C06, C08, C11, C18, C19 / `protocol`。

**改变的决定：** 既防止带致命依赖大投入，也避免把坏运行误判成机制被科学推翻。

**现有互补与缺口：** 已有批判和资源检查；可把决定性风险提前成表。上游输给基线即锁定 Reject，会误判实现错误、测量缺陷或低精度结果。

**补齐：** 按证据、受影响主张、有效性、最小补救和下一动作处理；限制肯定主张但允许必要诊断。

**保留：** 先查近邻覆盖、不可测主张、不可得资源、范围膨胀、错误归因；不以乐观叙事冲淡有效负结果。

**拒绝或收紧：** 拒绝一次落后即永久否定、跳过完整性检查、最多两项问题、两项 MAJOR 自动 CRITICAL、按修复周数定科学严重性；不把旧基线或某年度SOTA当通用判据。

**落地步骤：**

1. 建立有来源的阻断项记录并按决策影响排序。
2. 先检查实现、测量、公平预算与不确定性，再解释负结果。
3. 资源不足记 parked；有效反证限制确切版本；新机制另建版本，保留失败。

**产物：** blocker review / decision 节点，连接 claim、experiment、source ID。

**现有归属：** `references/methodology.md §8/10/11/12`；`references/evidence-and-claims.md §4/7`

**互补来源：** `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`, `SRC-ARIS-RESULT-TO-CLAIM`, `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION`

**精确上游定位：**

- [skills/idea-evaluator/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/SKILL.md)，§ Step 2: Fatal-flaws（标题行 80）。
- [skills/idea-evaluator/references/fatal-flaws.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/fatal-flaws.md)，§ 5. Severity escalation（标题行 175）。
- [skills/idea-evaluator/references/fatal-flaws.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/fatal-flaws.md)，§ 6. The data-refuted mechanism（标题行 195）。

#### SUP-A-IE03 · 将五个改善方向转换为取舍和归因检查

**映射 / 建议状态：** C08, C10, C13, C17, C18 / `protocol`。

**改变的决定：** 路由更快但更容易误判时，判断真实取舍，不能用多个主观高分掩盖副作用。

**现有互补与缺口：** Atlas 已有质量/成本取舍和消融。新增可用的是一个找切口的菜单，不需再建打分器。

**补齐：** 只选相关轴，分别列基线、单位、预测、实测、附加资源和归因检查。

**保留：** 质量、速度、鲁棒性、数据/部署成本、迁移范围；检查收益是否其实来自路由、强基模、后处理或选择样本。

**拒绝或收紧：** 不采用默认5分、两维8分即 Strong Accept、3倍提速等通用阈值；未测机制可值得测试，但不能写成已测收益。

**落地步骤：**

1. 从失败/成本记录选主要轴，相关副作用作为约束。
2. 用等资源简单基线及移除/替换检查隔离机制。
3. 按实际效应与不确定性决策；偏好分数只能表示权重，不能表示录用概率。

**产物：** 改善轴—基线—预测/实测—代价—归因表。

**现有归属：** `references/methodology.md §2/6/9`；`references/evidence-and-claims.md §5/8`

**互补来源：** `SRC-ORCHESTRA-BRAINSTORMING-RESEARCH-IDEAS`, `SRC-ARIS-EXPERIMENT-PLAN`

**精确上游定位：**

- [skills/idea-evaluator/references/five-dimensions.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/five-dimensions.md)，§ 8. Summary table（标题行 232）。
- [skills/idea-evaluator/references/five-dimensions.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/five-dimensions.md)，§ 10. What counts as grounds（标题行 255）。
- [skills/idea-evaluator/references/five-dimensions.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/five-dimensions.md)，§ 11. Attribution discipline（标题行 284）。
- [handbook/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/02_Idea_Generation/2.2_%E6%83%B3Idea%E7%9A%84%E6%80%9D%E8%B7%AF_%E6%9B%B4%E9%AB%98%E6%9B%B4%E5%BF%AB%E6%9B%B4%E5%BC%BA.md)，§ Idea生成五维思考框架总结表（标题行 57）。

#### SUP-A-IE04 · 区分完成关键路径与竞争/平台变化风险

**映射 / 建议状态：** C08, C11, C24 / `protocol`。

**改变的决定：** 以获得可信答案的能力选题，不以研究者画像或粗略竞争倒计时替代可行性。

**现有互补与缺口：** 已有资源状态，尚可明确写执行关键路径和相关工作变化风险。上游月份、工时、GPU数未经校准，手册与reference数值也不同。

**补齐：** 按实际任务估数据、基线、实现、区分实验、分析、写作和修订的依赖与时间区间。

**保留：** 能力、兴趣、可用时间与协作影响可持续执行；可先缩小问题、核实最大依赖。

**拒绝或收紧：** 不继承固定研究生命周期、1.3倍阈值、50小时/周、四张GPU或基于这些的顶会判断。

**落地步骤：**

1. 核实任务实际资源，未知保持 unverified。
2. 安排最先能改变决定的廉价检查。
3. 写哪些近期论文、平台或资源变化会触发重新评估。

**产物：** 关键路径/依赖表；watch_conditions；暂存和重启理由。

**现有归属：** `references/methodology.md §8/12`；`references/evidence-and-claims.md §4`

**互补来源：** `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION`, `SRC-ARIS-IDEA-CREATOR`

**精确上游定位：**

- [skills/idea-evaluator/references/lifecycle-capability-matching.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/lifecycle-capability-matching.md)，§ 3. Capability self-assessment（标题行 43）。
- [skills/idea-evaluator/references/lifecycle-capability-matching.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/lifecycle-capability-matching.md)，§ 4. Matching logic（标题行 96）。
- [skills/idea-evaluator/references/lifecycle-capability-matching.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/lifecycle-capability-matching.md)，§ 5. Mismatch detection（标题行 110）。
- [handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/02_Idea_Generation/2.1_Idea%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E4%B8%8E%E8%83%BD%E5%8A%9B%E5%8C%B9%E9%85%8D.md)，§ 从学生能力特点评估（标题行 15）。

#### SUP-A-IE05 · 活前提审计：原理由、条件变化、替代系统与新预测

**映射 / 建议状态：** C07, C09, C10, C12 / `protocol`。

**改变的决定：** 将“无限上下文让检索消失”之类口号改为预算、信息、噪声条件下的可检验问题。

**现有互补与缺口：** 已有假设反演；独特增量是证明该前提现在仍被强近邻采用，并追到其历史理由，避免稻草共识。

**补齐：** 记录 live_source、original_reason、changed_condition、replacement、prediction 和 nearest_work。

**保留：** 从最终目的检查中间步骤是否必要；防假打破、过时前提和虚构可用能力。

**拒绝或收紧：** 不把暂时脱离文献构思解释为免查新；不通过 Yes 计数/分数认证范式转移。

**落地步骤：**

1. 在当前原文/代码定位仍依赖该前提的地方。
2. 区分历史理由、已变条件和思想实验。
3. 同一问题锚点下提出最小替代，与简单基线写不同预测，再查旧术语和邻域先例。

**产物：** assumption-change 卡及对应最小区分实验。

**现有归属：** `references/methodology.md §2/5/6/7`

**互补来源：** `SRC-ORCHESTRA-CREATIVE-THINKING-FOR-RESEARCH`, `SRC-ARIS-RESEARCH-REFINE`, `SRC-RESEARCHSTUDIO-SCOOP-CHECK`

**精确上游定位：**

- [skills/idea-evaluator/references/paradigm-first-principles.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-first-principles.md)，§ 2. Technique A（标题行 25）。
- [skills/idea-evaluator/references/paradigm-first-principles.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-first-principles.md)，§ 3. Technique B（标题行 51）。
- [skills/idea-evaluator/references/paradigm-first-principles.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-first-principles.md)，§ 6. Common misuses（标题行 100）。
- [handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/02_Idea_Generation/2.3_%E8%BF%9B%E9%98%B6_%E5%A6%82%E4%BD%95%E5%81%9A%E9%A2%A0%E8%A6%86%E5%BC%8F%E5%88%9B%E6%96%B0.md)，§ 1. 第一性原理（标题行 11）。

#### SUP-A-IE06 · 从实践失败与长尾样本形成可测的研究问题

**映射 / 建议状态：** C05, C06, C07, C13 / `protocol`。

**改变的决定：** 发现均值刷榜外的研究点，同时不把单例包装为普遍空白。

**现有互补与缺口：** 已有失败分析；可补失败发现来源、抽样分母、频率与后果分开记录，防benchmark均值掩盖问题。

**补齐：** 用已授权日志、公开复现或真实访谈材料分类失效，再查简单修复与已有形式化。

**保留：** 实践痛点→任务/测量→基线→研究问题；分清工程故障与机制限制。

**拒绝或收紧：** 不强制三位从业者、两年历史或10%发生率；稀有高损失也可重要；不臆测下次模型一定解决，不主动联系他人。

**落地步骤：**

1. 保留失败原件、抽样条件、分母及代表性限制。
2. 检查已知修复与最近工作，判断可推广部分。
3. 做能区分实现缺陷和机制限制的最小诊断。

**产物：** failure-to-question 表与候选任务定义。

**现有归属：** `references/methodology.md §5/9`；`references/evidence-and-claims.md §3/5`

**互补来源：** `SRC-ORCHESTRA-BRAINSTORMING-RESEARCH-IDEAS`, `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`

**精确上游定位：**

- [skills/idea-evaluator/references/paradigm-elephant.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-elephant.md)，§ 2. Technique A（标题行 24）。
- [skills/idea-evaluator/references/paradigm-elephant.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-elephant.md)，§ 3. Technique B（标题行 48）。
- [skills/idea-evaluator/references/paradigm-elephant.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-elephant.md)，§ 6. What to ignore（标题行 100）。
- [handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/02_Idea_Generation/2.3_%E8%BF%9B%E9%98%B6_%E5%A6%82%E4%BD%95%E5%81%9A%E9%A2%A0%E8%A6%86%E5%BC%8F%E5%88%9B%E6%96%B0.md)，§ 2. 寻找（标题行 18）。

#### SUP-A-IE07 · 长期问题清单通过解锁条件回到当前研究

**映射 / 建议状态：** C02, C07, C08, C11, C20 / `optional`。

**改变的决定：** 让暂时不可做保留为机会，只有前提真变时才重花资源。

**现有互补与缺口：** Atlas 已有 parked 和条件变化重启；可增加“缺哪项能力、何种证据能解锁”的轻量长期视图。

**补齐：** 复用现有 problem/decision，记重要性、旧阻碍、unlock_condition 与验证方式。

**保留：** 新论文和新能力与长期问题匹配；资源极限思想实验可揭示隐含约束。

**拒绝或收紧：** 不固定10/20个问题、70/20/10配比、半年日程，不自动安排任务；便宜token不是实际无限预算，也不自动消除检索的质量作用。

**落地步骤：**

1. 保存重要但暂无路线的问题和失败历史。
2. 指定可观察的解锁条件。
3. 新证据出现后先核实是否解除阻碍，再最小检查或继续暂存。

**产物：** 长期问题派生视图和解锁决定，不另建真源。

**现有归属：** `references/methodology.md §2/5/12`；`references/evidence-and-claims.md §4/11`

**互补来源：** `SRC-ORCHESTRA-BRAINSTORMING-RESEARCH-IDEAS`, `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION`, `SRC-ARIS-RESEARCH-WIKI`

**精确上游定位：**

- [skills/idea-evaluator/references/paradigm-technology-cycle.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-technology-cycle.md)，§ 2. Technique A（标题行 25）。
- [skills/idea-evaluator/references/paradigm-technology-cycle.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-technology-cycle.md)，§ 3. Technique B（标题行 49）。
- [skills/idea-evaluator/references/paradigm-technology-cycle.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-technology-cycle.md)，§ 6. How to tell（标题行 102）。
- [skills/idea-evaluator/references/paradigm-hamming.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-hamming.md)，§ 3. The prepared-mind practice（标题行 59）。
- [skills/idea-evaluator/references/paradigm-hamming.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-hamming.md)，§ 6. The template（标题行 104）。
- [skills/idea-evaluator/references/paradigm-shift-probe.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/references/paradigm-shift-probe.md)，§ 6. Portfolio strategy（标题行 143）。

### deep-research

该技能及全部references共8份，已全文读。

#### SUP-A-DR01 · 研究问题到检索视角的明确分工

**映射 / 建议状态：** C01, C03, C19 / `protocol`。

**改变的决定：** 确保有人检查评测有效性或邻域先例，而非所有人寻找支持。

**现有互补与缺口：** 已有双语矩阵；可加每个视角要回答的反问题及真实执行回执，避免多个代理重复搜支持文献。

**补齐：** 按需选主流、批评、相邻机制、测量、部署视角，写各自问题、语言、查询和访问结果。

**保留：** 可回答RQ约束范围，独立视角合并后查遗漏。

**拒绝或收紧：** 不固定RQ/代理数量，不因缺子代理停工；同上下文串行标自审，不称独立。

**落地步骤：**

1. 读已有RQ和边界。
2. 分配能改变决定的缺失视角，按实际工具执行。
3. 合并时保留未执行、空集、阻断和失败。

**产物：** rq-perspective-ledger，复用来源回执和paper ID。

**现有归属：** `references/methodology.md §1/3`；`references/bilingual-retrieval.md 检索矩阵 / 执行与停止`

**互补来源：** `SRC-ARIS-RESEARCH-LIT`, `SRC-KDENSE-LITERATURE-REVIEW`, `SRC-KDENSE-SCIENTIFIC-BRAINSTORMING`

**精确上游定位：**

- [skills/deep-research/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/SKILL.md)，§ Step 0: freeze（标题行 53）。
- [skills/deep-research/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/SKILL.md)，§ Phase 1: scout（标题行 78）。
- [skills/deep-research/references/search-strategy.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/search-strategy.md)，§ Keyword construction（标题行 3）。

#### SUP-A-DR02 · 从引用链、缺席方法群和排除池发现检索盲区

**映射 / 建议状态：** C03, C04, C05, C20, C23 / `protocol`。

**改变的决定：** 证据多但偏一派会触发有目标的补查；证据少不会被包装成空白。

**现有互补与缺口：** Atlas 已保留排除原因；新增是用排除池主动寻找遗漏术语、分支和错误筛选。

**补齐：** 核对共同被引但缺席的工作、完全缺失的方法群、排除结果中的新方向，定向补查。

**保留：** 覆盖失败回到具体检索单元，新证据增量更新综合。

**拒绝或收紧：** 拒绝每分支≥3篇、全部CLEAR、直到自审不再改稿作为完整性认证；不允许无预算循环。

**落地步骤：**

1. 列候选遗漏及证据。
2. 区分不相关、访问不足、同研究别版、术语偏差和真实未测条件。
3. 按预算与决策影响补查，保留未决范围。

**产物：** blind-spot follow-up表、query收据、exploration更新。

**现有归属：** `references/methodology.md §3/4/12`；`references/bilingual-retrieval.md 覆盖报告`

**互补来源：** `SRC-ARIS-RESEARCH-LIT`, `SRC-RESEARCHSTUDIO-PAPER-SEARCH`, `SRC-KDENSE-LITERATURE-REVIEW`

**精确上游定位：**

- [skills/deep-research/references/search-strategy.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/search-strategy.md)，§ Blind-spot discovery（标题行 31）。
- [skills/deep-research/references/quality-gates.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/quality-gates.md)，§ Coverage（标题行 28）。
- [skills/deep-research/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/SKILL.md)，§ The six gates（标题行 123）。

#### SUP-A-DR03 · 引用存在性与引用句含义分别核验

**映射 / 建议状态：** C04, C05, C06, C21 / `protocol`。

**改变的决定：** 阻止论文存在被等同于支持当前句子。

**现有互补与缺口：** Atlas已有更强读取深度/逐句审计；上游title/abstract匹配不能验证方法、统计或“对方没做”之类具体结论。

**补齐：** 核稳定身份，再把引用句映射到实际读到的位置；存在、访问、含义分开判断。

**保留：** 未核实来源不能支撑结论；发现误引要重审依赖判断。

**拒绝或收紧：** 不把摘要符合当全文检查，不把暂时访问失败当伪造；待查线索留历史，不进入正式论证；不沿用禁DOI/URL。

**落地步骤：**

1. 确认身份和版本。
2. 按句子需要读摘要/正文/附录并记录真实范围。
3. 待核/blocked留工作清单，正式引用只表达已支持范围。

**产物：** citation occurrence→locator→支持/部分/冲突/未核实→动作表。

**现有归属：** `references/evidence-and-claims.md §2/3/11`；`references/methodology.md §11`

**互补来源：** `SRC-ARIS-CITATION-AUDIT`, `SRC-KDENSE-LITERATURE-REVIEW`, `SRC-ARIS-RESEARCH-LIT`

**精确上游定位：**

- [skills/deep-research/references/citation-protocol.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/citation-protocol.md)，§ Two-step verification（标题行 3）。
- [skills/deep-research/references/citation-protocol.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/citation-protocol.md)，§ Five-grade verdict（标题行 19）。
- [skills/deep-research/references/citation-protocol.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/citation-protocol.md)，§ Grey zone（标题行 29）。
- [skills/deep-research/references/quality-gates.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/quality-gates.md)，§ Citation（标题行 43）。

#### SUP-A-DR04 · 按条件与争议综合，产生可裁决的新问题

**映射 / 建议状态：** C01, C05, C06, C18, C21 / `protocol`。

**改变的决定：** 把文献表面矛盾转为可验证的机制/评测问题。

**现有互补与缺口：** 已有条件抽取和关系图；可补章节结论→支持/挑战→条件差异→下一测试的工作单。

**补齐：** 使用可重叠分类与同设定比较；无法直接比较就记录原因，跨章节引用保留相同paper ID。

**保留：** finding、method signature、conditions、relations；冲突不平均掉，比较表揭示实际差异。

**拒绝或收紧：** 不强制MECE、每段两引文、一文只归一支、空格即gap；关键缺失列不得为美观删除；不同协议不能简单排分。

**落地步骤：**

1. 按RQ选分类轴并允许例外。
2. 对齐任务、信息、预算、数据、版本和度量，记录共享证据。
3. 能解释冲突则缩小条件；不能则列判别实验并保持未决。

**产物：** condition-comparison表、矛盾记录、RQ→claim/evidence映射。

**现有归属：** `references/methodology.md §3/4/6/10`；`references/evidence-and-claims.md §3/5`

**互补来源：** `SRC-KDENSE-LITERATURE-REVIEW`, `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`, `SRC-ARIS-RESULT-TO-CLAIM`

**精确上游定位：**

- [skills/deep-research/references/synthesis-framework.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/synthesis-framework.md)，§ The three-step flow（标题行 11）。
- [skills/deep-research/references/synthesis-framework.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/synthesis-framework.md)，§ Comparison-table design（标题行 79）。
- [skills/deep-research/references/synthesis-framework.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/synthesis-framework.md)，§ Presenting contradictions（标题行 91）。
- [skills/deep-research/references/synthesis-framework.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/synthesis-framework.md)，§ The per-section skeleton（标题行 109）。
- [skills/deep-research/references/output-structure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/output-structure.md)，§ 6. Taxonomy section（标题行 102）。

#### SUP-A-DR05 · 对核心结论搜反命题，允许有版本的研究问题修订

**映射 / 建议状态：** C06, C19, C20 / `protocol`。

**改变的决定：** 问题可随证据调整，同时避免不利结果后无记录换题。

**现有互补与缺口：** 已有反证评审；新增点是综合后审查brief自身和地理/语言/方法遗漏，而非只审结论措辞。

**补齐：** 检索最影响决策主张的反命题；RQ变化保存旧版、理由及下游影响。

**保留：** 有效反证导致修订；兼容视角并列；没有可定位问题时不表演自我否定。

**拒绝或收紧：** 不把冻结brief当禁止学习；真实推翻应撤回确切主张，不一律仅改条件句；不以审查票数认证。

**落地步骤：**

1. 选核心主张写反向预测并检查实际反证搜索。
2. 判断缺席视角是否改变范围。
3. 记录保留/缩小/撤回/新版本并沿C20复核下游。

**产物：** adversarial delta、brief amendment和下一最小检查。

**现有归属：** `references/methodology.md §11/12`；`references/evidence-and-claims.md §7/11`

**互补来源：** `SRC-KDENSE-SCIENTIFIC-BRAINSTORMING`, `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`, `SRC-ARIS-RESEARCH-REFINE`

**精确上游定位：**

- [skills/deep-research/references/self-adversarial.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/self-adversarial.md)，§ Three retrospective questions（标题行 7）。
- [skills/deep-research/references/self-adversarial.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/self-adversarial.md)，§ Perspective-omission check（标题行 38）。
- [skills/deep-research/references/self-adversarial.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/self-adversarial.md)，§ Concession rules（标题行 51）。

#### SUP-A-DR06 · 报告闭合研究问题，结论强度不按论文篇数决定

**映射 / 建议状态：** C06, C17, C18, C21, C24 / `protocol`。

**改变的决定：** 避免多份同源报告制造虚假强证据，也避免长报告未回答问题。

**现有互补与缺口：** Atlas已有claim类型和交接；完整综述结构可选，但上游按一两篇/多篇选弱强动词不可靠。

**补齐：** 按设计效度、直接性、独立性、精度和适用条件校准语句；正式综述逐RQ闭合，短答先给决定。

**保留：** 有范围/方法/分类/综合/未决问题的报告；不夸大也不堆模糊词。

**拒绝或收紧：** 不把篇数转为证据等级，不将无证据写无人研究；不强制所有任务长篇survey或结论最后，不禁稳定链接。

**落地步骤：**

1. 逐claim检查共享研究、测量与不确定性。
2. 对每RQ给回答或未决原因。
3. 按任务交付短结论或完整综述，保留真实覆盖、访问限制和下一检查。

**产物：** claim措辞决定；可选survey.md与RQ-answer map。

**现有归属：** `references/evidence-and-claims.md §4/5/8`；`references/methodology.md §3/10/12`

**互补来源：** `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`, `SRC-KDENSE-HYPOTHESIS-GENERATION`, `SRC-ANTHROPIC-SCIENTIFIC-PROBLEM-SELECTION`

**精确上游定位：**

- [skills/deep-research/references/hedge-calibration.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/hedge-calibration.md)，§ The ladder（标题行 9）。
- [skills/deep-research/references/quality-gates.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/quality-gates.md)，§ Calibration（标题行 70）。
- [skills/deep-research/references/output-structure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/output-structure.md)，§ 1. The survey skeleton（标题行 23）。
- [skills/deep-research/references/output-structure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/output-structure.md)，§ 10. Conclusion（标题行 141）。
- [skills/deep-research/references/output-structure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/deep-research/references/output-structure.md)，§ 11. References（标题行 148）。

### vibe-research-workflow

该技能及全部references共6份，已全文读。

#### SUP-A-VR01 · 按工作阶段分配科研协作，而非禁止AI提供研究建议

**映射 / 建议状态：** C07, C12, C19, C22, C24 / `protocol`。

**改变的决定：** 允许实质科研协作，同时看得清哪些仅是建议、哪些得到证据支持。

**现有互补与缺口：** Atlas目标包含自主发现观点/实验设计；照搬实验室禁AI关键判断会与用户目标冲突。

**补齐：** 分开AI候选、真实证据和采纳决定；每项任务写输入、产物与核验责任。

**保留：** 正式研究主张须能解释且有证据，不能编造实验或引用。

**拒绝或收紧：** 不导入禁AI提出问题/设计/判断的普遍规定，不每轮复述规则和索取确认；组内规范不是全学界政策。

**落地步骤：**

1. 依据当前未决问题选择检索、实现、作图或写作任务。
2. 明确输入版本与可核验成功条件。
3. 在授权内完成并保留建议/采纳理由；正式用途核实真实政策。

**产物：** session work card；proposal/evidence/decision分离。

**现有归属：** `SKILL.md Research loop / Tools`；`references/methodology.md §6/12`

**互补来源：** `SRC-ARIS-RESEARCH-REFINE`, `SRC-KDENSE-SCIENTIFIC-BRAINSTORMING`

**精确上游定位：**

- [skills/vibe-research-workflow/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/SKILL.md)，§ When NOT to use（标题行 53）。
- [skills/vibe-research-workflow/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/SKILL.md)，§ Step 1: Phase classification（标题行 72）。
- [skills/vibe-research-workflow/references/behavior-guidelines.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/behavior-guidelines.md)，§ 3. Rule 2（标题行 41）。
- [handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/05_Vibe_Research/5.1_Vibe_Research%E4%B8%8EVibe_Coding%E5%85%A5%E9%97%A8.md)，§ 行为准则（标题行 17）。

#### SUP-A-VR02 · 最小功能单元必须对应研究机制和评价器

**映射 / 建议状态：** C12, C13, C15, C16 / `protocol`。

**改变的决定：** 及早发现代码实现错问题、读取标签或没有调用目标度量。

**现有互补与缺口：** 已有运行/冻结契约；可把小步交付具体落实为方法语义检查，避免exit0被误作有效实验。

**补齐：** 每个改变说明I/O、假设、约束、最小对照和结果位置；先实现最有信息量单元。

**保留：** 明确需求、精确报错上下文、小步验证、可回滚版本。

**拒绝或收紧：** 不要求每个可逆改动先批准，不固定三次失败，不自动push；编译/单测通过不等于科学有效。

**落地步骤：**

1. 按方法卡拆出新增操作和评价器边界。
2. 实现并核验关键单元，保存命令/输入/错误。
3. 修补无新信息时重规划；评价器和GT保持冻结，方案变更新ID。

**产物：** method→unit→code→metric对应和真实run记录。

**现有归属：** `references/methodology.md §6/9/11`；`references/experiments.md`

**互补来源：** `SRC-ARIS-EXPERIMENT-BRIDGE`, `SRC-ARIS-RESEARCH-REFINE`, `SRC-RESEARCHSTUDIO-IDEA-SPARK`

**精确上游定位：**

- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 3. Technique 1（标题行 46）。
- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 4. Technique 2（标题行 63）。
- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 5. Technique 3（标题行 90）。
- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 7. Technique 5（标题行 127）。
- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 8. Technique 6（标题行 140）。

#### SUP-A-VR03 · 会话切换交接最小研究上下文

**映射 / 建议状态：** C02, C20, C24 / `protocol`。

**改变的决定：** 减少重复失败实验和旧结论被误复用。

**现有互补与缺口：** Atlas持久化比开新聊天更完整；可明确阶段上下文包，防压缩后丢失败和限制。

**补齐：** 从同一atlas选择anchor、方案版本、失败、未决问题、冻结输入、剩余预算与下一动作。

**保留：** 减少无关上下文，调试提供精确命令与报错，遗忘时恢复原材料。

**拒绝或收紧：** 不以摘要代替原始证据，不因新会话丢历史，不把全部仓库/上游技能灌入上下文。

**落地步骤：**

1. 切换前保存revision与相关ID。
2. 下轮先读失败、变更、pending review，再加载相关源。
3. 新结果回同一图谱，避免第二真源。

**产物：** 最小续接包和当前版本引用。

**现有归属：** `SKILL.md Begin with the existing project / Minimum handoff`；`references/methodology.md §12`；`references/evidence-and-claims.md §11`

**互补来源：** `SRC-ARIS-RESEARCH-WIKI`, `SRC-ARIS-RESEARCH-REFINE`

**精确上游定位：**

- [skills/vibe-research-workflow/references/vibe-coding.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-coding.md)，§ 6. Technique 4（标题行 104）。
- [handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/05_Vibe_Research/5.1_Vibe_Research%E4%B8%8EVibe_Coding%E5%85%A5%E9%97%A8.md)，§ 技法（可以利用的技巧）（标题行 131）。

#### SUP-A-VR04 · 图形先说明论点和证据类型，再选择制作路线

**映射 / 建议状态：** C16, C21, C22 / `optional`。

**改变的决定：** 让图真正支持论证而非取代证据，也不强加无用手工流程。

**现有互补与缺口：** C21有claim–figure–run，但概念图、方法结构图、结果图的生产路线尚可区分；详细图形技能由其他组审。

**补齐：** 数据图用真实结果与可再生脚本；结构图核对实体/箭头/标签；概念图声明假设关系。

**保留：** 先布局后精修；最终按目标尺寸检查视觉与证据。

**拒绝或收紧：** 不继承所有最终图必须手绘、AI不能可编辑矢量、PNG不能投稿或PDF/SVG一定纯矢量的断言。

**落地步骤：**

1. figure ID连接claim/run或明确假设。
2. 用实际可用工具制作；不让生图补测量。
3. 核对标签、误差、缩放、图注、版本；必要变化触发下游复核。

**产物：** figure purpose/type/source/version card；源文件/脚本和预览。

**现有归属：** `references/evidence-and-claims.md §8/10`；`references/methodology.md §11`

**互补来源：** `SRC-ARIS-PAPER-CLAIM-AUDIT`, `SRC-ARIS-RESULT-TO-CLAIM`

**精确上游定位：**

- [skills/vibe-research-workflow/references/vibe-figure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-figure.md)，§ 2. Step 1（标题行 23）。
- [skills/vibe-research-workflow/references/vibe-figure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-figure.md)，§ 4. Step 3（标题行 69）。
- [skills/vibe-research-workflow/references/vibe-figure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-figure.md)，§ 5. Step 4（标题行 85）。
- [skills/vibe-research-workflow/references/vibe-figure.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-figure.md)，§ 6. What AI cannot do（标题行 105）。

#### SUP-A-VR05 · 写作审查科学含义、数据和真实引用

**映射 / 建议状态：** C05, C18, C20, C21 / `protocol`。

**改变的决定：** 保持研究表达忠实，不把去AI腔替代研究核验。

**现有互补与缺口：** 已有逐句/数字审计；上游新主技能允许起草而旧reference仍禁直接AI文本，禁词无法检查科研真实性。

**补齐：** 以作者意图、证据、语义改动为对象，科学含义变动单列并回证据；具体正式政策另核实。

**保留：** 完整上下文、逐句含义和引用核验；不补造缺失结果或掩盖来源。

**拒绝或收紧：** 不因破折号、词表或AI率判不端，不强迫无意义重写，不禁止AI检索得到的真实来源；摘要不认证全部正文。

**落地步骤：**

1. 从claim card和已读来源组织草稿。
2. 核对是否扩大范围、因果、显著性或成本优势。
3. 结果/来源变化使相关文字待复核，按正式用途记录必要披露。

**产物：** 段落→claim/source表、含义变更表和引用审计。

**现有归属：** `references/evidence-and-claims.md §8/11`；`references/methodology.md §11`

**互补来源：** `SRC-ARIS-CITATION-AUDIT`, `SRC-ARIS-PAPER-CLAIM-AUDIT`, `SRC-ARIS-RESULT-TO-CLAIM`

**精确上游定位：**

- [skills/vibe-research-workflow/references/vibe-writing.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-writing.md)，§ 1. The resolved contradiction（标题行 12）。
- [skills/vibe-research-workflow/references/vibe-writing.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-writing.md)，§ 2. Red-line rules（标题行 31）。
- [skills/vibe-research-workflow/references/vibe-writing.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/vibe-writing.md)，§ 3. Recommended flow（标题行 50）。
- [skills/vibe-research-workflow/references/behavior-guidelines.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/behavior-guidelines.md)，§ 5. Rule 4（标题行 72）。
- [skills/vibe-research-workflow/references/behavior-guidelines.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/behavior-guidelines.md)，§ 7. Rule 6（标题行 105）。

#### SUP-A-VR06 · 区分真实能力、核验与声明，不沿用固定工具和自认证

**映射 / 建议状态：** C06, C11, C16, C19, C22, C23, C24 / `protocol`。

**改变的决定：** 避免工具名冒充接通能力、自我声明冒充复验。

**现有互补与缺口：** 上游工具价目/模型/代理端点和2–5倍生产率未经本次核实；inspect/attest区分有价值，但重复确认不能变成验证。

**补齐：** 按任务所需能力、实际权限、版本和预算选工具；核验分别记资产检查、操作者声明与未解决。

**保留：** 按阶段选工具，有真实回退；该技能自认是行为提醒而非验证引擎。

**拒绝或收紧：** 不复制第三方代理为默认端点，不默认付费/安装/云运行，不沿用价格/功能/效率倍数；不把用户勾选或PASS清单认证为研究正确。

**落地步骤：**

1. 盘点实际宿主工具、访问和资源边界。
2. 机械检查连接实际产物；科学解释连接证据和审查者。
3. 最终交接报告实质缺口，不为例行检查增加确认流程。

**产物：** 工具路由理由、版本/访问/成本状态；核验范围与未决事项。

**现有归属：** `SKILL.md Tools and honest fallbacks`；`references/bilingual-retrieval.md 可选适配器契约`；`references/evidence-and-claims.md §3/7/9`

**互补来源：** `SRC-ARIS-EXPERIMENT-BRIDGE`, `SRC-KDENSE-SCIENTIFIC-CRITICAL-THINKING`

**精确上游定位：**

- [skills/vibe-research-workflow/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/SKILL.md)，§ Integrity gate（标题行 130）。
- [skills/vibe-research-workflow/references/tool-selection.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/tool-selection.md)，§ 1. Selection heuristic（标题行 12）。
- [skills/vibe-research-workflow/references/tool-selection.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/tool-selection.md)，§ 5. Cost considerations（标题行 108）。
- [skills/vibe-research-workflow/references/tool-selection.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/vibe-research-workflow/references/tool-selection.md)，§ 6. Access from mainland China（标题行 127）。
- [skills/idea-evaluator/SKILL.md](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/idea-evaluator/SKILL.md)，§ Integrity gate（标题行 209）。

## 3. 必须保留的上游冲突与证据限制

### SUP-A-CF01 · License metadata

idea-evaluator/SKILL.md 与 vibe-research-workflow/SKILL.md frontmatter为CC-BY-4.0，根LICENSE为CC BY-NC-SA 4.0；deep-research标NC-SA。

**处理：** 按根的较严格条件将方法改编单独标CC BY-NC-SA 4.0，保留归因与修改说明；不据冲突声称可以改为MIT。

**来源：** `LICENSE`；`skills/idea-evaluator/SKILL.md`；`skills/vibe-research-workflow/SKILL.md`。

### SUP-A-CF02 · Severity contradiction

fatal-flaws §5 同时写两项MAJOR升级CRITICAL和两项MAJOR对应Accept with Revisions。

**处理：** 不导入该状态机；用具体证据后果与资源边界判定动作。

**来源：** `skills/idea-evaluator/references/fatal-flaws.md §5`。

### SUP-A-CF03 · Acceptance score inconsistency

主SKILL要求两维8分才Strong Accept，参考rubric强调一维8+另一维6+；回溯Alpha-SQL/AFlow只有一维8+却给Strong Accept。

**处理：** 不采用接受分数。三个案例均为已发表论文回放且无拒绝组，不能校准未来录用率。

**来源：** `skills/idea-evaluator/SKILL.md Step 4/8`；`skills/idea-evaluator/references/five-dimensions.md §7`；`skills/idea-evaluator/references/worked-examples.md §1/2/3/5`。

### SUP-A-CF04 · Hours and lifecycle

手册将低于50小时/周与发表困难联系，reference另给<10等工时分档，且GPU/月份均无校准。

**处理：** 按实际任务依赖、资源和误差估计，不用工时画像判断科研潜力。

**来源：** `handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md`；`skills/idea-evaluator/references/lifecycle-capability-matching.md §3`。

### SUP-A-CF05 · Brief freeze versus learning

deep-research主文件不许brief漂移，自审reference又允许重做brief。

**处理：** 保留锚点和旧版本，证据改变问题时明示原因和受影响计划。

**来源：** `skills/deep-research/SKILL.md Step 0`；`skills/deep-research/references/self-adversarial.md`。

### SUP-A-CF06 · Abstract / count / taxonomy overreach

具体finding以标题摘要核验、篇数映射证据等级、MECE空格即gap均可能扩大结论。

**处理：** 优先Atlas逐句源定位、设计效度/独立性、真实检索覆盖及重叠分类。

**来源：** `skills/deep-research/references/quality-gates.md`；`skills/deep-research/references/hedge-calibration.md`；`skills/deep-research/references/synthesis-framework.md`。

### SUP-A-CF07 · Vibe internal rule drift

当前主技能允许证据约束起草，旧手册/reference仍有必须手写/禁AI研究判断；手册说不必逐行看代码，reference却要求逐行。

**处理：** 按实际任务授权允许实质协作，核验关键语义和证据；具体机构/venue规定不能由该组内规则代替。

**来源：** `skills/vibe-research-workflow/SKILL.md`；`skills/vibe-research-workflow/references/behavior-guidelines.md`；`skills/vibe-research-workflow/references/vibe-writing.md`；`handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md`。

### SUP-A-CF08 · Figure / tool absolutes

必须手工最终图、AI不能矢量、PNG不能论文、PDF/SVG即矢量以及固定产品价格/生产率都是需限制的断言。

**处理：** 按可再生、可编辑、视觉和数据要求选工具；动态产品信息另查官方，不据本文推荐私人代理。

**来源：** `skills/vibe-research-workflow/references/vibe-figure.md`；`skills/vibe-research-workflow/references/tool-selection.md`。

**案例证据限制：** `worked-examples.md`明确说明是已发表论文的回溯评价，三个例子全为Strong Accept且没有拒绝组；`paradigm-examples.md`是启发叙事。本组未核原论文与历史断言，不能以这些例子证明选题评分有效、颠覆概率或发表收益。手册中的产品价格、模型能力、生产率/创业公司数字也未独立核验。

## 4. 可用于独立NC-SA方法附录的原创整合段落

以下为重新组织并加入Atlas证据与授权约束的候选文本，非上游大段复制，尚未插入主技能。应保留上游署名、固定版本与修改说明。

### SUP-A-B01 · 立项前先解决决定性未知

**映射：** C08, C11, C18。

在投入完整实现前，先列出会改变继续决定的关键未知：最近工作是否已覆盖目标、必要数据或评价器能否取得、所提机制能否与简单替代区分。给每项未知关联证据和最小检查，优先完成最便宜且最影响决定的一项。一次落后基线先检查实现、测量、预算公平和不确定性；有效负结果应限制或推翻相应版本的主张。修订机制时保留旧记录，不用新措辞把负结果变成支持。

### SUP-A-B02 · 为前提变化建立可检验卡片

**映射：** C07, C09, C10, C12。

当候选想法声称改变既有范式，先定位当前强方法仍依赖的具体前提，再记录它最初解决什么约束、今天哪项条件已经改变，以及哪些条件仍未改变。用同一问题锚点描述去掉该前提的最小系统，并写出它与简单替代会出现的不同观察。近期技术能力须实际核实；无限资源只是思想实验，不据此扩充预算或宣称可行。最后搜索旧名称和邻域先例，保留未解决重叠。

### SUP-A-B03 · 让检索盲区产生定向补查

**映射：** C03, C04, C05, C19。

围绕当前问题选择能覆盖不同未知的检索视角，分别保存实际查询、语言、来源、返回ID与访问状态。合并后检查关键论文共同引用但尚未核实的工作、完全缺席的方法或条件，以及暂未纳入结果暴露的新术语。只有可能改变判断的缺口才进入下一轮补查。分类格为空时，先区分没有检索、访问不足、命名不同和目前未找到适用研究，不能直接称为科研空白。

### SUP-A-B04 · 从文献冲突形成下一项判别实验

**映射：** C06, C13, C18, C21。

每个综合结论同时指向支持、挑战和限定范围的证据，并对齐任务、数据、可见信息、模型、预算和测量。不同条件下的结果不直接平均或排名。若条件差异能够解释冲突，将结论缩小到这些条件；若仍有竞争解释，明确什么共同设置或干预能区分它们，并把检查写入候选实验。结论力度取决于设计有效性、直接性、独立性和精度，不能用引文数量替代。

### SUP-A-B05 · 保留长期问题及其解锁条件

**映射：** C02, C08, C11, C20。

对重要但暂时不可行的问题，复用现有problem和decision，写清它为何值得回答、当前阻碍、哪些可观察变化会使它值得重启，以及已有失败和近邻工作。当新论文、数据或能力到来时，先核实它是否解除一个明确阻碍，再决定做最小检查还是继续暂存。清单长度和复查频率由任务需要决定；不自动创建日程，也不因出现新工具就重复已失败路线。

### SUP-A-B06 · 把协作任务交付为可核验的最小单元

**映射：** C12, C16, C21, C24。

每个代码、图形或写作任务都写明研究问题、输入版本、预期产物与核验方法。代码检查实际实现和评价器的对应；数据图从真实结果和可再生脚本生成；稿件句子回指已核实论点与来源。AI可以提出候选、实现和起草，正式研究主张仍须有可解释的证据和采纳理由。区分检查过的资产、操作者声明和未决事项，不以自评PASS、文风扫描或确认提示代替核验。

## 5. 对新 supervisor-discovery.md 的复核

已全文阅读主代理新增草稿，主要方法及关键冲突已处理得当，只建议补充以下三个小点：

- §4: Require evidence that the premise is still used by current strongest neighboring work, not only a historical source.
- §4: For long-lived questions record current blocker→observable unlock condition→new-evidence-triggered minimal check, using existing problem/decision IDs.
- §3/4: Record failure sampling/denominator/frequency separately from consequence; do not inherit 10 percent or two-year thresholds.

## 6. 最小前向检验建议（未执行）

- **案例：** 首次实现输给基线，但日志显示评价器未读取新输出。 **应见行为：** 先诊断实现/测量，保留失败；不宣布机制被推翻，也不改旧冻结方案来冒充成功。 **映射：** C12, C16, C18。
- **案例：** 分类格为空，三个来源中两个超时，只有一篇相关全文。 **应见行为：** 保留失败与范围，定向补查或按预算停止；不宣布全面检索、新颖空白或凑三篇。 **映射：** C03, C06, C09。
- **案例：** 两篇Agent方法结果相反，但可见信息和调用预算不同。 **应见行为：** 按条件对齐，保留两侧证据，不给不公平总排名；提出共同条件判别实验。 **映射：** C06, C13, C18。
- **案例：** 用户请求AI提出候选机制，已有上下文和真实来源。 **应见行为：** 允许候选与可验证预测，分清建议和证据；不导入原组内全面禁AI研究判断。 **映射：** C07, C10, C19。

这些检查验证协议是否避免具体失败，不评价录用率，不把流程完成或自评分当科学认证。

## 7. 已读文件与未读资产

下表为全部32份指定Markdown。JSON同时保存固定版本URL、SHA-256和Git blob SHA-1。本组重算本地指纹；原始GitHub blob匹配由主代理此前下载核验提供，本组没有独立再拉取。

| 文件 | 阅读深度 | 行数 |
| --- | --- | --- |
| `skills/idea-evaluator/SKILL.md` | 全文 | 327 |
| `skills/idea-evaluator/references/domain-evaluation-frameworks.md` | 全文 | 162 |
| `skills/idea-evaluator/references/fatal-flaws.md` | 全文 | 217 |
| `skills/idea-evaluator/references/five-dimensions.md` | 全文 | 297 |
| `skills/idea-evaluator/references/lifecycle-capability-matching.md` | 全文 | 177 |
| `skills/idea-evaluator/references/paradigm-elephant.md` | 全文 | 112 |
| `skills/idea-evaluator/references/paradigm-examples.md` | 全文 | 107 |
| `skills/idea-evaluator/references/paradigm-first-principles.md` | 全文 | 115 |
| `skills/idea-evaluator/references/paradigm-hamming.md` | 全文 | 137 |
| `skills/idea-evaluator/references/paradigm-shift-probe.md` | 全文 | 160 |
| `skills/idea-evaluator/references/paradigm-technology-cycle.md` | 全文 | 116 |
| `skills/idea-evaluator/references/worked-examples.md` | 全文 | 206 |
| `skills/deep-research/SKILL.md` | 全文 | 209 |
| `skills/deep-research/references/citation-protocol.md` | 全文 | 52 |
| `skills/deep-research/references/hedge-calibration.md` | 全文 | 62 |
| `skills/deep-research/references/output-structure.md` | 全文 | 177 |
| `skills/deep-research/references/quality-gates.md` | 全文 | 96 |
| `skills/deep-research/references/search-strategy.md` | 全文 | 57 |
| `skills/deep-research/references/self-adversarial.md` | 全文 | 68 |
| `skills/deep-research/references/synthesis-framework.md` | 全文 | 123 |
| `skills/vibe-research-workflow/SKILL.md` | 全文 | 198 |
| `skills/vibe-research-workflow/references/behavior-guidelines.md` | 全文 | 149 |
| `skills/vibe-research-workflow/references/tool-selection.md` | 全文 | 144 |
| `skills/vibe-research-workflow/references/vibe-coding.md` | 全文 | 154 |
| `skills/vibe-research-workflow/references/vibe-figure.md` | 全文 | 131 |
| `skills/vibe-research-workflow/references/vibe-writing.md` | 全文 | 181 |
| `handbook/01_Preliminary/1.1_如何评价一篇论文的质量.md` | 全文 | 27 |
| `handbook/02_Idea_Generation/2.1_Idea的生命周期与能力匹配.md` | 全文 | 30 |
| `handbook/02_Idea_Generation/2.2_想Idea的思路_更高更快更强.md` | 全文 | 67 |
| `handbook/02_Idea_Generation/2.3_进阶_如何做颠覆式创新.md` | 全文 | 41 |
| `handbook/05_Vibe_Research/5.1_Vibe_Research与Vibe_Coding入门.md` | 全文 | 510 |
| `handbook/05_Vibe_Research/5.2_李伯岩实战经验分享与会议纪要.md` | 全文 | 156 |

另全文读取根`LICENSE`。

**未读图片：** 5.1手册引用的`assets/5.1_vibe_research/image1.png`至`image10.png`和5.2的`assets/5.2_meeting_notes/foundation_agents_vibe_research_overview.png`，共11张未视觉检查。只读周围Markdown、图像提示词和alt文本，不能声称核验了视觉内容。

**未读PDF、视频和外链：** 本组未读配套PDF讲义、会议录像及文中链接的原始论文/外部页面。其他技能和手册章节属于其他审查部分。产品、技术史、案例效果和效率数字均只视为上游文本的陈述。

**实现与效果限制：** 没有执行上游程序或真实研究效果试验。建议可使证据与决定更容易检查，不能保证候选新颖、实验支持原论点或论文获得SCI/顶会/顶刊录用。
