// SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
// Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker)
import { DEFAULT_SETTINGS } from "../src/settings.js";

const I18N = globalThis.PWM_I18N; // aus ../src/i18n.js (klassisches Skript davor)
const $ = (id) => document.getElementById(id);
const BOOLS = ["dimPaywalled", "hidePaywalled", "showFreeBadge"];
const LISTS = ["alwaysPaywall", "alwaysFree"];

let lang = I18N.resolve("auto");

let flashTimer = null;
function flash(key) {
  // Alten Timer stoppen, sonst blendet ein früherer Klick die neue Meldung zu früh aus.
  clearTimeout(flashTimer);
  $("status").textContent = I18N.t(lang, key);
  flashTimer = setTimeout(() => ($("status").textContent = ""), 2000);
}

/** Alle Texte der Seite in der gewählten Sprache setzen. */
function applyTexts(setting) {
  lang = I18N.resolve(setting);
  document.documentElement.lang = lang;
  for (const el of document.querySelectorAll("[data-i18n]")) el.textContent = I18N.t(lang, el.dataset.i18n);

  // Sprachliste: jeder Name in seiner eigenen Sprache (Endonym), damit man
  // auch aus einer unverständlichen Oberfläche heraus zurückfindet.
  // "Automatisch" in der aktuellen Sprache + erkannte Browsersprache.
  const sel = $("language");
  sel.setAttribute("aria-label", I18N.t(lang, "o_language"));
  const browser = I18N.fromBrowser();
  sel.replaceChildren(
    new Option(`${I18N.t(lang, "o_auto")} (${I18N.LANGS[browser].name})`, "auto"),
    ...Object.entries(I18N.LANGS).map(([code, l]) => {
      const o = new Option(l.name, code);
      o.lang = code;
      return o;
    })
  );
  sel.value = setting;
}

async function load() {
  const s = { ...DEFAULT_SETTINGS, ...(await chrome.storage.sync.get(DEFAULT_SETTINGS)) };
  applyTexts(s.language);
  BOOLS.forEach((k) => ($(k).checked = !!s[k]));
  LISTS.forEach((k) => ($(k).value = s[k].join("\n")));
}

// Sprache wird sofort übernommen (Seite und Google-News-Tags), ohne "Speichern".
$("language").addEventListener("change", async (e) => {
  const value = e.target.value;
  applyTexts(value);
  await chrome.storage.sync.set({ language: value });
  flash("o_saved");
});

$("save").addEventListener("click", async () => {
  const data = {};
  BOOLS.forEach((k) => (data[k] = $(k).checked));
  LISTS.forEach(
    (k) =>
      (data[k] = $(k)
        .value.split(/[\s,]+/)
        .map((d) => d.trim().toLowerCase().replace(/^https?:\/\//, "").replace(/\/.*$/, "").replace(/^www\./, ""))
        .filter(Boolean))
  );
  await chrome.storage.sync.set(data);
  flash("o_saved");
});

$("clear").addEventListener("click", async () => {
  await chrome.runtime.sendMessage({ type: "clearCache" });
  flash("o_cleared");
});

load();
