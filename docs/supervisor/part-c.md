# Supervisor-Skills 集成审查：写作、润色、图形与可编辑重建（Part C）

审查日期：2026-10-21。对象：HKUSTDial/Supervisor-Skills，固定提交 a20d76ef3979b804d7dbf599d577826957e0a8a9。本报告是本地文本审查与整合建议；没有运行上游脚本，没有安装绘图系统，没有生成论文或重建图像，也没有验证上游效果宣传。

## 1. 结论与范围

建议把三项写作 skill 作为拟议 **C26「证据约束的成稿与保真润色」**，把 figure-designer 与 drawio-reconstruction 作为拟议 **C28「图形设计与可编辑重建适配」**。编号由主维护者统一。本轮建议的实现性质是 host protocol / optional adapter，不能因为加了注册表就标为可执行绘图工具已经集成。

最有价值的增量是：按论文类型组织叙事；把研究逻辑工作文件与自然成稿分开；在润色前后维持数值、比较条件、否定、量词和因果强度；按图的任务选择表达方式；对图像重建逐元素建立清单并做参考图与导出图的视觉核对。Atlas 已有来源、数值、状态和依赖审查机制，可以为这些操作提供持续的证据约束，无需再建一套研究真源。

不应直接继承的内容包括：六段式、三四项贡献、固定引用密度等统一硬门槛；把任何全文或用户结果当作任意论点的充分证据；把尚未执行的预期写成 preliminary results；按弱化形容词替代补证据；一律只许矢量、通用截断纵轴、指定 Ours 必须在右上角；把成功导出当作重建完成；为了绘图强制安装全套依赖或使用指定模型。

### 版本与读取边界

上游文本根目录：[upstream-supervisor-a20d76e](sandbox:/workspace/scratch/f7a517081da8/upstream-supervisor-a20d76e)。本轮完整阅读 5 个 SKILL.md、它们在该文本快照中的全部 24 个 references、7 个指定 handbook Markdown；另完整读 drawio 的中英 README 与根 LICENSE。drawio 在本地快照没有 references 目录。根 README 只读仓库身份及 License 等相关行；未称全文读过。

Atlas 对照根目录：[agent-research-atlas](sandbox:/workspace/scratch/f7a517081da8/agent-research-atlas-public/skills/agent-research-atlas)。完整阅读 SKILL.md 与原有 7 份 references；审查期间主维护者新增 supervisor-discovery.md、supervisor-publication.md、supervisor-figures.md，随后也全文补读，合计 10 份 references。registry 为选择性结构审查：24 个 capability 的职责、依赖和边界全部读取；C05、C06、C16、C18、C19、C20、C21、C22、C23、C24 全对象读取；65 个 source 的身份索引、20 个 conflict 全对象，以及 5 个最相关 ARIS source 全对象读取。未把 registry 的所有 65 个 source 特性、其上游原文或测试执行情况都声称为本轮审查。

逐文件 SHA-256、行数、读取方式与本地 manifest 的 Git blob 核对见同目录 part-c.json；报告末尾附读取清单。上游固定版本来自任务和本地 manifest；对列入清单的文件另外按本地字节计算 blob 摘要。此检查证明字节与该 manifest 条目一致，不替代对远端提交签名或来源真实性的独立认证。Atlas 在多人协作中可能继续改变，本报告只绑定清单所列字节。

## 2. 逐 skill 特色、互补和取舍

### 2.1 intro-drafter

**特色。** 它把 Introduction 当作研究论证的压缩表达，先区分 Technique 与 New Problem/Setting，再用背景/真实例子、已有局限、目标、挑战、方法、贡献检查逻辑联系。新问题论文把问题定义置于中心；技术论文突出关键机制。running example 要来自真实材料并贯穿图、方法和案例分析；模块、挑战、贡献及正文位置要能对应。缺少例子时明确不编造。默认交付自然段落，内部思考标签不进入成稿；用户明确要求 outline 时才外显提纲。

来源：skills/intro-drafter/SKILL.md 的「Core procedure」「Outline mode」；references/paper-types.md §§2–6；flowchart.md §§1–8；running-example.md §§1–6；contribution-patterns.md §§1–6；worked-examples.md。worked-examples 对 Alpha-SQL、AFlow、LEAD 的叙述只是本次读到的上游案例说明，没有重新读取三篇原论文或检查相应图片，不能把这些案例的事实与效果当成本轮验证结果。

**与 Atlas 互补。** Atlas C09/C10/C12/C18 已管最近工作、问题机制、方法卡、结果到论点；intro-drafter 补上从这些已存在的对象到段落组织的具体步骤。贡献到章节映射与 C21 的 claim–run–figure/table 相接；真实例子到数据记录的关系继续使用 C05/C06。不要把叙事连贯性变成研究有效性状态。

