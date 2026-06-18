const CACHE = 'aicoper-v1';
const ASSETS = [
  '/','/index.html','/aggregate.html','/advocate.html','/diverge.html',
  '/eval.html','/os-eval.html','/scenes.html','/collaborate.html',
  '/payment.html','/referral.html','/assets/style.css','/manifest.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
