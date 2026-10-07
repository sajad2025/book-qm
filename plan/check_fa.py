"""Check the Farsi translation of each written session against its English source.

usage (from the book folder): python3 plan/check_fa.py [N ...]
With numbers, only those sessions are checked. Exit status 1 if any check fails.
The conventions are in plan/fa/STYLE.md.
"""
import json, re, sys
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent.parent
parts, sessions = [], []
for line in (root / 'plan' / 'sessions.jsonl').read_text(encoding='utf-8').splitlines():
    if line.strip():
        o = json.loads(line)
        if o['type'] == 'part':
            parts.append(o)
        else:
            o['part'] = parts[-1]['id']; sessions.append(o)
num = {s['slug']: i for i, s in enumerate(sessions, 1)}
uses = {num[s['slug']]: {num[u] for u in s['uses']} for s in sessions}
closure = {}
for n in sorted(uses):
    c = set()
    for u in uses[n]:
        c |= {u} | closure[u]
    closure[n] = c
fa_meta = json.loads((root / 'plan' / 'fa.json').read_text(encoding='utf-8')) if (root / 'plan' / 'fa.json').exists() else {}

FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
EN = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
def fa(x): return str(x).translate(FA)
KIND = {'definition': 'تعریف', 'theorem': 'قضیه', 'construction': 'ساخت', 'calculation': 'محاسبه',
        'example': 'مثال', 'experiment': 'آزمایش', 'survey': 'مرور', 'problems': 'مسئله‌ها'}
BANNED = ['بدیهی است', 'واضح است', 'به‌وضوح', 'به‌سادگی دیده', 'به‌آسانی دیده', 'می‌توان نشان داد', 'به‌راحتی دیده']
REF = re.compile(r'(?:جلسهٔ|جلسه‌های|جلسه)\s+([۰-۹]+(?:(?:\s*،\s*(?:و\s+)?|\s+و\s+|\s+یا\s+|\s+تا\s+|\s*[-–]\s*)[۰-۹]+)*)')

def refs(text):
    out = set()
    for m in REF.finditer(text):
        chunk = m.group(1).translate(EN)
        for a, b in re.findall(r'(\d+)\s*(?:-|–|تا)\s*(\d+)', chunk):
            out |= set(range(int(a), int(b) + 1))
        chunk = re.sub(r'(\d+)\s*(?:-|–|تا)\s*(\d+)', ' ', chunk)
        out |= {int(x) for x in re.findall(r'\d+', chunk)}
    return out

def norm_math(m):
    m = re.sub(r'\\text\{[^{}]*\}', r'\\text{}', m)
    return re.sub(r'\s+', '', m)

def maths(text):
    displays = [norm_math(x) for x in re.findall(r'^\$\$\n([\s\S]*?)\n\$\$$', text, re.M)]
    rest = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    inline = Counter(norm_math(x) for x in re.findall(r'(?<!\$)\$(?!\$)((?:\\.|[^\\$\n])+?)\$', rest))
    return displays, inline

def strip_math(text):
    text = re.sub(r'\$\$[\s\S]*?\$\$', ' ', text)
    return re.sub(r'\$(?:\\.|[^\\$\n])+?\$', ' ', text)

def list_items(text, heading):
    if heading not in text:
        return 0
    return len(re.findall(r'^\d+\. ', text.split(heading, 1)[1].split('\nSolutions:')[0].split('\nحل‌ها:')[0], re.M))