**真正冲突及取舍。** 上游主文件明确要求六个自然段、每段约 100–250 词、通常 15–25 篇引用，贡献引用章节也被引用文件列为硬审查门槛。Atlas 面向多种研究贡献，适配时只保留六项逻辑问题，允许合并、拆分及改变顺序；benchmark、理论、复现、负结果、短文和非 STEM 使用对应结构。引用数量与篇幅由论证需要和真实材料决定。贡献—模块也允许多对多，不为了凑数量捏造挑战。主文件的「无具体增益则写 improves over prior baselines」不能作为无结果时的回退；没有比较证据就只写 proposed/aims to test。所有强弱比较均须有来源。

**最小产物。** 独立的 narrative-plan.md（论文类型、论证链、真实例子 ID、claim ID、章节位置、缺口），加 introduction.md 或稿件对应章节。前者是可复用研究规划摘要，不要求展示模型内部推理过程；后者只含能成立的正文与引用。按 C26 protocol 登记，固定段落/引用数量按 rejected 或 context-specific guidance 登记。

### 2.2 paper-writer

**特色。** 六阶段 Scope → Evidence → Blueprint → Draft → Review → Deliver，区分段落、章节和全文；根据研究方法区分 STEM、文本研究、实证社会科学、经济、法律及综述。非 STEM 采用 Claim–Evidence–Reasoning–Role 作为工作层结构。Evidence Map 强制记录 cannot support，给来源级别和实际位置；全文单独保存 Evidence Map 与 blueprint。独立引用核对采用新上下文、同上下文检索、无检索三档，并区分 NOT_FOUND 与 INCONCLUSIVE，避免把工具故障删除成假文献。它还明确同上下文复读无法可靠发现自己的语义编造。

来源：skills/paper-writer/SKILL.md「Hard rules」「Capability check」「Workflow」；references/evidence-discipline.md §§1–8；prose-delivery.md；verification-ladder.md §§1–7；verification-checklist.md；citation-style.md §§1–6；section-guidance.md；section-conventions.md。

**与 Atlas 互补。** Evidence Map 可以是 C05/C06/C18 证据账本的可读投影；蓝图和成稿补 C21 的组织步骤。verification-ladder 的状态与回退补 C19，但本地有完整材料时不应因离线就退化成只能引用元数据。引用存在性、元数据、引用句语义是三项检查；新上下文审查者只接收稿件、引用表和可读来源及定位，不接收作者希望的 verdict。独立引用核对不是独立复验，也不是科学结论认证。

**真正冲突及取舍。** evidence-discipline 的 L1 表格写成 full text/data 可支持 any claim、不能支持 none；这与 Atlas「实际读取的具体内容和范围」冲突。替换为来源位置、观察、推论、边界逐项配对。文件 §§6/8 与主文件把 expected/planned/uncertain 建议写成 preliminary results suggest 或 the authors report；适配时分别标为计划、已观察的初步结果、转述的来源主张，不能靠 hedge 把未执行结果写成已观察。section-guidance 的 Results 又要求 describe-then-interpret、缺数值写 substantial margin，Discussion 可提出作者未给的 plausible mechanism；这与主文件「Results 不解释 why」「不编机制」存在内部张力。取舍是尊重目标刊物章节安排，但观察和解释必须可辨；没有真实比较不能写 substantial；新解释只作为明确未测假设并回写 hypothesis，不能偷偷补进 Methods 或既有贡献。

上游检索轮数、英文默认、数字引文默认和三行交付说明均是情境默认：沿用用户语言、目标 venue 风格和已授权检索范围。正文干净不意味着项目记录可以隐藏未完成项；较长缺口清单放 sidecar，并在交付中指出。Final 无未决项才可称 ready 是可保留的边界，但「引用 suspended 即 resolved」只表示本轮处理路径明确，不能据此把包含关键缺证据内容的全文宣布 submission-ready。

**最小产物。** evidence-map.md、chapter-blueprint.md、manuscript.md/tex、citation-occurrences.json、citation-review.md、release-notes.md。已有 graph 的 ID 是关联键，不给 Evidence Map 再造一套独立科学状态。C26 是写作协议；C21 继续拥有引用与论证审计，C16 继续拥有数值抄录核对。

### 2.3 paper-polish

**特色。** 默认轻改、先理解章节作用、保留作者意思；语法与语言顺序可直接修改，可能改变科学含义的编辑必须显式标出供作者判断。因果、限定范围、论证内容不能静默增删；不补数字、公式、引用、机制。中译英先提取命题再组织自然英文，技术术语统一；文件工作用 diff 留痕，长文逐段完整处理，未读公式/图表必须标明实际范围。AI-tone 清单是提示判断，不是命中词一律删除的规则。

来源：skills/paper-polish/SKILL.md「The overriding rule」「Never fabricate content」「Conservative by default」「Rewriting Chinese drafts into English」「Working on files versus pasted text」「Content you cannot read」「How to deliver」；references/academic-phrasebank.md；ai-tone-guardrails.md；section-conventions.md。

**与 Atlas 互补。** C18 已要求措辞随证据范围校准；polish 补版本差异、语义风险项、术语一致性和分段覆盖收据。加入数值、单位、分母、方向、置信区间、条件、否定、量词及因果动词的前后核对；C16 只承担能由结构化字段核对的数值，不能替代整段语义比较。

