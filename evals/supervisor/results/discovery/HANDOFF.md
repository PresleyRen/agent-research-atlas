# 交接：澄清价值诊断评测的下一步

日期：2026-10-21。项目：`/workspace/scratch/f7a517081da8/supervisor-forward/discovery`。

## 先读什么、当前决定是什么

先读 [研究设计](RESEARCH-DESIGN.md)，再读 [修订地图](research-map.revised.md) 和 [评测 dossier](design/benchmark-dossier.md)。当前优先 B：先建设区分答案敏感意图歧义、文档证据缺失和明确版本约束的诊断评测。学习门控 A 暂缓训练；多检索 C 留作强基线；明确可解析版本纳入确定性过滤；旧地图“一律追问”继续 parked。

主问题是在相同决策前信息下，一次澄清比补检索、版本过滤或完整条件回答多带来什么。允许多个有效动作；答案敏感不自动等于必须追问。理想诚实回复的诊断上界与真实用户交互价值分开。

## 已完成产物

| 产物 | 用途 |
|---|---|
| [RESEARCH-DESIGN.md](RESEARCH-DESIGN.md) | 问题锚点、候选比较、选择理由、竞争解释、可行性与下一步 |
| [evidence-synthesis.md](design/evidence-synthesis.md) | 7 份内容输入的来源/行号、条件性综合、最近材料差异与未核验边界 |
| [benchmark-dossier.md](design/benchmark-dossier.md) | 缺口、构建谱系、任务、基线、分割、效度、指标、诊断和发布计划 |
| [annotation-and-data-contract.md](design/annotation-and-data-contract.md) | 双人分阶段标注、信息隔离、集合答案、争议、失败与评分 rubric |
| [analysis-and-execution.md](design/analysis-and-execution.md) | E0–E4、族级配对分析、精度/成本、停止/转向、未来冻结流程 |
| [bilingual-retrieval-plan.md](design/bilingual-retrieval-plan.md) | 中英最近工作、反证、相邻领域检索；所有远端查询均 not_run |
| [annotation-template.json](design/annotation-template.json) / [protocol.json](design/protocol.json) | 空白数据登记模板与机器可读设计；不是案例或运行结果 |
| [research-map.revised.md](research-map.revised.md) | 旧图延续、五条原内容映射、领域入口与当前决策 |
| [atlas.json](research-atlas/atlas.json) / [MAP.md](research-atlas/MAP.md) / [map.html](research-atlas/map.html) | 权威图谱、自动总览与离线交互图；revision 5 |
| `research-atlas/domains/{intent,clarification,routing,ingestion-retrieval,evaluation}/notes.md` | 观点、问题、方案与下一步的持续领域笔记 |
| [reading-and-provenance.md](worklog/reading-and-provenance.md) / [commands.jsonl](worklog/commands.jsonl) | 已读范围、真实命令/退出码、授权与执行边界 |

## 必须带着走的证据判断

两份“paper”和调试记录都是虚构情景，不是外部发表研究。原调试分数 62/64 对 51/64 原样保留；由于基线预读事后 `reference_intent`、8 家族改写跨分割且无成本测量，这些数不能支持方法胜负或整体弃题。修评测也不意味着候选方法已被证实更好。[原笔记](notes/comparison.md) L3–8

资源笔记称有 8 家族×8 改写，但当前文件没有逐行案例、文档、标签、家族 ID、实现或原始输出。因此所有实验仍 planned_not_run，H1/H2 为 proposed，未提升 testable；没有 pilot_supported、independently_supported 或 refuted 实证状态。任何条件性工作量/预算公式均为设计估算，不是已测结果。

原提醒完整保留：**旧版任务里的旧文档不一定错误。** 当前评测按任务版本与适用条件评分，不能以“越新越正确”替代金标准。

## 地图与验证状态

- 原地图通过 adopt 保留字节与 SHA-256，再将 L3–7 的五条内容逐一 upsert 为有来源的节点；import 状态为 normalized，没有未完成语义导入。
- 当前 revision 5，40 节点、15 关系；重点 5 领域 partial，其余 9 个种子领域 unsearched。未把种子目录或本地虚构材料当作全域综述。
- `atlas.py check` 退出 0、valid=true；`status` 显示 pending reviews=0；`audit.py project` 退出 0，保留 G-COVERAGE-UNSEARCHED 和 G-FEASIBILITY，未强行清除真实缺口。结构检查不能认证新颖性或科学结论。
- [inputs-before.json](worklog/inputs-before.json) 保存 8 个初始文件快照；[verification-final.json](worklog/verification-final.json) 记录最终输入哈希、链接和关键状态核对。原 `INPUT-MANIFEST.json` 的 7 个内容输入与清单本身都纳入保留检查。

