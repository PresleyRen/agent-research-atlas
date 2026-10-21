# 当前能力缺口、负责位置与补足路线

日期：2026-10-20。依据：本地 skill、能力注册表、`docs/EXTENDING.md` 和项目实际记录。**本轮没有修改技能源文件、安装依赖、探测账号或执行远端工具。** 以下是定位与待办，不是完成了新集成。

## 1. 实际可用与未核验能力

本轮已使用的是本地文件阅读、Python 标准库、`atlas.py` 的发现/增量写入/渲染/校验，以及 `audit.py` 的本地诊断。宿主工具元数据里可见公开 web search，但用户本轮明确禁止网络，所以它没有被调用。当前枚举中未见直接命名为 S2、Elicit、PaperQA2、OpenAlex、Scite 或 Undermind 的 callable；这只是当前元数据检查结果，不是账号、服务或机器全局安装状态调查。

`docs/history/requests-original-2026-10-20.json` 声明 S2 没做账号检查、Elicit 未连接、PaperQA2 范围只有三个本地文件。保持这些边界：不要把注册表里的 `optional` 服务当成已接通，不因现有通用搜索就执行本轮被禁止的外部请求。

## 2. 从项目症状定位到维护责任

路径以技能源目录 `agent-research-atlas-public/skills/agent-research-atlas/` 为根；下表指明未来该去哪里补足，本轮不改这些位置。每个 C-ID 的完整定位输出已存于 `docs/audit/locate-Cxx.json`。

| 当前不足 / 对研究的影响 | 能力 ID 与负责位置 | 本轮已做的补救 | 未来扩展或验证要求 |
|---|---|---|---|
| 自定义“时变意图与撤销”域不在内置 `queries` 种子词表 | C01/C03：`assets/agent-taxonomy.json`、`references/agent-domains.md`、`scripts/atlas.py::queries` | 新域通过普通 sourced domain 节点入图，宿主编写双语查询账本；覆盖仍为 unsearched。 | 若需自动生成该域查询，在获准维护技能时同步词表与 planner；检查中英齐全、旧域保留、查询不冒充执行。已有回归位置：`tests/test_atlas.py::AtlasCliTests.test_bilingual_query_focus_preserves_both_languages_and_does_not_claim_execution`。 |
| 统一 Boolean 与 filters 无法跨 provider 通用，真实接口未内置 | C03/C22：`references/bilingual-retrieval.md` 的 provider syntax / optional adapter contract；注册表 SRC-S2-F01、SRC-ELICIT-F01 | 拆普通文本 relevance、semantic 自然语言与未来 keyword 分支；保存原请求；请求均未发。 | 写独立 adapter，核验实际 endpoint/version/mode/corpus，保留 exact payload、warnings/effective settings、页数和截断。先离线固定回执再在未来获授权时做真实连接检查；文档/fixture 通过不能标实连通过。 |
| 推荐负种子误删除相关反证，且本地 ID 不是真实论文 ID | C04/C06/C09/C22：SRC-S2-F02；`bilingual-retrieval.md`；`evidence-and-claims.md` | 保留 support 与 counter 的相关角色、irrelevant 的排除理由；recommendation payload 为 null、sendable:false。 | 对种子同时验证“领域相关性”和“外部身份”；科学立场单独记录。回归用相关支持、相关反驳、无关三类和无效外部 ID。 |
| 本地仅三句合成材料；没有真实全文、引用语境和独立证据 | C05/C06/C09：阅读/证据契约；SRC-PAPERQA-F01/F02/F03、SRC-SCITE | 人工读取全文短片段，逐条记条件、缺失身份与真实阅读深度；不宣称全域查新。 | 先获合法真实材料，再用原文定位/宿主 reader；PaperQA2 仅作明确 corpus 的问答，contracrow/Scite 标签只作线索。针对中英 PDF、公式、表格、版本和矛盾做固定样例回归。 |
| 团队把同一上下文的三个角色称为独立评审 | C19：`references/methodology.md`、`references/evidence-and-claims.md`；冲突 CF13/CF20 | 原稿留存，团队笔记及地图追加更正：串行角色自审，无独立评审证据。 | 独立上下文评审应有实际身份、输入范围、质疑与共享来源说明；评价设计不能替代独立经验复验。现有前向冲突文档 `docs/forward-conflicts.md` 标为 not_run，不虚报已测。 |
| 每次重新初始化会丢研究连续性；旧失败分支易被忽略 | C02/C20：`Atlas.init`、`Atlas.write_view`、`dependency_links`、`update_review_queue`、`Atlas.resolve_review` | 复用配置指向的 research-memory，从 revision 1 增量 upsert；保留旧 ID、手写笔记、原始请求、暂停原因和更正。 | 新前提用 upsert 登记，沿 impact 查下游；只在完成实际复核后 resolve-review，不能手工清队列或用重新初始化解决冲突。 |
| 未来实验缺数据、工具语义、评价器、样本依据及真实预算 | C11/C13/C17：`methodology.md`、`atlas.py::validate`、`audit.py::project_gaps`、`experiments.py::validate_plan` | H1 保持 proposed，写强基线、时序/噪声诊断及停止条件，未写虚假结果。 | 数据/许可、计算、评价、预算逐项验证后再决定可测性；该技能没有通用统计或功效引擎，不能用结构检查代替测量与统计设计。 |
| 工具成功易误作科研正确；技能覆盖与研究覆盖混淆 | C23/C24：`audit.py::locate/check_registry/project_gaps`、`references/extension-contract.md`、`SKILL.md` handoff | 保存每条命令回执和原文 hash；区分能力记录、查询计划、本地阅读与真实实验证据。 | 能力维护要同时更新 owner、schema/fallback、测试、互补来源、版本记录；项目里不能因此升级领域 reviewed 或假设 supported。 |