**真正冲突及取舍。** 「忠实原意」与「不要让作者 overclaim」并非不能兼容：默认不静默改变原结论，发现越界则提出有理由的缩窄版本和前后对照，在任务已授权科学性修订时可执行并明确记录。不得把 proves 一律改 suggest 后当作证据问题已解决。上游「Restore the omitted logic」不能授权从中文隐含关系猜出因果；连接关系不明确时保留中性表达并列出疑点。上游一处建议把 parenthetical note 放原段，和 writer 的零内嵌批注要求有真实呈现冲突；集成默认成稿与作者说明分文件，用户明确要批注版时另交 annotated copy。

paper-polish 与 handbook 3.5 的「禁止中文稿用 GPT 翻译」及「严禁 AI 生成内容」相冲突。不能把两套规则都声称无缝遵守。集成采用由用户授权、作者核验、必要时按目标 venue 要求披露的写作辅助路径；不把老师给特定训练场景的禁令变成 Atlas 全局禁止，也不把自然文风处理描述成规避披露或检测。已有明确深改授权时不额外强制用户再选 light/deep。

另有应拒绝的文体伪错：3.5「英语语法问题」把一句话含两个动词或从句直接禁止，不能当作真实英语语法规则；合乎语法的复合句可以包含多个动词与从句，检查对象应是连接和依存关系。「大模型写作问题」将引号内外标点的英美风格差别一律判错，并列举 stems from、reveal 等禁用词，也不能做自动错误检测；同文件后文还推荐 reveal，说明列表不构成一致语法契约。连字符、文件名、章节时态及句长应按用途和 venue 统一，不能因关键词命中而破坏必要术语或作者原意。保留简明和准确的目标，拒绝把老师的文风偏好转化为普遍科学规则。

**最小产物。** 原稿版本、修订稿、diff、polish-review.md（处理范围、术语表、数值与语义不变量、需要作者判断的前后对照）。这提供保真审查记录，不保证学术含义已被自动形式证明。

### 2.4 figure-designer

**特色。** 把动机示例、方法总览、实验结果分别设计。动机图在失败案例、已有方案对比、性能预览中选型；总览图在流水线、系统架构、分层视角中选型；结果图根据数据关系选择图类。输出具体布局、标签、颜色、工具和可复核审查项。强调图注自包含、正文模块同名、双重视觉编码、最终插入尺寸下可读，以及结果图从数据和共享样式脚本重生成。

来源：skills/figure-designer/SKILL.md「Core procedure」「Integrity gate」；references/motivated-example.md、solution-overview.md、experimental-results.md、design-rules.md、tools.md；handbook/04_Scientific_Plotting/4.1–4.4 的相应章节。

**与 Atlas 互补。** C21 已有 claim–figure/table–run 对应，新增图形 brief 可把要传达的判断、实际数据字段、aggregation、单位、独立运行集合和图注约束写清。C12 的方法卡供方法总览使用；C18 决定图注可声称什么。示例图中的预期输出与真实输出必须分开，不能从概念示意偷换成实验成功图。设计建议本身不是已完成图像或视觉审计。

**真正冲突及取舍。** 上游一律 vector-only/禁 PNG，与 drawio 对复杂视觉优先 crop PNG 以及其自身 code screenshot 建议冲突。图的用途决定：真实数据图优先可重生成的矢量输出；照片、显微图、UI 证据、参考图局部可保留合适分辨率位图；混合媒体如实披露。不能说 PDF 容器自动保证矢量，也不能只看 PNG 判定源文件是矢量。可读字体等用最终版式实际检查，精确 pt 由源样式/排版元数据验证，目测只能报告估计。

通用「准确率 60–80 就从 50/55 起轴」不继承为硬规则。长度编码的柱图应保持有意义的共同零基线；若要比较小差异，可换点图/差值图并明确范围。点图、折线和必要的 log 图按数据含义设置，轴变化必须可见。4.3 以推理时间为 X 却要求 Ours 右上角，方向不自洽；时间越少越好时相应优势在左侧，除非明确换成吞吐率等不同量。不能为了让方法在预定象限修改单位、方向或选择性裁剪。图类清单不是全部图形；不能因为数据不适合列出的六类，就认定实验设计没有意义。

配色、8pt、150×100pt、最重要三张图、图数、作图用时、某软件优劣都作为来源经验，依据最终版式和可用工具调整。无图像访问时保留 unverified；上游输出模板只给 pass/fail，但正文要求 user-verify，适配输出应允许 pass/fail/not-checked/not-applicable，避免填假 pass。C28 protocol 适合，自动绘图与渲染仍是 optional adapter。

### 2.5 drawio-reconstruction

**特色。** 在重建任务中明确视觉保真优先、可编辑性分层。先记录每个可见元素、位置、内容、媒介、样式与状态，再为文字/结构用原生图元、简单形状用 SVG/native、复杂图像用对应 crop。箭头有独立的起止、方向、形状、层级与语义清单；文字改动要联动文本框、卡片、父容器和邻居。批处理先 manifest，限定输出集，每项独立资产；有限并发不可用时串行且保持同样验收标准。协调者必须逐项看预览和审计记录，不能相信 worker 的完成声明。已有手改文字和样式参考应保留，红框反馈当具体待修项。

