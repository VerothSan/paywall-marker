// Content Script für news.google.com: findet Artikel, ermittelt die echte URL,
// fragt den Service Worker nach dem Paywall-Status und markiert den Artikel.
(() => {
  "use strict";

  const SETTINGS_DEFAULTS = { dimPaywalled: true, hidePaywalled: false, showFreeBadge: true, language: "auto" };
  let settings = { ...SETTINGS_DEFAULTS };
  const I18N = globalThis.PWM_I18N; // aus src/i18n.js (im Manifest davor geladen)
  let lang = I18N.resolve("auto");
  const t = (key) => I18N.t(lang, key);

  const ID_RE = /\/(?:read|articles)\/([A-Za-z0-9_-]{20,})/;
  const LINK_SEL = 'a[href*="/read/"], a[href*="/articles/"]';

  // Symbol + Schlüssel für Tag-Text und Tooltip-Titel (Übersetzung in i18n.js)
  const LABELS = {
    pending: { icon: "…", text: "lbl_pending", title: "ttl_pending" },
    paywall: { icon: "🔒", text: "lbl_paywall", title: "ttl_paywall" },
    metered: { icon: "⏳", text: "lbl_metered", title: "ttl_metered" },
    free: { icon: "✓", text: "lbl_free", title: "ttl_free" },
    likelyFree: { icon: "✓?", text: "lbl_free", title: "ttl_likelyFree" },
    unknown: { icon: "?", text: "lbl_unknown", title: "ttl_unknown" },
  };

  /** Grund-Code (+ technisches Detail, + Ursprungsgrund bei Listen) → Text. */
  function reasonText(r) {
    if (!r?.reason) return "";
    let s = t(r.reason);
    if (r.detail) s += ` (${r.detail})`;
    if (r.base) s += ` – ${reasonText(r.base)}`;
    return s;
  }

  const results = new Map(); // articleId → {status, reason, url}
  const requested = new Set(); // articleIds, für die schon eine Prüfung läuft

  // ---------- Echte Artikel-URL ermitteln ----------

  /** Google legt die Ziel-URL Base64-kodiert im jslog-Attribut ab ("5:<base64>"). */
  function urlFromJslog(a) {
    const m = (a.getAttribute("jslog") || "").match(/(?:^|;)\s*5:([A-Za-z0-9+/=_-]+)/);
    if (!m) return null;
    try {
      const b64 = m[1].replace(/-/g, "+").replace(/_/g, "/");
      const bytes = Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
      const arr = JSON.parse(new TextDecoder().decode(bytes));
      return (Array.isArray(arr) && arr.find((x) => typeof x === "string" && /^https?:\/\//.test(x))) || null;
    } catch {
      return null;
    }
  }

  /** Fallback: Google-eigene Auflösung über batchexecute (same-origin, daher ohne CORS-Probleme). */
  async function urlFromGoogle(id) {
    try {
      const page = await fetch(`/articles/${id}`, { credentials: "include" }).then((r) => r.text());
      // Regex statt DOMParser: Google News erzwingt Trusted Types, DOMParser wird dort blockiert.
      const sg = page.match(/data-n-a-sg="([^"]+)"/)?.[1];
      const ts = page.match(/data-n-a-ts="([^"]+)"/)?.[1];
      if (!sg || !ts) return null;
      const inner = JSON.stringify([
        "garturlreq",
        [["X", "X", ["X", "X"], null, null, 1, 1, "US:en", null, 1, null, null, null, null, null, 0, 1], "X", "X", 1, [1, 1, 1], 1, 1, null, 0, 0, null, 0],
        id,
        Number(ts),
        sg,
      ]);
      const body = "f.req=" + encodeURIComponent(JSON.stringify([[["Fbv4je", inner, null, "generic"]]]));
      const txt = await fetch("/_/DotsSplashUi/data/batchexecute", {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
        body,
      }).then((r) => r.text());
      const json = JSON.parse(txt.split("\n\n")[1]);
      return JSON.parse(json[0][2])[1] || null;
    } catch {
      return null;
    }
  }

  // ---------- DOM-Struktur ----------

  function idOf(a) {
    const m = (a.getAttribute("href") || "").match(ID_RE);
    return m ? m[1] : null;
  }

  /** Größter Container, der nur Links auf genau diesen Artikel enthält = die Karte. */
  function cardFor(link, id) {
    let el = link;
    while (el.parentElement && el.parentElement !== document.body) {
      const p = el.parentElement;
      const foreign = [...p.querySelectorAll(LINK_SEL)].some((a) => idOf(a) !== id);
      if (foreign) break;
      el = p;
    }
    return el;
  }

  /** Alle Artikel-Gruppen im aktuellen DOM einsammeln. */
  function collectArticles() {
    const groups = new Map();
    for (const a of document.querySelectorAll(LINK_SEL)) {
      const id = idOf(a);
      if (!id) continue;
      let g = groups.get(id);
      if (!g) groups.set(id, (g = { id, links: [], url: null }));
      g.links.push(a);
      g.url ||= urlFromJslog(a);
    }
    return groups;
  }

  // ---------- Darstellung ----------

  function render(group, result) {
    const label = LABELS[result.status] || LABELS.unknown;
    // Titel-Links = Links mit sichtbarem Text (der Overlay-Link ist leer)
    const titleLinks = group.links.filter((a) => a.textContent.trim().length > 0);
    for (const a of titleLinks) {
      let badge = a.previousElementSibling;
      if (!badge || !badge.classList?.contains("pwm-badge")) {
        badge = document.createElement("span");
        badge.className = "pwm-badge";
        a.before(badge);
      }
      // Nur schreiben, wenn sich etwas ändert – sonst triggert der
      // MutationObserver endlos neue Scans.
      const text = `${label.icon} ${t(label.text)}`;
      if (badge.textContent !== text) badge.textContent = text;
      badge.dataset.status = result.status;
      const why = reasonText(result);
      badge.title = `${t(label.title)}${why ? " – " + why : ""}${result.url ? "\n" + result.url : ""}`;
      badge.lang = lang;
      badge.hidden = (result.status === "free" || result.status === "likelyFree") && !settings.showFreeBadge;
    }
    const anchor = titleLinks[0] || group.links[0];
    if (anchor) {
      const card = cardFor(anchor, group.id);
      if (card.dataset.pwmStatus !== result.status) card.dataset.pwmStatus = result.status;
    }
  }

  function applyCardSettings() {
    document.documentElement.classList.toggle("pwm-dim", !!settings.dimPaywalled);
    document.documentElement.classList.toggle("pwm-hide", !!settings.hidePaywalled);
  }

  // ---------- Ablauf ----------

  async function process(group) {
    if (requested.has(group.id)) return;
    requested.add(group.id);
    render(group, { status: "pending" });

    const url = group.url || (await urlFromGoogle(group.id));
    if (!url) {
      const r = { status: "unknown", reason: "r_no_url" };
      results.set(group.id, r);
      return render(group, r);
    }
    let r;
    try {
      r = await chrome.runtime.sendMessage({ type: "check", url });
    } catch {
      r = { status: "unknown", reason: "r_unreachable" };
    }
    r = { ...r, url };
    results.set(group.id, r);
    // DOM kann sich inzwischen geändert haben → Gruppe frisch einsammeln
    render(collectArticles().get(group.id) || group, r);
  }

  // Nur sichtbare (bzw. bald sichtbare) Artikel prüfen → spart Anfragen.
  const io = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (!e.isIntersecting) continue;
        io.unobserve(e.target);
        const id = idOf(e.target);
        const g = id && collectArticles().get(id);
        if (g) process(g);
      }
    },
    { rootMargin: "600px 0px" }
  );

  const observed = new WeakSet();

  function scan() {
    for (const g of collectArticles().values()) {
      if (results.has(g.id)) {
        // Bereits bekannt (z. B. nach Neu-Rendern durch Google) → sofort zeichnen
        render(g, results.get(g.id));
        continue;
      }
      if (requested.has(g.id)) continue;
      const link = g.links[0];
      if (!observed.has(link)) {
        observed.add(link);
        io.observe(link);
      }
    }
  }

  let scanTimer = null;
  const mo = new MutationObserver((muts) => {
    // Eigene Badge-Änderungen ignorieren
    const own = (m) =>
      m.target.closest?.(".pwm-badge") ||
      (m.addedNodes.length > 0 && [...m.addedNodes].every((n) => n.classList?.contains("pwm-badge")));
    if (muts.every(own)) return;
    clearTimeout(scanTimer);
    scanTimer = setTimeout(scan, 300);
  });

  chrome.storage.sync.get(SETTINGS_DEFAULTS).then((s) => {
    settings = { ...SETTINGS_DEFAULTS, ...s };
    lang = I18N.resolve(settings.language);
    applyCardSettings();
    scan();
    mo.observe(document.body, { childList: true, subtree: true });
  });

  chrome.storage.onChanged.addListener((changes, area) => {
    if (area !== "sync") return;
    for (const [k, v] of Object.entries(changes)) if (k in SETTINGS_DEFAULTS) settings[k] = v.newValue;
    lang = I18N.resolve(settings.language);
    applyCardSettings();
    for (const g of collectArticles().values()) if (results.has(g.id)) render(g, results.get(g.id));
  });
})();
