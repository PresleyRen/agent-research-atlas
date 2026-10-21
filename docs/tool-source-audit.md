# 工具、自动科研系统与扩展能力审计

核验日期：**2026-10-20**。这份审计解释哪些特点被保留、哪些只能通过外部服务获得、哪些建议经过调整，以及以后怎样定位缺口。逐特征记录见 [tool-source-manifest.json](tool-source-manifest.json)；它可与主能力注册表按 `C01`–`C24` 关联。

## 审计结论与边界

v1.0.0 已参考主要检索和自动科研来源，但来源表粒度不足：读过产品文档、采用工作流思想、具备同类本地功能、已连接远端服务四种情况没有逐特征展开。此次补充 **39 个来源条目、85 个特点**：16 个检索入口、7 个自动科研参考、9 个 Research-Equality 技能，以及 7 个 Hugging Face 扩展候选。方法类原始技能的审计另见同目录方法审计文件；不要把两份报告中的重叠来源重复计成独立能力。

这些条目包含 `protocol` 33、`optional` 37、`reference` 6、`deferred` 3、`rejected` 6。这里故意没有把任何外部服务写成已实连的 `implemented`：Atlas 的原生图谱、去重与实验记录有自己的代码和测试，其存在不能证明这些服务接口已经接通。

| 状态 | 本报告中的含义 |
| --- | --- |
| `protocol` | 已在 Atlas 工作流中采用，由宿主按证据执行；并非完整实现上游软件 |
| `optional` | 官方能力已核对，按现有权限可选接入；本项目未执行该远端通路或上游运行时 |
| `reference` | 理解其设计与取舍，用作对照；未复制其系统或性能 |
| `deferred` | 已列入范围但当前需求不适用、缺专门资源或尚未完成相应细节审计 |
| `rejected` | 明确拒绝继承有问题的默认项，并保留替代处理 |

**全文阅读范围：**Research-Equality 所列 9 个 `SKILL.md`、Orchestra 的 `0-autoresearch-skill/SKILL.md` 已逐文件读完；并不包含它们引用的全部模板、脚本和文献。其余条目的具体阅读范围、官方 URL、文档版本或 Git blob SHA 都写入机器清单。Git blob SHA 标识读到的文件内容，不代表整个仓库已按该提交复现。Hugging Face 条目主要检查本会话可用技能的范围与工作流章节，并核对公开入口，不声称逐包源码审计。

## 检索入口：各自保留什么，怎样互补

表中短 ID 加 `SRC-` 即机器清单的来源 ID。当前全部远端账户、调用额度和全文权限仍须按实际连接情况确认；没有原生连接器时可用宿主公开检索和合法本地文件继续。