来源：skills/drawio-reconstruction/SKILL.md「Fidelity Contract」「Batch Folder Workflow」「Mandatory Reference Inventory」「Medium Decision Rules」「Curves And Arrows」「Typography And Layout」「Mandatory Visual Audit」「Using A User-Approved Reference Diagram」「Redline Feedback」；README.md/README.zh-CN.md 的流程、要求、quality gates 与 License 章节。

**与 Atlas 互补。** 这是 C21/C28 的窄工具适配：让作者把既有参考图转成可继续修改的图，保留源图 hash、图中文字、图元清单、导出预览和逐项缺陷审查。图中文字/箭头含义可回连方法卡和 claim。图像看起来相同只能支持重建保真，不能证明图中方法正确或数据真实。一个含 crop 的 drawio 文件不能称所有细节均原生矢量可编辑。

**真正冲突及取舍。** 重建复刻有时会保留原图的小字体、不友好配色或非零基线；figure-designer 的重新设计建议不能悄悄覆盖用户要求的忠实重建。默认按参考图复刻并另列可读性/科学表达问题；改版只在用户任务允许时另存版本。语义等价不等于视觉等价，视觉等价也不等于数值/事实正确。结构校验、成功导出、视觉比较、语义核对分别记录。缺 renderer、未看参考图、存在 needs-fix 时可交清楚标记的草稿和剩余工作，但不能宣布完成。

**最小产物。** 单图为 source reference、figure.drawio、figure.preview.png、figure.audit.md；批处理增加 manifest.json，列每项输入/输出/状态/排他写集，保留原图与手工编辑。只在任务需要、工具已经可用并获授权时使用适配器；没有 Draw.io/Pillow 不自动安装。来源提及的图像生成 cleanup 只用于允许的背景清理，不能重画测量证据、篡改前景或调用未经授权服务。本轮未审查/执行 helper，不建议整包捆绑；同样不把 README 推荐的 Codex + GPT-5.5 xhigh 当硬依赖或已证实效果要求。

## 3. 需要登记的冲突与裁决

| 局部规则或张力 | 保留内容 | 不直接继承 / 裁决 | 建议归属 |
|---|---|---|---|
| 六段、三四贡献、固定引用密度 | 目标—挑战—方法—证据—贡献的联系 | 按研究类型与目标 venue 调整；数量不作科学门槛 | C26 / C21 |
| 自然成稿 vs 可审查研究地图 | 成稿流畅，工作证据可回查 | 工作账本独立保存；不把规划标签塞入稿件，也不删除实际缺口 | C26 / C20 |
| L1 full text 支持 any claim | 实际读取与 cannot support 字段 | 全文可读不等于任意主张成立，必须限定内容、设置与推论 | C05 / C06 / C18 |
| planned/expected → preliminary results | 对初步观察使用适当措辞 | 未执行只写计划/预测，未知比较不能写 improves/substantial | C18 / C26 |
| 结果解释与机制猜测 | 可讨论真实证据的解释 | 观察与假设分开；未知机制不写成事实或既有方法 | C18 / C21 |
| 忠实作者原意 vs 降低 overclaim | 轻改和强度校准 | 科学含义变化须明确对照；hedge 不能替代证据 | C26 / C18 |
| writer 零内嵌注释 vs polish parenthetical notes | 干净稿件和作者可知的缺口 | 默认 notes sidecar；批注稿是显式另一种交付 | C26 |
| handbook 禁 AI/翻译 vs skills 生成/中译英 | 作者负责、术语准确、证据真实 | 拒绝同时宣称遵守冲突指令；按用户请求和实际 venue 约束工作 | C26 / C21 |
| vector-only vs 重建 crop | 图形清晰、可编辑结构、视觉一致 | 数据图优先可再生矢量；照片/证据/复杂原图局部可用位图 | C28 |
| 通用截断轴、Ours 右上 | 诚实尺度和实际优劣方向 | 依据视觉编码、单位及 maximize/minimize 决定；不为宣传改轴 | C28 / C16 / C17 |
| 有图即能测字体/源格式 | 在最终版式审查可读性 | 源格式/pt 精确值需源文件元数据；未知保留 not-checked | C28 |
| XML/check/export 成功 vs 高保真完成 | 技术检查、预览生成 | 每项视觉及语义审查独立；失败/未看预览不称完成 | C28 / C22 |
| Fidelity-first vs 图形设计优化 | 准确复刻与发现问题 | 未获改版授权不重写文字或内容；改版另存 | C28 |
| 引用未核验的「已处理」vs Final ready | 明确挂起与可继续工作 | 关键 unresolved 不可因 suspended 标记而宣布投稿就绪 | C21 / C26 |
| 固定 DB 增益/数据集数量/漂亮叙事 | 强基线、真实数据、闭环证据 | 不继承 50%/10%/至少3数据集等通用门槛；保留负结果价值 | C13 / C18 / C21 |
| 文体偏好被写成语法事实 | 简洁、术语统一、符合目标格式 | 不机械禁多个动词/从句、英美引号风格或正常词语；判断实际语义和语法 | C26 |

