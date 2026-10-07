"""Generate book.json for the reader from plan/sessions.jsonl and the session files that exist.

usage (from the book-qm folder): python3 plan/build_book_json.py
"""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
parts, sessions = [], []
for line in (root / 'plan' / 'sessions.jsonl').read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    o = json.loads(line)
    if o['type'] == 'part':
        parts.append({'id': o['id'], 'title': o['title'], 'goal': o['goal']})
    else:
        o['part'] = parts[-1]['id']
        sessions.append(o)
num = {s['slug']: i for i, s in enumerate(sessions, 1)}

def find(folder, n, slug):
    p = root / folder / f'{n:03d}-{slug}.md'
    return f'{folder}/{p.name}' if p.exists() else None

out_sessions = []
for n, s in enumerate(sessions, 1):
    out_sessions.append({
        'n': n, 'slug': s['slug'], 'title': s['title'], 'kind': s['kind'], 'part': s['part'],
        'claim': s['establishes'], 'uses': sorted(num[u] for u in s['uses']), 'gap': bool(s.get('gap', '').strip()),
        'file': find('sessions', n, s['slug']), 'solutions': find('solutions', n, s['slug']),
    })
for p in parts:
    ns = [s['n'] for s in out_sessions if s['part'] == p['id']]
    p['first'], p['last'] = ns[0], ns[-1]

front = (root / 'plan' / 'front-matter.md').read_text(encoding='utf-8')
title_line = re.search(r'^\*\*(.+?)\*\*\s*$', front, re.M).group(1)
title, _, subtitle = title_line.partition(': ')
paras = [p.strip() for p in front.split('\n\n')]
desc = next(p for p in paras if p.startswith('This is a graduate course'))
desc = re.sub(r', in <<N_SESSIONS>> sessions in <<N_PARTS>> Parts', f', in {len(sessions)} sessions in {len(parts)} Parts', desc)
questions = re.findall(r'^\d\. (whether .+?) \(Q\d\);?\.?$', front, re.M)

book = {
    'title': title, 'subtitle': subtitle[:1].upper() + subtitle[1:], 'description': desc,
    'questions': questions, 'syllabus': '00-syllabus.md',
    'parts': parts, 'sessions': out_sessions,
}
(root / 'book.json').write_text(json.dumps(book, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
written = sum(1 for s in out_sessions if s['file'])
print(f'book.json: {len(parts)} parts, {len(out_sessions)} sessions, {written} written')
