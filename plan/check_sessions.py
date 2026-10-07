"""Check every written session against the syllabus and the writing plan.

usage (from the book-qm folder): python3 plan/check_sessions.py [N ...]
With numbers, only those sessions are checked. Exit status 1 if any check fails.
"""
import json, re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
parts, sessions = [], []
for line in (root / 'plan' / 'sessions.jsonl').read_text(encoding='utf-8').splitlines():
    if line.strip():
        o = json.loads(line)
        (parts if o['type'] == 'part' else sessions).append(o)
num = {s['slug']: i for i, s in enumerate(sessions, 1)}
uses = {num[s['slug']]: {num[u] for u in s['uses']} for s in sessions}
closure = {}
for n in sorted(uses):
    c = set()
    for u in uses[n]:
        c |= {u} | closure[u]
    closure[n] = c

KIND = {'definition': 'Definition', 'theorem': 'Theorem', 'construction': 'Construction', 'calculation': 'Calculation',
        'example': 'Example', 'experiment': 'Experiment', 'survey': 'Survey', 'problems': 'Problems'}
BANNED = ['clearly', 'obviously', 'it is easy to see', 'it can be shown', 'trivially', 'evidently', 'it is straightforward',
          'it is not hard to see', 'one easily', 'needless to say']

def numbers(text):
    out = set()
    for m in re.finditer(r'Sessions?\s+((?:\d+(?:\s*(?:,|and|-|–|to)\s*)?)+)', text):
        chunk = m.group(1)
        for a, b in re.findall(r'(\d+)\s*(?:-|–|to)\s*(\d+)', chunk):
            out |= set(range(int(a), int(b) + 1))
        chunk = re.sub(r'(\d+)\s*(?:-|–|to)\s*(\d+)', ' ', chunk)
        out |= {int(x) for x in re.findall(r'\d+', chunk)}
    return out

def strip_math(text):
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    return re.sub(r'\$(?:\\.|[^\\$\n])+?\$', ' ', text)

errors, warnings, checked = [], [], 0
only = {int(a) for a in sys.argv[1:]}
for n, s in enumerate(sessions, 1):
    if only and n not in only:
        continue
    f = root / 'sessions' / f'{n:03d}-{s["slug"]}.md'
    if not f.exists():
        if only:
            errors.append(f'{n}: no file {f.relative_to(root)}')
        continue
    checked += 1
    text = f.read_text(encoding='utf-8')
    lines = [l for l in text.splitlines()]
    def err(msg): errors.append(f'{n} {s["slug"]}: {msg}')
    def warn(msg): warnings.append(f'{n} {s["slug"]}: {msg}')
    nonempty = [l for l in lines if l.strip()]
    if not nonempty or nonempty[0].strip() != f'# Session {n}. {s["title"]}':
        err(f'first line must be "# Session {n}. {s["title"]}"')
    kind_line = nonempty[1].strip() if len(nonempty) > 1 else ''
    m = re.fullmatch(r'\*(\w+)\. Builds on (.+)\.\*', kind_line)
    if not m:
        err('second line must be "*Kind. Builds on ... .*"')
    else:
        if m.group(1) != KIND[s['kind']]:
            err(f'kind is {m.group(1)!r}, syllabus says {KIND[s["kind"]]!r}')
        listed = set() if m.group(2) == 'nothing earlier' else numbers('Sessions ' + m.group(2).replace('Session ', '').replace('Sessions ', ''))
        if listed != uses[n]:
            err(f'builds-on lists {sorted(listed)}, syllabus says {sorted(uses[n])}')
    if not re.search(r'^\*\*Claim\.\*\*', text, re.M):
        err('no "**Claim.**" paragraph')
    secs = [tuple(map(int, x)) for x in re.findall(r'^## (\d+)\.(\d+) ', text, re.M)]
    if any(a != n for a, _ in secs):
        err('section numbers must start with the session number')
    if [b for _, b in secs] != list(range(1, len(secs) + 1)):
        warn(f'sections are not numbered 1, 2, 3, ...: {[b for _, b in secs]}')
    if s['kind'] == 'problems':
        if '## Problems' not in text:
            err('a problems session needs a "## Problems" section')
    elif s['kind'] != 'survey' and '## Exercises' not in text:
        err('no "## Exercises" section')
    if '## Exercises' in text:
        ex = text.split('## Exercises', 1)[1]
        for tier in ('*Check*', '*Prove*'):
            if tier not in ex and s['kind'] not in ('survey', 'problems'):
                err(f'exercises lack the {tier} tier')
    sol = root / 'solutions' / f'{n:03d}-{s["slug"]}.md'
    if '## Exercises' in text or '## Problems' in text:
        if not sol.exists():
            err(f'no solutions file {sol.relative_to(root)}')
        elif sol.read_text(encoding='utf-8').splitlines()[0].strip() != f'# Solutions to Session {n}. {s["title"]}':
            err('solutions file must start with "# Solutions to Session N. Title"')
        if f'solutions/{n:03d}-{s["slug"]}.md' not in text:
            err('no link to the solutions file')
    has_gap = bool(s.get('gap', '').strip())
    if has_gap and '> **Gap.**' not in text:
        err('the syllabus lists a gap but the session has no "> **Gap.**" box')
    if not has_gap and '> **Gap.**' in text:
        err('the session has a gap box but the syllabus lists none')
    body = '\n'.join(lines[2:])
    for k in sorted(numbers(strip_math(body))):
        if k == n:
            continue
        if k > n:
            err(f'refers to later Session {k}')
        elif k not in closure[n]:
            warn(f'refers to Session {k}, which is not among its prerequisites')
    prose = strip_math(text).lower()
    for b in BANNED:
        if re.search(r'\b' + re.escape(b) + r'\b', prose):
            err(f'banned phrase "{b}"')
    if re.search(r'\biff\b', prose):
        warn('uses "iff"; write "if and only if"')
    for i, l in enumerate(lines, 1):
        if '$$' in l and l.strip() != '$$':
            err(f'line {i}: "$$" must stand on a line of its own')
    inline = re.findall(r'(?<!\$)\$(?!\$)((?:\\.|[^\\$\n])+?)\$', re.sub(r'\$\$[\s\S]*?\$\$', ' ', text))
    for expr in inline:
        if '<' in expr or '>' in expr:
            warn(f'raw < or > inside $...$: {expr[:40]!r}')
    if sum(1 for l in lines if l.strip() == '$$') % 2:
        err('unbalanced "$$" display delimiters')

for w in warnings: print('WARNING:', w)
for e in errors: print('ERROR:', e)
print(f'checked {checked} session file(s): {len(errors)} errors, {len(warnings)} warnings')
sys.exit(1 if errors else 0)
