// Gemeinsame Standard-Einstellungen für Hintergrund-Skript und Optionsseite.
export const DEFAULT_SETTINGS = {
  // "auto" = Browsersprache, sonst Sprachcode aus src/i18n.js (de, en, …)
  language: "auto",
  // Paywall-Artikel im Feed abblenden
  dimPaywalled: true,
  // Paywall-Artikel komplett ausblenden
  hidePaywalled: false,
  // Auch "frei"-Badges anzeigen (sonst nur Paywall/Zähler/unbekannt)
  showFreeBadge: true,
  // Fallback-Listen: greifen nur, wenn die automatische Erkennung kein
  // eindeutiges Ergebnis liefert ("unklar" oder "wahrscheinlich frei").
  // Domains, die dann als Paywall gelten
  alwaysPaywall: [],
  // Domains, die dann als frei gelten
  alwaysFree: ["tagesschau.de", "zdfheute.de", "sportschau.de", "ndr.de", "br.de", "wdr.de", "swr.de", "mdr.de", "rbb24.de", "deutschlandfunk.de"],
};

export const CACHE_TTL_MS = {
  definite: 7 * 24 * 3600 * 1000, // paywall/free/metered
  unknown: 2 * 3600 * 1000, // unknown/error → später erneut probieren
};
