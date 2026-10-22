"""Contract tests for supervision/gap/citation workbenches.

These tests verify maintained structure and safety boundaries, not scientific quality.
"""
import json
from pathlib import Path
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills/agent-research-atlas"
REGISTRY = SKILL / "assets/capability-registry.json"


class SupervisionContractTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        self.caps = {c["id"]: c for c in self.registry["capabilities"]}

    def test_supervisor_decision_contract_is_present(self):
        text = (SKILL / "references/research-supervision.md").read_text(encoding="utf-8")
        for token in ("PROCEED", "SEARCH MORE", "REPAIR MEASUREMENT", "NARROW", "PIVOT", "PARK", "STOP"):
            self.assertIn(token, text)
        self.assertIn("C29", self.caps)
        self.assertIn("evidence", self.caps["C29"]["limits"].lower())

    def test_loop_contains_pivot_and_return_to_literature(self):
        text = (SKILL / "references/research-supervision.md").read_text(encoding="utf-8")
        self.assertIn("Scientist", text)
        self.assertIn("Critic", text)
        self.assertIn("Supervisor", text)
        self.assertIn("pivot", text.lower())
        self.assertIn("literature", text.lower())
        cf = next(c for c in self.registry["conflicts"] if c["id"] == "CF29")
        self.assertIn("never stop", cf["reject"].lower())

    def test_citation_corpus_requires_support_and_non_support_fields(self):
        text = (SKILL / "assets/supervision/citation-corpus.md").read_text(encoding="utf-8")
        self.assertIn("Claim this source can support", text)
        self.assertIn("What this source does NOT support", text)
        self.assertIn("Exact locator", text)
        self.assertIn("C31", self.caps)

    def test_mentor_panel_preserves_evidence_levels(self):
        text = (SKILL / "assets/supervision/mentor-panel.md").read_text(encoding="utf-8")
        for token in ("direct", "recurring_inference", "speculative_extension"):
            self.assertIn(token, text)
        source = next(s for s in self.registry["sources"] if s["id"] == "SRC-MENTORFORGE-DISTILLER")
        self.assertTrue(any("private" in f["gap"].lower() or "私人" in f["gap"] for f in source["features"]))

    def test_new_sources_and_counts_are_registered(self):
        ids = {s["id"] for s in self.registry["sources"]}
        expected = {
            "SRC-KALARIS-AUTORESEARCH",
            "SRC-KDENSE-RESEARCH-LOOKUP",
            "SRC-45CK-GAP-FINDER",
            "SRC-MENTORFORGE-DISTILLER",
        }
        self.assertTrue(expected <= ids)
        self.assertEqual(len(self.registry["capabilities"]), 32)
        self.assertEqual(len(self.registry["conflicts"]), 32)
        self.assertEqual(sum(len(s["features"]) for s in self.registry["sources"]), 312)


if __name__ == "__main__":
    unittest.main()
