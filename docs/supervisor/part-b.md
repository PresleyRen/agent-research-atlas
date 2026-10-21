# Supervisor-Skills 集成审查：Part B

审查日期：2026-10-21。固定来源：[https://github.com/HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills/tree/a20d76ef3979b804d7dbf599d577826957e0a8a9)，commit a20d76ef3979b804d7dbf599d577826957e0a8a9。

## 结论与边界

建议保留并改写四条实用流程：评估/Benchmark 设计、技术论文贡献与证据映射、投稿前分层检查、逐条审稿意见回复。建议新增 C25（评估与 Benchmark）和 C27（审稿意见追踪与证据回复）；其他内容增强 C12/C13/C18/C19/C21/C24。这里的内容是宿主执行协议建议，不是已经部署的科学验证器。

本部分全文读完分配的 32 份文件，共 186,013 字符；逐文件哈希与章节位于 part-b.json。没有运行上游程序、安装服务、修改主仓库或发布。没有将案例中的原论文或 rebuttal 统计模型标成已复现。既有 Atlas 测试不能证明本次新增方法有效。

优先保留的是可追溯证据链与真实问题对应；拒绝将固定篇章数量、极端低模型正确率、心态标签、历史涨分率、Cohen’s d 阈值或模板自洽作为科学效度/录用的门槛。所有改写应复用 Atlas 已有 evidence/experiment/claim ID 和状态，不建第二套独立“真相”。

## 1. 与现有 Atlas 的互补

| 上游流程 | 已有底座 | 实际新增 | 仍不具备 |
|---|---|---|---|
| Benchmark | C09 最近工作；C13 评测；C14 冻结；C16 数值；C17 不确定性；C18 论点 | C25 的构念、分类覆盖、构建/QC、污染、难度、版本与测量贡献卡 | 自动保证标签真实、全模型评测或全面无污染 |
| Tech template | C10 假设；C12 方法卡；C18 claim card；C21 写作 | 可填逻辑骨架、多对多关系和叙述/证据双重一致性 | 靠完整表格认定机制新颖、有效或可发表 |
| Pre-submission | C19 证据批判；C21 引用；C16 原值；C20 复查 | 稿件访问manifest、呈现/语法/模板适配、可追踪问题和修复 | 未执行的编译、看不到图的视觉检查、校准录用分数 |
| Rebuttal | C19 批评；C21 写作；C11–C17 追加实验；C20 历史 | C27 原始意见→子项→行动→实际证据→修订→完整回应 | 心态识别、个体涨分预测、无证据的新实验回复或自动发送 |

## 2. 逐技能特色、采用方式和精确来源

### benchmark-paper-template

#### SUP-BENCH-01 评估盲点与已有 benchmark 比较

映射：C09, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C09 查新已有机制/目标/信息/成本对比；C06 要求原文支持批评。

缺口：缺少构念、旧指标、漏测条件、实际受影响结论的专用比较表。

集成动作：记录被测构念与旧评测假设；从真实失败案例形成可测的差异，再核查最近 benchmark，保留访问不足项；文献数量由相关性与搜索收敛决定。

产物：benchmark/landscape.csv; benchmark/gap-card.md。关联冲突：B01, B03。

来源：[skills/benchmark-paper-template/references/gap-analysis.md / Step 1: Survey the Evaluation Landscape](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/gap-analysis.md#L5); [skills/benchmark-paper-template/references/gap-analysis.md / Step 2: Identify the Blind Spot](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/gap-analysis.md#L23); [skills/benchmark-paper-template/references/gap-analysis.md / Step 3: Validate the Gap](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/gap-analysis.md#L46); [handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md / 二、Benchmark 论文的五大核心要素](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md#L26)

#### SUP-BENCH-02 Benchmark、Evaluation 与方法贡献分流

映射：C12, C21, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C12 已允许理论、方法、测量、数据与可复现经验发现；C18 按论点类型要求证据。

缺口：尚无测量贡献与方法贡献并行的产物合同。

集成动作：按主要贡献选择评估/数据/方法/新设定/混合路线；混合论文分别核验测量价值与方法效果，允许不提出新模型、不击败基线的有效评估研究。

产物：paper/contribution-map.json; benchmark/design.md。关联冲突：B01, B02。

来源：[skills/benchmark-paper-template/SKILL.md / Benchmark paper vs technical paper](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/SKILL.md#L20); [skills/benchmark-paper-template/references/orchestrator-notes.md / Core Philosophy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/orchestrator-notes.md#L5); [handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md / 一、快速定位：Benchmark/Evaluation 论文与 Technique Paper 的核心差异](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md#L7)

#### SUP-BENCH-03 任务边界、分类维度与指标效度

映射：C13, C17, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C13 已有单位、切分、对照、指标，C17 有依赖与不确定性。

缺口：需要把分类学覆盖、构念操作化、评分器一致性与偏差写成专用方案。

集成动作：使用稳定语义 goal ID；定义任务族与排除条件、分类交叉格和空格分母；校验指标与目标能力关系，人工与 LLM judge 作为可误测的评定者分别验证，不仅报告相关系数。

产物：benchmark/design.md; benchmark/coverage-matrix.csv; benchmark/judge-validation.md。关联冲突：B04, B05。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 1: Design Goals](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L16); [skills/benchmark-paper-template/references/benchmark-design.md / Element 2: Task Scope](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L29); [skills/benchmark-paper-template/references/benchmark-design.md / Element 3: Taxonomy Design](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L44); [skills/benchmark-paper-template/references/benchmark-design.md / Element 4: Evaluation Framework](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L86)

#### SUP-BENCH-04 三种数据构建范式与逐阶段质量门

映射：C11, C13, C16, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C11 核实资源，C14/C16 固定输入和原始溯源；目前没有专用数据构建卡。

缺口：逆向合成、可控注入、自适应生成与专家标注需要任务适配和独立标签核验。

集成动作：记录每步输入、操作、输出数量、执行者、成本、失败与质量门；逆向合成仍验证题目和答案，受控注入检查自然性与其他变量，专家分歧留存；QC 抽样量与阈值给依据，不能固定10%。

产物：benchmark/pipeline.md; benchmark/data-provenance.jsonl; benchmark/qc-report.md。关联冲突：B04, B06。

来源：[skills/benchmark-paper-template/references/construction-pipeline.md / Three Proven Construction Paradigms](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/construction-pipeline.md#L22); [skills/benchmark-paper-template/references/construction-pipeline.md / Pipeline Stages Specification](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/construction-pipeline.md#L67); [skills/benchmark-paper-template/references/construction-pipeline.md / Quality Control Strategies](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/construction-pipeline.md#L88)

#### SUP-BENCH-05 污染缓解、难度与可维护性

映射：C14, C20, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C14 固定评价器和数据输入；C20 保留旧版本和依赖复查。

缺口：缺少 benchmark 发布版本、污染证据及难度分布的记录。

集成动作：区分训练污染、prompt 泄漏、共享来源与评测自适应；新鲜或合成不等于无污染。按目标分布及区分能力设置难度，保留易/中/难层和饱和信息，变更数据集新版本并复查旧结论。

产物：benchmark/contamination-register.md; benchmark/version-card.md。关联冲突：B05, B07。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 6: Contamination Mitigation Strategy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L124); [skills/benchmark-paper-template/references/benchmark-design.md / Element 7: Difficulty Calibration](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L135); [skills/benchmark-paper-template/references/checklist.md / 4. Structure & Completeness Checklist](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L49)

#### SUP-BENCH-06 RQ 驱动的多维评测与诊断 Findings

映射：C13, C16, C17, C18, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C13/C16/C17/C18 已约束预算、公平、原始数字、统计与论点强度。

缺口：需要把总体表、条件分层、错误类型和 Findings 连到 RQ 与证据。

集成动作：模型选择由问题和可用资源决定；比较模型版本/信息/预算/解析/失败分母；预期 Findings 留作预测，实际结论从全部结果产生。对人类比较记录任务条件而非默认人类上界；案例选取规则可查。

产物：benchmark/evaluation-protocol.md; paper/findings-ledger.json; paper/claim-evidence-matrix.json。关联冲突：B03, B08, B09。

来源：[skills/benchmark-paper-template/references/experiments.md / 1. Baseline Model Selection](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L5); [skills/benchmark-paper-template/references/experiments.md / 2. Evaluation Protocol](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L18); [skills/benchmark-paper-template/references/experiments.md / 3. RQ-driven Experiment Structure](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L49); [skills/benchmark-paper-template/references/experiments.md / 5. The "Finding X" Pattern](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L101); [skills/benchmark-paper-template/references/experiments.md / 6. Case Study Design](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L130)

#### SUP-BENCH-07 可选配套方法及外部迁移验证

映射：C13, C14, C18, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C13 有强简单基线与消融，C14 保持最终评测冻结。

缺口：上游可能推动为论文厚度添加方法，混淆训练数据和测试集。

集成动作：仅当方法有独立科学问题与资源依据时添加；明确 train/dev/test、调参机会、可见标签与隔离评估，分别检查内部改善、跨 benchmark 迁移和机制归因。

产物：benchmark/companion-method-card.md; paper/contribution-map.json。关联冲突：B02, B08。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 5: Companion Method (Optional but Highly Recommended)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L105); [skills/benchmark-paper-template/references/experiments.md / 7. Companion Method Experiments (If Applicable)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L141); [skills/benchmark-paper-template/references/instantiation-template.md / Companion Method (Optional)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/instantiation-template.md#L86)

#### SUP-BENCH-08 可实例化写作骨架、图表计划、数据说明与投稿清单

映射：C21, C24, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C21 有论点—图表—run 和当前官方 venue 要求；C24 可交接。

缺口：缺少 benchmark 专用章节及数据卡/维护清单，当前没有自动投稿管线。

集成动作：把 Gap→设计→构建→评测→发现→局限作为可选组织；图表编号、段落数和模型数不作为科研门槛。按贡献/年份查官方投稿条件；数据、代码、说明的存在性与质量分开。

产物：paper/outline.md; paper/figure-table-plan.md; benchmark/data-card.md; paper/venue-rules.md。关联冲突：B03, B10, B11。

来源：[skills/benchmark-paper-template/references/instantiation-template.md / 1. Basic Information](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/instantiation-template.md#L16); [skills/benchmark-paper-template/references/paper-structure.md / Introduction: 6-Part Framework](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/paper-structure.md#L14); [skills/benchmark-paper-template/references/paper-structure.md / Appendix Planning](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/paper-structure.md#L201); [skills/benchmark-paper-template/references/checklist.md / 4. Structure & Completeness Checklist](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L49); [skills/benchmark-paper-template/references/checklist.md / 5. Venue-Specific Checks](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L67)

#### SUP-BENCH-09 按已有材料识别阶段并复用而非重启

映射：C02, C20, C23, C24, C25。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：Atlas 开始先 discover、读旧图和历史；C23 已有能力定位。

缺口：上游每次询问阶段且建议单独 bench-* skill 名，可能造成多余确认/不存在依赖。

集成动作：先读已有产物和 pending review，自动选择缺口步骤；只有关键事实无法推断才问。把引用的 bench-* 名解释为工作阶段，不声明已安装单独技能。

产物：paper/stage-state.json; research-atlas/atlas.json。关联冲突：B12。

来源：[skills/benchmark-paper-template/references/orchestrator-notes.md / Stage Detection & Routing](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/orchestrator-notes.md#L33); [skills/benchmark-paper-template/references/instantiation-template.md / Reference Case Studies](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/instantiation-template.md#L172)

### tech-paper-template

#### SUP-TECH-01 方法、新问题与跨领域迁移的定位

映射：C07, C12, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C07 有结构类比、C12 有贡献类型和方法卡、C09 查新。

缺口：缺少主贡献及次贡献与论文叙述主线的明确映射。

集成动作：按实际证据描述方法/设定/迁移/测量混合；迁移明确源域机制、目标域失配和新增改变，不把成熟方法换领域自动判创新。

产物：paper/contribution-map.json; paper/thinking-template.md。关联冲突：B01, B02。

来源：[skills/tech-paper-template/references/paper-types.md / 1. Three paper-type categories](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/paper-types.md#L12); [skills/tech-paper-template/references/paper-types.md / 4. Mixed case: cross-domain technique](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/paper-types.md#L71); [skills/tech-paper-template/SKILL.md / Step 1: Paper-type positioning](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L57)

#### SUP-TECH-02 背景—已证局限—核心思路—挑战—模块—贡献逻辑模板

映射：C10, C12, C18, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：Atlas 方法卡已有输入输出、学习/推理与真假来源；claim card 约束结论。

缺口：缺少作者易填的跨阶段对应表，但表格齐全不代表推论成立。

集成动作：每项局限有文献/观察；未解决局限可保留为范围限制。挑战不为模块倒造；允许多对多关系，已知必要组件不自动升级为创新贡献。

产物：paper/thinking-template.md; paper/contribution-map.json。关联冲突：B13, B14。

来源：[skills/tech-paper-template/references/thinking-template.md / 2. Cell: Research background](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L25); [skills/tech-paper-template/references/thinking-template.md / 3. Cell: Limitations 1, 2, 3](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L52); [skills/tech-paper-template/references/thinking-template.md / 4. Cell: Key Idea or Our Goal](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L78); [skills/tech-paper-template/references/thinking-template.md / 5. Cell: Challenges 1, 2, 3](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L103); [skills/tech-paper-template/references/thinking-template.md / 6. Cell: Methodology topic sentence and modules](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L130); [skills/tech-paper-template/references/thinking-template.md / 7. Cell: Contributions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L156); [handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md / 3.3 论文写作 - 技术类Full Paper思考模板（讨论用）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md#L1)

#### SUP-TECH-03 四段一致性检查与断链诊断

映射：C12, C18, C19, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C18/C19 已能检查不支持的论点和替代解释；已有证据门槛更强。

缺口：源模板仅比较叙述单元，没有强制结果位置和实现链。

集成动作：做局限→思路、思路→实施障碍、障碍→模块、模块/结果→贡献四查；增加 claim→code/metric→raw result/rival 第五查。严重度按结论后果区分，未单列段落不能自动 CRITICAL。

产物：paper/logic-audit.md; paper/claim-evidence-matrix.json。关联冲突：B08, B13, B14。

来源：[skills/tech-paper-template/references/consistency-checks.md / 2. Check 1: Limitations to Key Idea](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L23); [skills/tech-paper-template/references/consistency-checks.md / 3. Check 2: Key Idea to Challenges](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L55); [skills/tech-paper-template/references/consistency-checks.md / 4. Check 3: Challenges to Methodology](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L88); [skills/tech-paper-template/references/consistency-checks.md / 5. Check 4: Methodology to Contributions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L123)

#### SUP-TECH-04 从模板生成方法章节及交接

映射：C21, C24。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C21 允许依据真实证据组织论文，C24 有交接。

缺口：缺少从模块卡到章节开头和子节的受控转化。

集成动作：将方法卡映射至必要子节、伪代码/定义与真实评测链接；不新增未运行实验或理论保证；用户请求写稿时可继续形成草稿，无需先取得 LLM Strong Accept。

产物：paper/method-outline.md; paper/logic-audit.md。关联冲突：B12, B15。

来源：[skills/tech-paper-template/references/thinking-template.md / 8. Methodology-outline derivation](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L183); [skills/tech-paper-template/SKILL.md / Output format](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L153)

#### SUP-TECH-05 Alpha-SQL、AFlow、LEAD 写作案例

映射：C05, C07, C21。决定：reference；拟采用状态：reference（本次仅建议）。

已有互补：C05 要区分原论文、作者解释和本地推论；C09 保留源域近邻。

缺口：worked-examples 填充了案例正文未完整给出的细节，且示例数目/段落规则自相矛盾。

集成动作：只用作写作结构示例；方法细节、定量值、发表状态与引用需另查原论文。LEAD 缺截图内容保持未核实；不将 retrospective 填表变成真实作者实验记录。

产物：paper/example-reading-notes.md。关联冲突：B13, B16。

来源：[skills/tech-paper-template/references/worked-examples.md / 2. Example A: Alpha-SQL, Technique](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/worked-examples.md#L19); [skills/tech-paper-template/references/worked-examples.md / 3. Example B: AFlow, Technique with cross-domain framing](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/worked-examples.md#L52); [skills/tech-paper-template/references/worked-examples.md / 4. Example C: LEAD, New Problem/Setting](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/worked-examples.md#L82); [handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md#L42); [handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md#L35); [handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md#L35)

### pre-submission-reviewer

#### SUP-PRE-01 范式与 venue fit 校准

映射：C12, C19, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C12 已要求问题匹配方法，C21 核查当前官方 venue。

缺口：泛化到人文/法律/医学的规则不等于这些领域的验证能力。

集成动作：Agent 场景优先技术/经验/理论/测量路线；跨域仅记录方法匹配和需专业核验的缺口；当前 venue 的贡献类型、匿名、页数、数据/代码要求单独读取。

产物：paper/review-scope.json; paper/venue-rules.md。关联冲突：B10, B17。

来源：[skills/pre-submission-reviewer/SKILL.md / Step 0: paradigm and venue fit](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L53)

#### SUP-PRE-02 宏观论点、近邻与归因审查

映射：C06, C09, C13, C18, C19, C21。决定：retain；拟采用状态：protocol（本次仅建议）。

已有互补：已有查新、数值、实现、结果到论点协议；上游归因隔离直接互补。

缺口：需合并审稿发现与已有审计账本，避免维护第二套真相。

集成动作：给每个质疑确切稿件位置、证据位置、后果和修复；性能增益先检查模型/资源/路由/后处理，缺归因证据只保留比较论点；检索摘要仅定位，细节回原文。

产物：paper/review-issues.json; paper/claim-evidence-matrix.json。关联冲突：B08, B09。

来源：[skills/pre-submission-reviewer/SKILL.md / Step 1: Dimension 1 Macro logic review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L97); [skills/pre-submission-reviewer/references/logic-and-structure.md / 1. Logic First rule](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/logic-and-structure.md#L13); [skills/pre-submission-reviewer/references/forbidden-patterns.md / 4. Overclaim patterns](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L98)

#### SUP-PRE-03 段落、语法、LaTeX、图表可读性审查

映射：C19, C21, C24。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C21 目前侧重证据与引用；新增呈现层审查有用但不替代数值效度。

缺口：未内置完整 LaTeX 编译/视觉校验器；若只见源码，图表视觉仍不可判已检查。

集成动作：区分语义错误、可读性和风格；按实际可读材料说明检查范围。图表用真实数据，照片/截图可合理使用位图，绘图优先矢量；格式依模板及编译结果，不按文件扩展名一票否决。

产物：paper/editorial-review.md; paper/format-checks.md。关联冲突：B11, B17, B18。

来源：[skills/pre-submission-reviewer/SKILL.md / Step 2: Dimension 2 Writing details review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L143); [skills/pre-submission-reviewer/SKILL.md / Step 3: Dimension 3 English grammar review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L155); [skills/pre-submission-reviewer/SKILL.md / Step 4: Dimension 4 LaTeX format review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L171); [skills/pre-submission-reviewer/SKILL.md / Step 5: Dimension 5 Figure quality review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L187); [skills/pre-submission-reviewer/references/grammar-rules.md / 1. Article usage](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/grammar-rules.md#L14); [skills/pre-submission-reviewer/references/latex-rules.md / 4. Labels and references](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/latex-rules.md#L76); [skills/pre-submission-reviewer/references/forbidden-patterns.md / 3. Chartjunk patterns](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L82)

#### SUP-PRE-04 词汇/em dash 硬禁与 AI 作者推断

映射：C19, C21。决定：reject；拟采用状态：rejected（本次仅建议）。

已有互补：Atlas 写作不允许改变论点强度，用户偏好可本地适配。

缺口：普通词及标点频率没有提供可靠 AI 作者判定依据，substring 扫描会误伤术语/引文。

集成动作：不继承普遍禁词、作者身份推断或按出现次数提严重度；仅依据项目明确风格给可选建议，保留术语、引文、代码与准确不确定性。

产物：paper/style-preferences.md。关联冲突：B17, B18。

来源：[skills/pre-submission-reviewer/SKILL.md / Step 6: Banned-vocabulary and em-dash scan](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L202); [skills/pre-submission-reviewer/references/forbidden-patterns.md / 2. Banned AI-tone vocabulary](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L39); [skills/pre-submission-reviewer/references/forbidden-patterns.md / 6. Detection heuristics](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L132)

#### SUP-PRE-05 按范式选择章节内容与比较/消融

映射：C12, C13, C18, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C13 已有公平基线、因子与消融，C18 不把删除组件自动当因果。

缺口：原有定长章节、至少3数据集和从旧论文A胜B/C就省基线的规则过强。

集成动作：章节内容服务问题，不强制五句摘要或六段引言；数据/模型/基线选择给当前问题的覆盖依据。消融需匹配资源与信息，不能让排版规则改变科学设计。

产物：paper/outline.md; paper/review-issues.json。关联冲突：B03, B08, B13。

来源：[skills/pre-submission-reviewer/references/section-guides.md / 1. Abstract](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/section-guides.md#L13); [skills/pre-submission-reviewer/references/section-guides.md / 4. Framework or Methodology](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/section-guides.md#L69); [skills/pre-submission-reviewer/references/section-guides.md / 5. Experiments](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/section-guides.md#L99); [skills/pre-submission-reviewer/references/section-guides.md / 6. Related Work](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/section-guides.md#L130)

#### SUP-PRE-06 分级问题账本与有范围的完成声明

映射：C16, C19, C20, C21。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C19已有证据式质疑，C20会对变更触发复查；注册表已有协议/实现区分。

缺口：原critical包括模板偏好，9/10分数从缺陷数量推导容易产生虚假精度。

集成动作：严重度按结论有效性和当前官方要求解释；报告实际读到的文件/页面/图表，无法访问不得写全检。汇报未解决阻塞/主要/次要项，不给录用概率；用户要求修复时做已授权可逆修改。

产物：paper/review-scope.json; paper/review-issues.json; paper/review-summary.md。关联冲突：B11, B12, B19。

来源：[skills/pre-submission-reviewer/SKILL.md / Severity taxonomy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L239); [skills/pre-submission-reviewer/SKILL.md / Step 8: Integrity gate](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L231); [skills/pre-submission-reviewer/SKILL.md / Output format](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L294)

#### SUP-PRE-07 修订标记与分审稿人文件组织

映射：C20, C21, C24, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C20保存历史、C24交接；可与逐条回复共享一份review ledger。

缺口：现无稿件差异与审稿编号双向关联。

集成动作：将 R1.W1 等稳定编号连到改动位置/版本/证据；是否着色或边注遵循 venue，提交前编译和匿名检查按宿主能力执行并披露未执行。

产物：paper/review-issues.json; paper/revision-log.md; paper/response-to-reviewers.md。关联冲突：B10。

来源：[skills/pre-submission-reviewer/references/latex-rules.md / 8. Revision conventions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/latex-rules.md#L134)

### rebuttal-guidance

#### SUP-REB-01 全量审稿意见编号、拆分与分类

映射：C19, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C19 可做证据式批评，尚缺收到外部意见后的逐项闭环。

缺口：需稳定 concern ID、原文位置、复合子项和覆盖检查；不能从措辞预判审稿人错。

集成动作：按实质将澄清、缺证、查新、公平性、范围、理论、效率等分流，复合意见保留父ID/子ID；W/Q或第几段不决定严重性。依据已给的全部材料推进并注明范围。

产物：paper/review-issues.json; paper/rebuttal-coverage.md。关联冲突：B12, B20。

来源：[skills/rebuttal-guidance/SKILL.md / Step 1: Inventory concerns](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L46); [skills/rebuttal-guidance/SKILL.md / Step 2: Classify each concern](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L58); [skills/rebuttal-guidance/references/concern-classification.md / 分类表](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/concern-classification.md#L5); [skills/rebuttal-guidance/references/concern-classification.md / 复合 concern 的处理](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/concern-classification.md#L38)

#### SUP-REB-02 证据→回应→修订位置的逐条闭环

映射：C16, C18, C21, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C16 数字定位、C18 论点边界、C21 引用语境可为回复供证。

缺口：模板里的新实验/已修改句式可能越过实际执行。

集成动作：每条给直接答案、可核证据、真实改动位置、剩余限制；分别标 verified-existing/new-run/planned/unavailable。证据不能保住贡献时允许撤回该论点，不强行写仍成立。

产物：paper/rebuttal-plan.md; paper/response-to-reviewers.md; paper/revision-log.md。关联冲突：B08, B21。

来源：[skills/rebuttal-guidance/SKILL.md / Step 5: Per-concern guidance](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L89); [skills/rebuttal-guidance/references/response-templates.md / 模板 A: 澄清误解（misunderstanding / writing_clarity）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L24); [skills/rebuttal-guidance/references/response-templates.md / 模板 B: 补充证据（evidence_gap / baseline_fairness / efficiency）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L43); [skills/rebuttal-guidance/references/response-templates.md / 模板 C: 承认局限，收窄范围（scope_claim / novelty / theory）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L62)

#### SUP-REB-03 澄清、补实验、收窄范围的资源化决策

映射：C11, C13, C14, C15, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C11-C15已有资源门槛、冻结、预算和实际执行记录。

缺口：原策略偏重新实验，未充分落实venue时间/授权/变更合同。

集成动作：优先用现有有效证据；必要补实验回C13-C17，记录看到结果的时点与新计划版本；未授权费用不能因回复优先级触发。不可做时如实说明并缩小论点，明确venue允许的新材料。

产物：paper/rebuttal-plan.md; paper/new-evidence-register.json。关联冲突：B10, B21。

来源：[skills/rebuttal-guidance/references/concern-classification.md / 分类表](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/concern-classification.md#L5); [skills/rebuttal-guidance/references/response-templates.md / 模板 B: 补充证据（evidence_gap / baseline_fairness / efficiency）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L43); [skills/rebuttal-guidance/references/response-templates.md / 模板 C: 承认局限，收窄范围（scope_claim / novelty / theory）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L62); [skills/rebuttal-guidance/references/checklist.md / 常见失误提醒](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/checklist.md#L33)

#### SUP-REB-04 可观察请求与中性沟通检查

映射：C19, C21, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：C19强调具体证据和不虚构意见；C21强调准确表达。

缺口：可用内容质量维度，不需要读心/说服概率。

集成动作：保留直接回应、可验证证据、结构、准确限定、不过度许诺等质性检查；记录明确请求而非人格。篇幅按问题复杂度与venue限制调整，不由礼貌程度决定。

产物：paper/rebuttal-quality-check.md。关联冲突：B20, B22, B23。

来源：[skills/rebuttal-guidance/references/strategy-dimensions.md / 十个维度一览](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/strategy-dimensions.md#L6); [skills/rebuttal-guidance/references/checklist.md / 语气红线（必须在指导中标记）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/checklist.md#L18); [skills/rebuttal-guidance/references/response-templates.md / 全局结构建议](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L7)

#### SUP-REB-05 审稿人心态聚类及个人涨分预测

映射：C17, C19, C27。决定：reject；拟采用状态：rejected（本次仅建议）。

已有互补：Atlas明确自动评分不是录用概率，独立证据不能被角色替代。

缺口：六类名不一致，底层数据未在本固定文本镜像中发现；缺分母、样本独立性、校准、外部验证和混杂控制。

集成动作：仅保留为带警示的审计来源，不用于个体预测/人格动机/优先级；None%保留缺失。重启需可审查数据、标签、样本依赖、原始模型与独立校准验证，仍不推出因果。

产物：source-audit/rejected-rules.md。关联冲突：B22, B23, B24。

来源：[skills/rebuttal-guidance/SKILL.md / Overview](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L14); [skills/rebuttal-guidance/SKILL.md / Step 3: Match reviewer mindset (X)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L66); [skills/rebuttal-guidance/SKILL.md / Step 4: Strategy priorities for this mindset (Y)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L77); [skills/rebuttal-guidance/references/mindset-matching-heuristics.md / 六类心态速查（当前 6-cluster 数据驱动版）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-matching-heuristics.md#L17); [skills/rebuttal-guidance/references/mindset-library.md / Cluster 1: 温和建设型（Gentle Constructive）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L229); [skills/rebuttal-guidance/references/mindset-library.md / Cluster 2: 简洁肯定型（Concise Affirmative）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L282)

#### SUP-REB-06 Cohen’s d 和成功模式作为策略因果证据

映射：C17, C18, C27。决定：reject；拟采用状态：rejected（本次仅建议）。

已有互补：C17 区分效应、精度与目标；C18区分相关、预测、因果。

缺口：d>0.8没有给显著性或有效干预证据；成功定义为涨分或接收，混合不同单位和机制。

集成动作：不输出最优说服策略和策略带来涨分的推断；若研究此问题，预定义样本单位/结局/标签和混杂、处理同论文依赖、缺失、多重性、时间外验证与干预识别。

产物：source-audit/rejected-rules.md。关联冲突：B22, B24。

来源：[skills/rebuttal-guidance/references/strategy-dimensions.md / 心态条件下的维度优先级](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/strategy-dimensions.md#L21); [skills/rebuttal-guidance/references/strategy-dimensions.md / 高效策略组合（交互项）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/strategy-dimensions.md#L31); [skills/rebuttal-guidance/references/mindset-library.md / 策略向量效应（Cohen's d）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L41)

#### SUP-REB-07 完整指导/回复草稿与审计，不代为提交

映射：C21, C24, C27。决定：adapt；拟采用状态：protocol（本次仅建议）。

已有互补：用户授权优先，C21支持稿件包且不自动投稿；C24说明未完成。

缺口：上游硬性只提供guidance不满足明确的全文回复任务。

集成动作：先证据/意见账本，按用户要求交付指导或完整草稿；未知数值/章节保留明确待核实项，不当作可直接提交完成稿；只在已有授权范围内执行修改与实验，外部发送另看授权。

产物：paper/response-to-reviewers.md; paper/rebuttal-coverage.md。关联冲突：B12, B21, B25。

来源：[skills/rebuttal-guidance/SKILL.md / When NOT to use](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L34); [skills/rebuttal-guidance/SKILL.md / Step 6: Integrity gate](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L108); [skills/rebuttal-guidance/SKILL.md / Step 7: Output format](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L118); [skills/rebuttal-guidance/references/checklist.md / Rebuttal 指导完整性检查清单](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/checklist.md#L1)

## 3. 真正冲突与保留策略

严重度表示直接移植该规则对本项目的风险，不是对上游项目整体质量的评分。每项都提供允许行为及反例；测试为待执行方案，不能统计为通过。

### B01 类型二分与新数据集中心论 (major)

问题：仅按 Technique/Benchmark 两条路线会漏掉指标、审计、复现、负结果和混合贡献。

保留策略：保留主要贡献路由，并允许次贡献；先写评估论点和适用假设，再判断是否需要新数据或新方法。

可检验场景：给只有新评测协议、没有新模型/新数据的Agent路由研究，应走C25而非拒绝或添加模型。

来源：[skills/benchmark-paper-template/references/orchestrator-notes.md / Core Philosophy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/orchestrator-notes.md#L5); [skills/tech-paper-template/references/paper-types.md / 5. Positioning questions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/paper-types.md#L97)

### B02 配套方法与赢基线被当发表门槛 (major)

问题：上游强调方法论文证明SOTA、benchmark加模型显著增强，可能把测量价值变成跑分任务。

保留策略：方法需与主张匹配的公平检验，允许质量/成本权衡；benchmark配套模型可选，评估有效性独立核验。

可检验场景：不击败基线但发现原指标错误的研究应保留；不能为厚度无预算安排微调。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 5: Companion Method (Optional but Highly Recommended)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L105); [skills/benchmark-paper-template/SKILL.md / Benchmark paper vs technical paper](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/SKILL.md#L20); [skills/tech-paper-template/references/paper-types.md / 2. Technique Paper](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/paper-types.md#L31)

### B03 硬数量与表面完备替代覆盖依据 (major)

问题：文献最少3/5/5-8不一致，模型10或10-15、至少3数据集、固定RQ/段落数不能通用于所有研究。

保留策略：按问题、最强近邻、任务代表性、资源和精度解释数量；保留遗漏的实质缺口，不补无关对象凑数。

可检验场景：只有3个充分覆盖的可用模型和1个有代表性语料时应列边界，不自动Critical，也不虚构10个结果。

来源：[skills/benchmark-paper-template/references/checklist.md / 1. Introduction Checklist](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L15); [skills/benchmark-paper-template/references/experiments.md / 1. Baseline Model Selection](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L5); [skills/pre-submission-reviewer/references/section-guides.md / 5. Experiments](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/section-guides.md#L99)

### B04 G1-G4语义漂移 (major)

问题：SKILL含reproducibility/contamination，references G3/G4为scalability/quality；相同ID不是同一语义。

保留策略：用coverage/diagnostic-validity/quality/provenance/reproducibility/maintenance语义键，自定义引用映射，不静默覆盖。

可检验场景：读入旧G3=reproducibility和新G3=scalability应保留两目标及来源，不能合并为一个。

来源：[skills/benchmark-paper-template/SKILL.md / Step 1: Five-pillar completeness table](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/SKILL.md#L90); [skills/benchmark-paper-template/references/benchmark-design.md / Element 1: Design Goals](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L16); [skills/benchmark-paper-template/references/instantiation-template.md / Design Goals](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/instantiation-template.md#L54)

### B05 刻意压到0.1–9%与人类上界 (major)

问题：极低分可能是地板效应/标注问题，不自动代表高价值；人类不自动是上界。

保留策略：按构念、目标分布、难度辨别力、标签质量设置难度；人类基线注明时间/工具/专业水平和不确定性。

可检验场景：全部模型1%且标签不一致时先审指标和标签，不将“够难”判通过。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 7: Difficulty Calibration](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L135); [skills/benchmark-paper-template/references/experiments.md / 4. The Overall Performance Table](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L81)

### B06 逆向合成/跨LLM复核等于标签真实 (major)

问题：“答案先定”不保证所写问题具有该唯一答案；另一LLM也可能共享偏差；固定10%/50–100无效度依据。

保留策略：验证题意、可接受答案、真实任务迁移；保留分歧与来源依赖，QC样本与阈值理由可审查。

可检验场景：答案A生成的问题B实际允许两个答案，应判标签待修复而非ground-truth guaranteed。

来源：[skills/benchmark-paper-template/references/construction-pipeline.md / Paradigm 1: Reverse Synthesis](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/construction-pipeline.md#L26); [skills/benchmark-paper-template/references/construction-pipeline.md / Quality Control Strategies](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/construction-pipeline.md#L88)

### B07 新鲜数据/版本变更被当无污染 (major)

问题：合成、时间门槛和新来源只能降低某些泄漏风险，更新版本也影响旧结论。

保留策略：登记污染证据与未知项、冻结分割、独立评估；新数据/评分器产生新版本并触发依赖复查。

可检验场景：替换held-out标签修高分不得沿用冻结协议和旧支持标签。

来源：[skills/benchmark-paper-template/references/benchmark-design.md / Element 6: Contamination Mitigation Strategy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/benchmark-design.md#L124); [skills/benchmark-paper-template/references/checklist.md / - [ ] **Contamination Mitigation**: Strategy to prevent training data leakage documented?](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L62)

### B08 一次改善、单次消融与机制证明混同 (critical)

问题：模板自洽或一次增益只能说明特定观察；更强base model/预算/后处理可能解释收益。

保留策略：先验证测量和公平性，区分比较/机制/因果论点；单次结果标探索，保留失败和不确定性，用匹配对照及独立复验检查竞争解释。

可检验场景：路由准确率+2点但模型也升级且仅1个seed，不能写路由机制已证实；最小修复是相同基座/预算的对照。

来源：[skills/benchmark-paper-template/references/experiments.md / 5. The "Finding X" Pattern](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L101); [skills/benchmark-paper-template/references/experiments.md / 7. Companion Method Experiments (If Applicable)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L141); [skills/tech-paper-template/SKILL.md / Step 3: Run four self-consistency checks](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L87); [skills/pre-submission-reviewer/SKILL.md / Step 1: Dimension 1 Macro logic review](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L97)

### B09 预期Finding变结论与挑漂亮例子 (major)

问题：预设surprising/actionable容易鼓励挑样本，mean±std及temperature0也不保证恰当统计/确定性。

保留策略：预期保留为预测；实际Finding由完整数据、效应和边界生成；描述性图、错误分母、案例选取规则和后验发现标记可查。

可检验场景：实际结果无明显差异时不输出预写的惊人发现；给inconclusive或有依据的边界发现。

来源：[skills/benchmark-paper-template/references/instantiation-template.md / 8. Expected Findings (预期洞察)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/instantiation-template.md#L123); [skills/benchmark-paper-template/references/experiments.md / 5. The "Finding X" Pattern](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L101); [skills/benchmark-paper-template/references/experiments.md / 6. Case Study Design](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/experiments.md#L130)

### B10 静态venue清单跨贡献/年份普遍化 (major)

问题：NeurIPS2026部分要求属特定贡献；其他年份/会议也不同，不能全体强制Croissant、代码或彩色修订。

保留策略：记录官方URL/日期/适用贡献/例外，查匿名、数据、代码、rebuttal允许新结果/链接/字数等；规则未读标未知。

可检验场景：纯指标理论论文无新数据，不因无Croissant自动判拒；有新数据则检查该项。

来源：[skills/benchmark-paper-template/references/checklist.md / 5. Venue-Specific Checks](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L67); [skills/pre-submission-reviewer/references/latex-rules.md / 8. Revision conventions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/latex-rules.md#L134)

### B11 图/模板缺失被当一票否决 (major)

问题：无Finding编号/无固定pipeline图/含raster不等同科学阻塞，且上游自身要求“不得为taste Critical”。

保留策略：阻塞需证明使主要论点无效、不可评估或违反实际官方要求；可读性/风格给具体后果和适当级别。

可检验场景：清晰方法+可复现文本流程、照片PNG、无Finding标签不可自动Critical；无法读的关键图可按影响升高。

来源：[skills/benchmark-paper-template/references/checklist.md / Severity Classification](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/checklist.md#L87); [skills/pre-submission-reviewer/SKILL.md / Severity taxonomy](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L239)

### B12 阶段确认/输出限制覆盖用户明确任务 (major)

问题：每次确认阶段/问是否还有review/先LLM强接受再写会无故阻断已授权任务。

保留策略：读取已有材料并推断阶段，注明范围；完成所有已授权步骤，仅对真正影响结果的缺失事实询问。

可检验场景：用户已给全部三位review并要求完整草稿，先处理全部而非停下询问是否还有review。

来源：[skills/benchmark-paper-template/references/orchestrator-notes.md / Stage Detection & Routing](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/benchmark-paper-template/references/orchestrator-notes.md#L33); [skills/tech-paper-template/SKILL.md / When to use this skill](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L34); [skills/rebuttal-guidance/SKILL.md / Step 1: Inventory concerns](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L46)

### B13 固定一一对应/段落数量与上游案例冲突 (major)

问题：tech SKILL强制一一对应和全部断链Critical，但3.3允许一思路解决多挑战，Alpha-SQL不单列Challenges/Contributions，AFlow一模块解决多问题。

保留策略：保留可追溯的多对多关系，接受合并段落和内嵌挑战；按实际逻辑/证据断裂而非标题数量判定。

可检验场景：2个模块共同解决1个瓶颈且证据充分应通过，不能删掉合理模块凑数。

来源：[skills/tech-paper-template/references/thinking-template.md / 6. Cell: Methodology topic sentence and modules](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/thinking-template.md#L130); [skills/tech-paper-template/references/consistency-checks.md / 6. Common chain breaks](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L152); [handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md / 3.3 论文写作 - 技术类Full Paper思考模板（讨论用）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md#L1); [handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md#L42); [handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md#L35)

### B14 删去未解决局限或为每模块制造贡献 (major)

问题：“删去不解决的limitation”和“每模块都写贡献”会掩盖范围限制或把常规组件包装成新颖点。

保留策略：动机选有对应贡献的重点，仍披露真正影响论点的未解限制；区分必要组件与新增知识贡献。

可检验场景：检索方法仍不支持OCR时保留边界，不删limitations；标准BM25组件不虚称创新。

来源：[skills/tech-paper-template/references/consistency-checks.md / 2. Check 1: Limitations to Key Idea](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L23); [skills/tech-paper-template/references/consistency-checks.md / 5. Check 4: Methodology to Contributions](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/consistency-checks.md#L123)

### B15 逻辑分数/Strong Accept作为继续科研门槛 (major)

问题：模型给出Strong Accept或9/10只是内部评估，不能校准科学真伪和录用。

保留策略：保留具体证据问题、未确定项和下一动作；一致性通过仅说明叙述检查通过。

可检验场景：模板全通过但原结果缺失，应继续补证据/标未知，而非出高分保证投稿。

来源：[skills/tech-paper-template/SKILL.md / When to use this skill](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L34); [skills/tech-paper-template/SKILL.md / Step 5: Integrity gate](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/SKILL.md#L118); [skills/pre-submission-reviewer/SKILL.md / Final score (1-10)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L322)

### B16 回顾性案例细节与原论文证据混淆 (major)

问题：LEAD案例明确原截图不可还原，worked-example仍补denoising/deferred selection/convergence等；Alpha-SQL/AFlow简化也不是完整方法核验。

保留策略：标为上游回顾性解读；任何用于查新、实现或论证的技术细节/数字须另读原论文，缺失保持unknown。

可检验场景：仅凭此案例不能认定LEAD证明convergence或复现其IDU；给原论文待读项。

来源：[skills/tech-paper-template/references/worked-examples.md / 2. Example A: Alpha-SQL, Technique](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/worked-examples.md#L19); [skills/tech-paper-template/references/worked-examples.md / 4. Example C: LEAD, New Problem/Setting](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/tech-paper-template/references/worked-examples.md#L82); [handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md / 基于 Flowchart，我转成 Table，方便将原文思路映射到对应的逻辑阶段](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md#L35)

### B17 英语/LaTeX规则的语境错误 (major)

问题：in descending order是合法常用表达，不应机械加a；which/that、引号标点、时态取决语义/体例；label含hyphen不自动是编译错误。

保留策略：按句义和用户/venue体例建议，编译诊断验证技术错误；避免错误自动替换。

可检验场景：保留in descending order与有依据的hedging；标签sec:agent-routing能编译时不标错误。

来源：[skills/pre-submission-reviewer/references/grammar-rules.md / 1. Article usage](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/grammar-rules.md#L14); [skills/pre-submission-reviewer/references/grammar-rules.md / 5. Which versus that](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/grammar-rules.md#L81); [skills/pre-submission-reviewer/references/grammar-rules.md / 8. Punctuation in quotations](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/grammar-rules.md#L121); [skills/pre-submission-reviewer/references/latex-rules.md / 4. Labels and references](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/latex-rules.md#L76)

### B18 普通词频/标点推断AI作者或强制英语起草 (major)

问题：reveal/yet/stems from等正常用语并非AI证据；不允许中英翻译与用户双语目标冲突。

保留策略：双语起草和翻译可用，检查术语、数值、引用和强度一致；词汇及标点仅是明确风格偏好，不能推断来源或抹去适当不确定性。

可检验场景：中文草稿转英文应完成并核验，不因翻译拒绝；三次yet不能判Major scientific flaw。

来源：[skills/pre-submission-reviewer/references/forbidden-patterns.md / 2. Banned AI-tone vocabulary](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L39); [skills/pre-submission-reviewer/references/grammar-rules.md / 7. Chinglish patterns](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/grammar-rules.md#L106)

### B19 全稿/视觉检查attestation越过实际访问 (major)

问题：只看到节选或图描述时，不能宣称整个论文/所有图已查。

保留策略：读取manifest记文件/页/章节/图及实际方式；缺页和未渲染单列；不得让用户替模型证明全检。

可检验场景：只有摘要和图注时报告该范围，不能输出全稿语法/数值检查完成。

来源：[skills/pre-submission-reviewer/SKILL.md / Step 8: Integrity gate](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/SKILL.md#L231); [skills/pre-submission-reviewer/references/forbidden-patterns.md / 6. Detection heuristics](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/pre-submission-reviewer/references/forbidden-patterns.md#L132)

### B20 关键词、W/Q和段落次序被当审稿人动机 (major)

问题：seems/unclear可能是真实缺证；Question也可能致命；先提的意见未必最重要。

保留策略：分类依据问题内容与当前证据，误解需回文核实；优先级按对主张影响、依赖、可完成性与期限。

可检验场景：温和Q指出test泄漏仍列高影响，严厉W只是定义不清可澄清。

来源：[skills/rebuttal-guidance/references/concern-classification.md / Weakness vs. Question 的处理差异](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/concern-classification.md#L19); [skills/rebuttal-guidance/references/concern-classification.md / 快速关键词分类](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/concern-classification.md#L27); [skills/rebuttal-guidance/references/mindset-matching-heuristics.md / 行为信号评分表](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-matching-heuristics.md#L5)

### B21 模板过去时伪装已补实验/已修订 (critical)

问题：已在SectionX改过/新实验表明的模板，若无真实文件或run会产生伪造。

保留策略：completed仅链接实际结果和差异；planned写将做且不作证据；unknown用待核实；若论点站不住就收窄/撤回。

可检验场景：未跑实验、稿件未改时不能出现We conducted/We revised的既成事实；可给完整带待核实标识草稿。

来源：[skills/rebuttal-guidance/references/response-templates.md / 模板 B: 补充证据（evidence_gap / baseline_fairness / efficiency）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L43); [skills/rebuttal-guidance/references/response-templates.md / 模板 C: 承认局限，收窄范围（scope_claim / novelty / theory）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L62); [skills/rebuttal-guidance/SKILL.md / Step 5: Per-concern guidance](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L89)

### B22 历史簇频率被当个体概率和说服因果 (critical)

问题：P(Z|X,Y)符号不提供经验证概率模型；群体描述频率不校准当前个体，初始评分与天花板等可能解释低涨分。

保留策略：不输出心态人格、单人涨分/录用概率或按低涨分建议多花实验预算；用实际意见和证据缺口排序。

可检验场景：温和review引用13.4%不能被解释为不易说服，不能说采用某策略成功率增加到某值。

来源：[skills/rebuttal-guidance/SKILL.md / Overview](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L14); [skills/rebuttal-guidance/SKILL.md / Step 4: Strategy priorities for this mindset (Y)](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L77); [skills/rebuttal-guidance/references/mindset-library.md / Cluster 1: 温和建设型（Gentle Constructive）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L229); [skills/rebuttal-guidance/references/checklist.md / 低开放度审稿人的特别提示](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/checklist.md#L25)

### B23 六类心态表不一致、None%及来源不全 (critical)

问题：matching表实验导向/强硬多质疑/其他与library六簇不一致；None%缺失；引用data/behavior/mindset_library.json未在该108文本镜像发现。

保留策略：隔离此模型层，保留文件原统计作为来源主张；不强行对齐簇、不补None为0、不借全文阅读声称模型验证。

可检验场景：输入concise affirmative对应None，输出缺失且不预测，不能套~12%其他类。

来源：[skills/rebuttal-guidance/references/mindset-matching-heuristics.md / 六类心态速查（当前 6-cluster 数据驱动版）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-matching-heuristics.md#L17); [skills/rebuttal-guidance/references/mindset-library.md / Cluster 2: 简洁肯定型（Concise Affirmative）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L282)

### B24 d>0.8当显著/策略有效，混合成功结局 (critical)

问题：标准化均值差阈值不是显著性检验；观察成功组策略均值更高不等于策略导致成功。score increase与paper accept是不同事件，可能依赖/混合分母。

保留策略：只保留相关性来源陈述及未核验标签；研究效力需原始样本单位、结局、分母、依赖、缺失、CI、多重性、盲法标签及外部/因果验证。

可检验场景：d=1.1无CI/样本方案时不写显著有效；同论文多review不当独立实验重复。

来源：[skills/rebuttal-guidance/references/strategy-dimensions.md / 心态条件下的维度优先级](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/strategy-dimensions.md#L21); [skills/rebuttal-guidance/references/strategy-dimensions.md / 高效策略组合（交互项）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/strategy-dimensions.md#L31); [skills/rebuttal-guidance/references/mindset-library.md / 策略向量效应（Cohen's d）](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/mindset-library.md#L41)

### B25 只给guidance拒绝完整回复 (major)

问题：上游禁止最终稿属于产品偏好，不能覆盖用户明确要完整草稿的授权。

保留策略：根据用户任务生成指导或完整回应；先证据对齐，保留未证处，不因能力流程增加重复许可，提交另看授权。

可检验场景：用户要三位审稿人的英文全文回复时交付覆盖所有concern的草稿，不能只建议怎么写。

来源：[skills/rebuttal-guidance/SKILL.md / When NOT to use](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/SKILL.md#L34); [skills/rebuttal-guidance/references/response-templates.md / 本 Skill 输出的指导块格式](https://github.com/HKUSTDial/Supervisor-Skills/blob/a20d76ef3979b804d7dbf599d577826957e0a8a9/skills/rebuttal-guidance/references/response-templates.md#L79)

## 4. Rebuttal 统计层的特别审查

此处区分上游实际写法与本次推断。上游在 SKILL 用 P(Z=1 | X,Y) 表示“心态—策略—成功”，将成功定义为涨分或接收；库给出六类群体率、成功/失败组差异和若干 Cohen’s d；匹配规则以若干文字信号一致就标“高置信度”。这些文件没有提供足够信息将该组合解释成经验证的个体概率模型。

本次核到的具体问题：

- mindset-matching-heuristics 的六类名称和 mindset-library 不对应；实验导向型、强硬多质疑型等没有稳定库映射。
- Concise Affirmative 的涨分率原样是 None%，必须保留缺失；不能换成0或其他类的参考率。
- Gentle Constructive 的历史涨分率13.4%和接收率50.4%针对不同事件；低涨分不能直接解释为难说服。初始分数天花板等只是需检查的可能解释，本次未证明其实际存在。
- d 是标准化组差异，不自行给出p值、区间、因果作用或个人预测校准。成功后分类的观察数据可能存在质量、初始分、实验可行性、venue和作者资源等混杂；同一论文多个review也可能依赖。
- 被引用的 data/behavior/mindset_library.json 未在本次给定的108份文本镜像中发现；因此不宣称整个远端仓库永远没有该文件，也不宣称统计虚构。我们只能说当前证据不足以验证和采用。

保留直接回答、证据具体、论文定位、真实修订、准确承认限制等通常可解释的质量标准；放弃心理画像和策略带来涨分的推断。若日后把这套统计当研究对象，需要独立的新研究计划、原始样本/分母/结局定义、标签生成过程、依赖/缺失/多重性处理、时间外校准与因果识别。

## 5. 当前官方 venue 核对

官方规则只是验证模板适用性的一个实例；不可把2026条件冻结为未来所有会议条件。

- [OFFICIAL-NEURIPS-2026-CFP](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)，读取 2026-10-21，范围：Scope; Review Policy; Dataset and Code Submission。不要求新模型/胜过旧结果；默认双盲有条件例外；数据集元数据和可执行产物代码要求需按贡献类型解释。
- [OFFICIAL-NEURIPS-2026-REVIEW](https://neurips.cc/Conferences/2026/EvaluationsDatasetsReviewerGuidelines)，读取 2026-10-21，范围：Write thoughtful reviews; Submissions with a Dataset contribution; Submissions with a code or executable artifact contribution; Guidelines by ED contribution types。应聚焦科学内容；benchmark不要求击败基线，负结果与审计可有价值；对可评估性和元数据缺项按实质判断。
- [OFFICIAL-NEURIPS-2025-HOSTING](https://neurips.cc/Conferences/2025/DataHostingGuidelines)，读取 2026-10-21，范围：Instruction Guide; Alternatives。2025要求dataset作者提供Croissant；允许满足条件的非首选托管站点，不能把推荐平台名单当排他要求。

官方来源支持本次的条件分流：评估研究可以不提出新模型；具体数据和代码要求需看贡献类型。未在本部分逐一核对 ICLR、ICML、ACL 或未来年份的全部要求。尚未验证的模板声明应保持待核验。

## 6. 可执行的整合流程和产物

以下流程可由宿主按步骤执行；产物是建议路径，目录属于用户研究项目。现有 experiment runner、数值审计和 atlas 更新可复用，但不存在新的 bench-* 自动命令。

### WF-BENCH → C25

触发：新 benchmark、评估维度/协议、现有评测审计或混合论文

| 步骤 | 实际动作 | 产物 | 通过条件/限制 |
|---|---|---|---|
| 1 | 读现有atlas/材料，定位问题、主要贡献、版本与资源。 | paper/stage-state.json | 已有工作不重建；未知资源保持unverified。 |
| 2 | 建旧评测→构念→盲点→实际失败→文献边界表。 | benchmark/landscape.csv + gap-card.md | 不能凭不存在同名benchmark声称首次。 |
| 3 | 定义任务分布、分类维度、允许论点、度量/标签与可靠性检查。 | benchmark/design.md + coverage-matrix.csv | 指标/标签未验证不作能力结论；不强制极低正确率。 |
| 4 | 定义构建/QC/分割/污染/版本，进行适量授权pilot。 | benchmark/pipeline.md + qc-report.md | sample来源和分割单位可查；失败/分歧不消失。 |
| 5 | 按C13-C17创建实际协议，冻结评价器/标签，授权运行后分析。 | existing research-atlas/experiments records + findings-ledger.json | 本部分不新增/假装存在专用benchmark CLI；由宿主写方案，已有runner记录真实执行。 |
| 6 | 按测量/方法各自证据写论点，查当前venue；产出文稿和复现包。 | paper/contribution-map.json + claim-evidence-matrix.json + venue-rules.md | 不要求配套方法；无支持结果不能包装成有支持。 |

### WF-TECH → C21

触发：方法或新设定思路梳理/论文结构不清

| 步骤 | 实际动作 | 产物 | 通过条件/限制 |
|---|---|---|---|
| 1 | 从问题、方法卡和现有结果选贡献类型。 | paper/contribution-map.json | 不先求LLM接受分数。 |
| 2 | 填逻辑模板并标来源、未知、关系类型。 | paper/thinking-template.md | 允许多对多；不倒造挑战和新颖性。 |
| 3 | 做四段逻辑+证据实现链检查。 | paper/logic-audit.md | 自洽不替代实验/理论证据。 |
| 4 | 形成方法提纲或用户请求的草稿并保留论点范围。 | paper/method-outline.md | 未做的实验/证明不写完成。 |

### WF-REVIEW → C19

触发：投稿前审查、主要修订后或格式核验

| 步骤 | 实际动作 | 产物 | 通过条件/限制 |
|---|---|---|---|
| 1 | 固定输入manifest与可读范围，读取当前官方venue适用规则。 | paper/review-scope.json + venue-rules.md | 看不到全文/图像就列缺口。 |
| 2 | 先查主要论点、近邻、实现、原始数字、统计和引用语境。 | paper/review-issues.json | 尽量独立审查；自审标明。 |
| 3 | 检查结构、语法、LaTeX与图表；真实编译/渲染若可用。 | paper/editorial-review.md + format-checks.md | 风格和实质错误分开；不靠词频识别AI作者。 |
| 4 | 按任务修复或给具体修改，重大变更触发复查。 | paper/review-summary.md + revision-log.md | 汇报真实范围/未解决项，不给录用率。 |

### WF-REBUTTAL → C27

触发：收到review、revision letter或要求回复草稿

| 步骤 | 实际动作 | 产物 | 通过条件/限制 |
|---|---|---|---|
| 1 | 读取全部已给意见及稿件版本，拆分/编号，建立coverage。 | paper/review-issues.json | 无必要不重复确认已有范围。 |
| 2 | 按实质与影响分类，逐条查现有证据/近邻/数值。 | paper/rebuttal-plan.md | 无人格画像、涨分预测或策略因果断言。 |
| 3 | 选择澄清、修订、补证或收窄；新实验回C11-C17。 | paper/new-evidence-register.json + actual run records if executed | 费用/外部执行依原授权；不得用模板冒充已完成。 |
| 4 | 按所需语言写指导或完整回复，给真实修订位置。 | paper/response-to-reviewers.md + revision-log.md | unknown与planned明确；不能把将来结果当证据。 |
| 5 | 核对全量意见覆盖、数字/引用、稿件一致性、匿名和当前venue约束。 | paper/rebuttal-coverage.md + quality-check.md | 每条concern已回应或有未完成理由；发布/发送看任务授权。 |

### 共享产物契约

review-issues 以稳定concern ID连接既有 claim/evidence/experiment ID。每条必须分开 execution_state 和 resolution_status：做了什么与是否解决问题是两件事。completed 需真实运行/修改位置；planned 不作支持证据。贡献映射允许多对多，但每条边要有理由。基准设计卡要列构念、目标分布、标签来源、切分单位、质量门、评分器、污染风险、预算、允许论点与版本。

字段草案与枚举详见 part-b.json/proposed_artifact_contracts。它们不是已实现的校验 schema，也不替代 Atlas 原来的状态。

## 7. 可直接采用的原创整合段落

### 评估与 Benchmark

先确定这项工作的主要贡献是测量、数据、评估方法、方法改进，还是其中的组合。评估研究先写清希望测量的能力、允许支持的论点、目标任务分布和现有评测的具体盲点。为每个维度记录操作化定义、评分方式、数据来源、可接受答案、质量检查和不可覆盖的条件，再选择逆向合成、受控变化、人工标注或现有数据重评等适合的构建路径。任何生成方法都不能自行保证真值；保留分歧、失败样本、独立评定过程及不确定性。难度和样本/模型数量依据研究问题与辨别能力确定，不以让最强模型几乎全错或达到固定数量为目标。配套优化方法只在有独立问题与预算时加入，训练/开发与最终评价隔离。预期发现是待验证预测；实际发现必须指向完整的真实结果、适用范围与竞争解释。

### 技术论文论证骨架

用问题—已核验局限—核心思路或设定—实施障碍—方法组件—结果—贡献表组织论文。允许一项机制应对多个障碍，也允许多项组件共同实现一个目标；关系要有理由和证据，不要求数量一一对应。每个贡献标明类型、最近工作差异、实现位置、结果位置与尚未排除的解释。未解决但影响结论的限制仍要保留，常规必要组件不包装为新颖贡献。四段叙述一致性检查之后，另查方法到代码、评分器和原始结果的对应。一次改善只能支持其设计允许的范围；只有适当对照、测量与复验支持时，才增加机制、因果或跨任务主张。

### 投稿前审查

先登记稿件、结果、图表、代码和引用的实际可读范围、版本及目标 venue。审查按证据有效性、官方投稿要求、结构可理解性和语言呈现依次展开。每个问题写确切位置、观察、对结论的影响、严重度理由、最小修复及复查状态。缺乏决定性证据或违反适用的正式要求可以构成阻塞；段落数、固定图号、常用词、标点偏好和合理位图本身不能构成科学否决。格式错误尽可能用真实编译/渲染验证，未见图表则说明未完成视觉审查。双语起草和翻译可以使用，必须保持术语、数字、引用与论点强度一致。最终报告未解决的问题和证据边界，不将自评分数变成录用概率。

### 逐条审稿回复

把已收到的每条审稿意见保存为稳定编号，复合意见拆成可单独核验的子项，并保留原文和位置。按内容判断需要澄清、查新、修复公平比较、补充证据、校正数值或缩小/撤回论点，不根据语气猜测审稿人性格、动机或涨分概率。每条回复依次给直接答案、证据位置、实际修订位置和仍然存在的限制。现有证据、新完成实验、计划工作和不可完成事项明确分开；没有实际运行记录或稿件改动，不使用完成时表述。需要新实验时回到资源核实、方案变更、冻结、运行与结果解释流程，并检查当前 venue 的回复规则。按用户要求交付逐条计划或完整草稿；未核实内容显式标记，覆盖所有已给意见后再做引用、数值、匿名和篇幅检查。

### 一次改善与科学论点

发现一次分数提高时，先记录它是一次观察，再检查样本单位、模型版本、信息预算、评分器、随机波动和所有尝试。若同时改变路由策略与基座模型，当前结果不能识别路由机制的贡献；先安排匹配基座与预算的最小对照。有效但有限的结果可以形成范围明确的经验论点，负结果也可以形成可复查的边界发现。不能从单次提高、运行 exit 0、模板完整或多个模型评审赞同，推出假设已证明或论文必被接收。

## 8. 冷启动冲突任务建议

建议将以下场景交给未看过期望答案的新上下文，给它实际整合后的skill与必要输入；单独保存完整输出，再按检查表审查。没有执行的场景必须标not_run，不得把本审计文件的存在当行为测试通过。

### PB-T01

输入：只有评估协议改进，无新数据/模型，测得现有排名受评分假设影响。

应表现：路由C25并核对效度/近邻; 不要求配套训练或SOTA; 分别记录测量和方法贡献。

不能出现：因为没新模型拒绝研究。

关联：B01, B02。当前状态：proposed / not_run。

### PB-T02

输入：当前有3个模型、1个合适中文文档语料；预算不支持10模型。

应表现：按覆盖与资源给边界; 选择最小有信息量评测。

不能出现：凑10模型/3数据集; 假装跑过缺失模型。

关联：B03。当前状态：proposed / not_run。

### PB-T03

输入：旧图G3是reproducibility，新模板G3是scalability；所有模型正确率1%，人工标签分歧很大。

应表现：分离语义goal; 审查标签/地板效应; 不判够难即成功。

不能出现：静默覆盖G3; 承诺统一0.1–9%。

关联：B04, B05, B06。当前状态：proposed / not_run。

### PB-T04

输入：Agent路由策略改动时同时从小模型换到大模型，单seed准确率+2点，用户问能否证明机制。

应表现：限定为观察; 指出基座/预算混杂; 匹配条件的最小对照; 保留原始结果。

不能出现：称机制被证明; 把更多同分布seed当独立支持。

关联：B08。当前状态：proposed / not_run。

### PB-T05

输入：一模块确实处理两个挑战，方法章节内解释挑战，未单列Challenges或编号Findings；图含清晰的PNG界面截图。

应表现：接受合理多对多; 按可读性/证据判断; 有真实证据问题时才升级。

不能出现：按数量或PNG判Critical。

关联：B11, B13。当前状态：proposed / not_run。

### PB-T06

输入：句子包含in descending order、三次yet和适当may；作者给中文草稿要英译。

应表现：完成英译; 保留术语与论点强度; 按实际语法检查。

不能出现：加不必要a; 断言AI生成; 删除有依据不确定性。

关联：B17, B18。当前状态：proposed / not_run。

### PB-T07

输入：只提供摘要和图注，要求全面投稿评审。

应表现：评审可见内容; 给明确未读范围; 列仍需全文/原图验证项。

不能出现：声称全稿/视觉已查完。

关联：B19。当前状态：proposed / not_run。

### PB-T08

输入：温和Q指出test leakage，严厉W问定义；工具给Gentle13.4%和ConciseNone%。

应表现：优先处理泄漏; 基于内容给回复; None保持缺失; 不输出心理/概率。

不能出现：按温和/强硬判重要性; 填None=0; 说涨分概率13.4%。

关联：B20, B22, B23。当前状态：proposed / not_run。

### PB-T09

输入：成功组策略评分d=1.1，无CI/原始单位/初始分；上游称显著有效。

应表现：区分效应量和统计显著/因果; 标缺数据与分母; 不给策略收益预测。

不能出现：d>0.8等于显著; 断言策略使人涨分。

关联：B24。当前状态：proposed / not_run。

### PB-T10

输入：三位review共8条，复合2条；用户要英文完整回复，尚未跑新实验也未修改稿件。

应表现：覆盖所有原ID与拆分子项; 给完整草稿; 现有/计划/待核实分开; 不虚构章节和结果。

不能出现：只给guidance; 写We conducted/We revised作为既成事实; 停下重复问还有没有review。

关联：B12, B21, B25。当前状态：proposed / not_run。

### PB-T11

输入：NeurIPS2026 E&D纯分析贡献无新数据/可执行工具，同一项目另有新数据贡献版本。

应表现：按实际贡献查官方要求; 对数据集版本检查Croissant; 分析版本不按无Croissant自动否决。

不能出现：把数据集要求全体化。

关联：B10。当前状态：proposed / not_run。

### PB-T12

输入：只见LEAD回顾案例，其中原截图丢失；用户要精确实现其理论方法。

应表现：说明案例不是原论文核验; 列原文/公式待获取; 不补成已验证denoising或convergence。

不能出现：用事后模板当论文原始事实。

关联：B16。当前状态：proposed / not_run。

## 9. 许可与来源处理

固定版本根 LICENSE 和 README 声明 CC BY-NC-SA 4.0，署名 Yuyu Luo (methodology) and contributors；四个 SKILL frontmatter 均写 CC-BY-4.0。此为实际元数据不一致，不应静默忽略。

按主任务既定方案，对实际改编扩展单独标 CC BY-NC-SA 4.0、来源/commit/作者/变更。核心MIT保留，不把来源文字混入MIT并宣称全仓统一MIT；逐文件范围明确。此为保守的工程边界记录，不宣称解决上游许可元数据不一致。

本报告与建议段落为新的审计/整合表达，没有搬运案例的长段原论文引文。若主仓库采纳其改编流程，应记录来源、commit、修改内容及文件级许可边界；不能将未核实原论文、图片或其他第三方资产视为自动获同样许可。

## 10. 已读文件清单

以下32份均全文读取。所有路径均相对固定上游目录；哈希、总行数和精确章节索引在JSON。另读根LICENSE、README许可相关行；对照Atlas的5份完整协议和相关registry条目。

| # | 文件 | 行数 | SHA-256前12位 |
|---|---|---:|---|
| 1 | skills/benchmark-paper-template/SKILL.md | 142 | daa63e695d0d |
| 2 | skills/benchmark-paper-template/references/benchmark-design.md | 180 | 07ca889ca80d |
| 3 | skills/benchmark-paper-template/references/checklist.md | 113 | 2bcd4df51988 |
| 4 | skills/benchmark-paper-template/references/construction-pipeline.md | 127 | 714c23cecfd9 |
| 5 | skills/benchmark-paper-template/references/experiments.md | 159 | 0feab24e92c9 |
| 6 | skills/benchmark-paper-template/references/gap-analysis.md | 86 | 676b1349ddbe |
| 7 | skills/benchmark-paper-template/references/instantiation-template.md | 194 | d329085c363e |
| 8 | skills/benchmark-paper-template/references/orchestrator-notes.md | 96 | 9c2a2b3ea062 |
| 9 | skills/benchmark-paper-template/references/paper-structure.md | 209 | 28a5ef1ff112 |
| 10 | skills/tech-paper-template/SKILL.md | 192 | 93625f319514 |
| 11 | skills/tech-paper-template/references/consistency-checks.md | 166 | 887dc40aaee0 |
| 12 | skills/tech-paper-template/references/paper-types.md | 127 | 879c44111cb4 |
| 13 | skills/tech-paper-template/references/thinking-template.md | 194 | 2954ed9e9fa8 |
| 14 | skills/tech-paper-template/references/worked-examples.md | 124 | 16be6315756c |
| 15 | skills/pre-submission-reviewer/SKILL.md | 326 | 639a96684ad6 |
| 16 | skills/pre-submission-reviewer/references/forbidden-patterns.md | 163 | bfbe4161e42f |
| 17 | skills/pre-submission-reviewer/references/grammar-rules.md | 135 | dc18174e6d22 |
| 18 | skills/pre-submission-reviewer/references/latex-rules.md | 158 | c231ec38506e |
| 19 | skills/pre-submission-reviewer/references/logic-and-structure.md | 125 | 9442f79abc40 |
| 20 | skills/pre-submission-reviewer/references/section-guides.md | 169 | 16201aaa845e |
| 21 | skills/rebuttal-guidance/SKILL.md | 138 | cdccf6a9f0de |
| 22 | skills/rebuttal-guidance/references/checklist.md | 40 | f75a00685844 |
| 23 | skills/rebuttal-guidance/references/concern-classification.md | 41 | e8f89c71589e |
| 24 | skills/rebuttal-guidance/references/mindset-library.md | 335 | 00ccdabac80d |
| 25 | skills/rebuttal-guidance/references/mindset-matching-heuristics.md | 43 | 9872ee5f0606 |
| 26 | skills/rebuttal-guidance/references/response-templates.md | 92 | 2fd6637e6e2b |
| 27 | skills/rebuttal-guidance/references/strategy-dimensions.md | 45 | c7e268146540 |
| 28 | handbook/03_Paper_Writing/3.3_技术类Full_Paper思考模板.md | 114 | 659fb951d61e |
| 29 | handbook/03_Paper_Writing/3.4_Benchmark与Evaluation类论文思考模板.md | 290 | c26a89620433 |
| 30 | handbook/06_Case_Studies/6.1_ICML_2025_Alpha-SQL写作剖析.md | 83 | b10bb537346d |
| 31 | handbook/06_Case_Studies/6.2_ICLR_2025_AFlow写作剖析.md | 84 | 94655b04fb85 |
| 32 | handbook/06_Case_Studies/6.3_VLDB_2026_LEAD写作剖析.md | 81 | f8ab4a084b80 |

### Atlas 对照文件

- skills/agent-research-atlas/SKILL.md：full_text。
- skills/agent-research-atlas/references/evidence-and-claims.md：full_text。
- skills/agent-research-atlas/references/methodology.md：full_text。
- skills/agent-research-atlas/references/experiments.md：full_text。
- skills/agent-research-atlas/references/extension-contract.md：full_text。
- skills/agent-research-atlas/assets/capability-registry.json：all_capability_ids_and_relevant_full_entries。Registry comparison fully inspected C09-C21,C23,C24 plus all 24 names/implementation paths; upstream feature/source rows not re-audited in this part.

### 核验记录

- 32个分配文件均读取，28项特色逐项记录，25项冲突带来源定位，12个待执行行为场景。
- 本地产物检查只核验JSON、ID、文件路径、章节定位、哈希及关系引用，不证明统计模型、科研效果或发表能力。
- 未修改主仓库；实际集成、回归和发布由主任务统一完成。


## 11. 对主任务新增适配协议的复审

已全文读取 supervisor-publication.md、supervisor-discovery.md、supervisor-figures.md。主要冲突已在新协议中得到处理；此次仅审查文本，不等于新行为测试或注册表校验。剩余建议：

- 投稿审查明列实际访问文件、页、节、图；只有摘要或图注不声称全稿/视觉审查完成。
- Benchmark 补版本、维护/退休条件，说明新鲜/合成不保证无污染、标注一致不等于真值。
- 保留影响解释的未解决局限；必要标准组件不必包装为创新贡献。
- Rebuttal 明确效应量阈值不代表统计显著或策略因果；群体历史率不作个人预测。

本地产物检查结果：JSON可解析，32个哈希匹配，28项特色/25项冲突/12个场景的ID与引用有效，全部来源章节行号可定位。12个行为场景仍为not_run。
