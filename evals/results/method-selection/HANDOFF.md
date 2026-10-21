# 交接：版本变化与意图含糊时的路由

日期：2026-10-20。**本轮交付完成并停止；仅本地阅读、分析、项目文件整理与校验。SYNTHETIC教学材料，未产生研究运行结果。**

## 当前最重要的决定

优先 **M0：恢复原例和版本出处，检查标签及路由时可见信息能否区分缺口**。先看缺的是用户目标还是适用证据，再决定是否值得发展新的路由方法。C1优先的原因是最能改变下一步选择，不是已知它更有效。[原始开发线索](docs/observations.md)、[资源约束](docs/resources.md)

| 候选/遗留方向 | 当前状态 | 下一步 |
|---|---|---|
| C1 缺失信息来源与动作选择 | `proposed` | M0先行；通过后做M1配对四格动作诊断。 |
| C2 答案不变时减少澄清 | `proposed` | C1之后，比较固定提问与条件式回答，防止答案差异标签泄漏。 |
| C3 检索停滞后换动作 | `parked` | 取得逐次检索轨迹后重启；不从“重复两次”定阈值。 |
| 遗留更大reranker | `parked` | 正确版本已召回却被排序/装配压制、且简单过滤不足时再考虑。 |

没有方向被实测反驳，没有假设进入grounded、testable或经验支持状态。更强检索器的默认偏好仅作为无比较支持的来源主张保留。[定位笔记](surveys/overview.md)

## 已完成的具体交付

- [简明地图](docs/research-map.md)：候选、依赖和当前状态的中文入口。
- [问题锚点](docs/problem-anchor.md)：目标、非目标、固定条件与未知资源。
- [候选与方法取舍](docs/candidates-and-methods.md)：三个候选、机制/预测/竞争解释、最近工作缺口、C1方法卡、共享流程逐项裁决。
- [最小判别方案](plans/minimal-discriminating-study.md)：M0恢复/遮罩标注、M1四格/基线/指标、泄漏与依赖、成本、支持/负结果/无法判断分支。
- [双语检索续接表](plans/retrieval-followup.md)：下一轮查询与真实not_run覆盖收据；不是本轮查新结果。
- [独立上下文审阅](reviews/2026-10-20/independent-review.md)：实际意见、采用决定与独立性的限制。
- [材料清单](reviews/2026-10-20/source-ledger.md)、[完整材料哈希](reviews/2026-10-20/source-ledger.json)、[技能路径/哈希](reviews/2026-10-20/skill-provenance.json)、[命令回执](reviews/2026-10-20/validation-commands.json)、[最终检查](reviews/2026-10-20/final-artifact-check.json)。

## 当前图谱

规范文件：[research-atlas/atlas.json](research-atlas/atlas.json)，**revision 7，28节点、12边**。生成视图：[MAP.md](research-atlas/MAP.md)、[离线交互地图](research-atlas/map.html)；人工续接说明：[routing/notes.md](research-atlas/domains/routing/notes.md)。

六个相关领域仅有本地教学材料定位，保持partial；其余八个种子领域为unsearched。真实论文记录0。两份experiment节点是design-only，均未冻结/执行。没有既有地图需要导入，imports=0。初次来源关联触发六个领域待复核，均按具体材料重新核对并记录理由；当前pending=0，不能据此宣称文献覆盖或机制已经成立。

## 续接顺序与资源门槛

先读本交接、问题锚点和M0。恢复原始问题、目标版本依据、完整版本文档、当时的片段与轨迹，并核实权利；目标未知时不能直接给策略“证据过期”标签。隐藏目标/有效性只供评价器，理想状态路由单列为诊断上界。一家族的四变体保持配对，25条描述的单人来源与已用于选题的事实继续保留，不能转成独立评测集。[S04](docs/resources.md)

M0若不可判，转向任务定义/元数据/可观测性；若强简单规则已充分，保留诊断价值，停止堆复杂组件。只有M0通过、数据/评价器/CPU实现及未来执行范围可用，才建立真实计划、明确预算、检查方法→代码→指标→真值，再冻结/运行。本轮没有执行这个后续步骤，也没有为schema捏造正数预算或输入文件。

真实近邻和新颖性仍未核验。未来允许检索时，先核对C1的近邻、简单替代和反证，记录实际provider/查询/日期/访问深度；本轮无在线请求，不能把not_run写成“未发现相关工作”。

## 保留、变化与方法裁决

原五文件全部保留；已有五类路线、检索/澄清取舍、两类失败线索、大reranker建议及共享流程原文均可回查。本轮新增的是有来源的区分、候选和后续判别设计。

采纳共享流程的问题锚点、固定/可变条件、竞争解释与早期分支测试；不执行清空目录、强制十框架/四十候选、8.5分认证创新、无预算付费/安装和自动公开。取舍依据为本任务授权、原始资源约束及技能C08/C12、CF04/CF15契约；[能力定位回执](reviews/2026-10-20/method-capability-locate.json)保留，技能源文件未修改。

## 实际检查与精确版本

| 检查 | 结果 |
|---|---|
| 五份原始文件SHA-256 | 5/5保持不变 |
| 实际使用的技能/脚本/模板文件SHA-256 | 14/14保持不变；整个技能目录前后文件对账无变化 |
| 图谱结构 | valid=true；revision 7；引用存在、状态合法 |
| 本地来源路径/版本 | 问题数0 |
| HTML静态检查 | 内嵌状态与atlas一致；无外部主动资源或网络调用指示；未做浏览器渲染验收 |
| 项目缺口 | G-COVERAGE-UNSEARCHED, G-FEASIBILITY继续保留；不是为消除警告而把覆盖或资源写成可用 |
| 文档链接与当前产物 | 见最终检查中的逐项结果；自检脚本只做文件/结构/哈希校验 |

指定技能正文路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/SKILL.md`。SHA-256：`9e2fef60cf0ae464bf8ef4791bfdafca7003eab5c7a6059d9059974214384eee`。

实际执行工具：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/atlas.py`，SHA-256 `bcf13a70cdff1f64dc10d2f054621d182fcd55bca04d9d128dc36d5973e9181b`；`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/audit.py`，SHA-256 `9ad10da5eb49186d9d7a5c0323f2af51b56d52ab1e88d0b766ddb1541e877c61`。其余协议、解析依赖与模板路径/哈希/读取深度见完整技能清单。`experiments.py`仅被audit解析依赖导入，没有调用实验CLI或研究runner。

本轮网络请求、安装、研究负载、付费调用与发布均为0。文件校验不能认证机制、标签、新颖性或发表价值；完成本次可审查交付后停止。
