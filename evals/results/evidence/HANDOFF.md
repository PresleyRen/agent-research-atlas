# 下一轮交接：歧义请求的一次澄清路由

更新：2026-10-20。项目：SYNTHETIC教学材料。审查者：cold_evidence_review。

## 现在可以写什么

可以写：两份历史合成日志的accuracy字段都是0.625、n字段都是8、seed标记分别是7和13；当前源码只作关键词路由，准确率0.97是常量且没有真值比较、没有澄清实现。日志生成链仍未核验。不能将0.625当作已验证准确率，也不能把两个seed当作独立评测。原草稿准备写的0.97、独立验证、普遍机制、摘要证明与首次提出均撤回使用，原稿留存。

主候选仍值得继续检验：**在等一次提问预算下，针对性澄清是否比通用追问更有用？** 先恢复标签与真实计量。现有证据没有支持或有效反驳澄清机制。仅增加关键词路线继续暂停。

保留旧原句：**先检查标注歧义，再归因于模型。**

## 从这里继续读

| 需要 | 文件 |
|---|---|
| 本轮核心判断、来源、争议和候选取舍 | reviews/2026-10-20/evidence-review.md |
| 可以采用的有限结果正文 | docs/results-reviewed.md |
| 最小诊断的方法卡、比较、反证和预算条件 | plans/minimal-discriminating-study.md |
| 尚未执行的中英查新清单 | plans/retrieval-followup.md |
| 原生研究地图 | research-atlas/atlas.json |
| 便于浏览的地图 | research-atlas/MAP.md、research-atlas/map.html |
| 原件及其SHA-256 | reviews/2026-10-20/source-manifest.json |
| 数字账本与回执 | reviews/2026-10-20/values-draft*.json、values-observed*.json |
| 实现与来源检查 | reviews/2026-10-20/static-code-review.json、legacy-provenance-review.json |
| 实际校验命令/退出码 | reviews/2026-10-20/validation-commands.json |
| 技能正文、协议、脚本、模板的实际路径与SHA-256 | reviews/2026-10-20/skill-provenance.json |

原有八个文件均未改动，包括docs/prior-map.md、docs/draft-results.md、code/router.py、两个历史结果、虚构摘要、资源说明和检索回执。旧图不是只登记：已读后语义导入，并把旧问题、笔记、暂停决定、9.2评分和无结果新颖性错误推断都明确归档。评分和模板说法留作历史，不能继续充当科学依据。

## 图谱状态

当前 **revision 5，40节点、20边**，校验通过；原旧图导入状态normalized。四个初始领域因新挂接检索/审查记录触发的pending review已分别核对并通过resolve-review记下理由，当前pending=0；四条审查日志保留在atlas及reviews/2026-10-20/review-resolutions.json。此前待审状态保存在post-import-status.json。

意图、澄清、路由、评测四领域为partial，其他十个种子领域为unsearched，没有把本地阅读宣称为全领域综述。图谱中的一条paper是明确fictional_fixture的本地摘要记录，不是真实发表文献；模型回忆题目仅为unverified_lead exploration。

| 关键ID | 当前状态 | 含义 |
|---|---|---|
| hyp-targeted-clarification | proposed | 主研究候选；真实近邻、数据、计量与执行条件未齐 |
| hyp-label-ambiguity | proposed | 最先检查的诊断解释，尚未声称已发现标签错误 |
| hyp-keywords-only | parked | 保留旧暂停及重启条件 |
| exp-legacy-a、exp-legacy-b | legacy_record_unverified | 指向原始日志，无历史来源/计量背书 |
| exp-plan-clarification | draft_blocked | 方案已写，未执行、未冻结 |
| claim-old-accuracy等五个旧论点 | withdrawn | 撤回写作用途，原文留档 |
| claim-log-observation、claim-abstract-scope | supported | 只支持文件内容的材料观察，不能解读为方法实证获支持 |

没有假设被标为pilot_supported、independently_supported或refuted。

## 已执行的校验

