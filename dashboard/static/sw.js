// sw.js
self.addEventListener('install', (e) => {
  console.log('[Service Worker] Install');
});

self.addEventListener('fetch', (e) => {
  // Deixa o navegador gerenciar as requisições normalmente
});