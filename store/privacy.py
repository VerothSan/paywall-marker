#!/usr/bin/env python3
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker)
"""Erzeugt docs/privacy.html (Datenschutzerklärung) aus den Texten unten.

Englisch steht zuerst und ist maßgeblich; danach folgen alle weiteren Sprachen der
Erweiterung in derselben Reihenfolge wie in src/i18n.js. Alle Sprachen nutzen
dieselbe Struktur (Schlüssel), damit keine Übersetzung einen Abschnitt auslässt.

Aufruf:  python3 store/privacy.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/VerothSan/paywall-marker"

# Reihenfolge = Reihenfolge auf der Seite. name = Sprachname in der eigenen Sprache.
L = {}

L["en"] = dict(name="English",
  title="Privacy Policy",
  updated="Last updated: November 20, 2026 · applies to the browser extension “Paywall-Marker” from version 1.2.0",
  binding="This policy is available in several languages. If the translations differ, the English version applies.",
  tldr_l="In short:", tldr="The extension collects no personal data, has no server of its own and shares nothing with the developer or third parties. Everything is processed and stored locally in your browser.",
  h_what="What the extension does",
  p_what="Paywall-Marker shows next to each article in the Google News feed (<code>news.google.com</code>) whether it is behind a paywall. To do so, it fetches the linked article pages directly from the publisher and reads the marking the publisher itself puts into the page (e.g. <code>isAccessibleForFree</code>).",
  h_data="What data is processed", th=("Data", "Purpose", "Where / how long"),
  rows=[("Addresses (URLs) of the articles visible in the Google News feed", "Fetch and check the article page", "Only in memory and in the local cache (see below)"),
        ("Content of the fetched article pages", "Read the paywall marking", "Briefly in memory only, never stored"),
        ("Check result per article URL (status, reason, time)", "Avoid repeated fetches", "Locally in the browser (<code>chrome.storage.local</code>), 2 hours to 7 days; “Clear cache” deletes everything immediately"),
        ("Your settings (language, display, your own domain lists)", "Remember settings", "In the browser (<code>chrome.storage.sync</code>). If Chrome Sync is enabled, Chrome syncs them across your devices via your Google account – a Chrome feature, not part of the extension.")],
  p_none="The extension does <strong>not</strong> collect usage statistics, use analytics or advertising services, read your browsing history, or load code from the internet.",
  h_conn="Connections to other services",
  conn_pub_l="Publisher websites:", conn_pub="For each article visible in the feed, your browser fetches the article page from the publisher, as if you briefly opened it. Cookies you already have for that site are sent along (e.g. a cookie consent you gave earlier). The publisher receives the usual technical data of a page request (e.g. IP address, browser identifier); the publisher’s own privacy policy applies to that data.",
  conn_g_l="Google News:", conn_g="If an article’s target address cannot be read directly from the page, the extension asks <code>news.google.com</code> for it – the service you are already using.",
  p_nodev="There is no connection to any server of the developer. The developer receives no data at all.",
  h_perm="Permissions",
  perm_all_l="Access to all websites:", perm_all="required because articles are hosted by arbitrary publishers whose pages must be fetched. The extension only modifies <code>news.google.com</code> (inserting the tags), no other website.",
  perm_st_l="Storage", perm_st="(<code>storage</code>): for settings and the local cache.",
  h_ctrl="Your control",
  ctrl1="“Clear cache” in the settings deletes all stored check results.",
  ctrl2="When you remove the extension, Chrome deletes all of its locally stored data.",
  h_contact="Contact and changes",
  p_contact="Questions via {issues}. The source code is public: {repo}. If the handling of data changes, this page will be updated and the date above adjusted.",
  langs="Languages")

L["de"] = dict(name="Deutsch",
  title="Datenschutzerklärung",
  updated="Stand: 20. November 2026 · gilt für die Browser-Erweiterung „Paywall-Marker“ ab Version 1.2.0",
  binding="Diese Erklärung gibt es in mehreren Sprachen. Weichen die Übersetzungen ab, gilt die englische Fassung.",
  tldr_l="Kurz gesagt:", tldr="Die Erweiterung sammelt keine personenbezogenen Daten, hat keinen eigenen Server und gibt nichts an den Entwickler oder an Dritte weiter. Alles wird lokal in deinem Browser verarbeitet und gespeichert.",
  h_what="Was die Erweiterung tut",
  p_what="Paywall-Marker zeigt im Google-News-Feed (<code>news.google.com</code>) neben jedem Artikel an, ob er hinter einer Bezahlschranke liegt. Dazu ruft die Erweiterung die verlinkten Artikelseiten direkt beim jeweiligen Verlag ab und liest die Kennzeichnung, die der Verlag selbst in die Seite schreibt (z. B. <code>isAccessibleForFree</code>).",
  h_data="Welche Daten verarbeitet werden", th=("Daten", "Zweck", "Wo / wie lange"),
  rows=[("Adressen (URLs) der Artikel, die im Google-News-Feed sichtbar sind", "Artikelseite abrufen und prüfen", "Nur im Arbeitsspeicher und im lokalen Zwischenspeicher (siehe unten)"),
        ("Inhalt der abgerufenen Artikelseiten", "Paywall-Kennzeichnung auslesen", "Nur kurz im Arbeitsspeicher, wird nicht gespeichert"),
        ("Prüfergebnis je Artikel-URL (Status, Grund, Zeitpunkt)", "Doppelte Abrufe vermeiden", "Lokal im Browser (<code>chrome.storage.local</code>), 2 Stunden bis 7 Tage; „Cache leeren“ löscht alles sofort"),
        ("Deine Einstellungen (Sprache, Darstellung, eigene Domain-Listen)", "Einstellungen merken", "Im Browser (<code>chrome.storage.sync</code>). Ist die Chrome-Synchronisierung aktiv, gleicht Chrome sie über dein Google-Konto zwischen deinen Geräten ab – eine Funktion von Chrome, nicht der Erweiterung.")],
  p_none="Die Erweiterung erhebt <strong>keine</strong> Nutzungsstatistiken, verwendet keine Analyse- oder Werbedienste, liest keinen Browserverlauf und lädt keinen Code aus dem Internet nach.",
  h_conn="Verbindungen zu anderen Diensten",
  conn_pub_l="Verlagsseiten:", conn_pub="Für jeden im Feed sichtbaren Artikel ruft dein Browser die Artikelseite beim Verlag ab, so als würdest du sie kurz öffnen. Dabei werden die für diese Seite vorhandenen Cookies mitgesendet (z. B. eine bereits erteilte Cookie-Zustimmung). Der Verlag erhält die üblichen technischen Daten eines Seitenaufrufs (z. B. IP-Adresse, Browserkennung); dafür gilt die Datenschutzerklärung des jeweiligen Verlags.",
  conn_g_l="Google News:", conn_g="Lässt sich die Zieladresse eines Artikels nicht direkt aus der Seite lesen, fragt die Erweiterung sie bei <code>news.google.com</code> ab – dem Dienst, den du ohnehin gerade nutzt.",
  p_nodev="Es gibt keine Verbindung zu Servern des Entwicklers. Der Entwickler erhält keinerlei Daten.",
  h_perm="Berechtigungen",
  perm_all_l="Zugriff auf alle Websites:", perm_all="nötig, weil die Artikel bei beliebigen Verlagen liegen und deren Seiten abgerufen werden müssen. Die Erweiterung verändert nur <code>news.google.com</code> (Markierungen einfügen), keine anderen Websites.",
  perm_st_l="Speicher", perm_st="(<code>storage</code>): für Einstellungen und den lokalen Zwischenspeicher.",
  h_ctrl="Deine Kontrolle",
  ctrl1="„Cache leeren“ in den Einstellungen löscht alle gespeicherten Prüfergebnisse.",
  ctrl2="Beim Entfernen der Erweiterung löscht Chrome alle ihre lokal gespeicherten Daten.",
  h_contact="Kontakt und Änderungen",
  p_contact="Fragen bitte über {issues}. Der Quellcode ist öffentlich einsehbar: {repo}. Ändert sich der Umgang mit Daten, wird diese Seite aktualisiert und das Datum oben angepasst.",
  langs="Sprachen")

L["es"] = dict(name="Español",
  title="Política de privacidad",
  updated="Última actualización: 20 de noviembre de 2026 · se aplica a la extensión de navegador «Paywall-Marker» a partir de la versión 1.2.0",
  binding="Esta política está disponible en varios idiomas. Si las traducciones difieren, prevalece la versión en inglés.",
  tldr_l="En resumen:", tldr="La extensión no recopila datos personales, no tiene servidor propio y no comparte nada con el desarrollador ni con terceros. Todo se procesa y almacena localmente en tu navegador.",
  h_what="Qué hace la extensión",
  p_what="Paywall-Marker indica junto a cada artículo del feed de Google Noticias (<code>news.google.com</code>) si está detrás de un muro de pago. Para ello, descarga las páginas de los artículos enlazados directamente desde el medio y lee la indicación que el propio medio incluye en la página (p. ej. <code>isAccessibleForFree</code>).",
  h_data="Qué datos se procesan", th=("Datos", "Finalidad", "Dónde / cuánto tiempo"),
  rows=[("Direcciones (URL) de los artículos visibles en el feed de Google Noticias", "Descargar y comprobar la página del artículo", "Solo en memoria y en la caché local (ver abajo)"),
        ("Contenido de las páginas de artículos descargadas", "Leer la indicación de muro de pago", "Solo brevemente en memoria, nunca se guarda"),
        ("Resultado de la comprobación por URL (estado, motivo, hora)", "Evitar descargas repetidas", "Localmente en el navegador (<code>chrome.storage.local</code>), de 2 horas a 7 días; «Vaciar caché» lo borra todo al instante"),
        ("Tus ajustes (idioma, visualización, tus listas de dominios)", "Recordar los ajustes", "En el navegador (<code>chrome.storage.sync</code>). Si la sincronización de Chrome está activada, Chrome los sincroniza entre tus dispositivos mediante tu cuenta de Google; es una función de Chrome, no de la extensión.")],
  p_none="La extensión <strong>no</strong> recopila estadísticas de uso, no utiliza servicios de analítica ni de publicidad, no lee tu historial de navegación y no descarga código de internet.",
  h_conn="Conexiones con otros servicios",
  conn_pub_l="Sitios de los medios:", conn_pub="Para cada artículo visible en el feed, tu navegador descarga la página del artículo desde el medio, como si la abrieras brevemente. Se envían las cookies que ya tengas para ese sitio (p. ej. un consentimiento de cookies que diste antes). El medio recibe los datos técnicos habituales de una visita (p. ej. dirección IP, identificador del navegador); a esos datos se aplica la política de privacidad del propio medio.",
  conn_g_l="Google Noticias:", conn_g="Si la dirección de destino de un artículo no puede leerse directamente de la página, la extensión la solicita a <code>news.google.com</code>, el servicio que ya estás usando.",
  p_nodev="No hay ninguna conexión con servidores del desarrollador. El desarrollador no recibe ningún dato.",
  h_perm="Permisos",
  perm_all_l="Acceso a todos los sitios web:", perm_all="necesario porque los artículos están alojados por medios de todo tipo cuyas páginas deben descargarse. La extensión solo modifica <code>news.google.com</code> (añade las etiquetas), ningún otro sitio.",
  perm_st_l="Almacenamiento", perm_st="(<code>storage</code>): para los ajustes y la caché local.",
  h_ctrl="Tu control",
  ctrl1="«Vaciar caché» en los ajustes borra todos los resultados guardados.",
  ctrl2="Al quitar la extensión, Chrome borra todos sus datos almacenados localmente.",
  h_contact="Contacto y cambios",
  p_contact="Para preguntas, usa {issues}. El código fuente es público: {repo}. Si cambia el tratamiento de los datos, esta página se actualizará y se ajustará la fecha indicada arriba.",
  langs="Idiomas")

L["fr"] = dict(name="Français",
  title="Politique de confidentialité",
  updated="Dernière mise à jour : 20 novembre 2026 · s’applique à l’extension de navigateur « Paywall-Marker » à partir de la version 1.2.0",
  binding="Cette politique existe en plusieurs langues. En cas de divergence entre les traductions, la version anglaise fait foi.",
  tldr_l="En bref :", tldr="L’extension ne collecte aucune donnée personnelle, n’a pas de serveur propre et ne transmet rien au développeur ni à des tiers. Tout est traité et stocké localement dans votre navigateur.",
  h_what="Ce que fait l’extension",
  p_what="Paywall-Marker indique, à côté de chaque article du fil Google Actualités (<code>news.google.com</code>), s’il se trouve derrière un paywall. Pour cela, l’extension charge les pages d’articles liées directement auprès de l’éditeur et lit le marquage que l’éditeur place lui-même dans la page (p. ex. <code>isAccessibleForFree</code>).",
  h_data="Données traitées", th=("Données", "Finalité", "Où / combien de temps"),
  rows=[("Adresses (URL) des articles visibles dans le fil Google Actualités", "Charger et vérifier la page de l’article", "Uniquement en mémoire et dans le cache local (voir ci-dessous)"),
        ("Contenu des pages d’articles chargées", "Lire le marquage paywall", "Brièvement en mémoire uniquement, jamais enregistré"),
        ("Résultat de la vérification par URL (statut, motif, heure)", "Éviter les chargements répétés", "Localement dans le navigateur (<code>chrome.storage.local</code>), de 2 heures à 7 jours ; « Vider le cache » supprime tout immédiatement"),
        ("Vos paramètres (langue, affichage, vos listes de domaines)", "Mémoriser les paramètres", "Dans le navigateur (<code>chrome.storage.sync</code>). Si la synchronisation Chrome est activée, Chrome les synchronise entre vos appareils via votre compte Google – une fonction de Chrome, pas de l’extension.")],
  p_none="L’extension ne collecte <strong>aucune</strong> statistique d’utilisation, n’utilise aucun service d’analyse ou de publicité, ne lit pas votre historique de navigation et ne charge aucun code depuis Internet.",
  h_conn="Connexions à d’autres services",
  conn_pub_l="Sites des éditeurs :", conn_pub="Pour chaque article visible dans le fil, votre navigateur charge la page de l’article auprès de l’éditeur, comme si vous l’ouvriez brièvement. Les cookies que vous possédez déjà pour ce site sont envoyés (p. ex. un consentement aux cookies donné auparavant). L’éditeur reçoit les données techniques habituelles d’une visite (p. ex. adresse IP, identifiant du navigateur) ; la politique de confidentialité de l’éditeur s’applique à ces données.",
  conn_g_l="Google Actualités :", conn_g="Si l’adresse cible d’un article ne peut pas être lue directement dans la page, l’extension la demande à <code>news.google.com</code>, le service que vous utilisez déjà.",
  p_nodev="Il n’existe aucune connexion à un serveur du développeur. Le développeur ne reçoit aucune donnée.",
  h_perm="Autorisations",
  perm_all_l="Accès à tous les sites web :", perm_all="nécessaire, car les articles sont hébergés par toutes sortes d’éditeurs dont les pages doivent être chargées. L’extension ne modifie que <code>news.google.com</code> (ajout des étiquettes), aucun autre site.",
  perm_st_l="Stockage", perm_st="(<code>storage</code>) : pour les paramètres et le cache local.",
  h_ctrl="Vos moyens de contrôle",
  ctrl1="« Vider le cache » dans les paramètres supprime tous les résultats enregistrés.",
  ctrl2="Lorsque vous supprimez l’extension, Chrome efface toutes ses données stockées localement.",
  h_contact="Contact et modifications",
  p_contact="Pour toute question : {issues}. Le code source est public : {repo}. Si le traitement des données change, cette page sera mise à jour et la date ci-dessus modifiée.",
  langs="Langues")

L["pt"] = dict(name="Português",
  title="Política de privacidade",
  updated="Última atualização: 20 de novembro de 2026 · aplica-se à extensão de navegador “Paywall-Marker” a partir da versão 1.2.0",
  binding="Esta política está disponível em vários idiomas. Em caso de divergência entre as traduções, prevalece a versão em inglês.",
  tldr_l="Em resumo:", tldr="A extensão não coleta dados pessoais, não tem servidor próprio e não compartilha nada com o desenvolvedor nem com terceiros. Tudo é processado e armazenado localmente no seu navegador.",
  h_what="O que a extensão faz",
  p_what="O Paywall-Marker mostra, ao lado de cada artigo no feed do Google Notícias (<code>news.google.com</code>), se ele está atrás de um paywall. Para isso, a extensão carrega as páginas dos artigos diretamente do veículo e lê a marcação que o próprio veículo coloca na página (p. ex. <code>isAccessibleForFree</code>).",
  h_data="Quais dados são processados", th=("Dados", "Finalidade", "Onde / por quanto tempo"),
  rows=[("Endereços (URLs) dos artigos visíveis no feed do Google Notícias", "Carregar e verificar a página do artigo", "Apenas na memória e no cache local (veja abaixo)"),
        ("Conteúdo das páginas de artigos carregadas", "Ler a marcação de paywall", "Apenas brevemente na memória, nunca é salvo"),
        ("Resultado da verificação por URL (estado, motivo, horário)", "Evitar carregamentos repetidos", "Localmente no navegador (<code>chrome.storage.local</code>), de 2 horas a 7 dias; “Limpar cache” apaga tudo imediatamente"),
        ("Suas configurações (idioma, exibição, suas listas de domínios)", "Lembrar as configurações", "No navegador (<code>chrome.storage.sync</code>). Se a sincronização do Chrome estiver ativada, o Chrome as sincroniza entre seus dispositivos pela sua Conta do Google – um recurso do Chrome, não da extensão.")],
  p_none="A extensão <strong>não</strong> coleta estatísticas de uso, não usa serviços de análise ou publicidade, não lê seu histórico de navegação e não carrega código da internet.",
  h_conn="Conexões com outros serviços",
  conn_pub_l="Sites dos veículos:", conn_pub="Para cada artigo visível no feed, seu navegador carrega a página do artigo no veículo, como se você a abrisse rapidamente. Os cookies que você já tem para esse site são enviados (p. ex. um consentimento de cookies dado antes). O veículo recebe os dados técnicos usuais de um acesso (p. ex. endereço IP, identificação do navegador); a esses dados aplica-se a política de privacidade do próprio veículo.",
  conn_g_l="Google Notícias:", conn_g="Se o endereço de destino de um artigo não puder ser lido diretamente na página, a extensão o solicita a <code>news.google.com</code>, o serviço que você já está usando.",
  p_nodev="Não há nenhuma conexão com servidores do desenvolvedor. O desenvolvedor não recebe nenhum dado.",
  h_perm="Permissões",
  perm_all_l="Acesso a todos os sites:", perm_all="necessário porque os artigos ficam em sites de veículos variados, cujas páginas precisam ser carregadas. A extensão só modifica <code>news.google.com</code> (inserindo as etiquetas), nenhum outro site.",
  perm_st_l="Armazenamento", perm_st="(<code>storage</code>): para as configurações e o cache local.",
  h_ctrl="Seu controle",
  ctrl1="“Limpar cache” nas configurações apaga todos os resultados salvos.",
  ctrl2="Ao remover a extensão, o Chrome apaga todos os dados dela armazenados localmente.",
  h_contact="Contato e alterações",
  p_contact="Dúvidas pelo {issues}. O código-fonte é público: {repo}. Se o tratamento de dados mudar, esta página será atualizada e a data acima ajustada.",
  langs="Idiomas")

L["uk"] = dict(name="Українська",
  title="Політика конфіденційності",
  updated="Останнє оновлення: 20 листопада 2026 р. · стосується розширення для браузера «Paywall-Marker» починаючи з версії 1.2.0",
  binding="Ця політика доступна кількома мовами. У разі розбіжностей між перекладами переважну силу має англійська версія.",
  tldr_l="Коротко:", tldr="Розширення не збирає персональних даних, не має власного сервера й нічого не передає розробникові чи третім особам. Усе обробляється та зберігається локально у вашому браузері.",
  h_what="Що робить розширення",
  p_what="Paywall-Marker показує біля кожної статті у стрічці Google Новин (<code>news.google.com</code>), чи вона за платним доступом. Для цього розширення завантажує сторінки статей безпосередньо з сайту видання й зчитує позначку, яку видання саме розміщує на сторінці (напр. <code>isAccessibleForFree</code>).",
  h_data="Які дані обробляються", th=("Дані", "Мета", "Де / як довго"),
  rows=[("Адреси (URL) статей, видимих у стрічці Google Новин", "Завантажити й перевірити сторінку статті", "Лише в оперативній пам’яті та в локальному кеші (див. нижче)"),
        ("Вміст завантажених сторінок статей", "Зчитати позначку платного доступу", "Лише короткочасно в пам’яті, ніколи не зберігається"),
        ("Результат перевірки для кожної URL-адреси (статус, причина, час)", "Уникати повторних завантажень", "Локально в браузері (<code>chrome.storage.local</code>), від 2 годин до 7 днів; «Очистити кеш» одразу видаляє все"),
        ("Ваші налаштування (мова, відображення, ваші списки доменів)", "Запам’ятовувати налаштування", "У браузері (<code>chrome.storage.sync</code>). Якщо синхронізацію Chrome увімкнено, Chrome синхронізує їх між вашими пристроями через ваш обліковий запис Google – це функція Chrome, а не розширення.")],
  p_none="Розширення <strong>не</strong> збирає статистику використання, не використовує аналітичних чи рекламних сервісів, не читає історію перегляду й не завантажує код з інтернету.",
  h_conn="З’єднання з іншими сервісами",
  conn_pub_l="Сайти видань:", conn_pub="Для кожної статті, видимої у стрічці, ваш браузер завантажує сторінку статті з сайту видання, ніби ви ненадовго її відкрили. При цьому надсилаються наявні у вас cookie для цього сайту (напр. раніше надана згода на cookie). Видання отримує звичайні технічні дані запиту (напр. IP-адресу, ідентифікатор браузера); до цих даних застосовується політика конфіденційності самого видання.",
  conn_g_l="Google Новини:", conn_g="Якщо цільову адресу статті не вдається прочитати безпосередньо зі сторінки, розширення запитує її в <code>news.google.com</code> – сервісу, яким ви вже користуєтеся.",
  p_nodev="Жодного з’єднання із серверами розробника немає. Розробник не отримує жодних даних.",
  h_perm="Дозволи",
  perm_all_l="Доступ до всіх вебсайтів:", perm_all="потрібен, бо статті розміщені на сайтах різних видань, сторінки яких треба завантажувати. Розширення змінює лише <code>news.google.com</code> (додає позначки) і жодних інших сайтів.",
  perm_st_l="Сховище", perm_st="(<code>storage</code>): для налаштувань і локального кешу.",
  h_ctrl="Ваш контроль",
  ctrl1="«Очистити кеш» у налаштуваннях видаляє всі збережені результати перевірок.",
  ctrl2="Після видалення розширення Chrome стирає всі його локально збережені дані.",
  h_contact="Контакти та зміни",
  p_contact="Запитання – через {issues}. Вихідний код відкритий: {repo}. Якщо порядок обробки даних зміниться, цю сторінку буде оновлено, а дату вгорі змінено.",
  langs="Мови")

L["ja"] = dict(name="日本語",
  title="プライバシーポリシー",
  updated="最終更新日：2026年11月20日 · ブラウザ拡張機能「Paywall-Marker」バージョン1.2.0以降に適用",
  binding="本ポリシーは複数の言語で提供しています。翻訳間で内容が異なる場合は、英語版が優先されます。",
  tldr_l="概要：", tldr="この拡張機能は個人データを収集せず、独自のサーバーを持たず、開発者や第三者に何も送信しません。すべての処理と保存はお使いのブラウザ内で行われます。",
  h_what="拡張機能の動作",
  p_what="Paywall-Marker は、Google ニュースのフィード（<code>news.google.com</code>）の各記事の横に、その記事が有料かどうかを表示します。そのために、リンク先の記事ページを発行元から直接取得し、発行元自身がページに記載している表示（例：<code>isAccessibleForFree</code>）を読み取ります。",
  h_data="処理されるデータ", th=("データ", "目的", "保存場所／期間"),
  rows=[("Google ニュースのフィードに表示されている記事のアドレス（URL）", "記事ページの取得と確認", "メモリ内とローカルキャッシュのみ（下記参照）"),
        ("取得した記事ページの内容", "有料表示の読み取り", "メモリ内に一時的に保持するのみで、保存しません"),
        ("記事URLごとの確認結果（状態、理由、日時）", "重複取得の防止", "ブラウザ内（<code>chrome.storage.local</code>）に2時間～7日間。「キャッシュを消去」ですぐにすべて削除されます"),
        ("設定（言語、表示、独自のドメインリスト）", "設定の保存", "ブラウザ内（<code>chrome.storage.sync</code>）。Chrome の同期が有効な場合、Chrome が Google アカウントを通じてデバイス間で同期します。これは Chrome の機能であり、拡張機能の機能ではありません。")],
  p_none="この拡張機能は、利用統計の収集、分析サービスや広告サービスの利用、閲覧履歴の読み取り、インターネットからのコードの読み込みを<strong>一切行いません</strong>。",
  h_conn="他のサービスとの通信",
  conn_pub_l="発行元のサイト：", conn_pub="フィードに表示されている各記事について、ブラウザが発行元から記事ページを取得します。これは記事を短時間開くのと同じです。その際、そのサイトに対して既にお持ちの Cookie（例：以前に行った Cookie への同意）が送信されます。発行元は通常のアクセスと同じ技術情報（例：IPアドレス、ブラウザの識別情報）を受け取り、これらには発行元のプライバシーポリシーが適用されます。",
  conn_g_l="Google ニュース：", conn_g="記事のリンク先アドレスをページから直接読み取れない場合、拡張機能は現在ご利用中のサービスである <code>news.google.com</code> に問い合わせます。",
  p_nodev="開発者のサーバーとの通信は一切ありません。開発者がデータを受け取ることはありません。",
  h_perm="権限",
  perm_all_l="すべてのウェブサイトへのアクセス：", perm_all="記事はさまざまな発行元のサイトにあり、そのページを取得する必要があるため必要です。拡張機能が変更するのは <code>news.google.com</code>（タグの挿入）のみで、他のサイトは変更しません。",
  perm_st_l="ストレージ", perm_st="（<code>storage</code>）：設定とローカルキャッシュのため。",
  h_ctrl="ユーザーによる管理",
  ctrl1="設定の「キャッシュを消去」で、保存されたすべての確認結果が削除されます。",
  ctrl2="拡張機能を削除すると、Chrome がローカルに保存されたデータをすべて削除します。",
  h_contact="お問い合わせと変更",
  p_contact="ご質問は {issues} からどうぞ。ソースコードは公開されています：{repo}。データの取り扱いが変わる場合は、このページを更新し、上記の日付を変更します。",
  langs="言語")

L["no"] = dict(name="Norsk",
  title="Personvernerklæring",
  updated="Sist oppdatert: 20. november 2026 · gjelder nettleserutvidelsen «Paywall-Marker» fra versjon 1.2.0",
  binding="Denne erklæringen finnes på flere språk. Ved avvik mellom oversettelsene gjelder den engelske versjonen.",
  tldr_l="Kort fortalt:", tldr="Utvidelsen samler ikke inn personopplysninger, har ingen egen server og deler ingenting med utvikleren eller tredjeparter. Alt behandles og lagres lokalt i nettleseren din.",
  h_what="Hva utvidelsen gjør",
  p_what="Paywall-Marker viser ved hver artikkel i Google Nyheter-feeden (<code>news.google.com</code>) om den ligger bak en betalingsmur. For å gjøre det henter utvidelsen de lenkede artikkelsidene direkte fra utgiveren og leser merkingen som utgiveren selv legger inn på siden (f.eks. <code>isAccessibleForFree</code>).",
  h_data="Hvilke data som behandles", th=("Data", "Formål", "Hvor / hvor lenge"),
  rows=[("Adresser (URL-er) til artiklene som vises i Google Nyheter-feeden", "Hente og sjekke artikkelsiden", "Bare i minnet og i den lokale hurtigbufferen (se nedenfor)"),
        ("Innholdet i de hentede artikkelsidene", "Lese merkingen av betalingsmur", "Bare kortvarig i minnet, lagres aldri"),
        ("Resultatet per artikkel-URL (status, grunn, tidspunkt)", "Unngå gjentatte hentinger", "Lokalt i nettleseren (<code>chrome.storage.local</code>), 2 timer til 7 dager; «Tøm hurtigbuffer» sletter alt umiddelbart"),
        ("Innstillingene dine (språk, visning, egne domenelister)", "Huske innstillingene", "I nettleseren (<code>chrome.storage.sync</code>). Er Chrome-synkronisering slått på, synkroniserer Chrome dem mellom enhetene dine via Google-kontoen din – en funksjon i Chrome, ikke i utvidelsen.")],
  p_none="Utvidelsen samler <strong>ikke</strong> inn bruksstatistikk, bruker ingen analyse- eller annonsetjenester, leser ikke nettleserloggen din og laster ikke inn kode fra internett.",
  h_conn="Forbindelser til andre tjenester",
  conn_pub_l="Utgivernes nettsteder:", conn_pub="For hver artikkel som vises i feeden, henter nettleseren artikkelsiden fra utgiveren, som om du åpnet den et øyeblikk. Informasjonskapsler du allerede har for nettstedet, sendes med (f.eks. et samtykke du har gitt tidligere). Utgiveren mottar de vanlige tekniske dataene ved et sidebesøk (f.eks. IP-adresse, nettleseridentifikator); for disse gjelder utgiverens egen personvernerklæring.",
  conn_g_l="Google Nyheter:", conn_g="Hvis måladressen til en artikkel ikke kan leses direkte fra siden, spør utvidelsen <code>news.google.com</code> om den – tjenesten du allerede bruker.",
  p_nodev="Det finnes ingen forbindelse til utviklerens servere. Utvikleren mottar ingen data.",
  h_perm="Tillatelser",
  perm_all_l="Tilgang til alle nettsteder:", perm_all="nødvendig fordi artiklene ligger hos vilkårlige utgivere, og sidene deres må hentes. Utvidelsen endrer bare <code>news.google.com</code> (legger inn merkene), ingen andre nettsteder.",
  perm_st_l="Lagring", perm_st="(<code>storage</code>): for innstillinger og den lokale hurtigbufferen.",
  h_ctrl="Din kontroll",
  ctrl1="«Tøm hurtigbuffer» i innstillingene sletter alle lagrede resultater.",
  ctrl2="Når du fjerner utvidelsen, sletter Chrome alle data den har lagret lokalt.",
  h_contact="Kontakt og endringer",
  p_contact="Spørsmål via {issues}. Kildekoden er offentlig: {repo}. Endres behandlingen av data, oppdateres denne siden og datoen ovenfor.",
  langs="Språk")

L["sv"] = dict(name="Svenska",
  title="Integritetspolicy",
  updated="Senast uppdaterad: 20 november 2026 · gäller webbläsartillägget ”Paywall-Marker” från version 1.2.0",
  binding="Policyn finns på flera språk. Om översättningarna skiljer sig åt gäller den engelska versionen.",
  tldr_l="I korthet:", tldr="Tillägget samlar inte in personuppgifter, har ingen egen server och delar ingenting med utvecklaren eller tredje part. Allt behandlas och lagras lokalt i din webbläsare.",
  h_what="Vad tillägget gör",
  p_what="Paywall-Marker visar vid varje artikel i Google Nyheter-flödet (<code>news.google.com</code>) om den ligger bakom en betalvägg. För att göra det hämtar tillägget de länkade artikelsidorna direkt från utgivaren och läser den märkning som utgivaren själv lägger in på sidan (t.ex. <code>isAccessibleForFree</code>).",
  h_data="Vilka uppgifter som behandlas", th=("Uppgifter", "Syfte", "Var / hur länge"),
  rows=[("Adresser (URL:er) till artiklarna som syns i Google Nyheter-flödet", "Hämta och kontrollera artikelsidan", "Endast i minnet och i den lokala cachen (se nedan)"),
        ("Innehållet i de hämtade artikelsidorna", "Läsa betalväggsmärkningen", "Endast kort i minnet, sparas aldrig"),
        ("Resultat per artikel-URL (status, orsak, tidpunkt)", "Undvika upprepade hämtningar", "Lokalt i webbläsaren (<code>chrome.storage.local</code>), 2 timmar till 7 dagar; ”Töm cache” raderar allt direkt"),
        ("Dina inställningar (språk, visning, egna domänlistor)", "Komma ihåg inställningarna", "I webbläsaren (<code>chrome.storage.sync</code>). Om Chrome-synkronisering är aktiverad synkroniserar Chrome dem mellan dina enheter via ditt Google-konto – en funktion i Chrome, inte i tillägget.")],
  p_none="Tillägget samlar <strong>inte</strong> in användningsstatistik, använder inga analys- eller annonstjänster, läser inte din webbhistorik och laddar inte kod från internet.",
  h_conn="Anslutningar till andra tjänster",
  conn_pub_l="Utgivarnas webbplatser:", conn_pub="För varje artikel som syns i flödet hämtar din webbläsare artikelsidan från utgivaren, som om du öppnade den en kort stund. Kakor som du redan har för webbplatsen skickas med (t.ex. ett tidigare givet samtycke till kakor). Utgivaren får de vanliga tekniska uppgifterna vid ett sidbesök (t.ex. IP-adress, webbläsaridentifierare); för dessa gäller utgivarens egen integritetspolicy.",
  conn_g_l="Google Nyheter:", conn_g="Om en artikels måladress inte kan läsas direkt från sidan frågar tillägget <code>news.google.com</code> efter den – tjänsten du redan använder.",
  p_nodev="Det finns ingen anslutning till utvecklarens servrar. Utvecklaren får inga uppgifter alls.",
  h_perm="Behörigheter",
  perm_all_l="Åtkomst till alla webbplatser:", perm_all="krävs eftersom artiklarna ligger hos godtyckliga utgivare vars sidor måste hämtas. Tillägget ändrar bara <code>news.google.com</code> (lägger in etiketterna), inga andra webbplatser.",
  perm_st_l="Lagring", perm_st="(<code>storage</code>): för inställningar och den lokala cachen.",
  h_ctrl="Din kontroll",
  ctrl1="”Töm cache” i inställningarna raderar alla sparade resultat.",
  ctrl2="När du tar bort tillägget raderar Chrome alla dess lokalt sparade uppgifter.",
  h_contact="Kontakt och ändringar",
  p_contact="Frågor via {issues}. Källkoden är offentlig: {repo}. Om hanteringen av uppgifter ändras uppdateras denna sida och datumet ovan.",
  langs="Språk")

L["fi"] = dict(name="Suomi",
  title="Tietosuojaseloste",
  updated="Päivitetty: 20. marraskuuta 2026 · koskee selainlaajennusta ”Paywall-Marker” versiosta 1.2.0 alkaen",
  binding="Tämä seloste on saatavilla useilla kielillä. Jos käännökset poikkeavat toisistaan, englanninkielinen versio on ratkaiseva.",
  tldr_l="Lyhyesti:", tldr="Laajennus ei kerää henkilötietoja, sillä ei ole omaa palvelinta, eikä se jaa mitään kehittäjälle tai kolmansille osapuolille. Kaikki käsitellään ja tallennetaan paikallisesti selaimessasi.",
  h_what="Mitä laajennus tekee",
  p_what="Paywall-Marker näyttää jokaisen Google Uutisten syötteen (<code>news.google.com</code>) artikkelin kohdalla, onko se maksumuurin takana. Sitä varten laajennus hakee linkitetyt artikkelisivut suoraan julkaisijalta ja lukee merkinnän, jonka julkaisija itse on lisännyt sivulle (esim. <code>isAccessibleForFree</code>).",
  h_data="Mitä tietoja käsitellään", th=("Tiedot", "Tarkoitus", "Missä / kuinka kauan"),
  rows=[("Google Uutisten syötteessä näkyvien artikkelien osoitteet (URL)", "Artikkelisivun haku ja tarkistus", "Vain muistissa ja paikallisessa välimuistissa (ks. alla)"),
        ("Haettujen artikkelisivujen sisältö", "Maksumuurimerkinnän lukeminen", "Vain hetken muistissa, ei tallenneta"),
        ("Tarkistuksen tulos artikkelin URL-osoitetta kohden (tila, syy, aika)", "Toistuvien hakujen välttäminen", "Paikallisesti selaimessa (<code>chrome.storage.local</code>) 2 tunnista 7 päivään; ”Tyhjennä välimuisti” poistaa kaiken heti"),
        ("Asetuksesi (kieli, näkymä, omat verkkotunnuslistat)", "Asetusten muistaminen", "Selaimessa (<code>chrome.storage.sync</code>). Jos Chromen synkronointi on käytössä, Chrome synkronoi ne laitteidesi välillä Google-tilisi kautta – kyseessä on Chromen, ei laajennuksen, toiminto.")],
  p_none="Laajennus <strong>ei</strong> kerää käyttötilastoja, käytä analytiikka- tai mainospalveluja, lue selaushistoriaasi eikä lataa koodia internetistä.",
  h_conn="Yhteydet muihin palveluihin",
  conn_pub_l="Julkaisijoiden sivustot:", conn_pub="Jokaisesta syötteessä näkyvästä artikkelista selaimesi hakee artikkelisivun julkaisijalta, ikään kuin avaisit sen hetkeksi. Samalla lähetetään evästeet, jotka sinulla jo on sivustolle (esim. aiemmin annettu evästesuostumus). Julkaisija saa sivupyynnön tavanomaiset tekniset tiedot (esim. IP-osoite, selaimen tunniste); niihin sovelletaan julkaisijan omaa tietosuojaselostetta.",
  conn_g_l="Google Uutiset:", conn_g="Jos artikkelin kohdeosoitetta ei voi lukea suoraan sivulta, laajennus kysyy sitä palvelusta <code>news.google.com</code>, jota jo käytät.",
  p_nodev="Kehittäjän palvelimiin ei ole mitään yhteyttä. Kehittäjä ei saa mitään tietoja.",
  h_perm="Käyttöoikeudet",
  perm_all_l="Pääsy kaikille sivustoille:", perm_all="tarvitaan, koska artikkelit ovat eri julkaisijoiden sivustoilla, joiden sivut on haettava. Laajennus muuttaa vain sivustoa <code>news.google.com</code> (lisää tunnisteet), ei muita sivustoja.",
  perm_st_l="Tallennustila", perm_st="(<code>storage</code>): asetuksia ja paikallista välimuistia varten.",
  h_ctrl="Sinun hallintasi",
  ctrl1="Asetusten ”Tyhjennä välimuisti” poistaa kaikki tallennetut tulokset.",
  ctrl2="Kun poistat laajennuksen, Chrome poistaa kaikki sen paikallisesti tallentamat tiedot.",
  h_contact="Yhteystiedot ja muutokset",
  p_contact="Kysymykset: {issues}. Lähdekoodi on julkinen: {repo}. Jos tietojen käsittely muuttuu, tämä sivu päivitetään ja yllä oleva päivämäärä muutetaan.",
  langs="Kielet")

L["da"] = dict(name="Dansk",
  title="Privatlivspolitik",
  updated="Senest opdateret: 20. november 2026 · gælder browserudvidelsen »Paywall-Marker« fra version 1.2.0",
  binding="Denne politik findes på flere sprog. Hvis oversættelserne afviger fra hinanden, gælder den engelske version.",
  tldr_l="Kort fortalt:", tldr="Udvidelsen indsamler ingen personoplysninger, har ingen egen server og deler intet med udvikleren eller tredjeparter. Alt behandles og gemmes lokalt i din browser.",
  h_what="Hvad udvidelsen gør",
  p_what="Paywall-Marker viser ved hver artikel i Google Nyheder-feedet (<code>news.google.com</code>), om den ligger bag en betalingsmur. Det gør udvidelsen ved at hente de linkede artikelsider direkte fra udgiveren og læse den mærkning, som udgiveren selv har lagt ind på siden (f.eks. <code>isAccessibleForFree</code>).",
  h_data="Hvilke data der behandles", th=("Data", "Formål", "Hvor / hvor længe"),
  rows=[("Adresser (URL'er) på de artikler, der vises i Google Nyheder-feedet", "Hente og tjekke artikelsiden", "Kun i hukommelsen og i den lokale cache (se nedenfor)"),
        ("Indholdet af de hentede artikelsider", "Læse betalingsmur-mærkningen", "Kun kortvarigt i hukommelsen, gemmes aldrig"),
        ("Resultat pr. artikel-URL (status, årsag, tidspunkt)", "Undgå gentagne hentninger", "Lokalt i browseren (<code>chrome.storage.local</code>), 2 timer til 7 dage; »Ryd cache« sletter alt med det samme"),
        ("Dine indstillinger (sprog, visning, egne domænelister)", "Huske indstillingerne", "I browseren (<code>chrome.storage.sync</code>). Hvis Chrome-synkronisering er slået til, synkroniserer Chrome dem mellem dine enheder via din Google-konto – en funktion i Chrome, ikke i udvidelsen.")],
  p_none="Udvidelsen indsamler <strong>ikke</strong> brugsstatistik, bruger ingen analyse- eller annoncetjenester, læser ikke din browserhistorik og indlæser ikke kode fra internettet.",
  h_conn="Forbindelser til andre tjenester",
  conn_pub_l="Udgivernes websites:", conn_pub="For hver artikel, der vises i feedet, henter din browser artikelsiden fra udgiveren, som om du åbnede den et øjeblik. Cookies, du allerede har for sitet, sendes med (f.eks. et tidligere givet cookiesamtykke). Udgiveren modtager de sædvanlige tekniske data ved et sidebesøg (f.eks. IP-adresse, browser-id); for disse gælder udgiverens egen privatlivspolitik.",
  conn_g_l="Google Nyheder:", conn_g="Hvis en artikels måladresse ikke kan læses direkte fra siden, spørger udvidelsen <code>news.google.com</code> om den – den tjeneste, du allerede bruger.",
  p_nodev="Der er ingen forbindelse til udviklerens servere. Udvikleren modtager ingen data.",
  h_perm="Tilladelser",
  perm_all_l="Adgang til alle websites:", perm_all="nødvendig, fordi artiklerne ligger hos vilkårlige udgivere, hvis sider skal hentes. Udvidelsen ændrer kun <code>news.google.com</code> (indsætter mærkerne), ingen andre websites.",
  perm_st_l="Lagring", perm_st="(<code>storage</code>): til indstillinger og den lokale cache.",
  h_ctrl="Din kontrol",
  ctrl1="»Ryd cache« i indstillingerne sletter alle gemte resultater.",
  ctrl2="Når du fjerner udvidelsen, sletter Chrome alle dens lokalt gemte data.",
  h_contact="Kontakt og ændringer",
  p_contact="Spørgsmål via {issues}. Kildekoden er offentlig: {repo}. Hvis behandlingen af data ændres, opdateres denne side og datoen ovenfor.",
  langs="Sprog")

L["it"] = dict(name="Italiano",
  title="Informativa sulla privacy",
  updated="Ultimo aggiornamento: 20 novembre 2026 · si applica all'estensione del browser «Paywall-Marker» dalla versione 1.2.0",
  binding="Questa informativa è disponibile in più lingue. In caso di differenze tra le traduzioni, prevale la versione inglese.",
  tldr_l="In breve:", tldr="L'estensione non raccoglie dati personali, non ha un proprio server e non condivide nulla con lo sviluppatore o con terzi. Tutto viene elaborato e salvato localmente nel tuo browser.",
  h_what="Cosa fa l'estensione",
  p_what="Paywall-Marker indica accanto a ogni articolo del feed di Google News (<code>news.google.com</code>) se è dietro un paywall. Per farlo, l'estensione scarica le pagine degli articoli collegati direttamente dall'editore e legge l'indicazione che l'editore stesso inserisce nella pagina (ad es. <code>isAccessibleForFree</code>).",
  h_data="Quali dati vengono trattati", th=("Dati", "Scopo", "Dove / per quanto tempo"),
  rows=[("Indirizzi (URL) degli articoli visibili nel feed di Google News", "Scaricare e verificare la pagina dell'articolo", "Solo in memoria e nella cache locale (vedi sotto)"),
        ("Contenuto delle pagine degli articoli scaricate", "Leggere l'indicazione di paywall", "Solo brevemente in memoria, mai salvato"),
        ("Risultato della verifica per URL (stato, motivo, ora)", "Evitare download ripetuti", "Localmente nel browser (<code>chrome.storage.local</code>), da 2 ore a 7 giorni; «Svuota cache» cancella tutto subito"),
        ("Le tue impostazioni (lingua, visualizzazione, i tuoi elenchi di domini)", "Ricordare le impostazioni", "Nel browser (<code>chrome.storage.sync</code>). Se la sincronizzazione di Chrome è attiva, Chrome le sincronizza tra i tuoi dispositivi tramite il tuo account Google: è una funzione di Chrome, non dell'estensione.")],
  p_none="L'estensione <strong>non</strong> raccoglie statistiche di utilizzo, non usa servizi di analisi o pubblicità, non legge la cronologia di navigazione e non carica codice da internet.",
  h_conn="Connessioni ad altri servizi",
  conn_pub_l="Siti degli editori:", conn_pub="Per ogni articolo visibile nel feed, il browser scarica la pagina dell'articolo dall'editore, come se la aprissi per un attimo. Vengono inviati i cookie che hai già per quel sito (ad es. un consenso ai cookie dato in precedenza). L'editore riceve i normali dati tecnici di una visita (ad es. indirizzo IP, identificativo del browser); a tali dati si applica l'informativa sulla privacy dell'editore.",
  conn_g_l="Google News:", conn_g="Se l'indirizzo di destinazione di un articolo non può essere letto direttamente dalla pagina, l'estensione lo chiede a <code>news.google.com</code>, il servizio che stai già usando.",
  p_nodev="Non esiste alcuna connessione ai server dello sviluppatore. Lo sviluppatore non riceve alcun dato.",
  h_perm="Autorizzazioni",
  perm_all_l="Accesso a tutti i siti web:", perm_all="necessario perché gli articoli si trovano su siti di editori qualsiasi, le cui pagine devono essere scaricate. L'estensione modifica solo <code>news.google.com</code> (inserendo le etichette), nessun altro sito.",
  perm_st_l="Archiviazione", perm_st="(<code>storage</code>): per le impostazioni e la cache locale.",
  h_ctrl="Il tuo controllo",
  ctrl1="«Svuota cache» nelle impostazioni cancella tutti i risultati salvati.",
  ctrl2="Quando rimuovi l'estensione, Chrome cancella tutti i dati che ha salvato localmente.",
  h_contact="Contatti e modifiche",
  p_contact="Per domande: {issues}. Il codice sorgente è pubblico: {repo}. Se il trattamento dei dati cambia, questa pagina verrà aggiornata e la data indicata sopra modificata.",
  langs="Lingue")

L["nl"] = dict(name="Nederlands",
  title="Privacybeleid",
  updated="Laatst bijgewerkt: 20 november 2026 · geldt voor de browserextensie ‘Paywall-Marker’ vanaf versie 1.2.0",
  binding="Dit beleid is beschikbaar in meerdere talen. Bij verschillen tussen de vertalingen is de Engelse versie leidend.",
  tldr_l="Kort gezegd:", tldr="De extensie verzamelt geen persoonsgegevens, heeft geen eigen server en deelt niets met de ontwikkelaar of derden. Alles wordt lokaal in je browser verwerkt en opgeslagen.",
  h_what="Wat de extensie doet",
  p_what="Paywall-Marker toont bij elk artikel in de Google Nieuws-feed (<code>news.google.com</code>) of het achter een betaalmuur staat. Daarvoor haalt de extensie de gelinkte artikelpagina’s rechtstreeks bij de uitgever op en leest ze de markering die de uitgever zelf in de pagina zet (bijv. <code>isAccessibleForFree</code>).",
  h_data="Welke gegevens worden verwerkt", th=("Gegevens", "Doel", "Waar / hoe lang"),
  rows=[("Adressen (URL’s) van de artikelen die zichtbaar zijn in de Google Nieuws-feed", "Artikelpagina ophalen en controleren", "Alleen in het geheugen en in de lokale cache (zie hieronder)"),
        ("Inhoud van de opgehaalde artikelpagina’s", "Betaalmuurmarkering uitlezen", "Alleen kort in het geheugen, wordt nooit opgeslagen"),
        ("Controleresultaat per artikel-URL (status, reden, tijdstip)", "Herhaald ophalen voorkomen", "Lokaal in de browser (<code>chrome.storage.local</code>), 2 uur tot 7 dagen; ‘Cache wissen’ verwijdert alles direct"),
        ("Je instellingen (taal, weergave, eigen domeinlijsten)", "Instellingen onthouden", "In de browser (<code>chrome.storage.sync</code>). Als Chrome-synchronisatie aan staat, synchroniseert Chrome ze via je Google-account tussen je apparaten – een functie van Chrome, niet van de extensie.")],
  p_none="De extensie verzamelt <strong>geen</strong> gebruiksstatistieken, gebruikt geen analyse- of advertentiediensten, leest je browsegeschiedenis niet en laadt geen code van internet.",
  h_conn="Verbindingen met andere diensten",
  conn_pub_l="Websites van uitgevers:", conn_pub="Voor elk artikel dat in de feed zichtbaar is, haalt je browser de artikelpagina op bij de uitgever, alsof je die even opent. Cookies die je al voor die site hebt, worden meegestuurd (bijv. een eerder gegeven cookietoestemming). De uitgever ontvangt de gebruikelijke technische gegevens van een paginabezoek (bijv. IP-adres, browser-ID); daarop is het privacybeleid van de uitgever van toepassing.",
  conn_g_l="Google Nieuws:", conn_g="Als het doeladres van een artikel niet rechtstreeks uit de pagina kan worden gelezen, vraagt de extensie het op bij <code>news.google.com</code> – de dienst die je al gebruikt.",
  p_nodev="Er is geen verbinding met servers van de ontwikkelaar. De ontwikkelaar ontvangt geen enkel gegeven.",
  h_perm="Rechten",
  perm_all_l="Toegang tot alle websites:", perm_all="nodig omdat de artikelen bij willekeurige uitgevers staan, waarvan de pagina’s moeten worden opgehaald. De extensie wijzigt alleen <code>news.google.com</code> (labels invoegen), geen andere websites.",
  perm_st_l="Opslag", perm_st="(<code>storage</code>): voor instellingen en de lokale cache.",
  h_ctrl="Jouw controle",
  ctrl1="‘Cache wissen’ in de instellingen verwijdert alle opgeslagen resultaten.",
  ctrl2="Als je de extensie verwijdert, wist Chrome alle lokaal opgeslagen gegevens ervan.",
  h_contact="Contact en wijzigingen",
  p_contact="Vragen via {issues}. De broncode is openbaar: {repo}. Als de omgang met gegevens verandert, wordt deze pagina bijgewerkt en de datum hierboven aangepast.",
  langs="Talen")

L["pl"] = dict(name="Polski",
  title="Polityka prywatności",
  updated="Ostatnia aktualizacja: 20 listopada 2026 r. · dotyczy rozszerzenia przeglądarki „Paywall-Marker” od wersji 1.2.0",
  binding="Polityka jest dostępna w kilku językach. W razie rozbieżności między tłumaczeniami rozstrzyga wersja angielska.",
  tldr_l="W skrócie:", tldr="Rozszerzenie nie zbiera danych osobowych, nie ma własnego serwera i niczego nie przekazuje twórcy ani osobom trzecim. Wszystko jest przetwarzane i przechowywane lokalnie w Twojej przeglądarce.",
  h_what="Co robi rozszerzenie",
  p_what="Paywall-Marker pokazuje przy każdym artykule w kanale Google News (<code>news.google.com</code>), czy znajduje się on za paywallem. W tym celu rozszerzenie pobiera strony powiązanych artykułów bezpośrednio od wydawcy i odczytuje oznaczenie, które wydawca sam umieszcza na stronie (np. <code>isAccessibleForFree</code>).",
  h_data="Jakie dane są przetwarzane", th=("Dane", "Cel", "Gdzie / jak długo"),
  rows=[("Adresy (URL) artykułów widocznych w kanale Google News", "Pobranie i sprawdzenie strony artykułu", "Tylko w pamięci i w lokalnej pamięci podręcznej (zob. niżej)"),
        ("Treść pobranych stron artykułów", "Odczytanie oznaczenia paywalla", "Tylko chwilowo w pamięci, nigdy nie jest zapisywana"),
        ("Wynik sprawdzenia dla każdego adresu URL (status, przyczyna, czas)", "Unikanie ponownego pobierania", "Lokalnie w przeglądarce (<code>chrome.storage.local</code>), od 2 godzin do 7 dni; „Wyczyść pamięć podręczną” natychmiast usuwa wszystko"),
        ("Twoje ustawienia (język, wygląd, własne listy domen)", "Zapamiętanie ustawień", "W przeglądarce (<code>chrome.storage.sync</code>). Jeśli synchronizacja Chrome jest włączona, Chrome synchronizuje je między Twoimi urządzeniami przez konto Google – to funkcja Chrome, a nie rozszerzenia.")],
  p_none="Rozszerzenie <strong>nie</strong> zbiera statystyk użycia, nie korzysta z usług analitycznych ani reklamowych, nie odczytuje historii przeglądania i nie pobiera kodu z internetu.",
  h_conn="Połączenia z innymi usługami",
  conn_pub_l="Strony wydawców:", conn_pub="Dla każdego artykułu widocznego w kanale przeglądarka pobiera stronę artykułu od wydawcy, tak jakby została na chwilę otwarta. Wysyłane są przy tym pliki cookie, które już masz dla tej strony (np. wcześniej udzielona zgoda na cookie). Wydawca otrzymuje zwykłe dane techniczne odwiedzin (np. adres IP, identyfikator przeglądarki); do tych danych stosuje się polityka prywatności wydawcy.",
  conn_g_l="Google News:", conn_g="Jeśli adresu docelowego artykułu nie da się odczytać bezpośrednio ze strony, rozszerzenie pyta o niego <code>news.google.com</code> – usługę, z której już korzystasz.",
  p_nodev="Nie ma żadnego połączenia z serwerami twórcy. Twórca nie otrzymuje żadnych danych.",
  h_perm="Uprawnienia",
  perm_all_l="Dostęp do wszystkich stron internetowych:", perm_all="potrzebny, ponieważ artykuły znajdują się na stronach dowolnych wydawców, które trzeba pobrać. Rozszerzenie zmienia tylko <code>news.google.com</code> (dodaje etykiety), żadnych innych stron.",
  perm_st_l="Pamięć", perm_st="(<code>storage</code>): na ustawienia i lokalną pamięć podręczną.",
  h_ctrl="Twoja kontrola",
  ctrl1="„Wyczyść pamięć podręczną” w ustawieniach usuwa wszystkie zapisane wyniki.",
  ctrl2="Po usunięciu rozszerzenia Chrome kasuje wszystkie zapisane przez nie lokalnie dane.",
  h_contact="Kontakt i zmiany",
  p_contact="Pytania przez {issues}. Kod źródłowy jest publiczny: {repo}. Jeśli zmieni się sposób przetwarzania danych, ta strona zostanie zaktualizowana, a data powyżej zmieniona.",
  langs="Języki")

L["cs"] = dict(name="Čeština",
  title="Zásady ochrany osobních údajů",
  updated="Poslední aktualizace: 20. listopadu 2026 · platí pro rozšíření prohlížeče „Paywall-Marker“ od verze 1.2.0",
  binding="Tyto zásady jsou k dispozici v několika jazycích. Pokud se překlady liší, rozhoduje anglická verze.",
  tldr_l="Stručně:", tldr="Rozšíření neshromažďuje žádné osobní údaje, nemá vlastní server a nic nepředává vývojáři ani třetím stranám. Vše se zpracovává a ukládá lokálně ve vašem prohlížeči.",
  h_what="Co rozšíření dělá",
  p_what="Paywall-Marker u každého článku ve zdroji Google Zprávy (<code>news.google.com</code>) ukazuje, zda je za paywallem. K tomu rozšíření načte odkazované stránky článků přímo od vydavatele a přečte označení, které vydavatel sám uvádí na stránce (např. <code>isAccessibleForFree</code>).",
  h_data="Jaké údaje se zpracovávají", th=("Údaje", "Účel", "Kde / jak dlouho"),
  rows=[("Adresy (URL) článků viditelných ve zdroji Google Zprávy", "Načtení a kontrola stránky článku", "Pouze v paměti a v lokální mezipaměti (viz níže)"),
        ("Obsah načtených stránek článků", "Přečtení označení paywallu", "Jen krátce v paměti, nikdy se neukládá"),
        ("Výsledek kontroly pro každou URL článku (stav, důvod, čas)", "Zabránění opakovanému načítání", "Lokálně v prohlížeči (<code>chrome.storage.local</code>), 2 hodiny až 7 dní; „Vymazat mezipaměť“ vše okamžitě smaže"),
        ("Vaše nastavení (jazyk, zobrazení, vlastní seznamy domén)", "Zapamatování nastavení", "V prohlížeči (<code>chrome.storage.sync</code>). Pokud je zapnutá synchronizace Chrome, Chrome je synchronizuje mezi vašimi zařízeními přes váš účet Google – jde o funkci Chrome, ne rozšíření.")],
  p_none="Rozšíření <strong>neshromažďuje</strong> statistiky používání, nepoužívá analytické ani reklamní služby, nečte historii prohlížení a nenačítá kód z internetu.",
  h_conn="Připojení k jiným službám",
  conn_pub_l="Weby vydavatelů:", conn_pub="Pro každý článek viditelný ve zdroji váš prohlížeč načte stránku článku od vydavatele, jako byste ji krátce otevřeli. Přitom se odešlou soubory cookie, které pro daný web už máte (např. dříve udělený souhlas s cookies). Vydavatel obdrží běžné technické údaje o návštěvě (např. IP adresu, identifikátor prohlížeče); na ně se vztahují zásady ochrany osobních údajů vydavatele.",
  conn_g_l="Google Zprávy:", conn_g="Pokud cílovou adresu článku nelze přečíst přímo ze stránky, rozšíření se na ni zeptá služby <code>news.google.com</code>, kterou již používáte.",
  p_nodev="Neexistuje žádné připojení k serverům vývojáře. Vývojář nedostává žádné údaje.",
  h_perm="Oprávnění",
  perm_all_l="Přístup ke všem webům:", perm_all="nutný, protože články jsou na webech libovolných vydavatelů, jejichž stránky je třeba načíst. Rozšíření mění pouze <code>news.google.com</code> (vkládá štítky), žádné jiné weby.",
  perm_st_l="Úložiště", perm_st="(<code>storage</code>): pro nastavení a lokální mezipaměť.",
  h_ctrl="Vaše kontrola",
  ctrl1="„Vymazat mezipaměť“ v nastavení smaže všechny uložené výsledky.",
  ctrl2="Při odebrání rozšíření Chrome smaže všechna jeho lokálně uložená data.",
  h_contact="Kontakt a změny",
  p_contact="Dotazy přes {issues}. Zdrojový kód je veřejný: {repo}. Pokud se nakládání s údaji změní, bude tato stránka aktualizována a datum výše upraveno.",
  langs="Jazyky")

L["hr"] = dict(name="Hrvatski",
  title="Pravila o privatnosti",
  updated="Posljednje ažuriranje: 20. studenoga 2026. · vrijedi za proširenje preglednika „Paywall-Marker” od verzije 1.2.0",
  binding="Ova pravila dostupna su na više jezika. U slučaju odstupanja među prijevodima mjerodavna je engleska verzija.",
  tldr_l="Ukratko:", tldr="Proširenje ne prikuplja osobne podatke, nema vlastiti poslužitelj i ništa ne dijeli s razvojnim programerom ni s trećim stranama. Sve se obrađuje i pohranjuje lokalno u vašem pregledniku.",
  h_what="Što proširenje radi",
  p_what="Paywall-Marker uz svaki članak u feedu Google vijesti (<code>news.google.com</code>) prikazuje nalazi li se iza naplatnog zida. Za to proširenje dohvaća povezane stranice članaka izravno od izdavača i čita oznaku koju izdavač sam stavlja na stranicu (npr. <code>isAccessibleForFree</code>).",
  h_data="Koji se podaci obrađuju", th=("Podaci", "Svrha", "Gdje / koliko dugo"),
  rows=[("Adrese (URL-ovi) članaka vidljivih u feedu Google vijesti", "Dohvaćanje i provjera stranice članka", "Samo u memoriji i u lokalnoj predmemoriji (vidi dolje)"),
        ("Sadržaj dohvaćenih stranica članaka", "Čitanje oznake naplatnog zida", "Samo kratko u memoriji, nikad se ne sprema"),
        ("Rezultat provjere po URL-u članka (status, razlog, vrijeme)", "Izbjegavanje ponovnog dohvaćanja", "Lokalno u pregledniku (<code>chrome.storage.local</code>), od 2 sata do 7 dana; „Očisti predmemoriju” odmah briše sve"),
        ("Vaše postavke (jezik, prikaz, vlastiti popisi domena)", "Pamćenje postavki", "U pregledniku (<code>chrome.storage.sync</code>). Ako je sinkronizacija Chromea uključena, Chrome ih sinkronizira između vaših uređaja putem Google računa – to je funkcija Chromea, a ne proširenja.")],
  p_none="Proširenje <strong>ne</strong> prikuplja statistiku korištenja, ne koristi usluge analitike ni oglašavanja, ne čita povijest pregledavanja i ne učitava kod s interneta.",
  h_conn="Veze s drugim uslugama",
  conn_pub_l="Stranice izdavača:", conn_pub="Za svaki članak vidljiv u feedu vaš preglednik dohvaća stranicu članka od izdavača, kao da ste je nakratko otvorili. Pritom se šalju kolačići koje već imate za tu stranicu (npr. ranije dani pristanak na kolačiće). Izdavač prima uobičajene tehničke podatke posjeta (npr. IP adresu, identifikator preglednika); na njih se primjenjuju pravila o privatnosti izdavača.",
  conn_g_l="Google vijesti:", conn_g="Ako se odredišna adresa članka ne može pročitati izravno sa stranice, proširenje je traži od <code>news.google.com</code> – usluge koju već koristite.",
  p_nodev="Ne postoji nikakva veza s poslužiteljima razvojnog programera. Razvojni programer ne prima nikakve podatke.",
  h_perm="Dopuštenja",
  perm_all_l="Pristup svim web-stranicama:", perm_all="potreban je jer se članci nalaze na stranicama različitih izdavača, koje treba dohvatiti. Proširenje mijenja samo <code>news.google.com</code> (umeće oznake), nijednu drugu stranicu.",
  perm_st_l="Pohrana", perm_st="(<code>storage</code>): za postavke i lokalnu predmemoriju.",
  h_ctrl="Vaša kontrola",
  ctrl1="„Očisti predmemoriju” u postavkama briše sve spremljene rezultate.",
  ctrl2="Kad uklonite proširenje, Chrome briše sve njegove lokalno spremljene podatke.",
  h_contact="Kontakt i izmjene",
  p_contact="Pitanja putem {issues}. Izvorni kod je javan: {repo}. Ako se način obrade podataka promijeni, ova će se stranica ažurirati, a datum iznad prilagoditi.",
  langs="Jezici")


def section(code, t):
    issues = f'<a href="{REPO}/issues">GitHub Issues</a>'
    repo = f'<a href="{REPO}">github.com/VerothSan/paywall-marker</a>'
    rows = "\n".join(f"        <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in t["rows"])
    return f"""
  <section id="{code}" lang="{code}">
    <h2 class="title">{t['title']} <span class="langname">· {t['name']}</span></h2>
    <p class="meta">{t['updated']}</p>
    <p class="meta">{t['binding']}</p>
    <div class="tldr"><strong>{t['tldr_l']}</strong> {t['tldr']}</div>

    <h3>{t['h_what']}</h3>
    <p>{t['p_what']}</p>

    <h3>{t['h_data']}</h3>
    <div class="table"><table>
        <tr><th>{t['th'][0]}</th><th>{t['th'][1]}</th><th>{t['th'][2]}</th></tr>
{rows}
    </table></div>
    <p>{t['p_none']}</p>

    <h3>{t['h_conn']}</h3>
    <ul>
      <li><strong>{t['conn_pub_l']}</strong> {t['conn_pub']}</li>
      <li><strong>{t['conn_g_l']}</strong> {t['conn_g']}</li>
    </ul>
    <p>{t['p_nodev']}</p>

    <h3>{t['h_perm']}</h3>
    <ul>
      <li><strong>{t['perm_all_l']}</strong> {t['perm_all']}</li>
      <li><strong>{t['perm_st_l']}</strong> {t['perm_st']}</li>
    </ul>

    <h3>{t['h_ctrl']}</h3>
    <ul>
      <li>{t['ctrl1']}</li>
      <li>{t['ctrl2']}</li>
    </ul>

    <h3>{t['h_contact']}</h3>
    <p>{t['p_contact'].format(issues=issues, repo=repo)}</p>
    <p class="top"><a href="#langs">↑ {t['langs']}</a></p>
  </section>"""


def build():
    keys = set(L["en"])
    for code, t in L.items():
        assert set(t) == keys, f"{code}: {set(t) ^ keys}"
        assert len(t["rows"]) == 4 and all(len(r) == 3 for r in t["rows"]), code
    nav = "".join(f'<a href="#{c}" hreflang="{c}" lang="{c}">{t["name"]}</a>' for c, t in L.items())
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="google-site-verification" content="g5WwJk1qUhYB-CWL628liKd2dmR1e5mvN2iMsZIXc8E" />
  <title>Paywall-Marker – Privacy Policy</title>
  <meta name="description" content="Privacy policy of the Paywall-Marker browser extension, in 16 languages.">
  <link rel="icon" href="icon-32.png">
  <!-- Generiert von store/privacy.py – Änderungen bitte dort vornehmen. -->
  <!-- SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
       Required Notice: Copyright 2026 VerothSan (https://github.com/VerothSan/paywall-marker) -->
  <style>
    :root {{ color-scheme: light dark; --fg:#1f2328; --muted:#59636e; --bg:#fff; --line:#d1d9e0; --accent:#4f46e5; --card:#f6f8fa; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --fg:#e6edf3; --muted:#9198a1; --bg:#0d1117; --line:#30363d; --accent:#a5b4fc; --card:#161b22; }} }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
    body {{ margin: 0; font: 16px/1.6 system-ui, sans-serif; color: var(--fg); background: var(--bg); }}
    main {{ max-width: 780px; margin: 0 auto; padding: 32px 16px 64px; }}
    header {{ display: flex; align-items: center; gap: 12px; }}
    header img {{ width: 48px; height: 48px; }}
    h1 {{ font-size: 26px; margin: 0; }}
    h2.title {{ font-size: 24px; margin: 0 0 4px; }}
    .langname {{ color: var(--muted); font-weight: 400; font-size: 18px; }}
    h3 {{ font-size: 18px; margin-top: 28px; border-bottom: 1px solid var(--line); padding-bottom: 4px; }}
    .meta {{ color: var(--muted); font-size: 14px; margin: 2px 0; }}
    nav.lang {{ margin: 20px 0 36px; display: flex; flex-wrap: wrap; gap: 8px; }}
    nav.lang a {{ padding: 4px 12px; border: 1px solid var(--line); border-radius: 999px; color: var(--fg); text-decoration: none; font-size: 14px; }}
    nav.lang a:hover, nav.lang a:focus-visible {{ border-color: var(--accent); color: var(--accent); }}
    .tldr {{ background: var(--card); border: 1px solid var(--line); border-radius: 8px; padding: 12px 16px; margin-top: 16px; }}
    .table {{ overflow-x: auto; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 15px; }}
    th, td {{ text-align: left; vertical-align: top; padding: 8px; border-bottom: 1px solid var(--line); }}
    a {{ color: var(--accent); }}
    code {{ font-size: .9em; overflow-wrap: anywhere; }}
    section {{ scroll-margin-top: 16px; }}
    section + section {{ margin-top: 56px; padding-top: 32px; border-top: 3px double var(--line); }}
    .top {{ font-size: 14px; margin-top: 24px; }}
  </style>
</head>
<body>
<main>
  <header>
    <img src="icon-128.png" alt="">
    <h1>Paywall-Marker</h1>
  </header>
  <nav class="lang" id="langs" aria-label="Languages">{nav}</nav>
{"".join(section(c, t) for c, t in L.items())}
</main>
</body>
</html>
"""
    out = ROOT / "docs" / "privacy.html"
    out.write_text(html, encoding="utf-8")
    print(f"{out.relative_to(ROOT)}: {len(L)} Sprachen, {len(html):,} Zeichen")


if __name__ == "__main__":
    build()