| 来源 ID / 官方来源 | 已明确的特点 | 互补方式与尚未接通的部分 |
| --- | --- | --- |
| UNDERMIND / [MCP](https://www.undermind.ai/mcp) | 复杂目标深搜、引用和作者拓展、批量元数据定位、PDF/图表问答、远端搜索记忆/笔记/目录、展示卡片 | 深搜提供候选，本地 Atlas 保留来源和方向历史；远端工作区同步与卡片未测试，停止搜索不等于查全 |
| ELICIT / [REST v2](https://docs.elicit.com/) / [MCP README](https://github.com/elicit/api-examples/blob/main/integrations/mcp/README.md) | 语义/关键词检索，摘要和全文筛选，证据字段/图表抽取，阶段导出；异步报告与 Research Agent、配额恢复、文库/项目/调度 | 补证据表和有阶段记录的综述；REST 与 MCP 工具集合不能推定相同，未使用付费账户；临床试验检索列为领域扩展 |
| SCITE / [MCP](https://scite.ai/mcp) | 引用全文语境、引用类别、机构 holdings 和 collection/monitoring | 补主动反证；分类不能替代原文核对，机构全文和监测均未接入 |
| PAPERQA / [README](https://github.com/Future-House/paper-qa) | 本地材料索引、检索/重排/上下文摘要/答案、contracrow、多源元数据、多模态和非英语解析配置 | 补已收集文献的深读，外部发现仍需其他入口；未安装或执行其解析和模型运行时 |
| OPENALEX / [Agent 文档](https://help.openalex.org/access/agents/) | 学术图谱、可复跑查询与元数据；API、CLI、connector、snapshot/sync/fulltext 等不同入口 | 补系统查找与刷新；各访问层的权限/配额不同，当前没有内置 API 客户端 |
| S2 / [Graph API](https://api.semanticscholar.org/api-docs/) / [推荐 API](https://api.semanticscholar.org/api-docs/recommendations) | 学术元数据、引用和参考文献、positive/negative seed 推荐、下载数据和 snippet | 补精确论文及邻域；推荐的 negative 表示不相关，不能用来剔除相关反证；未运行本项目 API 检索 |
| RESEARCHRABBIT / [官方功能说明](https://learn.researchrabbit.ai/en/articles/12865509-researchrabbit-free-tier) | 多种子发现、引用图、集合/子集合、Zotero 与 BibTeX 交换、笔记/共享 | 图邻近拓展术语搜索盲区；本次未核实通用官方 API/MCP，导出后可按来源归一化 |
| CROSSREF / [REST](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | DOI、出版元数据、关系与更新线索 | 补标识核对；原生 Atlas 归一化 DOI 不等于内置 Crossref 请求 |
| ARXIV / [API manual](https://info.arxiv.org/help/api/user-manual.html) | 字段查询、Atom、排序分页、版本和可得 PDF/HTML | 补最近预印本；与正式发表记录关联，不把版本重复计独立证据 |
| DBLP / [API](https://dblp.org/faq/How+to+use+the+dblp+search+API.html) | 计算机论文/作者/venue 消歧、查询分页 | 补跨 NLP 的计算机元数据；全文结论另读原始论文 |
| OPENREVIEW / [官方文档](https://docs.openreview.net/) | 投稿版本、公开评审、rebuttal、决定及 track | 补审稿争议和发表状态；公开投稿页不代表被录用 |
| ACL / [Anthology](https://aclanthology.org/) | NLP/Agent 论文卷、原始文章页、作者/PDF/标识 | 已实际打开文章的元数据/摘要；补英文原始来源，不能扩写成全域全文阅读 |
| CHINAXIV / [门户](https://www.chinaxiv.org/) | 中文及相关预印本和版本线索 | 已核对入口，未做库内系统检索；与正式中文期刊记录互补 |
| CNKI / [入口](https://kns.cnki.net/) | 中文期刊、会议、学位论文补查 | 本次受阻且无已验证订阅检索，保留未覆盖，继续公开期刊/机构/作者页 |
| WANFANG / [入口](https://www.wanfangdata.com.cn/) | 中文学术元数据、期刊及学位论文 | 门户可见不代表原生检索或全文成功；按实际访问记录边界 |
| ZH-JOURNALS / [实际已读文章](https://www.china-simulation.com/CN/abstract/article/1004-731X/3623) | 中文原始综述、出版字段、英文原始工作的交叉核对 | 有真实文章通路记录，部分其他期刊入口失败；逐条访问和阅读深度见 [检索通路记录](retrieval-smoke.md) |

## 自动科研系统：可移植的环节与真实缺口

| 来源 ID / 官方来源 | 特点 | Atlas 的选择及未实现项 |
| --- | --- | --- |
| AIRAS / [README](https://github.com/airas-org/airas) | 阶段契约、预先声明、追加记录、外部评价器、数值引用校验、GitHub Actions/Seyval 执行及论文构建 | 采用阶段交接、冻结与记录思想；Atlas 本地文件哈希不等于它的独立存储和分支门禁，没有部署其后端或验证全链 |
| AUTORESEARCH / [README](https://github.com/karpathy/autoresearch) | 固定训练时间/评价器、限定可改脚本、保留/丢弃/崩溃循环 | 采用对齐预算与评测的原则；不默认需要 GPU，不继承关闭权限建议，不声称本地 runner 是训练搜索器 |
| ORCHESTRA-LOOP / [Skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/0-autoresearch-skill/SKILL.md) | 快实验内循环与回看结果/文献/方向的外循环、领域技能路由、叙事和进度材料 | 保留迭代和反思；不默认开无限循环、定时任务或发送外部消息；领域工程技能需要独立接入与测试 |
| AI-RESEARCHER / [README](https://github.com/HKUDS/AI-Researcher) | 给定想法实施、参考论文出发两入口；资源收集、实现/验证/写作及代理评价 | 保留入口分流与阶段工件；Docker/GPU 完整链未运行，引用量/代理评分不作有效性认证 |
| AI-SCIENTIST-V2 / [README](https://github.com/SakanaAI/AI-Scientist-v2) | 开放选题、实验树搜索、分支调试、研究稿；说明强模板与广泛探索的取舍 | 借鉴分支记录与预算控制；没有实现该树搜索，也未做其性能复现；workshop 个案不是本项目录用保证 |
| IDEASCIENTIST / [README](https://github.com/jiarui-liu/IdeaScientist) | 同问题缺口→邻域机制→提案；结果遮蔽文库、时间截止、角色工具隔离、逐角色 RL | 采用任务分工与结构迁移，未建专用索引、训练策略或实施硬隔离；README 的 CC BY-NC 4.0 提醒后续复制须单独核许可 |
| GOOGLE-COSCIENTIST / [官方文档](https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve) | 生成/反思/排名/演进/近邻/元评审与 supervisor | 作为角色设计参考；受限 Preview 未接入；同页 AlphaEvolve 入口不表示已经审计其全部算法细节 |

自动记录、独立存储、实验设计有效性是不同能力。采用 AIRAS 的记录思想后，仍需检查泄漏和设计偏离；采用 autoresearch 的预算优化后，仍需问改善是否解释机制；采用树搜索后，仍需保留所有分支与多重选择影响。这里没有运行完整上游系统的同题对照，所以没有“某一套科学发现效果普遍最好”的排名。

## Research-Equality：9 个具名技能全部显式核对

原先遗漏了 [RE-idea-generation](https://github.com/Research-Equality/RE-idea-generation) 的独立工作流特点；此次读完其 9 个 `SKILL.md`。它收集了部分上游快照，也增加了自己的路由与阶段产物。重复来源不重复计有效证据，快照不能默认等于原仓库最新版本。

| 来源 ID / 具名技能 | 保留的特点 | 调整、互补和边界 |
| --- | --- | --- |
| RE-BRAINSTORM / brainstorming-research-ideas | 十种选题视角、发散/筛选/细化、所有候选的理由 | 按瓶颈选择视角；固定候选数量和两周 pilot 由实际预算替代 |
| RE-CREATIVE / creative-thinking-for-research | 八种思考操作：组合、重述、类比、约束、反向、抽象、可行边界、矛盾综合 | 结构映射必须产生区分性预测；不继承未经核实的历史/理论示例或完成框架就有发表价值的推断 |
| RE-SCIENTIFIC-BRAINSTORM / scientific-brainstorming | 对话探索、六类发散技术、连接形成、建设性评价和后续技能分流 | 用户信息已充分时直接推进；关联的 SCAMPER/TRIZ 等教程不在本次全文阅读范围 |
| RE-HYPOTHESIS / hypothesis-generation | 观测/解释/猜想分开、竞争机制、可区分预测、最便宜的检验 | 与开放发散互补；真实资源门槛闭合后再进入实验 |
| RE-CRITICAL / scientific-critical-thinking | 论点证据、设计、偏差混淆、统计、证据质量五视角，批判转明确问题 | 不机械套一种证据层级；每项重大问题说明影响、余下不确定性与修补 |
| RE-IDEA / idea-generation v2 | topic-first / template-grounded 双入口；读现有代码/基线/失败，寻找假设、可干预代码位置、缺失基线和切片 | 补“已有可运行项目该从哪找问题”；数值评分和 `novel=true` 不当认证，不默认重构项目 |
| RE-NOVELTY / novelty-assessment | 分轮定向查重叠、批判和最相近工作的差异 | 不保留“至少几轮后就 novel/high confidence”；改为有检索边界的差异结论和不确定项 |
| RE-IDEATION / ideation | 发散、收敛、记录、仲裁、可选事实研究分工，会话 lineage 与继续 | 采用足够的分工，有限预算；同上下文模拟不称独立审查，不采用 exhaustive 无固定上限 |
| RE-DIRECTION / direction-evolution | memory-update 与 stage-reflection；区分方向问题和实现问题，按指标/混淆/数据/基线/运行分诊 | 补“之后快速找短板”；用原始证据选最小诊断，保留模糊和失败方向的重启条件 |

## Hugging Face：适合 Agent 实验的 7 个扩展候选

它们是本会话可用的相关技能入口，不是 Atlas 的强制依赖，也没有因被列在这里就自动安装、运行、训练或发布。公开 skill 目录曾与本会话包清单不同：`huggingface-jobs` 包可用，但本次公开 `huggingface/skills/skills` 目录未见同名项，因此其公开来源链接使用官方 Jobs 文档；不能捏造同名 GitHub 路径。

| 来源 ID / 技能 | 最有用的扩展能力 | 可补的短板与启用边界 |
| --- | --- | --- |
| HF-PAPERS / [papers](https://github.com/huggingface/skills/tree/main/skills/huggingface-papers) | 论文 Markdown/元数据、关联模型/数据/Spaces、发现与 feed、论文页操作 | 从论文找到可实验资源；Markdown 需检查是否只是主页，热度不认证质量 |
| HF-DATASETS / [datasets](https://github.com/huggingface/skills/tree/main/skills/huggingface-datasets) | split/subset、分页/筛选、Parquet、大小/统计、Croissant、可选上传 | 补数据可行性检查；许可、标签质量、训练/测试隔离仍需独立确认 |
| HF-EVALS / [community-evals](https://github.com/huggingface/skills/tree/main/skills/huggingface-community-evals) | inspect-ai/lighteval、vLLM/HF/accelerate 选择及小样例验证 | 补真实模型评测；该技能不自动负责 Jobs 或评测发布，不能因名称而推定边界 |
| HF-TRACKIO / [trackio](https://github.com/huggingface/skills/tree/main/skills/huggingface-trackio) | 指标时间序列、配置、告警、CLI JSON、dashboard、Space 同步 | 补长训练可观察性；监控图不替代 raw record，同步需明确项目和权限 |
| HF-JOBS / [Jobs](https://huggingface.co/docs/hub/jobs) | UV/Docker 远端 CPU/GPU/TPU、超时、成本、状态/取消、持久化、调度 | 补没有本地算力；任务授权、预算和工件位置明确后再提交；远端不能直接读本地路径 |
| HF-TRAINER / [llm-trainer](https://github.com/huggingface/skills/tree/main/skills/huggingface-llm-trainer) | SFT/DPO/GRPO/reward、数据校验、监控、模型保存和 GGUF | 补明确需训练的研究；不同反馈/标注条件选择方法，上游“立即提交”不扩大用户授权 |
| HF-PUBLISHER / [paper-publisher](https://github.com/huggingface/skills/tree/main/skills/huggingface-paper-publisher) | 论文页索引/认领/显示、模型/数据关联、Markdown/HTML 模板 | 补研究工件交付；Hub 托管、arXiv、会议投稿和 SCI 收录分别核实 |

## 关键冲突及验收依据

以下是应保留的行为选择。协议审计说明为何这样设计；回归、冷启动任务、真实连接器调用是不同层级的测试。**此表不把验收要求冒充已运行结果**，本次实际结果统一看 [validation.md](validation.md)。

| 冲突 | 保留方案 | 验收输入与应观察行为 |
| --- | --- | --- |
| 一个 Boolean 查询发给所有来源 | 保留研究意图，逐接口生成实际查询 | 给同一中英问题和不同接口；S2 relevance 不接收通用 Boolean，Elicit keyword 不混 filters，记录实际查询 |
| negative seeds 误删反证 | 保留相关反证，将“不相关”独立编码 | 给一篇相关但反驳候选的论文；不得将它自动放进不相关过滤集 |
| 空结果、失败、配额与未执行混同 | 使用明确结果状态和原始工件 | 401/429、暂停、分页半途失败与真正零命中分别进入不同状态 |
| 本地 QA 或云 workspace 冒充全球查新 | 每次调用保留实际 corpus/scope | 只有本地论文时允许回答该语料内问题，不能宣布全领域没有相近工作 |
| 强证据分类、热度、评分直接变科学结论 | 分类作线索，原文和实验决定论点 | 仅抽取摘要或工具打分时保持受限结论；相关性或 novelty 标签不能升级假设 |
| 远端记忆覆盖本地图和人工笔记 | atlas revision 加带来源导入 | 旧地图/远端导出对同一观点冲突时，两份保留并写决定，不静默覆盖 |
| 创意开放探索与已有代码约束 | 选择 topic-first 或 template-grounded | 给已有可运行路由器、基线和失败日志；先找可检验代码位置与切片，不默认重建项目 |
| runner 成功与科学支持混同 | 先读评价器、raw record 和 rival | 给硬编码高分或共用评估污染；流程成功可以成立，真实科研结论仍不能升级 |
| 单上下文扮演多个角色与独立审查混同 | 报告真实上下文和证据分离 | 宿主仅单代理时标 serial self-review；不能输出“独立复核通过” |
| 无限循环、默认云算力、论文外发 | 有预算的迭代与明确交接 | 预算不明或用尽时保留计划/记录，完成已授权部分；不得凭上游文件增加收费或外发动作 |

## 以后怎样定位和弥补

先按症状找到能力 ID，再查机器清单中该能力的来源特征、状态、缺口和 remedy。主能力注册表负责把能力映射到当前实现和测试，来源清单负责说明“为什么需要它、借鉴谁、还缺什么”。不要为每个供应商另外建一个相互覆盖的主工作流。

| 症状 | 能力 | 首先检查的位置 | 最小修补 |
| --- | --- | --- | --- |
| 总是只找到热门英文论文 | C03 / C04 | [检索矩阵与查询适配](../skills/agent-research-atlas/references/bilingual-retrieval.md#按来源适配查询--provider-syntax) | 补中文原始入口、旧术语、反证与引用拓展；先检查实际 query 语法 |
| 摘要很多，实验细节无法复核 | C05 / C06 | 同一检索协议的元数据/阅读深度和适配器契约 | 补关键章节定位、可读性检查与一组抽取校准样例 |
| 地图有记录却反复重启失败路线 | C02 / C20 | [本地图协议](../skills/agent-research-atlas/references/local-atlas.md) 与 SRC-RE-DIRECTION | 保存失败条件、实现差异与允许重启的新证据 |
| 产生很多想法，但找不到现有项目能做的 | C07 / C11 / C12 | [方法协议](../skills/agent-research-atlas/references/methodology.md) 与 SRC-RE-IDEA | 以基线/代码位置/缺失切片为入口，形成最小可区分实验 |
| 训练慢、日志丢失、不清楚失败点 | C15 / C16 | [实验协议](../skills/agent-research-atlas/references/experiments.md)、HF-TRACKIO / HF-JOBS | 先完整记录 raw output；需要时独立适配监控或云端输出导入 |
| 新提供商接上后行为互相覆盖 | C22 / C23 | [可选适配器契约](../skills/agent-research-atlas/references/bilingual-retrieval.md#可选适配器契约--optional-adapter-contract) | 固定 envelope 与图谱权威状态，跑成功/失败/重复/语言/矛盾的契约测试 |
| README 说有能力，找不到实际实现 | C23 / C24 | 主能力清单加 [来源机器片段](tool-source-manifest.json) | 为能力补定位、证据级别、测试和下一步；没有代码就如实记 protocol/optional |

需要新工具时，先新增稳定来源和特征 ID、明确所补能力、访问边界与最小回归样例，再选择是否实现。只有真实运行并保留可审查结果后，才能把 optional 改成相应的已测试状态；不能仅因为说明文档完整就改状态。核对当前官方接口后再接入，价格、套餐、字段、模型和公开技能路径都可能变化。

### English note

This is a scoped feature audit, not an evaluation of all upstream repositories or a ranking of their scientific-discovery performance. All nine named Research-Equality `SKILL.md` files were read in full; their entire reference/script trees were not. External services and HF runtime workflows remain optional unless an actual integration record demonstrates otherwise. Feature IDs, source revisions, adoption status, gaps, remedies and complementary sources are recorded in the JSON fragment. Use the main capability registry for code/test locations and the validation report for what was actually executed.
