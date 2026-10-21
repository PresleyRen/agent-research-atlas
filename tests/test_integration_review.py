"""Independent integration review of the revised local record tools.

These are transparent code-review regressions using synthetic temporary files.
They are not blind forward trials, real-data experiments, or scientific evidence.
"""

import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "skills/agent-research-atlas/scripts"
LOADED_SOURCE_SHA256 = {}


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    source = path.read_bytes()
    LOADED_SOURCE_SHA256[path.name] = hashlib.sha256(source).hexdigest()
    exec(compile(source, str(path), "exec"), module.__dict__)
    return module


ATLAS = load_module("atlas_integration_review", SCRIPTS / "atlas.py")
EXPERIMENTS = load_module("experiments_integration_review", SCRIPTS / "experiments.py")
with mock.patch.dict(sys.modules, {"atlas": ATLAS, "experiments": EXPERIMENTS}):
    AUDIT = load_module("audit_integration_review", SCRIPTS / "audit.py")


class IntegrationReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="atlas-integration-review-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.atlas = ATLAS.Atlas(self.root)

    def initialize(self):
        self.atlas.init("SYNTHETIC integration review", synthetic=True)

    def paper(self, identifier):
        path = self.root / (identifier + ".txt")
        path.write_text("SYNTHETIC source for software testing only.\n", encoding="utf-8")
        return {
            "id": identifier, "type": "paper", "title": "SYNTHETIC " + identifier,
            "status": "read", "domains": ["routing"], "data": {},
            "sources": [{"path": path.name, "access": "local",
                         "accessed_at": "2026-10-20", "locator": "entire synthetic fixture"}],
        }

    def establish(self):
        self.initialize()
        self.atlas.upsert({"nodes": [self.paper("paper-a"), self.paper("paper-b"), {
            "id": "claim-a", "type": "claim", "title": "SYNTHETIC descriptive claim",
            "status": "supported", "domains": ["routing"],
            "data": {"evidence_ids": ["paper-a"], "reasoning": "Software fixture only.",
                     "limitations": "No empirical or scientific meaning."},
        }, {
            "id": "followup-a", "type": "experiment", "title": "SYNTHETIC planned follow-up",
            "status": "planned", "domains": ["routing"], "data": {"depends_on": ["claim-a"]},
        }], "edges": [{"id": "extra-support", "source": "paper-b", "target": "claim-a",
                       "relation": "supports"}]}, expected=0)

    def pending(self):
        return {entry["node_id"] for entry in self.atlas.load().get("maintenance", {}).get("pending_reviews", [])}

    def test_removed_support_relation_flags_previous_consumer_and_followup(self):
        self.establish()
        # Updating an existing edge is currently accepted by upsert. The former
        # consumer must not silently keep its old interpretation after removal.
        self.atlas.upsert({"edges": [{"id": "extra-support", "relation": "relates_to"}]}, expected=1)
        self.assertEqual(self.pending(), {"claim-a", "followup-a"})

    def test_planned_tests_edge_propagates_changed_hypothesis_to_plan(self):
        self.initialize()
        self.atlas.upsert({"nodes": [{
            "id": "hyp-a", "type": "hypothesis", "title": "SYNTHETIC proposed hypothesis",
            "status": "proposed", "data": {"prediction": "original prediction"},
        }, {
            "id": "planned-test", "type": "experiment", "title": "SYNTHETIC planned test",
            "status": "planned", "data": {},
        }], "edges": [{"id": "test-link", "source": "planned-test", "target": "hyp-a",
                       "relation": "tests"}]}, expected=0)
        self.atlas.upsert({"nodes": [{"id": "hyp-a", "data": {"prediction": "changed prediction"}}]}, expected=1)
        self.assertIn("planned-test", self.pending())

    def test_reverse_uses_dependency_and_review_reopening(self):
        self.establish()
        self.atlas.upsert({"nodes": [{"id": "rule-a", "type": "decision",
                                    "title": "SYNTHETIC dependent rule", "data": {}}],
                           "edges": [{"id": "rule-uses", "source": "rule-a",
                                      "target": "followup-a", "relation": "uses"}]}, expected=1)
        self.atlas.upsert({"nodes": [{"id": "paper-a", "data": {"observation": "first correction"}}]}, expected=2)
        self.assertEqual(self.pending(), {"claim-a", "followup-a", "rule-a"})
        for identifier in ("claim-a", "followup-a", "rule-a"):
            self.atlas.resolve_review(identifier, "synthetic-code-reviewer", "Reviewed fixture relationship only.", self.atlas.load()["revision"])
        self.assertEqual(self.pending(), set())
        self.atlas.upsert({"nodes": [{"id": "paper-a", "data": {"observation": "second correction"}}]}, expected=self.atlas.load()["revision"])
        self.assertEqual(self.pending(), {"claim-a", "followup-a", "rule-a"})
        state = self.atlas.load()
        self.assertEqual(len(state["maintenance"]["review_log"]), 3)
        self.assertEqual(next(n for n in state["nodes"] if n["id"] == "claim-a")["status"], "supported")

    def test_boolean_atlas_schema_version_is_rejected(self):
        self.initialize()
        malformed = self.atlas.load()
        malformed["schema_version"] = True
        with self.assertRaises(ATLAS.AtlasError):
            ATLAS.validate(malformed, self.root)

    def test_malformed_review_trigger_rejected_before_any_commit(self):
        self.establish()
        malformed = self.atlas.load()
        malformed["maintenance"] = {"pending_reviews": [{"node_id": "claim-a", "triggers": [{}],
                                                         "first_flagged_revision": 1,
                                                         "last_flagged_revision": 1}], "review_log": []}
        with self.assertRaises(ATLAS.AtlasError):
            ATLAS.validate(malformed, self.root)

    def test_pending_review_visible_in_domain_view(self):
        self.establish()
        self.atlas.upsert({"nodes": [{"id": "paper-a", "data": {"observation": "corrected"}}]}, expected=1)
        view = (self.root / "research-atlas/domains/routing/MAP.md").read_text(encoding="utf-8")
        self.assertTrue("Pending evidence reviews" in view or "Needs review" in view or "待复核" in view,
                        "A domain-only reader sees historical supported status without its pending-review warning")

    def prepare_experiment(self, payload, *, mutable=False):
        candidate = self.root / "candidate.py"
        candidate.write_text(payload, encoding="utf-8")
        (self.root / "evaluator.json").write_text('{"threshold": 0.8}\n', encoding="utf-8")
        plan = json.loads((REPO / "skills/agent-research-atlas/assets/experiment-plan.example.json").read_text())
        plan["experiment_id"] = "integration-fixture"
        plan["command"] = {"argv": [sys.executable, "-I", "-B", "candidate.py"], "cwd": ".",
                           "input_files": ["candidate.py", "evaluator.json"]}
        if mutable:
            plan["command"]["mutable_input_files"] = ["candidate.py"]
        plan["budget"] = {"max_runs": 1, "max_run_seconds": 1, "max_total_seconds": 1}
        plan["seeds"] = [7]
        source = self.root / "input-plan.json"
        source.write_text(json.dumps(plan), encoding="utf-8")
        project = EXPERIMENTS.Project(self.root)
        EXPERIMENTS.save_plan(project, str(source))
        EXPERIMENTS.freeze_plan(project, "integration-fixture", "exploratory", "SYNTHETIC integration code review fixture.")
        return project

    def test_mutable_candidate_may_change_during_run_and_both_hashes_remain(self):
        project = self.prepare_experiment('from pathlib import Path\np=Path(__file__)\np.write_text(p.read_text()+"\\n# changed synthetic candidate\\n")\nprint("SYNTHETIC success")\n', mutable=True)
        record = EXPERIMENTS.run_local(project, "integration-fixture", "once", authorized=True, seed=7)
        self.assertEqual((record["status"], record["exit_code"]), ("succeeded", 0))
        provenance = record["provenance"]
        self.assertNotEqual(provenance["declared_inputs"]["candidate.py"], provenance["declared_inputs_after"]["candidate.py"])
        self.assertEqual(provenance["declared_inputs"]["evaluator.json"], provenance["declared_inputs_after"]["evaluator.json"])
        self.assertEqual(provenance["immutable_inputs_changed_during_run"], [])
        self.assertEqual(record["scientific_verdict"], "not_assessed")

    def test_deleted_immutable_evaluator_preserves_success_exit_but_fails_run(self):
        project = self.prepare_experiment('from pathlib import Path\nPath("evaluator.json").unlink()\nprint("SYNTHETIC exit zero with deleted evaluator")\n')
        record = EXPERIMENTS.run_local(project, "integration-fixture", "once", authorized=True, seed=7)
        self.assertEqual((record["status"], record["exit_code"]), ("failed", 0))
        self.assertEqual(record["error"]["type"], "InputIntegrityError")
        self.assertEqual(record["provenance"]["immutable_inputs_changed_during_run"], ["evaluator.json"])
        report = EXPERIMENTS.validate_records(project, "integration-fixture")
        self.assertEqual(report["runs"][0]["status"], "failed")

    def test_historical_records_stay_valid_after_current_source_is_changed(self):
        project = self.prepare_experiment('print("SYNTHETIC successful code review fixture")\n')
        record = EXPERIMENTS.run_local(project, "integration-fixture", "once", authorized=True, seed=7)
        self.assertEqual(record["status"], "succeeded")
        path = self.root / "research-atlas/experiments/integration-fixture/runs/once/record.json"
        before = path.read_bytes()
        (self.root / "candidate.py").write_text("changed after historical run\n", encoding="utf-8")
        report = EXPERIMENTS.validate_records(project, "integration-fixture")
        self.assertEqual(report["status"], "integrity_checked")
        self.assertEqual(path.read_bytes(), before)

    def test_legacy_freeze_loads_without_claiming_new_input_pinning(self):
        project = self.prepare_experiment('print("SYNTHETIC legacy schema compatibility fixture")\n')
        path = self.root / "research-atlas/experiments/integration-fixture/freeze.json"
        # Construct an explicitly synthetic v1 historical shape, not a migration
        # of real evidence. No payload is executed in this compatibility test.
        frozen = json.loads(path.read_text())
        frozen.pop("declared_inputs")
        frozen.pop("input_policy")
        content = EXPERIMENTS.json_bytes(frozen)
        path.write_bytes(content)
        path.with_suffix(".json.sha256").write_text(hashlib.sha256(content).hexdigest() + "\n")
        report = EXPERIMENTS.validate_records(project, "integration-fixture")
        self.assertEqual(report["input_policy"], "legacy_unpinned")
        self.assertEqual(report["scientific_verdict"], "not_assessed")
        self.assertEqual(path.read_bytes(), content)

    def test_boolean_freeze_schema_version_is_rejected(self):
        project = self.prepare_experiment('print("SYNTHETIC malformed metadata fixture")\n')
        path = self.root / "research-atlas/experiments/integration-fixture/freeze.json"
        original = path.read_bytes()
        frozen = json.loads(original)
        frozen["schema_version"] = True
        content = EXPERIMENTS.json_bytes(frozen)
        path.write_bytes(content)
        path.with_suffix(".json.sha256").write_text(hashlib.sha256(content).hexdigest() + "\n")
        with self.assertRaises(EXPERIMENTS.RecordError):
            EXPERIMENTS.load_frozen(project, "integration-fixture")
        with self.subTest("final-record schema also rejects bool instead of accepting True == 1"):
            # These are deliberately constructed metadata fixtures. No child
            # process is launched and no real historical record is modified.
            path.write_bytes(original)
            path.with_suffix(".json.sha256").write_text(hashlib.sha256(original).hexdigest() + "\n")
            _, valid_frozen = EXPERIMENTS.load_frozen(project, "integration-fixture")
            directory, attempt = EXPERIMENTS.new_attempt(project, "integration-fixture", "cancelled-fixture", valid_frozen, "local")
            record = EXPERIMENTS.finish_record(directory, attempt, "cancelled", [], exit_code=None, elapsed_seconds=0.0)
            record["schema_version"] = True
            record_path = directory / "record.json"
            malformed = EXPERIMENTS.json_bytes(record)
            record_path.write_bytes(malformed)
            record_path.with_suffix(".json.sha256").write_text(hashlib.sha256(malformed).hexdigest() + "\n")
            with self.assertRaises(EXPERIMENTS.RecordError):
                EXPERIMENTS.validate_records(project, "integration-fixture")

    def value_report(self, document, reported, *, pointer="/value", **extra):
        (self.root / "values.json").write_text(json.dumps(document), encoding="utf-8")
        return AUDIT.audit_values(self.root, {"schema_version": 1, "claims": [{
            "id": "synthetic-number", "artifact_path": "values.json", "pointer": pointer,
            "reported_value": reported, **extra,
        }]})

    def test_zero_tolerance_does_not_round_distinct_large_integers_into_a_match(self):
        report = self.value_report({"value": 9007199254740993}, 9007199254740992)
        self.assertFalse(report["all_values_match"])
        self.assertEqual(report["claims"][0]["status"], "mismatch")

    def test_pointer_escape_and_exact_number_match_remain_scientifically_unassessed(self):
        report = self.value_report({"a/b": {"~key": [0, 0.1]}}, 0.1, pointer="/a~1b/~0key/1")
        self.assertTrue(report["all_values_match"])
        self.assertEqual(report["claims"][0]["observed_value"], 0.1)
        self.assertEqual(report["scientific_verdict"], "not_assessed")

    def test_matching_number_does_not_hide_changed_source_version(self):
        report = self.value_report({"value": 42}, 42, expected_sha256="0" * 64)
        self.assertFalse(report["all_values_match"])
        self.assertEqual(report["claims"][0]["status"], "version_mismatch")
        self.assertEqual(report["claims"][0]["value_status"], "match")

    def test_boolean_value_is_not_a_numeric_claim(self):
        report = self.value_report({"value": True}, 1)
        self.assertFalse(report["all_values_match"])
        self.assertEqual(report["claims"][0]["status"], "non_numeric")

    def test_malformed_pointer_is_rejected_even_if_file_is_missing(self):
        ledger = {"schema_version": 1, "claims": [{"id": "synthetic-missing", "artifact_path": "missing.json",
                   "pointer": "/~2bad", "reported_value": 1}]}
        with self.assertRaises(ATLAS.AtlasError):
            AUDIT.audit_values(self.root, ledger)


if __name__ == "__main__":
    print("REVIEW_SOURCE_SHA256=" + json.dumps(LOADED_SOURCE_SHA256, sort_keys=True), flush=True)
    unittest.main()
