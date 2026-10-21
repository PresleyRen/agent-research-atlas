# Writing project handoff / 写作项目交接

更新日期：2026-10-21。项目范围：明确的合成离线技能任务。所有“结果”仅指输入虚构记录；本轮没有执行真实研究。任务类型为 C26 英文论文写作/润色与 C27 投稿前审查/完整回复，采用 `supervisor-publication.md` §§3–7。

## 1. 已交付

| 产物 | 路径 | 内容 |
|---|---|---|
| 英文 Introduction + Methods | [sections-en.md](manuscript/sections-en.md) | 四段 Introduction、六个 Methods 小节；连续可用 prose，方法与结果范围已更正 |
| 英文原句润色 | [polished-sentences-en.md](manuscript/polished-sentences-en.md) | 保留 `was associated with`；保留正确的 `in descending order`，区分语言示例与正文可用句 |
| 完整英文审稿回复 | [response-en.md](review/response-en.md) | R1.1、R1.2、R2.1、R2.2、R3.1 原文及逐条实际回复 |
| 投稿前审查 | [pre-submission-review-zh.md](review/pre-submission-review-zh.md) | 12 个有定位的发现、严重度、修复与余项；明确实际检查范围 |
| 审稿覆盖表 | [concern-ledger.md](review/concern-ledger.md) | 五个父意见拆成12个子项，映射证据、动作、完成状态、文稿/回复位置 |
| 中文依据与改动 | [edit-notes-zh.md](records/edit-notes-zh.md) | 原文/改后/原因、内容纠错与语言编辑区分、双语术语、待办 |
| 句级证据表 | [evidence-map-zh.md](records/evidence-map-zh.md) | 23条句级映射、原始来源与版本、观察/解释/计划边界、4条撤回主张 |
| 研究地图 | [MAP.md](research-atlas/MAP.md) / [map.html](research-atlas/map.html) / [atlas.json](research-atlas/atlas.json) | 原生地图及离线视图，revision 4，30节点、11关系 |
| 检查总记录 | [verification.json](records/verification.json) | 原件完整性、计数、覆盖、数值/地图检查、产物哈希与范围 |

原始 `PROJECT.md`、`draft-zh.md`、`notes/method.md`、`results/pilot.json`、`reviews.md` 和输入清单均未改写。新稿、记录和地图仅保存在本项目。

## 2. 关键结论与分歧处理

输入 `results/pilot.json` 给出的准确率是：版本感知策略 50/64 = **78.125%**，对照 44/64 = **68.75%**，绝对差为 **9.375 个百分点**。原稿 96% 与该字段不匹配，已更正；原错误和审计失败结果仍保留。输入只有一个手工合成案例集，64 个案例、8 个案例家族；没有三个真实业务数据集，也没有本轮真实研究执行。

保留的结论严格限于该虚构记录中的描述性关联。撤回“解决所有文档 Agent 的意图问题”“在真实数据上证实泛化”“澄清必然提高推理”的主张。8 个家族的数量不证明家族之间独立，更不能当作64次独立重复。没有逐例/家族级记录，所以没有附加置信区间、显著性检验、哪几例改善的断言或因果估计。

方法描述保留一个共享版本状态同时支持过滤和追问，不强制拆成两个模块。明确它是规则策略；隐藏参考标签仅供评估器使用是输入方法的声明，代码层面尚无法验证。旧备忘录中的评审人格分类和分数提升预测未被采纳，其原文与弃用理由都有保留。

R2.1 要求的两个更大模型和相同延迟预算实验未执行。完整回复明确说明未完成，并取消任何等预算效率优势暗示；没有以“已补充”描述未做的工作。设计在看过合成案例后计划、未预注册的事实已经写入正文和回复。

## 3. 实际检查和运行结果

