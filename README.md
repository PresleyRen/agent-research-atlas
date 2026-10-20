# Agent Research Atlas

**把文献探索、研究问题、可检验假设、实验和论文论点，放进一张能够持续维护的科研地图。**

[English](README.en.md) · [完整技能](skills/agent-research-atlas/SKILL.md) · [方法来源](SOURCES.md) · [测试说明](docs/validation.md)

Agent Research Atlas 是面向智能体研究的中英双语 Skill。它指挥具备搜索、文件读写和代码执行能力的 AI 助手，沿着“读综述与原始论文 → 建立研究地图 → 找问题与最近工作 → 评估可行性 → 设计区分性实验 → 记录结果与反证 → 形成证据支持的论文论点”开展工作。

同时提供两个只依赖 Python 标准库的工具：`atlas.py` 管理持久图谱，`experiments.py` 管理冻结计划、预算和实验记录。项目目录是长期记忆，后续会话可以接着已有进度研究。

**目标是帮助发现值得研究、能实施、能被检验的问题。新颖性、科学成立和录用仍需要真实文献、实验及同行判断。** 这不是承诺自动发表 SCI 或顶刊的软件，也没有把模型自评分当作发表概率。

## 能做什么

| 能力 | 实际工作与产物 |
|---|---|
| 综述起步与领域梳理 | 读相关综述，建立问题定义、方法谱系、进展、分歧、未解决问题和证据位置；回到原始论文核实关键判断。 |
| 中英文检索 | 分别构建中文与英文术语、相邻领域词及查询；覆盖综述、最近似工作、负面证据、数据集与评测。记录实际日期、来源、查询、结果与失败。 |
| 最近工作与查新 | 对比目标、决策时可见信息、机制、评测、成本及贡献差别；前后向引用拓展；结论限定在已执行搜索范围。 |
| 科研点发现 | 从失败模式、矛盾、假设变化、评价缺陷、机制迁移、成本与效果取舍等角度生成候选；避免把模块组合直接写成创新。 |
| 可行性评估 | 核实本地数据、代码、算力、评价器和预算；未知资源保留 unknown/unverified；先安排低成本关键检查。 |
| 方法选择 | 按问题选择理论分析、反例、误差分析、比较实验、消融、因果/反事实检查、鲁棒性、统计估计或数据/指标研究。 |
| 实验设计 | 写明假设、竞争解释、强/简单基线、实验单位、数据划分、指标、控制变量、重复、预算、成功/失败/不确定条件。 |
| 实验执行与导入 | 在已有授权下执行检查过的本地 argv 命令，或导入外部结果；保留原始日志、退出码、超时、失败和取消记录。 |
| 计划冻结与溯源 | 保存冻结计划的 SHA-256、时间和前瞻/探索声明，记录明确列出的代码/数据文件哈希；检测冻结后的改动。 |
| 结果到论点 | 区分支持、部分支持、不支持、不确定和机制未排除；论点链接实际实验/论文，不根据“程序运行成功”宣布假设成立。 |
| 本地研究地图 | 一个 JSON 真源，生成 Markdown 总览、分领域 Mermaid 图，以及可筛选、可点选的离线 HTML 关系图。 |
| 旧项目续接 | 自动复用已有原生图谱；遇到其他格式先阅读、保留原文与哈希，再由助手语义归一化；不盲目覆盖旧地图。 |
| 增量更新与失败记忆 | 稳定 ID、修订号、冲突检查、历史快照、保留手写 notes；已暂停、被反驳、失败方向保留原因和重启条件。 |
| 论文论证准备 | 输出最近工作表、贡献边界、实验协议、真实结果图表、claim–evidence 对应、局限和复现步骤；可继续准备稿件。 |
| 可选独立审查 | 宿主支持时分开提案与查新/反证评审；单上下文回看明确标为自审。 |

上述研究判断由宿主 AI 结合实际来源完成。脚本负责状态、链接、路径和记录完整性，**不会自动判断文献是否为真、机制是否成立或设计是否足以发表**。

## 默认覆盖的 Agent 方向

初始目录包含以下 **14 个可扩展种子域**；初始化时全部是 `unsearched`，不会凭空生成已读论文或领域进展。

