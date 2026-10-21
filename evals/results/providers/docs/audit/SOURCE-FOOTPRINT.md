# 实际使用的技能/脚本来源与 SHA-256

记录日：2026-10-20。外部网页均未请求。注册表在父级发布流程中并发变更，具体开始/结束双哈希及来源说明见 `source-version-boundary.json`；不将全部源码未变写为通过。下表保留实际使用时记录的本地副本哈希。

## SKILL.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/SKILL.md`

SHA-256：`9e2fef60cf0ae464bf8ef4791bfdafca7003eab5c7a6059d9059974214384eee`

使用范围：全文读取；按 existing-project、extension、research loop 与 handoff 执行。

## local-atlas.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/local-atlas.md`

SHA-256：`bff297c626f9c1e76ac82748831354a0535f7866739fab54c04cb9f17b17b1c6`

使用范围：全文读取；增量写入、sources、status、coverage、history 与 review queue。

## bilingual-retrieval.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/bilingual-retrieval.md`

SHA-256：`8b1e37bc89f583ee2224dfc6ed38e38d13fc84ef3782115b2f06c864558566f5`

使用范围：按需读取范围、双语矩阵、来源、阅读深度、provider syntax、adapter 和 complement 路由；未打开其中外部 URL。

## extension-contract.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/extension-contract.md`

SHA-256：`5370cfadb1b27fd18d7e6c2722579e0276183abae2287d7babca5c30c9888816`

使用范围：全文读取；能力归属、扩展契约与兼容规则。

## methodology.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/methodology.md`

SHA-256：`2fff220c393e03a10f77192ef3480e8d524e7a1ba355ea0958330ce2cf449e33`

使用范围：按需读取问题锚点、综述/反证、竞争预测、可行性、设计、统计目标、独立性与交接；未读取其外链原文。

## evidence-and-claims.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/evidence-and-claims.md`

SHA-256：`5ce313f74b01be5d5da5706139348aaeefe7a1e886debaae059c8d9e35c36bce`

使用范围：按需读取来源/读取深度、证据与状态、反证、评审独立性、论点边界及更新契约。

## agent-domains.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/references/agent-domains.md`

SHA-256：`759a8ae66e9f9266a6faf5556cd3c994a21e0415951c9dbf175a49a1ee554a3a`

使用范围：按需读取跨接口问题、领域扩展、术语、示例与测量原则。

## capability-registry.json

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/assets/capability-registry.json`

SHA-256：`69146c0a704b080aebe1c595bcf4ab2cd81b2bb2e5ba642efe1dabe98e7b7bf1`

使用范围：通过 locate/selective JSON extraction 阅读相关能力、sources/features/conflicts；全注册表结构由 check 校验。

## agent-taxonomy.json

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/assets/agent-taxonomy.json`

SHA-256：`22827ff1c41ba4e0687da33120f9e2be074e894a506b0c4ddd1579addabb2724`

使用范围：由 queries 命令加载；没有将生成查询当成真实检索。

## viewer.html

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/assets/viewer.html`

SHA-256：`4c2d050457fbe42cea8496f10c95b8c8dcd2452e73d14c8e12a4138361fc8b19`

使用范围：由 atlas upsert 渲染读取；只做后续离线结构检查，不声称浏览器交互测试。

## atlas.py

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/atlas.py`

SHA-256：`bcf13a70cdff1f64dc10d2f054621d182fcd55bca04d9d128dc36d5973e9181b`

使用范围：执行 discover/status/queries/upsert/check/impact/resolve-review；人工查看 validate、update_review_queue、save 和 queries 相关代码。

## audit.py

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/scripts/audit.py`

SHA-256：`9ad10da5eb49186d9d7a5c0323f2af51b56d52ab1e88d0b766ddb1541e877c61`

使用范围：执行 locate/project/check；未完整人工审查源代码或运行全部测试。

## EXTENDING.md

路径：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/docs/EXTENDING.md`

SHA-256：`4b53fb8d787cffa750e0412f8efa1f97eb1c5856d5803eb2b67e98044536e9c9`

使用范围：全文读取，定位 symptom-to-file 与 provider 扩展验收；仅阅读。

## 注册表版本边界

文件：`/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas/assets/capability-registry.json`

开始 SHA-256：`cc6d5c391a2640f0b2435725b18578314624ca7d68c1ff58e6b6635dbf1ad00e`

结束观察 SHA-256：`69146c0a704b080aebe1c595bcf4ab2cd81b2bb2e5ba642efe1dabe98e7b7bf1`