表中是语义冲突，不是已经运行并失败的回归。现有 CF02、CF07、CF08、CF09、CF13、CF15、CF18、CF20 提供相关边界；新冲突 ID 由主维护者统一。上游大量规则本身与 Atlas 一致（不编数据、真实 running example、独立核对、未读不装懂、脚本不替代视觉检查），不应为表现批判性把互补强行写成冲突。

## 4. 具体整合流程与产物

1. **读取当前状态。** 先用现有项目地图、pending reviews、问题锚点和 claim 卡确定此次写的是计划、实际结果、修订稿还是图像重建。记录 atlas revision、输入稿件/来源/数据/图片 hash 和授权输出集；不存在的资源记为未知。
2. **建立证据投影。** evidence-map.md 引用现有 paper/experiment/claim ID，列具体 locator、source claim、observation、inference、支持范围和不能支持内容。数值逐处建 ledger；C16 只在实际运行时才可报告核对完成。没有结果的表只作为清楚标记的计划结构，不能生成看似实测的折线。
3. **选叙事路由。** 技术方法、新问题、benchmark、理论、复现、负结果等使用适配结构。narrative-plan.md 或 chapter-blueprint.md 写段落职责和证据 ID，不要求每篇六段。图和正文共享真实 example ID 和模块名称。
4. **从可支持内容成稿。** 交付稿件为自然段落和适用的学术章节；研究工作表、内部检查项、引用审计等级留在 sidecar。删除无支持句子时在工作记录留出原因及必要的知识缺口；不能因此把方法关键步骤凭空省略后声称可复现。
5. **执行保真润色。** 保存原稿与 diff。核对数值、单位、范围、统计术语、比较方向、否定/量词、因果与确定程度。纯语言修改直接做；科学判断的修改依授权执行并逐项显式说明。长文维护处理范围，未读图/公式单列。
6. **为图选择路径。** 实验结果由真实数据和可重生成脚本出图；方法/动机图由已核验的方法卡与例子出 brief；参考图重建走可选 drawio adapter。只启用当前任务所需的工具，工具缺失不会触发整套系统安装。
7. **分层审查。** 数值抄录、引用存在/元数据、句子支持、图元/箭头语义、渲染可读性/视觉保真分别留记录。引用核对可用独立上下文，资源不足则如实标自审/离线材料核对；任何一层通过不能替代其他层。
8. **更新图谱依赖。** 继续用 claim 节点承载稿件主张，experiment/paper 是其证据，figure/manuscript 路径放关联说明或 data 文件字段，不擅自新增 node type/schema。需要依赖传播的稿件/图审查，可用现有 decision/exploration 记录挂 data.depends_on 并链接 sidecar。新产物与历史记录都保留；发现上游材料更正先 upsert 真实变化，再审受影响句子/图注，最后按 revision resolve-review。
9. **交接。** 交 manuscript/figures 及短交付说明，另列工作记录位置、完成范围、尚未核验项、下次最有价值的工作。没有实际运行或看图时只能交计划/设计，不称论文就绪、图完成或科学论点已证实。

建议最小文件包：manuscript.md（或 tex）、evidence-map.md、chapter-blueprint.md、claim-occurrences.json、citation-review.md、polish-review.md、figures/brief.md、figures/data-manifest.json、需要时的原生可编辑图和 preview/audit、release-notes.md。小任务只留下真正有用的几项；这些名称是建议的项目产物，不是现有 CLI 新增的强制 schema。

### 拟议 capability 的注册方式

| 建议项 | 工作归属与依赖 | 应登记的实现状态 | 未完成与修复入口 |
|---|---|---|---|
| C26 证据约束写作与保真润色 | 依赖 C05/C06/C18/C21；C20/C24 为版本与交接 | protocol；写作结构/词表 optional；数量硬门槛 rejected | 尚无通用语义不变量检测器；先增加宿主协议和反例任务，不能称自动保证保真 |
| C28 图形设计与可编辑重建 | 依赖 C12/C16/C18/C21/C22；用 C20 保持审查版本 | design protocol；Draw.io/绘图库 optional adapter | 尚无 renderer/helper 实连；以后审查具体版本、授权试跑，比较源图与预览 |

不要让 C21 反向依赖 C26/C28 导致注册表依赖闭环；C21 仍是公共论证/引用审计所有者，新能力调用它。source feature 的 complements 可以双向表达互补，但 capability depends_on 要保持清楚的职责顺序。C26/C28 的完成不是给 C18 自动升级 supported 的条件。

### 新增 workbench 的只读复核

审查末尾全文读到的新 supervisor-publication.md 已纳入本轮主要裁决：段落/引用密度灵活、计划不写 preliminary results、来源访问不等于任意支持、无实测比较不写成功、中译英不添加因果、稿件与注释分开。supervisor-figures.md 已区分轴编码、允许混合媒体、要求原生对象、导出预览并说明无 renderer 的边界，也要求改变拓扑/含义的修订另存。supervisor-discovery.md 将工作产品路由到既有 Atlas 所有者，没有要求段落润色重新做文献综述。

