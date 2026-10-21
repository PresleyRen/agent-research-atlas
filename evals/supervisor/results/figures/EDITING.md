# 图稿编辑与复现

## 编辑入口

| 产物 | 可编辑对象 | 位图部分 / 注意事项 |
|---|---|---|
| `outputs/fig01_architecture.drawio` | 六个独立圆角模块及文字、六条原生有向连接、两条说明文字；分为 Connectors、Modules、Labels、Source detail 四层 | 仅 source detail 为 101 × 101 px 原图裁剪，可移动/缩放/替换，但其内部格子没有转换成测量数据或独立矢量对象 |
| `sources/architecture_scene.json` | 所有模块坐标/尺寸/文字、连线端点/折点、额外文字、裁剪位置 | 这是程序化重建的共同输入；直接改 drawio 后再运行生成脚本会覆盖 drawio，先另存人工编辑版 |
| `outputs/fig01_architecture.svg` | 原生 `<rect>`、`<text>`、带箭头标记的 `<path>` 与分组 | 与 drawio 来自同一 JSON，不是 drawio 原生导出；SVG 路径在一般矢量编辑器中不会自动保持模块吸附 |
| `outputs/fig02_latency_accuracy.svg` | 点形、文字、坐标轴、网格等矢量元素；可在 Inkscape 中继续编辑 | 不含栅格图；修改数值应更改来源数据副本并重新绘图，而非拖动点造成数据与标签不一致 |
| `scripts/plot_latency_accuracy.py` | 字号、配色、点形、标注偏移、尺寸、坐标范围和数据读取 | 当前校验只接受三行输入；新增方法时需重新安排标签并查看实际预览 |
| `outputs/*.pdf` | 用于排版的矢量导出 | 建议保留 SVG/Python/drawio 作为主要编辑源，PDF 用于论文插图 |

## drawio 对象与连线

在已有本地 draw.io / diagrams.net 桌面环境中打开 `outputs/fig01_architecture.drawio`，双击模块或说明文字可改文案；选择模块可调整尺寸位置；选择箭头可调整连接点和折点。文件内每条边通过 source/target 绑定模块，细节见下表。**本轮未在 draw.io 原生应用中验证以上交互，首次打开请按下表逐条复核。** 不需要访问线上编辑站点。

| 对象 ID | 显示内容 / 语义 |
|---|---|
| user_request、version_state、router | 主输入链路 |
| retriever、answer、clarify | 检索、输出、澄清模块 |
| e_request_state | User request → Version state |
| e_state_router | Version state → Router |
| e_router_retriever | Router → Retriever |
| e_retriever_answer | Retriever → Answer |
| e_router_clarify | Router → Clarify；保留 Router 左侧折线 |
| e_clarify_request | Clarify → User request；箭头向上进入用户请求 |
| feedback_label、source_detail_label | 两条独立可编辑说明文字 |
| source_detail_image | 独立位图小块，不是整页底图 |

## 完整本地复现命令

下列命令均在本项目内读写；需要本轮已验证存在的 Python、Pillow、Matplotlib、Inkscape 和 PyMuPDF。没有自动安装或联网逻辑。

```bash
python /workspace/scratch/f7a517081da8/supervisor-forward/figures/scripts/rebuild_architecture.py
python /workspace/scratch/f7a517081da8/supervisor-forward/figures/scripts/plot_latency_accuracy.py
python /workspace/scratch/f7a517081da8/supervisor-forward/figures/scripts/render_previews.py
python /workspace/scratch/f7a517081da8/supervisor-forward/figures/scripts/verify_artifacts.py
```

生成脚本把 Matplotlib、Inkscape/XDG 缓存定位到本项目 `.cache`。渲染日志保存在 `checks/render_log.json`；输出哈希保存在 `checks/output_manifest.json`；原始输入逐项完整性校验保存在 `checks/artifact_verification.json`。

`rebuild_architecture.py` 首次运行会建立 JSON 场景，后续读取现有 JSON；它检查 reference.png 的既有哈希，防止未经重新查看就重建变化后的参考图。脚本不会写入 `reference.png` 或原始 CSV。

## 修改后的必要复核

架构改动后检查所有六条箭头方向、模块名称、文字遮挡、折线是否误穿模块、裁剪是否仍对应原图。drawio 原生导出与伴随 SVG 应分别检查；不能用 XML 解析成功或 SVG 美观来替代原生应用验证。

数据改动后核对 CSV 的单位与分母，重新检查坐标范围和图注；若新增真实重复数据，应先明确实验单位、测量口径和不确定性方法，再增加误差条。更新 `CAPTIONS.md`、数据账本与研究地图中的依赖解释。未给定具体期刊，单栏 90 mm / 宽栏 180 mm 为当前版式选择，投稿前按已确定的期刊规范调整。
