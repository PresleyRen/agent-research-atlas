# Retrieval smoke / 双语检索通路验证

**Date / 日期:** 2026-10-20  
**Scope / 范围:** Small live Chinese-and-English retrieval check for planning and tool-use literature. / 针对规划和工具使用文献的小规模真实中英检索。  
**Execution surface / 执行面:** Available web search and page-reading tools, followed by primary article-page inspection. / 通过可用网页搜索与阅读工具检索，再打开原始文章页。  
**Not exercised / 未测试:** Native CNKI/Wanfang searches, paid research-product accounts, MCP authentication, PaperQA execution, complete literature coverage, hypothesis quality, or experiment outcomes. / 未测试数据库内部检索、付费产品、MCP 登录、PaperQA 运行、完整覆盖、假设质量和实验效果。

This is a route check, not a comprehensive Agent literature review or a benchmark of this skill's research effectiveness. It records a few live outcomes, including access failures. No research-paper PDFs were downloaded into the repository.

这是检索通路验证，不是完整 Agent 文献综述，也不是技能科研效果基准。记录少量真实结果及访问失败，没有把论文 PDF 下载进仓库。

## Submitted queries / 实际提交查询

The strings below were actually sent to the available search service. Boolean and site syntax are preserved as submitted; they do not imply native-database searching.

下列字符串确实发送给了当前搜索服务。保留实际 site/引号语法，不把它们描述为数据库内部检索。

| ID | Language / 语言 | Exact query / 精确查询 | Purpose and outcome / 目的与结果 |
| --- | --- | --- | --- |
| ZH-1 | Chinese | site.jos.org.cn 大语言模型 智能体 综述 工具 规划 | Broad Chinese entry query. The returned set included a Journal of Software code-agent survey; opening that article page failed. / 中文入口；找到软件学报相关文章线索，打开文章页失败 |
| ZH-2 | Chinese | "大语言模型视角下的智能规划方法综述" "系统仿真学报" | Exact-title follow-up to a discovered Chinese planning survey; official article metadata and abstract were accessible. This is a known-item lookup, not a recall test. / 已发现中文论文的精确标题复查；可打开官方元数据与摘要，不代表召回率测试 |
| EN-1 | English | site.aclanthology.org language agents planning survey | Found the COLING 2025 agent-paradigm survey; opened its ACL Anthology record. / 找到 COLING 2025 智能体范式综述并打开官方记录 |
| EN-2 | English | "language agents" planning barriers constraints site:aclanthology.org | Found a primary NAACL 2025 planning-failure analysis; opened the official record. / 找到 NAACL 2025 规划失败分析的原始研究并打开官方记录 |

The search service returned ranked result lists, not an independently complete relevant-paper set. No corpus-wide result count, precision, or Recall@K is claimed.

搜索服务返回排序结果，不是独立且完整的相关论文金标准。这里不声称全库结果数、精确率或 Recall@K。

## Successfully opened primary records / 成功打开的原始记录

