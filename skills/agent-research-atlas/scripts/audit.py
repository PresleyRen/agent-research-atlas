#!/usr/bin/env python3
"""Locate research capabilities, check extension contracts, and audit local numeric claims.

Read-only. No network clients, automatic scientific verdicts, or paid execution.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import math
from pathlib import Path, PureWindowsPath
import re
import sys
from fractions import Fraction

from atlas import Atlas, AtlasError, dumps, inside, read_json, validate
from experiments import RecordError, parse_json

SKILL = Path(__file__).resolve().parents[1]
REGISTRY = SKILL / 'assets/capability-registry.json'
FEATURE_STATUSES = {'implemented', 'protocol', 'optional', 'reference', 'deferred', 'rejected'}


def path_inside(root, relative):
    if not isinstance(relative, str) or '\\' in relative or PureWindowsPath(relative).drive:
        raise AtlasError('Expected a portable relative path')
    return inside(root, relative)


def symbols(path):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    result = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            result.add(node.name)
            if isinstance(node, ast.ClassDef):
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        result.add(node.name + '.' + member.name)
    return result


def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise AtlasError(field + ' must be nonempty text')


def check_reference(reference, root, label):
    if not isinstance(reference, dict):
        raise AtlasError(label + ': reference must be an object')
    path = path_inside(root, reference.get('path'))
    if not path.is_file():
        raise AtlasError(label + ': missing file ' + str(reference.get('path')))
    if reference.get('symbol') and (path.suffix != '.py' or reference['symbol'] not in symbols(path)):
        raise AtlasError(label + ': missing Python symbol ' + str(reference['symbol']))
    if reference.get('anchor'):
        require_text(reference['anchor'], label + '.anchor')
        if reference['anchor'] not in path.read_text(encoding='utf-8'):
            raise AtlasError(label + ': missing document anchor ' + reference['anchor'])


def unique_rows(rows, label):
    if not isinstance(rows, list) or not rows:
        raise AtlasError(label + ' must be a nonempty array')
    index = {}
    for row in rows:
        if not isinstance(row, dict):
            raise AtlasError(label + ' entries must be objects')
        require_text(row.get('id'), label + '.id')
        if row['id'] in index:
            raise AtlasError(label + ': duplicate ID ' + row['id'])
        index[row['id']] = row
    return index


def check_registry(registry, skill=SKILL, repo=None):
    if not isinstance(registry, dict) or type(registry.get('schema_version')) is not int or registry['schema_version'] != 1:
        raise AtlasError('Unsupported capability registry schema')
    caps = unique_rows(registry.get('capabilities'), 'capabilities')
    sources = unique_rows(registry.get('sources'), 'sources')
    conflicts = unique_rows(registry.get('conflicts'), 'conflicts')
    features = set()
    for identifier, cap in caps.items():
        for key in ('name', 'description', 'limits', 'remedy'):
            require_text(cap.get(key), identifier + '.' + key)
        if not isinstance(cap.get('implementation'), list) or not cap['implementation']:
            raise AtlasError(identifier + ': implementation locations required')
        for ref in cap['implementation']:
            check_reference(ref, skill, identifier)
        if not isinstance(cap.get('tests'), list) or not cap['tests']:
            raise AtlasError(identifier + ': verification references required (including honest untested records)')
        for ref in cap['tests']:
            if ref.get('kind') not in {'unit', 'conflict', 'forward', 'live', 'not_run'}:
                raise AtlasError(identifier + ': unknown verification kind')
            if repo:
                check_reference(ref, repo, identifier)
        dependencies = cap.get('depends_on', [])
        if not isinstance(dependencies, list) or any(dep not in caps or dep == identifier for dep in dependencies):
            raise AtlasError(identifier + ': invalid capability dependency')
    # Capability dependencies express required contracts and must form a DAG.
    visiting, visited = set(), set()
    def visit(identifier):
        if identifier in visiting:
            raise AtlasError('Capability dependency cycle at ' + identifier)
        if identifier in visited:
            return
        visiting.add(identifier)
        for dep in caps[identifier].get('depends_on', []):
            visit(dep)
        visiting.remove(identifier)
        visited.add(identifier)
    for identifier in caps:
        visit(identifier)
    for identifier, source in sources.items():
        for key in ('name', 'url', 'read_depth', 'revision'):
            require_text(source.get(key), identifier + '.' + key)
        if not re.match(r'^https?://[^/]+', source['url']):
            raise AtlasError(identifier + ': official/source URL required')
        for feature_id, feature in unique_rows(source.get('features'), identifier + '.features').items():
            if feature_id in features:
                raise AtlasError('Duplicate global feature ID ' + feature_id)
            features.add(feature_id)
            require_text(feature.get('label'), feature_id + '.label')
            if feature.get('status') not in FEATURE_STATUSES:
                raise AtlasError(feature_id + ': invalid adoption status')
            mapped = feature.get('capabilities')
            if not isinstance(mapped, list) or not mapped or any(cap not in caps for cap in mapped):
                raise AtlasError(feature_id + ': must map to real capabilities')
            for key in ('gap', 'remedy'):
                require_text(feature.get(key), feature_id + '.' + key)
            complements = feature.get('complements', [])
            if not isinstance(complements, list) or any(other not in sources for other in complements):
                raise AtlasError(feature_id + ': unknown complementary source')
    for identifier, conflict in conflicts.items():
        for key in ('tension', 'retain', 'reject', 'reason', 'extension_rule'):
            require_text(conflict.get(key), identifier + '.' + key)
        if not conflict.get('capabilities') or any(cap not in caps for cap in conflict['capabilities']):
            raise AtlasError(identifier + ': unknown conflict capability')
        if not conflict.get('tests'):
            raise AtlasError(identifier + ': conflict verification references required')
        for ref in conflict['tests']:
            if ref.get('kind') not in {'unit', 'conflict', 'forward', 'live', 'not_run'}:
                raise AtlasError(identifier + ': invalid test kind')
            if repo:
                check_reference(ref, repo, identifier)
    return {'valid': True, 'capabilities': len(caps), 'sources': len(sources), 'features': len(features),
            'conflicts': len(conflicts), 'test_references_checked': bool(repo),
            'meaning': 'Registry IDs, files, symbols and dependencies checked; coverage labels are reviewed declarations, not effectiveness scores.'}


def locate(registry, query):
    require_text(query, 'query')
    terms = query.casefold().split()
    results = []
    for cap in registry['capabilities']:
        searchable = ' '.join([cap['id'], cap['name'], cap['description'], ' '.join(cap.get('keywords', [])),
                               ' '.join(cap.get('symptoms', [])), cap['limits'], cap['remedy']]).casefold()
        score = sum(term in searchable for term in terms)
        if not score:
            continue
        sources = []
        for source in registry['sources']:
            matching = [feature for feature in source['features'] if cap['id'] in feature['capabilities']]
            if matching:
                sources.append({'id': source['id'], 'name': source['name'], 'features': matching})
        results.append({'match_terms': score, **cap, 'sources': sources,
                        'conflicts': [c['id'] for c in registry['conflicts'] if cap['id'] in c['capabilities']]})
    results.sort(key=lambda row: (-row['match_terms'], row['id']))
    return {'query': query, 'matches': results, 'meaning': 'Lexical maintenance lookup, not a research-quality ranking. Try a capability ID or a shorter symptom if empty.'}


def project_gaps(root, atlas_dir=None):
    atlas = Atlas(root, atlas_dir)
    if not atlas.file('atlas.json').is_file():
        return {'issues': [{'code': 'G-MAP', 'capabilities': ['C02'], 'reason': 'No selected native atlas',
                            'next': 'Run discover, read existing maps, then reuse/adopt/init.'}], 'scientific_verdict': 'not_assessed'}
    state = atlas.load()
    issues = []
    def add(code, caps, nodes, reason, next_step):
        issues.append({'code': code, 'capabilities': caps, 'node_ids': nodes, 'reason': reason, 'next': next_step})
    pending = state.get('maintenance', {}).get('pending_reviews', [])
    if pending:
        add('G-REVIEW', ['C20', 'C18'], [entry['node_id'] for entry in pending], 'Recorded premises changed',
            'Inspect impact paths, reread changed evidence, revise affected claims/plans, then resolve-review with current revision and reason.')
    imports = [item['path'] for item in state.get('imports', []) if item.get('status') != 'normalized']
    if imports:
        add('G-IMPORT', ['C02', 'C05'], [], 'Unfinished semantic imports: ' + ', '.join(imports), 'Read original maps and normalize sourced nodes; registration is not understanding.')
    for coverage in ('unsearched', 'stale'):
        nodes = [n['id'] for n in state['nodes'] if n['type'] == 'domain' and n.get('data', {}).get('coverage', 'unsearched') == coverage]
        if nodes:
            add('G-COVERAGE-' + coverage.upper(), ['C01', 'C03'], nodes, 'Recorded coverage is ' + coverage,
                'Scope a bilingual search, execute available providers, record limits and actual results; seed folders are not a literature review.')
    gaps = [n for n in state['nodes'] if n['type'] == 'gap']
    active_gaps = [n['id'] for n in gaps if n.get('status', 'candidate') in {'candidate', 'open', 'partially_solved', 'unknown', 'inaccessible'}]
    if active_gaps:
        add('G-RESEARCH-GAPS', ['C29', 'C30', 'C31', 'C32'], active_gaps,
            'Recorded research gaps still require direction decisions or further evidence',
            'Read the Gap Ledger/linked papers, verify later work and data support, then record a Supervisor proceed/search-more/repair/narrow/pivot/park/stop decision.')
    hypotheses = [n for n in state['nodes'] if n['type'] == 'hypothesis']
    unresolved = [n['id'] for n in hypotheses if n.get('status', 'proposed') in {'proposed', 'grounded'} and any(
        n.get('data', {}).get('feasibility', {}).get(key) != 'available' for key in ('data', 'compute', 'evaluation', 'budget'))]
    if unresolved:
        add('G-FEASIBILITY', ['C11', 'C13'], unresolved, 'One or more resources are not verified available',
            'Inspect local data rights, implementation, evaluator and budget. Resolve the cheapest decision-changing uncertainty before promotion.')
    return {'revision': state['revision'], 'issues': issues, 'scientific_verdict': 'not_assessed',
            'limits': 'Only explicit recorded states are diagnosed. A clean report does not establish novelty, sound design, data rights or complete literature coverage.'}


def json_pointer(document, pointer):
    if not isinstance(pointer, str) or (pointer and not pointer.startswith('/')):
        raise AtlasError('JSON Pointer must be empty (root) or start with /')
    if re.search(r'~(?![01])', pointer):
        raise AtlasError('Invalid JSON Pointer escape')
    current = document
    if not pointer:
        return current
    for token in pointer[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        if isinstance(current, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', token):
                raise KeyError(token)
            current = current[int(token)]
        elif isinstance(current, dict):
            current = current[token]
        else:
            raise KeyError(token)
    return current


def finite_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def audit_values(root, ledger):
    if not isinstance(ledger, dict) or set(ledger) != {'schema_version', 'claims'} or type(ledger['schema_version']) is not int or ledger['schema_version'] != 1:
        raise AtlasError('Value ledger must contain schema_version=1 and claims')
    rows = unique_rows(ledger['claims'], 'claims')
    results = []
    for identifier, item in rows.items():
        required = {'id', 'artifact_path', 'pointer', 'reported_value'}
        if not required <= set(item) or set(item) - required - {'abs_tol', 'rel_tol', 'expected_sha256'}:
            raise AtlasError(identifier + ': unknown or missing numerical claim fields')
        if not finite_number(item['reported_value']):
            raise AtlasError(identifier + ': reported_value must be finite numeric')
        for key in ('abs_tol', 'rel_tol'):
            if not finite_number(item.get(key, 0)) or item.get(key, 0) < 0:
                raise AtlasError(identifier + ': tolerances must be finite and nonnegative')
        if 'expected_sha256' in item and not re.fullmatch(r'[0-9a-f]{64}', str(item['expected_sha256'])):
            raise AtlasError(identifier + ': expected_sha256 must be a lowercase SHA-256')
        # Validate syntax even when a file is absent, so malformed queries cannot hide as access failures.
        try:
            json_pointer({}, item['pointer'])
        except KeyError:
            pass
        path = path_inside(Path(root), item['artifact_path'])
        row = {'id': identifier, 'artifact_path': item['artifact_path'], 'pointer': item['pointer'],
               'reported_value': item['reported_value'], 'status': 'missing_file'}
        if path.is_file():
            raw = path.read_bytes()
            row['source_sha256'] = hashlib.sha256(raw).hexdigest()
            row['version_match'] = item.get('expected_sha256') in (None, row['source_sha256'])
            try:
                document = parse_json(raw)
            except (RecordError, UnicodeError) as exc:
                row.update(status='unparseable', detail=str(exc))
            else:
                try:
                    observed = json_pointer(document, item['pointer'])
                except (KeyError, IndexError):
                    row['status'] = 'missing_locator'
                else:
                    if not finite_number(observed):
                        row['status'] = 'non_numeric'
                    else:
                        row['observed_value'] = observed
                        # Strict abs/relative tolerance; zero defaults require exact numeric equality.
                        observed_exact, reported_exact = Fraction(observed), Fraction(item['reported_value'])
                        tolerance = max(Fraction(item.get('abs_tol', 0)), Fraction(item.get('rel_tol', 0)) * max(abs(observed_exact), abs(reported_exact)))
                        close = abs(observed_exact - reported_exact) <= tolerance
                        row['status'] = 'match' if close else 'mismatch'
                if not row['version_match']:
                    row['value_status'] = row['status']
                    row['status'] = 'version_mismatch'
        results.append(row)
    return {'all_values_match': all(row['status'] == 'match' for row in results), 'claims': results,
            'scientific_verdict': 'not_assessed',
            'meaning': 'Numbers checked against specified local JSON locations. This does not validate measurement, independence, statistical analysis or the scientific claim.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', default=str(REGISTRY))
    parser.add_argument('--root', help='Existing research project for project/values commands')
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check')
    check.add_argument('--repo', help='Distribution repository root; include test path/symbol checks')
    sub.add_parser('coverage')
    look = sub.add_parser('locate')
    look.add_argument('--query', required=True)
    project = sub.add_parser('project')
    project.add_argument('--atlas-dir')
    values = sub.add_parser('values')
    values.add_argument('--ledger', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command in {'project', 'values'}:
            if not args.root or not Path(args.root).is_dir():
                raise AtlasError('--root must name an existing project')
            result = project_gaps(args.root, args.atlas_dir) if args.command == 'project' else audit_values(args.root, read_json(args.ledger))
        else:
            registry = read_json(args.registry)
            if args.command == 'check':
                result = check_registry(registry, repo=Path(args.repo) if args.repo else None)
            elif args.command == 'locate':
                result = locate(registry, args.query)
            else:
                result = {'audit_scope': registry['audit_scope'], 'capabilities': registry['capabilities'],
                          'source_counts': len(registry['sources']), 'features_by_status': {
                              status: sum(f['status'] == status for source in registry['sources'] for f in source['features']) for status in sorted(FEATURE_STATUSES)}}
        print(dumps(result), end='')
        return 3 if args.command == 'values' and not result['all_values_match'] else 0
    except (AtlasError, OSError, UnicodeError, KeyError, TypeError, ValueError) as exc:
        print(dumps({'error': str(exc)}), file=sys.stderr, end='')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
