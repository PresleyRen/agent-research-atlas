# Validation report / 验证记录

## v1.2.0 Supervisor–Scientist loop: pre-push results — 2026-10-22

- The branch CI run before correction contained **101 tests: 100 passed, one failed**. The failing bilingual assertion sought English `evidence`, while C29 recorded the equivalent Chinese `证据`. Failure preserved at [Actions run 39711343183](https://github.com/PresleyRen/agent-research-atlas/actions/runs/39711343183). GitHub's fail-fast matrix cancelled sibling jobs; no claim that those versions passed.
- Before pushing the correction, local standalone regression checks for the bilingual gate ran **4/4**, including English, Chinese, absent-requirement and blank cases. The original assertion has been made bilingual without removing the requirement.
- Five real published Agent/RAG papers were checked from ACL Anthology, and one original paper's full-text HTML was read on MIT Press. An offline fixture based on these **real publication records** passed **8/8** deterministic tests on 2026-10-22. See [real-publication case and reading depths](../evals/real_literature/README.md).
- These tests show metadata/claim/counterevidence consistency. They are **not** real model execution, novel research validation, full-text screening of all five papers, or publication acceptance evidence.
- Version-specific **full GitHub CI** is judged only from the exact subsequent tested commit; historical failures are retained rather than relabelled green.

## v1.1.0 Supervisor integration — 2026-10-21

当前候选已扩展到 **77 来源、296 特征、28 能力、28 冲突**。新增 12 个 Supervisor 技能的完整文本审查、三个完整项目任务及一个区间边界微任务。94 项确定性测试在集成后再次通过；独立产物复核发现并修复一处真实的阈值方向错误，初版与修订均保留。

实际任务、74 项新增来源特征的验证边界、图稿原生应用未运行项和版本记录见 [Supervisor 集成验证](supervisor-validation.md)，来源与许可见 [来源审计](supervisor-source-audit.md)。下面的 65/222/24/20 及较早哈希是本次整合前的基线记录，按历史原样保留。

## v1.1.0 pre-Supervisor baseline — 2026-10-20

本版本把验证分为四类：**确定性软件回归、独立代码审查、独立上下文真实任务、外部通路/科研效果**。前三类按下述范围执行；第四类只继承 v1.0 已记录的狭窄中英检索通路观察，没有增加商业账号、训练/云作业或科研发表效果测试。不能把注册表完整、程序通过或任务产物齐全合并成“全部方法都有效”。

### 当前软件回归

从仓库根运行：

```bash
python -m unittest discover -s tests -v
python skills/agent-research-atlas/scripts/audit.py check --repo .
```

本地最终确定性套件 **94/94 通过**，本次运行耗时17.814秒、退出码0。对应发行候选的完整输出保存在 [v1.1-local-tests.txt](v1.1-local-tests.txt)，命令、时间与实现哈希见 [v1.1-local-test-run.json](v1.1-local-test-run.json)。

| 套件 | 测试数 | 具体范围 |
|---|---:|---|
| [test_atlas.py](../tests/test_atlas.py) | 40 | 旧图发现/复用/采用、原文与人工笔记、revision、证据门槛、标识去重、覆盖状态、双语查询、严格JSON、路径与视图序列化。 |
| [test_experiments.py](../tests/test_experiments.py) | 20 | 计划、冻结、授权声明、运行/超时/失败、日志、输入记录、预算和取消、外部结果原字节、路径与格式。 |
| [test_conflicts.py](../tests/test_conflicts.py) | 8 | 固定评价器与可变候选的正反条件；执行中漂移；新反证、依赖传播、循环、复核闭环与可见提示。 |
| [test_audit.py](../tests/test_audit.py) | 10 | 来源/特征/能力/文件/函数/测试映射；损坏引用与依赖；症状定位；本地缺口；数值字段、来源版本和容差。 |
| [test_integration_review.py](../tests/test_integration_review.py) | 16 | 独立构造的跨工具边界：双向tests、移除支持、旧记录兼容、领域待复核提示、严格schema与维护对象、评价器删除/候选变更、大整数与JSON Pointer。 |

软件测试在临时目录执行合成小程序和本地文件检查，不使用真实科研数据、真实模型、GPU、付费服务或网络请求。测试次数不等于独立研究样本数。

### 独立代码审查发现的真实缺陷

[完整审查报告](integration-review.md) 保留了最初失败、逐次补例和最终 **16/16** 通过的日志。实际修复包括：

- 仅有 `experiment --tests--> hypothesis` 时，修改问题也会提示关联计划复核。
- 领域 Markdown 与总览/HTML 一样呈现待复核语境，避免旧 supported 标签被单独引用。
- 保存前校验维护队列、触发路径及审查日志；拒绝不完整 trigger。
- atlas、freeze、attempt、final record 都拒绝布尔值冒充整数 schema 1。
- 数值核对使用精确的解析后数字比较；零容差不能把 `9007199254740993` 与 `9007199254740992` 判成相等。

有益行为一并验证：声明过的候选文件可以变化；固定 evaluator 不得静默变化；旧冻结仍可读但标记 `legacy_unpinned`；当前代码改动不会把已保存的历史记录伪装成新版本，历史日志仍按其真实版本核验。依赖复核保留原科学状态与历史，不自动改成 refuted。

### 独立上下文任务与冲突

新增三个普通项目任务，分别从**混合证据、检索与旧图扩展、方法选择**进入工作流。任务助手从新上下文收到 Skill 路径、项目和正常工作要求，没有收到期望结论或通过答案。协调者另行检查原文件、输出、命令、版本及语义限制。方法任务还使用另一代理审阅竞争解释，但该审阅者并非全新的模型或独立科学复验。

原始夹具、可重用普通任务及精选真实产物见 [evals/README.md](../evals/README.md)；具体结果、协调说明和 **CF01–CF20 逐项实际验证映射**见 [forward-conflicts.md](forward-conflicts.md)。这些任务均为明确的合成场景，本轮研究负载、网络/账号请求、安装、付费与项目发布次数均为零。

第一任务识别了草稿与日志数字矛盾及硬编码评价器，保留失败账本、原始材料和暂停方向；数字吻合只用于材料描述。第二任务修订 provider 请求与推荐种子，保留相关反驳材料、已有 atlas 和未探索状态，并保存注册表在协调期间变化的版本边界。第三任务的阶段选择、竞争解释和外部默认流程处理按实际产物单列报告，不以框架标题齐全判定通过。

这些任务没有测试统计功效引擎、复杂因果估计器、真实新颖性发现率、论文写作整体准确率或上游系统端到端效果。查询请求只被设计和本地核查，没有发送给 Semantic Scholar、Elicit 或其他账号服务。

### 源码、包装与注册表

本轮代码审查及任务使用的关键实现 SHA-256：

| 文件（相对安装 Skill） | SHA-256 |
|---|---|
| `SKILL.md` | `9e2fef60cf0ae464bf8ef4791bfdafca7003eab5c7a6059d9059974214384eee` |
| `scripts/atlas.py` | `bcf13a70cdff1f64dc10d2f054621d182fcd55bca04d9d128dc36d5973e9181b` |
| `scripts/experiments.py` | `653555bf96a36b74419cf47167ce9c9c05d89db774a4ff3bc45175848aae4219` |
| `scripts/audit.py` | `9ad10da5eb49186d9d7a5c0323f2af51b56d52ab1e88d0b766ddb1541e877c61` |

来源注册表属于另行合并的审计元数据；冷任务记录了它的读取版本，后来还更新了采用状态定义和验证引用。此变更不会被写成“任务时所有文件均与最终发布字节相同”。脚本、研究协议和原始任务资料的检查边界分别保留。

- Skill 创建工具的 `quick_validate.py` 返回 **Skill is valid!**；正文保持小于 500 行。
- 三份脚本可编译；离线 viewer 的 JavaScript 通过 Node 语法检查。没有进行新版完整浏览器交互/无障碍/安全审计。
- 注册表检查覆盖 **65 来源、222 特征、24 能力、20 冲突** 的合法ID、采用状态、依赖、互补引用、真实文件/函数与测试引用；这是维护性检查，不能证明来源特色或科学方法全部生效。
- 两种 README 的能力表和文本图均包含 C01–C24；SOURCES 的65来源与覆盖表的222特征均与注册表逐项核对。相对文件链接及代码围栏经本地检查。
- 精选归档的链接核对发现1份交接引用和4份图谱本地来源缺档，已按原字节补入。三个公开快照各自运行 `atlas.py check` 均退出0；这只校验归档的图谱结构与来源路径。

### 远端 CI 与发布核验

[GitHub Actions workflow](../.github/workflows/tests.yml) 在 Python **3.10、3.12、3.13** 执行完整确定性套件、三个脚本编译和 registry check。远端结论应以 发布标签实际对应 commit 的 Actions 运行记录为准；工作流文件存在本身不算运行通过。发布流程先提交候选、核对对应 commit 的任务结果，再创建 release。

### 没有通过这些检查消除的限制

输入保护只检查声明的文件和运行前后观察点，无法检测中途改动后恢复、未声明依赖或任何操作系统/云计费边界。图谱只对已记录的更改传播复核，不能自动感知外部论文改版或本地任意文件变化。`resolve-review` 保存实际审查声明，不证明审查科学上充分。精确数值核对只核对解析后的JSON数据及来源字节，不证明指标定义、测量、独立性或因果解释。

可选方法和外部工具并未完整实现或验证；部分已标 `deferred` 的扩展有明确补法。一般统计、自动全文语义抽取、定时更新和资源调度需要具体工具与项目验证。SCI/SCIE、顶刊/顶会录用及科研成功率都未被本报告建立。

---

## v1.0.0 historical record / 保留的历史验证

Date: **2026-10-20**. Release candidate: **1.0.0**.

This report separates software tests, independent-context task trials, live retrieval checks and scientific effectiveness. The first three were exercised as described below; scientific discovery effectiveness and publication outcomes were not established.

本报告区分软件测试、独立上下文实际任务、真实检索通路和科研效果。前三类按下述范围执行；没有据此声称创新成功率或论文录用率。

## 1. Reproducible local tests

Executed from the repository root:

```bash
python -m unittest discover -s tests -q
```

Observed final result:

```text
Ran 60 tests in 14.795s
OK
```

| Suite | Passed | What it exercises |
|---|---:|---|
| `test_atlas.py` | 40 | Initialization/reuse/adoption, original bytes and notes, revision conflicts, additive updates, graph references, DOI/arXiv identity variants, hypothesis/claim requirements, scoped coverage, staleness, bilingual query planning, path/symlink checks, write locks, JSON ambiguity and generated HTML serialization. |
| `test_experiments.py` | 20 | Successful/failed/timeout execution, raw logs, authorization declaration, plan freeze, checksums, immutable run IDs, conservative budgets/cancellations, lock exclusion, exact-byte external imports, numeric JSON, path/symlink handling and retained incomplete attempts. |

All test inputs and executed workloads are explicitly synthetic and local. No paid services, package installs, real model inference, user datasets or web searches were performed by this unittest suite. Durations vary by machine. Source: [atlas tests](../tests/test_atlas.py), [experiment tests](../tests/test_experiments.py).

### Defects found and fixed before release

An independently written CLI suite initially passed 33/37 atlas tests and exposed four defects:

1. Unversioned arXiv PDF URLs were not deduplicated against their bare identifiers.
2. A paper with both DOI and arXiv identifiers lost its arXiv identity during deduplication.
3. Domain activity status could be confused with exploration coverage.
4. A known unsafe render destination could be rejected only after canonical state had changed.

The implementation now compares all normalized identifiers, keeps domain status separate from coverage, and preflights known output-path hazards before committing state. All four regressions pass. Three additional tests exercise adoption into an existing atlas, changed-import provenance and ambiguous/non-finite JSON rejection.

Preflight is not a multi-file database transaction: disk failure or adversarial filesystem changes after checking can still interrupt view generation. The canonical state is atomically replaced; generated views can be rebuilt. Local history is not externally attested or tamper-proof.

## 2. Skill packaging and viewer checks

- The skill-creator validator returned **`Skill is valid!`** for the completed installable directory.
- The HTML viewer's executable JavaScript passed Node's syntax check.
- HTML parsing tests verified that hostile title strings stay in the inert JSON payload and round-trip as data, rather than becoming injected HTML elements.
- Documentation links, code fences, the 14 taxonomy IDs and JSON syntax were checked.

These checks do **not** constitute a full browser-execution security audit or visual/accessibility review on every device. The viewer has no external library/CDN dependencies. Its graph limit of 140 matching nodes is explicitly announced, while the record index retains all matching records.

## 3. Independent-context task A: resume an existing local map

A fresh agent context received the Skill path and a realistic offline request to continue an existing project. It did not receive implementation answers, expected node counts or bug hints. The artificial project contained one Chinese Markdown map with:

- A reported debugging observation involving 18 hand-written inputs, without the original inputs or runnable baseline.
- A question about one clarification turn versus extra latency.
- Unknown data rights, GPU access and paid-API budget.
- A paused keyword-routing direction and a human note about annotation ambiguity.

Observed result, independently inspected by the coordinating agent:

| Check | Observed outcome |
|---|---|
| Reuse instead of blind replacement | Existing map was read, adopted, and semantically normalized with a provenance record. |
| Preserve source | Original SHA-256 stayed `4de6e26cef14b947baae1b09f40c62cc94adad729f60ba7e7bd899e97e8a17a3`; original notes and a byte backup were retained. |
| Persistent map | Revision 1, 28 nodes, 21 explicit edges; 14 domain folders and HTML/Markdown maps generated. |
| Research candidates | Three proposed hypotheses; one retrieval-related hypothesis parked pending access/resources. |
| Honest evidence state | All 14 literature domains remained unsearched; no papers or actual searches were invented. |
| Bilingual next steps | Chinese/English query plans saved as not executed, alongside resource and candidate files. |
| Failed-direction memory | Keyword-rule work remained paused with a reopening condition. |
| Final structural check | `atlas.py check` returned valid. |

The coordinating agent separately reviewed the one-turn clarification proposal. That review tightened the single primary metric and clarified that “always clarify” is a cost-curve reference, not a matched-budget comparison. This was a logic review, **not** literature verification, empirical support or blinded peer review.

## 4. Independent-context task B: run a bounded local experiment

A second fresh agent context received the Skill path, a project containing the hand-authored [tiny synthetic experiment](../examples/tiny_agent_experiment.py), and a request for exactly seeds 7 and 13. The budget was two runs, at most 3 seconds each, 6 seconds reserved in total. It was instructed to inspect the code and operate offline, with no installations or paid services.

The agent inspected the source, recorded and froze an **exploratory** plan, ran the two authorized payloads, preserved logs, interpreted the results, and updated the atlas.

| Seed | Direct process status | Fixture accuracy | Synthetic constant-label baseline | Runner elapsed seconds |
|---|---|---:|---:|---:|
| 7 | succeeded, exit 0 | 1.0 | 0.18333333333333332 | 0.03595322199998918 |
| 13 | succeeded, exit 0 | 1.0 | 0.31666666666666665 | 0.03523815999960789 |

**The accuracy of 1.0 is hard-coded in the fixture.** It is not a measured Agent routing result. The agent identified this from the code and explicitly rejected the claim of perfect real-world routing. The fixture also prints a fixed elapsed value; the table uses the runner's independently recorded local elapsed time instead.

Observed record details:

- Freeze time: `2026-10-20T03:09:39.975182Z`.
- Frozen plan SHA-256: `012326144ba46426518be71275e748415103af8a1be4cd1ca47e3d7e1ad70874`.
- Exactly two payload runs; full 3+3-second reservations consumed, without refunding unused time or running a third trial.
- `validate-record` returned `integrity_checked`, no incomplete attempts, and `scientific_verdict: not_assessed`.
- Final atlas: revision 2, 24 nodes, 12 explicit edges; final `check` returned valid.
- A process-completion claim was supported; a perfect-real-routing claim was unsupported; the real research hypothesis remained proposed.
- All 14 literature domains remained unsearched. Eight bilingual query rows were planned, not executed.

This tested plan→freeze→run→logs→interpretation→map maintenance. It did not test a real model, independent scientific replication, causal mechanism or research novelty. The coordinator subsequently inspected both raw run records and re-ran their integrity validation.

During development, the coordinating agent patched `atlas.py` after the experiment runs to fix atlas regressions. The trial recorded this tool-version boundary; the payload and experiment recorder were unchanged. Final map checks used the updated atlas tool. No historical experiment record was rewritten to conceal the change.

## 5. Live Chinese/English retrieval smoke

[retrieval-smoke.md](retrieval-smoke.md) records exact live queries, successfully opened original Chinese/English paper records and failed access. One Chinese journal record and two English conference records were opened at metadata/abstract depth. The report explicitly retains article-page timeouts and untested database-native searches.

This verifies those narrow retrieval routes. It does not measure comprehensive recall, full-text claim accuracy, access to paid providers, freshness across all Agent subfields or successful hypothesis discovery.

## 6. CI and reproducibility

The repository includes [a GitHub Actions workflow](../.github/workflows/tests.yml) for the same deterministic suite on Python 3.10, 3.12 and 3.13. The local outcome above is an observed result. The presence of a workflow is not evidence that a particular remote run passed; inspect the repository's Actions page for live results.

To repeat a forward task, create a separate project containing your own nonsensitive map or a copy of the synthetic example, give a fresh compatible host the Skill path and a normal user task, and inspect its artifacts. Outputs from a language-model-driven task are not expected to be byte-identical. Keep the test budget and the distinction between proposed, observed and supported explicit.

## What remains unproven

No test here establishes complete literature coverage, correct scientific reasoning on every problem, autonomous general research ability, improved publication success, SCI indexing or acceptance by a leading journal/conference. No commercial literature service was installed or authenticated. A local runner does not provide operating-system isolation or enforce cloud charges. These are material limits, not hidden assumptions.
