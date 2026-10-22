# 快速定位不足与扩展 / Locate a gap and extend it

Agent Research Atlas uses one capability registry as its maintenance index: [capability-registry.json](../skills/agent-research-atlas/assets/capability-registry.json). Each source feature maps to one or more `Cxx` capabilities; each capability maps to a protocol or function and a verification record. Optional integrations and untested work remain explicit.

## 从症状找到负责位置

| 遇到的问题 | ID | 首先改哪里 | 用什么验证 |
|---|---|---|---|
| 新领域没有术语/目录 | C01/C03 | `assets/agent-taxonomy.json`; `references/agent-domains.md`; `atlas.py::queries` | 双语查询、未探索初始化、保留旧域回归 |
| 旧图被重复建立/手写内容丢失 | C02 | `atlas.py::discover`, `Atlas.init`, `Atlas.write_view`; `local-atlas.md` | 旧图复用、原文哈希、并发 revision、notes 保留 |
| 中文与英文检索差很远 | C03/C22 | `bilingual-retrieval.md` 的 provider-syntax、optional-adapter-contract | 两种语言、空结果、限流/无权限、语法不支持的独立任务 |
| 同一论文算两次/引文图代替证据 | C04/C06 | `atlas.py::canonical_identifiers`; evidence/provenance 协议 | DOI/arXiv 多身份；全文深度和 studies/reports 差别审查 |
| 点子只有模块拼接/最近工作未排除 | C07/C09/C10 | `methodology.md` 的策略选择、问题锚点、四轴比较 | 空搜索/记忆文献/强基线反例场景；不能用标题相异认证创新 |
| 问题重要却本地做不了 | C08/C11 | problem-selection 工作台；`atlas.py::validate` | 数据、算力、评价器、预算未核实时禁止提升 testable |
| 实验跑了却不是所提方法 | C12/C13 | method→code→metric/GT 审计台；计划模板 | 实现卡、比较单位/预算、指标是否被实际调用 |
| 自动调优顺带改了评价器 | C14/C15 | `experiments.py::freeze_plan`, `run_local` | 冻结前后 evaluator 漂移拒绝；允许 candidate 修改；失败不退预算 |
| 表格数字与日志不一致 | C16/C18 | `audit.py::audit_values`; `evidence-and-claims.md` | JSON Pointer 数值、缺失字段、不可解析、版本哈希、舍入容差 |
| p 值、种子数或样本量不适用 | C17 | `methodology.md` 的统计目标/单位/精度工作台 | 设计特定统计验证；不能把数值抄写测试算作统计方法测试 |
| 新论文来了旧结论还在用 | C20 | `atlas.py::dependency_links`, `impact`, `update_review_queue` | 双向 tests、移除支持、传递/循环、清除后重新触发、各视图提示 |
| 引用存在但并不支持这句话 | C21 | citation existence/metadata/context 与 claim audit | 对每次出现位置检查相邻句；定位不充分时缩小/删除表述 |
| 两个方法互相冲突/不知道怎么选 | C19/C23 | registry `conflicts`, `methodology.md`, `audit.py::locate` | 必须保留原冲突例并验证好的两侧条件；不要只比模型自评分 |
| Benchmark 构建/真值/划分/诊断不足 | C25 | `supervisor-publication.md` §2；`assets/supervisor/benchmark-dossier.md` | 合成案例家族泄漏、oracle信息、无配套模型的完整评测设计任务 |
| 引言/正文写不成稿或润色改变结论 | C26 | `supervisor-publication.md` §3–5；`manuscript-evidence.md` | 数字冲突、计划与实测、关联与因果、clean prose与sidecar分离 |
| 审稿意见漏答/行动状态错误 | C27 | `supervisor-publication.md` §6–7；`review-response.md` | 原意见ID全覆盖、复合意见拆分、planned不写completed、实际修订位置 |
| 图稿不能编辑或预览无法验收 | C28 | `supervisor-figures.md`；`figure-brief.md` | native对象/连线、坐标方向、来源数据、真实预览与未决项 |
| 想接 HF 训练/云作业/商业检索 | C22/C24 | optional-adapter-contract，新增独立 adapter | 无账号、权限、预算、超时、版本不兼容回退；实际运行后再更改 tested 状态 |
| 导师意见泛、方向没有明确 proceed/pivot/stop | C29 | `research-supervision.md`; `assets/supervision/mentor-panel.md` | 公开证据范围、Supervisor decision vocabulary、不同lens分歧与next task |
| future work/高引用/空搜索被直接当创新点 | C30 | `research-supervision.md`; `assets/supervision/gap-ledger.md`; `atlas.py::validate` | source_kind、later work、open/partial/solved/invalid状态及无证据拒绝 |
| 引用很多但以后写作无法证明句子 | C31 | `research-supervision.md`; `assets/supervision/citation-corpus.md`; `evidence-and-claims.md` | locator、can-support、cannot-support、stale/version复核 |
| Scientist一直实验却不会回文献/换方向 | C32 | `research-supervision.md`; `methodology.md` | Scientist→Critic→Supervisor loop；pivot/park/stop和CF29边界 |

路径均相对 `skills/agent-research-atlas/`，测试目录位于仓库根。CLI 返回精确文件与函数定位；上表用于人工快速阅读。

