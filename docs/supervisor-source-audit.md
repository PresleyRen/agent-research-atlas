# Supervisor-Skills 整合与来源审查

日期：**2026-10-21**。Agent Research Atlas v1.1.0 候选。

## 项目身份和读取边界

本轮用户补充“鸭博士”后定位到正式项目 **[HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)**。相关教程使用该昵称关联科研技能包；官方名称仍为 Supervisor-Skills，归因给 Yuyu Luo（骆昱宇）及贡献者，不把昵称写作官方项目名。此前65项来源清单未含这个项目，本轮新增其12个具名技能。

所有方法读取固定在 [commit a20d76ef3979b804d7dbf599d577826957e0a8a9](https://github.com/HKUSTDial/Supervisor-Skills/tree/a20d76ef3979b804d7dbf599d577826957e0a8a9)。仓库少量导览仍写11项；以该commit实际12个含SKILL.md的目录计数，包含 rebuttal-guidance。

已全文读取 **12份 SKILL.md、70份配套 Markdown references、18份中文 handbook 章节**，以及根README、许可、Drawio双语README、CHANGELOG和llms等7份文本。107份完整读取文件的路径、字节数、SHA-256、Git blob和读取角色见 [读取账本](supervisor-source-manifest.json)。源文件按固定Git blob核对；原文不全量复制进发行包。

图片/图形资产、配套PDF、英文手册镜像、上游helper代码和案例外链论文未纳入全文/视觉/执行验证；部分技能目录导览只预览。文本中案例的引用或结果没有因此变成独立复验。三份来源审查的原始范围和提出时状态保持不变：

- [Part A：选题、深度调研、科研协作](supervisor/part-a.md) · [JSON](supervisor/part-a.json)
- [Part B：Benchmark、方法论文、投稿审查与回复](supervisor/part-b.md) · [JSON](supervisor/part-b.json)
- [Part C：引言、正文、润色、科研图与重建](supervisor/part-c.md) · [JSON](supervisor/part-c.json)

## 逐技能覆盖

| Skill | 全读的本目录MD数 | 特征数 | 映射能力 |
|---|---:|---:|---|
| `idea-evaluator` | 12 | 7 | C02, C05, C06, C07, C08, C09, C10, C11, C12, C13, C17, C18, C19, C20, C21, C24 |
| `deep-research` | 8 | 6 | C01, C03, C04, C05, C06, C17, C18, C19, C20, C21, C23, C24 |
| `vibe-research-workflow` | 6 | 6 | C02, C05, C06, C07, C11, C12, C13, C15, C16, C18, C19, C20, C21, C22, C23, C24 |
| `benchmark-paper-template` | 9 | 9 | C02, C09, C11, C12, C13, C14, C16, C17, C18, C20, C21, C23, C24, C25 |
| `tech-paper-template` | 5 | 5 | C05, C07, C10, C12, C18, C19, C21, C24 |
| `pre-submission-reviewer` | 6 | 7 | C06, C09, C12, C13, C16, C18, C19, C20, C21, C24, C27 |
| `rebuttal-guidance` | 7 | 7 | C11, C13, C14, C15, C16, C17, C18, C19, C21, C24, C27 |
| `intro-drafter` | 8 | 5 | C05, C06, C12, C18, C21, C24, C26, C28 |
| `paper-writer` | 10 | 6 | C05, C06, C12, C18, C19, C21, C22, C24, C26 |
| `paper-polish` | 4 | 5 | C18, C21, C24, C26 |
| `figure-designer` | 6 | 5 | C16, C17, C21, C22, C28 |
| `drawio-reconstruction` | 3 | 6 | C12, C20, C22, C24, C28 |

合计 **74项来源特色**（Part A 19、B 28、C 27），每项都保留来源章节、原审查feature ID、采用状态、互补来源和补法。原审查报告里的“proposed / not_run”反映审查当时；最终采用记录以 [当前registry](../skills/agent-research-atlas/assets/capability-registry.json) 为准，实际任务行为见 [测试记录](supervisor-validation.md)。全项目扩大到 **77来源、296特征、28能力、28冲突**，其中48份具名SKILL正文已全文读过。

## 进入现有项目的实现

| 入口 | 实际增加的文件 | 研究产物与连接 |
|---|---|---|
| 选题与调研 C01/C03–C12 | [supervisor-discovery](../skills/agent-research-atlas/references/supervisor-discovery.md) | 决策驱动研究简报、前提历史、长期问题解锁条件、条件性证据综合；复用问题/论文/假设/决定ID |
| Benchmark C25 | [supervisor-publication §2](../skills/agent-research-atlas/references/supervisor-publication.md) | 评估缺口、构建谱系、标注/真值、划分与污染、RQ诊断、可选配套方法、维护/退休条件 |
| 方法论文与成稿 C21/C26 | 同一publication工作台 §3–5 | 多对多论证关系、实际正文、中英术语与润色、单独句级证据表及科学改动说明 |
| 投稿审查与回复 C27 | publication工作台 §6–7 | 实际读取范围、定位问题、原意见/子项ID、证据→行动→修订→回复状态 |
| 科研图与重建 C28 | [supervisor-figures](../skills/agent-research-atlas/references/supervisor-figures.md) | 图的用途、数据/量纲、原生文字和连线、混合媒体编辑范围、实际预览与检查 |

增加五个 [项目模板](../skills/agent-research-atlas/assets/supervisor)，分别保存研究简报、Benchmark设计、论文证据表、审稿意见/回复和图稿交接。SKILL.md按实际请求路由到相应章节。没有为各来源另建独立文献库；所有工作仍回到现有图谱、冻结计划、来源、运行和待复核机制。

## 冲突的具体裁决

| 冲突 | 最终处理 | 相关契约 |
|---|---|---|
| 一次输给简单基线就Reject，并跳过后续有效性 | 检查信息可见性、实现、测量、预算与精度；有效反证限制确切预测，坏测量先诊断 | CF07/CF21 |
| 主观分数、固定GPU/工时、论文年龄或失败率决定科研潜力 | 保留收益/成本维度、关键路径和长期问题；判断依赖实际证据、资源和可观察解锁条件 | CF04/CF06/CF21 |
| 每分支凑论文配额、MECE空格当研究缺口、迭代到全CLEAR | 保留多视角与盲区检查，允许交叉分类，按决策影响与预算补查 | CF01/CF02/CF15/CF16 |
| Benchmark必须新算法、固定模型数或极低准确率 | 以测量贡献为主线；模型、数据、难度和配套方法按研究问题选择 | CF22 |
| 六段/三个模块/一一对应作为论文硬结构 | 保留问题到贡献的可追溯关系，允许多对多；常规组件不强行包装为创新 | CF15/CF23 |
| 计划结果写preliminary、全文层级支持任意claim | 按实际观测与来源语句限制；自然正文和证据表分别保存 | CF02/CF08/CF24 |
| 润色改强因果、机械禁词/标点和错误语法修正 | 保持数字、单位、否定、范围与因果；科学更正保存前后差异和依据 | CF26 |
| 回复按审稿人心态和历史涨分百分比优化 | 保留逐条技术问题和证据/修订闭环；不预测人格、个体涨分或策略因果 | CF25 |
| 所有图只许矢量、所有纵轴不从零、时间轴右上最优 | 按图的任务和量纲选编码；延迟越小、准确率越大；合适的位图细节可保留 | CF27 |
| XML有效等于图已通过、整图嵌入等于可编辑 | 原生对象、箭头、导出、视觉与语义检查分别记录，未完成保留待修 | CF28 |

上述行是冲突类别归并；更细的源文件矛盾与修订理由保存在三份审查报告和74项feature记录中。局部实验室工作习惯、过时工具建议和上游安装命令不扩大本次项目授权。

## 官方投稿规则的核验

本轮按 **2026-10-21** 检查 [NeurIPS 2026 E&D官方征稿](https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets)：评估是可独立研究的对象，文章可以不提出新模型或超过先前结果；默认双盲，特殊数据情形另有说明；数据集元数据要求和可复用可执行产物的代码要求各有适用范围。这支持按实际贡献路由，不能将某年清单推广成所有研究的固定准入条件。后续投稿仍需重查目标年份/轨道的官方要求。

## 许可与改编

Atlas核心Python脚本和原协议保持MIT。Supervisor根许可为CC BY-NC-SA 4.0，部分旧skill frontmatter仍写CC-BY-4.0，源审查保留此不一致。三份改编工作台和五个模板单独按根CC BY-NC-SA 4.0声明并署名，注明改写与Agent适配，见 [LICENSE.supervisor.md](../skills/agent-research-atlas/LICENSE.supervisor.md)。

Drawio子目录的MIT许可证已由协调者另行全文获取，Git blob为 `47c7a5678977e445cc2d340c12628207c8c28ff1`，版权行为 **2026 VCG-Bench Authors**。Part C最初只读到README中的MIT声明；这次补读以本段和读取账本扩充，不改写原报告。未搬入上游drawio代码或推荐模型运行时。完整发行包因此含不同许可范围，见 [THIRD_PARTY_NOTICES](../THIRD_PARTY_NOTICES.md)。

## 继续补强

运行 `audit.py locate --query C25`、`C26`、`C27` 或 `C28`，直接定位本轮新增工作台、模板、来源与回归任务。旧能力中相关owner已指向新选题/调研工作台。新增绘图renderer或真实文献服务时，应补对应输入输出和失败回执，再验证实际执行；不用重写整个研究流程。
