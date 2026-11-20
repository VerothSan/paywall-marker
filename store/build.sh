#!/usr/bin/env bash
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker)
# Baut alles für den Chrome Web Store:
#   dist/paywall-marker-<version>.zip   – Upload-Paket (nur Erweiterungsdateien)
#   dist/store/*.png                    – Screenshots 1280x800 und Werbebild 440x280 (EN/DE)
# Voraussetzungen: python3, firefox, ImageMagick (magick), zip
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$PWD"
VERSION=$(python3 -c 'import json;print(json.load(open("manifest.json"))["version"])')
mkdir -p dist/store

# 1) Einstellungsseite als eigenständige Vorschau (Chrome-APIs simuliert), je Sprache
python3 - <<'EOF'
import json
html = open("options/options.html", encoding="utf8").read()
i18n = open("src/i18n.js", encoding="utf8").read()
opt = open("options/options.js", encoding="utf8").read()
defaults = 'const DEFAULT_SETTINGS={language:"auto",dimPaywalled:true,hidePaywalled:false,showFreeBadge:true,alwaysPaywall:[],alwaysFree:[]};'
opt = opt.replace('import { DEFAULT_SETTINGS } from "../src/settings.js";', defaults)
for lang in ("en", "de"):
    store = {"language": lang, "alwaysPaywall": ["faz.net", "zeit.de"], "alwaysFree": ["tagesschau.de", "br.de", "n-tv.de"]}
    mock = ("window.__store=" + json.dumps(store) + ";window.chrome={storage:{sync:{get:async d=>({...d,...window.__store}),"
            "set:async o=>Object.assign(window.__store,o)}},runtime:{sendMessage:async()=>({ok:true})}};")
    out = html.replace('<script src="../src/i18n.js"></script>', "<script>" + i18n + "</script>")
    out = out.replace('<script type="module" src="options.js"></script>', "<script>" + mock + "</script><script type=\"module\">" + opt + "</script>")
    out = out.replace("max-width: 640px; margin: 32px auto;", "max-width: 640px; margin: 20px auto;")
    open(f"dist/preview_options_{lang}.html", "w", encoding="utf8").write(out)
EOF

# 2) Bilder mit Firefox headless rendern (eigenes Wegwerf-Profil, stört kein offenes Firefox)
PROFILE=$(mktemp -d)
trap 'rm -rf "$PROFILE"' EXIT
shot() { # $1=motiv $2=breite $3=höhe $4=ausgabe
  firefox --headless --no-remote --profile "$PROFILE" --window-size="$2,$3" \
    --screenshot "$ROOT/$4" "file://$ROOT/store/screens.html#$1" >/dev/null 2>&1  # Firefox braucht absoluten Pfad
  # Store verlangt 24-Bit-Bilder ohne Alphakanal
  magick "$4" -background white -alpha remove -alpha off -resize "$2x$3!" -depth 8 "PNG24:$4"
}
for lang in en de; do
  shot "$lang-feed"     1280 800 "dist/store/screenshot-1-feed-$lang.png"
  shot "$lang-settings" 1280 800 "dist/store/screenshot-2-settings-$lang.png"
  shot "$lang-promo"     440 280 "dist/store/promo-small-440x280-$lang.png"
done

# 3) Upload-Paket: nur was die Erweiterung zur Laufzeit braucht + LICENSE.md
#    (die Lizenz verlangt, dass jede weitergegebene Kopie den Lizenztext enthält)
ZIP="dist/paywall-marker-$VERSION.zip"
rm -f "$ZIP"
zip -qr -X "$ZIP" LICENSE.md manifest.json _locales src options icons/icon-16.png icons/icon-32.png icons/icon-48.png icons/icon-128.png
echo "Fertig: $ZIP"; ls -la dist/store
