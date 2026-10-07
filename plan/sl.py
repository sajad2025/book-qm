"""Safe edits to a session list in JSON Lines form (see validate.py for the format).

Use from Python:
    import sys; sys.path.insert(0, '<dir of this file>'); import sl
    db = sl.load('sessions.jsonl')
    sl.set_field(db, 'slug', 'establishes', 'new text')
    sl.add_uses(db, 'slug', ['earlier-slug'])
    sl.remove_uses(db, 'slug', ['some-slug'])
    sl.insert(db, {...session dict...}, after='slug')        # or before='slug'
    sl.delete(db, 'slug', redirect='other-slug')             # citations of slug become citations of redirect
    sl.merge(db, keep='slug-a', absorb='slug-b', **fields)   # absorb disappears; its citations move to keep
    sl.move(db, 'slug', after='other-slug')                  # or before=...
    sl.rename(db, 'old-slug', 'new-slug')
    sl.save(db, 'sessions.jsonl', log='changes.log', note='why')   # validates first; refuses to save if invalid
Every operation raises on a bad slug. save() refuses to write a list with forward references.
"""
import json, re

KINDS = {'definition', 'theorem', 'construction', 'calculation', 'example', 'experiment', 'survey', 'problems'}

def load(path):
    items = []
    for line in open(path, encoding='utf-8'):
        line = line.strip()
        if line:
            items.append(json.loads(line))
    return items

def _sessions(db):
    return [o for o in db if o['type'] == 'session']

def _index(db, slug):
    for i, o in enumerate(db):
        if o['type'] == 'session' and o['slug'] == slug:
            return i
    raise KeyError(f'no session {slug!r}')

def get(db, slug):
    return db[_index(db, slug)]

def number(db, slug):
    n = 0
    for o in db:
        if o['type'] == 'session':
            n += 1
            if o['slug'] == slug:
                return n
    raise KeyError(slug)

def set_field(db, slug, field, value):
    if field in ('slug', 'type'):
        raise ValueError('use rename()')
    get(db, slug)[field] = value

def add_uses(db, slug, uses):
    s = get(db, slug)
    for u in uses:
        get(db, u)
        if u not in s['uses']:
            s['uses'].append(u)

def remove_uses(db, slug, uses):
    s = get(db, slug)
    s['uses'] = [u for u in s['uses'] if u not in uses]

def _check_new(o):
    for k in ('slug', 'title', 'establishes', 'kind', 'uses', 'tags', 'size'):
        if k not in o:
            raise ValueError(f'new session missing {k}')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', o['slug']):
        raise ValueError(f'bad slug {o["slug"]!r}')
    if o['kind'] not in KINDS:
        raise ValueError(f'bad kind {o["kind"]!r}')
    o.setdefault('gap', '')
    o['type'] = 'session'

def insert(db, o, after=None, before=None):
    _check_new(o)
    if any(x['type'] == 'session' and x['slug'] == o['slug'] for x in db):
        raise ValueError(f'slug exists: {o["slug"]}')
    if (after is None) == (before is None):
        raise ValueError('give exactly one of after= or before=')
    i = _index(db, after) + 1 if after else _index(db, before)
    db.insert(i, o)

def insert_part(db, part, before_slug):
    for k in ('id', 'title', 'goal'):
        if k not in part:
            raise ValueError(f'part missing {k}')
    part['type'] = 'part'
    db.insert(_index(db, before_slug), part)

def delete(db, slug, redirect=None):
    i = _index(db, slug)
    del db[i]
    for s in _sessions(db):
        if slug in s['uses']:
            s['uses'] = [u for u in s['uses'] if u != slug]
            if redirect and redirect not in s['uses'] and redirect != s['slug']:
                s['uses'].append(redirect)

def merge(db, keep, absorb, **fields):
    a = get(db, absorb)
    k = get(db, keep)
    for u in a['uses']:
        if u not in k['uses'] and u != keep:
            k['uses'].append(u)
    for f, v in fields.items():
        k[f] = v
    delete(db, absorb, redirect=keep)

def move(db, slug, after=None, before=None):
    o = db.pop(_index(db, slug))
    if (after is None) == (before is None):
        raise ValueError('give exactly one of after= or before=')
    i = _index(db, after) + 1 if after else _index(db, before)
    db.insert(i, o)

def rename(db, old, new):
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', new):
        raise ValueError(f'bad slug {new!r}')
    get(db, old)['slug'] = new
    for s in _sessions(db):
        s['uses'] = [new if u == old else u for u in s['uses']]

def problems(db):
    errs, seen, num = [], set(), {}
    n = 0
    if not db or db[0]['type'] != 'part':
        errs.append('first line must be a part')
    for o in db:
        if o['type'] != 'session':
            continue
        n += 1
        if o['slug'] in seen:
            errs.append(f'duplicate slug {o["slug"]}')
        seen.add(o['slug']); num[o['slug']] = n
    for o in _sessions(db):
        for u in o['uses']:
            if u not in num:
                errs.append(f'{o["slug"]} uses unknown {u}')
            elif num[u] >= num[o['slug']]:
                errs.append(f'{o["slug"]} ({num[o["slug"]]}) uses later {u} ({num[u]})')
    return errs

def save(db, path, log=None, note=''):
    errs = problems(db)
    if errs:
        raise ValueError('not saved; invalid list:\n' + '\n'.join(errs[:30]))
    with open(path, 'w', encoding='utf-8') as f:
        for o in db:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    if log:
        with open(log, 'a', encoding='utf-8') as f:
            f.write(note.rstrip() + '\n')
    return len(_sessions(db))