## 3. 应保留的冲突契约

| 冲突 | 需要保留的两侧 |
|---|---|
| CF01：检索与新颖性 | 合理开展查新；无命中、限流或未运行不能证明不存在近邻。 |
| CF11：统一意图与 provider 语法 | 用同一个研究问题组织请求；真正提交必须使用各接口语法。 |
| CF12：工具标签与证据 | 支持/反驳标签用于导航；科学判断仍回到原文条件。 |
| CF13：角色分工与独立性 | 保留有用的角色自审；拒绝把角色数当独立评审人数。 |
| CF16：技能与研究覆盖 | 能力注册表可维护；生成领域/查询不等于完成文献综述。 |
| CF19：更新与历史 | 新证据触发复核并修订当前判断；保留旧解释、失败和变化原因。 |

## 4. 补足的优先级与停止边界

第一优先是取得真实支持和反驳近邻、核实标签与执行语义；这会决定问题是否值得继续。第二优先是按已授权 provider 补查询回执与全文定位。只在重复人工步骤已成为瓶颈时考虑 adapter；没有必要先安装全部科研服务。

将来维护 connector 时的最小验收应包括：未执行、成功有结果、成功空集、401/403、429、超时、解析失败、部分结果与分页截断；中文/英文查询；相关反驳保留；synthetic/internal ID 拒绝当外部 ID；metadata/abstract/fulltext 保真；无收费异步任务的盲重建；版本变化后的回归。这里列的是**未执行的扩展验收要求**，不是本轮测试成绩。

本轮不会为这些缺口发送网络或账号请求。后续若用户仍限定本地，就继续处理新提供的合法材料和现有记录；若用户明确允许公开检索，再逐项启用相应范围，不能把这份交接视为自动授权。

## 5. 本地审计的实际结果与边界

本地 `audit.py check --repo ...` 返回 `valid:true`，核对 24 项能力、65 个来源、222 个特色条目、20 项冲突及其已声明路径/符号/测试引用。**没有运行这些测试，也没有验证服务、科学方法或论文结论。** 原始回执见 `docs/audit/registry-check.json`。

开始时 `discover` 找到唯一原生 atlas（research-memory、revision 1）且未截断；`status` 没有 pending review 或未完成 import；`project` 明确列出 14 个 unsearched 域。结束时以交接文件和最新 `docs/audit/project-after.json` 为准。新增域仍未做真实检索，所以出现覆盖缺口是准确状态，不需要为了得到“干净报告”消除它。
