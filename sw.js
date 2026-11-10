// Service worker for the offline reader.
//
// The book's own files (index.html, book.json, the syllabus, the sessions and
// their solutions) are network-first: the book is still being written, so an
// online reader should see the latest deploy. On a slow connection, though, a
// saved copy is served after TIMEOUT ms, and the network response still
// updates the cache for the next visit.
//
// Version-pinned files (vendor/katex-*, vendor/marked-*, Google Fonts) are
// cache-first: once cached they never need refetching. Bump CACHE only when
// those versions change.
const CACHE = 'qm-book-v2';
const TIMEOUT = 4000;

const SHELL = [
  './',
  'index.html',
  'book.json',
  'fa/book.json',
  'vendor/katex-0.16.11/katex.min.css',
  'vendor/katex-0.16.11/katex.min.js',
  'vendor/marked-12.0.2/marked.min.js',
];

const FONTS = [
  'https://fonts.googleapis.com/css2?family=STIX+Two+Text:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=JetBrains+Mono:wght@400;500&family=Vazirmatn:wght@400;500;600;700&display=swap',
];

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(CACHE);
    await c.addAll(SHELL);
    await Promise.all(FONTS.map(async (u) => {
      try {
        const res = await fetch(u);
        if (res.ok) await c.put(u, res);
      } catch {}
    }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const pinned = url.origin !== self.location.origin || url.pathname.includes('/vendor/');
  e.respondWith(pinned ? cacheFirst(req) : networkFirst(req, e));
});

// The cache write is awaited so that once the page has a response, the file
// is guaranteed to be in Cache Storage — the "Save for offline" button relies
// on that to verify each download.
async function store(req, res) {
  try { await (await caches.open(CACHE)).put(req, res); } catch {}
}

function networkFirst(req, event) {
  // {cache: 'reload'} skips the HTTP cache, which on GitHub Pages would
  // otherwise serve a copy up to ten minutes old.
  const network = fetch(req, { cache: 'reload' }).then(async (res) => {
    if (res.ok) await store(req, res.clone());
    return res;
  });
  event.waitUntil(network.catch(() => {}));
  const cached = caches.match(req, { ignoreSearch: true });
  // A saved copy answers if the network is slower than TIMEOUT; without one,
  // the network is awaited however long it takes.
  const slow = new Promise((resolve) => setTimeout(resolve, TIMEOUT)).then(() => cached).then((c) => c || network);
  return Promise.race([network, slow]).catch(async (err) => {
    const c = await cached;
    if (c) return c;
    if (req.mode === 'navigate') {
      const fallback = await caches.match('index.html');
      if (fallback) return fallback;
    }
    throw err;
  });
}

async function cacheFirst(req) {
  const cached = await caches.match(req);
  if (cached) return cached;
  const res = await fetch(req);
  if (res.ok || res.type === 'opaque') await store(req, res.clone());
  return res;
}
