"""Merge the translators' metadata files plan/fa/meta-*.json into plan/fa.json.

usage (from the book folder): python3 plan/merge_fa.py
plan/fa.json holds {"book": {...}, "parts": {id: {title, goal}}, "sessions": {slug: {title, claim, gap?}}}.
A file plan/fa/meta-book.json supplies "book" and "parts"; every other meta file maps slugs to entries.
Merged meta files are deleted. Later translations edit plan/fa.json directly.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
target = root / 'plan' / 'fa.json'
fa = json.loads(target.read_text(encoding='utf-8')) if target.exists() else {'book': {}, 'parts': {}, 'sessions': {}}
merged = []
for f in sorted((root / 'plan' / 'fa').glob('meta-*.json')):
    data = json.loads(f.read_text(encoding='utf-8'))
    if f.name == 'meta-book.json':
        fa['book'].update(data.get('book', {})); fa['parts'].update(data.get('parts', {}))
    else:
        for slug, entry in data.items():
            fa['sessions'].setdefault(slug, {}).update(entry)
    merged.append(f)
slugs = [json.loads(l)['slug'] for l in (root / 'plan' / 'sessions.jsonl').read_text(encoding='utf-8').splitlines() if l.strip() and '"type": "session"' in l]
unknown = sorted(set(fa['sessions']) - set(slugs))
if unknown:
    raise SystemExit(f'unknown slugs in Farsi metadata: {unknown[:10]}')
target.write_text(json.dumps(fa, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for f in merged:
    f.unlink()
missing = [s for s in slugs if not fa['sessions'].get(s, {}).get('title')]
print(f'plan/fa.json: {len(fa["sessions"])} sessions, {len(fa["parts"])} parts; merged {len(merged)} file(s); {len(missing)} sessions without a Farsi title')