建议图形 workbench 进一步把逐元素 unresolved/needs-fix 与“未完成”直接关联，并保留复杂箭头的几何/起止/方向清单；当前文字有检查要求，但这些可操作的验收细节比“视觉核对”总称更便于续接。注册表仍需如实区分 protocol 与 optional/not_run；新增文件不等于 renderer/helper 已实连。本轮未修改这些文件，全文及哈希已列入账本。

## 5. 可直接采用的原创整合段落（草案）

以下为基于所列来源重新组织的适配文字，不是复制上游条款。拟放入独立注明来源和更改内容的 CC BY-NC-SA 4.0 方法文档；并不对整个现有代码仓库重新许可。

### 草案 A：从研究记录到成稿

先确定本次稿件要表达的具体判断，再从项目已有的论文、实验和论点记录中选择证据。工作蓝图写清每节的任务、使用的证据 ID 和尚未解决的缺口；它与交给读者的稿件分开保存。技术引言可检查背景、局限、问题、挑战、方法与贡献之间是否连贯，但不要求固定段落数量。新问题、理论、测量、复现和负结果按各自论证目标组织。真实例子、方法模块和贡献应能回到相同的项目对象；缺少材料时保留缺口，不用流畅的文字补造结果。正文使用自然的学术表达，证据表、审查状态和规划说明放在独立工作文件中，供后续更新与核查。

### 草案 B：润色保持科学含义

润色前保存原稿版本，并明确此次是语言整理还是包含论证修订。修改后的数值、单位、比较方向、实验范围、否定与量词、因果关系及确定程度应与被授权的原意一致。语法与句序可以直接调整；可能改变科学结论的编辑列出原句、建议句、依据及影响。若原稿超过证据所能支持的范围，指出缺口并给出有依据的缩窄方案，不以 suggest 等弱词掩盖没有观察。翻译应保持技术术语和命题关系，原文没有建立的因果联系不得通过连接词加入。清洁稿件与作者说明分别交付，长文记录实际处理范围，未读图表和公式保持待核验。

### 草案 C：图形表达与证据

先说明图要回答的问题、所支持的论点和输入来源，再选择布局与视觉编码。结果图从真实记录及可检查的聚合过程生成，保留单位、样本/运行集合、误差定义和数据版本；概念示意、计划输出与测量结果明确区分。图中模块名称和箭头含义与方法记录一致，图注的强度不能超过证据。根据最终排版检查文字可读性、色觉友好和非颜色编码，按轴含义决定范围与方向。优先交付可再生成的源文件；需要照片、UI 或复杂原图局部时可保留位图，并说明编辑范围。未检查的项目保持未检查，不用格式或导出成功替代数值与语义核对。

### 草案 D：可选参考图重建

当任务要求把参考图转成可编辑文件时，先保存输入版本并逐项列出文字、容器、图像、箭头及其位置和样式。文字与结构尽量使用原生图元，简单形状可用矢量，复杂视觉可以保留对应局部图像；说明哪些部分仍为嵌入图片。按任务限定的输出集工作，保留原图、手工修改和版本。完成检查包含结构有效、能够渲染、参考图与导出图逐项一致、文字及连接含义未变四个层面。存在缺项、未看的预览或待修缺陷时交付明确标记的草稿与审计记录，不宣布重建完成。需要改进原图的可读性或内容时另存改版，工具缺失时记录回退，不为这一适配器捆绑安装整个绘图系统。

## 6. 许可、来源与分发边界

| 已读位置 | 文本实际声明 | 本次处置 |
|---|---|---|
| 根 LICENSE；README「License」 | CC BY-NC-SA 4.0，Yuyu Luo (methodology) and contributors | 方法改编单独注明来源、固定提交、变更与许可；不声称主代码全受新许可覆盖 |
| intro-drafter / paper-writer / paper-polish 的 YAML | CC-BY-NC-SA-4.0 | 与上述方法改编范围一致 |
| figure-designer/SKILL.md YAML | CC-BY-4.0 | 与根声明不同，登记冲突，不凭推测抹平；本适配同时使用 NC-SA handbook，拟独立 NC-SA 标注且保留原声明 |
| drawio-reconstruction 的中英 README「License」 | 该 skill repository 为 MIT，链接本子目录 LICENSE | 保留子目录许可边界；本地文本快照无该 LICENSE 原文，搬运代码前另核验和保留对应许可/notice |

drawio 的 MIT 声明不扩展为 Supervisor-Skills 全包 MIT，也不扩展到 README 引用的论文、数据集、图像或其他第三方素材。本轮没有搬运代码或图像。拟议改编文档应注明：方法来源 HKUSTDial/Supervisor-Skills @ a20d76e；修改包括去除固定数量门槛、增加证据范围与计划/观察区分、加入保真编辑和图形分层检查、接入 Atlas ID 与版本依赖。保留作者归属，不暗示原作者背书。这里记录源文件声明与集成安排，不替代对未提供许可文本的核验。

