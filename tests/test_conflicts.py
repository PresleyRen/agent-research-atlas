"""Cross-workflow conflict regressions. All evidence and payloads are synthetic."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / 'skills/agent-research-atlas/scripts'


class ConflictTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='atlas-conflict-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def cli(self, script, *args, expected=0):
        result = subprocess.run([sys.executable, str(SCRIPTS / script), '--root', str(self.root), *args],
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout or result.stderr)

    def init(self):
        self.cli('atlas.py', 'init', '--synthetic')

    def patch(self, **batch):
        path = self.root / 'batch.json'
        path.write_text(json.dumps(batch), encoding='utf-8')
        return self.cli('atlas.py', 'upsert', '--file', str(path))

    def state(self):
        return json.loads((self.root / 'research-atlas/atlas.json').read_text())

    def paper(self, identifier='paper-a'):
        return {'id': identifier, 'type': 'paper', 'title': 'SYNTHETIC observation', 'status': 'read',
                'domains': ['routing'], 'sources': [{'access': 'abstract', 'url': 'https://example.org/' + identifier,
                'accessed_at': '2026-10-20', 'locator': 'synthetic abstract'}], 'data': {'observation': 'uncertain'}}

    def prepare_graph(self):
        self.init()
        self.patch(nodes=[self.paper(),
            {'id': 'claim-a', 'type': 'claim', 'title': 'SYNTHETIC limited claim', 'status': 'supported',
             'data': {'evidence_ids': ['paper-a'], 'reasoning': 'Fixture-only observation', 'limitations': 'SYNTHETIC schema test'}},
            {'id': 'plan-a', 'type': 'experiment', 'title': 'SYNTHETIC proposed follow-up', 'status': 'planned',
             'data': {'depends_on': ['claim-a']}},
            {'id': 'unrelated', 'type': 'problem', 'title': 'SYNTHETIC topical neighbor', 'domains': ['routing'], 'data': {}}],
            edges=[{'id': 'topic-link', 'source': 'paper-a', 'target': 'unrelated', 'relation': 'relates_to'}])

    def test_cf_evidence_change_flags_transitive_consumers_without_rewriting_truth(self):
        self.prepare_graph()
        self.patch(nodes=[{'id': 'paper-a', 'data': {'observation': 'corrected synthetic observation'}}])
        state = self.state()
        pending = {entry['node_id'] for entry in state['maintenance']['pending_reviews']}
        self.assertEqual(pending, {'claim-a', 'plan-a'})
        self.assertEqual(next(n for n in state['nodes'] if n['id'] == 'claim-a')['status'], 'supported')
        self.assertIn('Pending evidence reviews', (self.root / 'research-atlas/MAP.md').read_text())
        archives = list((self.root / 'research-atlas/history').glob('revision-000001-*.json'))
        self.assertEqual(len(archives), 1)
        old = json.loads(archives[0].read_text())
        self.assertEqual(next(n for n in old['nodes'] if n['id'] == 'paper-a')['data']['observation'], 'uncertain')

    def test_cf_new_counterevidence_reopens_old_claim_and_followup_only(self):
        self.prepare_graph()
        self.patch(nodes=[self.paper('paper-b')], edges=[{'id': 'counter', 'source': 'paper-b', 'target': 'claim-a', 'relation': 'contradicts'}])
        self.assertEqual({x['node_id'] for x in self.state()['maintenance']['pending_reviews']}, {'claim-a', 'plan-a'})
        self.assertEqual(next(n for n in self.state()['nodes'] if n['id'] == 'claim-a')['status'], 'supported')

    def test_cf_review_resolution_needs_current_revision_and_keeps_reason(self):
        self.prepare_graph()
        self.patch(nodes=[{'id': 'paper-a', 'data': {'observation': 'updated'}}])
        before = (self.root / 'research-atlas/atlas.json').read_bytes()
        args = ['resolve-review', '--node', 'claim-a', '--reviewer', 'synthetic-reviewer', '--note', 'Narrowed claim separately; dependencies inspected.']
        self.cli('atlas.py', *args, '--expected-revision', '1', expected=2)
        self.assertEqual(before, (self.root / 'research-atlas/atlas.json').read_bytes())
        self.cli('atlas.py', *args, '--expected-revision', str(self.state()['revision']))
        maintenance = self.state()['maintenance']
        self.assertEqual([e['node_id'] for e in maintenance['pending_reviews']], ['plan-a'])
        self.assertEqual(maintenance['review_log'][0]['reviewer'], 'synthetic-reviewer')
        self.assertIn('Narrowed', maintenance['review_log'][0]['note'])
        self.assertEqual(next(n for n in self.state()['nodes'] if n['id'] == 'claim-a')['status'], 'supported')

    def test_cf_noop_and_topical_membership_do_not_invalidate_research(self):
        self.prepare_graph()
        self.patch(nodes=[{'id': 'paper-a', 'data': {'observation': 'uncertain'}}])
        self.assertEqual(self.state()['maintenance']['pending_reviews'], [])
        report = self.cli('atlas.py', 'impact', '--node', 'paper-a')
        self.assertEqual({x['node_id'] for x in report['affected']}, {'claim-a', 'plan-a'})
        self.assertEqual(self.state()['maintenance']['pending_reviews'], [])

    def test_cf_dependency_cycles_terminate_and_missing_dependency_is_rejected(self):
        self.init()
        self.patch(nodes=[{'id': 'a', 'type': 'decision', 'title': 'SYNTHETIC a', 'data': {'depends_on': ['b']}},
                          {'id': 'b', 'type': 'decision', 'title': 'SYNTHETIC b', 'data': {'depends_on': ['a']}}])
        self.assertEqual([x['node_id'] for x in self.cli('atlas.py', 'impact', '--node', 'a')['affected']], ['b'])
        path = self.root / 'bad.json'
        path.write_text(json.dumps({'nodes': [{'id': 'a', 'data': {'depends_on': ['missing']}}]}))
        before = self.state()
        self.cli('atlas.py', 'upsert', '--file', str(path), expected=2)
        self.assertEqual(before, self.state())

    def prepare_experiment(self, *, mutable=False, self_edit=False):
        (self.root / 'examples').mkdir()
        shutil.copyfile(REPO / 'examples/tiny_agent_experiment.py', self.root / 'examples/tiny_agent_experiment.py')
        evaluator = self.root / 'evaluator.json'
        evaluator.write_text('{"threshold": 0.8}\n')
        plan = json.loads((REPO / 'skills/agent-research-atlas/assets/experiment-plan.example.json').read_text())
        plan['experiment_id'] = 'conflict-fixture'
        plan['command']['argv'][0] = sys.executable
        plan['command']['input_files'].append('evaluator.json')
        if mutable:
            plan['command']['mutable_input_files'] = ['examples/tiny_agent_experiment.py']
        if self_edit:
            plan['command']['argv'] = [sys.executable, '-c', 'from pathlib import Path; Path("evaluator.json").write_text("changed"); print("payload exit zero")']
        plan['budget'] = {'max_runs': 2, 'max_run_seconds': 2, 'max_total_seconds': 4}
        path = self.root / 'plan.json'
        path.write_text(json.dumps(plan))
        self.cli('experiments.py', 'plan', '--file', str(path))
        self.cli('experiments.py', 'freeze', 'conflict-fixture', '--mode', 'exploratory', '--rationale', 'SYNTHETIC conflict fixture')

    def run_experiment(self, name='run-one', expected=0):
        return self.cli('experiments.py', 'run', 'conflict-fixture', '--run-id', name, '--authorized-local', expected=expected)

    def test_cf_evaluator_drift_is_retained_but_never_executed_as_same_protocol(self):
        self.prepare_experiment()
        (self.root / 'evaluator.json').write_text('{"threshold": 0.1}\n')
        record = self.run_experiment(expected=4)
        self.assertEqual(record['status'], 'launch_failed')
        self.assertIsNone(record['exit_code'])
        self.assertIn('Frozen input changed', record['error']['message'])
        self.assertEqual((self.root / 'research-atlas/experiments/conflict-fixture/runs/run-one/stdout.txt').read_text(), '')
        self.cli('experiments.py', 'validate-record', 'conflict-fixture')

    def test_cf_explicit_candidate_mutation_is_allowed_but_evaluator_stays_fixed(self):
        self.prepare_experiment(mutable=True)
        candidate = self.root / 'examples/tiny_agent_experiment.py'
        candidate.write_text(candidate.read_text() + '\n# SYNTHETIC new candidate implementation\n')
        record = self.run_experiment()
        self.assertEqual(record['status'], 'succeeded')
        self.assertEqual(record['scientific_verdict'], 'not_assessed')
        self.assertEqual(record['provenance']['input_policy'], 'frozen_except_declared_mutable')
        (self.root / 'evaluator.json').write_text('{"threshold": 0.01}')
        self.run_experiment('run-two', expected=4)

    def test_cf_midrun_evaluator_mutation_preserves_exit_zero_but_fails_integrity(self):
        self.prepare_experiment(self_edit=True)
        record = self.run_experiment(expected=4)
        self.assertEqual(record['status'], 'failed')
        self.assertEqual(record['exit_code'], 0)
        self.assertEqual(record['provenance']['immutable_inputs_changed_during_run'], ['evaluator.json'])
        self.assertEqual(record['scientific_verdict'], 'not_assessed')
        self.cli('experiments.py', 'validate-record', 'conflict-fixture')


if __name__ == '__main__':
    unittest.main()