## 实际执行的关键命令

以下缩写仅为方便续接，不改任何系统变量：

```bash
ATLAS_SKILL=/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas
ATLAS_PROJECT=/workspace/scratch/f7a517081da8/supervisor-forward/discovery
python -B "$ATLAS_SKILL/scripts/atlas.py" --root "$ATLAS_PROJECT" discover
python -B "$ATLAS_SKILL/scripts/atlas.py" --root "$ATLAS_PROJECT" adopt --file research-map.md --title '意图与文档 Agent：澄清价值的离线合成研究地图' --synthetic
python -B "$ATLAS_SKILL/scripts/atlas.py" --root "$ATLAS_PROJECT" upsert --file "$ATLAS_PROJECT/research-atlas/imports/normalized-local-inputs-v1.json" --expected-revision 0
python -B "$ATLAS_SKILL/scripts/atlas.py" --root "$ATLAS_PROJECT" check
python -B "$ATLAS_SKILL/scripts/atlas.py" --root "$ATLAS_PROJECT" status
python -B "$ATLAS_SKILL/scripts/audit.py" --root "$ATLAS_PROJECT" project
```

这些操作实际已执行且退出 0。最初 discover 检查 8 文件、未截断；adopt 创建 revision 0；upsert 创建 revision 1 并自动生成视图。**不要把 expected-revision 0 的 batch 盲目重跑**；续接先读当前 status，以新 batch 和当前 revision 增量更新。实际展开的 upsert/check/status/audit argv、stdout、stderr 和退出码见 `commands.jsonl`。早期命令回执摘要见阅读记录。

本轮还实际运行标准库文件读取、输入 SHA-256/字节数检查、JSON 解析和本地产物链接/状态核对；没有安装依赖。工具运行使用 `python -B`，避免写技能目录。

## 下一步的最小可判别工作

1. **取得并核验原始数据**：要的是真实 case rows、文档快照、family/模板/用户谱系和许可，不是再写资源说明。缺这些时不得生成“已有64条”的假数据。
2. **E0 构念审计**：按 rubric 分两阶段盲标，检查相同 O0、不同目标、不同答案的反事实对是否有效；同时允许条件回答、保留标签争议。先判断能否做有效测量。
3. **实际 split 与强基线实现**：按谱系连通组隔离。旧家族重切仅 exploratory；真实确认性需新独立家族。把隐藏字段移出候选输入，实际验证 metric 被调用。
4. **再确定资源与 freeze**：落实标注工时、评价器、模型/代码版本、真实调用预算与决策效应 δ；将协议转换为有真实 argv 与 immutable inputs 的实验计划。当前协议 `execution_ready=false`，没有占位命令、freeze 或 runs。
5. **未来真实查新**：在后续允许的条件下执行中英计划，优先找已经覆盖问题或支持简单方案的工作；若重叠，复用/缩小/停止新 benchmark。当前禁止联网边界继续有效，不能自动启动搜索。

## 明确未完成项

真实文献新颖性和最近 benchmark 比较、原始案例获取、双人标注与裁决、实际切分、可运行评价器/基线、科学实验、模型表现、用户容忍度/生产频率、真实时延/费用、样本量/δ 的最终取值、正式许可和公开发布均未完成。没有联网、安装、模型调用、付费、实验 freeze/run、公共上传或自动化任务。

本轮提案与反解释最初由同一上下文自审；收尾时协调者 /root 在独立上下文检查了分析协议，发现并要求修正区间相对 δ 的方向错误。已保留旧字节，修订 design-v1.1，更新 E1 并逐项完成 H1、E3、优先 B 决策的依赖复核；revision 2 为修订，3–5 为三个 resolve-review。详见 [协调者复核记录](worklog/coordinator-protocol-review.md)。这是实际产物逻辑复核，没有独立学术实验复验，也不能代替真实文献或数据。后续若来源、指标或方案改变，用 Atlas 的依赖队列复查受影响节点，保留历史与失败方向。
