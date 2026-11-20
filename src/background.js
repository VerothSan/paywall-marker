// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker)
// Service Worker: lädt Artikel-HTML, prüft auf Paywall, cached das Ergebnis.
import { analyzeHtml, analyzeUrl, looksLikeChallenge, hostOf, matchesDomain } from "./detect.js";
import { DEFAULT_SETTINGS, CACHE_TTL_MS } from "./settings.js";

const MAX_PARALLEL = 4;
const FETCH_TIMEOUT_MS = 12000;

let running = 0;
const queue = [];
const inflight = new Map(); // url → Promise (Doppelabfragen vermeiden)

async function getSettings() {
  const s = await chrome.storage.sync.get(DEFAULT_SETTINGS);
  return { ...DEFAULT_SETTINGS, ...s };
}

// Präfix "c2:" – Einträge älterer Versionen (deutsche Freitext-Gründe) werden
// so ignoriert statt falsch angezeigt.
function cacheKey(url) {
  // Tracking-Parameter entfernen, damit gleiche Artikel denselben Eintrag treffen
  try {
    const u = new URL(url);
    [...u.searchParams.keys()].forEach((k) => /^(utm_|at_|wt_|ref|cid)/i.test(k) && u.searchParams.delete(k));
    u.hash = "";
    return "c2:" + u.toString();
  } catch {
    return "c2:" + url;
  }
}

async function readCache(url) {
  const key = cacheKey(url);
  const entry = (await chrome.storage.local.get(key))[key];
  if (!entry) return null;
  const ttl = entry.status === "unknown" ? CACHE_TTL_MS.unknown : CACHE_TTL_MS.definite;
  return Date.now() - entry.ts < ttl ? entry : null;
}

async function writeCache(url, result) {
  await chrome.storage.local.set({ [cacheKey(url)]: { ...result, ts: Date.now() } });
}

function schedule(task) {
  return new Promise((resolve, reject) => {
    queue.push({ task, resolve, reject });
    pump();
  });
}

function pump() {
  while (running < MAX_PARALLEL && queue.length) {
    const { task, resolve, reject } = queue.shift();
    running++;
    task()
      .then(resolve, reject)
      .finally(() => {
        running--;
        pump();
      });
  }
}

async function fetchAndAnalyze(url) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
  try {
    // credentials: "include" → vorhandene Cookies (z. B. Consent, bestandene
    // Bot-Prüfung) werden mitgeschickt; das erhöht die Trefferquote deutlich.
    const res = await fetch(url, { credentials: "include", redirect: "follow", signal: ctrl.signal });
    const html = await res.text();
    // Weiterleitung auf eine Cookie-Zustimmungsseite (z. B. golem.de): Nach einem
    // normalen Besuch inkl. Zustimmung schickt fetch das Cookie mit und es klappt.
    if (/\/(zustimmung|consent|privacy-gate|cmp)\b/i.test(new URL(res.url).pathname)) {
      return { status: "unknown", reason: "r_consent" };
    }
    if (looksLikeChallenge(html, res.status)) {
      return analyzeUrl(res.url) || { status: "unknown", reason: "r_blocked", detail: `HTTP ${res.status}` };
    }
    return analyzeHtml(html, res.url);
  } catch (e) {
    return { status: "unknown", reason: e.name === "AbortError" ? "r_timeout" : "r_fetch_failed" };
  } finally {
    clearTimeout(timer);
  }
}

/** Domain-Listen nur als Fallback: Ein eindeutiges Signal vom Artikel selbst
 *  ist genauer als eine Pauschalregel pro Verlag (viele mischen frei/Plus). */
async function applyFallbackLists(url, result) {
  // Auch bei "likelyFree": Das ist nur eine Vermutung, deine Listen wissen es besser.
  if (result.status !== "unknown" && result.status !== "likelyFree") return result;
  const settings = await getSettings();
  const host = hostOf(url);
  if (settings.alwaysPaywall.some((d) => matchesDomain(host, d)))
    return { status: "paywall", reason: "r_list_paywall", base: result };
  if (settings.alwaysFree.some((d) => matchesDomain(host, d)))
    return { status: "free", reason: "r_list_free", base: result };
  return result;
}

async function detect(url) {
  const cached = await readCache(url);
  if (cached) return cached;

  if (inflight.has(url)) return inflight.get(url);
  const p = schedule(() => fetchAndAnalyze(url))
    .then(async (r) => {
      await writeCache(url, r);
      return r;
    })
    .finally(() => inflight.delete(url));
  inflight.set(url, p);
  return p;
}

async function check(url) {
  // Cache enthält das Roh-Ergebnis der Erkennung; Listen werden immer frisch
  // angewendet, damit Änderungen in den Einstellungen sofort wirken.
  return applyFallbackLists(url, await detect(url));
}

chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg?.type === "check" && typeof msg.url === "string" && /^https?:\/\//.test(msg.url)) {
    check(msg.url).then(sendResponse, () => sendResponse({ status: "unknown", reason: "r_internal" }));
    return true; // asynchrone Antwort
  }
  if (msg?.type === "clearCache") {
    chrome.storage.local.clear().then(() => sendResponse({ ok: true }));
    return true;
  }
});

chrome.action.onClicked.addListener(() => chrome.runtime.openOptionsPage());

// Beim Update: Cache-Einträge älterer Versionen ("c:"-Präfix) entfernen.
chrome.runtime.onInstalled?.addListener(async () => {
  const all = await chrome.storage.local.get(null);
  const old = Object.keys(all).filter((k) => k.startsWith("c:"));
  if (old.length) await chrome.storage.local.remove(old);
});
