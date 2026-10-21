# 新版记录工具的独立代码复核

日期：2026-10-20 UTC。复核者：ChatGPT 集成审查代理；实现修复者为父任务代理。

这是知道功能目标并读取实现后的代码审查与定向软件回归，**不是 blind forward 试跑，也不是研究假设的独立实验验证**。本代理只新增 `tests/test_integration_review.py` 与本报告/对应日志，没有修改 scripts、根 README 或 SOURCES。所有新执行均为标准库、本地临时目录和明确的合成测试负载；没有安装、联网、付费或使用真实数据。

## 结论与复核范围

范围包括 `atlas.py` 的依赖影响、待复核队列及闭环，`experiments.py` 的冻结输入、允许修改的候选代码、运行前后漂移与旧格式兼容，以及 `audit.py` 的数值 JSON Pointer 核对。审查区分记录完整性、执行成败与科学判断；没有把 `integrity_checked` 或 `all_values_match` 当成科学证据成立。

**最终状态：所发现的问题均已由父任务修复，16 条定向回归全部通过，耗时 0.601 秒。** 在本次审查范围与下列精确加载版本中，没有留下已复现而未修复的问题。初始失败与后续验证日志均保留，不以最终通过覆盖发现过程。

## 具体发现与修复验收点

| 发现 | 最小复现与影响 | 修复验收点 |
|---|---|---|
| 计划依赖方向遗漏 | `planned experiment --tests--> proposed hypothesis`；仅修改假设预测，计划未进入待复核，可能继续执行旧问题的方案 | `tests` 同时传播结果对解释、问题对计划的复核需要；只标记 review，不自动改变科学状态 |
| 领域视图丢失待复核语境 | overview/HTML 显示 pending，但 `domains/routing/MAP.md` 仍只呈现 supported | 在对应领域记录旁明确标注 Needs review / 待复核，保留历史状态的含义 |
| 待复核对象校验不完整 | `maintenance.pending_reviews[].triggers=[{}]` 被结构校验接受，后续渲染会访问缺失的 source_id | 校验 trigger、来源、路径、revision 和 review_log；在保存前拒绝不完整对象 |
| 布尔值被当作 schema 版本 1 | atlas、freeze 原先使用 `== 1`；Python 中 `True == 1`，违反 JSON 类型边界 | schema 必须是整数；冻结、attempt 和 final record 都须检查，不依赖宽松比较 |
| final record 仍有同类残留 | freeze/attempt 已修复后，final record 与 attempt 的字段 `!=` 比较仍接受 `true` 对 `1`；新增子例实际复现 | final record 自身也显式检查 schema 类型，再比较与 attempt 的关联 |
| 零容差核对错误接受不同大整数 | JSON 观测 `9007199254740993`，报告 `9007199254740992`；原 math.isclose 转 float 后返回 match | 对解析后的数字使用精确有理运算，明确绝对/相对容差；不同整数在零容差下必须 mismatch |

另有“删除已有 supports 关系应复核原消费者及后续计划”的定向回归：首次执行时已通过，父任务正在并行修复该路径，因此不将该项描述为本代理首次复现的新缺陷。检查所见实现使用旧/新依赖图及关系的对称差，覆盖移除和新增关系。

## 已验证的有效行为

- **可变候选与固定评价文件分开处理。** 允许声明为 mutable 的候选脚本在执行期间变化，记录前后两个 hash；固定 evaluator 删除时，即使子进程 exit 0，run 也标记 failed，保留 InputIntegrityError 和真实退出码。
- **历史证据不被当前代码变化误伤。** 完成一次合成运行后再改当前源文件，原记录仍能通过历史日志完整性验证；这不会追认新代码等于旧实验代码。
- **旧格式清楚标识。** 缺少新 frozen-input manifest 的旧 freeze 仍可读取，返回 `input_policy=legacy_unpinned`。未把旧格式伪装成已经固定输入的新版记录。
- **待复核可以闭环并重新开启。** 对 `uses` 反向依赖及传递消费者，记录 review 的人、理由和 revision；明确解决后新证据再次变化会重新排队，已有 supported 状态本身不自动改成 refuted。
- **数值定位保持语义限制。** 转义路径 `/a~1b/~0key/1` 正确定位；数字相等而来源 hash 变化时仍标 version_mismatch；布尔值不当数值；不存在文件也不能掩盖错误 Pointer 语法。