| 检查 | 实际结果 | 不能由此推出什么 |
|---|---|---|
| atlas.py discover | 初始扫描8文件、只找到docs/prior-map.md、truncated=false | 不是全机器/全领域检索 |
| 原八文件SHA-256 | 8/8与初次读取相同 | 不是历史运行真实性证明 |
| 源码AST与手工阅读 | accuracy=0.97为常量；不读真值；无澄清/seed使用 | 没有执行router，没有测新成绩 |
| audit.py values：原草稿账本 | 退出码3；2个accuracy mismatch、2个n match；哈希匹配 | 原稿失败不能被新账本“洗白” |
| audit.py values：有限观察账本 | 退出码0；accuracy/n/seed共6项match | 只表示转录正确，不认证标签、计量或独立性 |
| atlas.py check | 退出码0；revision5、40节点、20边、valid=true | 结构通过不代表科学结论成立 |
| atlas.py status | 退出码0；旧图normalized；pending=0 | pending清空不代表研究全部完成 |
| audit.py project | 退出码0；仍报告G-COVERAGE-UNSEARCHED、G-FEASIBILITY | 非零缺口应保留，不修改状态来美化报告 |
| resolve-review | 四次依当前revision顺序记录审查说明 | 不自动改变经验状态或替代独立复验 |

结果记录器的validate-record未执行：原记录没有原生计划/冻结/运行结构，也缺schema_version、elapsed_seconds等字段。没有补造这些字段、回填过去命令或重新运行来伪造完整来源。数值审计和自定义来源审查是适合本材料的实际校验。

本轮研究负载0，网络请求0，安装0，付费调用0，发布0。未修改技能源文件；skill-provenance.json是本轮所用源文件的路径与哈希快照。技能目录不含可用的git仓库元数据，未把git检查失败称为源文件版本校验通过。

## 下轮最小行动

1. **找回原八案例、标签规则和原运行链。** 区分“资源说明声称存在”和“文件可读”；找不回就继续记为缺失，不能从0.625反造五条正确案例。保留标签争议和所有错误。
2. **做P0计量修复。** 在新的实现版本中把评价器与候选分开；参考标签不被方法读取；逐条对齐case_id；验证手工可算的对错、空输入、缺失与重复情形。本轮仅完成设计，没有执行这些测试。
3. **开展已获后续授权的P1配对诊断。** 不问、通用一问、针对性一问、等长度无关一问四条件；主比较是两个同为一问的有效提问条件。原八例最多32次路由判定，必要时用保语义改写诊断关键词捷径，扩展上限64次。此数是开发预算，不是确认研究样本量。
4. **依观察决定。** 通用追问解释全部收益就停止更强“针对性策略”论点；无关文本也有效则查测量和信息泄漏；只在“文档”字面上有效则停止语义机制解释；有局部可解释增益也只作探索线索，下一步需要新独立场景。
5. **另补真实查新和独立评测。** 待新的联网/执行范围允许后，核验真实近邻、原文与强基线，再按未触碰场景、固定指标、实际有意义的效应界值设计确认研究。两个新seed不能替代这些工作。

当前研究执行授权为不可用，P1给出的CPU运行时间上限仅是未来方案建议。本轮交付的完整方案不意味着可以立即运行。无需重读已解决的八份材料或重复旧失败查询来找理由；按上述缺口续接。

## 所用技能关键文件与SHA-256

绝对技能根路径：/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas

| 文件 | 实际用途 | SHA-256 |
|---|---|---|
| SKILL.md | 主流程全文读取 | 9e2fef60cf0ae464bf8ef4791bfdafca7003eab5c7a6059d9059974214384eee |
| scripts/atlas.py | discover/adopt/status/upsert/check/resolve-review及自动视图生成 | bcf13a70cdff1f64dc10d2f054621d182fcd55bca04d9d128dc36d5973e9181b |
| scripts/audit.py | project、values | 9ad10da5eb49186d9d7a5c0323f2af51b56d52ab1e88d0b766ddb1541e877c61 |
| scripts/experiments.py | 由audit导入解析函数；未调用研究runner命令 | 653555bf96a36b74419cf47167ce9c9c05d89db774a4ff3bc45175848aae4219 |

六份实际参照协议及taxonomy/viewer模板的完整绝对路径、SHA-256和用途均列于skill-provenance.json。下轮若技能源版本变化，应保留该快照并记录差异，不能直接复用不匹配版本的验证结论。

可重新执行的本地校验入口是reviews/2026-10-20/check-local-evidence.py；它只做文件读取、AST、哈希、atlas状态和数字审计，不导入或执行研究router。它更新检查报告，因此如需保留本轮报告版本，先复制reviews/2026-10-20目录到新的项目内日期目录。不要重跑语义导入脚本来覆盖已续写图谱；后续修改应读取当前revision并用upsert增量写入。