| 检查/命令 | 实际结果 | 记录 |
|---|---|---|
| 初始 `atlas.py --root PROJECT discover` | 扫描6个原始文件，无地图候选，`truncated=false` | `records/initial-discovery.json` |
| INPUT-MANIFEST 大小与 SHA-256 | 5个列明输入全部匹配，原件未改 | `records/source-integrity.json` |
| 整数/Fraction 算术 | 两个正确数/64与准确率字段完全一致；派生值精确计算 | `records/calculations.json` |
| `audit.py ... values --ledger records/original-claim-ledger.json` | **exit 3**；原96%为预期检出的 `mismatch`，不是未解释工具故障 | `records/original-claim-audit.json` |
| `audit.py ... values --ledger records/numerical-ledger.json` | **exit 0**；11/11数值匹配，源哈希匹配，零容差 | `records/numerical-audit.json` |
| 审稿父 ID/原文覆盖 | 五条原文完整引入英文回复；12子项覆盖另表 | `records/review-coverage-check.json`、`review/concern-ledger.md` |
| `atlas.py ... init --synthetic` + `upsert --expected-revision 0` | 创建原生合成地图；写入来源、当前/撤回主张及待办 | `records/atlas-update.json`、地图历史 |
| `resolve-review` 对 clarification/evaluation/routing | 审查新增本地阅读依赖后保持 partial，依次记录revision 2/3/4 | `records/atlas-review-resolution-log.json` |
| 最终 `atlas.py ... check` | **exit 0**，revision 4，30节点、11关系，结构有效 | `records/atlas-check.json` |
| 最终 `atlas.py ... status` | pending reviews = 0；imports = []；三个已记录域partial，其余11域unsearched | `records/atlas-status.json` |
| 最终 `audit.py ... project` | **exit 0**，仍报告 `G-COVERAGE-UNSEARCHED`；不是全领域已查完 | `records/project-audit.json` |

上述 Python 命令使用 `python -B` 和已读取的技能本地脚本：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/atlas.py`、同目录的 `audit.py`。没有改动技能/distribution，未读取 distribution 的 evals/results 或测试答案。审计只核查可结构化一致性，不证明科学有效性。

英文两节稿计数为1146词，完整回复为1019词（计数包含标题和引述，按本地正则词元定义；确切规则/结果见 verification）。未给定正式字数或页数上限，不宣称符合某投稿场所要求。正文/回复由写作者串行自审，协调者另行全文阅读并对照输入，未发现虚构新实测或漏答；这不是独立科学复验或盲审。地图 HTML 由本地工具生成，未进行浏览器视觉验收；本任务没有科学图、PDF/Word或完整论文版式可检查。

## 4. 地图的当前语义

- `fixture-pilot-record`：明确的 supplied synthetic record，不是新实验运行。
- `claim-fixture-accuracy`、`claim-fixture-scope`：仅对“给定文件记载什么”得到支持；不代表算法获得真实实验验证。
- `old-accuracy-96`、`old-three-real-datasets`、`old-universal-intent-solution`、`old-clarification-causality`：均 withdrawn，历史原文保留。前两者与输入记录直接矛盾；后两者缺乏支持，不宣称反向因果命题已证实。
- `hyp-shared-state-mechanism`：parked；没有 grounded、pilot_supported 或 independently_supported 的假设。
- `decision-park-model-latency-comparison`：parked；R2.1 实证请求仍待未来材料和授权。
- `decision-reject-reviewer-profiling`：abandon；后续不重用旧人格/加分策略。
- `problem-reproducibility-gaps`、`problem-nearest-work-unresolved`：open。

`research-atlas/domains/routing/notes.md` 与 `domains/evaluation/notes.md` 有续接笔记。地图配置在 `research-atlas.config.json`，下次应复用，不重新初始化。没有非原生地图需要语义导入，也没有未完成导入。

## 5. 仍缺材料与下一步

目前最值得进一步区分的问题是：共享版本状态的任何收益，究竟来自过滤、针对性澄清、额外信息、预算差异还是案例选择。这个机制问题只是候选，最近外部工作未核验；不将其称为创新结论或已支持的研究方向。

1. 先取得逐例案例与家族 ID、两条件输出/评分、正确性规则和评分过程，检查案例对齐、家族依赖、错误类别及可能退步。当前只有汇总值，不能独立重评分。
2. 补完整版本状态/规则实现、模型和提示词、检索与运行配置、标签隔离和原始日志，才能谈计算级复现。
3. 若未来另行授权真实研究，先约定新的独立材料、两大模型版本、统一延迟预算及澄清等待时间处理，再进行具有区分力的比较；本轮未运行研究实验。
4. 在有外部来源材料或相应联网授权后补查最近工作和反例，明确目标场所后核验官方规则。没有任何已验证的最近论文可在本轮交接中列出。

未联网、安装、模型推理任务、付费、额外实验或外部提交。两节稿和回复的写作工作已完成；实际研究证据、未做实验与正式投稿完整性仍按上述边界留待后续处理。
