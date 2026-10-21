# 下轮查新清单（未执行）

日期：2026-10-20。所有下列查询均为`not_run`，本轮禁止联网。保留`searches/receipts.json`的原始429、空结果和未核验回忆，不能把它们改写成检索成功。项目为SYNTHETIC教学材料，没有任何已核验真实论文。

**比较锚点：** 同一歧义路由问题，面向缺失信息的提问选择，相同一次提问预算，与通用追问比较；区分信息价值和词面触发。将来先找最可能已经回答这个问题的真实来源。

| 目的 | 中文查询意图 | 英文查询意图 | 需查的内容 |
|---|---|---|---|
| 问题与综述 | 意图识别 路由 歧义 澄清问题 综述 | intent detection routing ambiguity clarification question survey | 旧术语、相关方法与最早工作 |
| 最近机制 | 不确定性驱动 澄清问题 任务路由 预算 | uncertainty guided clarification task routing question budget | 方法机制、何时信息可用、一次提问限制 |
| 强简单基线 | 澄清问题 通用追问 固定问题 比较 | targeted clarification generic follow-up fixed question comparison | 针对性是否超过通用追问 |
| 相邻领域 | 主动特征获取 价值信息 对话状态 选择性预测 | active feature acquisition value of information dialogue state selective prediction | 是否是旧机制换名、已知理论与失败条件 |
| 反证 | 澄清问题 无提升 消融 额外信息 预算匹配 | clarification no improvement ablation extra information matched budget | 负结果和信息/预算混杂 |
| 计量 | 意图标签 歧义 路由评测 数据泄漏 | intent label ambiguity routing evaluation label leakage | 真值定义、评测单位、跨场景检验 |

开始检索前确定真实时间范围；回溯基础工作并覆盖当时最新记录，不能将本地读取日期当成发表年份。查询应按实际provider语法重新形成`submitted_query`，记录provider/接口版本、语言、日期、分页或截断、状态、返回数、筛选理由、访问深度与原始回执。真实论文优先核对作者/正式页面/标识，再读原始方法与实验。

有限查新预算建议：先执行上述问题、机制、强基线、反证各一组中英查询，优先核对最相近的少量原始工作；达到访问上限时保留blocked，不能无限重试。数目只是工作预算，不是查全标准。服务未授权、不支持或仍限流时，保存缺口；只有获得本轮外的联网许可后才能执行。

`Budget-Revisable Dialogue Routing`是待核验的模型回忆字符串。查不到真实身份仍保留为未核验，不补造作者、年份、DOI或URL。`Uncertainty-guided clarification for routing`在当前文件明确虚构，不应尝试把该教学身份当作真实发表记录引用。

最相近工作表至少核对：研究问题、可用信息时点、提问选择机制、提问/调用预算、强基线、标签与评测单位、结果与反证、与本候选的重叠/差异。没有该表与原文定位之前，创新性仍为未决。
