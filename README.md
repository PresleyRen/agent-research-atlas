# Agent Research Atlas

**把读文献、找问题、设计实验、形成论文和持续更新，连成一张可以接着研究的地图。**

[English](README.en.md) · [使用技能](skills/agent-research-atlas/SKILL.md) · [全部来源](SOURCES.md) · [能力与互补](docs/coverage-audit.md) · [测试记录](docs/validation.md) · [扩展指南](docs/EXTENDING.md)

Agent Research Atlas 是面向 Agent 研究的中英双语 Skill。它帮助 AI 助手读取综述与原始论文，整理研究方向、进展和争议，从论文局限、真实失败、前提变化与评估缺口中建立可追踪 Gap；再由 Research Supervisor 指导 Scientist 检索、验证和实验，并让 Critic 从近邻工作、数据、测量与替代解释攻击当前观点，直到形成可行方向或有依据地转向。

每个项目保留自己的地图、领域文件夹、来源、Gap、Citation Corpus、方案、结果和决策。已有地图会优先读取并复用；新材料进入后可以更新关联结论和下一步。你可以从完整研究流程开始，也可以直接要求“继续查新”“设计 Benchmark”“写 Methods”“回复审稿意见”或“把方法图做成可编辑版本”。

## v1.3 · 真实论文研究和数据验证

现在有可运行的 [原文研究执行器](skills/agent-research-atlas/references/live-research-execution.md) 和 [真实验收记录](docs/v1.3-validation.md)。它们把原有的 Supervisor–Scientist–Critic 方法论连接到**实际 Crossref/ACL 检索、原始 PDF/Limitations 提取、证据与引用记录、有上限的导师决策、官方 BEIR 格式真实检索评测**。原有图谱程序、文献方法论和投稿工作台继续保留。

**实际案例一：2024 ACL 原始论文。** 在线获取 Hsieh et al., *Found in the Middle* 的 14 页原始 PDF，识别四项作者陈述的 Limitation，保留页码、来源哈希和抽取文本哈希；结论只是 **4 个待后续工作核实的 gap 候选**，不是四项已经确认的创新点。对照 2025 EMNLP 相关研究后，Supervisor 在宽泛的“所有 RAG 均有强位置偏差”主张上转向；缺少真实 LLM 回答与成本数据时，不得直接推进新机制实验。

**实际案例二：官方 BEIR SciFact。** 5,183 篇文档、300 条正式测试查询和相关性标注。两种预先给定的 BM25 标题权重（x1 与 x2）都运行了 300 条查询，并从原始标注及预测结果进行 1,800 次独立指标复算。

| 指标 | BM25 标题 x1 | 标题 x2 |
|---|---:|---:|
| Recall@10 | 0.7849 | 0.7908 |
| MRR@10 | 0.6325 | 0.6409 |
| nDCG@10 | 0.6645 | 0.6727 |

nDCG@10 增量 **+0.00824**；300 查询的探索性配对 Bootstrap 95% 区间约 **[−0.00333, +0.01970]**，跨零，**Supervisor 结论为 INCONCLUSIVE**，不宣称方法优势、因果机制或 SCI 新颖性。23 条查询变好，19 条变差，258 条不变。这个测试集已被查看，未来基于它迭代的方法不能把同一结果当独立确认。

```bash
# 一次性获取真实 SciFact 数据（会访问公开数据源）
python skills/agent-research-atlas/scripts/fetch_beir.py --dest /path/to/scifact-snapshot
# 对真实 qrels 和完整测试集运行可重现的两个检索基线
python skills/agent-research-atlas/scripts/retrieval_benchmark.py \
  --data-dir /path/to/scifact-snapshot/scifact --split test --k 10 \
  --output /path/to/project/research-atlas/experiments/scifact-bm25.json
# 查询公开论文元数据，记录实际结果
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project query \
  --topic 'RAG long context positional bias' --output work/crossref.json
# 读取 ACL 原始论文的实际 PDF 并提取候选局限
python skills/agent-research-atlas/scripts/research_cycle.py --root /path/to/project read \
  --paper 'https://aclanthology.org/2024.findings-acl.890.pdf' \
  --id doi:10.18653/v1/2024.findings-acl.890 --output work/hsieh-gaps.json
```

