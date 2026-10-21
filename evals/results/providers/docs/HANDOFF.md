# 接续交接：时变意图与撤销约束

日期：2026-10-20。项目根：`/workspace/scratch/f7a517081da8/forward-conflicts-providers`。

**本轮已完成本地续作。当前地图 revision 4，共 30 个节点、15 条边。没有真实网络/账号请求，没有安装、研究实验、付费负载或发布。** 本项目及三份“论文”均为 SYNTHETIC 教学材料。

## 从这里继续

| 入口 | 保存内容 |
|---|---|
| `research-memory/MAP.md` | 15 个领域的概览，均保留真实文献覆盖 `unsearched`。 |
| `research-memory/map.html` | 离线交互地图；嵌入数据与 canonical atlas 一致。未做真实浏览器交互测试。 |
| `research-memory/atlas.json` | 当前权威记录；旧 ID、历史、依赖和复核记录均保留。 |
| `research-memory/domains/temporal-intent-revocation/MAP.md` 与 `notes.md` | 新方向的地图与人工接续笔记。 |
| `docs/RESEARCH-DIRECTION.md` | 问题边界、主机制、六类替代解释、判别设计、资源与停止条件。 |
| `docs/EVIDENCE-LEDGER.md` | 支持、反驳、无关材料的条件与定位；原有失败分支及评审来源更正。 |
| `docs/RETRIEVAL-PLAN.md`、`docs/requests.json` | 8 个双语检索单元、19 个未执行请求草案、语法与种子修订、真实请求回执契约。 |
| `docs/CAPABILITY-GAPS.md` | Cxx 负责位置、当前限制、互补服务和未来验收路线。 |
| `docs/audit/SOURCE-FOOTPRINT.md`、`source-footprint.json` | 实际使用的技能正文/脚本绝对路径、SHA-256 与读取/执行深度。 |
| `docs/audit/command-index.json`、`validation-summary.json` | 实际命令、退出状态、失败与最终校验摘要。 |

## 当前研究判断

最值得继续检查的问题是：**当撤销已对执行层可见、动作仍可阻止时，正确意图是否仍未同步到动作提交边界？** 主候选 `hyp-versioned-intent-execution-gate` 保持 **proposed**。真实最相近论文为空；不能用合成 `local-*` ID 填补真实近邻或外部 provider 身份。

`local-support` 仅给出固定动作预算下的路由支持线索；`local-counter` 是带噪澄清的相关反证，两者都保留。`local-irrelevant` 因水果颜色分级与当前决策机制无关而排除，原节点仍保留。反例限制宽泛外推，但没有直接反驳尚未测试的时变意图机制。[精确位置：三个 `papers/*.md` 各第 1 行；`EVIDENCE-LEDGER.md`。]

`past-decision` 继续暂停“增加关键词”：必须先查标签歧义，不能把新方向当作无条件重启理由。此前“三位独立评审一致认可”已更正为同一上下文的三个角色串行自审；原团队笔记与原始请求按字节保存于 `docs/history/`。本轮语义复核也明确记为同一执行代理自审。

未来最小判别顺序是：先核实标签和时间线/动作提交语义；再在相同正确意图、相同信息与预算下比较路由时检查、强确定性取消规则和执行时版本/范围复核；最后才独立加入澄清噪声。必须同时观察撤销违规、合法任务完成率、误取消与成本。强规则或正确标签若已解释全部收益，应缩小或暂停方法主张。方案已写好，未执行、未冻结，也没有结果文件。

## 检索如何接续

本轮已完成的是查询设计与本地阅读。16 个 S2 relevance 普通文本草案覆盖 8 个中英单元；另有 1 个仅记录种子角色的 S2 recommendation 草案和 2 个 Elicit semantic 自然语言草案。全部为 `planned`、`executed:false`、`sendable:false`；`submitted_query`、真实结果和命中数为 null。

改动包括：不再把通用 AND/NOT 直接给 S2 relevance；不排除 failure；不把相关反驳放入 negativePaperIds；不把 synthetic local IDs 当真实 S2 ID；Elicit 不再 keyword/filters 混用。基础工作不限起始年份，2024 年以后仅作为独立近期补查。

若下轮仍只准本地，继续读取新提供的合法材料或澄清标签/边界；不执行草案。只有新的实际授权允许公开检索后，再核对当时 provider、版本、访问与成本边界并执行优先单元 Q01/Q02/Q04/Q06 的中英两路。账号无权、限流、语法失败、成功空集和未执行都必须分别保存，不能被写成新颖性结论。该交接不授权未来联网、付费或后台任务。