| 方向 ID | 研究范围 |
|---|---|
| `intent` | 意图理解、多意图、分布外意图、开放集与标注歧义 |
| `clarification` | 澄清问题、主动获取信息、拒答与人机协作 |
| `routing` | 任务/模型/工具/检索路由、校准、不确定性与预算 |
| `planning` | 任务分解、规划、约束、搜索、反思与重规划 |
| `ingestion-retrieval` | 文档摄入、切分、索引、检索、时效与权限条件 |
| `reranking-context` | 重排、证据选择、上下文压缩与长上下文干扰 |
| `knowledge-graphs` | 知识图谱、结构化检索、GraphRAG、实体与关系 |
| `memory` | 短/长期记忆、更新、遗忘、版本和跨会话一致性 |
| `tool-use` | 工具选择、调用、状态、失败恢复和执行反馈 |
| `answer-grounding` | 回答生成、证据归因、引用、忠实性和不确定性 |
| `multi-agent` | 协作、通信、分工、争论及多智能体评测 |
| `evaluation` | 任务成功、数据与评价器、污染、重复性和 OOD |
| `production` | 延迟、费用、可靠性、可观测性及线上反馈 |
| `safety-security` | 提示注入、权限、隐私、工具安全与可靠执行 |

它不限于文档 RAG，也允许新增具身、多模态、强化学习、形式化方法或其他学科节点。扩展目录见 [Agent 领域说明](skills/agent-research-atlas/references/agent-domains.md)。种子域是组织方式，不是“整个 Agent 领域已经探索完成”的声明。

## 如何使用

### 1. 安装或直接读取 Skill

克隆仓库：

```bash
git clone https://github.com/PresleyRen/agent-research-atlas.git
cd agent-research-atlas
```

安装目标是 `skills/agent-research-atlas` 这个目录，而不是仓库顶层。支持 `SKILL.md` 的宿主可以按自己的官方安装方式加载它。

在允许用户自定义本地技能的 Codex 环境中，可把该目录放到 `~/.codex/skills/agent-research-atlas`；Claude Code 等宿主使用各自的用户/项目技能目录。已有同名技能时先比较版本，不直接覆盖。受管理的聊天环境是否允许持久安装取决于它提供的权限；GitHub 发布不等于已经装进每个会话。

不安装也可在具备本地文件访问的助手中明确指定：

> 阅读 `/绝对路径/agent-research-atlas/skills/agent-research-atlas/SKILL.md`，使用这个技能处理我的项目 `/绝对路径/agent-project`。

宿主需要实际的搜索工具才能联网找论文；需要实际的文件/执行工具才能运行脚本。只有文本聊天能力时，可以提供研究方案，不能声称完成了本地文件操作。

### 2. 给它一个研究任务

**从领域探索开始：**

> 使用 $agent-research-atlas。我的方向是 Agent 的意图识别、路由、文档检索和回答。先检查项目中的已有地图与实验，再做中英文综述和原始论文检索，整理研究进展、分歧和未解决问题。选择三个有机制、有最近工作对照、适合我本地资源的候选问题，给出最小区分性实验，保存地图与来源。

**继续已有项目：**

> 继续这个项目，先阅读已有地图、失败方向和资源约束。把最近的新论文加入图谱，检查哪些假设或计划需要修订，并说明这次新增证据改变了什么。

**带着具体问题：**

> 我想研究检索前的不确定性校准是否能改善 Agent 的路由。请先查找最近似方法和反证，把机制差异说清楚，再判断现有数据能否区分“校准改善决策”和“只是调用了更强模型”两种解释。

**进入实验：**

> 针对图谱里的某个 hypothesis，检查当前资源和实验代码，设计并冻结比较协议。在我给定的本地预算内运行，保存所有失败和结果，更新论点与下一步决定。

不要把敏感项目、未公开论文或用户数据复制到这个公共工具仓库；研究状态存入你单独的项目目录。

### 3. 本地地图工具

Python 3.10+，没有 pip 依赖。下面假设已在仓库根目录，并且 `/path/to/agent-project` 是已存在的研究目录：

```bash
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project discover
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project init --title '我的 Agent 科研'
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project status
python skills/agent-research-atlas/scripts/atlas.py --root /path/to/agent-project check
```

有旧地图时先阅读，再使用 `adopt --file docs/原地图.md`；有多个原生地图时明确 `--atlas-dir`。增量写入使用 `upsert --file batch.json --expected-revision N`。完整字段与命令见 [本地图谱协议](skills/agent-research-atlas/references/local-atlas.md)。

生成的典型项目结构：

```text
agent-project/
  research-atlas.config.json
  research-atlas/
    atlas.json
    MAP.md
    map.html
    domains/<方向>/MAP.md
    domains/<方向>/notes.md
    papers/ hypotheses/ experiments/ claims/ explorations/ imports/
    history/
```

`map.html` 可本地打开，按中英文文本、方向、类型、状态筛选，点节点查看证据与关联。无 CDN、无需上传项目数据。为保证可读性，图中最多绘制前 140 个匹配节点，完整匹配索引仍保留，并显示截断提示；缩小筛选即可查看其余节点。

地图在每次成功更新后重新生成，刷新页面查看。它没有偷偷运行的后台监听器；要定期更新需要宿主另外提供并授权调度能力。

### 4. 实验记录工具

