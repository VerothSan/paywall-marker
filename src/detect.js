// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker)
// Reine Analyse-Logik (ohne Chrome-APIs), damit sie auch per Node testbar ist.
//
// Ergebnis-Status:
//   "paywall"  – Artikel ist (ganz oder teilweise) kostenpflichtig
//   "metered"  – Zähler-Paywall: einige Artikel gratis, dann Abo
//   "free"       – frei lesbar (ausdrücklich gekennzeichnet)
//   "likelyFree" – Artikel ist als solcher ausgezeichnet, trägt aber keine
//                  Paywall-Kennzeichnung → vermutlich frei
//   "unknown"    – keine verlässlichen Signale gefunden
//
// "reason" ist ein sprachneutraler Code (Übersetzung in src/i18n.js),
// "detail" optional ein technischer Zusatz, der unübersetzt angezeigt wird.

const LD_JSON_RE = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;

/** Sucht rekursiv nach isAccessibleForFree in JSON-LD-Objekten. */
function collectAccessFlags(node, out) {
  if (Array.isArray(node)) {
    node.forEach((n) => collectAccessFlags(n, out));
  } else if (node && typeof node === "object") {
    for (const [k, v] of Object.entries(node)) {
      if (k === "isAccessibleForFree") {
        const s = String(v).trim().toLowerCase();
        if (s === "false") out.push(false);
        else if (s === "true") out.push(true);
      } else {
        collectAccessFlags(v, out);
      }
    }
  }
}

function accessFlagsFromLdJson(html) {
  const flags = [];
  let m;
  LD_JSON_RE.lastIndex = 0;
  while ((m = LD_JSON_RE.exec(html))) {
    try {
      collectAccessFlags(JSON.parse(m[1].trim()), flags);
    } catch {
      // Kaputtes JSON (kommt vor) → Regex-Fallback auf diesen Block
      const re = /"isAccessibleForFree"\s*:\s*"?(true|false)"?/gi;
      let r;
      while ((r = re.exec(m[1]))) flags.push(r[1].toLowerCase() === "true");
    }
  }
  return flags;
}

function metaContent(html, name) {
  const re = new RegExp(
    `<meta[^>]+(?:property|name)=["']${name}["'][^>]*content=["']([^"']*)["']` +
      `|<meta[^>]+content=["']([^"']*)["'][^>]*(?:property|name)=["']${name}["']`,
    "i"
  );
  const m = html.match(re);
  return m ? (m[1] ?? m[2] ?? "").trim().toLowerCase() : null;
}

/** URL-Muster, die bei manchen Verlagen eindeutig auf Plus-Artikel hinweisen. */
const URL_PATTERNS = [
  { re: /[?&]reduced=true/i, detail: "?reduced=true" },
  { re: /welt\.de\/(?:.*\/)?plus[0-9a-f]{16,}\//i, detail: "WELTplus" },
  { re: /\/(plus|bildplus|zplus)\//i, detail: "/plus/" },
];

export function analyzeUrl(url) {
  for (const p of URL_PATTERNS) if (p.re.test(url)) return { status: "paywall", reason: "r_url", detail: p.detail };
  return null;
}

/**
 * Analysiert das HTML eines Artikels.
 * @param {string} html
 * @param {string} finalUrl URL nach Weiterleitungen
 */
export function analyzeHtml(html, finalUrl = "") {
  const byUrl = analyzeUrl(finalUrl);
  if (byUrl) return byUrl;

  // 1) Schema.org – Google verlangt dieses Markup von Verlagen mit Paywall,
  //    daher das zuverlässigste Signal. Ein einziges "false" (z. B. in hasPart)
  //    bedeutet: ein Teil des Artikels ist gesperrt.
  const flags = accessFlagsFromLdJson(html);
  if (flags.includes(false)) return { status: "paywall", reason: "r_marked_paywall", detail: "isAccessibleForFree: false" };

  // 2) Open-Graph-Erweiterung article:content_tier (free | metered | locked)
  const tier = metaContent(html, "article:content_tier");
  if (tier === "locked") return { status: "paywall", reason: "r_marked_paywall", detail: "content_tier: locked" };
  if (tier === "metered") return { status: "metered", reason: "r_marked_metered", detail: "content_tier: metered" };

  if (flags.includes(true)) return { status: "free", reason: "r_marked_free", detail: "isAccessibleForFree: true" };
  if (tier === "free") return { status: "free", reason: "r_marked_free", detail: "content_tier: free" };

  // 3) Weitere, seltenere Kennzeichnungen
  const access = metaContent(html, "cXenseParse:recs:access") || metaContent(html, "access");
  if (access && /^(abo|paid|premium|subscription|subscriber)/.test(access))
    return { status: "paywall", reason: "r_marked_paywall", detail: `access: ${access}` };

  // 4) Seite ist als Artikel ausgezeichnet, aber ohne jede Paywall-Angabe.
  //    Verlage mit Paywall müssen das für Google kennzeichnen (sonst gilt es
  //    als Cloaking) – fehlt die Angabe, ist der Artikel also vermutlich frei.
  //    Bewusst eigener Status, weil es ein Schluss aus fehlenden Daten ist.
  if (hasArticleMarkup(html))
    return { status: "likelyFree", reason: "r_article_no_marker" };

  return { status: "unknown", reason: "r_no_marker" };
}

const ARTICLE_TYPE_RE =
  /"@type"\s*:\s*\[?\s*"(?:[A-Za-z]*Article|BlogPosting|LiveBlogPosting)"/;

/** JSON-LD vom Typ *Article/BlogPosting oder og:type=article vorhanden? */
function hasArticleMarkup(html) {
  let m;
  LD_JSON_RE.lastIndex = 0;
  while ((m = LD_JSON_RE.exec(html))) if (ARTICLE_TYPE_RE.test(m[1])) return true;
  return metaContent(html, "og:type") === "article";
}

/** Erkennt Bot-Schutz-/Challenge-Seiten statt eines Artikels. */
export function looksLikeChallenge(html, status) {
  if (status === 403 || status === 429 || status === 503) return true;
  if (html.length < 5000 && /centinel|captcha|challenge|cf-chl|Just a moment/i.test(html)) return true;
  return false;
}

export function hostOf(url) {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
}

/** true, wenn host == domain oder eine Subdomain davon ist. */
export function matchesDomain(host, domain) {
  domain = domain.trim().toLowerCase().replace(/^www\./, "");
  return !!domain && (host === domain || host.endsWith("." + domain));
}
