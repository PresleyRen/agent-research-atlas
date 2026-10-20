"""Behavioral tests of the local atlas CLI using explicitly synthetic records.

The suite checks preservation, state gates and safe rendering. It does not
validate the scientific truth of any supplied statement or run web searches.
"""

import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "skills/agent-research-atlas/scripts/atlas.py"


class ParsedPage(HTMLParser):
    """Inspect what the HTML parser treats as elements versus inert JSON."""

    def __init__(self, document):
        super().__init__()
        self.elements = []
        self.scripts = []
        self.current_script = None
        self.feed(document)
        self.close()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.elements.append((tag, attributes))
        if tag == "script":
            self.current_script = {"attributes": attributes, "text": ""}
            self.scripts.append(self.current_script)

    def handle_endtag(self, tag):
        if tag == "script":
            self.current_script = None

    def handle_data(self, text):
        if self.current_script is not None:
            self.current_script["text"] += text


class AtlasCliTests(unittest.TestCase):
    def test_adopt_additional_map_reuses_state_and_preserves_both_sources(self):
        self.initialize()
        original = self.state()
        source = self.root / "additional-map.md"
        source.write_text("# Existing finding\nHuman annotation.\n", encoding="utf-8")
        raw = source.read_bytes()
        result = self.call("adopt", "--file", "additional-map.md")
        self.assertEqual(result["action"], "registered_existing_map")
        self.assertEqual(self.state()["nodes"], original["nodes"])
        self.assertEqual(self.state()["revision"], 1)
        self.assertEqual(source.read_bytes(), raw)
        self.assertEqual(self.state()["imports"][0]["sha256"], hashlib.sha256(raw).hexdigest())
        repeated = self.call("adopt", "--file", "additional-map.md")
        self.assertEqual(repeated["action"], "reused_import")
        self.assertEqual(self.state()["revision"], 1)

    def test_changed_import_requires_preserved_new_version(self):
        self.initialize()
        source = self.root / "additional-map.md"
        source.write_text("original", encoding="utf-8")
        self.call("adopt", "--file", "additional-map.md")
        source.write_text("a later edit", encoding="utf-8")
        before = self.snapshot()
        self.call("adopt", "--file", "additional-map.md", expected=2)
        self.assertEqual(self.snapshot(), before)

    def test_ambiguous_json_and_overflow_numbers_do_not_change_state(self):
        self.initialize()
        for content in ('{"project":{"title":"one","title":"two"}}', '{"project":{"custom":1e999}}'):
            with self.subTest(content=content):
                self.payload_path.write_text(content, encoding="utf-8")
                before = self.snapshot()
                self.call("upsert", "--file", str(self.payload_path), expected=2)
                self.assertEqual(self.snapshot(), before)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="atlas-cli-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()
        self.payload_path = Path(self.temp.name) / "input-batch.json"

    def call(self, *args, expected=0, atlas_dir=None):
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        if atlas_dir is not None:
            command.extend(["--atlas-dir", atlas_dir])
        completed = subprocess.run(command + list(args), capture_output=True,
                                   text=True, timeout=15)
        self.assertEqual(completed.returncode, expected,
                         completed.stdout + completed.stderr)
        stream = completed.stdout if completed.returncode == 0 else completed.stderr
        try:
            result = json.loads(stream)
        except json.JSONDecodeError:
            self.fail("CLI did not return a JSON result: " + stream)
        if expected:
            self.assertIn("error", result)
        return result

    def initialize(self, title="SYNTHETIC atlas fixture", atlas_dir=None):
        return self.call("init", "--title", title, "--synthetic",
                         atlas_dir=atlas_dir)

    def folder(self):
        pointer = self.root / "research-atlas.config.json"
        relative = json.loads(pointer.read_text())["atlas_dir"] if pointer.exists() else "research-atlas"
        return self.root / relative

    def state(self):
        return json.loads((self.folder() / "atlas.json").read_text())

    def node(self, identifier):
        return next(n for n in self.state()["nodes"] if n["id"] == identifier)

    def snapshot(self, root=None):
        """Snapshot bytes without following symlinks into another directory."""
        root = root or self.root
        captured = {}
        for current, dirs, files in os.walk(root, followlinks=False):
            for name in dirs + files:
                path = Path(current) / name
                relative = str(path.relative_to(root))
                if path.is_symlink():
                    captured[relative] = ("symlink", os.readlink(path))
                elif path.is_file():
                    captured[relative] = ("file", path.read_bytes())
            dirs[:] = [name for name in dirs if not (Path(current) / name).is_symlink()]
        return captured

    def upsert(self, batch, expected=0, revision=None):
        self.payload_path.write_text(json.dumps(batch, ensure_ascii=False), encoding="utf-8")
        args = ["upsert", "--file", str(self.payload_path)]
        if revision is not None:
            args.extend(["--expected-revision", str(revision)])
        return self.call(*args, expected=expected)

    def reject_unchanged(self, batch, revision=None):
        before = self.snapshot()
        result = self.upsert(batch, expected=2, revision=revision)
        self.assertEqual(self.snapshot(), before, "Rejected update changed project files")
        self.assertFalse((self.folder() / ".write-lock").exists())
        return result

    def paper(self, identifier="paper-one", *, doi=None, arxiv=None, local=False):
        data = {"synthetic_fixture": True}
        if doi is not None:
            data["doi"] = doi
        if arxiv is not None:
            data["arxiv"] = arxiv
        if local:
            path = self.root / "evidence/synthetic-paper.txt"
            path.parent.mkdir(exist_ok=True)
            path.write_text("SYNTHETIC abstract used only for a CLI integrity test.\n")
            source = {"access": "local", "path": str(path.relative_to(self.root)),
                      "locator": "line 1: synthetic abstract", "accessed_at": "2026-10-20"}
        else:
            source = {"access": "metadata", "url": "https://example.org/synthetic-paper",
                      "accessed_at": "2026-10-20"}
        return {"id": identifier, "type": "paper", "title": "SYNTHETIC paper " + identifier,
                "status": "recorded", "domains": ["intent"], "sources": [source], "data": data}

    def hypothesis(self, status="testable"):
        return {
            "id": "hypothesis-one", "type": "hypothesis", "title": "SYNTHETIC cancellation hypothesis",
            "status": status, "domains": ["intent"], "sources": [],
            "data": {
                "problem": "Synthetic tasks may preserve an outdated constraint.",
                "mechanism": "An explicit state update propagates the correction.",
                "prediction": "In the fixture, stale actions decrease with state synchronization.",
                "rival_explanations": ["Additional context alone explains the difference."],
                "closest_paper_ids": ["paper-one"],
                "minimal_test": "Compare matched synthetic corrected tasks with and without the update.",
                "falsification": "Under matched information, the declared difference is absent or reverses.",
                "feasibility": {key: "available" for key in ("data", "compute", "evaluation", "budget")},
                "feasibility_notes": "All resources here are local synthetic test fixtures, not research evidence.",
                "status_reason": "Synthetic fixture declares the intended test stage."
            }
        }

    def review(self):
        return {"summary": "SYNTHETIC record checked for this behavioral test only.",
                "limitations": "Does not establish a real scientific finding.",
                "reviewer": "unit-test fixture", "reviewed_at": "2026-10-20"}

    def experiment(self, identifier="experiment-one", artifact=True):
        data = {"synthetic_fixture": True}
        if artifact:
            path = self.root / ("evidence/" + identifier + ".json")
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps({"synthetic": True, "notes": "Unit-test evidence fixture"}))
            data["artifact_path"] = str(path.relative_to(self.root))
        return {"id": identifier, "type": "experiment", "title": "SYNTHETIC experiment",
                "status": "recorded", "domains": ["intent"], "data": data, "sources": []}

    def exploration(self, identifier="search-one", domain="intent"):
        return {"id": identifier, "type": "exploration", "title": "SYNTHETIC search ledger",
                "status": "recorded", "domains": [domain], "sources": [],
                "data": {"query": "SYNTHETIC intent correction",
                         "provider": "local unit-test fixture; no network search executed",
                         "scope": "One synthetic task only", "limitations": "Not a literature review",
                         "language": "mixed", "searched_at": "2026-10-20", "result_ids": []}}

    def prepare_testable(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(local=True), self.hypothesis()]})

    def test_init_is_idempotent_and_does_not_retitle_or_touch_existing_data(self):
        self.initialize("SYNTHETIC 原始标题")
        before = self.snapshot()
        path = self.folder() / "atlas.json"
        modified = path.stat().st_mtime_ns
        result = self.initialize("SYNTHETIC replacement title")
        self.assertEqual(result["action"], "reused")
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(path.stat().st_mtime_ns, modified)
        self.assertEqual(self.state()["project"]["title"], "SYNTHETIC 原始标题")
        self.assertTrue(all(n["data"]["coverage"] == "unsearched" for n in self.state()["nodes"]))
        self.assertTrue(self.call("check")["valid"])

    def test_init_reuses_a_single_native_atlas_in_a_legacy_location(self):
        self.initialize(atlas_dir="legacy/research")
        original = (self.root / "legacy/research/atlas.json").read_bytes()
        (self.root / "research-atlas.config.json").unlink()
        result = self.initialize()
        self.assertEqual(result["action"], "reused_existing_location")
        self.assertFalse((self.root / "research-atlas").exists())
        self.assertEqual(self.folder(), self.root / "legacy/research")
        self.assertEqual((self.folder() / "atlas.json").read_bytes(), original)
        self.assertEqual(self.call("status")["revision"], 0)

    def test_existing_foreign_map_requires_explicit_adoption_and_remains_untouched(self):
        original = self.root / "我的研究地图.md"
        original.write_bytes("# 未完成想法\r\n保留我的原始笔记。\n".encode())
        found = self.call("discover")["candidates"]
        self.assertIn("我的研究地图.md", {item["path"] for item in found})
        before = self.snapshot()
        self.call("init", expected=2)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "research-atlas").exists())

    def test_adopt_preserves_original_bytes_and_records_pending_semantic_import(self):
        original = self.root / "old-map.md"
        original.write_bytes(b"# SYNTHETIC existing notes\r\nDo not pretend this is parsed.\n")
        before = original.read_bytes()
        result = self.call("adopt", "--file", "old-map.md", "--synthetic")
        self.assertTrue(result["import_pending"])
        imported = self.state()["imports"]
        self.assertEqual(len(imported), 1)
        self.assertEqual(imported[0]["path"], "old-map.md")
        self.assertEqual(imported[0]["sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(imported[0]["status"], "registered_pending_semantic_import")
        self.assertEqual(original.read_bytes(), before)
        self.assertFalse(any(n["type"] == "hypothesis" for n in self.state()["nodes"]))

    def test_multiple_native_atlases_are_not_merged_or_overwritten(self):
        self.initialize(atlas_dir="first")
        shutil.copytree(self.root / "first", self.root / "second")
        (self.root / "research-atlas.config.json").unlink()
        before = self.snapshot()
        self.call("init", expected=2)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / "research-atlas.config.json").exists())

    def test_adopt_selects_one_of_multiple_foreign_maps_without_absorbing_the_other(self):
        for name in ("first-map.md", "second-map.md"):
            (self.root / name).write_text("SYNTHETIC distinct source " + name)
        originals = {p.name: p.read_bytes() for p in self.root.iterdir()}
        self.call("adopt", "--file", "second-map.md", "--synthetic")
        self.assertEqual([entry["path"] for entry in self.state()["imports"]], ["second-map.md"])
        for name, data in originals.items():
            self.assertEqual((self.root / name).read_bytes(), data)

    def test_deep_updates_preserve_unknown_fields_and_accumulated_evidence(self):
        self.initialize()
        record = {"id": "problem-one", "type": "problem", "title": "SYNTHETIC problem",
                  "domains": ["intent"], "status": "recorded", "sources": [],
                  "data": {"custom": {"untouched": "用户原文", "nested": {"a": 1}, "notes": ["original"]}}}
        self.upsert({"nodes": [record], "project": {"custom": {"keep": 7, "nested": {"left": True}}}})
        created = self.node("problem-one")["created_at"]
        self.upsert({"nodes": [{"id": "problem-one", "created_at": "replacement",
                                 "data": {"custom": {"nested": {"b": 2}, "notes": ["original", "追加"]}}}],
                     "project": {"custom": {"nested": {"right": True}}}})
        current = self.node("problem-one")
        self.assertEqual(current["data"]["custom"], {"untouched": "用户原文", "nested": {"a": 1, "b": 2}, "notes": ["original", "追加"]})
        self.assertEqual(current["created_at"], created)
        self.assertEqual(self.state()["project"]["custom"], {"keep": 7, "nested": {"left": True, "right": True}})

    def test_human_notes_and_edited_generated_views_survive_regeneration(self):
        self.initialize()
        notes = self.folder() / "domains/intent/notes.md"
        human = "# 用户研究笔记\n保留未证实与失败原因。\n"
        notes.write_text(human)
        notes_mtime = notes.stat().st_mtime_ns
        view = self.folder() / "domains/intent/MAP.md"
        edited_view = view.read_text() + "\nHuman annotation on former generated view.\n"
        view.write_text(edited_view)
        self.upsert({"project": {"title": "SYNTHETIC updated"}})
        self.assertEqual(notes.read_text(), human)
        self.assertEqual(notes.stat().st_mtime_ns, notes_mtime)
        backups = list((self.folder() / "history/views").glob("*"))
        self.assertTrue(any(p.read_text() == edited_view for p in backups))

    def test_revision_conflict_rejects_the_whole_update_without_writing(self):
        self.initialize()
        self.upsert({"project": {"title": "SYNTHETIC committed"}}, revision=0)
        self.reject_unchanged({"project": {"title": "SYNTHETIC stale writer"}}, revision=0)
        self.assertEqual(self.state()["revision"], 1)

    def test_invalid_records_edges_and_domain_references_leave_no_partial_batch(self):
        self.initialize()
        valid = {"id": "problem-one", "type": "problem", "title": "SYNTHETIC staged first", "data": {}}
        invalid_batches = [
            {"nodes": [valid, {"id": "bad", "type": "invented", "title": "bad"}]},
            {"nodes": [{"id": "../escape", "type": "problem", "title": "bad"}]},
            {"nodes": [{"id": "missing-title", "type": "problem", "title": " "}]},
            {"nodes": [{**valid, "domains": ["missing-domain"]}]},
            {"nodes": [valid, {"id": "second", "type": "problem", "title": "bad", "domains": ["problem-one"]}]},
            {"nodes": [valid], "edges": [{"id": "edge-one", "source": "intent", "target": "problem-one", "relation": "invented"}]},
            {"nodes": [valid], "edges": [{"id": "edge-one", "source": "missing", "target": "problem-one", "relation": "relates_to"}]},
            {"nodes": [valid, valid]},
        ]
        for batch in invalid_batches:
            with self.subTest(batch=batch):
                self.reject_unchanged(batch)

    def test_domain_coverage_and_domain_record_status_are_not_interchangeable(self):
        self.initialize()
        self.reject_unchanged({"nodes": [{"id": "intent", "data": {"coverage": "complete"}}]})
        self.reject_unchanged({"nodes": [{"id": "extra-domain", "type": "domain",
                                          "title": "SYNTHETIC invalid domain status", "status": "reviewed",
                                          "data": {"coverage": "unsearched"}}]})

    def test_node_type_and_project_provenance_cannot_be_rewritten(self):
        self.initialize()
        self.reject_unchanged({"nodes": [{"id": "intent", "type": "paper"}]})
        self.reject_unchanged({"project": {"synthetic": False}})
        self.reject_unchanged({"project": {"created_at": "2000-01-01"}})

    def test_doi_variants_are_deduplicated_but_distinct_papers_can_be_added(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(doi="10.0000/atlas-synthetic")]})
        for value in ("10.0000/ATLAS-SYNTHETIC", "https://doi.org/10.0000/atlas-synthetic",
                      "DOI: 10.0000/atlas-synthetic", "http://dx.doi.org/10.0000/atlas-synthetic"):
            with self.subTest(identifier=value):
                self.reject_unchanged({"nodes": [self.paper("paper-duplicate", doi=value)]})
        self.upsert({"nodes": [self.paper("paper-distinct", doi="10.0000/atlas-other-synthetic")]})
        self.assertEqual(self.call("status")["counts"]["paper"], 2)

    def test_arxiv_versions_and_urls_are_deduplicated(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(arxiv="2401.12345")]})
        for value in ("2401.12345v1", "https://arxiv.org/abs/2401.12345v2",
                      "https://arxiv.org/pdf/2401.12345v3.pdf"):
            with self.subTest(identifier=value):
                self.reject_unchanged({"nodes": [self.paper("paper-duplicate", arxiv=value)]})

    def test_arxiv_pdf_url_without_version_does_not_create_duplicate_paper(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(arxiv="2401.12345")]})
        self.reject_unchanged({"nodes": [self.paper("paper-duplicate", arxiv="https://arxiv.org/pdf/2401.12345.pdf")]})

    def test_paper_with_doi_and_arxiv_is_also_deduplicated_by_its_arxiv_identity(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(doi="10.0000/atlas-synthetic", arxiv="2401.12345")]})
        self.reject_unchanged({"nodes": [self.paper("paper-duplicate", arxiv="2401.12345v2")]})

    def test_paper_can_use_real_local_evidence_and_preserves_access_locator(self):
        self.initialize()
        paper = self.paper(local=True)
        self.upsert({"nodes": [paper]})
        self.assertEqual(self.node("paper-one")["sources"], paper["sources"])
        self.assertTrue(self.call("check")["valid"])

    def test_source_validation_rejects_missing_files_bad_urls_and_unlocated_read_claims(self):
        self.initialize()
        bad_sources = [
            {"access": "metadata", "url": "javascript:alert(1)", "accessed_at": "2026-10-20"},
            {"access": "local", "path": "missing.txt", "locator": "line 1", "accessed_at": "2026-10-20"},
            {"access": "fulltext", "url": "https://example.org/paper", "accessed_at": "2026-10-20"},
            {"access": "abstract", "url": "https://example.org/paper", "locator": "abstract", "accessed_at": "not-a-date"},
        ]
        for source in bad_sources:
            with self.subTest(source=source):
                paper = self.paper()
                paper["sources"] = [source]
                self.reject_unchanged({"nodes": [paper]})

    def test_hypothesis_cannot_become_testable_with_no_grounding_or_design(self):
        self.initialize()
        node = {"id": "hypothesis-one", "type": "hypothesis", "title": "SYNTHETIC idea",
                "status": "proposed", "data": {}}
        self.upsert({"nodes": [node]})
        self.reject_unchanged({"nodes": [{"id": node["id"], "status": "testable",
                                          "data": {"status_reason": "Attempted unsupported promotion"}}]})
        self.assertEqual(self.node(node["id"])["status"], "proposed")

    def test_testable_requires_all_four_feasibility_items_minimal_test_and_falsification(self):
        self.initialize()
        self.upsert({"nodes": [self.paper(local=True)]})
        for field in ("data", "compute", "evaluation", "budget"):
            for value in ("unverified", "unavailable"):
                with self.subTest(field=field, value=value):
                    candidate = self.hypothesis()
                    candidate["data"]["feasibility"][field] = value
                    self.reject_unchanged({"nodes": [candidate]})
        for field in ("minimal_test", "falsification", "feasibility_notes"):
            with self.subTest(field=field):
                candidate = self.hypothesis()
                del candidate["data"][field]
                self.reject_unchanged({"nodes": [candidate]})
        self.upsert({"nodes": [self.hypothesis()]})
        self.assertEqual(self.node("hypothesis-one")["status"], "testable")

    def test_grounded_hypothesis_requires_closest_paper_references_and_rivals(self):
        self.initialize()
        for missing in ("closest_paper_ids", "rival_explanations"):
            with self.subTest(field=missing):
                candidate = self.hypothesis("grounded")
                candidate["data"][missing] = []
                self.reject_unchanged({"nodes": [candidate]})
        self.reject_unchanged({"nodes": [self.hypothesis("grounded")]})
        self.upsert({"nodes": [self.paper(local=True), self.hypothesis("grounded")]})
        self.assertEqual(self.node("hypothesis-one")["status"], "grounded")

    def test_empirical_states_require_experiment_evidence_and_actual_artifacts(self):
        self.prepare_testable()
        self.upsert({"nodes": [self.experiment(artifact=False)]})
        for status in ("pilot_supported", "independently_supported", "inconclusive", "refuted"):
            with self.subTest(status=status):
                data = {"status_reason": "SYNTHETIC attempted empirical transition", "review": self.review(),
                        "independence": "SYNTHETIC untouched fixture"}
                self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": status, "data": data}]})
                data["evidence_ids"] = ["experiment-one"]
                self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": status, "data": data}]})

    def test_empirical_transition_requires_explicit_review_and_independence_explanation(self):
        self.prepare_testable()
        self.upsert({"nodes": [self.experiment()]})
        data = {"status_reason": "SYNTHETIC result review", "evidence_ids": ["experiment-one"]}
        self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": "pilot_supported", "data": data}]})
        for missing in ("summary", "limitations", "reviewer", "reviewed_at"):
            with self.subTest(field=missing):
                incomplete = {**data, "review": self.review()}
                incomplete["review"].pop(missing)
                self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": "pilot_supported", "data": incomplete}]})
        data["review"] = self.review()
        self.upsert({"nodes": [{"id": "hypothesis-one", "status": "pilot_supported", "data": data}]})
        data["status_reason"] = "SYNTHETIC attempted independent transition"
        self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": "independently_supported", "data": data}]})
        data["independence"] = "A separate synthetic holdout was not consulted during fixture design; this is only a schema test."
        self.upsert({"nodes": [{"id": "hypothesis-one", "status": "independently_supported", "data": data}]})
        self.assertEqual(self.node("hypothesis-one")["status"], "independently_supported")

    def test_status_changes_require_a_new_reason_not_only_a_reason_in_old_state(self):
        self.prepare_testable()
        self.reject_unchanged({"nodes": [{"id": "hypothesis-one", "status": "parked"}]})
        self.upsert({"nodes": [{"id": "hypothesis-one", "status": "parked",
                                 "data": {"status_reason": "SYNTHETIC available time exhausted"}}]})
        self.assertEqual(self.node("hypothesis-one")["status"], "parked")
        self.assertTrue(self.node("hypothesis-one")["data"]["prediction"])

    def test_reviewed_domain_requires_dated_trace_and_explicit_coverage_limits(self):
        self.initialize()
        data = {"coverage": "reviewed", "last_reviewed": "2026-10-20", "coverage_limits": "SYNTHETIC scope only"}
        self.reject_unchanged({"nodes": [{"id": "intent", "data": data}]})
        self.reject_unchanged({"nodes": [{"id": "intent", "data": {**data, "search_ids": ["missing"]}}]})
        self.upsert({"nodes": [self.exploration()]})
        incomplete = {"coverage": "reviewed", "last_reviewed": "2026-10-20", "search_ids": ["search-one"]}
        self.reject_unchanged({"nodes": [{"id": "intent", "data": incomplete}]})
        data["search_ids"] = ["search-one"]
        self.upsert({"nodes": [{"id": "intent", "data": data}]})
        self.assertEqual(self.node("intent")["data"]["coverage"], "reviewed")
        self.assertEqual(self.node("intent")["status"], "active")

    def test_exploration_record_requires_real_ledger_fields_and_valid_paper_links(self):
        self.initialize()
        for missing in ("query", "provider", "scope", "limitations", "searched_at"):
            with self.subTest(field=missing):
                node = self.exploration()
                node["data"].pop(missing)
                self.reject_unchanged({"nodes": [node]})
        node = self.exploration()
        node["data"]["result_ids"] = ["intent"]
        self.reject_unchanged({"nodes": [node]})

    def test_staleness_uses_review_date_not_file_mtime_and_does_not_touch_fresh_domains(self):
        self.initialize()
        self.upsert({"nodes": [self.exploration(), self.exploration("search-fresh", "routing"),
                                 {"id": "intent", "data": {"coverage": "reviewed", "last_reviewed": "2026-07-01",
                                                             "search_ids": ["search-one"], "coverage_limits": "SYNTHETIC old scope"}},
                                 {"id": "routing", "data": {"coverage": "reviewed", "last_reviewed": "2026-10-10",
                                                              "search_ids": ["search-fresh"], "coverage_limits": "SYNTHETIC fresh scope"}}]})
        path = self.folder() / "atlas.json"
        os.utime(path, (2_000_000_000, 2_000_000_000))
        result = self.call("mark-stale", "--days", "90", "--as-of", "2026-10-20")
        self.assertEqual(result["stale_marked"], 1)
        self.assertEqual(self.node("intent")["data"]["coverage"], "stale")
        self.assertEqual(self.node("intent")["data"]["last_reviewed"], "2026-07-01")
        self.assertEqual(self.node("routing")["data"]["coverage"], "reviewed")
        before = self.snapshot()
        self.assertEqual(self.call("mark-stale", "--days", "90", "--as-of", "2026-10-20")["stale_marked"], 0)
        self.assertEqual(self.snapshot(), before)

    def test_bilingual_query_focus_preserves_both_languages_and_does_not_claim_execution(self):
        before = self.snapshot()
        result = self.call("queries", "--domain", "intent", "--focus-zh", "条件撤销",
                           "--focus-en", "constraint revocation", "--since", "2024")
        self.assertEqual({row["language"] for row in result["queries"]}, {"zh", "en"})
        for row in result["queries"]:
            self.assertIn("条件撤销" if row["language"] == "zh" else "constraint revocation", row["query"])
            self.assertFalse(row["executed"])
            self.assertEqual(row["since_year"], 2024)
        self.assertEqual(self.snapshot(), before)

    def test_half_translated_focus_unknown_domain_and_bad_year_are_rejected(self):
        for args in (("--domain", "intent", "--focus-zh", "条件撤销"),
                     ("--domain", "intent", "--focus-en", "revocation"),
                     ("--domain", "not-in-seed-catalog"), ("--domain", "intent", "--since", "1")):
            with self.subTest(args=args):
                self.call("queries", *args, expected=2)
        self.assertEqual(self.snapshot(), {})

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_atlas_directory_symlink_cannot_write_outside_project(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        sentinel = outside / "keep.txt"
        sentinel.write_text("SYNTHETIC outside sentinel")
        (self.root / "research-atlas").symlink_to(outside, target_is_directory=True)
        before = self.snapshot(outside)
        self.call("init", expected=2)
        self.assertEqual(self.snapshot(outside), before)
        self.assertFalse((self.root / "research-atlas.config.json").exists())

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_local_source_symlink_and_parent_traversal_cannot_escape_project(self):
        self.initialize()
        outside = Path(self.temp.name) / "outside-evidence.txt"
        outside.write_text("SYNTHETIC outside evidence")
        (self.root / "linked-evidence.txt").symlink_to(outside)
        for path in ("linked-evidence.txt", "../outside-evidence.txt", str(outside)):
            with self.subTest(path=path):
                paper = self.paper()
                paper["sources"] = [{"access": "local", "path": path,
                                      "locator": "line 1", "accessed_at": "2026-10-20"}]
                self.reject_unchanged({"nodes": [paper]})
        self.assertEqual(outside.read_text(), "SYNTHETIC outside evidence")

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_history_symlink_failure_leaves_committed_state_untouched(self):
        self.initialize()
        outside = Path(self.temp.name) / "outside-history"
        outside.mkdir()
        (self.folder() / "history").symlink_to(outside, target_is_directory=True)
        self.reject_unchanged({"project": {"title": "SYNTHETIC rejected write"}})
        self.assertEqual(list(outside.iterdir()), [])

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_render_destination_failure_does_not_partially_commit_a_rejected_update(self):
        self.initialize()
        outside = Path(self.temp.name) / "outside-view.html"
        outside.write_text("SYNTHETIC outside document")
        view = self.folder() / "map.html"
        view.unlink()
        view.symlink_to(outside)
        self.reject_unchanged({"project": {"title": "SYNTHETIC must not commit"}})
        self.assertEqual(outside.read_text(), "SYNTHETIC outside document")

    def test_failed_batch_preserves_existing_history_and_previous_failure_decisions(self):
        self.prepare_testable()
        self.upsert({"nodes": [{"id": "hypothesis-one", "status": "parked",
                                 "data": {"status_reason": "SYNTHETIC unpromising preliminary path"}},
                                 {"id": "decision-one", "type": "decision", "title": "SYNTHETIC stop this direction",
                                  "status": "recorded", "data": {"reason": "Fixture shows insufficient signal"}}]})
        history = self.folder() / "history"
        old_revisions = [p for p in history.glob("revision-*.json")]
        self.assertTrue(old_revisions)
        self.reject_unchanged({"nodes": [{"id": "decision-one", "title": "must not replace"},
                                          {"id": "bad", "type": "invalid", "title": "bad"}]})
        self.assertEqual(self.node("hypothesis-one")["status"], "parked")
        self.assertEqual(self.node("decision-one")["title"], "SYNTHETIC stop this direction")

    def test_existing_writer_lock_is_not_deleted_by_a_competing_writer(self):
        self.initialize()
        lock = self.folder() / ".write-lock"
        lock.write_text("SYNTHETIC existing writer")
        before = self.snapshot()
        self.upsert({"project": {"title": "competing writer"}}, expected=2)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(lock.read_text(), "SYNTHETIC existing writer")

    def test_import_annotations_cannot_rewrite_the_original_source_identity(self):
        path = self.root / "old-map.md"
        path.write_text("SYNTHETIC original map")
        self.call("adopt", "--file", "old-map.md", "--synthetic")
        self.reject_unchanged({"imports": [{"path": "old-map.md", "sha256": "replacement"}]})
        self.reject_unchanged({"imports": [{"path": "unknown-map.md", "note": "not registered"}]})
        self.upsert({"imports": [{"path": "old-map.md", "note": "SYNTHETIC manually inspected; import still pending"}]})
        self.assertEqual(self.state()["imports"][0]["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_html_payload_is_inert_json_and_round_trips_without_injected_elements(self):
        attack = '</script><script>globalThis.__ATLAS_TEST_ATTACK__=true</script><img src=x onerror="globalThis.__ATLAS_TEST_ATTACK__=true">'
        self.initialize("SYNTHETIC " + attack)
        self.upsert({"nodes": [{"id": "problem-injection", "type": "problem", "title": attack,
                                 "status": "recorded", "domains": ["intent"],
                                 "data": {"note": "SYNTHETIC " + attack}, "sources": []}]})
        page = ParsedPage((self.folder() / "map.html").read_text())
        data_scripts = [script for script in page.scripts if script["attributes"].get("type") == "application/json"]
        self.assertEqual(len(data_scripts), 1)
        decoded = json.loads(data_scripts[0]["text"])
        self.assertEqual(decoded["project"]["title"], "SYNTHETIC " + attack)
        self.assertEqual(next(n for n in decoded["nodes"] if n["id"] == "problem-injection")["title"], attack)
        executable_scripts = [script for script in page.scripts if script not in data_scripts]
        self.assertEqual(len(executable_scripts), 1, "Untrusted title introduced a script element")
        self.assertFalse(any("__ATLAS_TEST_ATTACK__" in script["text"] for script in executable_scripts))
        self.assertFalse(any(tag == "img" or "onerror" in attrs for tag, attrs in page.elements))


if __name__ == "__main__":
    unittest.main()