## 7. 未读、未运行与建议验证

没有读取任何图片、PDF、drawio XML 或外部论文正文。没有打开 VCG-Bench 主页、论文、数据集或代码；README 里的重建效果和模型比较只是上游自述。指定 handbook 链接的 3.3、3.4 及 06_Case_Studies 也未全文读取，尽管 intro references 引用了案例描述。它们不在本轮指定全文范围内。

未读图像包括根 assets 中 intro_flowchart_board.png、dense_body_layout_example.png、aflow_existing_vs_ours.png、performance_teaser_example.png、aflow_solution_overview.png、alpha_sql_solution_overview.png、lead_solution_overview.png、experiment_canvas_bad.png、experiment_canvas_good.png；drawio 的 6 张 assets/cases 对比图、3 张 examples 原始 PNG 和 3 个示例 drawio。具体存在性及引用位置在 JSON 中列出。本地没有这些文件时记 not present in reviewed text snapshot，不据此断言正式上游仓库缺失。

未审查或执行 drawio 的 batch_manifest.py、batch_verify.py、check_drawio.py、export_drawio.py、crop_assist.py；未安装 requirements.txt 的 Pillow 或 Draw.io；未运行共享文档提及的 scripts/check_shared_sync.py；未调用图像生成服务。本轮只执行自己编写的本地文本清点、摘要计算和 JSON 结构读取，不能把它们报成上游验证。

建议未来用以下小任务验证协议，当前全部为 not_run：

- 给出未执行计划与 hardcoded accuracy fixture，要求写 Results：应保持计划/流程观察边界，不生成方法有效或 preliminary results 的暗示。
- 给出真实负结果、一个短理论稿和一个 benchmark 稿：检查不强制六段、三项贡献、固定引用数或漂亮正结果。
- 给原句“在数据集 A 上相关性为 0.20，可能与 X 有关”请求润色/翻译：数值、范围、关联性不变；有意义修改显式标出。
- 给三条引用且一条检索超时：不能标 NOT_FOUND；有本地全文时检查离线句子支持，不能只核 DOI。
- 给包含复杂图片和小字体的参考图：忠实重建与改版分开，报告 crop 的编辑范围；XML 成功但漏箭头/错文字必须未完成。
- 给时间—准确率散点和 60–80% 的柱图：按照单位和编码设置方向/基线，不为让 Ours 优势更醒目而扭曲。
- 改一个图注所依赖的实验记录：pending review 必须定位到已登记的引用消费者；一次 resolve 不清除其他未审稿件，历史记录保留。

这些测试需在单独的、确实运行过的记录中给出输入版本、实际输出、检查依据和未测边界。先保留现有 CLI 结构回归，再验证宿主行为；结构测试、写作可用性、视觉保真和科学有效性是不同结论。

## 8. 产物检查与并发版本边界

本报告的 JSON 已通过标准库解析和本地一致性断言：5 个 skill、27 条 feature、16 项冲突、52 条读取账本、21 个未读图像/XML 资产、6 个未执行 helper；7 个建议任务全部保持 not_run。已列上游文件的 Git blob 摘要均与本地 pinned manifest 一致。这里的检查只是本报告的结构与字节核对。

最终保存时观察到主维护者继续修改 Atlas 的 SKILL.md 以及三份 supervisor workbench。JSON 的 concurrent_input_changes_after_hash_capture 同时保存本次读到的 hash 与保存时 current hash；下表仍保留本次实际读取版本，没有把后来修改默认为已复核。上游 pinned 源文本和原有 7 份 Atlas references 在此次最终检查中未发生漂移。报告对新 workbench 的具体建议应结合这些版本边界理解。

## 附录：已读文件与字节版本

下表由本轮实际读取清单生成。full_text 表示文本全文读过，未包含文件链接出去的图片、论文、代码或其他文档；selective 表示明确的选择性读取。详尽字段见 part-c.json。

