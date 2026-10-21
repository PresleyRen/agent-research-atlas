# 依据与核对记录

日期：2026-10-21。范围仅为 `supervisor-forward/intervals` 的未来决策演练及指定本地 Skill 的相关参考。本轮未联网、未安装依赖、未运行模型、未读取其他项目产物。

## 项目材料

| 来源 | 已读定位 | 本轮作用 |
|---|---|---|
| `PROJECT.md` | 全文；尤其第 3、5、7 行 | 未来情景身份；Δ 的方向；δ = 0.02；严格大于；假定区间方法适用；保留原稿要求。 |
| `old-rule.md` | 第 1 行 | 逐项审核“排除 δ 就挑战”与“含 δ 就加资源”。 |
| `scenarios.json` | 全文件；`/scenarios/0` 至 `/scenarios/4` | A–E 的完整输入；不是运行输出。 |
| `INPUT-MANIFEST.json` | `/files/0` 至 `/files/2` | 只用于核对前三个输入文件的字节数与 SHA-256；不是实验真实性证明。 |

原始输入的完整性检查和逐情景算术位置记录在 [CHECKS.json](CHECKS.json)。该文件的性质是设计规则核对，不能导入或引用为实测结果。

## Skill 参考与采用范围

指定 Skill 根：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas`。

| 来源与定位 | 采用内容 | 本轮未据此声称的事项 |
|---|---|---|
| `SKILL.md`，Begin with the existing project；Match the requested depth；Research loop §3–5；Minimum handoff | 先发现既有状态，按 Design 的有限任务范围工作，保留原稿和未知项，解释支持／挑战／未决。 | 没有把完成文档等同于完成实验或完整研究流程。 |
| `references/local-atlas.md`，Files and reuse；State schema；Incremental writes | 首次写入前阅读；确认发现范围、地图和状态的语义。 | 没有创建空地图冒充文献研究，也没有把文件完整性当科学正确性。 |
| `references/methodology.md`，§8–10；尤其第 239–246 行 | L > δ、U < δ、含 δ、U < 0 的方向性解释；区分严格边界；区间精度与资源动作分开。 | 不验证区间算法、独立性、效应概率或因果识别；未为不存在的测量补值。 |
| `references/evidence-and-claims.md`，§4–6，第 90–168 行 | 实证状态须有真实实验记录；比较、机制、因果、等效等主张各自需要证据；保留计划变更。 | 不把假设情景写成 `pilot_supported`、`independently_supported`、`inconclusive` 或 `refuted` 的项目实证状态。表中“未决”只是一种未来分支。 |
| `references/experiments.md`，Plan schema；Freeze and study mode；What validate-record establishes | 计划中的阈值不是结果，记录工具不判断科学真假，正式方案还需单位、指标、预算和命令。 | 不制造假命令、假预算、假运行、结果导入或正式冻结记录。 |
| `references/supervisor-discovery.md`，§1–3、§7 | 按用户具体决策选择交付物；区分有效反证、测量问题、未检验预测；留存可继续的决定。 | 不要求为五个区间重新完成文献地图、查新或近邻综述。 |

上表中的方法性材料是已读取的本地 Skill 参考。文内列出的上游网页没有访问，本轮没有核验这些网页的内容或版本。

## 推理与草案核对

1. **A 是旧规则的反例。** A 的 0.03 > 0.02；“排除 δ”在这里表示整个区间高于门槛。旧草案却统一转成挑战，方向错误。来源：`scenarios.json` `/scenarios/0`；方法 §10。
2. **B 需要分开方向与实际大小。** 0.005 > 0 且 0.015 < 0.02；小幅改善与未达到预定目标可以同时成立。来源：`/scenarios/1`。
3. **C 是跨门槛未决。** 0.01 > 0，且 0.01 < 0.02 < 0.035；不能将实际门槛未决改写成效应方向未决。来源：`/scenarios/2`。
4. **D 是不利方向。** −0.01 < 0；Δ = baseline − candidate 的定义使整个负区间对应候选损失较高。来源：`/effect`、`/scenarios/3`。
5. **E 是严格边界。** L = 0.02，没有满足 L > 0.02；区间包含相等与严格超过两类值。来源：`/scenarios/4`。这里没有区间下方越过 δ 的值。
6. **资源决策有额外前提。** C、E 不能直接触发无上限追加；应事先确定能改变何种决定、可达到精度、成本与停止依据。此为方法 §9 的计划原则应用，不是由本项目数据估计的资源收益。

边界补充 U = δ 出现在修订规则中，仅用于消除未来使用歧义，不是第六个观察或新输入情景。

## 实际完成的检查

- 读取全部四个原始项目文件，定位全部五个情景与旧规则的两个分句。
- 运行 `atlas.py --root <本项目> discover`：`files_examined = 4`、`candidates = []`、`truncated = false`，扫描上限为 20,000 文件、深度 6。没有发现现成地图。
- 运行 `audit.py --root <本项目> project`：仅报告 `G-MAP`（未选定原生地图），`scientific_verdict = not_assessed`。该项是工作流提示，不是本次区间推理失败；按任务的有限范围，不为演练初始化完整地图。
- 用 Python 标准库 `decimal` 按输入文本精确比较五个区间与 0、δ，并用 `hashlib` 比对原始输入清单；详细结果见 `CHECKS.json`。这是数值和文件核对，未运行统计模型、计算区间或执行研究实验。
- 对交付物进行文字核对：所有研究解释均保留未来条件；没有增加置信水平、p 值、点估计、效应概率、资源数字、最近工作或新颖性结论。

## 保留的未知与限制

项目未指定区间类型及水平、抽样设计、独立单位、数据、基线实现、算力或预算。本任务已明确假定区间适用，所以这些项目没有阻止区间位置解释；若要实际运行，须另行补全并核查。未做文献检索，最近工作与新颖性均不评估。不存在可报告的实测效应、失败运行或独立复验。
