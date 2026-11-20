# Chrome Web Store – Texte zum Einfügen

Alles, was im Entwickler-Dashboard (https://chrome.google.com/webstore/devconsole) abgefragt wird, in der Reihenfolge der Reiter.
Bilder: `dist/store/` (erzeugt mit `store/build.sh`). Upload-Paket: `dist/paywall-marker-<version>.zip`.

---

## Reiter „Paket“

ZIP hochladen: `dist/paywall-marker-1.2.0.zip`

## Reiter „Store-Eintrag“

| Feld                        | Wert                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| Name                        | kommt aus dem Paket: **Paywall-Marker**                                                    |
| Kurzbeschreibung            | kommt aus dem Paket (`_locales`, 16 Sprachen)                                              |
| Kategorie                   | **Nachrichten & Wetter** (News & Weather)                                                  |
| Sprache (Hauptsprache)      | Englisch, zusätzlich Deutsch als lokalisierter Eintrag                                     |
| Store-Symbol 128×128        | `icons/icon-128.png`                                                                       |
| Screenshots (1280×800)      | `dist/store/screenshot-1-feed-<en/de>.png`, `dist/store/screenshot-2-settings-<en/de>.png` |
| Kleines Werbebild (440×280) | `dist/store/promo-small-440x280-<en/de>.png`                                               |
| Offizielle URL / Website    | https://verothsan.github.io/paywall-marker/                                                |
| Support-URL                 | https://github.com/VerothSan/paywall-marker/issues                                         |

### Ausführliche Beschreibung – English

```
Know before you click.

Paywall-Marker adds a small tag to every article in your Google News feed that tells you whether it is free to read or behind a paywall – so you no longer open articles you can't read.

TAGS
🔒 Paywall – the publisher marks the article as paid content
⏳ Metered – a few articles are free, then a subscription is required
✓ free – the publisher marks the article as free
✓? free – marked up as an article, but without any paywall marking (probably free)
? unclear – the site blocks automated checks or has no markup at all
Hover over a tag to see why it was chosen.

HOW IT WORKS
Publishers that use a paywall mark their articles in a machine-readable way so search engines can handle them correctly (schema.org "isAccessibleForFree" and "article:content_tier"). Paywall-Marker fetches the articles visible in your feed and reads exactly this marking. Nothing is bypassed or unlocked – the extension only reads what publishers state themselves.

FEATURES
• Dim or completely hide paywalled articles
• Your own fallback lists for sites that block automated checks
• Results are cached locally to avoid repeated requests
• Only articles currently visible are checked
• 16 languages: English, Deutsch, Español, Français, Português, Українська, 日本語, Norsk, Svenska, Suomi, Dansk, Italiano, Nederlands, Polski, Čeština, Hrvatski

PRIVACY
No tracking, no analytics, no server of our own. Everything is processed and stored locally in your browser. The source code is public.
Privacy policy: https://verothsan.github.io/paywall-marker/privacy.html
Source code: https://github.com/VerothSan/paywall-marker (PolyForm Noncommercial 1.0.0 – free for noncommercial use)

Not affiliated with Google. Google News is a trademark of Google LLC.
```

### Ausführliche Beschreibung – Deutsch

```
Wissen, bevor du klickst.

Paywall-Marker setzt im Google-News-Feed vor jeden Artikel eine kleine Markierung, die zeigt, ob er frei lesbar ist oder hinter einer Paywall liegt – damit du keine Artikel mehr öffnest, die du nicht lesen kannst.

MARKIERUNGEN
🔒 Paywall – der Verlag kennzeichnet den Artikel als kostenpflichtig
⏳ Zähler – einige Artikel sind gratis, danach braucht es ein Abo
✓ frei – der Verlag kennzeichnet den Artikel als frei
✓? frei – als Artikel ausgezeichnet, aber ohne Paywall-Kennzeichnung (wahrscheinlich frei)
? unklar – die Seite blockt die automatische Prüfung oder hat gar keine Auszeichnung
Mit der Maus auf eine Markierung zeigen, um den Grund zu sehen.

SO FUNKTIONIERT ES
Verlage mit Paywall kennzeichnen ihre Artikel maschinenlesbar, damit Suchmaschinen sie richtig behandeln (schema.org „isAccessibleForFree“ und „article:content_tier“). Paywall-Marker lädt die im Feed sichtbaren Artikel und liest genau diese Kennzeichnung. Es wird nichts umgangen oder freigeschaltet – die Erweiterung liest nur, was die Verlage selbst angeben.

FUNKTIONEN
• Paywall-Artikel abblenden oder komplett ausblenden
• Eigene Fallback-Listen für Seiten, die die automatische Prüfung blocken
• Ergebnisse werden lokal zwischengespeichert, um wiederholte Abrufe zu vermeiden
• Geprüft werden nur gerade sichtbare Artikel
• 16 Sprachen: Deutsch, English, Español, Français, Português, Українська, 日本語, Norsk, Svenska, Suomi, Dansk, Italiano, Nederlands, Polski, Čeština, Hrvatski

DATENSCHUTZ
Kein Tracking, keine Statistiken, kein eigener Server. Alles wird lokal in deinem Browser verarbeitet und gespeichert. Der Quellcode ist öffentlich.
Datenschutzerklärung: https://verothsan.github.io/paywall-marker/privacy.html
Quellcode: https://github.com/VerothSan/paywall-marker (PolyForm Noncommercial 1.0.0 – frei für nicht-kommerzielle Nutzung)

Keine Verbindung zu Google. Google News ist eine Marke von Google LLC.
```

---

## Reiter „Datenschutz“ (Privacy practices)

### Einziger Zweck (Single purpose)

```
Marks articles in the Google News feed as paywalled, metered or free by reading the paywall marking (schema.org isAccessibleForFree / article:content_tier) that publishers put into their own article pages.
```

### Begründung je Berechtigung

**storage**
```
Stores the user's settings (language, display options, fallback domain lists) and a local cache of check results per article URL, so the same article is not fetched repeatedly. Nothing leaves the browser.
```

**Host permission `<all_urls>`**
```
Articles in the Google News feed link to arbitrary publisher websites. To determine whether an article is behind a paywall, the extension's service worker fetches the linked article page and reads the paywall marking the publisher declares in it (schema.org isAccessibleForFree, article:content_tier). The list of publishers is open-ended, so access cannot be limited to fixed domains. Only articles currently visible in the feed are fetched; page content is analyzed in memory and discarded. The content script itself runs only on https://news.google.com/*, where it inserts the tags. No other website is modified.
```

### Remote-Code

```
No, I am not using remote code.
```
(Alle Skripte liegen im Paket. Es wird kein Code nachgeladen oder per eval ausgeführt.)

### Datennutzung (Data usage)

Ankreuzen:
- [x] **Website content** – Begründung: Artikelseiten werden abgerufen und lokal auf die Paywall-Kennzeichnung geprüft. Ehrlich angegeben ist sicherer als zu wenig. Die Daten verlassen das Gerät nicht in Richtung Entwickler.
- Alle anderen Kategorien (personenbezogene Daten, Gesundheit, Finanzen, Authentifizierung, Kommunikation, Standort, Webverlauf, Nutzeraktivität): **nicht** ankreuzen.

Alle drei Bestätigungen ankreuzen:
- [x] I do not sell or transfer user data to third parties, outside of the approved use cases
- [x] I do not use or transfer user data for purposes that are unrelated to my item's single purpose
- [x] I do not use or transfer user data to determine creditworthiness or for lending purposes

### Datenschutzerklärung (URL)

```
https://verothsan.github.io/paywall-marker/privacy.html
```

---

## Reiter „Vertrieb“ (Distribution)

| Feld | Empfehlung |
|---|---|
| Preis | Kostenlos |
| Sichtbarkeit | Öffentlich (oder erst „Nicht gelistet“ zum Testen) |
| Regionen | Alle |

## Hinweise für die Prüfer (Test instructions, optional)

```
No account or login needed.
1. Install the extension and open https://news.google.com/
2. Tags appear above article headlines within a few seconds (only for articles visible on screen).
3. Hover over a tag to see the reason (e.g. "Publisher marks it as paid (isAccessibleForFree: false)").
4. Click the toolbar icon to open the settings (language, dim/hide, fallback lists).
Note: some publishers block automated requests; those articles show "? unclear". This is expected.
```

## Konto (einmalig, nur du)

- Google-Konto mit Bestätigung in zwei Schritten
- Registrierung als Entwickler: einmalig 5 US-Dollar
- Händlerstatus: für ein kostenloses Hobby-Projekt „kein Händler“ (Non-trader)