```bash
python skills/agent-research-atlas/scripts/audit.py locate --query '数值'
python skills/agent-research-atlas/scripts/audit.py locate --query 'C20'
python skills/agent-research-atlas/scripts/audit.py --root /path/to/project project
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

`project` 的 G-* 是本地研究记录缺口，C-* 是技能负责模块。二者不是“自动发现科研创新点”的分数。定位为空时换短词或 ID；不要猜造新能力已存在。

## 扩展步骤与验收

1. 写最小复现：实际输入、期望行为、观测结果和影响。用合成或经授权的数据建立可分享回归；保留原版本失败记录。
2. 在 registry 选择现有 C-ID。只有职责确实新增时新增 ID；声明依赖，禁止循环依赖。研究图本身可以有循环关系，能力依赖图应保持可维护的先后契约。
3. 新来源要记录官方 URL、commit/检查日期、读到什么、未读什么。每个特长要有 status、capabilities、gap、remedy 和可核查的 complements。`protocol` 不能写成原生执行；`optional` 不能写成账号实连。
4. 修改所属文件与数据契约。优先组合既有 paper/evidence/experiment 记录，避免出现第二个互不一致的论文库、评测结论库或失败记忆库。
5. 为真冲突补正反两侧：允许的有益行为仍能完成，不合理升级/越权/数据混淆会被阻止或显式标记。一次高分、无报错或框架文本齐全不足以通过科学审查。
6. 执行相关回归，再跑 registry check；若改变宿主推理，使用未见预期结论的新上下文正常任务。记录未执行的服务/方法测试及原因，不补虚假的通过率。
7. 更新 README 能力表、文本图（若流程改变）、SOURCES/审计报告与 CHANGELOG。发布前核实远端当前 HEAD；正常提交新版本，保留用户已有内容和历史。

## 三类常见扩展

**新增 provider。** 首先实现规范化请求与回执，不假设通用布尔语法通吃。必须区分 planned / succeeded / empty / blocked / rate_limited / failed，保留 exact query、provider、日期、语言、来源 URL、元数据/摘要/全文深度与定位。不把 S2 的 negativePaperIds 当反驳文献；不要隐式启用付费任务、定期搜索或共享项目。先用不含凭证的固定回执测试契约，再在已有授权下做一次真接口测试。测试记录完成之前继续标 optional/untested。

**新增方法。** 例如自适应路由的非劣设计：先说明 estimand、实验单位、非劣界限来源、配对与聚类依赖、主要分析和失效条件，再接适用统计实现。已提供的数字核对工具不能取代非劣统计检验。为零效应/边界效应/设计违例加与实际分析一致的验证；模拟失败保留在分母，报告 Monte Carlo 不确定性。

**新增执行 backend。** 将本地已冻结协议映射到 backend job，并带回真实 run ID、配置、模型/数据版本、原始结果和预算。GPU/云成本应由 backend 的真实计费/配额机制控制；本地秒数预算不能声称覆盖远端花费。外部结果通过 `import-result` 保留来源且不自动认定独立复验。

## 版本与回归原则

- 原生 atlas schema 1 保持兼容。新增 maintenance 字段通过正常写入产生；不得伪造旧审查。
- v1.0 frozen plans 保留 `legacy_unpinned`；新输入固定策略不会追溯到旧记录。
- 旧来源笔记、失败/零结果、状态理由和原始字节必须保留。对错误证据添加更正/替代关系，不从历史抹除。
- `check` 只校验可维护性声明和路径，不证明特色已被完整实现、适配器可用或科研结论成立。
- 审计不是一次性结论。上游变更时更新它的 revision、受影响特长和冲突回归；不要直接拉入整套默认工作流覆盖当前项目。

## 新增研究工作台

Supervisor 接入展示了怎样扩展协议而保持同一项目记忆；v1.2 的 Research Supervision 又增加 C29–C32，把导师决策、论文级 gap、引用语料和 Scientist–Critic 循环接到同一 Atlas。新工作台明确任务入口、输入、决策、输出及证据依赖。研究简报、Benchmark、论文与审稿文件仍引用既有 paper/hypothesis/experiment/claim ID。画图按科学设计、原生对象、导出与视觉检查分别定位；没有必要为每个来源创建一套研究数据库。

添加来源后运行 `python tools/render_audit_docs.py`，从注册表重新生成 SOURCES 与逐特征覆盖表；再更新中英文 README 的任务/能力说明，执行 registry check 和受影响的普通项目任务。来源的许可范围与改编说明一起更新，不能把可选上游运行时写成已经集成执行。

## Supervision / gap 扩展原则

- 新的导师视角必须说明公开证据来源与 direct / recurring inference / speculative extension 等级；不要新增人格扮演。
- 新 gap extractor 必须输出 source kind、原文 locator、later-work 核验和边界；不能把 Future Work 或零命中直接升级为 open gap。
- 新引用 provider 必须能回收到稳定 paper ID、访问深度和 claim-support 位置；bibliography 规模不算覆盖验证。
- 新循环/agent 角色要接到 Supervisor decision contract；不得用“never stop”覆盖预算、授权或停止条件。
