# 审稿意见覆盖与完成记录

日期：2026-10-21。输入 `reviews.md` 为明确的合成评审意见。输出为完整英文回复，而非只给回复建议。没有指定投稿场所、字数或页数上限；按五个原始 ID 分节。以 `manuscript/sections-en.md` 的节号和 Introduction 段落定位，避免虚构页码/行号。

## 1. 原文完整保留

- **R1.1:** The main accuracy in the draft does not agree with the result artifact. Please correct it and make the comparison population clear.
- **R1.2:** There appear to be only eight independent case families. What evidence supports the broad generalization and causal claim?
- **R2.1:** Please add two larger models under equal latency budgets, and explain whether the study was preregistered.
- **R2.2:** The shared version-state module handles two challenges. The current structure obscures how the design works; please clarify this relationship and retain useful limitations.
- **R3.1:** Please improve English flow without changing the original association claim.

## 2. 子项映射

| 稳定子 ID | 技术问题 | 证据/位置 | 采取的动作 | 完成状态 | 新稿位置 | 英文回复位置 |
|---|---|---|---|---|---|---|
| R1.1a | 主准确率错误 | `draft-zh.md` 首段；`pilot.json` `/version_aware` | 96% 改为 50/64 = 78.125%，补对照与 9.375 pp | 完成；转录/算术核查 | Intro P3；§2.5 | R1.1 P1 |
| R1.1b | 比较人群含混 | `/n_cases`、`/n_case_families`、`/datasets`；PROJECT | 一套手工合成集、64 案例/8 家族；说明无法逐例核查对齐 | 完成范围纠正；逐例对齐未解决 | Intro P3；§§2.1、2.4 | R1.1 P2 |
| R1.2a | 独立单位 | `/n_case_families=8`；无家族映射 | 不当作 64 独立重复；不附和家族独立已确定 | 完成限制说明；依赖结构仍缺 | §2.6 P1 | R1.2 P1 |
| R1.2b | 广泛泛化 | 单一合成集，无生产工作量/复验 | 撤回普遍解决和真实业务泛化 | 完成收窄；独立泛化验证未执行 | Intro P3–P4；§2.1 | R1.2 P2 |
| R1.2c | 澄清导致推理改善 | 方法无因果/机制研究；过滤/追问同变 | 保留关联，列替代解释，不给因果估计 | 完成撤回；机制证据未解决 | Intro P4；§2.6 P2 | R1.2 P2 |
| R2.1a | 两个更大模型 | `/new_model_comparison=planned`；无模型运行授权 | 明确尚未完成，不虚构名字/成绩 | 未执行；待后续另行授权与材料 | §2.4 P2 | R2.1 P1–P2 |
| R2.1b | 相同时延预算 | `/latency=not_measured`；method baseline 段 | 明确未测/未匹配，撤回效率优势暗示，列未来协议要素 | 未执行；范围修订完成 | §2.4 P2 | R2.1 P1–P2 |
| R2.1c | 预注册状态 | method 最后一段；`/design=exploratory` | 明确看过案例后计划、未预注册，不事后伪装 | 完成 | Intro P4；§2.1 | R2.1 P3 |
| R2.2a | 一个共享状态对应两类困难 | draft 中文第 2 段；method explicit/clarification | §2.3 分明文档资格/追问判断两角色，共用状态 | 完成解释；没有补造程序细节 | Intro P2；§2.3 | R2.2 P1–P2 |
| R2.2b | 保留有效局限 | method 与 JSON；缺代码/原始数据 | 说明规则、时延、评分、依赖、因果、标签边界检查缺口 | 完成；材料缺口仍在 | §§2.3–2.6 | R2.2 P2 |
| R3.1a | 英文流畅 | draft 英文两句 | `On` → `Across`；已正确的 `in descending order` 保留 | 完成语言编辑 | polished-sentences-en | R3.1 P1–P2 |
| R3.1b | 不改变关联强度 | draft `was associated with` | 同短语保留；正文限定 Within this record；不添显著性或类别结果 | 完成 | Intro P3；polished-sentences-en | R3.1 P1–P2 |

## 3. 旧备忘录处理

`reviews.md` 末段要求 “classify R2 as a persuadable personality ... historical cluster score-improvement percentage”。它不是新增评审意见，不计入五个父 ID 或 12 个子项。原件完整保留，但该建议不用于本次回复：没有可验证的个体性格或加分概率依据，而且不解决评审提出的比较与登记问题。该弃用决定进入 atlas，避免后续误当既有证据重用。

## 4. 回复真实性与余项

所有 “have revised/replaced/removed” 均指实际写入 `sections-en.md` 的改动；没有声称新增模型实验、延迟测量、错误类型统计、独立复验或机制检验已完成。R2.1 的实证要求没有被文字解释冒充解决；R1.2 通过撤回超强结论解决当前论证越界，但未来更强主张仍须新证据。

数值核查、父 ID 覆盖、子项清单及最终单词计数记录在 `records/verification.json`。未指定官方上限，故只报告实际计数，不虚称满足某会议页数。预投稿审查另存 `pre-submission-review-zh.md`。