原文 PDF 提取需要系统 Poppler 的 `pdftotext`；在双栏 PDF 上经过真实失败、修复、再运行的验证。引用 BibTeX 采用正式会议类型并保留原稿更正历史。科研导师的 `queue` 需要有来源的 proposal 与 review 输入，**不等于可无人监督自动生成整套独立审查意见**。真实验证/失败日志见 [在线 GitHub Actions](https://github.com/PresleyRen/agent-research-atlas/actions/runs/39965544143)、[研究案例与原文证据](evals/real_research_cycle/README.md)。

## 快速开始

把 `skills/agent-research-atlas/` 作为一个 Skill 安装到兼容宿主；也可以让具有搜索、文件与代码能力的助手先读取其中的 `SKILL.md`。核心本地工具使用 **Python 3.10+ 标准库**；真实 PDF 阅读还需安装 Poppler，按研究任务调用宿主已有的检索、全文阅读、实验和绘图工具。

```text
使用 agent-research-atlas，继续 /path/to/my-agent-project。
我的方向是意图识别、文档检索、路由和回答。
先读取已有地图、综述、论文与失败记录；补中英文检索，
由 Supervisor 明确本轮最关键的问题；Scientist 回原文、查后续工作并更新 Gap Ledger 与 Citation Corpus。
比较最接近的工作、数据与测量可行性，给出值得推进的问题和本地可行的区分性实验；Critic 复核后再决定继续、补查、收窄、转向或停止。
```

按阶段直接提出请求也可以：

| 你现在要做什么 | 可以这样说 | 得到什么 |
|---|---|---|
| 摸清方向 | “整理意图到检索到回答的研究地图，标出进展、争议和未探索部分。” | 有来源的方向图、文献比较与待查问题 |
| 挑选研究点 | “结合现有代码和预算，比较这些点子的最近工作、机制与最小实验。” | 研究简报、竞争解释、可行性与行动决策 |
| 导师式探索 | “像博士导师一样持续指导 Scientist：从原文找真实 gap，反复审查数据和观点，不行就换方向。” | Supervisor 决策、Gap Ledger、Critic 复核、下一任务与 Citation Corpus |
| 做评测研究 | “设计区分意图歧义与知识缺失的 Agent Benchmark。” | 构建与效度方案、独立划分、基线、RQ和分析设计 |
| 做实验 | “按这个已批准计划运行，保留所有结果并更新论点。” | 冻结计划、原始记录、数值核对和结果解释 |
| 写论文 | “基于实际材料写英文 Introduction 和 Methods，另存证据表。” | 可使用正文、引用与证据映射 |
| 修稿与回复 | “核查稿件并逐条回应这些审稿意见。” | 问题位置、修订记录、意见覆盖和完整回复 |
| 做科研图 | “把方法画清楚；参考图做成可编辑 drawio，并检查预览。” | 图稿、源文件、数据/图注与编辑说明 |
| 继续或扩展 | “更新旧地图；定位当前能力不足应该改哪里。” | 受影响记录、待复核项、模块/测试/补法定位 |

## 完整能力说明

研究协议由宿主按实际材料执行；本地脚本负责地图、记录与可重复核查。以下 **32 项能力**都有稳定 ID，可用 `audit.py locate` 查到对应文件、来源、互补能力和验证记录。

| 能力 | 工作与产物 |
|---|---|
| C01 · 范围与领域分类 | 定义问题、研究边界、时间与语言；从14个Agent种子领域起步，随研究扩展分类。 |
| C02 · 持久研究地图 | 发现并复用本地地图；保留原文、人工笔记与历史，生成JSON、Markdown/Mermaid和离线HTML视图。 |
| C03 · 中英双语检索 | 组合中文、英文、同义词和相邻领域查询；记录检索式、渠道、时间、命中与访问状态。 |
| C04 · 论文身份与引用拓展 | 规范DOI/arXiv等身份，去重并保留版本；沿引用链发现相关工作与反证。 |
| C05 · 阅读与结构化抽取 | 先读综述建立方向，再读原始论文，提取问题、方法、条件、结果、局限和具体出处。 |
| C06 · 证据评价与批判 | 区分观察、作者判断和推断，检查测量、比较、偏差与竞争解释，保留争议。 |
| C07 · 选题发散与结构迁移 | 从失败案例、前提变化、邻域方法、反问题与质量/成本取舍产生候选机制。 |
| C08 · 研究问题选择 | 按知识目标、风险、约束、决策树和最小信息检查比较方向，给出推进、修订或暂缓理由。 |
| C09 · 最近工作与创新重叠 | 比较最相近工作的目标、信息、机制、洞察、领域及评估成本，定位具体差异。 |
| C10 · 机制假设与竞争预测 | 把想法写成可观察预测、替代解释和证伪条件，连接证据与实验。 |
| C11 · 本地可行性 | 核对数据权限、标注、代码、算力、评价器和预算，优先解决会改变决策的未知项。 |
| C12 · 方法选择与实现对应 | 按问题选择理论、诊断、比较、干预或测量方法；把方法卡对应到输入、代码、输出和指标。 |
| C13 · 区分性实验设计 | 设计简单/强基线、消融、公平信息与预算、独立样本、划分、指标及正/负/不确定结果的解释。 |
| C14 · 冻结计划与修订 | 保存前瞻计划与指定输入哈希；支持候选文件迭代，并记录评价器和数据变更。 |
| C15 · 有预算的实验执行 | 运行已授权的本地命令，保留运行预算、失败、超时、取消与原始输出；也可导入外部结果。 |
| C16 · 结果来源与数字核对 | 保存来源、版本、哈希和日志；按JSON Pointer核对稿件数字、具体字段、容差和大整数。 |
| C17 · 统计推断设计 | 先明确估计目标和独立单位，再选择功效、最小效应、精度、等效/非劣或序贯分析及适用实现。 |
| C18 · 从结果到论点 | 判断结果支持的具体范围，区分实现、测量和机制问题，形成有条件的支持、反证或未决解释。 |
| C19 · 独立审视与对抗检查 | 可用时分离提案与批评上下文，以实际来源和反解释审视最强候选。 |
| C20 · 增量更新与失败记忆 | 保留被否定/暂停方向和重启条件；记录前提变化后追踪受影响的实验、结论、稿件与待复核项。 |
| C21 · 论文论证与引用审查 | 建立论点—运行—图表映射，整理相关工作、方法、局限和复现资料，核查引用身份与引用句含义。 |
| C22 · 外部工具适配 | 按宿主可用工具接检索、全文/PDF、引用上下文、模型评估、训练和云执行，并保存统一回执。 |
| C23 · 能力覆盖与补强定位 | 从症状或C-ID定位负责文件/函数、来源特长、互补对象、冲突和测试；诊断当前项目记录中的缺口。 |
| C24 · 复现与交接 | 汇总研究范围、关键来源、资源、方案、实际结果、失败、地图版本与下一步，支持跨会话继续。 |
| C25 · Benchmark与评估研究 | 形成评估缺口、数据构建、标注与真值、划分/污染、RQ驱动诊断、可选配套方法及维护发布方案。 |
| C26 · 论文成稿与中英润色 | 按贡献类型组织引言和各章，直接输出正文；另存证据表、术语表和改动说明，保持科学含义。 |
| C27 · 投稿前审查与审稿回复 | 按实际稿件定位问题，保留每条原意见，连接证据、行动、修订位置和完成状态，生成完整回复。 |
| C28 · 科研图与可编辑图稿 | 设计动机、方法、结果图；将参考图拆成文字/模块/连线，保存可编辑源、实际预览与编辑说明。 |
| C29 · 科研导师与方向决策 | Supervisor/PI 以论文、数据、可行性和 Critic 结果决定继续、补查、修复测量、收窄、转向、暂存或停止。 |
| C30 · 论文级 Gap 挖掘与状态账本 | 从综述、原始论文、Discussion/Limitations、后续引用与负结果提取 gap，并跟踪 open/partial/solved/invalid/parked。 |
| C31 · 可复用引用证据库 | 保存论文身份、版本、原文 locator、可以/不可以支持的 claim、论文角色和 Atlas 关联，供后续写作直接复用。 |
| C32 · Scientist–Critic 自适应研究循环 | Scientist 执行，Critic 攻击，Supervisor 决策；结果不支持时能回文献、换假设、换方向或停止。 |

## 工作流文本图

```text
项目入口
  → C29 Research Supervisor：定义“哪项未知最可能改变方向”
  → C01/C02 范围与已有地图
  → Scientist: C03 中英检索 → C04 引用图 → C05 综述/原始论文
  → C30 Gap Ledger：作者局限 / 观察局限 / 项目推断 / 搜索缺失
  → C31 Citation Corpus：把可引用证据和不能支持的范围一起沉淀
  → C06 批判综合 + C09 最近工作 → C07/C08 候选方向
  → C10 竞争假设 → C11 数据/测量/资源可行性 → C12 方法卡

Supervisor Gate
  ├─ gap 无效/已解决 → STOP / 换 gap
  ├─ 数据或评价器不能证明观点 → REPAIR MEASUREMENT / NARROW
  ├─ 关键文献不足 → SEARCH MORE
  └─ 可检验 → PROCEED → C13 区分性实验

实证循环
  C14 冻结 → C15 执行 → C16 数字/来源 → C17 统计 → C18 论点
  → C19/C32 Critic 从近邻、数据、泄漏、baseline、机制、解释再次攻击
  → C29 Supervisor：DEEPEN / BROADEN / PIVOT / PARK / STOP
  → 必要时回 C03–C06，而不是随机继续实验

成稿
  C21 论证与引用 → C26 正文/润色 + C28 图稿
  → C27 投稿审查/回复 → C24 复现与交接

贯穿
  C20 新证据/失败记忆；C22 工具适配；C23 缺口与补强定位；C02 持续更新地图
```

## 已整合 Supervisor-Skills（“鸭博士”相关科研技能包）

本项目按正式名称 **[HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)** 归档。已阅读固定版本下的 **12 份 SKILL.md、全部配套 Markdown references 与18份中文手册章节**，将其方法接到已有地图和证据链。具体文件、取舍与阅读记录见 [整合说明](docs/supervisor-source-audit.md)。

| 技能 | 接入的特色 | 能力位置 |
|---|---|---|
| `idea-evaluator` | 贡献类型、投入前关键风险、五维取舍、前提变化和本地资源匹配 | C07–C11 |
| `deep-research` | 研究问题驱动的多视角调研、检索盲区、条件性综合和逐项引用核验 | C03–C06/C09 |
| `vibe-research-workflow` | 科研、实现、绘图与写作的任务分工、方法卡和持续交接 | C12/C15/C24 |
| `tech-paper-template` | 问题—局限—机制—实现—贡献逻辑和方法章节结构 | C12/C21/C26 |
| `intro-drafter` | 按贡献类型组织引言、运行实例和可直接使用的段落 | C26 |
| `paper-writer` | 从现有材料写各章/全文，单独维护论点证据表与引用核查 | C21/C26 |
| `benchmark-paper-template` | 评估缺口、构建、效度、诊断发现和配套方法的完整研究设计 | C25 |
| `paper-polish` | 保持数值、范围和因果强度的语言润色、中译英与术语统一 | C26 |
| `pre-submission-reviewer` | 按论文范式审视论证、测量、比较、表达和复现，定位可修复问题 | C19/C21/C27 |
| `rebuttal-guidance` | 逐条意见拆分、证据与实际修改对应、完整回复和修订覆盖 | C27 |
| `figure-designer` | 按科学用途选图型、数据与视觉编码、图注和可复现绘图 | C28 |
| `drawio-reconstruction` | 参考图逐对象拆解、原生文字与连线、混合媒体和视觉交接 | C28 |

常用工作台：[选题与深度调研](skills/agent-research-atlas/references/supervisor-discovery.md)、[Benchmark/论文/审稿回复](skills/agent-research-atlas/references/supervisor-publication.md)、[科研图与重建](skills/agent-research-atlas/references/supervisor-figures.md)。五个 [项目模板](skills/agent-research-atlas/assets/supervisor) 分别用于研究简报、Benchmark设计、论文证据、审稿回复和图稿交接。

## 新增 Research Supervisor–Scientist 闭环

v1.2 将原有方法提升为明确的三角色架构：[Research Supervision 工作台](skills/agent-research-atlas/references/research-supervision.md)。

- **Supervisor / PI Advisor**：反复追问“原文在哪里、后续有没有解决、数据能否回答、什么结果会推翻、下一步最值钱的检查是什么”。
- **Scientist / Executor**：真正执行搜索、全文阅读、Gap 更新、实验和 Atlas 写入。
- **Critic / Reviewer**：从最近工作、数据、测量、泄漏、强 baseline、替代机制和论点范围找致命问题。

新增 [Gap Ledger](skills/agent-research-atlas/assets/supervision/gap-ledger.md)、[Citation Corpus](skills/agent-research-atlas/assets/supervision/citation-corpus.md) 和 [Mentor Panel](skills/agent-research-atlas/assets/supervision/mentor-panel.md)。`gap` 也是 Atlas 的正式节点类型，可保存 candidate/open/partially_solved/solved/invalid_gap/inaccessible/unknown/parked 状态。来源与冲突取舍见 [v1.2 来源审计](docs/supervision-source-audit.md)。

## 不同来源如何互补

| 来源组 | 贡献 | 与 Atlas 的配合 |
|---|---|---|
| ResearchStudio | 问题发散、论文搜索、最近工作重叠检查 | 候选先入图，再以具体近邻工作检验差异 |
| ARIS | 调研、方案、实现桥接、实验/消融、结果与引用审查 | 把研究问题连到代码、原始结果和论文论点 |
| K-Dense | 文献综述、科学假设、批判思考、实验设计、功效与 research-lookup evidence packet | 给候选、实验和 Citation Corpus 补充研究设计、claim-support/contradict 证据 |
| Kalaris autoresearch | 文献 bootstrap、实验 inner loop、综合 outer loop、pivot 回文献 | 接入 C32，但不继承“never stop”或无人授权后台循环 |
| Gap Finder | source→theme→gap、矛盾和弱证据显式化 | 接入 C30，并由 later work/可行性门判断 gap 是否真实仍开放 |
| MentorForge | 从真实研究者公开论文提炼 research taste 与 evaluation standards | 接入 C29 Mentor Panel，只保留有公开证据的重复信号，不模拟私人意见 |
| Orchestra / Anthropic / Research-Equality | 创意操作、问题选择、风险和决策树、研究循环 | 根据当前卡点选择方法，保存分支与决策理由 |
| Supervisor-Skills | 研究指导、Benchmark、成稿润色、审稿回复与图稿 | 将探索和实验产物组织成完整的研究与写作交付 |
| 中英文检索与引用服务 | 论文身份、全文、引文关系、证据上下文与结构化提取 | 多渠道检索与回执共用论文 ID 和来源记录 |
| Hugging Face / 自动科研系统 | 数据、评估、训练、日志、云作业与执行流程参考 | 按可用环境接适配器，回收版本、结果和资源记录 |
| Atlas 本地工具 | 地图、冻结输入、运行记录、影响传播、数值与缺口定位 | 为上述方法提供可持续复用的项目状态 |

整合后的方法以实际研究设计裁决分歧：先确认测量与比较是否有效再解释负结果；Benchmark 可以以测量贡献为中心；论文模块允许多对多对应；正文与工作证据表分别保存；回复对应每条技术意见；图形编码服从数据单位和方向。完整 [312 项特征及32类冲突](docs/coverage-audit.md) 记录每一项的采用方式、互补对象和后续补法。

## 研究方向与双语来源

内置起点覆盖意图与目标、歧义澄清、路由、规划、文档摄入检索、RAG与回答、工具使用、记忆、多智能体协作、评估、可靠性安全、成本效率、数据与适应等领域；可继续添加具身、多模态、人机协作、强化学习与形式化验证方向。每个领域保存探索状态和具体来源。

检索词同时包含中文、英文、缩写与邻域术语。可使用宿主搜索及 OpenAlex、Semantic Scholar、Crossref、arXiv、DBLP、OpenReview、ACL Anthology、ChinaXiv、中文期刊、CNKI、万方等适用入口；全文与账号渠道取决于当前可用权限。引用上下文、批量抽取和本地论文问答可通过 Scite、Elicit、Undermind、PaperQA 等适配。见 [双语检索协议](skills/agent-research-atlas/references/bilingual-retrieval.md)。

## 本地地图与工具

研究目录内通常保存：`atlas.json` 及历史、总览与分领域地图、`domains/<id>/notes.md` 人工笔记、来源与检索记录、gap、导师决策、Citation Corpus、假设/决策、冻结实验与结果，以及论文/Benchmark/回复/图稿工作文件。JSON 是可维护状态；Markdown/Mermaid 和离线 HTML 便于阅读。每次正式写入更新视图，记录的前提变化会生成下游复核清单。

```bash
# 在仓库目录下；项目路径换成你的实际目录
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project discover
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project init --title "Agent research"
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project status
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/project queries --domain routing --focus-zh "意图歧义" --focus-en "intent ambiguity"
python skills/agent-research-atlas/scripts/audit.py --root /path/to/project project
```

更多命令与记录格式：[地图](skills/agent-research-atlas/references/local-atlas.md)、[实验](skills/agent-research-atlas/references/experiments.md)、[证据与论点](skills/agent-research-atlas/references/evidence-and-claims.md)。

## 快速定位不足并扩展

```bash
python skills/agent-research-atlas/scripts/audit.py locate --query "C29"
python skills/agent-research-atlas/scripts/audit.py locate --query "C30"
python skills/agent-research-atlas/scripts/audit.py locate --query "C25"
python skills/agent-research-atlas/scripts/audit.py locate --query "润色"
python skills/agent-research-atlas/scripts/audit.py locate --query "drawio"
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

| 发现的不足 | 从这里定位 | 典型补法 |
|---|---|---|
| 文献覆盖/中文术语不足 | C01/C03/C05 | 扩术语和来源；用实际检索回执与全文定位验证 |
| 想法缺乏机制或近邻比较 | C07–C10 | 补前提历史、最强近邻和可区分预测 |
| 实验条件/统计不清 | C11–C17 | 明确资源、独立单位、信息/成本和分析设计 |
| Benchmark 的构建或测量不足 | C25 | 补构念、谱系、真值、划分、污染与诊断实验 |
| 正文/润色没有保留原科学含义 | C26 | 查具体句子的来源、数字、范围与因果强度 |
| 审稿意见漏答或修改不对应 | C27 | 原意见 ID 到证据、行动、位置、状态逐项核对 |
| 图不能编辑或预览不正确 | C28 | 分开检查对象、连线、渲染、数据与编辑范围 |
| 新证据影响旧结论 | C20/C23 | 查依赖路径，更新记录并完成实际复核 |
| 论文写了局限但不知道是不是研究点 | C30 | 建 Gap Ledger；查 later work、边界、反证、数据和最小判别实验 |
| 想要导师持续鞭策和方向决策 | C29/C32 | Supervisor 下任务→Scientist 执行→Critic 攻击→Supervisor 再决策 |
| 论文很多但以后写作无法复用 | C31 | 保存稳定身份、locator、支持/不支持的 claim 和 manuscript role |
| 想引入真实教授方法视角 | C29 | 只从公开论文/材料提炼重复方法信号，记录 direct/inference/speculative 等级 |

扩展时沿“症状 → C-ID → 负责文件 → 来源特长/冲突 → 最小修复 → 回归任务”推进。注册表维护 **81 个来源、312 项特征、32 项能力、32 类冲突**的对应关系；[扩展指南](docs/EXTENDING.md) 提供 provider、方法、执行后端和新工作台的做法。

## 验证与复用

[真实论文 Gap/引用审查样本](evals/real_literature/README.md) 基于五篇真实论文，专门检查后续缓解论文和相反研究结果是否被保留，而不是将检索缺失或 Future Work 直接当创新点。


```bash
python -m unittest discover -s tests -v
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

确定性套件扩展至 **原有 109 项加 v1.3 新增的单元与集成测试**；准确数量以对应提交的 CI 记录为准，覆盖旧图复用、身份去重、状态与来源、冻结输入、预算/失败记录、依赖更新、数值核对和扩展引用。另有独立上下文的项目任务，保留实际产物和冲突处理结果。[验证总表](docs/validation.md)、[原有任务记录](docs/forward-conflicts.md)、[Supervisor 整合任务](docs/supervisor-validation.md) 与 [可重用夹具](evals/README.md) 给出各自执行范围和结果。

本项目用于支持严谨选题、检验与写作；新颖性、方法有效性和发表判断依据真实文献、实验和同行审查。SCI/SCIE、期刊或会议适配在具体投稿任务中核对当前规则。

## 许可与致谢

Atlas 核心代码与原创协议采用 [MIT](LICENSE)。Supervisor 衍生的三份工作台和五个模板采用 **CC BY-NC-SA 4.0**，署名 Yuyu Luo（骆昱宇）及贡献者，并注明本项目改编；具体范围见 [许可与第三方说明](THIRD_PARTY_NOTICES.md)。完整来源、版本和采用位置见 [SOURCES](SOURCES.md)。
