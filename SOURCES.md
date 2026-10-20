# Sources and design attribution / 来源与设计归因

Audit date: **2026-10-20**. This record distinguishes material actually inspected during development from optional services and claims that have not been validated by this project.

核验日期：**2026-10-20**。本文区分开发中实际阅读的资料、可选工具和本项目尚未验证的效果。这里的“全文阅读”仅指该行明确指定的文件或文档，不代表读完仓库全部文件、重现论文实验或使用过该服务。

## Contents / 目录

- [Scope of attribution](#scope-of-attribution--归因范围)
- [Methodology and skill sources](#methodology-and-skill-sources--方法与技能来源)
- [Automation systems](#automation-systems--自动科研系统)
- [Retrieval tools and data sources](#retrieval-tools-and-data-sources--检索工具与数据源)
- [Original scientific reference](#original-scientific-reference--原始科学方法文献)
- [Conflicts resolved](#conflicts-resolved--整合时解决的冲突)
- [Licenses and limitations](#licenses-and-limitations--许可与边界)

## Scope of attribution / 归因范围

Agent Research Atlas is an original workflow synthesis. It does not bundle upstream SKILL.md files, upstream application source code, research papers, or commercial connectors. The relationships below describe ideas and workflow elements considered during design.

Agent Research Atlas 是原创的流程综合，未打包上游 SKILL.md、应用源码、论文全文或商业连接器。下列对应关系说明设计时参考了什么，以及选择保留或调整的原因。

**Reading depth labels / 阅读深度标签**

| Label | Meaning / 含义 |
| --- | --- |
| Full skill | The named SKILL.md was read in full; referenced resources and the rest of the repository are not implicitly included / 指定 SKILL.md 全文已读，不含自动推定的所有引用文件 |
| Full README | The repository or component README was read; this is documentation inspection, not execution / README 全文已读，属于文档核验 |
| Paper consulted | The stated paper or section was inspected; no independent reproduction is implied / 读过所列论文或部分，不代表复现 |
| Official docs | Product/API documentation was opened and inspected; account access and live integration may remain untested / 官方文档已读，账号与集成未必实测 |
| Metadata + abstract | Only bibliographic fields and abstract support the entry / 仅据元数据与摘要，不夸大为全文阅读 |

Evidence is purpose-specific. A maintainer's README is a primary source for the intended interface, but an author benchmark alone does not establish independent effectiveness. A successful project smoke test establishes only the behavior that it exercises.

证据必须与用途对应：README 可以核实设计接口；作者自评不能直接证明独立效果；通路测试只能说明所测通路。README、论文、产品页与实际运行结果不能混作一种证据。

GitHub links below generally point to moving branches. This audit records the reading date; it is not a commit-pinned archival snapshot. Recheck the relevant revision before installing an upstream component or relying on a changed interface.

## Methodology and skill sources / 方法与技能来源

The development team inspected the specifically named material. No claim is made that every skill in a large collection was read, merged, or tested.

开发中实际检查的是下列明确列出的内容，不宣称某个大型集合的全部技能均已阅读、融合或验证。

| Source and inspected material / 来源与实际阅读内容 | Read depth / 深度 | Contribution to this skill / 本技能中的对应 | Reliability and adaptation / 可信度与调整 |
| --- | --- | --- | --- |
| [Microsoft ResearchStudio](https://github.com/microsoft/ResearchStudio), [idea_spark/SKILL.md](https://github.com/microsoft/ResearchStudio/blob/main/ResearchStudio-Idea/skills/idea_spark/SKILL.md); accompanying [arXiv:2607.04439v1](https://arxiv.org/abs/2607.04439v1) | Named skill and README in full; paper consulted / 指定技能及 README 全文；论文查阅 | Structured exploration, expansion and critical selection of candidate ideas / 系统展开候选思路，再批判筛选 | Preserve evidence-linked candidates; do not treat an idea score or generated proposal as proof of novelty / 候选评分不等于创新认证 |
| [ARIS / Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep): [idea-discovery](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/idea-discovery/SKILL.md), [experiment-plan](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/experiment-plan/SKILL.md), [result-to-claim](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/result-to-claim/SKILL.md) | These three SKILL.md files in full; README for the wider chain / 三个指定技能全文；更大流程据 README | Connect discovery, experimental planning, and evidence-bounded claims / 连接选题、实验计划与证据约束的论点 | Preserve stage artifacts and critical review; do not equate an unattended chain with a complete, correct research process / 保留阶段产物，避免把自动串联当科研有效性 |
| [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills): [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md), [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md), [experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/experimental-design/SKILL.md); [arXiv:2609.00065](https://arxiv.org/abs/2609.00065) | Named skills in full; accompanying paper consulted / 指定技能全文；配套论文查阅 | Explicit hypotheses, alternative explanations, controls, evidence quality / 明确假设、替代解释、对照与证据质量 | General scientific procedures require task-specific metrics and domain expertise; this audit did not establish task-level effectiveness for these skills / 通用流程仍需领域化，本次未验证任务级效果 |
| [Orchestra Research AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs): [brainstorming-research-ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/brainstorming-research-ideas/SKILL.md), [creative-thinking-for-research](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/21-research-ideation/creative-thinking-for-research/SKILL.md) | Both named skills in full / 两个指定技能全文 | Use several ways to explore mechanisms and question assumptions / 多角度探索机制、检查既定假设 | Divergent ideation remains separate from novelty checking; a new combination of components is not automatically a contribution / 发散生成和查新分开，组合不自动构成创新 |
| Orchestra [0-autoresearch-skill/SKILL.md](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/0-autoresearch-skill/SKILL.md) | Named skill in full, reviewed by a collaborating developer / 指定技能全文，由协作开发者审阅 | Bounded experiment iterations and explicit result records / 有边界的实验迭代与结果记录 | Keep budgets, baselines, evaluator separation, and failed runs visible; benchmark gains alone do not establish mechanism / 预算、基线、评测隔离和失败均保留 |
| [Anthropic scientific-problem-selection](https://github.com/anthropics/life-sciences/blob/main/scientific-problem-selection/SKILL.md) | Named skill in full / 指定技能全文 | Evaluate the importance and tractability of a problem, reason about decision branches, and choose informative early checks / 问题价值、可行性、决策分支与高信息量早期验证 | Transfer the method to Agent research, not life-science-specific assumptions or publication expectations / 迁移方法，不照搬生科前提或发表预期 |

Related skills mentioned in upstream READMEs but not named above are background pointers, not implicitly audited dependencies. This project is not an installer for any of these collections.

未在上表列出的上游技能，即使 README 提到，也只是后续线索，不是已审计依赖。本项目不负责自动安装这些集合。

## Automation systems / 自动科研系统

These systems informed the distinction between idea discovery, literature work, bounded experimental search, and end-to-end automation. They are optional reference implementations, not runtime requirements of Agent Research Atlas.

这些系统帮助区分“发现问题、分析文献、有界实验搜索、全流程自动化”。它们是可选参考实现，不是本技能的运行前提。

| Source / 来源 | Inspected / 阅读内容 | Design lesson / 本技能采用的判断 | Boundary / 边界 |
| --- | --- | --- | --- |
| [AIRAS](https://github.com/airas-org/airas) | README in full / README 全文 | Keep literature, idea, experiment, and report stages inspectable / 保留可检查的阶段交接 | Interface and workflow claims were inspected; no full pipeline run here / 未在本项目中完整运行 |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | README in full / README 全文 | Fix a task/evaluator and budget before iterative experiment changes / 迭代前固定任务、评价器和预算 | A constrained optimization loop does not independently choose an important research question / 有界优化不等于重要问题发现 |
| [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | README and paper limitations section / README 与论文局限章节 | Track failures in autonomous execution and evidence handoffs / 关注自动执行和证据交接失败 | Do not extrapolate author-reported runs to reliable general autonomous discovery / 不把作者个案推广为普适发现能力 |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2); [Nature article, DOI 10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5) | README and article consulted / README 与论文查阅 | Separate generation, selection, execution, and external evaluation / 区分生成、筛选、运行与外部评价 | The reported workshop exercise involved selection and a planned withdrawal; it is not evidence of acceptance at the ICLR main conference, nor a general SCI-acceptance guarantee / workshop 案例不等于 ICLR 主会录用或普遍 SCI 保证 |
| [IdeaScientist](https://github.com/jiarui-liu/IdeaScientist) | README in full / README 全文 | Treat automated idea assessment as a source of candidates and critique / 自动观点评估提供候选与质疑 | No independent reproduction by this project / 本项目未独立复现 |
| [Google Co-scientist and AlphaEvolve documentation](https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve) | Official preview documentation / 官方预览文档 | Distinguish a scientific reasoning service from a locally installable skill / 区分科研服务与本地 skill | Access is a restricted preview requiring contact with the relevant team; it is not a default available integration / 受限预览，非默认可用集成 |

## Retrieval tools and data sources / 检索工具与数据源

All commercial services are optional. Documentation availability does not establish account access, subscription entitlement, working credentials, or a tested integration.

商业服务均为可选。文档可见不意味着用户有账号权限、订阅、有效凭证或已完成集成。

| Source / 来源 | Read depth / 深度 | Role in Atlas / 用途 | Verified limitation / 已核实边界 |
| --- | --- | --- | --- |
| [Undermind](https://www.undermind.ai/), [official MCP](https://www.undermind.ai/mcp) | Homepage, benchmark description, MCP tool list and Codex instructions / 主页、评测说明、MCP 工具及 Codex 文档 | Complex research-goal search, citation expansion, available-PDF questions / 复杂目标检索、引用扩展、可得全文分析 | Full-text access depends on availability/upload. Its reported search benchmark is vendor-run; search stopping does not prove completeness / 全文依赖可得性，自评和停止不证明查全 |
| [Elicit API](https://docs.elicit.com/), [official examples](https://github.com/elicit/api-examples), [MCP README](https://github.com/elicit/api-examples/blob/main/integrations/mcp/README.md) | API and example/MCP READMEs; not all implementation source / API、示例和 MCP 文档，不是完整源码审计 | Search, screening and structured evidence extraction / 检索、筛选、证据抽取 | API requires an eligible paid plan; extraction requires source checks. The Claude Code wrapper's existence was verified, not its entire skill body / API 有套餐条件；未声称全文审计其包装 skill |
| [Scite API](https://scite.ai/api), [MCP](https://scite.ai/mcp), [literature-review guide](https://scite.ai/blog/how-to-use-ai-for-literature-review) | Official API/product and methodological documentation / 官方接口、产品与方法文档 | Search for later disagreement and inspect citation context / 查后续异议和引用语境 | supporting/contrasting/mentioning labels are navigation signals, not truth or quality certification / 分类不是论文真假或质量认证 |
| [Future-House/PaperQA2](https://github.com/Future-House/paper-qa) | README, local-search and contracrow sections / README、本地检索及 contracrow 配置段 | Source-grounded answers and contradiction leads over collected papers / 对已收集论文做证据问答和矛盾定位 | Default SearchPapers queries a local index; it is not an exhaustive global literature search. Runtime model costs remain / 默认查本地，模型运行仍有成本 |
| [Semantic Scholar API](https://www.semanticscholar.org/product/api), [official Python tutorial](https://www.semanticscholar.org/product/api/tutorial) | Official overview and tutorial / 官方总览和教程 | Metadata, recommendations, and citation graph / 元数据、相近论文与引用图 | Rate limits and field availability apply; metadata is not full text / 有速率及字段限制，元数据不是全文 |
| [OpenAlex agent guide](https://help.openalex.org/access/agents/), [access overview](https://help.openalex.org/access/overview/) | Official agent and access docs / 官方 Agent 与访问文档 | Repeatable API search and scholarly metadata / 可复跑 API 检索与学术元数据 | Website, API budget, and full-text access have different conditions; avoid assuming unlimited free API access / 网页、API、全文条件不同 |
| [ResearchRabbit free tier](https://learn.researchrabbit.ai/en/articles/12865509-researchrabbit-free-tier) | Official feature/pricing-boundary documentation / 官方功能及免费边界文档 | Explore seed-paper neighborhoods and citation maps / 种子论文拓展与引用地图 | Graph proximity is not mechanism validation; an official general API/MCP was not established in this audit / 关系近不等于机制成立，本次未核实官方通用 API/MCP |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/), [ACL Anthology](https://aclanthology.org/), [ChinaXiv](https://www.chinaxiv.org/), [Wanfang](https://www.wanfangdata.com.cn/) | Official documents/pages or article records, as recorded in the retrieval smoke / 官方文档、主页或文章页，具体深度见通路验证 | Publication identity, primary records, and complementary language coverage / 出版身份、原始记录与双语覆盖 | Portal access does not imply a successful database-wide query; ChinaXiv explicitly distinguishes preprints from strict peer review / 门户可见不等于全库检索成功 |
| [CNKI](https://kns.cnki.net/), [DBLP](https://dblp.org/), Chinese journal portals | Identified entry points; some page fetches failed in the smoke / 已识别入口，部分抓取失败 | Additional sources to use when accessible / 有权限时补充 | Blocked/unavailable cells stay explicit. No native CNKI search or subscription access was demonstrated / 不把失败与未执行改写为已覆盖 |

The bilingual retrieval protocol cites stable official entry points. The [retrieval smoke](docs/retrieval-smoke.md) records specific queries, opened article records, and failed accesses; it does not establish exhaustive Agent coverage.

## Original scientific reference / 原始科学方法文献

**Michael A. Fischbach.** “Problem choice and decision trees in science and engineering.” *Cell* **187**(8), 1828–1833 (2024). DOI: [10.1016/j.cell.2024.03.012](https://doi.org/10.1016/j.cell.2024.03.012). [PubMed record](https://pubmed.ncbi.nlm.nih.gov/38608651/).

The bibliographic record names **Michael A. Fischbach as the sole author**. Do not attribute this paper to a coauthor, “Fischbach et al.,” or Anthropic. Anthropic's related skill is a separate adaptation.

该论文是 **Michael A. Fischbach 独著**。不能写成“Fischbach 等人”，也不能把原始论文归于 Anthropic。相关 skill 是另一份方法应用。

Read depth for this audit: **PubMed bibliographic record and abstract**. The abstract supports the design themes of deliberate problem choice, impact and tractability, decision branches, and learning from failure. The full article was not independently reproduced or republished by this project.

本次核验深度是 **PubMed 元数据与摘要**。它支持重视问题选择、影响与可行性、决策分支以及从失败中获取信息的设计方向；本项目未转载原文，也未把摘要阅读写成全文研究。

## Conflicts resolved / 整合时解决的冲突

| Potential conflict / 潜在冲突 | Resolution in this project / 本项目的处理 |
| --- | --- |
| Broad brainstorming versus unsupported novelty / 发散想法与无依据的创新宣称 | Generate candidates, then require closest prior art, counterevidence, and a specific unresolved condition / 生成后查最相近工作、反证和明确未决条件 |
| Optimizing a score versus discovering a mechanism / 优化分数与发现机制 | Keep the evaluator fixed during a comparison; test alternative explanations and inspect failure slices / 比较期间固定评价器，检查替代解释与失败分层 |
| Automated positive stories versus negative results / 自动生成正面故事与负面结果 | Retain failed runs, null results, and conditions where a claim weakens; do not rewrite the hypothesis retrospectively without recording the change / 保留失败、无效和边界；修改假设要留痕 |
| One-language search versus field coverage / 单语检索与领域覆盖 | Search in Chinese and English with adjacent terminology; record inaccessible databases and unsearched cells / 双语加相邻术语，记录未覆盖部分 |
| Abstract summaries versus full-text claims / 摘要与全文结论 | Record reading depth and evidence locations; use only claims supported by the material actually read / 记录深度与定位，以实际阅读内容为限 |
| RAG-heavy examples versus broad Agent research / RAG 例子与全域 Agent | Use 14 extensible seed domains and permit new domains, overlaps, and non-RAG questions / 14 个可扩展种子域，允许新增、交叉与非 RAG 方向 |
| Automatic end-to-end execution versus bounded research / 全自动执行与有边界的科研 | Connect stages through reviewable artifacts and explicit resource limits; keep external access optional / 用可审查产物与资源边界交接，外部接入可选 |
| Publication anecdotes versus guaranteed acceptance / 发表个案与录用保证 | Report the exact venue, track, evaluation, selection, and status when supported; never promise SCI or leading-venue acceptance / 精确描述 venue、track、评价与状态，不保证录用 |

## Licenses and limitations / 许可与边界

The repository's license covers its original material. It does not relicense linked papers, upstream skills, datasets, APIs, trademarks, or product documentation. No upstream file is vendored here. Conceptual attribution is provided above.

仓库许可证仅适用于本项目原创内容，不改变外链论文、上游技能、数据、接口、商标或产品文档的许可。这里没有直接打包上游文件，理念来源已列于上文。

During the audit, PaperQA2's repository identified an Apache-2.0 license and Elicit's API example repository identified an MIT license. This is not a blanket license assertion about the rest of the sources. Before copying any upstream text or code, verify its current license and retain the required copyright and license notices. In particular, MIT-licensed material still requires preservation of the applicable notice; this project's license is not a substitute.

核验时 PaperQA2 标示 Apache-2.0，Elicit 示例仓库标示 MIT；这不代表其他来源都采用 MIT。将来若复制上游文本或代码，需针对相应版本核实许可并保留要求的版权和许可声明。MIT 也不意味着可以去掉原有归因声明。

This project does not claim that installing a skill guarantees novelty, correct hypotheses, reproducible findings, SCI indexing, journal acceptance, or acceptance at a leading conference. Source inspection, protocol testing, and research success are different claims. Test records should state the exact behavior exercised and unresolved limitations.

本项目不宣称安装技能即可保证创新、正确假设、可复现发现、SCI 收录、期刊录用或顶会录用。来源核验、协议测试与科研成功是不同结论，验证记录应说明测试覆盖的具体行为与仍存在的限制。