| 根目录 | 文件 | 读取范围 | 行数 | SHA-256 前 16 位 |
|---|---|---|---:|---|
| upstream | skills/intro-drafter/SKILL.md | 全文 | 211 | 675e8a97a58a841b |
| upstream | skills/intro-drafter/references/contribution-patterns.md | 全文 | 116 | 6ba9363a364fca46 |
| upstream | skills/intro-drafter/references/evidence-discipline.md | 全文 | 152 | 63c20c6b783b12b3 |
| upstream | skills/intro-drafter/references/flowchart.md | 全文 | 204 | 46aebd7605bcea34 |
| upstream | skills/intro-drafter/references/paper-types.md | 全文 | 155 | 21f1267c85df2b2f |
| upstream | skills/intro-drafter/references/prose-delivery.md | 全文 | 62 | 1a7e60145d6b55e0 |
| upstream | skills/intro-drafter/references/running-example.md | 全文 | 133 | 14f08a1da8f3e70e |
| upstream | skills/intro-drafter/references/worked-examples.md | 全文 | 168 | ddc22cddd503395f |
| upstream | skills/paper-writer/SKILL.md | 全文 | 284 | 5ac3df38ca0f6a4a |
| upstream | skills/paper-writer/references/academic-phrasebank.md | 全文 | 98 | 56091882b95163fe |
| upstream | skills/paper-writer/references/ai-tone-guardrails.md | 全文 | 85 | 2fd3f8960f0ffe34 |
| upstream | skills/paper-writer/references/citation-style.md | 全文 | 146 | 17a69ba23fbd7e93 |
| upstream | skills/paper-writer/references/evidence-discipline.md | 全文 | 152 | 37dfcc3452f1d768 |
| upstream | skills/paper-writer/references/prose-delivery.md | 全文 | 62 | 26ae7bbedea943d7 |
| upstream | skills/paper-writer/references/section-conventions.md | 全文 | 124 | 810700351410427d |
| upstream | skills/paper-writer/references/section-guidance.md | 全文 | 115 | 0a81a147c167a7a5 |
| upstream | skills/paper-writer/references/verification-checklist.md | 全文 | 121 | 474d8772cadd9299 |
| upstream | skills/paper-writer/references/verification-ladder.md | 全文 | 132 | 3702c85b12da5db8 |
| upstream | skills/paper-polish/SKILL.md | 全文 | 267 | fde7964acfea805a |
| upstream | skills/paper-polish/references/academic-phrasebank.md | 全文 | 98 | 4f199bd39c181045 |
| upstream | skills/paper-polish/references/ai-tone-guardrails.md | 全文 | 85 | 11f8570c540c7502 |
| upstream | skills/paper-polish/references/section-conventions.md | 全文 | 124 | 83348fb3658aee2a |
| upstream | skills/figure-designer/SKILL.md | 全文 | 207 | c9ba67c1c21972ac |
| upstream | skills/figure-designer/references/design-rules.md | 全文 | 99 | 088949487c3582e8 |
| upstream | skills/figure-designer/references/experimental-results.md | 全文 | 127 | 537445abb435703b |
| upstream | skills/figure-designer/references/motivated-example.md | 全文 | 138 | b05a774d84604db5 |
| upstream | skills/figure-designer/references/solution-overview.md | 全文 | 145 | 1770b0919bb7622f |
| upstream | skills/figure-designer/references/tools.md | 全文 | 124 | 96a96208550c033c |
| upstream | skills/drawio-reconstruction/SKILL.md | 全文 | 351 | ccc4e5fa5ccd4d7f |
| upstream | handbook/03_Paper_Writing/3.1_完成一篇科研论文你需要做几件事情.md | 全文 | 61 | 01d4fc98056538d1 |
| upstream | handbook/03_Paper_Writing/3.2_Introduction写作的思考模型.md | 全文 | 37 | ccf475b52b5ba1a8 |
| upstream | handbook/03_Paper_Writing/3.5_写作细节与Checklist.md | 全文 | 627 | edf65fb411494ab7 |
| upstream | handbook/04_Scientific_Plotting/4.1_Motivated_Example_Figure.md | 全文 | 62 | d53ee81cd90e520f |
| upstream | handbook/04_Scientific_Plotting/4.2_Solution_Overview_Figure.md | 全文 | 49 | da060d28a036e55b |
| upstream | handbook/04_Scientific_Plotting/4.3_Experimental_Results_Figure.md | 全文 | 56 | b0c7bd5247a2fed4 |
| upstream | handbook/04_Scientific_Plotting/4.4_绘图Checklist与工具速查表.md | 全文 | 29 | 3eecbfbf39120da4 |
| upstream | LICENSE | 全文 | 24 | b35c958b79726c11 |
| upstream | skills/drawio-reconstruction/README.md | 全文 | 212 | 370f90a35b2f973e |
| upstream | skills/drawio-reconstruction/README.zh-CN.md | 全文 | 213 | 25b1999581518292 |
| upstream | README.md | 选择性，详见 JSON | 226 | 3cf3791b0c13c684 |
| atlas | SKILL.md | 全文 | 120 | 9e2fef60cf0ae464 |
| atlas | references/agent-domains.md | 全文 | 190 | 759a8ae66e9f9266 |
| atlas | references/bilingual-retrieval.md | 全文 | 229 | 8b1e37bc89f583ee |
| atlas | references/evidence-and-claims.md | 全文 | 258 | 5ce313f74b01be5d |
| atlas | references/experiments.md | 全文 | 179 | 9c23a9e35fcb64c4 |
| atlas | references/extension-contract.md | 全文 | 37 | 5370cfadb1b27fd1 |
| atlas | references/local-atlas.md | 全文 | 138 | bff297c626f9c1e7 |
| atlas | references/methodology.md | 全文 | 284 | 2fff220c393e03a1 |
| atlas | references/supervisor-discovery.md | 全文 | 112 | 8ceaad966d6cfe47 |
| atlas | references/supervisor-figures.md | 全文 | 42 | 1bcfad7aa0b94a87 |
| atlas | references/supervisor-publication.md | 全文 | 112 | 01be53d8cf9c54b8 |
| atlas | assets/capability-registry.json | 选择性，详见 JSON | 5984 | 3408b0e92d210afc |
