"use strict";

const CACHE_NAME = 'static_machaneh_cache_v1.0.0';

const CACHE_FILES = [
  "/",
  "/index.html",
  "DAG.jpg",
  "favicon.ico"
];


self.addEventListener("install", evt => {
  console.log("[ServiceWorker] install");
  evt.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      cosole.log("[ServiceWorker] caching");
      return cache.addAll(CACHE_FILES);
    })
  );
  self.skipWaiting();
});


self.addEventListener("activate", evt => {
  console.log("[ServiceWorker] activate");
  evt.waitUntil(
    caches.keys().then(keyList => {
      return Promise.all(
        keyList.map(key => {
	  if (key != CACHE_NAME) {
	    console.log("[ServiceWorker] cleaning up old caches", key);
            caches.delete(key);
	  }
	})
      );
    }) 
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
    event.respondWith(
	    caches.match(event.request).then(response => {
		return response || fetch(event.request);
	    })
	);
});