errors, warnings, checked = [], [], 0
only = {int(a) for a in sys.argv[1:]}
for n, s in enumerate(sessions, 1):
    if only and n not in only:
        continue
    name = f'{n:03d}-{s["slug"]}.md'
    en_f, fa_f = root / 'sessions' / name, root / 'fa' / 'sessions' / name
    if not en_f.exists():
        continue
    if not fa_f.exists():
        if only:
            errors.append(f'{n}: no file fa/sessions/{name}')
        continue
    checked += 1
    en, t = en_f.read_text(encoding='utf-8'), fa_f.read_text(encoding='utf-8')
    def err(msg): errors.append(f'{n} {s["slug"]}: {msg}')
    def warn(msg): warnings.append(f'{n} {s["slug"]}: {msg}')
    lines = [l for l in t.splitlines() if l.strip()]
    label = f'{fa(s["part"])}.{fa(n)}.'
    title_fa = fa_meta.get('sessions', {}).get(s['slug'], {}).get('title')
    if not lines or not lines[0].startswith(f'# {label} '):
        err(f'first line must start with "# {label} "')
    elif title_fa and lines[0] != f'# {label} {title_fa}':
        err(f'heading title differs from plan/fa.json: {title_fa!r}')
    kind_line = lines[1] if len(lines) > 1 else ''
    m = re.fullmatch(r'\*(\S+)\. بر پایهٔ (.+)\.\*', kind_line.strip())
    if not m:
        err('second line must be "*Kind. بر پایهٔ ... .*"')
    else:
        if m.group(1) != KIND[s['kind']]:
            err(f'kind is {m.group(1)!r}, expected {KIND[s["kind"]]!r}')
        listed = set() if 'هیچ' in m.group(2) else refs(m.group(2) if m.group(2).startswith('جلسه') else 'جلسه ' + m.group(2))
        if listed != uses[n]:
            err(f'builds-on lists {sorted(listed)}, syllabus says {sorted(uses[n])}')
    if not re.search(r'^\*\*ادعا\.\*\*', t, re.M):
        err('no "**ادعا.**" paragraph')
    en_secs = re.findall(r'^## (\d+)\.(\d+) ', en, re.M)
    fa_secs = [(a.translate(EN), b.translate(EN)) for a, b in re.findall(r'^## ([۰-۹]+)\.([۰-۹]+) ', t, re.M)]
    if fa_secs != en_secs:
        err(f'sections {[".".join(x) for x in fa_secs]} differ from English {[".".join(x) for x in en_secs]}')
    for en_h, fa_h in (('## Exercises', '## تمرین‌ها'), ('## Problems', '## مسئله‌ها')):
        if (en_h in en) != (fa_h in t):
            err(f'"{en_h}" in English needs "{fa_h}" in Farsi')
        elif en_h in en and list_items(en, en_h) != list_items(t, fa_h):
            err(f'{list_items(t, fa_h)} numbered items under "{fa_h}", English has {list_items(en, en_h)}')
    if '## Exercises' in en:
        for tier_en, tier_fa in (('*Check*', '*بررسی*'), ('*Prove*', '*اثبات*'), ('*Extend*', '*فراتر*')):
            if (tier_en in en) != (tier_fa in t):
                err(f'tier {tier_en} needs {tier_fa}')
    if ('> **Gap.**' in en) != ('> **شکاف.**' in t):
        err('gap box: "> **Gap.**" in English needs "> **شکاف.**" in Farsi')
    pairs = [(en, t, 'session')]
    sol_en, sol_fa = root / 'solutions' / name, root / 'fa' / 'solutions' / name
    if sol_en.exists():
        if not sol_fa.exists():
            err(f'no file fa/solutions/{name}')
        else:
            st = sol_fa.read_text(encoding='utf-8')
            if not st.startswith(f'# حل تمرین‌های {label} '):
                err(f'solutions must start with "# حل تمرین‌های {label} "')
            pairs.append((sol_en.read_text(encoding='utf-8'), st, 'solutions'))
            se, sf = pairs[-1][0], st
            ce = len(re.findall(r'^\*\*\d+\.', se, re.M)); cf = len(re.findall(r'^\*\*[\d۰-۹]+\.', sf, re.M))
            if ce != cf:
                err(f'solutions: {cf} numbered solutions, English has {ce}')
        if f'solutions/{name}' not in t:
            err('no link to the solutions file')
    for src, tr, what in pairs:
        d_en, i_en = maths(src); d_fa, i_fa = maths(tr)
        if d_en != d_fa:
            k = next((i for i, (a, b) in enumerate(zip(d_en, d_fa)) if a != b), min(len(d_en), len(d_fa)))
            err(f'{what}: displayed formulas differ from English ({len(d_fa)} vs {len(d_en)}; first difference at block {k + 1}: '
                f'{(d_fa[k] if k < len(d_fa) else "-")[:60]!r} vs {(d_en[k] if k < len(d_en) else "-")[:60]!r})')
        missing, extra = i_en - i_fa, i_fa - i_en
        if missing or extra:
            err(f'{what}: inline formulas differ from English; missing {list(missing.elements())[:4]}, extra {list(extra.elements())[:4]}')
        prose = strip_math(tr)
        for k in sorted(refs(prose)):
            if k == n or k == 0:
                continue
            if k > n:
                err(f'{what}: refers to later جلسهٔ {fa(k)}')
            elif k not in closure[n]:
                warn(f'{what}: refers to جلسهٔ {fa(k)}, which is not among its prerequisites')
        for b in BANNED:
            if b in prose:
                err(f'{what}: banned phrase «{b}»')
        for i, l in enumerate(tr.splitlines(), 1):
            if '$$' in l and l.strip() != '$$':
                err(f'{what} line {i}: "$$" must stand on a line of its own')
        plain = re.sub(r'`[^`]*`|\]\([^)]*\)|\([^()]*[A-Za-z][^()]*\)|\*[^*]*\*', ' ', prose)
        for l in plain.splitlines():
            if re.search(r'(?:\b[A-Za-z][A-Za-z\'-]+\b[ ,;:]+){6,}', l):
                warn(f'{what}: English left untranslated? {l.strip()[:70]!r}')
                break
        if re.search(r'\bSessions?\s+\d', prose):
            err(f'{what}: English "Session N" reference left in the text')

for w in warnings: print('WARNING:', w)
for e in errors: print('ERROR:', e)
print(f'checked {checked} Farsi session file(s): {len(errors)} errors, {len(warnings)} warnings')
sys.exit(1 if errors else 0)