先按照 [实验协议](skills/agent-research-atlas/references/experiments.md) 编写计划；可参考 [示例 JSON](skills/agent-research-atlas/assets/experiment-plan.example.json)。

```bash
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project plan --file plan.json
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project freeze experiment-id --mode exploratory --rationale '首次探索，尚无独立确认数据'
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project run experiment-id --run-id seed-7 --seed 7 --authorized-local
python skills/agent-research-atlas/scripts/experiments.py --root /path/to/agent-project validate-record experiment-id
```

只有你已经授权的、检查过的命令才能执行。`--authorized-local` 是对此前授权的声明，不是权限授予或操作系统沙箱。脚本使用结构化 argv 和 `shell=False`，记录超时与预算，但不能限制子程序访问网络、写其他目录或消费外部服务；需要更强隔离时使用项目已有容器/沙箱。

执行成功只表示退出码为 0。结果的科学解释保留 `not_assessed`，由研究者检查实验、竞争解释和不确定性。外部集群或框架的结果可通过 `import-result` 导入，保留原字节和来源。冻结后的新协议用新实验 ID，避免覆盖历史。

## 哪些方法论会使用

| 问题 | 合适方法 | 要回答的关键问题 |
|---|---|---|
| 领域进展散乱 | 范围综述、分类矩阵、引用拓展 | 哪些结论针对同一设定，哪些只是表面相似？ |
| 不知道突破点 | 失败分析、假设审计、矛盾/取舍分析 | 哪个未解决条件重要且有可检验机制？ |
| 怀疑只是换组件 | 最近工作比较、简单基线、机制消融 | 差异来自哪里，是否超出工程调参？ |
| 结果看似有效 | 配对比较、效应量/区间、重复、预算匹配 | 差异稳定吗，是否有混杂或评价器偏差？ |
| 想论证机制 | 竞争预测、干预、反事实或适当因果设计 | 结果能否排除更简单的替代解释？ |
| 声称通用 | 分布外测试、压力测试、失败分层 | 在什么任务、数据、模型或成本条件下失效？ |
| 理论命题 | 定义与假设、推导、证明检查、反例 | 结论是否在明确条件下成立？ |
| 数据或评测贡献 | 标注一致性、测量效度、污染审计 | 测量对象是什么，是否反映真正任务成功？ |

这是一套选择方法和核查证据的流程，不声称自动精通所有学科的方法。专业统计、形式化证明、领域知识或硬件实验超出宿主能力时，要明确缺口并使用适当工具/专家。

## 检索来源与可选工具

默认使用宿主可用搜索与官方原文：arXiv、ACL Anthology、OpenReview、DBLP、OpenAlex、Semantic Scholar、Crossref；中文使用相关期刊、ChinaXiv 及有权限时的知网/万方等入口。语种之外还会扩展到任务型对话、信息检索、决策、规划等相邻术语。

Undermind、Elicit、Scite、PaperQA2 等是可选增强路径，**并未随仓库安装或完成账号接入**。不要求订阅全部服务，也不绕过付费墙。找到元数据不等于读过全文，文献图相邻不等于机制得到验证。详细策略见 [双语检索](skills/agent-research-atlas/references/bilingual-retrieval.md)。

## 验证与真实边界

运行本地测试：

```bash
python -m unittest discover -s tests -v
```

验证覆盖图谱复用、原文/笔记保留、修订冲突、证据状态要求、路径处理、预算、冻结篡改、失败/超时保留等；另有独立上下文的旧项目续接和双 seed 实验流程测试。详见 [验证记录](docs/validation.md)。

真实中英检索小样记录在 [retrieval-smoke.md](docs/retrieval-smoke.md)，包括成功打开的原始论文记录、摘要读取深度和访问失败。它不是全领域查全率测评。

以下能力没有因此得到证明：候选想法一定创新、所有文献均已覆盖、实验结论一定正确、显著提高研究成功率、获得 SCI/顶刊/顶会录用。示例实验全部标记 **SYNTHETIC**，没有真实 Agent 模型或私有科研数据。本地哈希也不是不可篡改的外部认证，不能检测所有历史整体删除。

## 设计来源与许可证

原创整合参考了 ResearchStudio-Idea、ARIS、K-Dense、Orchestra、Anthropic scientific-problem-selection，以及 AIRAS 等自动科研系统的流程经验。保留适用方法，调整了“自动评分即创新确认”“昂贵实验默认运行”等不适合通用环境的假设。具体阅读深度、对应能力、限制和原始科学文献见 [SOURCES.md](SOURCES.md)。没有把这些上游仓库整体复制进来，也无需全部安装。

本项目原创代码和文档采用 [MIT License](LICENSE)。链接的论文、数据、产品及上游技能保留各自许可。这个项目由用户控制其研究方向、资源和公开范围。