## 旧项目兼容核查

只读调用新版 `validate-record` 和 `atlas check` 检查已有 `forward-experiment`，没有再次运行其 payload：原两条 seed 记录仍为 succeeded，无 incomplete attempts，返回 `input_policy=legacy_unpinned` 与 `scientific_verdict=not_assessed`；地图仍为 revision 2、24 节点、12 边，check 通过。

该操作验证已有记录可读，不算第三次实验、不消耗旧计划的新增运行额度，也不增强它的科学证据等级。

## 测试与版本记录

测试文件：`tests/test_integration_review.py`，16 个 test 方法（其中 schema 方法另外覆盖 final-record 子例）。测试加载器对实际读取并执行的每份源码字节计算 SHA-256；直接运行测试文件时，日志首行 `REVIEW_SOURCE_SHA256` 给出精确加载版本。未依赖不存在的 git 提交标识。

| 阶段 | 结果 | 记录 |
|---|---|---|
| 初始 10 条集成回归 | 6 通过、4 失败，约 0.625 秒 | `docs/integration-review-tests-initial.txt` |
| 新增 audit / metadata 6 条 | 4 通过、2 失败，约 0.018 秒；无 payload | `docs/integration-review-tests-audit-initial.txt` |
| final-record schema 子例 | 原 freeze 检查通过，final-record 子例失败，约 0.012 秒；无 payload | `docs/integration-review-tests-record-schema.txt` |
| 最终 16 条回归 | **16/16 通过，0.601 秒，exit 0** | `docs/integration-review-tests-final.txt` |

初次源码读取时 atlas.py 的磁盘 hash 为 `50ac7670138d9465e15ec0576f1d52e85dce6d108a025f896236110df68c4995`，experiments.py 为 `8a4e50197418adefc34ddc12630afbbaa57eb71398038d0cae7dfd091f51318a`。首轮运行附近又观察到 atlas.py 为 `7fa49a247461e5eb5f4d574efe2c8d1a3d8ca56434adcf44a93e300f54b4bd23`，说明审查期间存在父任务并行修改；这些早期磁盘观察不冒充稳定的执行快照。最终验收以记录精确加载 hash 的日志为准。

最终复跑命令为 `python3 -B tests/test_integration_review.py -v`。该次实际加载的源码 SHA-256：

| 文件 | SHA-256 |
|---|---|
| scripts/atlas.py | `bcf13a70cdff1f64dc10d2f054621d182fcd55bca04d9d128dc36d5973e9181b` |
| scripts/experiments.py | `653555bf96a36b74419cf47167ce9c9c05d89db774a4ff3bc45175848aae4219` |
| scripts/audit.py | `9ad10da5eb49186d9d7a5c0323f2af51b56d52ab1e88d0b766ddb1541e877c61` |

路径均相对于 `skills/agent-research-atlas/`。16 条测试中只有 3 条启动自编写的微小合成 Python payload，各测试独立上限 1 秒/1 次，其余为临时文件、结构、图关系或只读数值检查；它们不触碰或重跑原 cold 项目的 payload。后续源码再次变化时，应明确那是另一版本，不能把这里的 hash 验收自动扩大到未来代码。

## 边界与后续责任

待复核传播是保守的依赖提示；双向 tests 可能多提示相关记录，需要人判断哪些解释或计划受影响，不等于自动撤销研究结论。`resolve-review` 保存审查者声明，不证明审查科学上充分。

输入检查覆盖声明的文件和运行前后观察点。它不能发现两次观察之间改动后恢复的瞬时变化，也不是操作系统沙箱；mutable 必须谨慎选为确实允许迭代的输入。真实研究的 evaluator、数据、切分和预算仍需研究者正确声明。

数值审计核对的是解析后的 JSON 数字和来源版本；它不知道 accuracy 是否在代码中写死，不能证明测量有效、样本独立、统计分析合理或论点成立。Python 浮点值的原始十进制文本精度已经由 JSON 解析方式决定，Fraction 修复不声称恢复丢失的十进制信息。

本次没有审计完整 capability registry 内容的语义覆盖率；父任务仍在合并来源片段、README 和 SOURCES。注册项指向文件/符号与测试名称不等于这些能力对真实科研有效。完整发行测试、source 审计和新 cold 任务应分别保留记录，不用本定向回归代替。
