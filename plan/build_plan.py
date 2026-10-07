"""Render 01-writing-plan.md: resolve [[slug]] to session numbers and append session notes."""
import json, re, sys
src, tmpl, out = sys.argv[1:4]
num, notes, n, part = {}, [], 0, None
for line in open(src, encoding='utf-8'):
    o = json.loads(line)
    if o['type'] != 'session':
        part = o['id']; continue
    n += 1; num[o['slug']] = n
    if o.get('note', '').strip():
        notes.append(f"- **{part}.{n}. {o['title']}.** {o['note'].strip()}")
text = open(tmpl, encoding='utf-8').read()
missing = []
def sub(m):
    s = m.group(1)
    if s not in num: missing.append(s); return m.group(0)
    return str(num[s])
text = re.sub(r'\[\[([a-z0-9-]+)\]\]', sub, text).replace('<<NOTES>>', '\n'.join(notes))
if missing: raise SystemExit(f'unresolved: {missing}')
open(out, 'w', encoding='utf-8').write(text)
print(f'{out}: {len(text.split())} words, {len(notes)} session notes')
