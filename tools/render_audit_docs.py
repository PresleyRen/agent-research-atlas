#!/usr/bin/env python3
"""Regenerate source/coverage documentation from the maintained registry."""
from collections import Counter
import json
from pathlib import Path


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def refs(items):
    return "; ".join(
        "`" + x["path"] + ("::" + x["symbol"] if x.get("symbol") else "") + "`"
        + (" (" + x["kind"] + ")" if x.get("kind") else "")
        for x in items
    )


def main():
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / "skills/agent-research-atlas/assets/capability-registry.json").read_text())
    sources = registry["sources"]
    features = [f for s in sources for f in s["features"]]
    caps = registry["capabilities"]
    conflicts = registry["conflicts"]
    counts = Counter(f["status"] for f in features)
    overview = f"**{len(sources)} sources · {len(features)} features · {len(caps)} capabilities · {len(conflicts)} conflict contracts**"
    source_lines = [
        "# Sources and design attribution / 来源与设计归因", "",
        f"Audit: **{registry['audit_date']} · v{registry['version']}**. {overview}.", "",
        "## Reading scope / 阅读范围", "",
        "The audit includes **52 fully read named SKILL.md bodies**: ResearchStudio 3, ARIS 14, K-Dense 7, Orchestra 3, Anthropic 1, Research-Equality 9, Supervisor-Skills 12, Kalaris autoresearch 1, 45ck gap-finder 1, and MentorForge 1. The Anthropic nine problem-selection references and Supervisor's **70 Markdown references plus 18 Chinese handbook chapters** were read. Other sources retain the exact, narrower depth recorded below; in particular, the seven HF candidates were reviewed at selected workflow/interface scope.", "",
        "File counts describe inspected texts, not independent scientific studies. Images, upstream runtime scripts, external case-study papers and entire repositories are not implicitly included. Source review and adapted task behavior are different from an upstream end-to-end run or a scientific effectiveness benchmark.", "",
        "- [26 original-method skill review](docs/method-source-audit.md)",
        "- [39 tool/system/RE/HF entries](docs/tool-source-audit.md)",
        "- [12 Supervisor skills: files, decisions and attribution](docs/supervisor-source-audit.md)",\n        "- [4 supervision-loop additions: gap, citation, mentor and adaptive loop](docs/supervision-source-audit.md)",
        "- [Feature/complement/conflict index](docs/coverage-audit.md)",
        "- [Maintained registry](skills/agent-research-atlas/assets/capability-registry.json)",
        "- [Validation records](docs/validation.md)", "",
        "## License scope", "",
        "Atlas core code/original protocols use MIT. Three Supervisor-derived workbenches and five templates carry CC BY-NC-SA 4.0, with source attribution and substantial changes identified in [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md). Upstream SKILL bodies, the full handbook, images and drawing runtime are not bundled. Optional services keep their own terms.", "",
        "## Every source / 逐项索引", "",
        "| Source ID | Named source | Reading depth | Features |",
        "|---|---|---|---:|",
    ]
    for s in sources:
        source_lines.append(f"| `{s['id']}` | [{cell(s['name'])}]({s['url']}) | {cell(s['read_depth'])} Revision: `{cell(s['revision'])}` | {len(s['features'])} |")
    source_lines += ["", "The registry is the current maintenance authority. Dated audit manifests and task snapshots preserve what was read or executed at that time; later changes do not rewrite those historical boundaries.", ""]
    (root / "SOURCES.md").write_text("\n".join(source_lines))
    lines = ["# Coverage, complements and conflict decisions / 覆盖与互补审计", "",
             f"Audit: **{registry['audit_date']} · v{registry['version']}**. {overview}.", "",
             "## Scope and status", "",
             "每个列出的来源特色均映射到采用状态、能力、互补来源、剩余边界与补法。来源读取细节见 [SOURCES](../SOURCES.md)；Supervisor 的完整文本审查、冲突依据与改编范围见 [专门说明](supervisor-source-audit.md)；v1.2 导师闭环新增来源见 [supervision source audit](supervision-source-audit.md)。已执行的行为见 [验证总表](validation.md) 和 [Supervisor任务记录](supervisor-validation.md)。", "",
             "| Status | Features | Meaning |", "|---|---:|---|"]
    for status in ["implemented", "protocol", "optional", "reference", "deferred", "rejected"]:
        lines.append(f"| `{status}` | {counts[status]} | {cell(registry['audit_scope']['status_meanings'][status])} |")
    lines += ["", "特征数量不是测试通过数量；多个来源可以对应同一个能力。`protocol` 表示本项目提供执行流程；实际研究和语义质量需在相应项目中检查。旧的对照任务与来源审查提案保留原版本边界。", "",
              "## Capability owners and verification / 负责位置与验证", "",
              "| Capability | Implementation / protocol | Verification references | Current limit and repair |", "|---|---|---|---|"]
    for c in caps:
        lines.append(f"| {c['id']} · {cell(c['name'])} | {refs(c['implementation'])} | {refs(c['tests'])} | {cell(c['limits'])} Repair: {cell(c['remedy'])} |")
    lines += ["", "## Every distinctive feature / 逐特色索引", "",
              "Exact source locations and review-feature IDs for new workbenches are retained in the JSON registry and detailed review reports. Complement IDs are source IDs from [SOURCES](../SOURCES.md).", "",
              "| Feature ID / source strength | Adoption | Capabilities | Complements | Remaining boundary and repair |", "|---|---|---|---|---|"]
    for s in sources:
        for f in s["features"]:
            lines.append(f"| `{f['id']}` · {cell(f['label'])} | {f['status']} | {', '.join(f['capabilities'])} | {', '.join(f['complements'])} | {cell(f['gap'])} Repair: {cell(f['remedy'])} |")
    lines += ["", "## Conflict decisions / 冲突裁决", "", "| ID / tension | Retain | Do not inherit | Reason | Verification |", "|---|---|---|---|---|"]
    for c in conflicts:
        lines.append(f"| {c['id']} · {cell(c['tension'])} | {cell(c['retain'])} | {cell(c['reject'])} | {cell(c['reason'])} | {refs(c['tests'])} |")
    lines += ["", "## Extend from an observed gap", "", "Use `audit.py locate --query <symptom-or-Cxx>` to locate owners and current contracts; `audit.py --root <PROJECT> project` reports recorded project gaps. Follow [EXTENDING](EXTENDING.md): reproduce the gap, repair the owner, retain both useful and conflicting cases, run the relevant task, and update registry/docs together.", ""]
    (root / "docs/coverage-audit.md").write_text("\n".join(lines))
    print(overview)


if __name__ == "__main__":
    main()