| Record / 记录 | Exact source / 精确来源 | Verified fields / 核实字段 | Actual reading depth / 实际阅读深度 |
| --- | --- | --- | --- |
| 大语言模型视角下的智能规划方法综述 / Survey on Intelligent Planning Methods from Large Language Models Perspective | [Journal of System Simulation record](https://www.china-simulation.com/CN/abstract/article/1004-731X/3623); [DOI 10.16182/j.issn1004731x.joss.23-1468](https://doi.org/10.16182/j.issn1004731x.joss.23-1468) | Chinese/English titles, journal, 2025, 37(4), pages 823–844, DOI, abstract; the HTML page also exposes references / 中英标题、期刊、年卷期页、DOI、摘要，页面另含参考文献 | Metadata + abstract; references visible. The main article/PDF was not read. / 元数据与摘要；参考文献可见，未读论文主体/PDF |
| A Review of Prominent Paradigms for LLM-Based Agents: Tool Use, Planning (Including RAG), and Feedback Learning | [ACL Anthology 2025.coling-main.652](https://aclanthology.org/2025.coling-main.652/) | Title, Xinzhe Li, COLING 2025, proceedings title, pages 9760–9779, abstract and PDF link. The DOI field was blank on the inspected record. / 标题、作者、会议、页码、摘要与 PDF 链接；所读页面 DOI 栏为空 | Metadata + abstract. PDF available as a link, not read. / 元数据与摘要；仅看到 PDF 链接 |
| Revealing the Barriers of Language Agents in Planning | [ACL Anthology 2025.naacl-long.93](https://aclanthology.org/2025.naacl-long.93/); [DOI 10.18653/v1/2025.naacl-long.93](https://doi.org/10.18653/v1/2025.naacl-long.93) | Title, authors, NAACL 2025 long-paper proceedings, pages 1872–1888, DOI, abstract and PDF link / 标题、作者、会议长文卷、页码、DOI、摘要与 PDF 链接 | Metadata + abstract. A search result exposed a PDF excerpt, but the full paper was not inspected. / 元数据与摘要；搜索曾显示 PDF 摘录，但未完成全文检查 |

The two English records establish that this search route can find a survey and a failure-oriented primary study beyond document RAG alone. They do not establish that the findings remain true for current models, that the methods were reproduced, or that a new idea has been discovered.

英文结果说明这条通路能找到不限于文档 RAG 的综述及失败分析原始研究；它们不证明论文结论对当前模型仍成立、不代表复现，也不表示已经发现新的研究点。

For the Chinese record, the HTML author-name rendering and a search-result PDF excerpt showed a differing Chinese character for one author. This smoke did not resolve it against the PDF. Identification therefore uses the title and DOI; author spelling should be checked before producing a final bibliography.

中文记录的 HTML 作者名与搜索结果中的 PDF 摘录存在一个汉字差异；本次未通过 PDF 定稿页解决。记录以标题和 DOI 对齐，正式参考文献使用作者名之前应再核对，不默默猜改。

## Failed or limited access / 失败与受限访问

| Target / 目标 | Observed result / 实际结果 | Consequence / 处理 |
| --- | --- | --- |
| [基于大语言模型智能体的代码生成综述](https://www.jos.org.cn/jos/article/abstract/7593) | Article appeared in search results; page reading failed, including a timeout on a bounded retry / 搜索结果可见，文章页读取失败，有限重试超时 | Retain as a search-result lead only; do not mark full-text or abstract-page reading / 仅保留搜索线索，不写已读文章页或全文 |
| [大语言模型的工具使用综述](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240793) | Search result identified an official article URL and DOI; both page-opening attempts timed out / 搜索识别官方链接与 DOI，两次打开超时 | Keep the lead and failure reason; no method or result claims attributed to an inspected full text / 留存线索与失败原因，不声称读过方法结果 |
| [CNKI entry point](https://kns.cnki.net/) | Page retrieval returned an error / 页面读取错误 | Native database search and subscription access remain not_run / 数据库内部检索及订阅访问未执行 |
| [DBLP entry point](https://dblp.org/) | Page retrieval returned an error / 页面读取错误 | DBLP search/API access remains unverified by this smoke / 本通路未验证 DBLP 检索或 API |
| [Wanfang homepage](https://www.wanfangdata.com.cn/) | Homepage was retrievable / 首页可读取 | This does not establish a native journal/thesis search or full-text entitlement / 不代表已检索期刊学位库或取得全文权限 |
| [ChinaXiv homepage](https://www.chinaxiv.org/) | Homepage and its preprint-status notice were retrievable / 首页与预印本状态说明可读 | No specific ChinaXiv Agent-paper search was completed in this smoke / 本次未完成 ChinaXiv 的具体 Agent 论文检索 |

## Assessment / 结论

**Passed for the narrow scope / 在小范围内通过：**

- Chinese and English queries were actually submitted. / 确实执行了中英文查询。
- At least one original Chinese journal record and two original English conference records were opened. / 打开了至少一个中文期刊原始记录和两个英文会议原始记录。
- Stable identifiers, publication type, and actual reading depth were preserved without inventing a missing DOI. / 保留稳定标识、发表类型与实际阅读深度，未编造缺失 DOI。
- Access failures were retained and did not become claims of coverage. / 保留访问失败，没有将其改写成已覆盖。

**Remaining untested / 仍未测试：**

- Systematic coverage across all 14 seed domains, citation-expansion saturation, and full-text claim verification. / 14 域系统覆盖、引用拓展饱和及全文论点核验。
- Native Chinese database access or paid literature services. / 中文数据库内部访问及付费文献工具。
- Whether the skill selects novel, important, feasible questions or improves experimental validity. / 技能是否能选出新颖、重要且可行的问题，是否提高实验有效性。
- Any probability of SCI or leading-venue acceptance. / 任何 SCI 或顶刊顶会录用概率。

Repeat this check when search tools or source access change, and extend it with a defined relevance set before reporting retrieval-quality metrics.

检索工具或访问条件改变时再做通路检查；如果要报告检索质量指标，需另建明确的相关性金标准。

