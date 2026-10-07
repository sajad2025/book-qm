"""Render the syllabus from a validated session list.

usage: python3 build_syllabus.py SESSIONS.jsonl FRONT_MATTER.md OUT.md [--fa FA.json]
The front matter is copied verbatim; in it, <<N_SESSIONS>>, <<N_PARTS>> and <<N_GAPS>> are replaced.
With --fa, the Farsi syllabus is written: titles, claims, goals and gaps come from FA.json
(English where a translation is missing), numbers are in Persian digits.
"""
import json, sys, collections
from fa_text import isolate, fa_digits

src, front, out = sys.argv[1:4]
FA = json.load(open(sys.argv[5], encoding='utf-8')) if len(sys.argv) > 5 and sys.argv[4] == '--fa' else None
D = fa_digits if FA else str
L = {
    'glance': ('## The parts at a glance', '## بخش‌ها در یک نگاه'),
    'glance_head': ('| Part | Sessions | Goal |', '| بخش | جلسه‌ها | هدف |'),
    'sessions': ('## Sessions', '## جلسه‌ها'),
    'sessions_intro': ("Each row gives the session's one claim and the earlier sessions it builds on. A session uses nothing that is not established in an earlier one. Sessions marked ◊ contain a labelled gap, listed in full after the sessions.",
                       'هر سطر ادعای یگانهٔ جلسه و جلسه‌های پیشینی را می‌دهد که جلسه بر پایهٔ آن‌هاست. هیچ جلسه‌ای چیزی را به کار نمی‌برد که در جلسه‌ای پیشین ثابت نشده باشد. جلسه‌هایی که با ◊ نشان خورده‌اند شکافی برچسب‌دار دارند که فهرست کامل آن‌ها پس از جلسه‌ها آمده است.'),
    'part': ('Part', 'بخش'),
    'table_head': ('| # | Session | Establishes | Builds on |', '| # | جلسه | ادعا | بر پایهٔ |'),
    'gaps': ('## Labelled gaps', '## شکاف‌های برچسب‌دار'),
    'gaps_intro': ('Every result the book uses without a full proof is listed here, with what is omitted, why, and where a complete proof can be found. The same label appears in the session itself.',
                   'هر نتیجه‌ای که کتاب بدون اثبات کامل به کار می‌برد اینجا فهرست شده است، همراه با آنچه حذف شده، دلیل آن، و جایی که اثبات کامل در آن آمده است. همین برچسب در خود جلسه نیز آمده است.'),
    'gaps_head': ('| Session | Gap |', '| جلسه | شکاف |'),
    'deps': ('## How the parts depend on each other', '## وابستگی بخش‌ها به یکدیگر'),
    'deps_intro': ('For each part, the earlier parts whose sessions it cites, with the number of citations.', 'برای هر بخش، بخش‌های پیشینی که این بخش به جلسه‌هایشان استناد می‌کند، همراه با شمار استنادها.'),
    'deps_head': ('| Part | Draws on |', '| بخش | بر پایهٔ |'),
}
def l(k): return L[k][1 if FA else 0]
def tr(kind, key, field, default):
    if not FA: return default
    v = FA.get(kind, {}).get(key, {}).get(field)
    return isolate(v) if v else default
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
        o.append(f'{D(ns[i])}-{D(ns[j])}' if j - i >= 2 else ('، ' if FA else ', ').join(D(x) for x in ns[i:j + 1]))
        i = j + 1
    return ('، ' if FA else ', ').join(o)

KIND = {'definition': 'Definition', 'theorem': 'Theorem', 'construction': 'Construction', 'calculation': 'Calculation',
        'example': 'Example', 'experiment': 'Experiment', 'survey': 'Survey', 'problems': 'Problems'}
if FA:
    KIND = {'definition': 'تعریف', 'theorem': 'قضیه', 'construction': 'ساخت', 'calculation': 'محاسبه',
            'example': 'مثال', 'experiment': 'آزمایش', 'survey': 'مرور', 'problems': 'مسئله‌ها'}
for p in parts:
    p['title'] = tr('parts', p['id'], 'title', p['title']); p['goal'] = tr('parts', p['id'], 'goal', p['goal'])
for s in sessions:
    for f, g in (('title', 'title'), ('establishes', 'claim'), ('gap', 'gap')):
        if s.get(f, '').strip(): s[f] = tr('sessions', s['slug'], g, s[f])

def cell(t):
    return str(t).replace('|', '\\|').replace('\n', ' ').strip()

gaps = [s for s in sessions if s['gap'].strip()]
o = []
fm = open(front, encoding='utf-8').read()
fm = fm.replace('<<N_SESSIONS>>', D(len(sessions))).replace('<<N_PARTS>>', D(len(parts))).replace('<<N_GAPS>>', D(len(gaps)))
o.append(fm.rstrip() + '\n')

o.append(l('glance') + '\n')
o.append(l('glance_head') + '\n|---|---|---|')
for p in parts:
    ns = [s['n'] for s in p['sessions']]
    o.append(f"| {D(p['id'])}. {cell(p['title'])} | {D(ns[0])}-{D(ns[-1])} | {cell(p['goal'])} |")
o.append('')

o.append(l('sessions') + '\n')
o.append(l('sessions_intro') + '\n')
for p in parts:
    o.append(f"### {l('part')} {D(p['id'])}. {p['title']}\n")
    o.append(p['goal'].strip() + '\n')
    o.append(l('table_head') + '\n|---|---|---|---|')
    for s in p['sessions']:
        mark = ' ◊' if s['gap'].strip() else ''
        kind = KIND.get(s['kind'], s['kind'].capitalize())
        o.append(f"| {D(s['part'])}.{D(s['n'])} | {cell(s['title'])}{mark} | *{kind}.* {cell(s['establishes'])} | {runs([num[u] for u in s['uses']]) or '-'} |")
    o.append('')

o.append(l('gaps') + '\n')
o.append(l('gaps_intro') + '\n')
o.append(l('gaps_head') + '\n|---|---|')
for s in gaps:
    o.append(f"| {D(s['part'])}.{D(s['n'])} {cell(s['title'])} | {cell(s['gap'])} |")
o.append('')

o.append(l('deps') + '\n')
o.append(l('deps_intro') + '\n')
o.append(l('deps_head') + '\n|---|---|')
for p in parts:
    c = collections.Counter(part_of[u] for s in p['sessions'] for u in s['uses'] if part_of[u] != p['id'])
    order = [q['id'] for q in parts]
    o.append(f"| {D(p['id'])}. {cell(p['title'])} | {('، ' if FA else ', ').join(f'{l('part')} {D(k)} ({D(c[k])})' for k in sorted(c, key=order.index)) or '-'} |")
o.append('')

open(out, 'w', encoding='utf-8').write('\n'.join(o))
print(f'{len(parts)} parts, {len(sessions)} sessions, {len(gaps)} gaps -> {out} ({len(" ".join(o).split())} words)')
