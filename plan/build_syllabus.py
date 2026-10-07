"""Render the syllabus from a validated session list.

usage: python3 -I build_syllabus.py SESSIONS.jsonl FRONT_MATTER.md OUT.md
The front matter is copied verbatim; in it, <<N_SESSIONS>>, <<N_PARTS>> and <<N_GAPS>> are replaced.
"""
import json, sys, collections

src, front, out = sys.argv[1:4]
parts, sessions = [], []
for line in open(src, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    o = json.loads(line)
    if o['type'] == 'part':
        o['sessions'] = []; parts.append(o)
    else:
        o.setdefault('gap', ''); o['part'] = parts[-1]['id']
        sessions.append(o); parts[-1]['sessions'].append(o)
num = {s['slug']: i for i, s in enumerate(sessions, 1)}
for s in sessions:
    s['n'] = num[s['slug']]
    for u in s['uses']:
        assert num[u] < s['n'], (s['slug'], u)
part_of = {s['slug']: s['part'] for s in sessions}

def runs(ns):
    ns = sorted(set(ns)); o = []; i = 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1: j += 1
        o.append(f'{ns[i]}-{ns[j]}' if j - i >= 2 else ', '.join(f'{x}' for x in ns[i:j + 1]))
        i = j + 1
    return ', '.join(o)

KIND = {'definition': 'Definition', 'theorem': 'Theorem', 'construction': 'Construction', 'calculation': 'Calculation',
        'example': 'Example', 'experiment': 'Experiment', 'survey': 'Survey', 'problems': 'Problems'}

def cell(t):
    return str(t).replace('|', '\\|').replace('\n', ' ').strip()

gaps = [s for s in sessions if s['gap'].strip()]
o = []
fm = open(front, encoding='utf-8').read()
fm = fm.replace('<<N_SESSIONS>>', str(len(sessions))).replace('<<N_PARTS>>', str(len(parts))).replace('<<N_GAPS>>', str(len(gaps)))
o.append(fm.rstrip() + '\n')

o.append('## The parts at a glance\n')
o.append('| Part | Sessions | Goal |\n|---|---|---|')
for p in parts:
    ns = [s['n'] for s in p['sessions']]
    o.append(f"| {p['id']}. {cell(p['title'])} | {ns[0]}-{ns[-1]} | {cell(p['goal'])} |")
o.append('')

o.append('## Sessions\n')
o.append('Each row gives the session\'s one claim and the earlier sessions it builds on. A session uses nothing that is not established in an earlier one. Sessions marked ◊ contain a labelled gap, listed in full after the sessions.\n')
for p in parts:
    o.append(f"### Part {p['id']}. {p['title']}\n")
    o.append(p['goal'].strip() + '\n')
    o.append('| # | Session | Establishes | Builds on |\n|---|---|---|---|')
    for s in p['sessions']:
        mark = ' ◊' if s['gap'].strip() else ''
        kind = KIND.get(s['kind'], s['kind'].capitalize())
        o.append(f"| {s['part']}.{s['n']} | {cell(s['title'])}{mark} | *{kind}.* {cell(s['establishes'])} | {runs([num[u] for u in s['uses']]) or '-'} |")
    o.append('')

o.append('## Labelled gaps\n')
o.append('Every result the book uses without a full proof is listed here, with what is omitted, why, and where a complete proof can be found. The same label appears in the session itself.\n')
o.append('| Session | Gap |\n|---|---|')
for s in gaps:
    o.append(f"| {s['part']}.{s['n']} {cell(s['title'])} | {cell(s['gap'])} |")
o.append('')

o.append('## How the parts depend on each other\n')
o.append('For each part, the earlier parts whose sessions it cites, with the number of citations.\n')
o.append('| Part | Draws on |\n|---|---|')
for p in parts:
    c = collections.Counter(part_of[u] for s in p['sessions'] for u in s['uses'] if part_of[u] != p['id'])
    order = [q['id'] for q in parts]
    o.append(f"| {p['id']}. {cell(p['title'])} | {', '.join(f'Part {k} ({c[k]})' for k in sorted(c, key=order.index)) or '-'} |")
o.append('')

open(out, 'w', encoding='utf-8').write('\n'.join(o))
print(f'{len(parts)} parts, {len(sessions)} sessions, {len(gaps)} gaps -> {out} ({len(" ".join(o).split())} words)')