## 实际写入与复核轨迹

1. 复用配置指向的 revision 1，没有运行 `init` 或 `adopt`。
2. `upsert --expected-revision 1` 写入 `docs/update-batch-2026-10-20.json`，生成 revision 2 及离线视图。首次相对 `--file` 路径在工作目录解析失败，未改地图；改用绝对路径成功，两个回执都保留。
3. 视图语义检查发现一个 claim 的否定表述与 `contradicts` 边指向的肯定外推不一致。用单独 correction batch 修正为受审查的肯定命题，状态仍为 unsupported，保存 revision 3。
4. 依赖队列实际触发 `decision-continue-temporal-slice` 的复核。重读证据和继续条件后，使用 `resolve-review --expected-revision 3` 留下同代理审查理由，得到 revision 4；没有直接修改 maintenance。当前 pending review 为空，有一条复核历史，未完成语义导入为空。

不要重新执行已应用的 batch，也不要用重建地图清理记录。下一次变更先读当前 revision 与 pending queue，给新证据/变更写来源与原因，使用新的 batch 和当前 expected revision。

## 实际校验及保留的失败

| 步骤 | 真实结果与证据 |
|---|---|
| `discover`、`status` | 找到配置中的唯一原生 atlas；discover 未截断；基线 revision 1，无 pending import/review。回执：`discover-before.json`、`status-before.json`。 |
| `audit.py locate` | 实际定位 C01、C02、C03、C04、C05、C06、C09、C11、C13、C17、C19、C20、C22、C23、C24。逐项回执在 `locate-Cxx.json`。 |
| `audit.py check --repo` | 对当时读取的注册表快照返回 valid；核对 24 能力、65 来源、222 特征、20 冲突和声明的测试引用。没有执行注册表列出的整套测试或真实 provider 检索。 |
| `queries --domain routing` | 生成 8 条包含双语 focus 的计划，exit 0；没有执行检索。 |
| `queries --domain temporal-intent-revocation` | 即使自定义域已入图，仍返回 Unknown seed domain，exit 2；这是已确认的 planner 边界。使用宿主双语账本继续，没有改词表或源码。 |
| `atlas.py check` | 最终 revision 4、30 节点、15 边、valid true，exit 0。 |
| `audit.py project` | 保留 15 域 unsearched 与 H1 资源未核验两类缺口；scientific_verdict 为 not_assessed。 |
| `impact --node local-counter` | 反例变化可定位宽泛外推、候选、继续决定、检索计划与判别设计的下游关系；没有自动升级科学状态。 |
| 项目完整性检查 | 20 项中 19 项通过：原始材料/请求/人工笔记/旧 revision、反证、暂停分支、计划标记、双语矩阵、HTML 与 canonical 数据一致等。原命令 exit 1 原样保留，因为它正确发现了下述源码版本边界。 |

### 必须保留的源码版本边界

本执行代理只在项目内写文件。父级主流程确认：在本次冷任务运行期间更新了技能源目录中的 `assets/capability-registry.json` 来源清单/采用范围元数据，之后还可能改验证引用和 optional 定义。16 个快照文件中，其余 15 个在本次结束检查时未变；脚本与研究协议在冷任务阶段保持固定。

因此不能写“全部技能源文件未变”或把源码未变检查改成通过。读取时与结束时注册表 SHA-256、父级确认及检查边界都保留在 `docs/audit/source-version-boundary.json`；完整用到的路径/哈希见 `SOURCE-FOOTPRINT.md`。本项目的 19 项完整性检查通过与这个并发元数据变化分别记录于 `validation-summary.json`，原 `integrity-check.json` 的失败没有被覆盖。

## 下次可直接执行的本地检查

以下命令只有本地读取/校验，不包含研究执行。使用绝对输入路径；`--root` 不会自动把 `upsert --file` 的相对路径改成项目相对路径。

```bash
python -B /workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/atlas.py --root /workspace/scratch/f7a517081da8/forward-conflicts-providers status
python -B /workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/atlas.py --root /workspace/scratch/f7a517081da8/forward-conflicts-providers check
python -B /workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/audit.py --root /workspace/scratch/f7a517081da8/forward-conflicts-providers project
python -B /workspace/scratch/f7a517081da8/forward-conflicts-providers/scripts/validate_continuation.py
```

最后一个检查脚本会继续报告旧快照与当前源树的任何差异，这是预期的版本提示；先读对应版本边界，不能改基线哈希来获得全绿。结构校验、依赖复核和静态 HTML 检查都不认证科学有效性、新颖性、统计充分性或外部服务可用性。
