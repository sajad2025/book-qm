"""Validate a session list in JSON Lines form.

usage: python3 -I validate.py FILE.jsonl
Each line is one JSON object:
  {"type": "part", "id": "I", "title": "...", "goal": "..."}
  {"type": "session", "slug": "kebab-case", "title": "...", "establishes": "one sentence",
   "kind": "definition|theorem|construction|calculation|example|experiment|survey|problems",
   "uses": ["earlier-slug", ...], "tags": ["math"|"formalism"|"Q1"|"Q2"|"Q3"|"interpretation"|"meta"],
   "gap": "" or "what is omitted, why, and where a full proof is", "size": "S"|"M"|"L"}
Sessions belong to the most recent part line. Numbering is the order of session lines (01, 02, ...).
"""
import json, sys, re, collections

path = sys.argv[1]
parts, sessions, errors, warnings = [], [], [], []
for i, line in enumerate(open(path, encoding='utf-8'), 1):
    line = line.strip()
    if not line:
        continue
    try:
        o = json.loads(line)
    except Exception as e:
        errors.append(f'line {i}: not valid JSON ({e})'); continue
    t = o.get('type')
    if t == 'part':
        for k in ('id', 'title', 'goal'):
            if not o.get(k): errors.append(f'line {i}: part missing {k}')
        o['sessions'] = []; parts.append(o)
    elif t == 'session':
        if not parts: errors.append(f'line {i}: session before any part'); continue
        for k in ('slug', 'title', 'establishes', 'kind', 'uses', 'tags', 'size'):
            if k not in o: errors.append(f'line {i}: session missing {k}')
        o.setdefault('gap', ''); o['part'] = parts[-1]['id']; o['line'] = i
        sessions.append(o); parts[-1]['sessions'].append(o)
    else:
        errors.append(f'line {i}: unknown type {t!r}')

num = {}
for n, s in enumerate(sessions, 1):
    slug = s.get('slug', '')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', slug or ''):
        errors.append(f'session {n}: bad slug {slug!r}')
    if slug in num: errors.append(f'session {n}: duplicate slug {slug}')
    num[slug] = n; s['n'] = n
for s in sessions:
    for u in s.get('uses', []):
        if u not in num: errors.append(f"session {s['n']} ({s['slug']}): uses unknown slug {u}")
        elif num[u] >= s['n']: errors.append(f"session {s['n']} ({s['slug']}): uses later or same session {u} ({num[u]})")
    if s['n'] > 1 and not s.get('uses') and s.get('kind') not in ('survey',):
        warnings.append(f"session {s['n']} ({s['slug']}): uses nothing earlier")
    if s.get('size') not in ('S', 'M', 'L'): warnings.append(f"session {s['n']}: size should be S, M or L")

# Unused sessions (nothing later uses them) are fine at the end of a thread, but list them.
used = collections.Counter(u for s in sessions for u in s.get('uses', []))
never = [s for s in sessions if used[s['slug']] == 0]

print(f'{len(parts)} parts, {len(sessions)} sessions')
for p in parts:
    if p['sessions']:
        print(f"  Part {p['id']}: {p['title']} - sessions {p['sessions'][0]['n']}-{p['sessions'][-1]['n']} ({len(p['sessions'])})")
sizes = collections.Counter(s.get('size') for s in sessions)
print('sizes:', dict(sizes), '| gaps:', sum(1 for s in sessions if s.get('gap')))
print('sessions that nothing later uses:', len(never), '(' + ', '.join(str(s['n']) for s in never[:40]) + (' ...' if len(never) > 40 else '') + ')')
far = sorted(((s['n'] - num[u], s['n'], u) for s in sessions for u in s.get('uses', []) if u in num), reverse=True)[:8]
print('longest back-references (distance, session, uses):', far)
for w in warnings[:30]: print('WARNING:', w)
if len(warnings) > 30: print(f'... {len(warnings) - 30} more warnings')
for e in errors: print('ERROR:', e)
sys.exit(1 if errors else 0)
