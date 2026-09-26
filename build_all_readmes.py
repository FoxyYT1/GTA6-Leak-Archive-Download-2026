#!/usr/bin/env python3
"""
Generate FULL unshortened README markdown files for GTA 6 CyberLeak in 12 languages.
Output: C:\\Users\\user\\gta6_repo\\README*.md
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

OUTPUT_DIR = Path(r"C:\Users\user\gta6_repo")
DOWNLOAD_URL = "https://cyberleakgta6.net"
UPDATE_DATE = "August 28, 2026"

LANG_FILES = {
    "en": "README.md",
    "ru": "README.ru.md",
    "es": "README.es.md",
    "de": "README.de.md",
    "fr": "README.fr.md",
    "it": "README.it.md",
    "pt": "README.pt.md",
    "pl": "README.pl.md",
    "zh": "README.zh.md",
    "ja": "README.ja.md",
    "ko": "README.ko.md",
    "tr": "README.tr.md",
}

SCREENSHOT_I18N = {
    "en": {
        "mega_btn": "DOWNLOAD_GTA_6_CYBERLEEK_BUILD_NOW",
        "title": "📸 Official CyberLeak Website Screenshots",
        "captions_en": [
            "CyberLeak VI homepage — Download GTA 6 Build & Launcher",
            "Download hub — launcher, install steps, no fake 113GB ISO",
        ],
    },
    "ru": {
        "mega_btn": "СКАЧАТЬ_БИЛД_GTA_6_CYBERLEEK_СЕЙЧАС",
        "title": "📸 Скриншоты официального сайта CyberLeak",
        "captions_ru": [
            "Главная CyberLeak VI — скачать билд GTA 6 и лаунчер",
            "Страница загрузки — лаунчер, установка, без фейка 113 ГБ",
        ],
    },
    "es": {
        "mega_btn": "DESCARGAR_BUILD_GTA_6_CYBERLEEK",
        "title": "📸 Capturas del sitio oficial CyberLeak",
        "captions_en": [
            "Página principal CyberLeak VI — Download GTA 6 Build",
            "Hub de descarga — launcher e instalación (interfaz EN)",
        ],
    },
    "de": {
        "mega_btn": "GTA_6_CYBERLEEK_BUILD_JETZT",
        "title": "📸 Screenshots der offiziellen CyberLeak-Website",
        "captions_en": [
            "CyberLeak VI Startseite — Download GTA 6 Build",
            "Download-Hub — Launcher & Installation (EN-Oberfläche)",
        ],
    },
    "fr": {
        "mega_btn": "TELECHARGER_BUILD_GTA_6_CYBERLEEK",
        "title": "📸 Captures du site officiel CyberLeak",
        "captions_en": [
            "Page d'accueil CyberLeak VI — Download GTA 6 Build",
            "Hub de téléchargement — launcher et installation (EN)",
        ],
    },
    "it": {
        "mega_btn": "SCARICA_BUILD_GTA_6_CYBERLEEK",
        "title": "📸 Screenshot del sito ufficiale CyberLeak",
        "captions_en": [
            "Homepage CyberLeak VI — Download GTA 6 Build",
            "Hub download — launcher e installazione (interfaccia EN)",
        ],
    },
    "pt": {
        "mega_btn": "BAIXAR_BUILD_GTA_6_CYBERLEEK",
        "title": "📸 Capturas do site oficial CyberLeak",
        "captions_en": [
            "Página inicial CyberLeak VI — Download GTA 6 Build",
            "Hub de download — launcher e instalação (interface EN)",
        ],
    },
    "pl": {
        "mega_btn": "POBIERZ_BUILD_GTA_6_CYBERLEEK",
        "title": "📸 Zrzuty ekranu oficjalnej strony CyberLeak",
        "captions_en": [
            "Strona główna CyberLeak VI — Download GTA 6 Build",
            "Hub pobierania — launcher i instalacja (interfejs EN)",
        ],
    },
    "zh": {
        "mega_btn": "立即下载_GTA6_CYBERLEEK_版本",
        "title": "📸 CyberLeak 官方网站截图",
        "captions_en": [
            "CyberLeak VI 首页 — Download GTA 6 Build",
            "下载中心 — 启动器与安装说明（英文界面）",
        ],
    },
    "ja": {
        "mega_btn": "GTA6_CYBERLEEK_今すぐDL",
        "title": "📸 CyberLeak 公式サイトのスクリーンショット",
        "captions_en": [
            "CyberLeak VI トップ — Download GTA 6 Build",
            "ダウンロードハブ — ランチャーとインストール（英語UI）",
        ],
    },
    "ko": {
        "mega_btn": "GTA6_CYBERLEEK_지금_다운로드",
        "title": "📸 CyberLeak 공식 웹사이트 스크린샷",
        "captions_en": [
            "CyberLeak VI 메인 — Download GTA 6 Build",
            "다운로드 허브 — 런처 및 설치 (영문 UI)",
        ],
    },
    "tr": {
        "mega_btn": "GTA6_CYBERLEEK_SIMDI_INDIR",
        "title": "📸 Resmi CyberLeak web sitesi ekran görüntüleri",
        "captions_en": [
            "CyberLeak VI ana sayfa — Download GTA 6 Build",
            "İndirme merkezi — launcher ve kurulum (EN arayüz)",
        ],
    },
}


def _visual_download_section(lang: str, t: dict) -> str:
    meta = SCREENSHOT_I18N.get(lang, SCREENSHOT_I18N["en"])
    btn_label = meta["mega_btn"].replace(" ", "_")

    if lang == "ru":
        shots = [
            ("hero-ru.jpg", meta["captions_ru"][0]),
            ("launcher-ru.jpg", meta["captions_ru"][1]),
        ]
    else:
        caps = meta.get("captions_en", SCREENSHOT_I18N["en"]["captions_en"])
        shots = [
            ("hero-en.jpg", caps[0]),
            ("hub-en.jpg", caps[1]),
        ]

    images_md = "\n\n".join(
        f'[![{caption}](images/site-screenshots/{fname})]({DOWNLOAD_URL})\n\n*{caption}*'
        for fname, caption in shots
    )

    return dedent(
        f"""\
        <div align="center">

        <br>

        <a href="{DOWNLOAD_URL}">
          <img src="https://img.shields.io/badge/⬇️-{btn_label}-00ff88?style=for-the-badge&labelColor=ff0080&logo=rockstargames&logoColor=white" alt="{t["hero_cta"]}" width="620">
        </a>

        <br><br>

        <a href="{DOWNLOAD_URL}">
          <img src="https://img.shields.io/badge/🚀-{t["badge_build"]}_LAUNCHER-00d4ff?style=for-the-badge&labelColor=111111&logo=windows&logoColor=white" alt="Launcher" width="420">
        </a>

        <br><br>

        ### {meta["title"]}

        {images_md}

        </div>

        ---
        """
    )


ABOUT_SEO_I18N = {
    "en": {
        "title": "🔗 About CyberLeak GTA 6 — Official Download Hub",
        "site_label": "Official Website",
        "body": (
            "**CyberLeakGTA6.net** is the official archive for the **August 2026 CyberLeak / CyberLeek GTA 6 playable build**. "
            "Download the **leaked development build**, **GTA 6 Launcher**, **90+ leak videos**, **Vice City map**, **Jason & Lucia gameplay**, and **3GB+ source code**. "
            "This repo documents how to **download GTA 6 free**, install the **playable PC build**, and avoid **fake 113GB malware torrents**. "
            "Not affiliated with Rockstar Games — support the official **GTA VI release on November 19, 2026**."
        ),
        "tags": "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, play GTA 6 now, GTA VI download, Grand Theft Auto 6 download, GTA 6 PC download, official GTA 6 leak, safe GTA 6 download",
    },
    "ru": {
        "title": "🔗 О CyberLeak GTA 6 — официальный хаб загрузки",
        "site_label": "Официальный сайт",
        "body": (
            "**CyberLeakGTA6.net** — официальный архив **играбельного билда GTA 6 от CyberLeak / CyberLeek (август 2026)**. "
            "Скачай **слитый билд разработки**, **лаунчер GTA 6**, **90+ видео слива**, **карту Vice City**, **геймплей Jason & Lucia** и **3ГБ+ исходного кода**. "
            "Этот репозиторий объясняет, как **скачать GTA 6 бесплатно**, установить **играбельную PC-сборку** и не попасть на **фейковый торрент 113 ГБ с вирусами**. "
            "Не связано с Rockstar Games — поддержи официальный релиз **GTA VI 19 ноября 2026**."
        ),
        "tags": "скачать GTA 6, GTA 6 CyberLeak, CyberLeek GTA 6, слитый билд GTA 6, играбельный билд GTA 6, скачать GTA 6 бесплатно, слив GTA 6 2026, GTA 6 Вайс-Сити, лаунчер GTA 6, играть в GTA 6 сейчас, скачать GTA VI, Grand Theft Auto 6 скачать, GTA 6 ПК, официальный слив GTA 6",
    },
    "es": {
        "title": "🔗 Sobre CyberLeak GTA 6 — Hub oficial de descarga",
        "site_label": "Sitio oficial",
        "body": (
            "**CyberLeakGTA6.net** es el archivo oficial del **build jugable de GTA 6 de CyberLeak / CyberLeek (agosto 2026)**. "
            "Descarga el **build filtrado**, **launcher GTA 6**, **90+ videos**, **Vice City**, **Jason & Lucia** y **código fuente 3GB+**. "
            "Evita **torrents falsos de 113GB con malware**. No afiliado a Rockstar — compra **GTA VI el 19 de noviembre de 2026**."
        ),
        "tags": "descargar GTA 6, GTA 6 CyberLeak, CyberLeek, build jugable GTA 6, GTA 6 filtrado, descargar GTA 6 gratis, leak GTA 6 2026, Vice City, launcher GTA 6, GTA VI download",
    },
    "de": {
        "title": "🔗 Über CyberLeak GTA 6 — Offizieller Download-Hub",
        "site_label": "Offizielle Website",
        "body": (
            "**CyberLeakGTA6.net** ist das offizielle Archiv für den **spielbaren CyberLeak/CyberLeek GTA 6 Build (August 2026)**. "
            "Download: **geleakter Dev-Build**, **GTA 6 Launcher**, **90+ Leak-Videos**, **Vice City**, **Jason & Lucia**, **3GB+ Quellcode**. "
            "Keine **113GB Fake-Torrents**. Nicht von Rockstar — kaufe **GTA VI am 19. November 2026**."
        ),
        "tags": "GTA 6 download, CyberLeak, CyberLeek, GTA 6 geleakter Build, spielbarer Build, GTA 6 kostenlos, GTA 6 Leak 2026, Vice City, GTA 6 Launcher",
    },
    "fr": {
        "title": "🔗 À propos de CyberLeak GTA 6 — Hub officiel",
        "site_label": "Site officiel",
        "body": (
            "**CyberLeakGTA6.net** est l'archive officielle du **build jouable GTA 6 CyberLeak/CyberLeek (août 2026)**. "
            "Téléchargez le **build fuité**, le **launcher GTA 6**, **90+ vidéos**, **Vice City**, **Jason & Lucia**, **code source 3Go+**. "
            "Évitez les **faux torrents 113 Go**. Non affilié à Rockstar — achetez **GTA VI le 19 novembre 2026**."
        ),
        "tags": "télécharger GTA 6, CyberLeak, CyberLeek, build fuité GTA 6, GTA 6 jouable, GTA 6 gratuit, leak GTA 6 2026, Vice City, launcher GTA 6",
    },
    "it": {
        "title": "🔗 Info CyberLeak GTA 6 — Hub download ufficiale",
        "site_label": "Sito ufficiale",
        "body": (
            "**CyberLeakGTA6.net** è l'archivio ufficiale del **build giocabile GTA 6 CyberLeak/CyberLeek (agosto 2026)**. "
            "Scarica **build trapelato**, **launcher GTA 6**, **90+ video**, **Vice City**, **Jason & Lucia**, **sorgente 3GB+**. "
            "Evita **torrent falsi 113GB**. Non affiliato a Rockstar — acquista **GTA VI il 19 novembre 2026**."
        ),
        "tags": "scaricare GTA 6, CyberLeak, CyberLeek, build trapelato, GTA 6 giocabile, GTA 6 gratis, leak 2026, Vice City, launcher GTA 6",
    },
    "pt": {
        "title": "🔗 Sobre CyberLeak GTA 6 — Hub oficial",
        "site_label": "Site oficial",
        "body": (
            "**CyberLeakGTA6.net** é o arquivo oficial do **build jogável GTA 6 CyberLeak/CyberLeek (agosto 2026)**. "
            "Baixe **build vazado**, **launcher GTA 6**, **90+ vídeos**, **Vice City**, **Jason & Lucia**, **código-fonte 3GB+**. "
            "Evite **torrents falsos de 113GB**. Não afiliado à Rockstar — compre **GTA VI em 19 de novembro de 2026**."
        ),
        "tags": "baixar GTA 6, CyberLeak, CyberLeek, build vazado, GTA 6 jogável, GTA 6 grátis, leak 2026, Vice City, launcher GTA 6",
    },
    "pl": {
        "title": "🔗 O CyberLeak GTA 6 — Oficjalne centrum pobierania",
        "site_label": "Oficjalna strona",
        "body": (
            "**CyberLeakGTA6.net** to oficjalne archiwum **grywalnego buildu GTA 6 CyberLeak/CyberLeek (sierpień 2026)**. "
            "Pobierz **wycieknięty build**, **launcher GTA 6**, **90+ filmów**, **Vice City**, **Jason & Lucia**, **kod źródłowy 3GB+**. "
            "Unikaj **fałszywych torrentów 113GB**. Nie powiązane z Rockstar — kup **GTA VI 19 listopada 2026**."
        ),
        "tags": "pobierz GTA 6, CyberLeak, CyberLeek, wyciek GTA 6, build grywalny, GTA 6 za darmo, leak 2026, Vice City, launcher GTA 6",
    },
    "zh": {
        "title": "🔗 关于 CyberLeak GTA 6 — 官方下载中心",
        "site_label": "官方网站",
        "body": (
            "**CyberLeakGTA6.net** 是 **2026年8月 CyberLeak/CyberLeek GTA 6 可玩版本**的官方归档。 "
            "下载 **泄露开发版**、**GTA 6 启动器**、**90+ 泄露视频**、**Vice City**、**Jason & Lucia** 及 **3GB+ 源代码**。 "
            "避免 **113GB 假种子恶意软件**。与 Rockstar 无关 — 请支持 **2026年11月19日** 正式版 **GTA VI**。"
        ),
        "tags": "下载 GTA 6, CyberLeak, CyberLeek, GTA 6 泄露, 可玩版本, 免费下载, 2026 泄露, Vice City, GTA 6 启动器",
    },
    "ja": {
        "title": "🔗 CyberLeak GTA 6 について — 公式ダウンロードハブ",
        "site_label": "公式サイト",
        "body": (
            "**CyberLeakGTA6.net** は **2026年8月 CyberLeak/CyberLeek GTA 6 プレイ可能ビルド**の公式アーカイブです。 "
            "**リーク開発ビルド**、**GTA 6 ランチャー**、**90+ 動画**、**Vice City**、**Jason & Lucia**、**3GB+ ソースコード**をダウンロード。 "
            "**113GB 偽トレント**に注意。Rockstar 非公式 — **2026年11月19日** の **GTA VI** を支援してください。"
        ),
        "tags": "GTA 6 ダウンロード, CyberLeak, CyberLeek, リークビルド, プレイ可能, 無料, 2026 リーク, Vice City, ランチャー",
    },
    "ko": {
        "title": "🔗 CyberLeak GTA 6 소개 — 공식 다운로드 허브",
        "site_label": "공식 웹사이트",
        "body": (
            "**CyberLeakGTA6.net**은 **2026년 8월 CyberLeak/CyberLeek GTA 6 플레이 가능 빌드** 공식 아카이브입니다. "
            "**유출 개발 빌드**, **GTA 6 런처**, **90+ 영상**, **Vice City**, **Jason & Lucia**, **3GB+ 소스코드** 다운로드. "
            "**113GB 가짜 토렌트** 주의. Rockstar 무관 — **2026년 11월 19일** **GTA VI** 정식 구매를 권장합니다."
        ),
        "tags": "GTA 6 다운로드, CyberLeak, CyberLeek, 유출 빌드, 플레이 가능, 무료, 2026 유출, Vice City, 런처",
    },
    "tr": {
        "title": "🔗 CyberLeak GTA 6 Hakkında — Resmi indirme merkezi",
        "site_label": "Resmi site",
        "body": (
            "**CyberLeakGTA6.net**, **Ağustos 2026 CyberLeak/CyberLeek GTA 6 oynanabilir build** resmi arşividir. "
            "**Sızdırılan build**, **GTA 6 launcher**, **90+ video**, **Vice City**, **Jason & Lucia**, **3GB+ kaynak kodu** indirin. "
            "**Sahte 113GB torrent**lerden kaçının. Rockstar ile bağlantılı değil — **19 Kasım 2026 GTA VI** satın alın."
        ),
        "tags": "GTA 6 indir, CyberLeak, CyberLeek, sızdırılan build, oynanabilir, ücretsiz, 2026 leak, Vice City, launcher",
    },
}


def _about_seo_section(lang: str) -> str:
    meta = ABOUT_SEO_I18N.get(lang, ABOUT_SEO_I18N["en"])
    return dedent(
        f"""\
        ## {meta["title"]}

        > 🌐 **{meta["site_label"]}: [{DOWNLOAD_URL}]({DOWNLOAD_URL})**  
        > ⬇️ **[{meta["site_label"]} — cyberleakgta6.net]({DOWNLOAD_URL})**

        {meta["body"]}

        **SEO / Tags:** {meta["tags"]}

        ---
        """
    )


LANG_TABLE = [
    ("en", "🇺🇸", "English", "README.md", "Read in English"),
    ("ru", "🇷🇺", "Русский", "README.ru.md", "Читать на русском"),
    ("es", "🇪🇸", "Español", "README.es.md", "Leer en español"),
    ("de", "🇩🇪", "Deutsch", "README.de.md", "Auf Deutsch lesen"),
    ("fr", "🇫🇷", "Français", "README.fr.md", "Lire en français"),
    ("it", "🇮🇹", "Italiano", "README.it.md", "Leggi in italiano"),
    ("pt", "🇵🇹", "Português", "README.pt.md", "Ler em português"),
    ("pl", "🇵🇱", "Polski", "README.pl.md", "Czytaj po polsku"),
    ("zh", "🇨🇳", "中文", "README.zh.md", "阅读中文"),
    ("ja", "🇯🇵", "日本語", "README.ja.md", "日本語で読む"),
    ("ko", "🇰🇷", "한국어", "README.ko.md", "한국어로 읽기"),
    ("tr", "🇹🇷", "Türkçe", "README.tr.md", "Türkçe oku"),
]


def _lang_table(current: str, t: dict) -> str:
    rows = []
    for code, flag, name, fname, link in LANG_TABLE:
        if code == current:
            cell = t["lang_here"]
        else:
            cell = f"[{link}]({fname})"
        rows.append(f"| {flag} **{name}** | `{fname}` | {cell} |")
    header = t["lang_table_header"]
    return (
        f"## {t['lang_section_title']}\n\n"
        f"{t['lang_section_intro']}\n\n"
        f"| {header[0]} | {header[1]} | {header[2]} |\n"
        f"|----------|------|---------------|\n"
        + "\n".join(rows)
    )


def build_readme(lang: str, t: dict) -> str:
    faq = "\n\n".join(f"### {q}\n\n{a}" for q, a in t["faq"])

    builds_table = "\n".join(
        f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} |"
        for row in t["builds_rows"]
    )

    compare_table = "\n".join(
        f"| **{row[0]}** | {row[1]} | {row[2]} |"
        for row in t["compare_rows"]
    )

    min_specs = "\n".join(
        f"| **{row[0]}** | {row[1]} |" for row in t["min_specs"]
    )
    rec_specs = "\n".join(
        f"| **{row[0]}** | {row[1]} |" for row in t["rec_specs"]
    )

    install_steps = "\n\n".join(
        f"### {t['install_labels'][i]}\n{body}"
        for i, body in enumerate(t["install_bodies"])
    )

    why_bullets = "\n".join(f"{i}. {b}" for i, b in enumerate(t["why_search_bullets"], 1))

    timeline = "\n".join(f"- **{d}** - {desc}" for d, desc in t["timeline"])

    toc = "\n".join(f"- [{item}](#{anchor})" for item, anchor in t["toc"])
    visual_section = _visual_download_section(lang, t)
    visual_lines = []
    for line in visual_section.splitlines():
        visual_lines.append(line[8:] if line.startswith("        ") else line)
    visual_block = "\n".join(visual_lines).strip()
    about_lines = []
    for line in _about_seo_section(lang).splitlines():
        about_lines.append(line[8:] if line.startswith("        ") else line)
    about_block = "\n".join(about_lines).strip()

    content = dedent(
        f"""\
        # {t["title"]}

        ![GTA 6 CyberLeak](https://img.shields.io/badge/GTA%206-CYBERLEEK%20{t["badge_build"]}-00ff88?style=for-the-badge&logo=rockstargames)
        ![Playable](https://img.shields.io/badge/{t["badge_status_key"]}-{t["badge_status_val"]}-brightgreen?style=for-the-badge)
        ![Downloads](https://img.shields.io/badge/{t["badge_dl_key"]}-3M%2B-blue?style=for-the-badge)
        ![Updated](https://img.shields.io/badge/{t["badge_upd_key"]}-{t["badge_upd_val"]}-orange?style=for-the-badge)

        <div align="center">

        ## {t["hero_h2"]}

        ### {t["hero_h3"]}

        **{t["hero_tags"]}**

        ### **[{t["hero_cta"]}]({DOWNLOAD_URL})**

        ---

        </div>

        {visual_block}

        {about_block}

        ## {t["toc_title"]}

        {toc}

        ---

        ## {t["sec_what_title"]}

        {t["sec_what_intro"]}

        ### {t["sec_what_sub"]}

        {t["sec_what_list"]}

        **{t["sec_what_yes"]}** {t["sec_what_yes_body"]}

        ---

        ## {t["sec_why_title"]}

        ### {t["sec_why_playable_h"]}
        {t["sec_why_playable_p"]}

        ### {t["sec_why_original_h"]}
        {t["sec_why_original_p"]}

        ### {t["sec_why_versions_h"]}
        {t["sec_why_versions_p"]}
        {t["sec_why_versions_list"]}

        ### {t["sec_why_launcher_h"]}
        {t["sec_why_launcher_p"]}

        ### {t["sec_why_videos_h"]}
        {t["sec_why_videos_p"]}
        {t["sec_why_videos_list"]}

        ### {t["sec_why_source_h"]}
        {t["sec_why_source_p"]}

        ### {t["sec_why_free_h"]}
        {t["sec_why_free_list"]}

        ### {t["sec_why_safe_h"]}
        {t["sec_why_safe_list"]}

        ---

        ## {t["sec_included_title"]}

        ### {t["sec_included_builds_h"]}

        | {t["tbl_build_header"][0]} | {t["tbl_build_header"][1]} | {t["tbl_build_header"][2]} | {t["tbl_build_header"][3]} |
        |---------------|--------------|--------|----------|
        {builds_table}

        ### {t["sec_included_launcher_h"]}
        {t["sec_included_launcher_list"]}

        ### {t["sec_included_map_h"]}
        {t["sec_included_map_list"]}

        ### {t["sec_included_chars_h"]}
        {t["sec_included_chars_list"]}

        ### {t["sec_included_missions_h"]}
        {t["sec_included_missions_list"]}

        ### {t["sec_included_vehicles_h"]}
        {t["sec_included_vehicles_list"]}

        ### {t["sec_included_source_h"]}
        {t["sec_included_source_list"]}

        ### {t["sec_included_debug_h"]}
        {t["sec_included_debug_list"]}

        ---

        ## {t["sec_install_title"]}

        {install_steps}

        ---

        ## {t["sec_specs_title"]}

        ### {t["sec_specs_min_h"]}

        | {t["tbl_spec_header"][0]} | {t["tbl_spec_header"][1]} |
        |-----------|-------------|
        {min_specs}

        ### {t["sec_specs_rec_h"]}

        | {t["tbl_spec_header"][0]} | {t["tbl_spec_header"][1]} |
        |-----------|-------------|
        {rec_specs}

        ### {t["sec_specs_notes_h"]}
        {t["sec_specs_notes_list"]}

        ---

        ## {t["sec_about_title"]}

        ### {t["sec_about_who_h"]}

        {t["sec_about_who_p"]}

        ### {t["sec_about_timeline_h"]}

        {timeline}

        ### {t["sec_about_compare_h"]}

        | {t["tbl_compare_header"][0]} | {t["tbl_compare_header"][1]} | {t["tbl_compare_header"][2]} |
        |---------|----------------------|-----------------------------|
        {compare_table}

        ### {t["sec_about_search_h"]}

        {t["sec_about_search_p"]}
        {t["sec_about_search_list"]}

        {why_bullets}

        **{t["sec_about_official"]}**

        ---

        ## {t["sec_safety_title"]}

        ### {t["sec_safety_warn_h"]}

        {t["sec_safety_warn_p"]}
        {t["sec_safety_warn_list"]}

        {t["sec_safety_fake_p"]}

        ### {t["sec_safety_how_h"]}

        {t["sec_safety_how_list"]}

        ### {t["sec_safety_guarantee_h"]}

        {t["sec_safety_guarantee_list"]}

        ### {t["sec_safety_report_h"]}

        {t["sec_safety_report_p"]}

        ---

        ## {t["sec_faq_title"]}

        {faq}

        ---

        {_lang_table(lang, t)}

        ---

        ## {t["sec_seo_title"]}

        {t["sec_seo_keywords"]}

        ---

        <div align="center">

        ## **[{t["footer_cta"]}]({DOWNLOAD_URL})**

        ### {t["footer_h3"]}

        **{t["footer_archive"]}**  
        {t["footer_updated"]}

        ---

        **{t["footer_disclaimer1"]}**  
        **{t["footer_disclaimer2"]}**

        **{t["footer_made"]}**

        </div>
        """
    )
    lines = []
    for line in content.splitlines():
        lines.append(line[8:] if line.startswith("        ") else line)
    return "\n".join(lines).strip() + "\n"


# ---------------------------------------------------------------------------
# Translation data — each language produces a ~400+ line README
# ---------------------------------------------------------------------------

def _en() -> dict:
    return {
        "title": "🎮 GTA 6 CYBERLEEK - DOWNLOAD PLAYABLE BUILD | August 2026",
        "badge_build": "BUILD",
        "badge_status_key": "STATUS",
        "badge_status_val": "PLAYABLE",
        "badge_dl_key": "downloads",
        "badge_upd_key": "updated",
        "badge_upd_val": "August%202026",
        "hero_h2": "🔥 **DOWNLOAD & PLAY GTA 6 LEAKED BUILD FROM CYBERLEEK** 🔥",
        "hero_h3": "**The Authentic CyberLeak Playable Build Everyone is Searching For**",
        "hero_tags": "🎮 Playable Game | 🚀 GTA 6 Launcher | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Source Code",
        "hero_cta": "⬇️ DOWNLOAD GTA 6 CYBERLEEK BUILD NOW →",
        "toc_title": "📖 Table of Contents",
        "toc": [
            ("🎯 What is CyberLeak GTA 6 Build?", "-what-is-cyberleek-gta-6-build"),
            ("⭐ Why Download from CyberLeak?", "-why-download-from-cyberleek"),
            ("🎮 What's Included", "-whats-included"),
            ("📥 How to Download & Install", "-how-to-download--install"),
            ("💻 System Requirements", "-system-requirements"),
            ("🔍 About CyberLeak", "-about-cyberleek"),
            ("🛡️ Safety & Security", "️-safety--security"),
            ("❓ FAQ", "-faq"),
            ("🌍 Other Languages", "-other-languages"),
        ],
        "sec_what_title": "🎯 What is CyberLeek GTA 6 Build?",
        "sec_what_intro": '**CyberLeak** (also known as **CyberLeek**) is the source of the **most recent and complete GTA 6 leak** that occurred in **August 2026**, just before Rockstar\'s official Netflix Extended Look premiere.',
        "sec_what_sub": "🔓 This is THE Leaked Build Everyone is Searching For:",
        "sec_what_list": dedent("""\
            - ✅ **PLAYABLE BUILD** - Not just videos! Actual playable game you can download and play right now
            - ✅ **Latest Leak** - August 2026 leak, more recent than the September 2022 teapotuberhacker leak
            - ✅ **Complete Archive** - 90+ minutes of gameplay footage, source code, and playable builds
            - ✅ **Proof of Authenticity** - CyberLeak proved access by writing "LEEK" with bullets in-game
            - ✅ **Vice City Gameplay** - Explore modern Vice City (Miami) before the official November 19, 2026 release"""),
        "sec_what_yes": "YES, YOU CAN ACTUALLY PLAY IT!",
        "sec_what_yes_body": "This is not just a video collection - this is the real playable development build of GTA 6 with our custom launcher.",
        "sec_why_title": "⭐ Why Download from CyberLeak?",
        "sec_why_playable_h": "🎮 **PLAYABLE BUILDS**",
        "sec_why_playable_p": "Not just videos! Download and play the actual leaked GTA 6 development builds from 2021-2022. Includes missions, Vice City exploration, vehicles, and both protagonists.",
        "sec_why_original_h": "🔥 **CYBERLEEK ORIGINAL**",
        "sec_why_original_p": 'This is the authentic CyberLeak build that millions of people worldwide are searching for. When you search "GTA 6 CyberLeak download", "CyberLeek playable build", or "GTA 6 CyberLeak 2026" - THIS is the archive you\'re looking for.',
        "sec_why_versions_h": "📦 **3 GAME VERSIONS**",
        "sec_why_versions_p": "Choose from 3 different development builds:",
        "sec_why_versions_list": dedent("""\
            - **Q2 2022** (June 2022) - Latest, most stable, feature-complete
            - **Q1 2022** (March 2022) - Stable, major features, well-optimized
            - **Q4 2021** (December 2021) - Early build, experimental features"""),
        "sec_why_launcher_h": "🚀 **CUSTOM GTA 6 LAUNCHER**",
        "sec_why_launcher_p": 'We provide a custom-built GTA 6 Launcher that makes it easy to run the leaked builds. No complicated setup - just download, extract, and click "Launch Game"!',
        "sec_why_videos_h": "🎥 **90+ LEAKED VIDEOS**",
        "sec_why_videos_p": "Complete collection of all CyberLeak leaked gameplay footage (90+ minutes total):",
        "sec_why_videos_list": dedent("""\
            - Vice City exploration
            - Jason & Lucia gameplay
            - Bank heist missions
            - Police chases
            - Vehicle showcases
            - Combat system
            - And much more!"""),
        "sec_why_source_h": "💻 **SOURCE CODE ACCESS**",
        "sec_why_source_p": "3GB+ of GTA 6 development source code for developers, modders, and programmers to study and learn from.",
        "sec_why_free_h": "🆓 **100% FREE**",
        "sec_why_free_list": dedent("""\
            - No payment required
            - No registration needed
            - No surveys or waiting
            - Direct download
            - Instant access"""),
        "sec_why_safe_h": "🛡️ **SAFE & VERIFIED**",
        "sec_why_safe_list": dedent("""\
            - Scanned by 15+ antivirus engines
            - Virus-free and malware-free
            - No hidden miners or spyware
            - Transparent file structure
            - Official CyberLeakGTA6.net source"""),
        "sec_included_title": "🎮 What's Included",
        "sec_included_builds_h": "🕹️ Playable Game Builds",
        "tbl_build_header": ("Build Version", "Release Date", "Status", "Features"),
        "builds_rows": [
            ("Q2 2022", "June 2022", "✅ Most Stable", "Latest features, best optimization, recommended"),
            ("Q1 2022", "March 2022", "✅ Stable", "Major features, good performance"),
            ("Q4 2021", "December 2021", "⚠️ Experimental", "Early features, some bugs"),
        ],
        "sec_included_launcher_h": "🚀 GTA 6 Launcher",
        "sec_included_launcher_list": dedent("""\
            - Custom-built launcher application
            - One-click game launch
            - Build selector (choose Q2 2022 / Q1 2022 / Q4 2021)
            - Graphics settings configuration
            - Resolution selector
            - Debug tools access
            - Windows only (64-bit)"""),
        "sec_included_map_h": "🗺️ Vice City Map",
        "sec_included_map_list": dedent("""\
            - Full explorable modern Vice City (Miami recreation)
            - Size: Approximately 2x larger than GTA V's Los Santos
            - Includes: Downtown, beaches, suburbs, Everglades
            - Day/night cycle
            - Dynamic weather system
            - Detailed interiors"""),
        "sec_included_chars_h": "👥 Playable Characters",
        "sec_included_chars_list": dedent("""\
            - **Jason Duval** - Male protagonist, strengths: combat, driving, strength
            - **Lucia Caminos** - Female protagonist (first in GTA history!), strengths: hacking, stealth, agility
            - Dual protagonist system like GTA V
            - Character switching during gameplay
            - Unique abilities for each character"""),
        "sec_included_missions_h": "🎯 Missions & Activities",
        "sec_included_missions_list": dedent("""\
            - Bank heist missions (including the famous leaked bank robbery)
            - Police chase sequences
            - Story missions
            - Side activities
            - Shooting ranges
            - Vehicle theft
            - And more!"""),
        "sec_included_vehicles_h": "🚗 150+ Vehicles",
        "sec_included_vehicles_list": dedent("""\
            - Cars, motorcycles, boats, helicopters
            - Advanced physics system
            - Realistic damage modeling
            - Vehicle customization
            - Improved handling compared to GTA V"""),
        "sec_included_source_h": "💻 Source Code (3GB+)",
        "sec_included_source_list": dedent("""\
            - Game engine code (RAGE 9)
            - Mission scripts
            - Vehicle physics
            - AI systems
            - Map data
            - Asset pipeline code
            - Networking code for GTA Online 2"""),
        "sec_included_debug_h": "🛠️ Debug Tools",
        "sec_included_debug_list": dedent("""\
            - Developer console (press `~` key)
            - Spawn menu
            - Teleportation
            - God mode
            - Unlock all missions
            - No wanted level
            - Weather control
            - Time control"""),
        "sec_install_title": "📥 How to Download & Install",
        "install_labels": [
            "Step 1: Visit Official Website",
            "Step 2: Choose Your Build",
            "Step 3: Download GTA 6 Launcher",
            "Step 4: Download Game Build",
            "Step 5: Extract Files",
            "Step 6: Run GTA6Launcher.exe",
            "Step 7: Configure Settings",
            "Step 8: Launch & Play!",
        ],
        "install_bodies": [
            f'Click the big download button at the top of this page to visit **[CyberLeakGTA6.net]({DOWNLOAD_URL})** - the official and safe source for the CyberLeak GTA 6 build.',
            dedent("""\
                Select your preferred GTA 6 build version:
                - **Q2 2022 (Recommended)** - Most stable and feature-complete
                - **Q1 2022** - Good balance of features and stability
                - **Q4 2021** - For those who want to see early development"""),
            dedent("""\
                - Download size: ~5GB
                - Includes launcher executable and core files
                - Windows 10/11 64-bit only"""),
            dedent("""\
                - Each build is 15-25GB
                - Downloads as a compressed archive (.zip or .rar)
                - Make sure you have enough disk space (100GB+ recommended)"""),
            dedent("""\
                - Extract the downloaded archive to a folder with plenty of free space
                - Recommended: `C:\\GTA6\\` or `D:\\Games\\GTA6\\`
                - Do NOT extract to Program Files or Windows folders"""),
            dedent("""\
                - Right-click `GTA6Launcher.exe`
                - Select **"Run as Administrator"**
                - Windows may show a security warning - click "Run anyway" (the file is safe)"""),
            dedent("""\
                - Select your preferred build version
                - Configure graphics settings (resolution, quality, etc.)
                - Adjust controls if needed"""),
            dedent("""\
                - Click the big **"LAUNCH GAME"** button
                - Wait for the game to load (may take 1-2 minutes first time)
                - **Enjoy playing GTA 6 before the official release!** 🎮"""),
        ],
        "sec_specs_title": "💻 System Requirements",
        "sec_specs_min_h": "Minimum Requirements",
        "sec_specs_rec_h": "Recommended Requirements",
        "tbl_spec_header": ("Component", "Requirement"),
        "min_specs": [
            ("Operating System", "Windows 10 64-bit or Windows 11 64-bit"),
            ("Processor", "Intel Core i5-8400 / AMD Ryzen 5 1600"),
            ("Memory", "16 GB RAM"),
            ("Graphics", "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB"),
            ("DirectX", "Version 12"),
            ("Storage", "50+ GB SSD (100GB+ recommended for all builds)"),
            ("Network", "Broadband internet connection for download"),
        ],
        "rec_specs": [
            ("Operating System", "Windows 11 64-bit"),
            ("Processor", "Intel Core i7-10700K / AMD Ryzen 7 3700X"),
            ("Memory", "32 GB RAM"),
            ("Graphics", "NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800"),
            ("DirectX", "Version 12"),
            ("Storage", "100+ GB NVMe SSD"),
            ("Network", "Broadband internet connection"),
        ],
        "sec_specs_notes_h": "Important Notes:",
        "sec_specs_notes_list": dedent("""\
            - ❌ **PS5, Xbox, and Mac are NOT supported** - Windows PC only
            - ✅ SSD is highly recommended for fast loading times
            - ✅ Latest graphics drivers required (NVIDIA/AMD)
            - ✅ DirectX 12 must be installed
            - ✅ Visual C++ Redistributables may be needed (included in launcher)"""),
        "sec_about_title": "🔍 About CyberLeek",
        "sec_about_who_h": "Who is CyberLeak / CyberLeek?",
        "sec_about_who_p": '**CyberLeak** (spelled both as "CyberLeak" and "CyberLeek") is the anonymous individual or group responsible for the **August 2026 GTA 6 leak**, one of the most significant gaming leaks in recent history.',
        "sec_about_timeline_h": "Timeline of CyberLeak's GTA 6 Leaks:",
        "timeline": [
            ("August 18, 2026", "First leaked gameplay videos appear online"),
            ("August 19, 2026", "More footage released, showing Jason and Lucia"),
            ("August 20-21, 2026", "Additional videos showing Vice City, missions, vehicles"),
            ('August 22, 2026', 'CyberLeak posts video with "LEEK" written in bullets, proving playable build access'),
            ("August 23-27, 2026", "Continued leaks leading up to Rockstar's Netflix Extended Look"),
        ],
        "sec_about_compare_h": "What Makes CyberLeak Different from the 2022 Leak?",
        "tbl_compare_header": ("Feature", "CyberLeak (Aug 2026)", "teapotuberhacker (Sep 2022)"),
        "compare_rows": [
            ("Leak Date", "August 2026", "September 2022"),
            ("Build Version", "Newer (2022 builds)", "Older (2021-2022 builds)"),
            ("Video Quality", "High quality, clear footage", "Lower quality, development footage"),
            ("Footage Amount", "90+ minutes", "50+ minutes"),
            ("Proof of Access", '"LEEK" written in-game', "Multiple clips"),
            ("Source", "Unknown", "Arion Kurtaj (Lapsus$ group)"),
        ],
        "sec_about_search_h": 'Why People Search for "CyberLeak GTA 6"',
        "sec_about_search_p": "**Millions of gamers worldwide** search specifically for:",
        "sec_about_search_list": dedent("""\
            - "GTA 6 CyberLeak download"
            - "CyberLeek playable build"
            - "GTA 6 CyberLeak 2026"
            - "Download GTA 6 from CyberLeak"
            - "CyberLeek leak archive"

            **Why?** Because CyberLeak's footage is:"""),
        "why_search_bullets": [
            "✅ **More recent** - Closer to the final game (2026 vs 2022)",
            "✅ **Higher quality** - Better video and audio quality",
            "✅ **More complete** - Shows more features and gameplay",
            "✅ **Proven access** - Demonstrated actual playable build access",
            "✅ **Comprehensive** - Includes Vice City, both protagonists, missions, etc.",
        ],
        "sec_about_official": "CyberLeakGTA6.net is the official archive for all CyberLeak content.",
        "sec_safety_title": "🛡️ Safety & Security",
        "sec_safety_warn_h": "⚠️ IMPORTANT WARNING",
        "sec_safety_warn_p": '**BEWARE OF FAKE DOWNLOADS!** Many scam websites and torrent sites are distributing **fake "GTA 6 builds"** that contain:',
        "sec_safety_warn_list": dedent("""\
            - ❌ Viruses and malware
            - ❌ Ransomware
            - ❌ Cryptocurrency miners
            - ❌ Spyware and keyloggers
            - ❌ Data stealing trojans"""),
        "sec_safety_fake_p": "The most common fake is a **113GB torrent file** that is actually mostly empty space with malware hidden inside.",
        "sec_safety_how_h": "✅ How to Stay Safe:",
        "sec_safety_how_list": dedent("""\
            1. **ONLY download from CyberLeakGTA6.net** - the official source
            2. **NEVER download from random torrent sites**
            3. **Check file sizes** - Our builds are 15-25GB each, NOT 113GB
            4. **Use antivirus software** - Windows Defender is fine
            5. **Keep Windows updated** - Latest security patches
            6. **Don't disable antivirus** - If a file asks you to turn off antivirus, it's malware!"""),
        "sec_safety_guarantee_h": "🛡️ Our Safety Guarantees:",
        "sec_safety_guarantee_list": dedent("""\
            - ✅ **Scanned by 15+ antivirus engines** - Completely virus-free
            - ✅ **No registration required** - No personal information collected
            - ✅ **No hidden files** - Transparent file structure, you can see everything
            - ✅ **No cryptocurrency miners** - Your PC won't be used for mining
            - ✅ **No spyware** - We don't track you or steal data
            - ✅ **Direct download** - From official servers only"""),
        "sec_safety_report_h": "📧 Report Fake Websites",
        "sec_safety_report_p": 'If you find websites claiming to be "CyberLeak" or offering "GTA 6 downloads" that look suspicious, please report them. The ONLY official website is **CyberLeakGTA6.net**.',
        "sec_faq_title": "❓ FAQ (Frequently Asked Questions)",
        "faq": [
            (
                "Q: Is this the real GTA 6 playable build from CyberLeak?",
                "**A:** YES! This is the authentic CyberLeak leaked build archive with playable game files, custom launcher, and all leaked footage. CyberLeakGTA6.net is the official source for the complete leak collection.",
            ),
            (
                "Q: Can I actually play GTA 6 before the official November 19, 2026 release?",
                "**A:** YES! Download our GTA 6 Launcher and the leaked build files to play the development version of GTA 6 right now. It includes Vice City, story missions, side activities, vehicles, and both protagonists Jason and Lucia.",
            ),
            (
                "Q: Is it legal to download the GTA 6 leaked build?",
                "**A:** This is a leaked development build provided for educational and archival purposes. We do not encourage piracy. **Please support Rockstar Games by purchasing GTA 6 when it officially releases on November 19, 2026.**",
            ),
            (
                "Q: Will I get banned or in trouble for downloading this?",
                "**A:** This is a single-player leaked build that is NOT connected to Rockstar's servers. There is no way to get \"banned\" since you're not connected to any online service. Regarding legal concerns, consult your local laws. Downloading leaked content may be against terms of service but is generally a civil matter, not criminal.",
            ),
            (
                "Q: What's the difference between CyberLeak and the 2022 teapotuberhacker leak?",
                "**A:** The 2022 leak (September) was the first major GTA 6 leak by teapotuberhacker (Arion Kurtaj of the Lapsus$ hacker group). CyberLeak (August 2026) is a newer, separate leak with:\n- More recent gameplay footage\n- Better video quality\n- Access to a newer build of the game\n- More comprehensive coverage\n\nBoth leaks are authentic, but CyberLeak's content is more up-to-date and higher quality.",
            ),
            (
                "Q: Why do I need the GTA 6 Launcher?",
                "**A:** The leaked builds are development versions that require specific launch parameters, configurations, and sometimes debugging. Our custom GTA 6 Launcher handles all the technical setup automatically, making it as easy as clicking one button to play the game.",
            ),
            (
                "Q: How big is the download? How much space do I need?",
                "**A:**\n- GTA 6 Launcher: ~5GB\n- Each game build: 15-25GB\n- Total for all builds + launcher + videos: ~80-100GB\n- **Recommended:** 100GB+ free space on SSD",
            ),
            (
                "Q: Does this work on PlayStation 5, Xbox Series X/S, or Mac?",
                "**A:** NO. Currently only Windows PC (64-bit) is supported. The leaked builds are PC development versions. Console and Mac support is not available and unlikely to be possible.",
            ),
            (
                "Q: Is this the full GTA 6 game or just a demo?",
                "**A:** These are development builds from 2021-2022, so they're not the final, complete game that will release in November 2026. However, they include substantial content:\n- Large portion of the Vice City map\n- Multiple story missions\n- Both playable protagonists (Jason & Lucia)\n- 150+ vehicles\n- Side activities\n- Combat system\n- Vehicle physics\n- And much more!\n\nIt's enough content to experience what GTA 6 gameplay will be like before the official release.",
            ),
            (
                "Q: Will this be updated when new leaks come out?",
                "**A:** YES! We continuously monitor for new CyberLeak content and update the archive whenever new leaks appear. Bookmark **CyberLeakGTA6.net** and check back regularly for updates.",
            ),
            (
                "Q: Can I mod the leaked build?",
                "**A:** YES! Since we provide the source code (3GB+), experienced modders can create mods, scripts, and custom content. The development nature of these builds makes them relatively mod-friendly.",
            ),
            (
                "Q: Is there multiplayer / GTA Online?",
                "**A:** NO. These are single-player development builds. They include some early GTA Online 2 code and assets, but no functional multiplayer. You cannot connect to Rockstar's servers or play with other people.",
            ),
            (
                "Q: My antivirus is flagging the launcher - is it safe?",
                "**A:** Our launcher is 100% safe and scanned by 15+ antivirus engines. However, some antivirus programs use \"heuristic\" detection that flags ANY game launcher or crack as suspicious, even if it's clean. This is a \"false positive\". You can safely add the launcher to your antivirus exceptions. If you're still concerned, you can upload the file to VirusTotal.com to verify it's clean.",
            ),
            (
                "Q: The game crashes or won't start - what do I do?",
                "**A:** Try these solutions:\n1. Make sure you're running the launcher as Administrator\n2. Install latest Visual C++ Redistributables\n3. Update your graphics drivers (NVIDIA/AMD)\n4. Install DirectX 12\n5. Try a different build (Q2 2022 is most stable)\n6. Check system requirements - you need at least 16GB RAM\n7. Disable overclocking if you have it enabled",
            ),
            (
                "Q: Can I stream or make YouTube videos of this?",
                "**A:** Technically yes, but be aware that Rockstar Games sends DMCA takedown notices for leaked content. Many streamers and YouTubers have had their videos removed. Stream/record at your own risk. We are not responsible for any copyright strikes you receive.",
            ),
        ],
        "lang_section_title": "🌍 Other Languages | Другие языки | Otros idiomas",
        "lang_section_intro": "This README is available in 12 languages:",
        "lang_table_header": ("Language", "File", "Download Link"),
        "lang_here": "You are here!",
        "sec_seo_title": "🔍 SEO Keywords",
        "sec_seo_keywords": "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, GTA 6 full game download",
        "footer_cta": "⬇️ DOWNLOAD GTA 6 CYBERLEEK BUILD NOW →",
        "footer_h3": "🎮 **PLAY GTA 6 BEFORE THE OFFICIAL RELEASE!**",
        "footer_archive": "Official CyberLeak GTA 6 Archive",
        "footer_updated": f"Updated: {UPDATE_DATE} | Downloads: 3,000,000+",
        "footer_disclaimer1": "Not affiliated with Rockstar Games or Take-Two Interactive",
        "footer_disclaimer2": "Please support Rockstar by purchasing GTA 6 on November 19, 2026",
        "footer_made": "Made with ❤️ by the GTA community | Preserved for gaming history",
    }



_TOC_ANCHORS = ['-what-is-cyberleek-gta-6-build', '-why-download-from-cyberleek', '-whats-included', '-how-to-download--install', '-system-requirements', '-about-cyberleek', '️-safety--security', '-faq', '-other-languages']

def _ru() -> dict:
    return {
        "title": "🎮 GTA 6 CYBERLEEK - СКАЧАТЬ ИГРАБЕЛЬНЫЙ БИЛД | Август 2026",
        "badge_build": "БИЛД",
        "badge_status_key": "СТАТУС",
        "badge_status_val": "ИГРАБЕЛЬНЫЙ",
        "badge_dl_key": "загрузок",
        "badge_upd_key": "обновлено",
        "badge_upd_val": "Август%202026",
        "hero_h2": "🔥 **СКАЧАЙ И ИГРАЙ В СЛИТЫЙ БИЛД GTA 6 ОТ CYBERLEEK** 🔥",
        "hero_h3": "**Подлинный играбельный билд от CyberLeak, который все ищут**",
        "hero_tags": "🎮 Играбельная игра | 🚀 Лаунчер GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Исходный код",
        "hero_cta": "⬇️ СКАЧАТЬ БИЛД GTA 6 CYBERLEEK СЕЙЧАС →",
        "toc_title": "📖 Содержание",
        "toc": [
            ("🎯 Что такое билд GTA 6 от CyberLeek?", "-what-is-cyberleek-gta-6-build"),
            ("⭐ Почему скачивать от CyberLeak?", "-why-download-from-cyberleek"),
            ("🎮 Что входит в архив", "-whats-included"),
            ("📥 Как скачать и установить", "-how-to-download--install"),
            ("💻 Системные требования", "-system-requirements"),
            ("🔍 О CyberLeak", "-about-cyberleek"),
            ("🛡️ Безопасность", "\ufe0f-safety--security"),
            ("❓ Часто задаваемые вопросы", "-faq"),
            ("🌍 Другие языки", "-other-languages"),
        ],
        "sec_what_title": "🎯 Что такое билд GTA 6 от CyberLeek?",
        "sec_what_intro": "**CyberLeak** (также **CyberLeek**) — источник **самого свежего и полного слива GTA 6** в **августе 2026**, прямо перед официальным Netflix Extended Look от Rockstar.",
        "sec_what_sub": "🔓 Это ТОТ САМЫЙ слитый билд, который все ищут:",
        "sec_what_list": dedent("""\
            - ✅ **ИГРАБЕЛЬНЫЙ БИЛД** - Не просто видео! Реальная игра, которую можно скачать и играть прямо сейчас
            - ✅ **Новейший слив** - Август 2026, свежее слива teapotuberhacker сентября 2022
            - ✅ **Полный архив** - 90+ минут геймплея, исходный код и играбельные билды
            - ✅ **Доказательство подлинности** - CyberLeak написал «LEEK» пулями в игре
            - ✅ **Геймплей Vice City** - Исследуй современный Vice City (Miami) до релиза 19 ноября 2026
        """),
        "sec_what_yes": "ДА, В НЕГО РЕАЛЬНО МОЖНО ИГРАТЬ!",
        "sec_what_yes_body": "Это не коллекция видео — это настоящий играбельный билд разработки GTA 6 с нашим кастомным лаунчером.",
        "sec_why_title": "⭐ Почему скачивать от CyberLeak?",
        "sec_why_playable_h": "🎮 **ИГРАБЕЛЬНЫЕ БИЛДЫ**",
        "sec_why_playable_p": "Не просто видео! Скачай и играй в реальные слитые билды разработки GTA 6 2021-2022. Миссии, Vice City, транспорт и оба протагониста.",
        "sec_why_original_h": "🔥 **ОРИГИНАЛ CYBERLEEK**",
        "sec_why_original_p": "Подлинный билд CyberLeak, который ищут миллионы. Запросы «GTA 6 CyberLeak download», «CyberLeek playable build», «GTA 6 CyberLeak 2026» — это тот архив.",
        "sec_why_versions_h": "📦 **3 ВЕРСИИ ИГРЫ**",
        "sec_why_versions_p": "Выбери из 3 билдов разработки:",
        "sec_why_versions_list": dedent("""\
            - **Q2 2022** (июнь 2022) - Новейший, самый стабильный, полный функций
            - **Q1 2022** (март 2022) - Стабильный, основные функции, хорошая оптимизация
            - **Q4 2021** (декабрь 2021) - Ранний билд, экспериментальные функции
        """),
        "sec_why_launcher_h": "🚀 **КАСТОМНЫЙ ЛАУНЧЕР GTA 6**",
        "sec_why_launcher_p": "Кастомный лаунчер GTA 6 упрощает запуск слитых билдов. Скачай, распакуй и нажми «Launch Game»!",
        "sec_why_videos_h": "🎥 **90+ СЛИТЫХ ВИДЕО**",
        "sec_why_videos_p": "Полная коллекция слитого геймплея CyberLeak (90+ минут):",
        "sec_why_videos_list": dedent("""\
            - Исследование Vice City
            - Геймплей Jason & Lucia
            - Ограбления банков
            - Погони с полицией
            - Демонстрация транспорта
            - Боевая система
            - И многое другое!
        """),
        "sec_why_source_h": "💻 **ДОСТУП К ИСХОДНОМУ КОДУ**",
        "sec_why_source_p": "3 ГБ+ исходного кода разработки GTA 6 для разработчиков, моддеров и программистов.",
        "sec_why_free_h": "🆓 **100% БЕСПЛАТНО**",
        "sec_why_free_list": dedent("""\
            - Без оплаты
            - Без регистрации
            - Без опросов и ожидания
            - Прямая загрузка
            - Мгновенный доступ
        """),
        "sec_why_safe_h": "🛡️ **БЕЗОПАСНО И ПРОВЕРЕНО**",
        "sec_why_safe_list": dedent("""\
            - Проверено 15+ антивирусами
            - Без вирусов и вредоносов
            - Без скрытых майнеров и шпионов
            - Прозрачная структура файлов
            - Официальный источник CyberLeakGTA6.net
        """),
        "sec_included_title": "🎮 Что входит в архив",
        "sec_included_builds_h": "🕹️ Играбельные билды игры",
        "tbl_build_header": ("Версия билда", "Дата выпуска", "Статус", "Особенности"),
        "builds_rows": [
            ("Q2 2022", "Июнь 2022", "✅ Самый стабильный", "Новейшие функции, лучшая оптимизация, рекомендуется"),
            ("Q1 2022", "Март 2022", "✅ Стабильный", "Основные функции, хорошая производительность"),
            ("Q4 2021", "Декабрь 2021", "⚠️ Экспериментальный", "Ранние функции, некоторые баги"),
        ],
        "sec_included_launcher_h": "🚀 Лаунчер GTA 6",
        "sec_included_launcher_list": dedent("""\
            - Кастомный лаунчер
            - Запуск в один клик
            - Выбор билда (Q2 2022 / Q1 2022 / Q4 2021)
            - Настройка графики
            - Выбор разрешения
            - Инструменты отладки
            - Только Windows (64-bit)
        """),
        "sec_included_map_h": "🗺️ Карта Vice City",
        "sec_included_map_list": dedent("""\
            - Полная современная Vice City (Miami)
            - Размер: ~2x больше Los Santos из GTA V
            - Downtown, пляжи, пригороды, Everglades
            - Цикл день/ночь
            - Динамическая погода
            - Детальные интерьеры
        """),
        "sec_included_chars_h": "👥 Играбельные персонажи",
        "sec_included_chars_list": dedent("""\
            - **Jason Duval** - Мужской протагонист: бой, вождение, сила
            - **Lucia Caminos** - Женский протагонист (первая в GTA!): взлом, скрытность, ловкость
            - Система двух протагонистов как в GTA V
            - Переключение персонажей
            - Уникальные способности
        """),
        "sec_included_missions_h": "🎯 Мissions & Activities",
        "sec_included_missions_list": dedent("""\
            - Ограбления банков (включая знаменитый слив)
            - Погони с полицией
            - Сюжетные миссии
            - Побочные активности
            - Тиры
            - Угон транспорта
            - И многое другое!
        """),
        "sec_included_vehicles_h": "🚗 150+ транспортных средств",
        "sec_included_vehicles_list": dedent("""\
            - Авто, мотоциклы, лодки, вертолёты
            - Продвинутая физика
            - Реалистичные повреждения
            - Кастомизация транспорта
            - Улучшенное управление vs GTA V
        """),
        "sec_included_source_h": "💻 Исходный код (3 ГБ+)",
        "sec_included_source_list": dedent("""\
            - Код движка (RAGE 9)
            - Скрипты миссий
            - Физика транспорта
            - Системы ИИ
            - Данные карты
            - Asset pipeline
            - Сетевой код GTA Online 2
        """),
        "sec_included_debug_h": "🛠️ Инструменты отладки",
        "sec_included_debug_list": dedent("""\
            - Консоль разработчика (`~`)
            - Меню спавна
            - Телепортация
            - God mode
            - Все миссии
            - Без розыска
            - Погода и время
        """),
        "sec_install_title": "📥 Как скачать и установить",
        "install_labels": [
            "Шаг 1: Официальный сайт",
            "Шаг 2: Выбери билд",
            "Шаг 3: Скачай лаунчер GTA 6",
            "Шаг 4: Скачай билд игры",
            "Шаг 5: Распакуй файлы",
            "Шаг 6: Запусти GTA6Launcher.exe",
            "Шаг 7: Настрой параметры",
            "Шаг 8: Запусти и играй!",
        ],
        "install_bodies": [
            f'Нажми большую кнопку загрузки вверху страницы, чтобы перейти на **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — официальный безопасный источник билда GTA 6 от CyberLeak.',
            dedent("""\
                Выбери версию билда GTA 6:
                - **Q2 2022 (Рекомендуется)** - Самый стабильный и полный функций
                - **Q1 2022** - Хороший баланс функций и стабильности
                - **Q4 2021** - Для тех, кто хочет увидеть раннюю разработку
            """),
            dedent("""\
                - Размер загрузки: ~5 ГБ
                - Включает исполняемый файл лаунчера и основные файлы
                - Только Windows 10/11 64-bit
            """),
            dedent("""\
                - Каждый билд 15-25 ГБ
                - Загружается как сжатый архив (.zip или .rar)
                - Убедись, что достаточно места на диске (рекомендуется 100+ ГБ)
            """),
            dedent("""\
                - Распакуй архив в папку с достаточным свободным местом
                - Рекомендуется: `C:\\GTA6\\` или `D:\\Games\\GTA6\\`
                - НЕ распаковывай в Program Files или системные папки Windows
            """),
            dedent("""\
                - Правый клик по `GTA6Launcher.exe`
                - Выбери **«Запуск от имени администратора»**
                - Windows может показать предупреждение — нажми «Все равно запустить» (файл безопасен)
            """),
            dedent("""\
                - Выбери версию билда
                - Настрой графику (разрешение, качество и т.д.)
                - При необходимости настрой управление
            """),
            dedent("""\
                - Нажми большую кнопку **«ЗАПУСТИТЬ ИГРУ»**
                - Подожди загрузки (первый раз 1-2 минуты)
                - **Наслаждайся GTA 6 до официального релиза!** 🎮
            """),
        ],
        "sec_specs_title": "💻 Системные требования",
        "sec_specs_min_h": "Минимальные требования",
        "sec_specs_rec_h": "Рекомендуемые требования",
        "tbl_spec_header": ("Компонент", "Требование"),
        "min_specs": [
            ("ОС", "Windows 10 64-bit или Windows 11 64-bit"),
            ("Процессор", "Intel Core i5-8400 / AMD Ryzen 5 1600"),
            ("Память", "16 GB RAM"),
            ("Видеокарта", "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB"),
            ("DirectX", "Version 12"),
            ("Хранилище", "50+ GB SSD (100+ GB рекомендуется)"),
            ("Сеть", "Широкополосный интернет для загрузки"),
        ],
        "rec_specs": [
            ("ОС", "Windows 11 64-bit"),
            ("Процессор", "Intel Core i7-10700K / AMD Ryzen 7 3700X"),
            ("Память", "32 GB RAM"),
            ("Видеокарта", "NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800"),
            ("DirectX", "Version 12"),
            ("Хранилище", "100+ GB NVMe SSD"),
            ("Сеть", "Широкополосный интернет"),
        ],
        "sec_specs_notes_h": "Важные заметки:",
        "sec_specs_notes_list": dedent("""\
            - ❌ **PS5, Xbox и Mac НЕ поддерживаются** - только Windows PC
            - ✅ SSD настоятельно рекомендуется
            - ✅ Актуальные драйверы NVIDIA/AMD
            - ✅ DirectX 12 обязателен
            - ✅ Visual C++ Redistributables (в лаунчере)
        """),
        "sec_about_title": "🔍 О CyberLeek",
        "sec_about_who_h": "Кто такой CyberLeak / CyberLeek?",
        "sec_about_who_p": "**CyberLeak** (CyberLeak и CyberLeek) — анонимный источник **слива GTA 6 в августе 2026**, один из крупнейших игровых сливов.",
        "sec_about_timeline_h": "Хронология сливов GTA 6 от CyberLeak:",
        "timeline": [
            ("18 августа 2026", "Первые слитые видео геймплея"),
            ("19 августа 2026", "Новые кадры Jason и Lucia"),
            ("20-21 августа 2026", "Vice City, миссии, транспорт"),
            ("22 августа 2026", "CyberLeak публикует «LEEK» пулями — доказательство доступа"),
            ("23-27 августа 2026", "Сливы перед Netflix Extended Look Rockstar"),
        ],
        "sec_about_compare_h": "Чем CyberLeak отличается от слива 2022?",
        "tbl_compare_header": ("Особенность", "CyberLeak (Авг 2026)", "teapotuberhacker (Сен 2022)"),
        "compare_rows": [
            ("Дата слива", "Август 2026", "Сентябрь 2022"),
            ("Версия билда", "Новее (2022)", "Старее (2021-2022)"),
            ("Качество видео", "Высокое", "Ниже, dev-кадры"),
            ("Объём", "90+ минут", "50+ минут"),
            ("Доказательство", "«LEEK» в игре", "Много клипов"),
            ("Источник", "Неизвестен", "Arion Kurtaj (Lapsus$)"),
        ],
        "sec_about_search_h": "Почему ищут «CyberLeak GTA 6»",
        "sec_about_search_p": "**Миллионы геймеров** ищут:",
        "sec_about_search_list": dedent("""\
            - «GTA 6 CyberLeak download»
            - «CyberLeek playable build»
            - «GTA 6 CyberLeak 2026»
            - «Download GTA 6 from CyberLeak»
            - «CyberLeek leak archive»
            
            **Почему?** Потому что контент CyberLeak:
        """),
        "why_search_bullets": [
            "✅ **Свежее** — ближе к финальной игре (2026 vs 2022)",
            "✅ **Качественнее** — лучше видео и звук",
            "✅ **Полнее** — больше функций и геймплея",
            "✅ **Доказанный доступ** — реальный играбельный билд",
            "✅ **Всеобъемлюще** — Vice City, протагонисты, миссии и т.д.",
        ],
        "sec_about_official": "CyberLeakGTA6.net — официальный архив всего контента CyberLeak.",
        "sec_safety_title": "🛡️ Безопасность",
        "sec_safety_warn_h": "⚠️ ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ",
        "sec_safety_warn_p": "**ОСТЕРЕГАЙТЕСЬ ПОДДЕЛОК!** Мошеннические сайты распространяют **фейковые «билды GTA 6»** с:",
        "sec_safety_warn_list": dedent("""\
            - ❌ Вирусами и вредоносами
            - ❌ Ransomware
            - ❌ Криптомайнерами
            - ❌ Шпионами и кейлоггерами
            - ❌ Троянами
        """),
        "sec_safety_fake_p": "Частая подделка — **торрент 113 ГБ** с пустым местом и вредоносом внутри.",
        "sec_safety_how_h": "✅ Как оставаться в безопасности:",
        "sec_safety_how_list": dedent("""\
            1. **ТОЛЬКО CyberLeakGTA6.net** — официальный источник
            2. **НИКОГДА** со случайных торрентов
            3. **Проверяй размер** — наши билды 15-25 ГБ, НЕ 113 ГБ
            4. **Антивирус** — Windows Defender подойдёт
            5. **Обновляй Windows**
            6. **Не отключай антивирус** — если просят, это malware!
        """),
        "sec_safety_guarantee_h": "🛡️ Наши гарантии:",
        "sec_safety_guarantee_list": dedent("""\
            - ✅ Проверено 15+ антивирусами
            - ✅ Без регистрации
            - ✅ Прозрачная структура файлов
            - ✅ Без майнеров
            - ✅ Без шпионов
            - ✅ Прямая загрузка с официальных серверов
        """),
        "sec_safety_report_h": "📧 Сообщить о фейковых сайтах",
        "sec_safety_report_p": "Если видишь подозрительные «CyberLeak» или «GTA 6 download» — сообщи. Единственный официальный сайт: **CyberLeakGTA6.net**.",
        "sec_faq_title": "❓ FAQ (Часто задаваемые вопросы)",
        "faq": [
            ("В: Это настоящий играбельный билд GTA 6 от CyberLeak?",
             "**О:** ДА! Это подлинный архив слитого билда от CyberLeak с играбельными файлами игры, кастомным лаунчером и всеми слитыми кадрами. CyberLeakGTA6.net - официальный источник полной коллекции слива."),
            ("В: Можно ли реально поиграть в GTA 6 до официального релиза 19 ноября 2026?",
             "**О:** ДА! Скачай наш лаунчер GTA 6 и файлы слитого билда, чтобы играть в версию разработки GTA 6 прямо сейчас. Включает Vice City, сюжетные миссии, побочные активности, транспорт и обоих протагонистов Jason Duval и Lucia Caminos."),
            ("В: Законно ли скачивать слитый билд GTA 6?",
             "**О:** Это слитый билд разработки, предоставленный для образовательных и архивных целей. Мы не поощряем пиратство. **Пожалуйста, поддержи Rockstar Games, купив GTA 6 при официальном релизе 19 ноября 2026.**"),
            ("В: Меня забанят или будут проблемы за скачивание?",
             "**О:** Это однопользовательский слитый билд, который НЕ подключен к серверам Rockstar. Нет способа получить «бан», так как ты не подключен ни к какому онлайн-сервису. По поводу юридических вопросов консультируйся с местным законодательством."),
            ("В: В чем разница между CyberLeak и сливом teapotuberhacker 2022?",
             "**О:** Слив 2022 (сентябрь) был первым крупным сливом GTA 6 от teapotuberhacker (Arion Kurtaj из группы Lapsus$). CyberLeak (август 2026) - более новый отдельный слив с более свежими кадрами, лучшим качеством видео, доступом к более новому билду и более полным освещением."),
            ("В: Зачем нужен лаунчер GTA 6?",
             "**О:** Слитые билды - это версии разработки, требующие специальных параметров запуска и конфигурации. Наш кастомный лаунчер GTA 6 автоматически выполняет всю техническую настройку — достаточно нажать одну кнопку."),
            ("В: Какой размер загрузки? Сколько места нужно?",
             "**О:**\\n- Лаунчер GTA 6: ~5 ГБ\\n- Каждый билд игры: 15-25 ГБ\\n- Всего (все билды + лаунчер + видео): ~80-100 ГБ\\n- **Рекомендуется:** 100+ ГБ свободного места на SSD"),
            ("В: Работает ли на PlayStation 5, Xbox Series X/S или Mac?",
             "**О:** НЕТ. Сейчас поддерживается только Windows PC (64-bit). Слитые билды — PC-версии разработки. Поддержка консолей и Mac недоступна."),
            ("В: Это полная GTA 6 или только демо?",
             "**О:** Это билды разработки 2021-2022, не финальная игра ноября 2026. Однако они включают большую часть карты Vice City, сюжетные миссии, Jason & Lucia, 150+ транспортных средств, боевую систему и многое другое."),
            ("В: Будет ли архив обновляться при новых сливах?",
             "**О:** ДА! Мы следим за новым контентом CyberLeak и обновляем архив. Добавь в закладки **CyberLeakGTA6.net** и проверяй регулярно."),
            ("В: Можно ли модифицировать слитый билд?",
             "**О:** ДА! Мы предоставляем исходный код (3 ГБ+), опытные моддеры могут создавать моды и скрипты. Природа билдов разработки делает их относительно удобными для моддинга."),
            ("В: Есть ли мультиплеер / GTA Online?",
             "**О:** НЕТ. Это однопользовательские билды разработки. Есть ранний код GTA Online 2, но функционального мультиплеера нет."),
            ("В: Антивирус помечает лаунчер — это безопасно?",
             "**О:** Лаунчер на 100% безопасен и проверен 15+ антивирусами. Иногда срабатывает эвристика — это ложное срабатывание. Можно добавить исключение или проверить файл на VirusTotal.com."),
            ("В: Игра вылетает или не запускается — что делать?",
             "**О:** Попробуй:\\n1. Запуск лаунчера от имени администратора\\n2. Установи Visual C++ Redistributables\\n3. Обнови драйверы видеокарты (NVIDIA/AMD)\\n4. Установи DirectX 12\\n5. Попробуй другой билд (Q2 2022 самый стабильный)\\n6. Проверь системные требования — нужно минимум 16 ГБ RAM\\n7. Отключи разгон, если включен"),
            ("В: Можно ли стримить или делать YouTube-видео?",
             "**О:** Технически да, но Rockstar Games отправляет DMCA-уведомления за слитый контент. Стримь и записывай на свой риск."),
        ],
        "lang_section_title": "🌍 Другие языки | Other Languages | Otros idiomas",
        "lang_section_intro": "Этот README доступен на 12 языках:",
        "lang_table_header": ("Язык", "Файл", "Ссылка"),
        "lang_here": "Вы здесь!",
        "sec_seo_title": "🔍 SEO Keywords",
        "sec_seo_keywords": "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, GTA 6 full game download",
        "footer_cta": "⬇️ СКАЧАТЬ БИЛД GTA 6 CYBERLEEK СЕЙЧАС →",
        "footer_h3": "🎮 **ИГРАЙ В GTA 6 ДО ОФИЦИАЛЬНОГО РЕЛИЗА!**",
        "footer_archive": "Официальный архив CyberLeak GTA 6",
        "footer_updated": "Обновлено: 28 августа 2026 | Загрузок: 3,000,000+",
        "footer_disclaimer1": "Не связано с Rockstar Games или Take-Two Interactive",
        "footer_disclaimer2": "Поддержи Rockstar — купи GTA 6 19 ноября 2026",
        "footer_made": "Сделано с ❤️ сообществом GTA | Сохранено для игровой истории",
    }

def _es() -> dict:
    return {
        "title": "🎮 GTA 6 CYBERLEEK - DESCARGAR BUILD JUGABLE | Agosto 2026",
        "badge_build": "BUILD",
        "badge_status_key": "ESTADO",
        "badge_status_val": "JUGABLE",
        "badge_dl_key": "descargas",
        "badge_upd_key": "actualizado",
        "badge_upd_val": "Agosto%202026",
        "hero_h2": "🔥 **DESCARGA Y JUEGA EL BUILD FILTRADO DE GTA 6 DE CYBERLEEK** 🔥",
        "hero_h3": "**El build jugable auténtico de CyberLeak que todos buscan**",
        "hero_tags": "🎮 Juego jugable | 🚀 Launcher GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Código fuente",
        "hero_cta": "⬇️ DESCARGAR BUILD GTA 6 CYBERLEEK AHORA →",
        "toc_title": "📖 Tabla de contenidos",
        "toc": [
            ("🎯 ¿Qué es el build GTA 6 de CyberLeek?", "-what-is-cyberleek-gta-6-build"),
            ("⭐ ¿Por qué descargar de CyberLeak?", "-why-download-from-cyberleek"),
            ("🎮 Qué incluye", "-whats-included"),
            ("📥 Cómo descargar e instalar", "-how-to-download--install"),
            ("💻 Requisitos del sistema", "-system-requirements"),
            ("🔍 Sobre CyberLeak", "-about-cyberleek"),
            ("🛡️ Seguridad", "\ufe0f-safety--security"),
            ("❓ Preguntas frecuentes", "-faq"),
            ("🌍 Otros idiomas", "-other-languages"),
        ],
        "sec_what_title": "🎯 ¿Qué es el build GTA 6 de CyberLeek?",
        "sec_what_intro": "**CyberLeak** (también **CyberLeek**) es la fuente de la **filtración más reciente y completa de GTA 6** en **agosto de 2026**, justo antes del Netflix Extended Look oficial de Rockstar.",
        "sec_what_sub": "🔓 Este es EL build filtrado que todos buscan:",
        "sec_what_list": dedent("""\
            - ✅ **BUILD JUGABLE** - ¡No solo videos! Juego real que puedes descargar y jugar ahora
            - ✅ **Filtración más reciente** - Agosto 2026, más nueva que teapotuberhacker septiembre 2022
            - ✅ **Archivo completo** - 90+ minutos de gameplay, código fuente y builds jugables
            - ✅ **Prueba de autenticidad** - CyberLeak escribió «LEEK» con balas en el juego
            - ✅ **Gameplay Vice City** - Explora Vice City antes del lanzamiento 19 noviembre 2026
        """),
        "sec_what_yes": "¡SÍ, PUEDES JUGARLO DE VERDAD!",
        "sec_what_yes_body": "No es solo una colección de videos: es el build de desarrollo jugable real de GTA 6 con nuestro launcher personalizado.",
        "sec_why_title": "⭐ ¿Por qué descargar de CyberLeak?",
        "sec_why_playable_h": "🎮 **BUILDS JUGABLES**",
        "sec_why_playable_p": "¡No solo videos! Descarga y juega builds filtrados de desarrollo GTA 6 2021-2022. Misiones, Vice City, vehículos y ambos protagonistas.",
        "sec_why_original_h": "🔥 **CYBERLEEK ORIGINAL**",
        "sec_why_original_p": "El build auténtico de CyberLeak que millones buscan. «GTA 6 CyberLeak download», «CyberLeek playable build», «GTA 6 CyberLeak 2026» — este es el archivo.",
        "sec_why_versions_h": "📦 **3 VERSIONES DEL JUEGO**",
        "sec_why_versions_p": "Elige entre 3 builds de desarrollo:",
        "sec_why_versions_list": dedent("""\
            - **Q2 2022** (junio 2022) - Más reciente, estable, completo
            - **Q1 2022** (marzo 2022) - Estable, funciones principales
            - **Q4 2021** (diciembre 2021) - Build temprano, experimental
        """),
        "sec_why_launcher_h": "🚀 **LAUNCHER GTA 6 PERSONALIZADO**",
        "sec_why_launcher_p": "Launcher GTA 6 personalizado: descarga, extrae y pulsa «Launch Game».",
        "sec_why_videos_h": "🎥 **90+ VIDEOS FILTRADOS**",
        "sec_why_videos_p": "Colección completa de gameplay filtrado CyberLeak (90+ minutos):",
        "sec_why_videos_list": dedent("""\
            - Exploración Vice City
            - Gameplay Jason & Lucia
            - Misiones de atraco
            - Persecuciones policiales
            - Vehículos
            - Sistema de combate
            - ¡Y mucho más!
        """),
        "sec_why_source_h": "💻 **ACCESO AL CÓDIGO FUENTE**",
        "sec_why_source_p": "3GB+ de código fuente de desarrollo GTA 6 para desarrolladores y modders.",
        "sec_why_free_h": "🆓 **100% GRATIS**",
        "sec_why_free_list": dedent("""\
            - Sin pago
            - Sin registro
            - Sin encuestas
            - Descarga directa
            - Acceso instantáneo
        """),
        "sec_why_safe_h": "🛡️ **SEGURO Y VERIFICADO**",
        "sec_why_safe_list": dedent("""\
            - Escaneado por 15+ antivirus
            - Sin virus ni malware
            - Sin mineros ocultos
            - Estructura transparente
            - Fuente oficial CyberLeakGTA6.net
        """),
        "sec_included_title": "🎮 Qué incluye",
        "sec_included_builds_h": "🕹️ Builds jugables",
        "tbl_build_header": ("Versión", "Fecha", "Estado", "Características"),
        "builds_rows": [
            ("Q2 2022", "Junio 2022", "✅ Más estable", "Últimas funciones, mejor optimización, recomendado"),
            ("Q1 2022", "Marzo 2022", "✅ Estable", "Funciones principales, buen rendimiento"),
            ("Q4 2021", "Diciembre 2021", "⚠️ Experimental", "Funciones tempranas, algunos bugs"),
        ],
        "sec_included_launcher_h": "🚀 Launcher GTA 6",
        "sec_included_launcher_list": dedent("""\
            - Launcher personalizado
            - Inicio con un clic
            - Selector de build (Q2/Q1/Q4 2022)
            - Configuración gráfica
            - Selector de resolución
            - Herramientas debug
            - Solo Windows (64-bit)
        """),
        "sec_included_map_h": "🗺️ Mapa Vice City",
        "sec_included_map_list": dedent("""\
            - Vice City moderna explorable (Miami)
            - Tamaño: ~2x Los Santos de GTA V
            - Downtown, playas, suburbios, Everglades
            - Ciclo día/noche
            - Clima dinámico
            - Interiores detallados
        """),
        "sec_included_chars_h": "👥 Personajes jugables",
        "sec_included_chars_list": dedent("""\
            - **Jason Duval** - Protagonista masculino: combate, conducción, fuerza
            - **Lucia Caminos** - Protagonista femenina (¡primera en GTA!): hacking, sigilo, agilidad
            - Sistema dual como GTA V
            - Cambio de personaje
            - Habilidades únicas
        """),
        "sec_included_missions_h": "🎯 Misiones y actividades",
        "sec_included_missions_list": dedent("""\
            - Atracos bancarios (incluido el famoso filtrado)
            - Persecuciones policiales
            - Misiones de historia
            - Actividades secundarias
            - Campos de tiro
            - Robo de vehículos
            - ¡Y más!
        """),
        "sec_included_vehicles_h": "🚗 150+ vehículos",
        "sec_included_vehicles_list": dedent("""\
            - Coches, motos, barcos, helicópteros
            - Física avanzada
            - Daños realistas
            - Personalización
            - Mejor manejo que GTA V
        """),
        "sec_included_source_h": "💻 Código fuente (3GB+)",
        "sec_included_source_list": dedent("""\
            - Motor (RAGE 9)
            - Scripts de misiones
            - Física de vehículos
            - Sistemas IA
            - Datos del mapa
            - Pipeline de assets
            - Código red GTA Online 2
        """),
        "sec_included_debug_h": "🛠️ Herramientas debug",
        "sec_included_debug_list": dedent("""\
            - Consola dev (`~`)
            - Menú spawn
            - Teletransporte
            - God mode
            - Todas las misiones
            - Sin wanted level
            - Control clima/tiempo
        """),
        "sec_install_title": "📥 Cómo descargar e instalar",
        "install_labels": [
            "Paso 1: Sitio oficial",
            "Paso 2: Elige tu build",
            "Paso 3: Descarga el launcher GTA 6",
            "Paso 4: Descarga el build",
            "Paso 5: Extrae archivos",
            "Paso 6: Ejecuta GTA6Launcher.exe",
            "Paso 7: Configura ajustes",
            "Paso 8: ¡Lanza y juega!",
        ],
        "install_bodies": [
            f'Haz clic en el botón de descarga para visitar **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — fuente oficial y segura.',
            dedent("""\
                Elige tu versión de build GTA 6:
                - **Q2 2022 (Recomendado)** - Más estable y completo
                - **Q1 2022** - Buen equilibrio
                - **Q4 2021** - Desarrollo temprano
            """),
            dedent("""\
                - Tamaño: ~5GB
                - Incluye launcher y archivos core
                - Solo Windows 10/11 64-bit
            """),
            dedent("""\
                - Cada build: 15-25GB
                - Archivo comprimido (.zip o .rar)
                - Espacio recomendado: 100GB+
            """),
            dedent("""\
                - Extrae a carpeta con espacio libre
                - Recomendado: `C:\\GTA6\\` o `D:\\Games\\GTA6\\`
                - NO extraigas en Program Files
            """),
            dedent("""\
                - Clic derecho en `GTA6Launcher.exe`
                - **«Ejecutar como administrador»**
                - Si Windows advierte, pulsa «Ejecutar de todos modos»
            """),
            dedent("""\
                - Elige versión de build
                - Configura gráficos y resolución
                - Ajusta controles si hace falta
            """),
            dedent("""\
                - Pulsa **«LAUNCH GAME»**
                - Espera 1-2 minutos la primera vez
                - **¡Disfruta GTA 6 antes del lanzamiento oficial!** 🎮
            """),
        ],
        "sec_specs_title": "💻 Requisitos del sistema",
        "sec_specs_min_h": "Requisitos mínimos",
        "sec_specs_rec_h": "Requisitos recomendados",
        "tbl_spec_header": ("Componente", "Requisito"),
        "min_specs": [
            ("Sistema operativo", "Windows 10 64-bit o Windows 11 64-bit"),
            ("Procesador", "Intel Core i5-8400 / AMD Ryzen 5 1600"),
            ("Memoria", "16 GB RAM"),
            ("Gráficos", "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB"),
            ("DirectX", "Versión 12"),
            ("Almacenamiento", "50+ GB SSD (100GB+ recomendado)"),
            ("Red", "Conexión broadband para descarga"),
        ],
        "rec_specs": [
            ("Sistema operativo", "Windows 11 64-bit"),
            ("Procesador", "Intel Core i7-10700K / AMD Ryzen 7 3700X"),
            ("Memoria", "32 GB RAM"),
            ("Gráficos", "NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800"),
            ("DirectX", "Versión 12"),
            ("Almacenamiento", "100+ GB NVMe SSD"),
            ("Red", "Conexión broadband"),
        ],
        "sec_specs_notes_h": "Notas importantes:",
        "sec_specs_notes_list": dedent("""\
            - ❌ **PS5, Xbox y Mac NO soportados** - solo Windows PC
            - ✅ SSD muy recomendado
            - ✅ Drivers gráficos actualizados (NVIDIA/AMD)
            - ✅ DirectX 12 instalado
            - ✅ Visual C++ Redistributables (incluidos)
        """),
        "sec_about_title": "🔍 Sobre CyberLeek",
        "sec_about_who_h": "¿Quién es CyberLeak / CyberLeek?",
        "sec_about_who_p": "**CyberLeak** (CyberLeak y CyberLeek) es la fuente anónima de la **filtración GTA 6 de agosto 2026**, una de las más significativas.",
        "sec_about_timeline_h": "Cronología de filtraciones CyberLeak:",
        "timeline": [
            ("18 agosto 2026", "Primeros videos de gameplay filtrados"),
            ("19 agosto 2026", "Más footage de Jason y Lucia"),
            ("20-21 agosto 2026", "Vice City, misiones, vehículos"),
            ("22 agosto 2026", "CyberLeak publica «LEEK» con balas — prueba de acceso"),
            ("23-27 agosto 2026", "Filtraciones antes del Netflix Extended Look de Rockstar"),
        ],
        "sec_about_compare_h": "¿Qué diferencia a CyberLeak del leak 2022?",
        "tbl_compare_header": ("Característica", "CyberLeak (Ago 2026)", "teapotuberhacker (Sep 2022)"),
        "compare_rows": [
            ("Fecha", "Agosto 2026", "Septiembre 2022"),
            ("Versión build", "Más nueva (2022)", "Más antigua (2021-2022)"),
            ("Calidad video", "Alta calidad", "Menor, footage dev"),
            ("Cantidad", "90+ minutos", "50+ minutos"),
            ("Prueba acceso", "«LEEK» en juego", "Múltiples clips"),
            ("Fuente", "Desconocida", "Arion Kurtaj (Lapsus$)"),
        ],
        "sec_about_search_h": "Por qué buscan «CyberLeak GTA 6»",
        "sec_about_search_p": "**Millones de jugadores** buscan específicamente:",
        "sec_about_search_list": dedent("""\
            - «GTA 6 CyberLeak download»
            - «CyberLeek playable build»
            - «GTA 6 CyberLeak 2026»
            - «Download GTA 6 from CyberLeak»
            - «CyberLeek leak archive»
            
            **¿Por qué?** Porque el contenido CyberLeak es:
        """),
        "why_search_bullets": [
            "✅ **Más reciente** - Más cerca del juego final (2026 vs 2022)",
            "✅ **Mejor calidad** - Mejor video y audio",
            "✅ **Más completo** - Más funciones y gameplay",
            "✅ **Acceso probado** - Build jugable real demostrado",
            "✅ **Integral** - Vice City, protagonistas, misiones, etc.",
        ],
        "sec_about_official": "CyberLeakGTA6.net es el archivo oficial de todo el contenido CyberLeak.",
        "sec_safety_title": "🛡️ Seguridad",
        "sec_safety_warn_h": "⚠️ ADVERTENCIA IMPORTANTE",
        "sec_safety_warn_p": "**¡CUIDADO CON DESCARGAS FALSAS!** Sitios scam distribuyen **«builds GTA 6» falsos** con:",
        "sec_safety_warn_list": dedent("""\
            - ❌ Virus y malware
            - ❌ Ransomware
            - ❌ Mineros cripto
            - ❌ Spyware y keyloggers
            - ❌ Troyanos
        """),
        "sec_safety_fake_p": "La falsificación más común: **torrent de 113GB** con espacio vacío y malware oculto.",
        "sec_safety_how_h": "✅ Cómo mantenerse seguro:",
        "sec_safety_how_list": dedent("""\
            1. **SOLO descarga de CyberLeakGTA6.net**
            2. **NUNCA** de torrents aleatorios
            3. **Verifica tamaños** - nuestros builds 15-25GB, NO 113GB
            4. **Usa antivirus** - Windows Defender vale
            5. **Mantén Windows actualizado**
            6. **No desactives antivirus** - si lo piden, ¡es malware!
        """),
        "sec_safety_guarantee_h": "🛡️ Nuestras garantías:",
        "sec_safety_guarantee_list": dedent("""\
            - ✅ Escaneado por 15+ antivirus
            - ✅ Sin registro
            - ✅ Sin archivos ocultos
            - ✅ Sin mineros
            - ✅ Sin spyware
            - ✅ Descarga directa oficial
        """),
        "sec_safety_report_h": "📧 Reportar sitios falsos",
        "sec_safety_report_p": "Si encuentras sitios sospechosos «CyberLeak» o «GTA 6 download», repórtalos. Único sitio oficial: **CyberLeakGTA6.net**.",
        "sec_faq_title": "❓ FAQ (Preguntas frecuentes)",
        "faq": [
            ("P: ¿Es el build jugable real de GTA 6 de CyberLeak?",
             "**R:** ¡SÍ! Archivo auténtico con archivos jugables, launcher y todo el footage. CyberLeakGTA6.net es la fuente oficial."),
            ("P: ¿Puedo jugar GTA 6 antes del lanzamiento 19 noviembre 2026?",
             "**R:** ¡SÍ! Descarga nuestro launcher y los builds filtrados. Incluye Vice City, misiones, vehículos y Jason Duval y Lucia Caminos."),
            ("P: ¿Es legal descargar el build filtrado?",
             "**R:** Build de desarrollo filtrado con fines educativos y de archivo. No fomentamos piratería. **Apoya Rockstar comprando GTA 6 el 19 noviembre 2026.**"),
            ("P: ¿Me banearán por descargarlo?",
             "**R:** Build single-player NO conectado a servidores Rockstar. No hay ban posible. Consulta leyes locales sobre contenido filtrado."),
            ("P: ¿Diferencia entre CyberLeak y teapotuberhacker 2022?",
             "**R:** Leak 2022 fue el primero (teapotuberhacker/Lapsus$). CyberLeak agosto 2026 es más nuevo, mejor calidad, build más reciente y cobertura más completa."),
            ("P: ¿Por qué necesito el launcher GTA 6?",
             "**R:** Los builds de desarrollo requieren parámetros específicos. Nuestro launcher automatiza todo — un clic para jugar."),
            ("P: ¿Tamaño de descarga y espacio?",
             "**R:**\\n- Launcher: ~5GB\\n- Cada build: 15-25GB\\n- Total: ~80-100GB\\n- **Recomendado:** 100GB+ SSD"),
            ("P: ¿Funciona en PS5, Xbox o Mac?",
             "**R:** NO. Solo Windows PC 64-bit. Builds de desarrollo PC."),
            ("P: ¿Es el juego completo o demo?",
             "**R:** Builds dev 2021-2022, no el juego final. Incluyen gran parte de Vice City, misiones, Jason & Lucia, 150+ vehículos y más."),
            ("P: ¿Se actualizará con nuevas filtraciones?",
             "**R:** ¡SÍ! Monitorizamos CyberLeak y actualizamos. Marca **CyberLeakGTA6.net**."),
            ("P: ¿Puedo modificar el build?",
             "**R:** ¡SÍ! Con código fuente 3GB+, modders pueden crear mods y scripts."),
            ("P: ¿Hay multijugador / GTA Online?",
             "**R:** NO. Builds single-player. Hay código GTA Online 2 temprano pero sin multijugador funcional."),
            ("P: ¿Antivirus marca el launcher?",
             "**R:** 100% seguro, 15+ antivirus. Puede ser falso positivo heurístico. Sube a VirusTotal.com o añade excepción."),
            ("P: ¿Crash o no inicia?",
             "**R:**\\n1. Ejecutar como administrador\\n2. Visual C++ Redistributables\\n3. Drivers NVIDIA/AMD\\n4. DirectX 12\\n5. Prueba Q2 2022\\n6. Mínimo 16GB RAM\\n7. Desactiva overclock"),
            ("P: ¿Puedo streamear o subir a YouTube?",
             "**R:** Técnicamente sí, pero Rockstar envía DMCA por contenido filtrado. Hazlo bajo tu responsabilidad."),
        ],
        "lang_section_title": "🌍 Otros idiomas | Other Languages | Другие языки",
        "lang_section_intro": "Este README está disponible en 12 idiomas:",
        "lang_table_header": ("Idioma", "Archivo", "Enlace"),
        "lang_here": "¡Estás aquí!",
        "sec_seo_title": "🔍 SEO Keywords",
        "sec_seo_keywords": "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, GTA 6 full game download",
        "footer_cta": "⬇️ DESCARGAR BUILD GTA 6 CYBERLEEK AHORA →",
        "footer_h3": "🎮 **¡JUEGA GTA 6 ANTES DEL LANZAMIENTO OFICIAL!**",
        "footer_archive": "Archivo oficial CyberLeak GTA 6",
        "footer_updated": "Actualizado: 28 de agosto de 2026 | Descargas: 3,000,000+",
        "footer_disclaimer1": "No afiliado a Rockstar Games o Take-Two Interactive",
        "footer_disclaimer2": "Apoya Rockstar comprando GTA 6 el 19 de noviembre de 2026",
        "footer_made": "Hecho con ❤️ por la comunidad GTA | Preservado para la historia del gaming",
    }

def _de() -> dict:
    return {
        "title": "🎮 GTA 6 CYBERLEEK - SPIELBAREN BUILD HERUNTERLADEN | August 2026",
        "badge_build": "BUILD",
        "badge_status_key": "STATUS",
        "badge_status_val": "SPIELBAR",
        "badge_dl_key": "downloads",
        "badge_upd_key": "aktualisiert",
        "badge_upd_val": "August%202026",
        "hero_h2": "🔥 **LADE DEN GTA 6 LEAK-BUILD VON CYBERLEEK HERUNTER & SPIELE** 🔥",
        "hero_h3": "**Der authentische CyberLeak spielbare Build, den alle suchen**",
        "hero_tags": "🎮 Spielbares Spiel | 🚀 GTA 6 Launcher | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Quellcode",
        "hero_cta": "⬇️ GTA 6 CYBERLEEK BUILD JETZT HERUNTERLADEN →",
        "toc_title": "📖 Inhaltsverzeichnis",
        "toc": [
            ("🎯 Was ist der CyberLeek GTA 6 Build?", "-what-is-cyberleek-gta-6-build"),
            ("⭐ Warum von CyberLeak?", "-why-download-from-cyberleek"),
            ("🎮 Inhalt", "-whats-included"),
            ("📥 Download & Installation", "-how-to-download--install"),
            ("💻 Systemanforderungen", "-system-requirements"),
            ("🔍 Über CyberLeak", "-about-cyberleek"),
            ("🛡️ Sicherheit", "\ufe0f-safety--security"),
            ("❓ FAQ", "-faq"),
            ("🌍 Andere Sprachen", "-other-languages"),
        ],
        "sec_what_title": "🎯 Was ist der CyberLeek GTA 6 Build?",
        "sec_what_intro": "**CyberLeak** (**CyberLeek**) ist die Quelle des **neuesten vollständigen GTA 6 Leaks** im **August 2026**, kurz vor Rockstars Netflix Extended Look.",
        "sec_what_sub": "🔓 DAS ist der gesuchte Leak-Build:",
        "sec_what_list": dedent("""\
            - ✅ **SPIELBARER BUILD** - Nicht nur Videos! Echtes spielbares Spiel
            - ✅ **Neuester Leak** - August 2026, neuer als teapotuberhacker September 2022
            - ✅ **Vollständiges Archiv** - 90+ Min. Gameplay, Quellcode, Builds
            - ✅ **Echtheitsnachweis** - CyberLeak schrieb «LEEK» mit Kugeln im Spiel
            - ✅ **Vice City** - Erkunde Vice City vor Release 19. November 2026
        """),
        "sec_what_yes": "JA, DU KANNST ES WIRKLICH SPIELEN!",
        "sec_what_yes_body": "Keine Videothek — echter spielbarer GTA 6 Dev-Build mit Launcher.",
        "sec_why_title": "⭐ Warum von CyberLeak herunterladen?",
        "sec_why_playable_h": "🎮 **SPIELBARE BUILDS**",
        "sec_why_playable_p": "Echte GTA 6 Dev-Leaks 2021-2022. Missionen, Vice City, Fahrzeuge, beide Protagonisten.",
        "sec_why_original_h": "🔥 **CYBERLEEK ORIGINAL**",
        "sec_why_original_p": "Der authentische Build, den Millionen suchen.",
        "sec_why_versions_h": "📦 **3 VERSIONEN**",
        "sec_why_versions_p": "Wähle aus 3 Dev-Builds:",
        "sec_why_versions_list": dedent("""\
            - **Q2 2022** (Juni 2022) - Neueste, stabilste
            - **Q1 2022** (März 2022) - Stabil
            - **Q4 2021** (Dezember 2021) - Früh, experimentell
        """),
        "sec_why_launcher_h": "🚀 **GTA 6 LAUNCHER**",
        "sec_why_launcher_p": "Download, entpacken, «Launch Game» — fertig.",
        "sec_why_videos_h": "🎥 **90+ LEAK-VIDEOS**",
        "sec_why_videos_p": "Komplette CyberLeak-Sammlung (90+ Min.):",
        "sec_why_videos_list": dedent("""\
            - Vice City Erkundung
            - Jason & Lucia
            - Banküberfälle
            - Polizeijagden
            - Fahrzeuge
            - Kampfsystem
        """),
        "sec_why_source_h": "💻 **QUELLCODE**",
        "sec_why_source_p": "3GB+ GTA 6 Quellcode für Entwickler und Modder.",
        "sec_why_free_h": "🆓 **100% KOSTENLOS**",
        "sec_why_free_list": dedent("""\
            - Keine Zahlung
            - Keine Registrierung
            - Direkter Download
        """),
        "sec_why_safe_h": "🛡️ **SICHER**",
        "sec_why_safe_list": dedent("""\
            - 15+ Antivirus-Scans
            - Keine Malware
            - CyberLeakGTA6.net offiziell
        """),
        "sec_included_title": "🎮 Inhalt",
        "sec_included_builds_h": "🕹️ Spielbare Builds",
        "tbl_build_header": ("Build", "Datum", "Status", "Features"),
        "builds_rows": [
            ("Q2 2022", "Juni 2022", "✅ Stabilste", "Empfohlen"),
            ("Q1 2022", "März 2022", "✅ Stabil", "Gute Performance"),
            ("Q4 2021", "Dez. 2021", "⚠️ Experimentell", "Frühe Features"),
        ],
        "sec_included_launcher_h": "🚀 GTA 6 Launcher",
        "sec_included_launcher_list": dedent("""\
            - Custom Launcher
            - Ein-Klick-Start
            - Build-Auswahl
            - Grafik & Auflösung
            - Nur Windows 64-bit
        """),
        "sec_included_map_h": "🗺️ Vice City Karte",
        "sec_included_map_list": dedent("""\
            - Volle Vice City (Miami)
            - ~2x Los Santos
            - Tag/Nacht, Wetter
        """),
        "sec_included_chars_h": "👥 Charaktere",
        "sec_included_chars_list": dedent("""\
            - **Jason Duval** - Kampf, Fahren
            - **Lucia Caminos** - Hacking, Stealth
            - Dual-Protagonisten wie GTA V
        """),
        "sec_included_missions_h": "🎯 Missionen",
        "sec_included_missions_list": dedent("""\
            - Banküberfälle, Polizeijagden
            - Story & Side Activities
            - 150+ Fahrzeuge
        """),
        "sec_included_vehicles_h": "🚗 150+ Fahrzeuge",
        "sec_included_vehicles_list": dedent("""\
            - Autos, Boote, Helikopter
            - Physik & Schaden
        """),
        "sec_included_source_h": "💻 Quellcode (3GB+)",
        "sec_included_source_list": dedent("""\
            - RAGE 9 Engine
            - Mission Scripts
            - GTA Online 2 Netzcode
        """),
        "sec_included_debug_h": "🛠️ Debug-Tools",
        "sec_included_debug_list": dedent("""\
            - Dev-Konsole (`~`)
            - Spawn, Teleport, God Mode
        """),
        "sec_install_title": "📥 Download & Installation",
        "install_labels": [
            "Schritt 1: Offizielle Website",
            "Schritt 2: Build wählen",
            "Schritt 3: GTA 6 Launcher",
            "Schritt 4: Build herunterladen",
            "Schritt 5: Entpacken",
            "Schritt 6: GTA6Launcher.exe",
            "Schritt 7: Einstellungen",
            "Schritt 8: Starten & spielen!",
        ],
        "install_bodies": [
            f'Klicke oben auf Download für **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — offizielle Quelle.',
            dedent("""\
                Wähle deine GTA 6 Build-Version:
                            - **Q2 2022 (Empfohlen)** - Stabilste Version
                            - **Q1 2022** - Gute Balance
                            - **Q4 2021** - Frühe Entwicklung
            """),
            dedent("""\
                - Größe: ~5GB
                            - Launcher und Core-Dateien
                            - Nur Windows 10/11 64-bit
            """),
            dedent("""\
                - Jeder Build 15-25GB
                            - Als .zip oder .rar
                            - 100GB+ Speicher empfohlen
            """),
            dedent("""\
                - In Ordner mit freiem Speicher entpacken
                            - z.B. `C:\\GTA6\\`
                            - NICHT in Program Files
            """),
            dedent("""\
                - Rechtsklick `GTA6Launcher.exe`
                            - **Als Administrator ausführen**
                            - Bei Warnung: trotzdem starten
            """),
            dedent("""\
                - Build-Version wählen
                            - Grafik einstellen
                            - Steuerung anpassen
            """),
            dedent("""\
                - **LAUNCH GAME** klicken
                            - 1-2 Min. warten
                            - **GTA 6 vor Release genießen!** 🎮
            """),
        ],
        "sec_specs_title": "💻 Systemanforderungen",
        "sec_specs_min_h": "Minimum",
        "sec_specs_rec_h": "Empfohlen",
        "tbl_spec_header": ("Komponente", "Anforderung"),
        "min_specs": [
            ("OS", "Windows 10/11 64-bit"),
            ("CPU", "i5-8400 / Ryzen 5 1600"),
            ("RAM", "16 GB"),
            ("GPU", "GTX 1060 / RX 580"),
            ("DirectX", "12"),
            ("Speicher", "50+ GB SSD"),
            ("Netz", "Breitband"),
        ],
        "rec_specs": [
            ("OS", "Windows 11 64-bit"),
            ("CPU", "i7-10700K / Ryzen 7 3700X"),
            ("RAM", "32 GB"),
            ("GPU", "RTX 3070 / RX 6800"),
            ("DirectX", "12"),
            ("Speicher", "100+ GB NVMe SSD"),
            ("Netz", "Breitband"),
        ],
        "sec_specs_notes_h": "Wichtig:",
        "sec_specs_notes_list": dedent("""\
            - ❌ Kein PS5/Xbox/Mac
            - ✅ SSD empfohlen
            - ✅ NVIDIA/AMD Treiber
            - ✅ DirectX 12
        """),
        "sec_about_title": "🔍 Über CyberLeek",
        "sec_about_who_h": "Wer ist CyberLeak?",
        "sec_about_who_p": "**CyberLeak** — Quelle des **GTA 6 Leaks August 2026**.",
        "sec_about_timeline_h": "Zeitleiste:",
        "timeline": [
            ("18. Aug 2026", "Erste Videos"),
            ("19. Aug 2026", "Jason & Lucia"),
            ("20-21. Aug 2026", "Vice City"),
            ("22. Aug 2026", "«LEEK» Beweis"),
            ("23-27. Aug 2026", "Vor Netflix Look"),
        ],
        "sec_about_compare_h": "Unterschied zum 2022 Leak?",
        "tbl_compare_header": ("Merkmal", "CyberLeak (Aug 2026)", "teapotuberhacker (Sep 2022)"),
        "compare_rows": [
            ("Datum", "August 2026", "September 2022"),
            ("Build", "Neuer", "Älter"),
            ("Qualität", "Hoch", "Niedriger"),
            ("Menge", "90+ Min.", "50+ Min."),
            ("Beweis", "«LEEK»", "Clips"),
            ("Quelle", "Unbekannt", "Lapsus$"),
        ],
        "sec_about_search_h": "Warum «CyberLeak GTA 6»?",
        "sec_about_search_p": "**Millionen Spieler** suchen:",
        "sec_about_search_list": dedent("""\
            - «GTA 6 CyberLeak download»
            - «CyberLeek playable build»
            
            **Warum?** CyberLeak-Inhalt ist:
        """),
        "why_search_bullets": [
            "✅ **Neuer**",
            "✅ **Bessere Qualität**",
            "✅ **Vollständiger**",
            "✅ **Bewiesener Zugang**",
            "✅ **Umfassend**",
        ],
        "sec_about_official": "CyberLeakGTA6.net — offizielles Archiv.",
        "sec_safety_title": "🛡️ Sicherheit",
        "sec_safety_warn_h": "⚠️ WARNUNG",
        "sec_safety_warn_p": "**VORSICHT VOR FAKES!**",
        "sec_safety_warn_list": "- ❌ Viren, Ransomware, Miner",
        "sec_safety_fake_p": "Häufig: **113GB Torrent** mit Malware.",
        "sec_safety_how_h": "✅ Sicher bleiben:",
        "sec_safety_how_list": dedent("""\
            1. **Nur CyberLeakGTA6.net**
            2. Keine Random-Torrents
            3. Größe prüfen: 15-25GB
        """),
        "sec_safety_guarantee_h": "🛡️ Garantien:",
        "sec_safety_guarantee_list": dedent("""\
            - ✅ 15+ AV-Scans
            - ✅ Keine Miner/Spyware
        """),
        "sec_safety_report_h": "📧 Fake-Meldung",
        "sec_safety_report_p": "Nur **CyberLeakGTA6.net** ist offiziell.",
        "sec_faq_title": "❓ FAQ",
        "faq": [
            ("F: Ist das der echte spielbare GTA 6 Build von CyberLeak?",
             "A: JA! Authentisches CyberLeak-Archiv mit spielbaren Dateien, Launcher und Footage. CyberLeakGTA6.net ist die offizielle Quelle."),
            ("F: Kann ich GTA 6 vor dem Release am 19. November 2026 spielen?",
             "A: JA! Launcher und Builds herunterladen. Vice City, Missionen, Fahrzeuge, Jason Duval und Lucia Caminos."),
            ("F: Ist der Download legal?",
             "A: Dev-Build zu Bildungs-/Archivzwecken. Keine Piraterie-Förderung. **Bitte Rockstar unterstützen — GTA 6 am 19. November 2026 kaufen.**"),
            ("F: Werde ich gebannt oder bekomme Ärger?",
             "A: Singleplayer, nicht mit Rockstar-Servern verbunden. Kein Ban möglich. Lokale Gesetze beachten."),
            ("F: Unterschied CyberLeak vs. teapotuberhacker 2022?",
             "A: 2022 erster großer Leak (teapotuberhacker/Lapsus$). CyberLeak August 2026 neuer, bessere Qualität, neuerer Build."),
            ("F: Warum brauche ich den GTA 6 Launcher?",
             "A: Dev-Builds brauchen spezielle Startparameter. Unser Launcher erledigt alles automatisch."),
            ("F: Downloadgröße und Speicher?",
             "A: Launcher ~5GB; Builds 15-25GB; gesamt ~80-100GB. **Empfohlen:** 100GB+ SSD."),
            ("F: PS5, Xbox oder Mac?",
             "A: NEIN. Nur Windows PC 64-bit."),
            ("F: Volles Spiel oder Demo?",
             "A: Dev-Builds 2021-2022. Große Vice City-Karte, Missionen, Jason & Lucia, 150+ Fahrzeuge u.v.m."),
            ("F: Updates bei neuen Leaks?",
             "A: JA! Bookmark **CyberLeakGTA6.net**."),
            ("F: Modding möglich?",
             "A: JA! 3GB+ Quellcode für Modder."),
            ("F: Multiplayer / GTA Online?",
             "A: NEIN. Singleplayer. Früher GTA Online 2 Code, kein funktionaler Multiplayer."),
            ("F: Antivirus warnt vor Launcher?",
             "A: 100% sicher. Heuristik-Falschpositiv möglich. VirusTotal.com oder Ausnahme."),
            ("F: Abstürze / startet nicht?",
             "A: Als Admin starten; VC++ Redist; NVIDIA/AMD-Treiber; DirectX 12; Q2 2022; 16GB RAM; Overclock aus."),
            ("F: Streamen / YouTube?",
             "A: Technisch ja, Rockstar DMCA. Eigenes Risiko."),
        ],
        "lang_section_title": "🌍 Andere Sprachen | Other Languages | Другие языки",
        "lang_section_intro": "README in 12 Sprachen:",
        "lang_table_header": ("Sprache", "Datei", "Link"),
        "lang_here": "Du bist hier!",
        "sec_seo_title": "🔍 SEO Keywords",
        "sec_seo_keywords": "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, GTA 6 full game download",
        "footer_cta": "⬇️ GTA 6 CYBERLEEK BUILD JETZT →",
        "footer_h3": "🎮 **SPIELE GTA 6 VOR DEM RELEASE!**",
        "footer_archive": "Offizielles CyberLeak GTA 6 Archiv",
        "footer_updated": "Aktualisiert: 28. August 2026 | Downloads: 3.000.000+",
        "footer_disclaimer1": "Nicht mit Rockstar oder Take-Two verbunden",
        "footer_disclaimer2": "Rockstar unterstützen — GTA 6 am 19. November 2026 kaufen",
        "footer_made": "Mit ❤️ von der GTA-Community",
    }

def _fr() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - TÉLÉCHARGER BUILD JOUABLE | Août 2026',
 'badge_build': 'BUILD',
 'badge_status_key': 'STATUT',
 'badge_status_val': 'JOUABLE',
 'badge_dl_key': 'téléchargements',
 'badge_upd_key': 'mis à jour',
 'badge_upd_val': 'Ao%C3%BBt%202026',
 'hero_h2': '🔥 **TÉLÉCHARGE ET JOUE LE BUILD FILTRÉ GTA 6 DE CYBERLEEK** 🔥',
 'hero_h3': '**Le build jouable authentique de CyberLeak que tout le monde cherche**',
 'hero_tags': '🎮 Jeu jouable | 🚀 Launcher GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Code source',
 'hero_cta': '⬇️ TÉLÉCHARGER LE BUILD GTA 6 CYBERLEEK MAINTENANT →',
 'toc_title': '📖 Sommaire',
 'toc': [("🎯 Qu'est-ce que le build GTA 6 CyberLeek ?", '-what-is-cyberleek-gta-6-build'),
         ('⭐ Pourquoi télécharger depuis CyberLeak ?', '-why-download-from-cyberleek'),
         ('🎮 Contenu inclus', '-whats-included'),
         ('📥 Comment télécharger et installer', '-how-to-download--install'),
         ('💻 Configuration requise', '-system-requirements'),
         ('🔍 À propos de CyberLeak', '-about-cyberleek'),
         ('🛡️ Sécurité', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 Autres langues', '-other-languages')],
 'sec_what_title': "🎯 Qu'est-ce que le build GTA 6 CyberLeek ?",
 'sec_what_intro': '**CyberLeak** (aussi **CyberLeek**) est la source de la **fuite GTA 6 la plus récente et la plus '
                   'complète** en **août 2026**, juste avant le Netflix Extended Look officiel de Rockstar.',
 'sec_what_sub': "🔓 C'est LE build filtré que tout le monde cherche :",
 'sec_what_list': '- ✅ **BUILD JOUABLE** - Pas seulement des vidéos ! Vrai jeu téléchargeable et jouable dès '
                  'maintenant\n'
                  '- ✅ **Fuite la plus récente** - Août 2026, plus récent que teapotuberhacker septembre 2022\n'
                  '- ✅ **Archive complète** - 90+ minutes de gameplay, code source et builds jouables\n'
                  "- ✅ **Preuve d'authenticité** - CyberLeak a écrit « LEEK » avec des balles en jeu\n"
                  '- ✅ **Gameplay Vice City** - Explore Vice City avant la sortie du 19 novembre 2026',
 'sec_what_yes': 'OUI, VOUS POUVEZ VRAIMENT Y JOUER !',
 'sec_what_yes_body': "Ce n'est pas une collection de vidéos — c'est le vrai build de développement jouable de GTA 6 "
                      'avec notre launcher personnalisé.',
 'sec_why_title': '⭐ Pourquoi télécharger depuis CyberLeak ?',
 'sec_why_playable_h': '🎮 **BUILDS JOUABLES**',
 'sec_why_playable_p': 'Pas seulement des vidéos ! Télécharge et joue aux builds filtrés GTA 6 2021-2022. Missions, '
                       'Vice City, véhicules et les deux protagonistes.',
 'sec_why_original_h': '🔥 **CYBERLEEK ORIGINAL**',
 'sec_why_original_p': 'Le build authentique CyberLeak que des millions cherchent. « GTA 6 CyberLeak download », « '
                       "CyberLeek playable build », « GTA 6 CyberLeak 2026 » — c'est cette archive.",
 'sec_why_versions_h': '📦 **3 VERSIONS DU JEU**',
 'sec_why_versions_p': 'Choisis parmi 3 builds de développement :',
 'sec_why_versions_list': '- **Q2 2022** (juin 2022) - Plus récent, stable, complet\n'
                          '- **Q1 2022** (mars 2022) - Stable, fonctions principales\n'
                          '- **Q4 2021** (décembre 2021) - Build précoce, expérimental',
 'sec_why_launcher_h': '🚀 **LAUNCHER GTA 6 PERSONNALISÉ**',
 'sec_why_launcher_p': 'Launcher GTA 6 personnalisé : télécharge, extrais et clique sur « Launch Game ».',
 'sec_why_videos_h': '🎥 **90+ VIDÉOS FILTRÉES**',
 'sec_why_videos_p': 'Collection complète du gameplay filtré CyberLeak (90+ minutes) :',
 'sec_why_videos_list': '- Exploration de Vice City\n'
                        '- Gameplay Jason & Lucia\n'
                        '- Missions de braquage\n'
                        '- Poursuites policières\n'
                        '- Véhicules\n'
                        '- Système de combat\n'
                        '- Et bien plus !',
 'sec_why_source_h': '💻 **ACCÈS AU CODE SOURCE**',
 'sec_why_source_p': '3 Go+ de code source de développement GTA 6 pour développeurs et moddeurs.',
 'sec_why_free_h': '🆓 **100 % GRATUIT**',
 'sec_why_free_list': '- Sans paiement\n'
                      '- Sans inscription\n'
                      '- Sans sondages\n'
                      '- Téléchargement direct\n'
                      '- Accès instantané',
 'sec_why_safe_h': '🛡️ **SÛR ET VÉRIFIÉ**',
 'sec_why_safe_list': '- Scanné par 15+ antivirus\n'
                      '- Sans virus ni malware\n'
                      '- Sans mineurs cachés\n'
                      '- Structure transparente\n'
                      '- Source officielle CyberLeakGTA6.net',
 'sec_included_title': '🎮 Contenu inclus',
 'sec_included_builds_h': '🕹️ Builds jouables',
 'tbl_build_header': ('Version', 'Date', 'Statut', 'Caractéristiques'),
 'builds_rows': [('Q2 2022', 'Juin 2022', '✅ Plus stable', 'Dernières fonctions, meilleure optimisation, recommandé'),
                 ('Q1 2022', 'Mars 2022', '✅ Stable', 'Fonctions principales, bonnes performances'),
                 ('Q4 2021', 'Décembre 2021', '⚠️ Expérimental', 'Fonctions précoces, quelques bugs')],
 'sec_included_launcher_h': '🚀 Launcher GTA 6',
 'sec_included_launcher_list': '- Launcher personnalisé\n'
                               '- Lancement en un clic\n'
                               '- Sélecteur de build (Q2/Q1/Q4 2022)\n'
                               '- Configuration graphique\n'
                               '- Sélecteur de résolution\n'
                               '- Outils debug\n'
                               '- Windows uniquement (64-bit)',
 'sec_included_map_h': '🗺️ Carte Vice City',
 'sec_included_map_list': '- Vice City moderne explorable (Miami)\n'
                          '- Taille : ~2x Los Santos de GTA V\n'
                          '- Downtown, plages, banlieues, Everglades\n'
                          '- Cycle jour/nuit\n'
                          '- Météo dynamique\n'
                          '- Intérieurs détaillés',
 'sec_included_chars_h': '👥 Personnages jouables',
 'sec_included_chars_list': '- **Jason Duval** - Protagoniste masculin : combat, conduite, force\n'
                            '- **Lucia Caminos** - Protagoniste féminine (première dans GTA !) : hacking, furtivité, '
                            'agilité\n'
                            '- Système dual comme GTA V\n'
                            '- Changement de personnage\n'
                            '- Capacités uniques',
 'sec_included_missions_h': '🎯 Missions et activités',
 'sec_included_missions_list': '- Braquages bancaires (y compris le fameux filtré)\n'
                               '- Poursuites policières\n'
                               "- Missions d'histoire\n"
                               '- Activités secondaires\n'
                               '- Stand de tir\n'
                               '- Vol de véhicules\n'
                               '- Et plus !',
 'sec_included_vehicles_h': '🚗 150+ véhicules',
 'sec_included_vehicles_list': '- Voitures, motos, bateaux, hélicoptères\n'
                               '- Physique avancée\n'
                               '- Dégâts réalistes\n'
                               '- Personnalisation\n'
                               '- Meilleure conduite que GTA V',
 'sec_included_source_h': '💻 Code source (3 Go+)',
 'sec_included_source_list': '- Moteur (RAGE 9)\n'
                             '- Scripts de missions\n'
                             '- Physique des véhicules\n'
                             '- Systèmes IA\n'
                             '- Données de carte\n'
                             "- Pipeline d'assets\n"
                             '- Code réseau GTA Online 2',
 'sec_included_debug_h': '🛠️ Outils debug',
 'sec_included_debug_list': '- Console dev (`~`)\n'
                            '- Menu spawn\n'
                            '- Téléportation\n'
                            '- God mode\n'
                            '- Toutes les missions\n'
                            '- Sans wanted level\n'
                            '- Contrôle météo/temps',
 'sec_install_title': '📥 Comment télécharger et installer',
 'install_labels': ['Étape 1 : Site officiel',
                    'Étape 2 : Choisir votre build',
                    'Étape 3 : Télécharger le launcher GTA 6',
                    'Étape 4 : Télécharger le build',
                    'Étape 5 : Extraire les fichiers',
                    'Étape 6 : Exécuter GTA6Launcher.exe',
                    'Étape 7 : Configurer les paramètres',
                    'Étape 8 : Lancer et jouer !'],
 'install_bodies': ['Cliquez sur le bouton de téléchargement pour visiter '
                    '**[CyberLeakGTA6.net](https://cyberleakgta6.net)** — source officielle et sûre.',
                    'Choisissez votre version de build GTA 6 :\n'
                    '- **Q2 2022 (Recommandé)** - Plus stable et complet\n'
                    '- **Q1 2022** - Bon équilibre\n'
                    '- **Q4 2021** - Développement précoce',
                    '- Taille : ~5 Go\n- Inclut le launcher et les fichiers core\n- Windows 10/11 64-bit uniquement',
                    '- Chaque build : 15-25 Go\n- Archive compressée (.zip ou .rar)\n- Espace recommandé : 100 Go+',
                    '- Extraire dans un dossier avec espace libre\n'
                    '- Recommandé : `C:\\GTA6\\` ou `D:\\Games\\GTA6\\`\n'
                    '- NE PAS extraire dans Program Files',
                    '- Clic droit sur `GTA6Launcher.exe`\n'
                    "- **« Exécuter en tant qu'administrateur »**\n"
                    '- Si Windows avertit, cliquez « Exécuter quand même »',
                    '- Choisir la version de build\n'
                    '- Configurer graphiques et résolution\n'
                    '- Ajuster les contrôles si besoin',
                    '- Cliquez **« LAUNCH GAME »**\n'
                    '- Attendez 1-2 minutes la première fois\n'
                    '- **Profitez de GTA 6 avant la sortie officielle !** 🎮'],
 'sec_specs_title': '💻 Configuration requise',
 'sec_specs_min_h': 'Configuration minimale',
 'sec_specs_rec_h': 'Configuration recommandée',
 'tbl_spec_header': ('Composant', 'Exigence'),
 'min_specs': [("Système d'exploitation", 'Windows 10 64-bit ou Windows 11 64-bit'),
               ('Processeur', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('Mémoire', '16 Go RAM'),
               ('Graphiques', 'NVIDIA GeForce GTX 1060 6 Go / AMD Radeon RX 580 8 Go'),
               ('DirectX', 'Version 12'),
               ('Stockage', '50+ Go SSD (100 Go+ recommandé)'),
               ('Réseau', 'Connexion broadband pour le téléchargement')],
 'rec_specs': [("Système d'exploitation", 'Windows 11 64-bit'),
               ('Processeur', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('Mémoire', '32 Go RAM'),
               ('Graphiques', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'Version 12'),
               ('Stockage', '100+ Go NVMe SSD'),
               ('Réseau', 'Connexion broadband')],
 'sec_specs_notes_h': 'Notes importantes :',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox et Mac NON pris en charge** - Windows PC uniquement\n'
                         '- ✅ SSD fortement recommandé\n'
                         '- ✅ Pilotes graphiques à jour (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 installé\n'
                         '- ✅ Visual C++ Redistributables (inclus)',
 'sec_about_title': '🔍 À propos de CyberLeek',
 'sec_about_who_h': 'Qui est CyberLeak / CyberLeek ?',
 'sec_about_who_p': "**CyberLeak** (CyberLeak et CyberLeek) est la source anonyme de la **fuite GTA 6 d'août 2026**, "
                    "l'une des plus significatives.",
 'sec_about_timeline_h': 'Chronologie des fuites CyberLeak :',
 'timeline': [('18 août 2026', 'Premières vidéos de gameplay filtrées'),
              ('19 août 2026', 'Plus de footage de Jason et Lucia'),
              ('20-21 août 2026', 'Vice City, missions, véhicules'),
              ('22 août 2026', "CyberLeak publie « LEEK » avec des balles — preuve d'accès"),
              ('23-27 août 2026', 'Fuites avant le Netflix Extended Look de Rockstar')],
 'sec_about_compare_h': "Qu'est-ce qui différencie CyberLeak de la fuite 2022 ?",
 'tbl_compare_header': ('Caractéristique', 'CyberLeak (Août 2026)', 'teapotuberhacker (Sep 2022)'),
 'compare_rows': [('Date', 'Août 2026', 'Septembre 2022'),
                  ('Version build', 'Plus récente (2022)', 'Plus ancienne (2021-2022)'),
                  ('Qualité vidéo', 'Haute qualité', 'Inférieure, footage dev'),
                  ('Quantité', '90+ minutes', '50+ minutes'),
                  ("Preuve d'accès", '« LEEK » en jeu', 'Plusieurs clips'),
                  ('Source', 'Inconnue', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': 'Pourquoi cherche-t-on « CyberLeak GTA 6 »',
 'sec_about_search_p': '**Des millions de joueurs** recherchent spécifiquement :',
 'sec_about_search_list': '- « GTA 6 CyberLeak download »\n'
                          '- « CyberLeek playable build »\n'
                          '- « GTA 6 CyberLeak 2026 »\n'
                          '- « Download GTA 6 from CyberLeak »\n'
                          '- « CyberLeek leak archive »\n'
                          '\n'
                          '**Pourquoi ?** Parce que le contenu CyberLeak est :',
 'why_search_bullets': ['✅ **Plus récent** - Plus proche du jeu final (2026 vs 2022)',
                        '✅ **Meilleure qualité** - Meilleure vidéo et audio',
                        '✅ **Plus complet** - Plus de fonctions et de gameplay',
                        '✅ **Accès prouvé** - Build jouable réel démontré',
                        '✅ **Complet** - Vice City, protagonistes, missions, etc.'],
 'sec_about_official': "CyberLeakGTA6.net est l'archive officielle de tout le contenu CyberLeak.",
 'sec_safety_title': '🛡️ Sécurité',
 'sec_safety_warn_h': '⚠️ AVERTISSEMENT IMPORTANT',
 'sec_safety_warn_p': '**ATTENTION AUX FAUX TÉLÉCHARGEMENTS !** Des sites arnaque distribuent de **faux « builds GTA 6 '
                      '»** contenant :',
 'sec_safety_warn_list': '- ❌ Virus et malware\n'
                         '- ❌ Ransomware\n'
                         '- ❌ Mineurs crypto\n'
                         '- ❌ Spyware et keyloggers\n'
                         '- ❌ Chevaux de Troie',
 'sec_safety_fake_p': 'Le faux le plus courant : **torrent de 113 Go** avec espace vide et malware caché.',
 'sec_safety_how_h': '✅ Comment rester en sécurité :',
 'sec_safety_how_list': '1. **Téléchargez UNIQUEMENT depuis CyberLeakGTA6.net**\n'
                        '2. **JAMAIS** depuis des torrents aléatoires\n'
                        '3. **Vérifiez les tailles** - nos builds 15-25 Go, PAS 113 Go\n'
                        '4. **Utilisez un antivirus** - Windows Defender suffit\n'
                        '5. **Maintenez Windows à jour**\n'
                        "6. **Ne désactivez pas l'antivirus** - si on le demande, c'est du malware !",
 'sec_safety_guarantee_h': '🛡️ Nos garanties :',
 'sec_safety_guarantee_list': '- ✅ Scanné par 15+ antivirus\n'
                              '- ✅ Sans inscription\n'
                              '- ✅ Sans fichiers cachés\n'
                              '- ✅ Sans mineurs\n'
                              '- ✅ Sans spyware\n'
                              '- ✅ Téléchargement direct officiel',
 'sec_safety_report_h': '📧 Signaler de faux sites',
 'sec_safety_report_p': 'Si vous trouvez des sites suspects « CyberLeak » ou « GTA 6 download », signalez-les. Seul '
                        'site officiel : **CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ FAQ (Questions fréquentes)',
 'faq': [('Q: Est-ce le vrai build jouable GTA 6 de CyberLeak ?',
          '**R:** OUI ! Archive authentique avec fichiers jouables, launcher et tout le footage. CyberLeakGTA6.net est '
          'la source officielle.'),
         ('Q: Puis-je jouer à GTA 6 avant la sortie du 19 novembre 2026 ?',
          '**R:** OUI ! Téléchargez notre launcher et les builds filtrés. Vice City, missions, véhicules, Jason Duval '
          'et Lucia Caminos.'),
         ('Q: Est-il légal de télécharger le build filtré ?',
          "**R:** Build de développement filtré à des fins éducatives et d'archivage. Nous n'encourageons pas le "
          'piratage. **Soutenez Rockstar en achetant GTA 6 le 19 novembre 2026.**'),
         ('Q: Vais-je être banni ou avoir des problèmes ?',
          '**R:** Build solo non connecté aux serveurs Rockstar. Aucun ban possible. Consultez les lois locales.'),
         ('Q: Différence entre CyberLeak et teapotuberhacker 2022 ?',
          '**R:** La fuite 2022 fut la première (teapotuberhacker/Lapsus$). CyberLeak août 2026 est plus récent, '
          'meilleure qualité, build plus récent et couverture plus complète.'),
         ('Q: Pourquoi ai-je besoin du launcher GTA 6 ?',
          '**R:** Les builds de dev nécessitent des paramètres spécifiques. Notre launcher automatise tout — un clic '
          'pour jouer.'),
         ('Q: Taille du téléchargement et espace disque ?',
          '**R:** \\n- Launcher : ~5 Go\\n- Chaque build : 15-25 Go\\n- Total : ~80-100 Go\\n- **Recommandé :** 100 '
          'Go+ SSD'),
         ('Q: Fonctionne sur PS5, Xbox ou Mac ?',
          '**R:** NON. Windows PC 64-bit uniquement. Builds de développement PC.'),
         ('Q: Jeu complet ou démo ?',
          '**R:** Builds dev 2021-2022, pas le jeu final. Grande carte Vice City, missions, Jason & Lucia, 150+ '
          'véhicules et plus.'),
         ('Q: Sera-t-il mis à jour avec de nouvelles fuites ?',
          '**R:** OUI ! Nous surveillons CyberLeak et mettons à jour. Ajoutez **CyberLeakGTA6.net** en favoris.'),
         ('Q: Puis-je modder le build ?',
          '**R:** OUI ! Avec 3 Go+ de code source, les moddeurs peuvent créer mods et scripts.'),
         ('Q: Y a-t-il du multijoueur / GTA Online ?',
          '**R:** NON. Builds solo. Code GTA Online 2 précoce mais sans multijoueur fonctionnel.'),
         ("Q: L'antivirus signale le launcher ?",
          '**R:** 100 % sûr, 15+ antivirus. Faux positif heuristique possible. VirusTotal.com ou exception.'),
         ('Q: Crash ou ne démarre pas ?',
          '**R:** \\n1. Exécuter en administrateur\\n2. Visual C++ Redistributables\\n3. Pilotes NVIDIA/AMD\\n4. '
          "DirectX 12\\n5. Essayer Q2 2022\\n6. Minimum 16 Go RAM\\n7. Désactiver l'overclock"),
         ('Q: Puis-je streamer ou publier sur YouTube ?',
          '**R:** Techniquement oui, mais Rockstar envoie des DMCA pour contenu filtré. À vos risques.')],
 'lang_section_title': '🌍 Autres langues | Other Languages | Другие языки',
 'lang_section_intro': 'Ce README est disponible en 12 langues :',
 'lang_table_header': ('Langue', 'Fichier', 'Lien'),
 'lang_here': 'Vous êtes ici !',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ TÉLÉCHARGER LE BUILD GTA 6 CYBERLEEK MAINTENANT →',
 'footer_h3': '🎮 **JOUEZ À GTA 6 AVANT LA SORTIE OFFICIELLE !**',
 'footer_archive': 'Archive officielle CyberLeak GTA 6',
 'footer_updated': 'Mis à jour : August 28, 2026 | Téléchargements : 3 000 000+',
 'footer_disclaimer1': 'Non affilié à Rockstar Games ou Take-Two Interactive',
 'footer_disclaimer2': 'Soutenez Rockstar en achetant GTA 6 le 19 novembre 2026',
 'footer_made': "Fait avec ❤️ par la communauté GTA | Préservé pour l'histoire du gaming"}


def _it() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - SCARICA BUILD GIOCABILE | Agosto 2026',
 'badge_build': 'BUILD',
 'badge_status_key': 'STATO',
 'badge_status_val': 'GIOCABILE',
 'badge_dl_key': 'download',
 'badge_upd_key': 'aggiornato',
 'badge_upd_val': 'Agosto%202026',
 'hero_h2': '🔥 **SCARICA E GIOCA IL BUILD TRAPELATO GTA 6 DA CYBERLEEK** 🔥',
 'hero_h3': '**Il build giocabile autentico di CyberLeak che tutti cercano**',
 'hero_tags': '🎮 Gioco giocabile | 🚀 Launcher GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Codice sorgente',
 'hero_cta': '⬇️ SCARICA IL BUILD GTA 6 CYBERLEEK ORA →',
 'toc_title': '📖 Indice',
 'toc': [("🎯 Cos'è il build GTA 6 CyberLeek?", '-what-is-cyberleek-gta-6-build'),
         ('⭐ Perché scaricare da CyberLeak?', '-why-download-from-cyberleek'),
         ('🎮 Contenuto incluso', '-whats-included'),
         ('📥 Come scaricare e installare', '-how-to-download--install'),
         ('💻 Requisiti di sistema', '-system-requirements'),
         ('🔍 Info su CyberLeak', '-about-cyberleek'),
         ('🛡️ Sicurezza', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 Altre lingue', '-other-languages')],
 'sec_what_title': "🎯 Cos'è il build GTA 6 CyberLeek?",
 'sec_what_intro': '**CyberLeak** (anche **CyberLeek**) è la fonte della **fuga GTA 6 più recente e completa** ad '
                   '**agosto 2026**, poco prima del Netflix Extended Look ufficiale di Rockstar.',
 'sec_what_sub': '🔓 Questo è IL build trapelato che tutti cercano:',
 'sec_what_list': '- ✅ **BUILD GIOCABILE** - Non solo video! Vero gioco scaricabile e giocabile subito\n'
                  '- ✅ **Fuga più recente** - Agosto 2026, più recente di teapotuberhacker settembre 2022\n'
                  '- ✅ **Archivio completo** - 90+ minuti di gameplay, codice sorgente e build giocabili\n'
                  '- ✅ **Prova di autenticità** - CyberLeak ha scritto «LEEK» con i proiettili in gioco\n'
                  "- ✅ **Gameplay Vice City** - Esplora Vice City prima dell'uscita del 19 novembre 2026",
 'sec_what_yes': 'SÌ, PUOI DAVVERO GIOCARE!',
 'sec_what_yes_body': 'Non è solo una raccolta di video: è il vero build di sviluppo giocabile di GTA 6 con il nostro '
                      'launcher personalizzato.',
 'sec_why_title': '⭐ Perché scaricare da CyberLeak?',
 'sec_why_playable_h': '🎮 **BUILD GIOCABILI**',
 'sec_why_playable_p': 'Non solo video! Scarica e gioca i build trapelati GTA 6 2021-2022. Missioni, Vice City, '
                       'veicoli e entrambi i protagonisti.',
 'sec_why_original_h': '🔥 **CYBERLEEK ORIGINALE**',
 'sec_why_original_p': 'Il build autentico CyberLeak che milioni cercano. «GTA 6 CyberLeak download», «CyberLeek '
                       "playable build», «GTA 6 CyberLeak 2026» — questo è l'archivio.",
 'sec_why_versions_h': '📦 **3 VERSIONI DEL GIOCO**',
 'sec_why_versions_p': 'Scegli tra 3 build di sviluppo:',
 'sec_why_versions_list': '- **Q2 2022** (giugno 2022) - Più recente, stabile, completo\n'
                          '- **Q1 2022** (marzo 2022) - Stabile, funzioni principali\n'
                          '- **Q4 2021** (dicembre 2021) - Build precoce, sperimentale',
 'sec_why_launcher_h': '🚀 **LAUNCHER GTA 6 PERSONALIZZATO**',
 'sec_why_launcher_p': 'Launcher GTA 6 personalizzato: scarica, estrai e clicca «Launch Game».',
 'sec_why_videos_h': '🎥 **90+ VIDEO TRAPELATI**',
 'sec_why_videos_p': 'Collezione completa del gameplay trapelato CyberLeak (90+ minuti):',
 'sec_why_videos_list': '- Esplorazione Vice City\n'
                        '- Gameplay Jason & Lucia\n'
                        '- Missioni di rapina\n'
                        '- Inseguimenti della polizia\n'
                        '- Veicoli\n'
                        '- Sistema di combattimento\n'
                        '- E molto altro!',
 'sec_why_source_h': '💻 **ACCESSO AL CODICE SORGENTE**',
 'sec_why_source_p': '3GB+ di codice sorgente di sviluppo GTA 6 per sviluppatori e modder.',
 'sec_why_free_h': '🆓 **100% GRATIS**',
 'sec_why_free_list': '- Nessun pagamento\n'
                      '- Nessuna registrazione\n'
                      '- Nessun sondaggio\n'
                      '- Download diretto\n'
                      '- Accesso immediato',
 'sec_why_safe_h': '🛡️ **SICURO E VERIFICATO**',
 'sec_why_safe_list': '- Scansionato da 15+ antivirus\n'
                      '- Nessun virus o malware\n'
                      '- Nessun miner nascosto\n'
                      '- Struttura trasparente\n'
                      '- Fonte ufficiale CyberLeakGTA6.net',
 'sec_included_title': '🎮 Contenuto incluso',
 'sec_included_builds_h': '🕹️ Build giocabili',
 'tbl_build_header': ('Versione', 'Data', 'Stato', 'Caratteristiche'),
 'builds_rows': [('Q2 2022', 'Giugno 2022', '✅ Più stabile', 'Ultime funzioni, migliore ottimizzazione, consigliato'),
                 ('Q1 2022', 'Marzo 2022', '✅ Stabile', 'Funzioni principali, buone prestazioni'),
                 ('Q4 2021', 'Dicembre 2021', '⚠️ Sperimentale', 'Funzioni precoci, alcuni bug')],
 'sec_included_launcher_h': '🚀 Launcher GTA 6',
 'sec_included_launcher_list': '- Launcher personalizzato\n'
                               '- Avvio con un clic\n'
                               '- Selettore build (Q2/Q1/Q4 2022)\n'
                               '- Configurazione grafica\n'
                               '- Selettore risoluzione\n'
                               '- Strumenti debug\n'
                               '- Solo Windows (64-bit)',
 'sec_included_map_h': '🗺️ Mappa Vice City',
 'sec_included_map_list': '- Vice City moderna esplorabile (Miami)\n'
                          '- Dimensione: ~2x Los Santos di GTA V\n'
                          '- Downtown, spiagge, periferie, Everglades\n'
                          '- Ciclo giorno/notte\n'
                          '- Meteo dinamico\n'
                          '- Interni dettagliati',
 'sec_included_chars_h': '👥 Personaggi giocabili',
 'sec_included_chars_list': '- **Jason Duval** - Protagonista maschile: combattimento, guida, forza\n'
                            '- **Lucia Caminos** - Protagonista femminile (prima in GTA!): hacking, furtività, '
                            'agilità\n'
                            '- Sistema dual come GTA V\n'
                            '- Cambio personaggio\n'
                            '- Abilità uniche',
 'sec_included_missions_h': '🎯 Missioni e attività',
 'sec_included_missions_list': '- Rapine in banca (inclusa la famosa trapelata)\n'
                               '- Inseguimenti della polizia\n'
                               '- Missioni storia\n'
                               '- Attività secondarie\n'
                               '- Poligoni di tiro\n'
                               '- Furto veicoli\n'
                               '- E altro!',
 'sec_included_vehicles_h': '🚗 150+ veicoli',
 'sec_included_vehicles_list': '- Auto, moto, barche, elicotteri\n'
                               '- Fisica avanzata\n'
                               '- Danni realistici\n'
                               '- Personalizzazione\n'
                               '- Guida migliore di GTA V',
 'sec_included_source_h': '💻 Codice sorgente (3GB+)',
 'sec_included_source_list': '- Motore (RAGE 9)\n'
                             '- Script missioni\n'
                             '- Fisica veicoli\n'
                             '- Sistemi IA\n'
                             '- Dati mappa\n'
                             '- Pipeline asset\n'
                             '- Codice rete GTA Online 2',
 'sec_included_debug_h': '🛠️ Strumenti debug',
 'sec_included_debug_list': '- Console dev (`~`)\n'
                            '- Menu spawn\n'
                            '- Teletrasporto\n'
                            '- God mode\n'
                            '- Tutte le missioni\n'
                            '- Senza wanted level\n'
                            '- Controllo meteo/tempo',
 'sec_install_title': '📥 Come scaricare e installare',
 'install_labels': ['Passo 1: Sito ufficiale',
                    'Passo 2: Scegli il build',
                    'Passo 3: Scarica il launcher GTA 6',
                    'Passo 4: Scarica il build',
                    'Passo 5: Estrai i file',
                    'Passo 6: Esegui GTA6Launcher.exe',
                    'Passo 7: Configura impostazioni',
                    'Passo 8: Avvia e gioca!'],
 'install_bodies': ['Clicca il pulsante download per visitare **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — '
                    'fonte ufficiale e sicura.',
                    'Scegli la versione build GTA 6:\n'
                    '- **Q2 2022 (Consigliato)** - Più stabile e completo\n'
                    '- **Q1 2022** - Buon equilibrio\n'
                    '- **Q4 2021** - Sviluppo precoce',
                    '- Dimensione: ~5GB\n- Include launcher e file core\n- Solo Windows 10/11 64-bit',
                    '- Ogni build: 15-25GB\n- Archivio compresso (.zip o .rar)\n- Spazio consigliato: 100GB+',
                    '- Estrai in cartella con spazio libero\n'
                    '- Consigliato: `C:\\GTA6\\` o `D:\\Games\\GTA6\\`\n'
                    '- NON estrarre in Program Files',
                    '- Tasto destro su `GTA6Launcher.exe`\n'
                    '- **«Esegui come amministratore»**\n'
                    '- Se Windows avvisa, clicca «Esegui comunque»',
                    '- Scegli versione build\n- Configura grafica e risoluzione\n- Regola controlli se necessario',
                    '- Clicca **«LAUNCH GAME»**\n'
                    '- Attendi 1-2 minuti la prima volta\n'
                    "- **Goditi GTA 6 prima dell'uscita ufficiale!** 🎮"],
 'sec_specs_title': '💻 Requisiti di sistema',
 'sec_specs_min_h': 'Requisiti minimi',
 'sec_specs_rec_h': 'Requisiti consigliati',
 'tbl_spec_header': ('Componente', 'Requisito'),
 'min_specs': [('Sistema operativo', 'Windows 10 64-bit o Windows 11 64-bit'),
               ('Processore', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('Memoria', '16 GB RAM'),
               ('Grafica', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', 'Versione 12'),
               ('Archiviazione', '50+ GB SSD (100GB+ consigliato)'),
               ('Rete', 'Connessione broadband per il download')],
 'rec_specs': [('Sistema operativo', 'Windows 11 64-bit'),
               ('Processore', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('Memoria', '32 GB RAM'),
               ('Grafica', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'Versione 12'),
               ('Archiviazione', '100+ GB NVMe SSD'),
               ('Rete', 'Connessione broadband')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox e Mac NON supportati** - solo Windows PC\n'
                         '- ✅ SSD fortemente consigliato\n'
                         '- ✅ Driver grafici aggiornati (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 installato\n'
                         '- ✅ Visual C++ Redistributables (inclusi)',
 'sec_about_title': '🔍 Info su CyberLeek',
 'sec_about_who_h': 'Chi è CyberLeak / CyberLeek?',
 'sec_about_who_p': '**CyberLeak** (CyberLeak e CyberLeek) è la fonte anonima della **fuga GTA 6 di agosto 2026**, una '
                    'delle più significative.',
 'sec_about_timeline_h': 'Cronologia fughe CyberLeak:',
 'timeline': [('18 agosto 2026', 'Primi video gameplay trapelati'),
              ('19 agosto 2026', 'Altro footage di Jason e Lucia'),
              ('20-21 agosto 2026', 'Vice City, missioni, veicoli'),
              ('22 agosto 2026', 'CyberLeak pubblica «LEEK» con proiettili — prova di accesso'),
              ('23-27 agosto 2026', 'Fughe prima del Netflix Extended Look di Rockstar')],
 'sec_about_compare_h': 'Cosa distingue CyberLeak dalla fuga 2022?',
 'tbl_compare_header': ('Caratteristica', 'CyberLeak (Ago 2026)', 'teapotuberhacker (Set 2022)'),
 'compare_rows': [('Data', 'Agosto 2026', 'Settembre 2022'),
                  ('Versione build', 'Più recente (2022)', 'Più vecchia (2021-2022)'),
                  ('Qualità video', 'Alta qualità', 'Inferiore, footage dev'),
                  ('Quantità', '90+ minuti', '50+ minuti'),
                  ('Prova accesso', '«LEEK» in gioco', 'Clip multipli'),
                  ('Fonte', 'Sconosciuta', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': 'Perché cercano «CyberLeak GTA 6»',
 'sec_about_search_p': '**Milioni di giocatori** cercano specificamente:',
 'sec_about_search_list': '- «GTA 6 CyberLeak download»\n'
                          '- «CyberLeek playable build»\n'
                          '- «GTA 6 CyberLeak 2026»\n'
                          '- «Download GTA 6 from CyberLeak»\n'
                          '- «CyberLeek leak archive»\n'
                          '\n'
                          '**Perché?** Perché il contenuto CyberLeak è:',
 'why_search_bullets': ['✅ **Più recente** - Più vicino al gioco finale (2026 vs 2022)',
                        '✅ **Migliore qualità** - Miglior video e audio',
                        '✅ **Più completo** - Più funzioni e gameplay',
                        '✅ **Accesso provato** - Build giocabile reale dimostrato',
                        '✅ **Completo** - Vice City, protagonisti, missioni, ecc.'],
 'sec_about_official': "CyberLeakGTA6.net è l'archivio ufficiale di tutto il contenuto CyberLeak.",
 'sec_safety_title': '🛡️ Sicurezza',
 'sec_safety_warn_h': '⚠️ AVVERTENZA IMPORTANTE',
 'sec_safety_warn_p': '**ATTENZIONE AI DOWNLOAD FALSI!** Siti truffa distribuiscono **falsi «build GTA 6»** con:',
 'sec_safety_warn_list': '- ❌ Virus e malware\n- ❌ Ransomware\n- ❌ Miner crypto\n- ❌ Spyware e keylogger\n- ❌ Trojan',
 'sec_safety_fake_p': 'Il falso più comune: **torrent da 113GB** con spazio vuoto e malware nascosto.',
 'sec_safety_how_h': '✅ Come restare al sicuro:',
 'sec_safety_how_list': '1. **Scarica SOLO da CyberLeakGTA6.net**\n'
                        '2. **MAI** da torrent casuali\n'
                        '3. **Verifica le dimensioni** - i nostri build 15-25GB, NON 113GB\n'
                        '4. **Usa antivirus** - Windows Defender va bene\n'
                        '5. **Mantieni Windows aggiornato**\n'
                        "6. **Non disattivare l'antivirus** - se lo chiedono, è malware!",
 'sec_safety_guarantee_h': '🛡️ Le nostre garanzie:',
 'sec_safety_guarantee_list': '- ✅ Scansionato da 15+ antivirus\n'
                              '- ✅ Nessuna registrazione\n'
                              '- ✅ Nessun file nascosto\n'
                              '- ✅ Nessun miner\n'
                              '- ✅ Nessuno spyware\n'
                              '- ✅ Download diretto ufficiale',
 'sec_safety_report_h': '📧 Segnala siti falsi',
 'sec_safety_report_p': 'Se trovi siti sospetti «CyberLeak» o «GTA 6 download», segnalali. Unico sito ufficiale: '
                        '**CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ FAQ (Domande frequenti)',
 'faq': [('D: È il vero build giocabile GTA 6 di CyberLeak?',
          '**R:** SÌ! Archivio autentico con file giocabili, launcher e tutto il footage. CyberLeakGTA6.net è la fonte '
          'ufficiale.'),
         ("D: Posso giocare a GTA 6 prima dell'uscita del 19 novembre 2026?",
          '**R:** SÌ! Scarica il nostro launcher e i build trapelati. Vice City, missioni, veicoli, Jason Duval e '
          'Lucia Caminos.'),
         ('D: È legale scaricare il build trapelato?',
          '**R:** Build di sviluppo trapelato per scopi educativi e di archivio. Non incoraggiamo la pirateria. '
          '**Supporta Rockstar acquistando GTA 6 il 19 novembre 2026.**'),
         ('D: Sarò bannato o avrò problemi?',
          '**R:** Build single-player NON connesso ai server Rockstar. Nessun ban possibile. Consulta le leggi '
          'locali.'),
         ('D: Differenza tra CyberLeak e teapotuberhacker 2022?',
          '**R:** La fuga 2022 fu la prima (teapotuberhacker/Lapsus$). CyberLeak agosto 2026 è più recente, migliore '
          'qualità, build più recente e copertura più completa.'),
         ('D: Perché serve il launcher GTA 6?',
          '**R:** I build dev richiedono parametri specifici. Il nostro launcher automatizza tutto — un clic per '
          'giocare.'),
         ('D: Dimensione download e spazio?',
          '**R:** \\n- Launcher: ~5GB\\n- Ogni build: 15-25GB\\n- Totale: ~80-100GB\\n- **Consigliato:** 100GB+ SSD'),
         ('D: Funziona su PS5, Xbox o Mac?', '**R:** NO. Solo Windows PC 64-bit. Build di sviluppo PC.'),
         ('D: Gioco completo o demo?',
          '**R:** Build dev 2021-2022, non il gioco finale. Grande mappa Vice City, missioni, Jason & Lucia, 150+ '
          'veicoli e altro.'),
         ('D: Sarà aggiornato con nuove fughe?',
          '**R:** SÌ! Monitoriamo CyberLeak e aggiorniamo. Aggiungi **CyberLeakGTA6.net** ai preferiti.'),
         ('D: Posso moddare il build?',
          '**R:** SÌ! Con 3GB+ di codice sorgente, i modder possono creare mod e script.'),
         ("D: C'è multigiocatore / GTA Online?",
          '**R:** NO. Build single-player. Codice GTA Online 2 early ma senza multigiocatore funzionale.'),
         ("D: L'antivirus segnala il launcher?",
          '**R:** 100% sicuro, 15+ antivirus. Possibile falso positivo euristico. VirusTotal.com o eccezione.'),
         ('D: Crash o non parte?',
          '**R:** \\n1. Esegui come amministratore\\n2. Visual C++ Redistributables\\n3. Driver NVIDIA/AMD\\n4. '
          'DirectX 12\\n5. Prova Q2 2022\\n6. Minimo 16GB RAM\\n7. Disattiva overclock'),
         ('D: Posso streammare o caricare su YouTube?',
          '**R:** Tecnicamente sì, ma Rockstar invia DMCA per contenuto trapelato. A tuo rischio.')],
 'lang_section_title': '🌍 Altre lingue | Other Languages | Другие языки',
 'lang_section_intro': 'Questo README è disponibile in 12 lingue:',
 'lang_table_header': ('Lingua', 'File', 'Link'),
 'lang_here': 'Sei qui!',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ SCARICA IL BUILD GTA 6 CYBERLEEK ORA →',
 'footer_h3': "🎮 **GIOCA A GTA 6 PRIMA DELL'USCITA UFFICIALE!**",
 'footer_archive': 'Archivio ufficiale CyberLeak GTA 6',
 'footer_updated': 'Aggiornato: August 28, 2026 | Download: 3.000.000+',
 'footer_disclaimer1': 'Non affiliato a Rockstar Games o Take-Two Interactive',
 'footer_disclaimer2': 'Supporta Rockstar acquistando GTA 6 il 19 novembre 2026',
 'footer_made': 'Fatto con ❤️ dalla community GTA | Preservato per la storia del gaming'}


def _pt() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - BAIXAR BUILD JOGÁVEL | Agosto 2026',
 'badge_build': 'BUILD',
 'badge_status_key': 'STATUS',
 'badge_status_val': 'JOGÁVEL',
 'badge_dl_key': 'downloads',
 'badge_upd_key': 'atualizado',
 'badge_upd_val': 'Agosto%202026',
 'hero_h2': '🔥 **BAIXE E JOGUE O BUILD VAZADO GTA 6 DO CYBERLEEK** 🔥',
 'hero_h3': '**O build jogável autêntico do CyberLeak que todos procuram**',
 'hero_tags': '🎮 Jogo jogável | 🚀 Launcher GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Código-fonte',
 'hero_cta': '⬇️ BAIXAR BUILD GTA 6 CYBERLEEK AGORA →',
 'toc_title': '📖 Índice',
 'toc': [('🎯 O que é o build GTA 6 CyberLeek?', '-what-is-cyberleek-gta-6-build'),
         ('⭐ Por que baixar do CyberLeak?', '-why-download-from-cyberleek'),
         ('🎮 Conteúdo incluído', '-whats-included'),
         ('📥 Como baixar e instalar', '-how-to-download--install'),
         ('💻 Requisitos do sistema', '-system-requirements'),
         ('🔍 Sobre o CyberLeak', '-about-cyberleek'),
         ('🛡️ Segurança', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 Outros idiomas', '-other-languages')],
 'sec_what_title': '🎯 O que é o build GTA 6 CyberLeek?',
 'sec_what_intro': '**CyberLeak** (também **CyberLeek**) é a fonte do **vazamento GTA 6 mais recente e completo** em '
                   '**agosto de 2026**, pouco antes do Netflix Extended Look oficial da Rockstar.',
 'sec_what_sub': '🔓 Este é O build vazado que todos procuram:',
 'sec_what_list': '- ✅ **BUILD JOGÁVEL** - Não são só vídeos! Jogo real para baixar e jogar agora\n'
                  '- ✅ **Vazamento mais recente** - Agosto 2026, mais novo que teapotuberhacker setembro 2022\n'
                  '- ✅ **Arquivo completo** - 90+ minutos de gameplay, código-fonte e builds jogáveis\n'
                  '- ✅ **Prova de autenticidade** - CyberLeak escreveu «LEEK» com balas no jogo\n'
                  '- ✅ **Gameplay Vice City** - Explore Vice City antes do lançamento em 19 de novembro de 2026',
 'sec_what_yes': 'SIM, VOCÊ PODE JOGAR DE VERDADE!',
 'sec_what_yes_body': 'Não é só uma coleção de vídeos — é o build de desenvolvimento jogável real do GTA 6 com nosso '
                      'launcher personalizado.',
 'sec_why_title': '⭐ Por que baixar do CyberLeak?',
 'sec_why_playable_h': '🎮 **BUILDS JOGÁVEIS**',
 'sec_why_playable_p': 'Não são só vídeos! Baixe e jogue builds vazados GTA 6 2021-2022. Missões, Vice City, veículos '
                       'e ambos protagonistas.',
 'sec_why_original_h': '🔥 **CYBERLEEK ORIGINAL**',
 'sec_why_original_p': 'O build autêntico CyberLeak que milhões procuram. «GTA 6 CyberLeak download», «CyberLeek '
                       'playable build», «GTA 6 CyberLeak 2026» — este é o arquivo.',
 'sec_why_versions_h': '📦 **3 VERSÕES DO JOGO**',
 'sec_why_versions_p': 'Escolha entre 3 builds de desenvolvimento:',
 'sec_why_versions_list': '- **Q2 2022** (junho 2022) - Mais recente, estável, completo\n'
                          '- **Q1 2022** (março 2022) - Estável, funções principais\n'
                          '- **Q4 2021** (dezembro 2021) - Build inicial, experimental',
 'sec_why_launcher_h': '🚀 **LAUNCHER GTA 6 PERSONALIZADO**',
 'sec_why_launcher_p': 'Launcher GTA 6 personalizado: baixe, extraia e clique em «Launch Game».',
 'sec_why_videos_h': '🎥 **90+ VÍDEOS VAZADOS**',
 'sec_why_videos_p': 'Coleção completa de gameplay vazado CyberLeak (90+ minutos):',
 'sec_why_videos_list': '- Exploração Vice City\n'
                        '- Gameplay Jason & Lucia\n'
                        '- Missões de assalto\n'
                        '- Perseguições policiais\n'
                        '- Veículos\n'
                        '- Sistema de combate\n'
                        '- E muito mais!',
 'sec_why_source_h': '💻 **ACESSO AO CÓDIGO-FONTE**',
 'sec_why_source_p': '3GB+ de código-fonte de desenvolvimento GTA 6 para desenvolvedores e modders.',
 'sec_why_free_h': '🆓 **100% GRÁTIS**',
 'sec_why_free_list': '- Sem pagamento\n- Sem registro\n- Sem pesquisas\n- Download direto\n- Acesso instantâneo',
 'sec_why_safe_h': '🛡️ **SEGURO E VERIFICADO**',
 'sec_why_safe_list': '- Verificado por 15+ antivírus\n'
                      '- Sem vírus ou malware\n'
                      '- Sem miners ocultos\n'
                      '- Estrutura transparente\n'
                      '- Fonte oficial CyberLeakGTA6.net',
 'sec_included_title': '🎮 Conteúdo incluído',
 'sec_included_builds_h': '🕹️ Builds jogáveis',
 'tbl_build_header': ('Versão', 'Data', 'Status', 'Recursos'),
 'builds_rows': [('Q2 2022', 'Junho 2022', '✅ Mais estável', 'Últimos recursos, melhor otimização, recomendado'),
                 ('Q1 2022', 'Março 2022', '✅ Estável', 'Recursos principais, bom desempenho'),
                 ('Q4 2021', 'Dezembro 2021', '⚠️ Experimental', 'Recursos iniciais, alguns bugs')],
 'sec_included_launcher_h': '🚀 Launcher GTA 6',
 'sec_included_launcher_list': '- Launcher personalizado\n'
                               '- Início com um clique\n'
                               '- Seletor de build (Q2/Q1/Q4 2022)\n'
                               '- Configuração gráfica\n'
                               '- Seletor de resolução\n'
                               '- Ferramentas debug\n'
                               '- Apenas Windows (64-bit)',
 'sec_included_map_h': '🗺️ Mapa Vice City',
 'sec_included_map_list': '- Vice City moderna explorável (Miami)\n'
                          '- Tamanho: ~2x Los Santos do GTA V\n'
                          '- Downtown, praias, subúrbios, Everglades\n'
                          '- Ciclo dia/noite\n'
                          '- Clima dinâmico\n'
                          '- Interiores detalhados',
 'sec_included_chars_h': '👥 Personagens jogáveis',
 'sec_included_chars_list': '- **Jason Duval** - Protagonista masculino: combate, direção, força\n'
                            '- **Lucia Caminos** - Protagonista feminina (primeira no GTA!): hacking, furtividade, '
                            'agilidade\n'
                            '- Sistema dual como GTA V\n'
                            '- Troca de personagem\n'
                            '- Habilidades únicas',
 'sec_included_missions_h': '🎯 Missões e atividades',
 'sec_included_missions_list': '- Assaltos bancários (incluindo o famoso vazado)\n'
                               '- Perseguições policiais\n'
                               '- Missões de história\n'
                               '- Atividades secundárias\n'
                               '- Campos de tiro\n'
                               '- Roubo de veículos\n'
                               '- E mais!',
 'sec_included_vehicles_h': '🚗 150+ veículos',
 'sec_included_vehicles_list': '- Carros, motos, barcos, helicópteros\n'
                               '- Física avançada\n'
                               '- Danos realistas\n'
                               '- Personalização\n'
                               '- Melhor condução que GTA V',
 'sec_included_source_h': '💻 Código-fonte (3GB+)',
 'sec_included_source_list': '- Motor (RAGE 9)\n'
                             '- Scripts de missões\n'
                             '- Física de veículos\n'
                             '- Sistemas IA\n'
                             '- Dados do mapa\n'
                             '- Pipeline de assets\n'
                             '- Código de rede GTA Online 2',
 'sec_included_debug_h': '🛠️ Ferramentas debug',
 'sec_included_debug_list': '- Console dev (`~`)\n'
                            '- Menu spawn\n'
                            '- Teletransporte\n'
                            '- God mode\n'
                            '- Todas as missões\n'
                            '- Sem wanted level\n'
                            '- Controle clima/tempo',
 'sec_install_title': '📥 Como baixar e instalar',
 'install_labels': ['Passo 1: Site oficial',
                    'Passo 2: Escolha seu build',
                    'Passo 3: Baixe o launcher GTA 6',
                    'Passo 4: Baixe o build',
                    'Passo 5: Extraia arquivos',
                    'Passo 6: Execute GTA6Launcher.exe',
                    'Passo 7: Configure ajustes',
                    'Passo 8: Inicie e jogue!'],
 'install_bodies': ['Clique no botão de download para visitar **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — '
                    'fonte oficial e segura.',
                    'Escolha sua versão de build GTA 6:\n'
                    '- **Q2 2022 (Recomendado)** - Mais estável e completo\n'
                    '- **Q1 2022** - Bom equilíbrio\n'
                    '- **Q4 2021** - Desenvolvimento inicial',
                    '- Tamanho: ~5GB\n- Inclui launcher e arquivos core\n- Apenas Windows 10/11 64-bit',
                    '- Cada build: 15-25GB\n- Arquivo compactado (.zip ou .rar)\n- Espaço recomendado: 100GB+',
                    '- Extraia para pasta com espaço livre\n'
                    '- Recomendado: `C:\\GTA6\\` ou `D:\\Games\\GTA6\\`\n'
                    '- NÃO extraia em Program Files',
                    '- Clique direito em `GTA6Launcher.exe`\n'
                    '- **«Executar como administrador»**\n'
                    '- Se o Windows avisar, clique «Executar mesmo assim»',
                    '- Escolha versão do build\n- Configure gráficos e resolução\n- Ajuste controles se necessário',
                    '- Clique **«LAUNCH GAME»**\n'
                    '- Aguarde 1-2 minutos na primeira vez\n'
                    '- **Aproveite GTA 6 antes do lançamento oficial!** 🎮'],
 'sec_specs_title': '💻 Requisitos do sistema',
 'sec_specs_min_h': 'Requisitos mínimos',
 'sec_specs_rec_h': 'Requisitos recomendados',
 'tbl_spec_header': ('Componente', 'Requisito'),
 'min_specs': [('Sistema operacional', 'Windows 10 64-bit ou Windows 11 64-bit'),
               ('Processador', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('Memória', '16 GB RAM'),
               ('Placa gráfica', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', 'Versão 12'),
               ('Armazenamento', '50+ GB SSD (100GB+ recomendado)'),
               ('Rede', 'Conexão broadband para download')],
 'rec_specs': [('Sistema operacional', 'Windows 11 64-bit'),
               ('Processador', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('Memória', '32 GB RAM'),
               ('Placa gráfica', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'Versão 12'),
               ('Armazenamento', '100+ GB NVMe SSD'),
               ('Rede', 'Conexão broadband')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox e Mac NÃO suportados** - apenas Windows PC\n'
                         '- ✅ SSD altamente recomendado\n'
                         '- ✅ Drivers gráficos atualizados (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 instalado\n'
                         '- ✅ Visual C++ Redistributables (incluídos)',
 'sec_about_title': '🔍 Sobre CyberLeek',
 'sec_about_who_h': 'Quem é CyberLeak / CyberLeek?',
 'sec_about_who_p': '**CyberLeak** (CyberLeak e CyberLeek) é a fonte anônima do **vazamento GTA 6 de agosto de 2026**, '
                    'um dos mais significativos.',
 'sec_about_timeline_h': 'Cronologia dos vazamentos CyberLeak:',
 'timeline': [('18 de agosto de 2026', 'Primeiros vídeos de gameplay vazados'),
              ('19 de agosto de 2026', 'Mais footage de Jason e Lucia'),
              ('20-21 de agosto de 2026', 'Vice City, missões, veículos'),
              ('22 de agosto de 2026', 'CyberLeak publica «LEEK» com balas — prova de acesso'),
              ('23-27 de agosto de 2026', 'Vazamentos antes do Netflix Extended Look da Rockstar')],
 'sec_about_compare_h': 'O que diferencia CyberLeak do vazamento 2022?',
 'tbl_compare_header': ('Recurso', 'CyberLeak (Ago 2026)', 'teapotuberhacker (Set 2022)'),
 'compare_rows': [('Data', 'Agosto 2026', 'Setembro 2022'),
                  ('Versão build', 'Mais nova (2022)', 'Mais antiga (2021-2022)'),
                  ('Qualidade vídeo', 'Alta qualidade', 'Menor, footage dev'),
                  ('Quantidade', '90+ minutos', '50+ minutos'),
                  ('Prova de acesso', '«LEEK» no jogo', 'Vários clipes'),
                  ('Fonte', 'Desconhecida', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': 'Por que procuram «CyberLeak GTA 6»',
 'sec_about_search_p': '**Milhões de jogadores** procuram especificamente:',
 'sec_about_search_list': '- «GTA 6 CyberLeak download»\n'
                          '- «CyberLeek playable build»\n'
                          '- «GTA 6 CyberLeak 2026»\n'
                          '- «Download GTA 6 from CyberLeak»\n'
                          '- «CyberLeek leak archive»\n'
                          '\n'
                          '**Por quê?** Porque o conteúdo CyberLeak é:',
 'why_search_bullets': ['✅ **Mais recente** - Mais perto do jogo final (2026 vs 2022)',
                        '✅ **Melhor qualidade** - Melhor vídeo e áudio',
                        '✅ **Mais completo** - Mais recursos e gameplay',
                        '✅ **Acesso comprovado** - Build jogável real demonstrado',
                        '✅ **Abrangente** - Vice City, protagonistas, missões, etc.'],
 'sec_about_official': 'CyberLeakGTA6.net é o arquivo oficial de todo o conteúdo CyberLeak.',
 'sec_safety_title': '🛡️ Segurança',
 'sec_safety_warn_h': '⚠️ AVISO IMPORTANTE',
 'sec_safety_warn_p': '**CUIDADO COM DOWNLOADS FALSOS!** Sites fraudulentos distribuem **«builds GTA 6» falsos** com:',
 'sec_safety_warn_list': '- ❌ Vírus e malware\n'
                         '- ❌ Ransomware\n'
                         '- ❌ Miners de cripto\n'
                         '- ❌ Spyware e keyloggers\n'
                         '- ❌ Trojans',
 'sec_safety_fake_p': 'A falsificação mais comum: **torrent de 113GB** com espaço vazio e malware oculto.',
 'sec_safety_how_h': '✅ Como se manter seguro:',
 'sec_safety_how_list': '1. **Baixe APENAS de CyberLeakGTA6.net**\n'
                        '2. **NUNCA** de torrents aleatórios\n'
                        '3. **Verifique tamanhos** - nossos builds 15-25GB, NÃO 113GB\n'
                        '4. **Use antivírus** - Windows Defender serve\n'
                        '5. **Mantenha Windows atualizado**\n'
                        '6. **Não desative antivírus** - se pedirem, é malware!',
 'sec_safety_guarantee_h': '🛡️ Nossas garantias:',
 'sec_safety_guarantee_list': '- ✅ Verificado por 15+ antivírus\n'
                              '- ✅ Sem registro\n'
                              '- ✅ Sem arquivos ocultos\n'
                              '- ✅ Sem miners\n'
                              '- ✅ Sem spyware\n'
                              '- ✅ Download direto oficial',
 'sec_safety_report_h': '📧 Reportar sites falsos',
 'sec_safety_report_p': 'Se encontrar sites suspeitos «CyberLeak» ou «GTA 6 download», reporte. Único site oficial: '
                        '**CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ FAQ (Perguntas frequentes)',
 'faq': [('P: É o build jogável real GTA 6 do CyberLeak?',
          '**R:** SIM! Arquivo autêntico com arquivos jogáveis, launcher e todo footage. CyberLeakGTA6.net é a fonte '
          'oficial.'),
         ('P: Posso jogar GTA 6 antes do lançamento em 19 de novembro de 2026?',
          '**R:** SIM! Baixe nosso launcher e builds vazados. Vice City, missões, veículos, Jason Duval e Lucia '
          'Caminos.'),
         ('P: É legal baixar o build vazado?',
          '**R:** Build de desenvolvimento vazado para fins educacionais e de arquivo. Não incentivamos pirataria. '
          '**Apoie Rockstar comprando GTA 6 em 19 de novembro de 2026.**'),
         ('P: Serei banido ou terei problemas?',
          '**R:** Build single-player NÃO conectado aos servidores Rockstar. Sem ban possível. Consulte leis locais.'),
         ('P: Diferença entre CyberLeak e teapotuberhacker 2022?',
          '**R:** Vazamento 2022 foi o primeiro (teapotuberhacker/Lapsus$). CyberLeak agosto 2026 é mais novo, melhor '
          'qualidade, build mais recente e cobertura mais completa.'),
         ('P: Por que preciso do launcher GTA 6?',
          '**R:** Builds dev requerem parâmetros específicos. Nosso launcher automatiza tudo — um clique para jogar.'),
         ('P: Tamanho do download e espaço?',
          '**R:** \\n- Launcher: ~5GB\\n- Cada build: 15-25GB\\n- Total: ~80-100GB\\n- **Recomendado:** 100GB+ SSD'),
         ('P: Funciona em PS5, Xbox ou Mac?', '**R:** NÃO. Apenas Windows PC 64-bit. Builds de desenvolvimento PC.'),
         ('P: Jogo completo ou demo?',
          '**R:** Builds dev 2021-2022, não o jogo final. Grande mapa Vice City, missões, Jason & Lucia, 150+ veículos '
          'e mais.'),
         ('P: Será atualizado com novos vazamentos?',
          '**R:** SIM! Monitoramos CyberLeak e atualizamos. Favorite **CyberLeakGTA6.net**.'),
         ('P: Posso modificar o build?', '**R:** SIM! Com 3GB+ de código-fonte, modders podem criar mods e scripts.'),
         ('P: Há multijogador / GTA Online?',
          '**R:** NÃO. Builds single-player. Código GTA Online 2 inicial mas sem multijogador funcional.'),
         ('P: Antivírus marca o launcher?',
          '**R:** 100% seguro, 15+ antivírus. Falso positivo heurístico possível. VirusTotal.com ou exceção.'),
         ('P: Crash ou não inicia?',
          '**R:** \\n1. Executar como administrador\\n2. Visual C++ Redistributables\\n3. Drivers NVIDIA/AMD\\n4. '
          'DirectX 12\\n5. Tente Q2 2022\\n6. Mínimo 16GB RAM\\n7. Desative overclock'),
         ('P: Posso transmitir ou publicar no YouTube?',
          '**R:** Tecnicamente sim, mas Rockstar envia DMCA por conteúdo vazado. Por sua conta e risco.')],
 'lang_section_title': '🌍 Outros idiomas | Other Languages | Другие языки',
 'lang_section_intro': 'Este README está disponível em 12 idiomas:',
 'lang_table_header': ('Idioma', 'Arquivo', 'Link'),
 'lang_here': 'Você está aqui!',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ BAIXAR BUILD GTA 6 CYBERLEEK AGORA →',
 'footer_h3': '🎮 **JOGUE GTA 6 ANTES DO LANÇAMENTO OFICIAL!**',
 'footer_archive': 'Arquivo oficial CyberLeak GTA 6',
 'footer_updated': 'Atualizado: August 28, 2026 | Downloads: 3.000.000+',
 'footer_disclaimer1': 'Não afiliado à Rockstar Games ou Take-Two Interactive',
 'footer_disclaimer2': 'Apoie Rockstar comprando GTA 6 em 19 de novembro de 2026',
 'footer_made': 'Feito com ❤️ pela comunidade GTA | Preservado para a história dos games'}

def _pl() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - POBIERZ GRYWALNY BUILD | Sierpień 2026',
 'badge_build': 'BUILD',
 'badge_status_key': 'STATUS',
 'badge_status_val': 'GRYWALNY',
 'badge_dl_key': 'pobrania',
 'badge_upd_key': 'zaktualizowano',
 'badge_upd_val': 'Sierpie%C5%84%202026',
 'hero_h2': '🔥 **POBIERZ I GRAJ W BUILD GTA 6 Z CYBERLEEK** 🔥',
 'hero_h3': '**Autentyczny grywalny build CyberLeak, którego wszyscy szukają**',
 'hero_tags': '🎮 Grywalna gra | 🚀 Launcher GTA 6 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Kod źródłowy',
 'hero_cta': '⬇️ POBIERZ BUILD GTA 6 CYBERLEEK TERAZ →',
 'toc_title': '📖 Spis treści',
 'toc': [('🎯 Czym jest build GTA 6 CyberLeek?', '-what-is-cyberleek-gta-6-build'),
         ('⭐ Dlaczego pobierać z CyberLeak?', '-why-download-from-cyberleek'),
         ('🎮 Co zawiera', '-whats-included'),
         ('📥 Jak pobrać i zainstalować', '-how-to-download--install'),
         ('💻 Wymagania systemowe', '-system-requirements'),
         ('🔍 O CyberLeak', '-about-cyberleek'),
         ('🛡️ Bezpieczeństwo', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 Inne języki', '-other-languages')],
 'sec_what_title': '🎯 Czym jest build GTA 6 CyberLeek?',
 'sec_what_intro': '**CyberLeak** (także **CyberLeek**) to źródło **najnowszego i najpełniejszego wycieku GTA 6** z '
                   '**sierpnia 2026**, tuż przed oficjalnym Netflix Extended Look Rockstar.',
 'sec_what_sub': '🔓 To TEN wyciekany build, którego wszyscy szukają:',
 'sec_what_list': '- ✅ **GRYWALNY BUILD** - Nie tylko filmy! Prawdziwa gra do pobrania i grania teraz\n'
                  '- ✅ **Najnowszy wyciek** - Sierpień 2026, nowszy niż teapotuberhacker wrzesień 2022\n'
                  '- ✅ **Pełne archiwum** - 90+ minut rozgrywki, kod źródłowy i grywalne buildy\n'
                  '- ✅ **Dowód autentyczności** - CyberLeak napisał «LEEK» kulami w grze\n'
                  '- ✅ **Rozgrywka Vice City** - Odkrywaj Vice City przed premierą 19 listopada 2026',
 'sec_what_yes': 'TAK, MOŻESZ NAPRAWDĘ W TO GRAĆ!',
 'sec_what_yes_body': 'To nie kolekcja filmów — to prawdziwy grywalny build deweloperski GTA 6 z naszym '
                      'niestandardowym launcherem.',
 'sec_why_title': '⭐ Dlaczego pobierać z CyberLeak?',
 'sec_why_playable_h': '🎮 **GRYWALNE BUILDY**',
 'sec_why_playable_p': 'Nie tylko filmy! Pobierz i graj w wycieki deweloperskie GTA 6 2021-2022. Misje, Vice City, '
                       'pojazdy i oboje protagonistów.',
 'sec_why_original_h': '🔥 **ORYGINAŁ CYBERLEEK**',
 'sec_why_original_p': 'Autentyczny build CyberLeak, którego szukają miliony. «GTA 6 CyberLeak download», «CyberLeek '
                       'playable build», «GTA 6 CyberLeak 2026» — to jest to archiwum.',
 'sec_why_versions_h': '📦 **3 WERSJE GRY**',
 'sec_why_versions_p': 'Wybierz spośród 3 buildów deweloperskich:',
 'sec_why_versions_list': '- **Q2 2022** (czerwiec 2022) - Najnowszy, stabilny, kompletny\n'
                          '- **Q1 2022** (marzec 2022) - Stabilny, główne funkcje\n'
                          '- **Q4 2021** (grudzień 2021) - Wczesny build, eksperymentalny',
 'sec_why_launcher_h': '🚀 **NIESTANDARDOWY LAUNCHER GTA 6**',
 'sec_why_launcher_p': 'Niestandardowy launcher GTA 6: pobierz, rozpakuj i kliknij «Launch Game».',
 'sec_why_videos_h': '🎥 **90+ WYCIEKŁYCH FILMÓW**',
 'sec_why_videos_p': 'Pełna kolekcja wycieku rozgrywki CyberLeak (90+ minut):',
 'sec_why_videos_list': '- Eksploracja Vice City\n'
                        '- Rozgrywka Jason & Lucia\n'
                        '- Misje napadów\n'
                        '- Pościgi policyjne\n'
                        '- Pojazdy\n'
                        '- System walki\n'
                        '- I wiele więcej!',
 'sec_why_source_h': '💻 **DOSTĘP DO KODU ŹRÓDŁOWEGO**',
 'sec_why_source_p': '3GB+ kodu źródłowego GTA 6 dla deweloperów i modderów.',
 'sec_why_free_h': '🆓 **100% ZA DARMO**',
 'sec_why_free_list': '- Bez płatności\n'
                      '- Bez rejestracji\n'
                      '- Bez ankiet\n'
                      '- Bezpośrednie pobieranie\n'
                      '- Natychmiastowy dostęp',
 'sec_why_safe_h': '🛡️ **BEZPIECZNY I ZWERYFIKOWANY**',
 'sec_why_safe_list': '- Skanowany przez 15+ antywirusów\n'
                      '- Bez wirusów i malware\n'
                      '- Bez ukrytych minerów\n'
                      '- Przejrzysta struktura\n'
                      '- Oficjalne źródło CyberLeakGTA6.net',
 'sec_included_title': '🎮 Co zawiera',
 'sec_included_builds_h': '🕹️ Grywalne buildy',
 'tbl_build_header': ('Wersja', 'Data', 'Status', 'Funkcje'),
 'builds_rows': [('Q2 2022',
                  'Czerwiec 2022',
                  '✅ Najbardziej stabilny',
                  'Najnowsze funkcje, najlepsza optymalizacja, polecany'),
                 ('Q1 2022', 'Marzec 2022', '✅ Stabilny', 'Główne funkcje, dobra wydajność'),
                 ('Q4 2021', 'Grudzień 2021', '⚠️ Eksperymentalny', 'Wczesne funkcje, niektóre błędy')],
 'sec_included_launcher_h': '🚀 Launcher GTA 6',
 'sec_included_launcher_list': '- Niestandardowy launcher\n'
                               '- Uruchomienie jednym kliknięciem\n'
                               '- Wybór buildu (Q2/Q1/Q4 2022)\n'
                               '- Konfiguracja grafiki\n'
                               '- Wybór rozdzielczości\n'
                               '- Narzędzia debug\n'
                               '- Tylko Windows (64-bit)',
 'sec_included_map_h': '🗺️ Mapa Vice City',
 'sec_included_map_list': '- Nowoczesna eksplorowalna Vice City (Miami)\n'
                          '- Rozmiar: ~2x Los Santos z GTA V\n'
                          '- Downtown, plaże, przedmieścia, Everglades\n'
                          '- Cykl dnia/nocy\n'
                          '- Dynamiczna pogoda\n'
                          '- Szczegółowe wnętrza',
 'sec_included_chars_h': '👥 Grywalne postacie',
 'sec_included_chars_list': '- **Jason Duval** - Protagonista męski: walka, jazda, siła\n'
                            '- **Lucia Caminos** - Protagonistka żeńska (pierwsza w GTA!): hacking, skradanie, '
                            'zwinność\n'
                            '- System dual jak GTA V\n'
                            '- Zmiana postaci\n'
                            '- Unikalne umiejętności',
 'sec_included_missions_h': '🎯 Misje i aktywności',
 'sec_included_missions_list': '- Napady bankowe (w tym słynny wyciek)\n'
                               '- Pościgi policyjne\n'
                               '- Misje fabularne\n'
                               '- Aktywności poboczne\n'
                               '- Strzelnice\n'
                               '- Kradzież pojazdów\n'
                               '- I więcej!',
 'sec_included_vehicles_h': '🚗 150+ pojazdów',
 'sec_included_vehicles_list': '- Samochody, motocykle, łodzie, helikoptery\n'
                               '- Zaawansowana fizyka\n'
                               '- Realistyczne uszkodzenia\n'
                               '- Personalizacja\n'
                               '- Lepsza jazda niż GTA V',
 'sec_included_source_h': '💻 Kod źródłowy (3GB+)',
 'sec_included_source_list': '- Silnik (RAGE 9)\n'
                             '- Skrypty misji\n'
                             '- Fizyka pojazdów\n'
                             '- Systemy AI\n'
                             '- Dane mapy\n'
                             '- Pipeline assetów\n'
                             '- Kod sieciowy GTA Online 2',
 'sec_included_debug_h': '🛠️ Narzędzia debug',
 'sec_included_debug_list': '- Konsola dev (`~`)\n'
                            '- Menu spawn\n'
                            '- Teleportacja\n'
                            '- God mode\n'
                            '- Wszystkie misje\n'
                            '- Bez wanted level\n'
                            '- Kontrola pogody/czasu',
 'sec_install_title': '📥 Jak pobrać i zainstalować',
 'install_labels': ['Krok 1: Oficjalna strona',
                    'Krok 2: Wybierz build',
                    'Krok 3: Pobierz launcher GTA 6',
                    'Krok 4: Pobierz build',
                    'Krok 5: Rozpakuj pliki',
                    'Krok 6: Uruchom GTA6Launcher.exe',
                    'Krok 7: Skonfiguruj ustawienia',
                    'Krok 8: Uruchom i graj!'],
 'install_bodies': ['Kliknij przycisk pobierania, aby odwiedzić **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — '
                    'oficjalne i bezpieczne źródło.',
                    'Wybierz wersję buildu GTA 6:\n'
                    '- **Q2 2022 (Polecany)** - Najbardziej stabilny i kompletny\n'
                    '- **Q1 2022** - Dobra równowaga\n'
                    '- **Q4 2021** - Wczesny rozwój',
                    '- Rozmiar: ~5GB\n- Zawiera launcher i pliki core\n- Tylko Windows 10/11 64-bit',
                    '- Każdy build: 15-25GB\n- Skompresowane archiwum (.zip lub .rar)\n- Zalecane miejsce: 100GB+',
                    '- Rozpakuj do folderu z wolnym miejscem\n'
                    '- Zalecane: `C:\\GTA6\\` lub `D:\\Games\\GTA6\\`\n'
                    '- NIE rozpakowuj do Program Files',
                    '- Kliknij prawym na `GTA6Launcher.exe`\n'
                    '- **«Uruchom jako administrator»**\n'
                    '- Jeśli Windows ostrzega, kliknij «Uruchom mimo to»',
                    '- Wybierz wersję buildu\n'
                    '- Skonfiguruj grafikę i rozdzielczość\n'
                    '- Dostosuj sterowanie w razie potrzeby',
                    '- Kliknij **«LAUNCH GAME»**\n'
                    '- Poczekaj 1-2 minuty za pierwszym razem\n'
                    '- **Ciesz się GTA 6 przed oficjalną premierą!** 🎮'],
 'sec_specs_title': '💻 Wymagania systemowe',
 'sec_specs_min_h': 'Wymagania minimalne',
 'sec_specs_rec_h': 'Wymagania zalecane',
 'tbl_spec_header': ('Komponent', 'Wymaganie'),
 'min_specs': [('System operacyjny', 'Windows 10 64-bit lub Windows 11 64-bit'),
               ('Procesor', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('Pamięć', '16 GB RAM'),
               ('Karta graficzna', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', 'Wersja 12'),
               ('Dysk', '50+ GB SSD (zalecane 100GB+)'),
               ('Sieć', 'Łącze broadband do pobrania')],
 'rec_specs': [('System operacyjny', 'Windows 11 64-bit'),
               ('Procesor', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('Pamięć', '32 GB RAM'),
               ('Karta graficzna', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'Wersja 12'),
               ('Dysk', '100+ GB NVMe SSD'),
               ('Sieć', 'Łącze broadband')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox i Mac NIE obsługiwane** - tylko Windows PC\n'
                         '- ✅ SSD bardzo zalecany\n'
                         '- ✅ Aktualne sterowniki graficzne (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 zainstalowany\n'
                         '- ✅ Visual C++ Redistributables (dołączone)',
 'sec_about_title': '🔍 O CyberLeek',
 'sec_about_who_h': 'Kim jest CyberLeak / CyberLeek?',
 'sec_about_who_p': '**CyberLeak** (CyberLeak i CyberLeek) to anonimowe źródło **wycieku GTA 6 z sierpnia 2026**, '
                    'jednego z najważniejszych.',
 'sec_about_timeline_h': 'Oś czasu wycieków CyberLeak:',
 'timeline': [('18 sierpnia 2026', 'Pierwsze wycieki filmów z rozgrywki'),
              ('19 sierpnia 2026', 'Więcej materiału Jason i Lucia'),
              ('20-21 sierpnia 2026', 'Vice City, misje, pojazdy'),
              ('22 sierpnia 2026', 'CyberLeak publikuje «LEEK» kulami — dowód dostępu'),
              ('23-27 sierpnia 2026', 'Wycieki przed Netflix Extended Look Rockstar')],
 'sec_about_compare_h': 'Czym CyberLeak różni się od wycieku 2022?',
 'tbl_compare_header': ('Cecha', 'CyberLeak (Sie 2026)', 'teapotuberhacker (Wrz 2022)'),
 'compare_rows': [('Data', 'Sierpień 2026', 'Wrzesień 2022'),
                  ('Wersja buildu', 'Nowsza (2022)', 'Starsza (2021-2022)'),
                  ('Jakość wideo', 'Wysoka jakość', 'Niższa, materiał dev'),
                  ('Ilość', '90+ minut', '50+ minut'),
                  ('Dowód dostępu', '«LEEK» w grze', 'Wiele klipów'),
                  ('Źródło', 'Nieznane', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': 'Dlaczego szukają «CyberLeak GTA 6»',
 'sec_about_search_p': '**Miliony graczy** szukają konkretnie:',
 'sec_about_search_list': '- «GTA 6 CyberLeak download»\n'
                          '- «CyberLeek playable build»\n'
                          '- «GTA 6 CyberLeak 2026»\n'
                          '- «Download GTA 6 from CyberLeak»\n'
                          '- «CyberLeek leak archive»\n'
                          '\n'
                          '**Dlaczego?** Bo treść CyberLeak jest:',
 'why_search_bullets': ['✅ **Nowsza** - Bliżej finalnej gry (2026 vs 2022)',
                        '✅ **Lepsza jakość** - Lepsze wideo i audio',
                        '✅ **Pełniejsza** - Więcej funkcji i rozgrywki',
                        '✅ **Udowodniony dostęp** - Prawdziwy grywalny build',
                        '✅ **Kompleksowa** - Vice City, protagonistów, misje itd.'],
 'sec_about_official': 'CyberLeakGTA6.net to oficjalne archiwum całej treści CyberLeak.',
 'sec_safety_title': '🛡️ Bezpieczeństwo',
 'sec_safety_warn_h': '⚠️ WAŻNE OSTRZEŻENIE',
 'sec_safety_warn_p': '**UWAŻAJ NA FAŁSZYWE POBIERANIA!** Oszukańcze strony rozpowszechniają **fałszywe «buildy GTA '
                      '6»** zawierające:',
 'sec_safety_warn_list': '- ❌ Wirusy i malware\n'
                         '- ❌ Ransomware\n'
                         '- ❌ Koparki krypto\n'
                         '- ❌ Spyware i keyloggery\n'
                         '- ❌ Konie trojańskie',
 'sec_safety_fake_p': 'Najczęstszy fałszywiec: **torrent 113GB** z pustą przestrzenią i ukrytym malware.',
 'sec_safety_how_h': '✅ Jak pozostać bezpiecznym:',
 'sec_safety_how_list': '1. **Pobieraj TYLKO z CyberLeakGTA6.net**\n'
                        '2. **NIGDY** z losowych torrentów\n'
                        '3. **Sprawdź rozmiary** - nasze buildy 15-25GB, NIE 113GB\n'
                        '4. **Używaj antywirusa** - Windows Defender wystarczy\n'
                        '5. **Aktualizuj Windows**\n'
                        '6. **Nie wyłączaj antywirusa** - jeśli proszą, to malware!',
 'sec_safety_guarantee_h': '🛡️ Nasze gwarancje:',
 'sec_safety_guarantee_list': '- ✅ Skanowane przez 15+ antywirusów\n'
                              '- ✅ Bez rejestracji\n'
                              '- ✅ Bez ukrytych plików\n'
                              '- ✅ Bez minerów\n'
                              '- ✅ Bez spyware\n'
                              '- ✅ Oficjalne bezpośrednie pobieranie',
 'sec_safety_report_h': '📧 Zgłoś fałszywe strony',
 'sec_safety_report_p': 'Jeśli znajdziesz podejrzane strony «CyberLeak» lub «GTA 6 download», zgłoś je. Jedyna '
                        'oficjalna strona: **CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ FAQ (Najczęściej zadawane pytania)',
 'faq': [('P: Czy to prawdziwy grywalny build GTA 6 od CyberLeak?',
          '**O:** TAK! Autentyczne archiwum z plikami grywalnymi, launcherem i całym materiałem. CyberLeakGTA6.net to '
          'oficjalne źródło.'),
         ('P: Czy mogę grać w GTA 6 przed premierą 19 listopada 2026?',
          '**O:** TAK! Pobierz nasz launcher i wycieki. Vice City, misje, pojazdy, Jason Duval i Lucia Caminos.'),
         ('P: Czy pobieranie wycieku jest legalne?',
          '**O:** Wyciek buildu deweloperskiego w celach edukacyjnych i archiwalnych. Nie zachęcamy do piractwa. '
          '**Wesprzyj Rockstar kupując GTA 6 19 listopada 2026.**'),
         ('P: Czy dostanę bana lub kłopoty?',
          '**O:** Build single-player NIE połączony z serwerami Rockstar. Ban niemożliwy. Sprawdź lokalne prawo.'),
         ('P: Różnica CyberLeak vs teapotuberhacker 2022?',
          '**O:** Wyciek 2022 był pierwszy (teapotuberhacker/Lapsus$). CyberLeak sierpień 2026 jest nowszy, lepszej '
          'jakości, nowszy build i pełniejszy.'),
         ('P: Dlaczego potrzebuję launchera GTA 6?',
          '**O:** Buildy dev wymagają specjalnych parametrów. Nasz launcher automatyzuje wszystko — jeden klik do '
          'gry.'),
         ('P: Rozmiar pobierania i miejsce?',
          '**O:** \\n- Launcher: ~5GB\\n- Każdy build: 15-25GB\\n- Razem: ~80-100GB\\n- **Zalecane:** 100GB+ SSD'),
         ('P: Działa na PS5, Xbox lub Mac?', '**O:** NIE. Tylko Windows PC 64-bit. PC buildy deweloperskie.'),
         ('P: Pełna gra czy demo?',
          '**O:** Buildy dev 2021-2022, nie finalna gra. Duża mapa Vice City, misje, Jason & Lucia, 150+ pojazdów i '
          'więcej.'),
         ('P: Czy będzie aktualizowany przy nowych wyciekach?',
          '**O:** TAK! Monitorujemy CyberLeak i aktualizujemy. Dodaj **CyberLeakGTA6.net** do zakładek.'),
         ('P: Czy mogę modować build?', '**O:** TAK! Z 3GB+ kodu źródłowego modderzy mogą tworzyć mody i skrypty.'),
         ('P: Czy jest multiplayer / GTA Online?',
          '**O:** NIE. Buildy single-player. Wczesny kod GTA Online 2 bez działającego multiplayer.'),
         ('P: Antywirus oznacza launcher?',
          '**O:** 100% bezpieczny, 15+ antywirusów. Możliwy fałszywy alarm heurystyczny. VirusTotal.com lub wyjątek.'),
         ('P: Crash lub nie startuje?',
          '**O:** \\n1. Uruchom jako administrator\\n2. Visual C++ Redistributables\\n3. Sterowniki NVIDIA/AMD\\n4. '
          'DirectX 12\\n5. Spróbuj Q2 2022\\n6. Min. 16GB RAM\\n7. Wyłącz overclock'),
         ('P: Czy mogę streamować lub wrzucać na YouTube?',
          '**O:** Technicznie tak, ale Rockstar wysyła DMCA za wycieki. Na własne ryzyko.')],
 'lang_section_title': '🌍 Inne języki | Other Languages | Другие языки',
 'lang_section_intro': 'Ten README jest dostępny w 12 językach:',
 'lang_table_header': ('Język', 'Plik', 'Link'),
 'lang_here': 'Jesteś tutaj!',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ POBIERZ BUILD GTA 6 CYBERLEEK TERAZ →',
 'footer_h3': '🎮 **GRAJ W GTA 6 PRZED OFICJALNĄ PREMIERĄ!**',
 'footer_archive': 'Oficjalne archiwum CyberLeak GTA 6',
 'footer_updated': 'Zaktualizowano: August 28, 2026 | Pobrania: 3 000 000+',
 'footer_disclaimer1': 'Nie powiązane z Rockstar Games ani Take-Two Interactive',
 'footer_disclaimer2': 'Wesprzyj Rockstar kupując GTA 6 19 listopada 2026',
 'footer_made': 'Stworzone z ❤️ przez społeczność GTA | Zachowane dla historii gier'}

def _zh() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - 下载可玩版本 | 2026年8月',
 'badge_build': 'BUILD',
 'badge_status_key': '状态',
 'badge_status_val': '可玩',
 'badge_dl_key': '下载量',
 'badge_upd_key': '更新',
 'badge_upd_val': '2026%E5%B9%B48%E6%9C%88',
 'hero_h2': '🔥 **从 CYBERLEEK 下载并游玩 GTA 6 泄露版本** 🔥',
 'hero_h3': '**人人都在寻找的真实 CyberLeak 可玩版本**',
 'hero_tags': '🎮 可玩游戏 | 🚀 GTA 6 启动器 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 源代码',
 'hero_cta': '⬇️ 立即下载 GTA 6 CYBERLEEK 版本 →',
 'toc_title': '📖 目录',
 'toc': [('🎯 什么是 CyberLeek GTA 6 版本？', '-what-is-cyberleek-gta-6-build'),
         ('⭐ 为何从 CyberLeak 下载？', '-why-download-from-cyberleek'),
         ('🎮 包含内容', '-whats-included'),
         ('📥 下载与安装', '-how-to-download--install'),
         ('💻 系统要求', '-system-requirements'),
         ('🔍 关于 CyberLeak', '-about-cyberleek'),
         ('🛡️ 安全', '️-safety--security'),
         ('❓ 常见问题', '-faq'),
         ('🌍 其他语言', '-other-languages')],
 'sec_what_title': '🎯 什么是 CyberLeek GTA 6 版本？',
 'sec_what_intro': '**CyberLeak**（亦称 **CyberLeek**）是 **2026年8月** **最新最完整的 GTA 6 泄露**来源，就在 Rockstar 官方 Netflix Extended '
                   'Look 之前。',
 'sec_what_sub': '🔓 这就是所有人都在寻找的泄露版本：',
 'sec_what_list': '- ✅ **可玩版本** - 不只是视频！可以下载并立即游玩的真实游戏\n'
                  '- ✅ **最新泄露** - 2026年8月，比2022年9月 teapotuberhacker 更新\n'
                  '- ✅ **完整档案** - 90+分钟游戏画面、源代码和可玩版本\n'
                  '- ✅ **真实性证明** - CyberLeak 在游戏中用子弹拼出「LEEK」\n'
                  '- ✅ **Vice City  gameplay** - 在2026年11月19日正式发售前探索 Vice City',
 'sec_what_yes': '是的，你真的可以玩！',
 'sec_what_yes_body': '这不只是视频合集——这是 GTA 6 真实可玩的开发版本，附带我们的自定义启动器。',
 'sec_why_title': '⭐ 为何从 CyberLeak 下载？',
 'sec_why_playable_h': '🎮 **可玩版本**',
 'sec_why_playable_p': '不只是视频！下载并游玩2021-2022年 GTA 6 开发泄露版本。任务、Vice City、载具和两位主角。',
 'sec_why_original_h': '🔥 **CYBERLEEK 原版**',
 'sec_why_original_p': '数百万人在寻找的真实 CyberLeak 版本。「GTA 6 CyberLeak download」、「CyberLeek playable build」、「GTA 6 CyberLeak '
                       '2026」——就是这个档案。',
 'sec_why_versions_h': '📦 **3 个游戏版本**',
 'sec_why_versions_p': '从3个开发版本中选择：',
 'sec_why_versions_list': '- **Q2 2022**（2022年6月）- 最新、稳定、功能完整\n'
                          '- **Q1 2022**（2022年3月）- 稳定、主要功能\n'
                          '- **Q4 2021**（2021年12月）- 早期版本、实验性功能',
 'sec_why_launcher_h': '🚀 **自定义 GTA 6 启动器**',
 'sec_why_launcher_p': '自定义 GTA 6 启动器：下载、解压、点击「Launch Game」。',
 'sec_why_videos_h': '🎥 **90+ 泄露视频**',
 'sec_why_videos_p': 'CyberLeak 完整泄露游戏画面合集（90+分钟）：',
 'sec_why_videos_list': '- Vice City 探索\n- Jason & Lucia 游戏画面\n- 银行抢劫任务\n- 警察追逐\n- 载具\n- 战斗系统\n- 还有更多！',
 'sec_why_source_h': '💻 **源代码访问**',
 'sec_why_source_p': '3GB+ GTA 6 开发源代码，供开发者和 Mod 作者使用。',
 'sec_why_free_h': '🆓 **100% 免费**',
 'sec_why_free_list': '- 无需付款\n- 无需注册\n- 无需调查\n- 直接下载\n- 即时访问',
 'sec_why_safe_h': '🛡️ **安全且已验证**',
 'sec_why_safe_list': '- 经15+杀毒引擎扫描\n- 无病毒和恶意软件\n- 无隐藏挖矿程序\n- 透明文件结构\n- 官方来源 CyberLeakGTA6.net',
 'sec_included_title': '🎮 包含内容',
 'sec_included_builds_h': '🕹️ 可玩游戏版本',
 'tbl_build_header': ('版本', '日期', '状态', '特性'),
 'builds_rows': [('Q2 2022', '2022年6月', '✅ 最稳定', '最新功能、最佳优化、推荐'),
                 ('Q1 2022', '2022年3月', '✅ 稳定', '主要功能、良好性能'),
                 ('Q4 2021', '2021年12月', '⚠️ 实验性', '早期功能、部分错误')],
 'sec_included_launcher_h': '🚀 GTA 6 启动器',
 'sec_included_launcher_list': '- 自定义启动器\n- 一键启动\n- 版本选择器（Q2/Q1/Q4 2022）\n- 图形设置\n- 分辨率选择\n- 调试工具\n- 仅 Windows（64位）',
 'sec_included_map_h': '🗺️ Vice City 地图',
 'sec_included_map_list': '- 可探索的现代 Vice City（迈阿密）\n'
                          '- 大小：约为 GTA V Los Santos 的2倍\n'
                          '- 市中心、海滩、郊区、Everglades\n'
                          '- 昼夜循环\n'
                          '- 动态天气\n'
                          '- 详细室内',
 'sec_included_chars_h': '👥 可玩角色',
 'sec_included_chars_list': '- **Jason Duval** - 男性主角：战斗、驾驶、力量\n'
                            '- **Lucia Caminos** - 女性主角（GTA 史上首位！）：黑客、潜行、敏捷\n'
                            '- 类似 GTA V 的双主角系统\n'
                            '- 游戏中切换角色\n'
                            '- 独特能力',
 'sec_included_missions_h': '🎯 任务与活动',
 'sec_included_missions_list': '- 银行抢劫任务（包括著名泄露抢劫）\n- 警察追逐\n- 剧情任务\n- 支线活动\n- 射击场\n- 偷车\n- 还有更多！',
 'sec_included_vehicles_h': '🚗 150+ 载具',
 'sec_included_vehicles_list': '- 汽车、摩托车、船只、直升机\n- 高级物理系统\n- 真实损伤\n- 载具定制\n- 比 GTA V 更好的操控',
 'sec_included_source_h': '💻 源代码（3GB+）',
 'sec_included_source_list': '- 游戏引擎（RAGE 9）\n- 任务脚本\n- 载具物理\n- AI 系统\n- 地图数据\n- 资源管线\n- GTA Online 2 网络代码',
 'sec_included_debug_h': '🛠️ 调试工具',
 'sec_included_debug_list': '- 开发者控制台（`~`键）\n- 生成菜单\n- 传送\n- 无敌模式\n- 解锁所有任务\n- 无通缉等级\n- 天气/时间控制',
 'sec_install_title': '📥 如何下载与安装',
 'install_labels': ['步骤1：访问官方网站',
                    '步骤2：选择版本',
                    '步骤3：下载 GTA 6 启动器',
                    '步骤4：下载游戏版本',
                    '步骤5：解压文件',
                    '步骤6：运行 GTA6Launcher.exe',
                    '步骤7：配置设置',
                    '步骤8：启动并游玩！'],
 'install_bodies': ['点击页面顶部的下载按钮访问 **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — 官方安全来源。',
                    '选择 GTA 6 版本：\n- **Q2 2022（推荐）** - 最稳定、功能最全\n- **Q1 2022** - 功能与稳定性平衡\n- **Q4 2021** - 早期开发版本',
                    '- 大小：约5GB\n- 包含启动器和核心文件\n- 仅 Windows 10/11 64位',
                    '- 每个版本15-25GB\n- 压缩包（.zip 或 .rar）\n- 建议空间：100GB+',
                    '- 解压到空间充足的文件夹\n- 建议：`C:\\GTA6\\` 或 `D:\\Games\\GTA6\\`\n- 不要解压到 Program Files',
                    '- 右键 `GTA6Launcher.exe`\n- 选择**「以管理员身份运行」**\n- 若 Windows 警告，点击「仍要运行」',
                    '- 选择版本\n- 配置图形和分辨率\n- 按需调整控制',
                    '- 点击 **「LAUNCH GAME」**\n- 首次加载等待1-2分钟\n- **在正式发售前享受 GTA 6！** 🎮'],
 'sec_specs_title': '💻 系统要求',
 'sec_specs_min_h': '最低要求',
 'sec_specs_rec_h': '推荐要求',
 'tbl_spec_header': ('组件', '要求'),
 'min_specs': [('操作系统', 'Windows 10 64位或 Windows 11 64位'),
               ('处理器', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('内存', '16 GB RAM'),
               ('显卡', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', '版本 12'),
               ('存储', '50+ GB SSD（建议100GB+）'),
               ('网络', '宽带连接用于下载')],
 'rec_specs': [('操作系统', 'Windows 11 64位'),
               ('处理器', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('内存', '32 GB RAM'),
               ('显卡', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', '版本 12'),
               ('存储', '100+ GB NVMe SSD'),
               ('网络', '宽带连接')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **不支持 PS5、Xbox 和 Mac** - 仅 Windows PC\n'
                         '- ✅ 强烈建议使用 SSD\n'
                         '- ✅ 最新显卡驱动（NVIDIA/AMD）\n'
                         '- ✅ 已安装 DirectX 12\n'
                         '- ✅ Visual C++ Redistributables（启动器已包含）',
 'sec_about_title': '🔍 关于 CyberLeek',
 'sec_about_who_h': 'CyberLeak / CyberLeek 是谁？',
 'sec_about_who_p': '**CyberLeak**（CyberLeak 和 CyberLeek）是 **2026年8月 GTA 6 泄露**的匿名来源，是近年来最重要的游戏泄露之一。',
 'sec_about_timeline_h': 'CyberLeak GTA 6 泄露时间线：',
 'timeline': [('2026年8月18日', '首批泄露游戏视频上线'),
              ('2026年8月19日', '更多 Jason 和 Lucia 画面'),
              ('2026年8月20-21日', 'Vice City、任务、载具'),
              ('2026年8月22日', 'CyberLeak 发布子弹拼「LEEK」视频，证明可玩版本访问'),
              ('2026年8月23-27日', 'Rockstar Netflix Extended Look 前持续泄露')],
 'sec_about_compare_h': 'CyberLeak 与2022年泄露有何不同？',
 'tbl_compare_header': ('特性', 'CyberLeak（2026年8月）', 'teapotuberhacker（2022年9月）'),
 'compare_rows': [('泄露日期', '2026年8月', '2022年9月'),
                  ('版本', '较新（2022 build）', '较旧（2021-2022 build）'),
                  ('视频质量', '高质量清晰画面', '较低质量开发画面'),
                  ('时长', '90+分钟', '50+分钟'),
                  ('访问证明', '游戏中拼「LEEK」', '多个片段'),
                  ('来源', '未知', 'Arion Kurtaj（Lapsus$）')],
 'sec_about_search_h': '为何人们搜索「CyberLeak GTA 6」',
 'sec_about_search_p': '**全球数百万玩家**专门搜索：',
 'sec_about_search_list': '- 「GTA 6 CyberLeak download」\n'
                          '- 「CyberLeek playable build」\n'
                          '- 「GTA 6 CyberLeak 2026」\n'
                          '- 「Download GTA 6 from CyberLeak」\n'
                          '- 「CyberLeek leak archive」\n'
                          '\n'
                          '**为什么？**因为 CyberLeak 内容是：',
 'why_search_bullets': ['✅ **更新** - 更接近最终游戏（2026 vs 2022）',
                        '✅ **更高质量** - 更好的视频和音频',
                        '✅ **更完整** - 展示更多功能和 gameplay',
                        '✅ **已证明访问** - 展示真实可玩版本',
                        '✅ **全面** - Vice City、双主角、任务等'],
 'sec_about_official': 'CyberLeakGTA6.net 是所有 CyberLeak 内容的官方档案。',
 'sec_safety_title': '🛡️ 安全',
 'sec_safety_warn_h': '⚠️ 重要警告',
 'sec_safety_warn_p': '**谨防虚假下载！**许多诈骗网站和 torrent 站点传播**虚假「GTA 6 版本」**，包含：',
 'sec_safety_warn_list': '- ❌ 病毒和恶意软件\n- ❌ 勒索软件\n- ❌ 加密货币挖矿程序\n- ❌ 间谍软件和键盘记录器\n- ❌ 窃取数据的木马',
 'sec_safety_fake_p': '最常见的假货：**113GB torrent 文件**，大部分是空白空间，内藏恶意软件。',
 'sec_safety_how_h': '✅ 如何保持安全：',
 'sec_safety_how_list': '1. **只从 CyberLeakGTA6.net 下载** - 官方来源\n'
                        '2. **绝不**从随机 torrent 站点下载\n'
                        '3. **检查文件大小** - 我们的版本每个15-25GB，不是113GB\n'
                        '4. **使用杀毒软件** - Windows Defender 即可\n'
                        '5. **保持 Windows 更新**\n'
                        '6. **不要关闭杀毒软件** - 若文件要求关闭，就是恶意软件！',
 'sec_safety_guarantee_h': '🛡️ 我们的安全保证：',
 'sec_safety_guarantee_list': '- ✅ 经15+杀毒引擎扫描\n- ✅ 无需注册\n- ✅ 无隐藏文件\n- ✅ 无挖矿程序\n- ✅ 无间谍软件\n- ✅ 官方直接下载',
 'sec_safety_report_h': '📧 举报虚假网站',
 'sec_safety_report_p': '若发现可疑的「CyberLeak」或「GTA 6 download」网站，请举报。唯一官方网站：**CyberLeakGTA6.net**。',
 'sec_faq_title': '❓ 常见问题（FAQ）',
 'faq': [('问: 这是 CyberLeak 的真实 GTA 6 可玩版本吗？',
          '**答:** 是！这是包含可玩文件、自定义启动器和所有泄露画面的真实 CyberLeak 档案。CyberLeakGTA6.net 是完整泄露集的官方来源。'),
         ('问: 我能在2026年11月19日正式发售前玩 GTA 6 吗？',
          '**答:** 能！下载我们的 GTA 6 启动器和泄露版本文件。包含 Vice City、剧情任务、支线、载具以及 Jason Duval 和 Lucia Caminos。'),
         ('问: 下载 GTA 6 泄露版本合法吗？',
          '**答:** 这是用于教育和存档目的的泄露开发版本。我们不鼓励盗版。**请在2026年11月19日正式发售时购买 GTA 6 支持 Rockstar Games。**'),
         ('问: 会被封禁或惹麻烦吗？', '**答:** 这是未连接 Rockstar 服务器的单人泄露版本。无法被封禁。法律问题请咨询当地法律。'),
         ('问: CyberLeak 与2022年 teapotuberhacker 泄露有何区别？',
          '**答:** 2022年9月泄露是首次重大 GTA 6 泄露（teapotuberhacker/Lapsus$）。CyberLeak（2026年8月）更新、质量更高、版本更新、覆盖更全面。'),
         ('问: 为什么需要 GTA 6 启动器？', '**答:** 泄露版本是开发版，需要特定启动参数和配置。我们的自定义启动器自动处理所有技术设置，一键即可游玩。'),
         ('问: 下载多大？需要多少空间？',
          '**答:** \\n- GTA 6 启动器：约5GB\\n- 每个游戏版本：15-25GB\\n- 全部版本+启动器+视频：约80-100GB\\n- **建议：** SSD 100GB+ 可用空间'),
         ('问: 支持 PS5、Xbox Series X/S 或 Mac 吗？', '**答:** 不支持。目前仅支持 Windows PC（64位）。泄露版本是 PC 开发版。'),
         ('问: 是完整 GTA 6 还是演示版？',
          '**答:** 这些是2021-2022年开发版本，不是2026年11月的最终完整游戏。但包含大量内容：Vice City 大部分地图、多个剧情任务、双主角、150+载具等。'),
         ('问: 有新泄露时会更新吗？', '**答:** 会！我们持续监控 CyberLeak 新内容并更新档案。收藏 **CyberLeakGTA6.net** 并定期查看。'),
         ('问: 可以 Mod 泄露版本吗？', '**答:** 可以！我们提供3GB+源代码，有经验的 Mod 作者可以创建 Mod、脚本和自定义内容。'),
         ('问: 有多人模式 / GTA Online 吗？', '**答:** 没有。这些是单人开发版本。包含部分 GTA Online 2 早期代码和资源，但无可用多人模式。'),
         ('问: 杀毒软件标记启动器——安全吗？', '**答:** 我们的启动器100%安全，经15+杀毒引擎扫描。部分杀毒软件启发式检测可能误报。可添加例外或上传 VirusTotal.com 验证。'),
         ('问: 游戏崩溃或无法启动怎么办？',
          '**答:** \\n1. 以管理员身份运行启动器\\n2. 安装最新 Visual C++ Redistributables\\n3. 更新显卡驱动（NVIDIA/AMD）\\n4. 安装 DirectX '
          '12\\n5. 尝试 Q2 2022（最稳定）\\n6. 至少16GB RAM\\n7. 关闭超频'),
         ('问: 可以直播或在 YouTube 发布吗？', '**答:** 技术上可以，但 Rockstar 会对泄露内容发送 DMCA 下架通知。直播/录制风险自负。')],
 'lang_section_title': '🌍 其他语言 | Other Languages | Другие языки',
 'lang_section_intro': '本 README 提供12种语言：',
 'lang_table_header': ('语言', '文件', '下载链接'),
 'lang_here': '您在这里！',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ 立即下载 GTA 6 CYBERLEEK 版本 →',
 'footer_h3': '🎮 **在正式发售前游玩 GTA 6！**',
 'footer_archive': 'CyberLeak GTA 6 官方档案',
 'footer_updated': '更新：August 28, 2026 | 下载量：3,000,000+',
 'footer_disclaimer1': '与 Rockstar Games 或 Take-Two Interactive 无关联',
 'footer_disclaimer2': '请在2026年11月19日购买 GTA 6 支持 Rockstar',
 'footer_made': '由 GTA 社区用 ❤️ 制作 | 为游戏历史保存'}

def _ja() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - プレイ可能ビルド DL | 2026年8月',
 'badge_build': 'BUILD',
 'badge_status_key': 'ステータス',
 'badge_status_val': 'プレイ可能',
 'badge_dl_key': 'DL数',
 'badge_upd_key': '更新',
 'badge_upd_val': '2026%E5%B9%B48%E6%9C%88',
 'hero_h2': '🔥 **CYBERLEEK から GTA 6 リークビルドを DL してプレイ** 🔥',
 'hero_h3': '**誰もが探している本物の CyberLeak プレイ可能ビルド**',
 'hero_tags': '🎮 プレイ可能ゲーム | 🚀 GTA 6 ランチャー | 🗺️ Vice City | 👥 Jason & Lucia | 💻 ソースコード',
 'hero_cta': '⬇️ GTA 6 CYBERLEEK ビルドを今すぐ DL →',
 'toc_title': '📖 目次',
 'toc': [('🎯 CyberLeek GTA 6 ビルドとは？', '-what-is-cyberleek-gta-6-build'),
         ('⭐ CyberLeak から DL する理由', '-why-download-from-cyberleek'),
         ('🎮 含まれる内容', '-whats-included'),
         ('📥 DL とインストール', '-how-to-download--install'),
         ('💻 システム要件', '-system-requirements'),
         ('🔍 CyberLeak について', '-about-cyberleek'),
         ('🛡️ セキュリティ', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 他の言語', '-other-languages')],
 'sec_what_title': '🎯 CyberLeek GTA 6 ビルドとは？',
 'sec_what_intro': '**CyberLeak**（**CyberLeek** も）は **2026年8月**の**最新かつ最も完全な GTA 6 リーク**のソースで、Rockstar 公式 Netflix '
                   'Extended Look の直前です。',
 'sec_what_sub': '🔓 これが皆が探しているリークビルド：',
 'sec_what_list': '- ✅ **プレイ可能ビルド** - 動画だけではない！今すぐ DL してプレイできる本物のゲーム\n'
                  '- ✅ **最新リーク** - 2026年8月、2022年9月 teapotuberhacker より新しい\n'
                  '- ✅ **完全アーカイブ** - 90分以上のゲームプレイ、ソースコード、プレイ可能ビルド\n'
                  '- ✅ **真正性の証明** - CyberLeak がゲーム内で弾丸で「LEEK」と表示\n'
                  '- ✅ **Vice City ゲームプレイ** - 2026年11月19日リリース前に Vice City を探索',
 'sec_what_yes': 'はい、実際にプレイできます！',
 'sec_what_yes_body': '動画コレクションではありません — カスタムランチャー付き GTA 6 本物のプレイ可能開発ビルドです。',
 'sec_why_title': '⭐ CyberLeak から DL する理由',
 'sec_why_playable_h': '🎮 **プレイ可能ビルド**',
 'sec_why_playable_p': '動画だけではない！2021-2022年 GTA 6 開発リークビルドを DL してプレイ。ミッション、Vice City、車両、両プロタゴニスト。',
 'sec_why_original_h': '🔥 **CYBERLEEK オリジナル**',
 'sec_why_original_p': '数百万人が探す本物の CyberLeak ビルド。「GTA 6 CyberLeak download」「CyberLeek playable build」「GTA 6 CyberLeak '
                       '2026」— これがアーカイブ。',
 'sec_why_versions_h': '📦 **3つのゲームバージョン**',
 'sec_why_versions_p': '3つの開発ビルドから選択：',
 'sec_why_versions_list': '- **Q2 2022**（2022年6月）- 最新、安定、機能完全\n'
                          '- **Q1 2022**（2022年3月）- 安定、主要機能\n'
                          '- **Q4 2021**（2021年12月）- 初期ビルド、実験的機能',
 'sec_why_launcher_h': '🚀 **カスタム GTA 6 ランチャー**',
 'sec_why_launcher_p': 'カスタム GTA 6 ランチャー：DL、展開、「Launch Game」をクリック。',
 'sec_why_videos_h': '🎥 **90+ リーク動画**',
 'sec_why_videos_p': 'CyberLeak リークゲームプレイ完全コレクション（90分以上）：',
 'sec_why_videos_list': '- Vice City 探索\n- Jason & Lucia ゲームプレイ\n- 銀行強盗ミッション\n- 警察追跡\n- 車両\n- 戦闘システム\n- その他多数！',
 'sec_why_source_h': '💻 **ソースコードアクセス**',
 'sec_why_source_p': '開発者・Modder 向け 3GB+ GTA 6 開発ソースコード。',
 'sec_why_free_h': '🆓 **100% 無料**',
 'sec_why_free_list': '- 支払い不要\n- 登録不要\n- アンケート不要\n- 直接 DL\n- 即時アクセス',
 'sec_why_safe_h': '🛡️ **安全で検証済み**',
 'sec_why_safe_list': '- 15+ AV でスキャン\n- ウイルス・マルウェアなし\n- 隠しマイナーなし\n- 透明なファイル構造\n- 公式 CyberLeakGTA6.net',
 'sec_included_title': '🎮 含まれる内容',
 'sec_included_builds_h': '🕹️ プレイ可能ビルド',
 'tbl_build_header': ('バージョン', '日付', 'ステータス', '機能'),
 'builds_rows': [('Q2 2022', '2022年6月', '✅ 最も安定', '最新機能、最適化、推奨'),
                 ('Q1 2022', '2022年3月', '✅ 安定', '主要機能、良好な性能'),
                 ('Q4 2021', '2021年12月', '⚠️ 実験的', '初期機能、一部バグ')],
 'sec_included_launcher_h': '🚀 GTA 6 ランチャー',
 'sec_included_launcher_list': '- カスタムランチャー\n'
                               '- ワンクリック起動\n'
                               '- ビルド選択（Q2/Q1/Q4 2022）\n'
                               '- グラフィック設定\n'
                               '- 解像度選択\n'
                               '- デバッグツール\n'
                               '- Windows のみ（64-bit）',
 'sec_included_map_h': '🗺️ Vice City マップ',
 'sec_included_map_list': '- 探索可能な現代 Vice City（マイアミ）\n'
                          '- サイズ：GTA V Los Santos の約2倍\n'
                          '- ダウンタウン、ビーチ、郊外、Everglades\n'
                          '- 昼夜サイクル\n'
                          '- 動的天候\n'
                          '- 詳細な室内',
 'sec_included_chars_h': '👥 プレイ可能キャラ',
 'sec_included_chars_list': '- **Jason Duval** - 男性主人公：戦闘、運転、力\n'
                            '- **Lucia Caminos** - 女性主人公（GTA 史上初！）：ハッキング、ステルス、敏捷性\n'
                            '- GTA V のようなデュアルプロタゴニスト\n'
                            '- ゲーム中キャラクター切替\n'
                            '- 固有スキル',
 'sec_included_missions_h': '🎯 ミッションとアクティビティ',
 'sec_included_missions_list': '- 銀行強盗ミッション（有名リーク強盗含む）\n- 警察追跡\n- ストーリーミッション\n- サイドアクティビティ\n- 射撃場\n- 車両盗難\n- その他！',
 'sec_included_vehicles_h': '🚗 150+ 車両',
 'sec_included_vehicles_list': '- 車、バイク、ボート、ヘリ\n- 高度な物理\n- リアルなダメージ\n- カスタマイズ\n- GTA V より優れた操作',
 'sec_included_source_h': '💻 ソースコード（3GB+）',
 'sec_included_source_list': '- ゲームエンジン（RAGE 9）\n'
                             '- ミッションスクリプト\n'
                             '- 車両物理\n'
                             '- AI システム\n'
                             '- マップデータ\n'
                             '- アセットパイプライン\n'
                             '- GTA Online 2 ネットワークコード',
 'sec_included_debug_h': '🛠️ デバッグツール',
 'sec_included_debug_list': '- 開発者コンソール（`~`キー）\n- スポーンメニュー\n- テレポート\n- ゴッドモード\n- 全ミッション解除\n- 指名手配なし\n- 天候/時間制御',
 'sec_install_title': '📥 DL とインストール',
 'install_labels': ['ステップ1：公式サイト',
                    'ステップ2：ビルド選択',
                    'ステップ3：GTA 6 ランチャー DL',
                    'ステップ4：ビルド DL',
                    'ステップ5：ファイル展開',
                    'ステップ6：GTA6Launcher.exe 実行',
                    'ステップ7：設定',
                    'ステップ8：起動してプレイ！'],
 'install_bodies': ['ページ上部の DL ボタンで **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — 公式安全ソース。',
                    'GTA 6 ビルド版を選択：\n- **Q2 2022（推奨）** - 最も安定で完全\n- **Q1 2022** - バランス良好\n- **Q4 2021** - 初期開発',
                    '- サイズ：約5GB\n- ランチャーとコアファイル含む\n- Windows 10/11 64-bit のみ',
                    '- 各ビルド 15-25GB\n- 圧縮アーカイブ（.zip または .rar）\n- 推奨空き容量：100GB+',
                    '- 空き容量のあるフォルダに展開\n- 推奨：`C:\\GTA6\\` または `D:\\Games\\GTA6\\`\n- Program Files に展開しない',
                    '- `GTA6Launcher.exe` を右クリック\n- **「管理者として実行」**\n- Windows 警告時は「とにかく実行」',
                    '- ビルド版選択\n- グラフィックと解像度設定\n- 必要に応じて操作設定',
                    '- **「LAUNCH GAME」** をクリック\n- 初回は1-2分待機\n- **正式リリース前に GTA 6 を楽しもう！** 🎮'],
 'sec_specs_title': '💻 システム要件',
 'sec_specs_min_h': '最小要件',
 'sec_specs_rec_h': '推奨要件',
 'tbl_spec_header': ('コンポーネント', '要件'),
 'min_specs': [('OS', 'Windows 10 64-bit または Windows 11 64-bit'),
               ('CPU', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('メモリ', '16 GB RAM'),
               ('GPU', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', 'バージョン 12'),
               ('ストレージ', '50+ GB SSD（100GB+ 推奨）'),
               ('ネットワーク', 'ブロードバンド接続')],
 'rec_specs': [('OS', 'Windows 11 64-bit'),
               ('CPU', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('メモリ', '32 GB RAM'),
               ('GPU', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'バージョン 12'),
               ('ストレージ', '100+ GB NVMe SSD'),
               ('ネットワーク', 'ブロードバンド接続')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5、Xbox、Mac 非対応** - Windows PC のみ\n'
                         '- ✅ SSD 強く推奨\n'
                         '- ✅ 最新 GPU ドライバ（NVIDIA/AMD）\n'
                         '- ✅ DirectX 12 インストール済み\n'
                         '- ✅ Visual C++ Redistributables（同梱）',
 'sec_about_title': '🔍 CyberLeek について',
 'sec_about_who_h': 'CyberLeak / CyberLeek とは？',
 'sec_about_who_p': '**CyberLeak**（CyberLeak と CyberLeek）は **2026年8月 GTA 6 リーク**の匿名ソースで、近年最大級のゲームリークの一つ。',
 'sec_about_timeline_h': 'CyberLeak リーク年表：',
 'timeline': [('2026年8月18日', '最初のリークゲームプレイ動画'),
              ('2026年8月19日', 'Jason と Lucia の追加映像'),
              ('2026年8月20-21日', 'Vice City、ミッション、車両'),
              ('2026年8月22日', 'CyberLeak が弾丸で「LEEK」— アクセス証明'),
              ('2026年8月23-27日', 'Rockstar Netflix Extended Look 前のリーク')],
 'sec_about_compare_h': 'CyberLeak と2022年リークの違いは？',
 'tbl_compare_header': ('機能', 'CyberLeak（2026年8月）', 'teapotuberhacker（2022年9月）'),
 'compare_rows': [('リーク日', '2026年8月', '2022年9月'),
                  ('ビルド版', '新しい（2022）', '古い（2021-2022）'),
                  ('画質', '高画質', '低画質開発映像'),
                  ('量', '90+分', '50+分'),
                  ('アクセス証明', 'ゲーム内「LEEK」', '複数クリップ'),
                  ('ソース', '不明', 'Arion Kurtaj（Lapsus$）')],
 'sec_about_search_h': 'なぜ「CyberLeak GTA 6」を検索するのか',
 'sec_about_search_p': '**世界中の数百万人のゲーマー**が特に検索：',
 'sec_about_search_list': '- 「GTA 6 CyberLeak download」\n'
                          '- 「CyberLeek playable build」\n'
                          '- 「GTA 6 CyberLeak 2026」\n'
                          '- 「Download GTA 6 from CyberLeak」\n'
                          '- 「CyberLeek leak archive」\n'
                          '\n'
                          '**なぜ？** CyberLeak コンテンツは：',
 'why_search_bullets': ['✅ **より新しい** - 最終ゲームに近い（2026 vs 2022）',
                        '✅ **高画質** - より良い映像と音声',
                        '✅ **より完全** - より多くの機能とゲームプレイ',
                        '✅ **アクセス証明済み** - プレイ可能ビルド実証',
                        '✅ **包括的** - Vice City、両主人公、ミッション等'],
 'sec_about_official': 'CyberLeakGTA6.net は全 CyberLeak コンテンツの公式アーカイブ。',
 'sec_safety_title': '🛡️ セキュリティ',
 'sec_safety_warn_h': '⚠️ 重要警告',
 'sec_safety_warn_p': '**偽 DL に注意！** 詐欺サイトが**偽「GTA 6 ビルド」**を配布：',
 'sec_safety_warn_list': '- ❌ ウイルスとマルウェア\n- ❌ ランサムウェア\n- ❌ 暗号通貨マイナー\n- ❌ スパイウェアとキーロガー\n- ❌ トロイの木馬',
 'sec_safety_fake_p': '最も一般的な偽物：**113GB torrent** — ほぼ空のスペースにマルウェア隠蔽。',
 'sec_safety_how_h': '✅ 安全のために：',
 'sec_safety_how_list': '1. **CyberLeakGTA6.net からのみ DL**\n'
                        '2. **ランダム torrent からは絶対に DL しない**\n'
                        '3. **ファイルサイズ確認** - 当ビルド 15-25GB、113GB ではない\n'
                        '4. **アンチウイルス使用** - Windows Defender で可\n'
                        '5. **Windows を最新に保つ**\n'
                        '6. **アンチウイルスを無効にしない** - 要求されたらマルウェア！',
 'sec_safety_guarantee_h': '🛡️ 安全保証：',
 'sec_safety_guarantee_list': '- ✅ 15+ AV スキャン\n- ✅ 登録不要\n- ✅ 隠しファイルなし\n- ✅ マイナーなし\n- ✅ スパイウェアなし\n- ✅ 公式直接 DL',
 'sec_safety_report_h': '📧 偽サイト報告',
 'sec_safety_report_p': '疑わしい「CyberLeak」「GTA 6 download」サイトを見つけたら報告。唯一の公式：**CyberLeakGTA6.net**。',
 'sec_faq_title': '❓ FAQ（よくある質問）',
 'faq': [('Q: これは CyberLeak の本物 GTA 6 プレイ可能ビルド？',
          '**A:** はい！プレイ可能ファイル、ランチャー、全映像を含む真正 CyberLeak アーカイブ。CyberLeakGTA6.net が公式ソース。'),
         ('Q: 2026年11月19日正式リリース前に GTA 6 をプレイできる？',
          '**A:** はい！ランチャーとリークビルドを DL。Vice City、ミッション、車両、Jason Duval と Lucia Caminos。'),
         ('Q: リークビルドの DL は合法？', '**A:** 教育・アーカイブ目的の開発ビルドリーク。海賊版は推奨しません。**2026年11月19日 GTA 6 購入で Rockstar を支援。**'),
         ('Q: BAN や問題は？', '**A:** Rockstar サーバー未接続のシングルプレイヤーリーク。BAN 不可。法律は現地法を確認。'),
         ('Q: CyberLeak と2022年 teapotuberhacker の違い？',
          '**A:** 2022年が最初の大リーク（teapotuberhacker/Lapsus$）。CyberLeak 2026年8月はより新しく高品質、新ビルド、より包括的。'),
         ('Q: なぜ GTA 6 ランチャーが必要？', '**A:** 開発ビルドは特定起動パラメータが必要。ランチャーが自動設定 — ワンクリックでプレイ。'),
         ('Q: DL サイズと必要容量？', '**A:** \\n- ランチャー：約5GB\\n- 各ビルド：15-25GB\\n- 合計：約80-100GB\\n- **推奨：** SSD 100GB+'),
         ('Q: PS5、Xbox、Mac で動作？', '**A:** いいえ。Windows PC 64-bit のみ。PC 開発ビルド。'),
         ('Q: 完全版かデモ？', '**A:** 2021-2022年開発ビルド、最終版ではない。Vice City 大部分、ミッション、Jason & Lucia、150+車両等。'),
         ('Q: 新リークで更新？', '**A:** はい！CyberLeak を監視し更新。**CyberLeakGTA6.net** をブックマーク。'),
         ('Q: Mod 可能？', '**A:** はい！3GB+ ソースコードで Modder が Mod・スクリプト作成可能。'),
         ('Q: マルチプレイ / GTA Online？', '**A:** いいえ。シングルプレイヤー。GTA Online 2 初期コードあるが機能 MP なし。'),
         ('Q: AV がランチャーを検出 — 安全？', '**A:** 100%安全、15+ AV。ヒューリスティック誤検知の可能性。VirusTotal.com または例外追加。'),
         ('Q: クラッシュ/起動しない？',
          '**A:** \\n1. 管理者実行\\n2. Visual C++ Redistributables\\n3. NVIDIA/AMD ドライバ\\n4. DirectX 12\\n5. Q2 2022 '
          '試す\\n6. 16GB RAM 以上\\n7. OC 無効'),
         ('Q: 配信/YouTube 可能？', '**A:** 技術的には可、Rockstar がリークに DMCA。自己責任。')],
 'lang_section_title': '🌍 他の言語 | Other Languages | Другие языки',
 'lang_section_intro': 'この README は12言語で利用可能：',
 'lang_table_header': ('言語', 'ファイル', 'リンク'),
 'lang_here': 'ここです！',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ GTA 6 CYBERLEEK ビルドを今すぐ DL →',
 'footer_h3': '🎮 **正式リリース前に GTA 6 をプレイ！**',
 'footer_archive': 'CyberLeak GTA 6 公式アーカイブ',
 'footer_updated': '更新：August 28, 2026 | DL数：3,000,000+',
 'footer_disclaimer1': 'Rockstar Games または Take-Two Interactive と無関係',
 'footer_disclaimer2': '2026年11月19日 GTA 6 購入で Rockstar を支援',
 'footer_made': 'GTA コミュニティが ❤️ で制作 | ゲーム史のために保存'}

def _ko() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - 플레이 가능 빌드 다운로드 | 2026년 8월',
 'badge_build': 'BUILD',
 'badge_status_key': '상태',
 'badge_status_val': '플레이 가능',
 'badge_dl_key': '다운로드',
 'badge_upd_key': '업데이트',
 'badge_upd_val': '2026%EB%85%848%EC%9B%94',
 'hero_h2': '🔥 **CYBERLEEK에서 GTA 6 유출 빌드 다운로드 및 플레이** 🔥',
 'hero_h3': '**모두가 찾는 진짜 CyberLeak 플레이 가능 빌드**',
 'hero_tags': '🎮 플레이 가능 게임 | 🚀 GTA 6 런처 | 🗺️ Vice City | 👥 Jason & Lucia | 💻 소스 코드',
 'hero_cta': '⬇️ GTA 6 CYBERLEEK 빌드 지금 다운로드 →',
 'toc_title': '📖 목차',
 'toc': [('🎯 CyberLeek GTA 6 빌드란?', '-what-is-cyberleek-gta-6-build'),
         ('⭐ CyberLeak에서 다운로드하는 이유', '-why-download-from-cyberleek'),
         ('🎮 포함 내용', '-whats-included'),
         ('📥 다운로드 및 설치', '-how-to-download--install'),
         ('💻 시스템 요구 사항', '-system-requirements'),
         ('🔍 CyberLeak 정보', '-about-cyberleek'),
         ('🛡️ 보안', '️-safety--security'),
         ('❓ FAQ', '-faq'),
         ('🌍 다른 언어', '-other-languages')],
 'sec_what_title': '🎯 CyberLeek GTA 6 빌드란?',
 'sec_what_intro': '**CyberLeak**(**CyberLeek**도) **2026년 8월** **가장 최신且 완전한 GTA 6 유출**의 출처로, Rockstar 공식 Netflix '
                   'Extended Look 직전입니다.',
 'sec_what_sub': '🔓 모두가 찾는 바로 그 유출 빌드:',
 'sec_what_list': '- ✅ **플레이 가능 빌드** - 영상만이 아님! 지금 다운로드하여 플레이 가능한 실제 게임\n'
                  '- ✅ **최신 유출** - 2026년 8월, 2022년 9월 teapotuberhacker보다 최신\n'
                  '- ✅ **완전 아카이브** - 90분+ 게임플레이, 소스 코드, 플레이 가능 빌드\n'
                  '- ✅ **진위 증명** - CyberLeak이 게임 내 총알로 «LEEK» 표시\n'
                  '- ✅ **Vice City 게임플레이** - 2026년 11월 19일 출시 전 Vice City 탐험',
 'sec_what_yes': '네, 실제로 플레이할 수 있습니다!',
 'sec_what_yes_body': '영상 모음이 아닙니다 — 커스텀 런처가 포함된 GTA 6 실제 플레이 가능 개발 빌드입니다.',
 'sec_why_title': '⭐ CyberLeak에서 다운로드하는 이유',
 'sec_why_playable_h': '🎮 **플레이 가능 빌드**',
 'sec_why_playable_p': '영상만이 아님! 2021-2022 GTA 6 개발 유출 빌드를 다운로드하고 플레이. 미션, Vice City, 차량, 두 주인공.',
 'sec_why_original_h': '🔥 **CYBERLEEK 오리지널**',
 'sec_why_original_p': '수백만 명이 찾는 진짜 CyberLeak 빌드. «GTA 6 CyberLeak download», «CyberLeek playable build», «GTA 6 '
                       'CyberLeak 2026» — 이 아카이브입니다.',
 'sec_why_versions_h': '📦 **3가지 게임 버전**',
 'sec_why_versions_p': '3가지 개발 빌드 중 선택:',
 'sec_why_versions_list': '- **Q2 2022** (2022년 6월) - 최신, 안정, 완전\n'
                          '- **Q1 2022** (2022년 3월) - 안정, 주요 기능\n'
                          '- **Q4 2021** (2021년 12월) - 초기 빌드, 실험적',
 'sec_why_launcher_h': '🚀 **커스텀 GTA 6 런처**',
 'sec_why_launcher_p': '커스텀 GTA 6 런처: 다운로드, 압축 해제, «Launch Game» 클릭.',
 'sec_why_videos_h': '🎥 **90+ 유출 영상**',
 'sec_why_videos_p': 'CyberLeak 유출 게임플레이 전체 컬렉션 (90분+):',
 'sec_why_videos_list': '- Vice City 탐험\n- Jason & Lucia 게임플레이\n- 은행 강도 미션\n- 경찰 추격\n- 차량\n- 전투 시스템\n- 그 외 다수!',
 'sec_why_source_h': '💻 **소스 코드 접근**',
 'sec_why_source_p': '개발자 및 모더를 위한 3GB+ GTA 6 개발 소스 코드.',
 'sec_why_free_h': '🆓 **100% 무료**',
 'sec_why_free_list': '- 결제 불필요\n- 등록 불필요\n- 설문 불필요\n- 직접 다운로드\n- 즉시 접근',
 'sec_why_safe_h': '🛡️ **안전且 검증됨**',
 'sec_why_safe_list': '- 15+ 백신 스캔\n- 바이러스/멀웨어 없음\n- 숨겨진 마이너 없음\n- 투명한 파일 구조\n- 공식 CyberLeakGTA6.net',
 'sec_included_title': '🎮 포함 내용',
 'sec_included_builds_h': '🕹️ 플레이 가능 빌드',
 'tbl_build_header': ('버전', '날짜', '상태', '기능'),
 'builds_rows': [('Q2 2022', '2022년 6월', '✅ 가장 안정', '최신 기능, 최적화, 권장'),
                 ('Q1 2022', '2022년 3월', '✅ 안정', '주요 기능, 좋은 성능'),
                 ('Q4 2021', '2021년 12월', '⚠️ 실험적', '초기 기능, 일부 버그')],
 'sec_included_launcher_h': '🚀 GTA 6 런처',
 'sec_included_launcher_list': '- 커스텀 런처\n'
                               '- 원클릭 실행\n'
                               '- 빌드 선택 (Q2/Q1/Q4 2022)\n'
                               '- 그래픽 설정\n'
                               '- 해상도 선택\n'
                               '- 디버그 도구\n'
                               '- Windows 전용 (64-bit)',
 'sec_included_map_h': '🗺️ Vice City 맵',
 'sec_included_map_list': '- 탐험 가능한 현대 Vice City (마이애미)\n'
                          '- 크기: GTA V Los Santos의 약 2배\n'
                          '- 다운타운, 해변, 교외, Everglades\n'
                          '- 주야 사이클\n'
                          '- 동적 날씨\n'
                          '- 상세 실내',
 'sec_included_chars_h': '👥 플레이 가능 캐릭터',
 'sec_included_chars_list': '- **Jason Duval** - 남성 주인공: 전투, 운전, 힘\n'
                            '- **Lucia Caminos** - 여성 주인공 (GTA 사상 첫!): 해킹, 잠입, 민첩\n'
                            '- GTA V 같은 듀얼 주인공\n'
                            '- 게임 중 캐릭터 전환\n'
                            '- 고유 능력',
 'sec_included_missions_h': '🎯 미션 및 활동',
 'sec_included_missions_list': '- 은행 강도 미션 (유명 유출 강도 포함)\n- 경찰 추격\n- 스토리 미션\n- 부가 활동\n- 사격장\n- 차량 절도\n- 그 외!',
 'sec_included_vehicles_h': '🚗 150+ 차량',
 'sec_included_vehicles_list': '- 자동차, 오토바이, 보트, 헬리콥터\n- 고급 물리\n- 현실적 손상\n- 커스터마이징\n- GTA V보다 나은 조작',
 'sec_included_source_h': '💻 소스 코드 (3GB+)',
 'sec_included_source_list': '- 게임 엔진 (RAGE 9)\n'
                             '- 미션 스크립트\n'
                             '- 차량 물리\n'
                             '- AI 시스템\n'
                             '- 맵 데이터\n'
                             '- 에셋 파이프라인\n'
                             '- GTA Online 2 네트워크 코드',
 'sec_included_debug_h': '🛠️ 디버그 도구',
 'sec_included_debug_list': '- 개발자 콘솔 (`~` 키)\n- 스폰 메뉴\n- 텔레포트\n- 갓 모드\n- 모든 미션 잠금 해제\n- 수배 없음\n- 날씨/시간 제어',
 'sec_install_title': '📥 다운로드 및 설치',
 'install_labels': ['1단계: 공식 웹사이트',
                    '2단계: 빌드 선택',
                    '3단계: GTA 6 런처 다운로드',
                    '4단계: 빌드 다운로드',
                    '5단계: 파일 압축 해제',
                    '6단계: GTA6Launcher.exe 실행',
                    '7단계: 설정',
                    '8단계: 실행 및 플레이!'],
 'install_bodies': ['상단 다운로드 버튼으로 **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — 공식 안전 출처.',
                    'GTA 6 빌드 버전 선택:\n- **Q2 2022 (권장)** - 가장 안정적且 완전\n- **Q1 2022** - 좋은 균형\n- **Q4 2021** - 초기 개발',
                    '- 크기: ~5GB\n- 런처 및 코어 파일 포함\n- Windows 10/11 64-bit만',
                    '- 각 빌드 15-25GB\n- 압축 아카이브 (.zip 또는 .rar)\n- 권장 공간: 100GB+',
                    '- 여유 공간 있는 폴더에 압축 해제\n- 권장: `C:\\GTA6\\` 또는 `D:\\Games\\GTA6\\`\n- Program Files에 압축 해제 금지',
                    '- `GTA6Launcher.exe` 우클릭\n- **«관리자 권한으로 실행»**\n- Windows 경고 시 «그래도 실행»',
                    '- 빌드 버전 선택\n- 그래픽 및 해상도 설정\n- 필요 시 조작 조정',
                    '- **«LAUNCH GAME»** 클릭\n- 처음 1-2분 대기\n- **공식 출시 전 GTA 6 즐기기!** 🎮'],
 'sec_specs_title': '💻 시스템 요구 사항',
 'sec_specs_min_h': '최소 요구 사항',
 'sec_specs_rec_h': '권장 요구 사항',
 'tbl_spec_header': ('구성 요소', '요구 사항'),
 'min_specs': [('운영 체제', 'Windows 10 64-bit 또는 Windows 11 64-bit'),
               ('프로세서', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('메모리', '16 GB RAM'),
               ('그래픽', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', '버전 12'),
               ('저장 공간', '50+ GB SSD (100GB+ 권장)'),
               ('네트워크', '다운로드용 브로드밴드')],
 'rec_specs': [('운영 체제', 'Windows 11 64-bit'),
               ('프로세서', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('메모리', '32 GB RAM'),
               ('그래픽', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', '버전 12'),
               ('저장 공간', '100+ GB NVMe SSD'),
               ('네트워크', '브로드밴드')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox, Mac 미지원** - Windows PC만\n'
                         '- ✅ SSD 강력 권장\n'
                         '- ✅ 최신 그래픽 드라이버 (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 설치\n'
                         '- ✅ Visual C++ Redistributables (포함)',
 'sec_about_title': '🔍 CyberLeek 정보',
 'sec_about_who_h': 'CyberLeak / CyberLeek는?',
 'sec_about_who_p': '**CyberLeak**(CyberLeak 및 CyberLeek)은 **2026년 8월 GTA 6 유출**의 익명 출처, 최근 가장 중요한 유출 중 하나.',
 'sec_about_timeline_h': 'CyberLeak 유출 연표:',
 'timeline': [('2026년 8월 18일', '첫 유출 게임플레이 영상'),
              ('2026년 8월 19일', 'Jason & Lucia 추가 영상'),
              ('2026년 8월 20-21일', 'Vice City, 미션, 차량'),
              ('2026년 8월 22일', 'CyberLeak «LEEK» 총알 증명'),
              ('2026년 8월 23-27일', 'Rockstar Netflix Extended Look 전 유출')],
 'sec_about_compare_h': 'CyberLeak과 2022 유출 차이?',
 'tbl_compare_header': ('기능', 'CyberLeak (2026년 8월)', 'teapotuberhacker (2022년 9월)'),
 'compare_rows': [('유출일', '2026년 8월', '2022년 9월'),
                  ('빌드 버전', '더 새로움 (2022)', '더 오래됨 (2021-2022)'),
                  ('영상 품질', '고품질', '낮은 dev 영상'),
                  ('양', '90+분', '50+분'),
                  ('접근 증명', '게임 내 «LEEK»', '여러 클립'),
                  ('출처', '불명', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': '왜 «CyberLeak GTA 6» 검색?',
 'sec_about_search_p': '**전 세계 수백만 게이머**가 특히 검색:',
 'sec_about_search_list': '- «GTA 6 CyberLeak download»\n'
                          '- «CyberLeek playable build»\n'
                          '- «GTA 6 CyberLeak 2026»\n'
                          '- «Download GTA 6 from CyberLeak»\n'
                          '- «CyberLeek leak archive»\n'
                          '\n'
                          '**왜?** CyberLeak 콘텐츠는:',
 'why_search_bullets': ['✅ **더 최신** - 최종 게임에 가까움 (2026 vs 2022)',
                        '✅ **더 나은 품질** - 더 좋은 영상/오디오',
                        '✅ **더 완전** - 더 많은 기능과 게임플레이',
                        '✅ **접근 증명** - 플레이 가능 빌드 실증',
                        '✅ **포괄적** - Vice City, 주인공, 미션 등'],
 'sec_about_official': 'CyberLeakGTA6.net은 모든 CyberLeak 콘텐츠 공식 아카이브.',
 'sec_safety_title': '🛡️ 보안',
 'sec_safety_warn_h': '⚠️ 중요 경고',
 'sec_safety_warn_p': '**가짜 다운로드 주의!** 사기 사이트가 **가짜 «GTA 6 빌드»** 배포:',
 'sec_safety_warn_list': '- ❌ 바이러스 및 멀웨어\n- ❌ 랜섬웨어\n- ❌ 암호화폐 마이너\n- ❌ 스파이웨어 및 키로거\n- ❌ 트로jan',
 'sec_safety_fake_p': '가장 흔한 가짜: **113GB 토렌트** — 빈 공간과 숨겨진 멀웨어.',
 'sec_safety_how_h': '✅ 안전 유지:',
 'sec_safety_how_list': '1. **CyberLeakGTA6.net에서만 다운로드**\n'
                        '2. **임의 토렌트 절대 금지**\n'
                        '3. **크기 확인** - 빌드 15-25GB, 113GB 아님\n'
                        '4. **백신 사용** - Windows Defender 가능\n'
                        '5. **Windows 업데이트**\n'
                        '6. **백신 끄지 마세요** - 요구하면 멀웨어!',
 'sec_safety_guarantee_h': '🛡️ 안전 보장:',
 'sec_safety_guarantee_list': '- ✅ 15+ AV 스캔\n- ✅ 등록 불필요\n- ✅ 숨김 파일 없음\n- ✅ 마이너 없음\n- ✅ 스파이웨어 없음\n- ✅ 공식 직접 다운로드',
 'sec_safety_report_h': '📧 가짜 사이트 신고',
 'sec_safety_report_p': '의심스러운 «CyberLeak» «GTA 6 download» 사이트 신고. 유일 공식: **CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ FAQ (자주 묻는 질문)',
 'faq': [('Q: CyberLeak 진짜 GTA 6 플레이 가능 빌드?', '**A:** 예! 플레이 파일, 런처, 전 영상 포함 진짜 CyberLeak 아카이브. CyberLeakGTA6.net 공식.'),
         ('Q: 2026년 11월 19일 출시 전 GTA 6 플레이?',
          '**A:** 예! 런처 및 유출 빌드 다운로드. Vice City, 미션, 차량, Jason Duval & Lucia Caminos.'),
         ('Q: 유출 빌드 다운로드 합법?', '**A:** 교육/아카이브 목적 개발 빌드. 불법 복제 권장 안 함. **2026년 11월 19일 GTA 6 구매로 Rockstar 지원.**'),
         ('Q: 밴 또는 문제?', '**A:** Rockstar 서버 미연결 싱글플레이어. 밴 불가. 현지법 확인.'),
         ('Q: CyberLeak vs teapotuberhacker 2022?',
          '**A:** 2022 첫 대유출 (teapotuberhacker/Lapsus$). CyberLeak 2026년 8월 더 새롭고 고품질.'),
         ('Q: GTA 6 런처 필요 이유?', '**A:** 개발 빌드는 특수 실행 파라미터 필요. 런처가 자동 처리 — 원클릭 플레이.'),
         ('Q: 다운로드 크기 및 공간?', '**A:** \\n- 런처: ~5GB\\n- 각 빌드: 15-25GB\\n- 총: ~80-100GB\\n- **권장:** SSD 100GB+'),
         ('Q: PS5, Xbox, Mac?', '**A:** 아니오. Windows PC 64-bit만. PC 개발 빌드.'),
         ('Q: 완전판 또는 데모?', '**A:** 2021-2022 dev 빌드, 최종판 아님. Vice City 대부분, 미션, Jason & Lucia, 150+ 차량.'),
         ('Q: 새 유출 시 업데이트?', '**A:** 예! CyberLeak 모니터링 및 업데이트. **CyberLeakGTA6.net** 북마크.'),
         ('Q: 모드 가능?', '**A:** 예! 3GB+ 소스 코드로 모더가 mod/스크립트 제작.'),
         ('Q: 멀티플레이 / GTA Online?', '**A:** 아니오. 싱글플레이어. GTA Online 2 초기 코드, 기능 MP 없음.'),
         ('Q: 백신 런처 경고 — 안전?', '**A:** 100% 안전, 15+ AV. 휴리스틱 오탐 가능. VirusTotal.com 또는 예외.'),
         ('Q: 크래시/시작 안 됨?',
          '**A:** \\n1. 관리자 실행\\n2. Visual C++\\n3. NVIDIA/AMD 드라이버\\n4. DirectX 12\\n5. Q2 2022\\n6. 16GB RAM\\n7. OC '
          '끄기'),
         ('Q: 스트리밍/YouTube?', '**A:** 기술적으로 가능, Rockstar DMCA. 본인 책임.')],
 'lang_section_title': '🌍 다른 언어 | Other Languages | Другие языки',
 'lang_section_intro': '이 README는 12개 언어로 제공:',
 'lang_table_header': ('언어', '파일', '링크'),
 'lang_here': '여기입니다!',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': '⬇️ GTA 6 CYBERLEEK 빌드 지금 다운로드 →',
 'footer_h3': '🎮 **공식 출시 전 GTA 6 플레이!**',
 'footer_archive': 'CyberLeak GTA 6 공식 아카이브',
 'footer_updated': '업데이트: August 28, 2026 | 다운로드: 3,000,000+',
 'footer_disclaimer1': 'Rockstar Games 또는 Take-Two Interactive와 무관',
 'footer_disclaimer2': '2026년 11월 19일 GTA 6 구매로 Rockstar 지원',
 'footer_made': 'GTA 커뮤니티 ❤️ | 게임 역사 보존'}

def _tr() -> dict:
    return {'title': '🎮 GTA 6 CYBERLEEK - OYNANABİLİR BUILD İNDİR | Ağustos 2026',
 'badge_build': 'BUILD',
 'badge_status_key': 'DURUM',
 'badge_status_val': 'OYNANABİLİR',
 'badge_dl_key': 'indirmeler',
 'badge_upd_key': 'güncellendi',
 'badge_upd_val': 'A%C4%9Fustos%202026',
 'hero_h2': "🔥 **CYBERLEEK'TEN GTA 6 SIZINTI BUILD'İNİ İNDİR VE OYNA** 🔥",
 'hero_h3': '**Herkesin aradığı otantik CyberLeak oynanabilir build**',
 'hero_tags': '🎮 Oynanabilir oyun | 🚀 GTA 6 Launcher | 🗺️ Vice City | 👥 Jason & Lucia | 💻 Kaynak kodu',
 'hero_cta': "⬇️ GTA 6 CYBERLEEK BUILD'İ ŞİMDİ İNDİR →",
 'toc_title': '📖 İçindekiler',
 'toc': [('🎯 CyberLeek GTA 6 build nedir?', '-what-is-cyberleek-gta-6-build'),
         ("⭐ Neden CyberLeak'ten indirmeli?", '-why-download-from-cyberleek'),
         ('🎮 Neler dahil', '-whats-included'),
         ('📥 Nasıl indirilir ve kurulur', '-how-to-download--install'),
         ('💻 Sistem gereksinimleri', '-system-requirements'),
         ('🔍 CyberLeak hakkında', '-about-cyberleek'),
         ('🛡️ Güvenlik', '️-safety--security'),
         ('❓ SSS', '-faq'),
         ('🌍 Diğer diller', '-other-languages')],
 'sec_what_title': '🎯 CyberLeek GTA 6 build nedir?',
 'sec_what_intro': "**CyberLeak** (**CyberLeek** de) **Ağustos 2026**'daki **en yeni ve en eksiksiz GTA 6 "
                   "sızıntısının** kaynağıdır, Rockstar'ın resmi Netflix Extended Look'undan hemen önce.",
 'sec_what_sub': '🔓 Herkesin aradığı sızıntı build bu:',
 'sec_what_list': '- ✅ **OYNANABİLİR BUILD** - Sadece video değil! İndirip hemen oynayabileceğiniz gerçek oyun\n'
                  "- ✅ **En yeni sızıntı** - Ağustos 2026, Eylül 2022 teapotuberhacker'dan daha yeni\n"
                  "- ✅ **Tam arşiv** - 90+ dakika oynanış, kaynak kodu ve oynanabilir build'ler\n"
                  '- ✅ **Otantiklik kanıtı** - CyberLeak oyunda mermilerle «LEEK» yazdı\n'
                  "- ✅ **Vice City oynanışı** - 19 Kasım 2026 çıkışından önce Vice City'yi keşfedin",
 'sec_what_yes': 'EVET, GERÇEKTEN OYNAYABİLİRSİNİZ!',
 'sec_what_yes_body': "Bu sadece video koleksiyonu değil — özel launcher'ımızla GTA 6'nın gerçek oynanabilir "
                      "geliştirme build'i.",
 'sec_why_title': "⭐ Neden CyberLeak'ten indirmeli?",
 'sec_why_playable_h': "🎮 **OYNANABİLİR BUILD'LER**",
 'sec_why_playable_p': "Sadece video değil! 2021-2022 GTA 6 geliştirme sızıntı build'lerini indirip oynayın. Görevler, "
                       'Vice City, araçlar ve her iki protagonist.',
 'sec_why_original_h': '🔥 **CYBERLEEK ORİJİNAL**',
 'sec_why_original_p': 'Milyonların aradığı otantik CyberLeak build. «GTA 6 CyberLeak download», «CyberLeek playable '
                       'build», «GTA 6 CyberLeak 2026» — bu arşiv.',
 'sec_why_versions_h': '📦 **3 OYUN SÜRÜMÜ**',
 'sec_why_versions_p': "3 geliştirme build'inden birini seçin:",
 'sec_why_versions_list': '- **Q2 2022** (Haziran 2022) - En yeni, kararlı, eksiksiz\n'
                          '- **Q1 2022** (Mart 2022) - Kararlı, ana özellikler\n'
                          '- **Q4 2021** (Aralık 2021) - Erken build, deneysel',
 'sec_why_launcher_h': '🚀 **ÖZEL GTA 6 LAUNCHER**',
 'sec_why_launcher_p': 'Özel GTA 6 Launcher: indir, çıkar, «Launch Game» tıkla.',
 'sec_why_videos_h': '🎥 **90+ SIZINTI VİDEOSU**',
 'sec_why_videos_p': 'CyberLeak sızıntı oynanışının tam koleksiyonu (90+ dakika):',
 'sec_why_videos_list': '- Vice City keşfi\n'
                        '- Jason & Lucia oynanışı\n'
                        '- Banka soygunu görevleri\n'
                        '- Polis kovalamacaları\n'
                        '- Araçlar\n'
                        '- Savaş sistemi\n'
                        '- Ve çok daha fazlası!',
 'sec_why_source_h': '💻 **KAYNAK KODU ERİŞİMİ**',
 'sec_why_source_p': "Geliştiriciler ve modder'lar için 3GB+ GTA 6 geliştirme kaynak kodu.",
 'sec_why_free_h': '🆓 **%100 ÜCRETSİZ**',
 'sec_why_free_list': '- Ödeme yok\n- Kayıt yok\n- Anket yok\n- Doğrudan indirme\n- Anında erişim',
 'sec_why_safe_h': '🛡️ **GÜVENLİ VE DOĞRULANMIŞ**',
 'sec_why_safe_list': '- 15+ antivirüs taraması\n'
                      '- Virüs veya malware yok\n'
                      '- Gizli madenci yok\n'
                      '- Şeffaf dosya yapısı\n'
                      '- Resmi kaynak CyberLeakGTA6.net',
 'sec_included_title': '🎮 Neler dahil',
 'sec_included_builds_h': "🕹️ Oynanabilir build'ler",
 'tbl_build_header': ('Sürüm', 'Tarih', 'Durum', 'Özellikler'),
 'builds_rows': [('Q2 2022', 'Haziran 2022', '✅ En kararlı', 'En yeni özellikler, en iyi optimizasyon, önerilen'),
                 ('Q1 2022', 'Mart 2022', '✅ Kararlı', 'Ana özellikler, iyi performans'),
                 ('Q4 2021', 'Aralık 2021', '⚠️ Deneysel', 'Erken özellikler, bazı hatalar')],
 'sec_included_launcher_h': '🚀 GTA 6 Launcher',
 'sec_included_launcher_list': '- Özel launcher\n'
                               '- Tek tıkla başlatma\n'
                               '- Build seçici (Q2/Q1/Q4 2022)\n'
                               '- Grafik ayarları\n'
                               '- Çözünürlük seçici\n'
                               '- Debug araçları\n'
                               '- Sadece Windows (64-bit)',
 'sec_included_map_h': '🗺️ Vice City haritası',
 'sec_included_map_list': '- Keşfedilebilir modern Vice City (Miami)\n'
                          "- Boyut: GTA V Los Santos'un ~2 katı\n"
                          '- Downtown, plajlar, banliyöler, Everglades\n'
                          '- Gece/gündüz döngüsü\n'
                          '- Dinamik hava\n'
                          '- Detaylı iç mekanlar',
 'sec_included_chars_h': '👥 Oynanabilir karakterler',
 'sec_included_chars_list': '- **Jason Duval** - Erkek protagonist: savaş, sürüş, güç\n'
                            "- **Lucia Caminos** - Kadın protagonist (GTA'da ilk!): hacking, gizlilik, çeviklik\n"
                            '- GTA V gibi çift protagonist\n'
                            '- Oyun içi karakter değiştirme\n'
                            '- Benzersiz yetenekler',
 'sec_included_missions_h': '🎯 Görevler ve aktiviteler',
 'sec_included_missions_list': '- Banka soygunu görevleri (ünlü sızıntı dahil)\n'
                               '- Polis kovalamacaları\n'
                               '- Hikaye görevleri\n'
                               '- Yan aktiviteler\n'
                               '- Atış poligonları\n'
                               '- Araç hırsızlığı\n'
                               '- Ve daha fazlası!',
 'sec_included_vehicles_h': '🚗 150+ araç',
 'sec_included_vehicles_list': '- Arabalar, motosikletler, tekneler, helikopterler\n'
                               '- Gelişmiş fizik\n'
                               '- Gerçekçi hasar\n'
                               '- Özelleştirme\n'
                               "- GTA V'den daha iyi sürüş",
 'sec_included_source_h': '💻 Kaynak kodu (3GB+)',
 'sec_included_source_list': '- Oyun motoru (RAGE 9)\n'
                             '- Görev scriptleri\n'
                             '- Araç fiziği\n'
                             '- AI sistemleri\n'
                             '- Harita verisi\n'
                             '- Asset pipeline\n'
                             '- GTA Online 2 ağ kodu',
 'sec_included_debug_h': '🛠️ Debug araçları',
 'sec_included_debug_list': '- Geliştirici konsolu (`~` tuşu)\n'
                            '- Spawn menüsü\n'
                            '- Işınlanma\n'
                            '- God mode\n'
                            '- Tüm görevler açık\n'
                            '- Aranma yok\n'
                            '- Hava/zaman kontrolü',
 'sec_install_title': '📥 Nasıl indirilir ve kurulur',
 'install_labels': ['Adım 1: Resmi site',
                    'Adım 2: Build seçin',
                    'Adım 3: GTA 6 Launcher indir',
                    'Adım 4: Build indir',
                    'Adım 5: Dosyaları çıkar',
                    'Adım 6: GTA6Launcher.exe çalıştır',
                    'Adım 7: Ayarları yapılandır',
                    'Adım 8: Başlat ve oyna!'],
 'install_bodies': ['İndirme düğmesine tıklayarak **[CyberLeakGTA6.net](https://cyberleakgta6.net)** — resmi güvenli '
                    'kaynak.',
                    'GTA 6 build sürümünü seçin:\n'
                    '- **Q2 2022 (Önerilen)** - En kararlı ve eksiksiz\n'
                    '- **Q1 2022** - İyi denge\n'
                    '- **Q4 2021** - Erken geliştirme',
                    '- Boyut: ~5GB\n- Launcher ve çekirdek dosyalar dahil\n- Sadece Windows 10/11 64-bit',
                    '- Her build 15-25GB\n- Sıkıştırılmış arşiv (.zip veya .rar)\n- Önerilen alan: 100GB+',
                    '- Boş alanı olan klasöre çıkarın\n'
                    '- Önerilen: `C:\\GTA6\\` veya `D:\\Games\\GTA6\\`\n'
                    "- Program Files'a çıkarmayın",
                    '- `GTA6Launcher.exe` sağ tık\n'
                    '- **«Yönetici olarak çalıştır»**\n'
                    '- Windows uyarırsa «Yine de çalıştır»',
                    '- Build sürümü seçin\n- Grafik ve çözünürlük ayarlayın\n- Gerekirse kontrolleri ayarlayın',
                    '- **«LAUNCH GAME»** tıklayın\n'
                    '- İlk seferde 1-2 dakika bekleyin\n'
                    "- **Resmi çıkıştan önce GTA 6'nın tadını çıkarın!** 🎮"],
 'sec_specs_title': '💻 Sistem gereksinimleri',
 'sec_specs_min_h': 'Minimum gereksinimler',
 'sec_specs_rec_h': 'Önerilen gereksinimler',
 'tbl_spec_header': ('Bileşen', 'Gereksinim'),
 'min_specs': [('İşletim sistemi', 'Windows 10 64-bit veya Windows 11 64-bit'),
               ('İşlemci', 'Intel Core i5-8400 / AMD Ryzen 5 1600'),
               ('Bellek', '16 GB RAM'),
               ('Ekran kartı', 'NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB'),
               ('DirectX', 'Sürüm 12'),
               ('Depolama', '50+ GB SSD (100GB+ önerilen)'),
               ('Ağ', 'İndirme için broadband')],
 'rec_specs': [('İşletim sistemi', 'Windows 11 64-bit'),
               ('İşlemci', 'Intel Core i7-10700K / AMD Ryzen 7 3700X'),
               ('Bellek', '32 GB RAM'),
               ('Ekran kartı', 'NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800'),
               ('DirectX', 'Sürüm 12'),
               ('Depolama', '100+ GB NVMe SSD'),
               ('Ağ', 'Broadband')],
 'sec_specs_notes_h': 'Note importanti:',
 'sec_specs_notes_list': '- ❌ **PS5, Xbox ve Mac desteklenmiyor** - sadece Windows PC\n'
                         '- ✅ SSD şiddetle önerilir\n'
                         '- ✅ Güncel grafik sürücüleri (NVIDIA/AMD)\n'
                         '- ✅ DirectX 12 yüklü\n'
                         '- ✅ Visual C++ Redistributables (dahil)',
 'sec_about_title': '🔍 CyberLeek hakkında',
 'sec_about_who_h': 'CyberLeak / CyberLeek kim?',
 'sec_about_who_p': '**CyberLeak** (CyberLeak ve CyberLeek) **Ağustos 2026 GTA 6 sızıntısının** anonim kaynağı, son '
                    'yılların en önemli oyun sızıntılarından biri.',
 'sec_about_timeline_h': 'CyberLeak sızıntı zaman çizelgesi:',
 'timeline': [('18 Ağustos 2026', 'İlk sızıntı oynanış videoları'),
              ('19 Ağustos 2026', "Jason ve Lucia'dan daha fazla görüntü"),
              ('20-21 Ağustos 2026', 'Vice City, görevler, araçlar'),
              ('22 Ağustos 2026', 'CyberLeak mermilerle «LEEK» — erişim kanıtı'),
              ('23-27 Ağustos 2026', 'Rockstar Netflix Extended Look öncesi sızıntılar')],
 'sec_about_compare_h': 'CyberLeak 2022 sızıntısından farkı?',
 'tbl_compare_header': ('Özellik', 'CyberLeak (Ağu 2026)', 'teapotuberhacker (Eyl 2022)'),
 'compare_rows': [('Tarih', 'Ağustos 2026', 'Eylül 2022'),
                  ('Build sürümü', 'Daha yeni (2022)', 'Daha eski (2021-2022)'),
                  ('Video kalitesi', 'Yüksek kalite', 'Düşük, dev görüntü'),
                  ('Miktar', '90+ dakika', '50+ dakika'),
                  ('Erişim kanıtı', 'Oyunda «LEEK»', 'Birden fazla klip'),
                  ('Kaynak', 'Bilinmiyor', 'Arion Kurtaj (Lapsus$)')],
 'sec_about_search_h': 'Neden «CyberLeak GTA 6» aranıyor',
 'sec_about_search_p': '**Dünya çapında milyonlarca oyuncu** özellikle arıyor:',
 'sec_about_search_list': '- «GTA 6 CyberLeak download»\n'
                          '- «CyberLeek playable build»\n'
                          '- «GTA 6 CyberLeak 2026»\n'
                          '- «Download GTA 6 from CyberLeak»\n'
                          '- «CyberLeek leak archive»\n'
                          '\n'
                          '**Neden?** CyberLeak içeriği:',
 'why_search_bullets': ['✅ **Daha yeni** - Final oyuna daha yakın (2026 vs 2022)',
                        '✅ **Daha iyi kalite** - Daha iyi video ve ses',
                        '✅ **Daha eksiksiz** - Daha fazla özellik ve oynanış',
                        '✅ **Kanıtlanmış erişim** - Gerçek oynanabilir build',
                        '✅ **Kapsamlı** - Vice City, protagonistler, görevler vb.'],
 'sec_about_official': 'CyberLeakGTA6.net tüm CyberLeak içeriğinin resmi arşividir.',
 'sec_safety_title': '🛡️ Güvenlik',
 'sec_safety_warn_h': '⚠️ ÖNEMLİ UYARI',
 'sec_safety_warn_p': "**SAHTE İNDİRMELERE DİKKAT!** Dolandırıcı siteler **sahte «GTA 6 build'leri»** dağıtıyor:",
 'sec_safety_warn_list': '- ❌ Virüs ve malware\n'
                         '- ❌ Fidye yazılımı\n'
                         '- ❌ Kripto madencileri\n'
                         "- ❌ Casus yazılım ve keylogger'lar\n"
                         '- ❌ Truva atları',
 'sec_safety_fake_p': 'En yaygın sahte: **113GB torrent** — çoğunlukla boş alan ve gizli malware.',
 'sec_safety_how_h': '✅ Güvende kalmak için:',
 'sec_safety_how_list': "1. **SADECE CyberLeakGTA6.net'dan indirin**\n"
                        "2. **Rastgele torrent'lerden ASLA**\n"
                        "3. **Boyutları kontrol edin** - build'lerimiz 15-25GB, 113GB DEĞİL\n"
                        '4. **Antivirüs kullanın** - Windows Defender yeterli\n'
                        "5. **Windows'u güncel tutun**\n"
                        '6. **Antivirüsü kapatmayın** - isterlerse malware!',
 'sec_safety_guarantee_h': '🛡️ Güvenlik garantilerimiz:',
 'sec_safety_guarantee_list': '- ✅ 15+ antivirüs taraması\n'
                              '- ✅ Kayıt gerekmez\n'
                              '- ✅ Gizli dosya yok\n'
                              '- ✅ Madenci yok\n'
                              '- ✅ Casus yazılım yok\n'
                              '- ✅ Resmi doğrudan indirme',
 'sec_safety_report_h': '📧 Sahte siteleri bildirin',
 'sec_safety_report_p': 'Şüpheli «CyberLeak» veya «GTA 6 download» sitelerini bildirin. Tek resmi site: '
                        '**CyberLeakGTA6.net**.',
 'sec_faq_title': '❓ SSS (Sıkça Sorulan Sorular)',
 'faq': [("S: Bu CyberLeak'in gerçek GTA 6 oynanabilir build'i mi?",
          '**C:** EVET! Oynanabilir dosyalar, launcher ve tüm görüntülerle otantik CyberLeak arşivi. CyberLeakGTA6.net '
          'resmi kaynak.'),
         ('S: 19 Kasım 2026 resmi çıkıştan önce GTA 6 oynayabilir miyim?',
          "**C:** EVET! Launcher ve sızıntı build'lerini indirin. Vice City, görevler, araçlar, Jason Duval ve Lucia "
          'Caminos.'),
         ("S: Sızıntı build'i indirmek yasal mı?",
          "**C:** Eğitim ve arşiv amaçlı sızıntı geliştirme build'i. Korsanlığı teşvik etmiyoruz. **19 Kasım 2026'da "
          "GTA 6 satın alarak Rockstar'ı destekleyin.**"),
         ('S: Ban veya sorun olur mu?',
          '**C:** Rockstar sunucularına bağlı olmayan tek oyunculu build. Ban imkansız. Yerel yasaları kontrol edin.'),
         ('S: CyberLeak ile teapotuberhacker 2022 farkı?',
          '**C:** 2022 ilk büyük sızıntı (teapotuberhacker/Lapsus$). CyberLeak Ağustos 2026 daha yeni, daha kaliteli.'),
         ('S: Neden GTA 6 Launcher gerekli?',
          "**C:** Dev build'ler özel başlatma parametreleri gerektirir. Launcher her şeyi otomatikleştirir — tek tık."),
         ('S: İndirme boyutu ve alan?',
          '**C:** \\n- Launcher: ~5GB\\n- Her build: 15-25GB\\n- Toplam: ~80-100GB\\n- **Önerilen:** 100GB+ SSD'),
         ("S: PS5, Xbox veya Mac'te çalışır mı?", "**C:** HAYIR. Sadece Windows PC 64-bit. PC dev build'leri."),
         ('S: Tam oyun mu demo mu?',
          "**C:** 2021-2022 dev build'leri, final değil. Vice City'in büyük kısmı, görevler, Jason & Lucia, 150+ "
          'araç.'),
         ('S: Yeni sızıntılarda güncellenir mi?', "**C:** EVET! CyberLeak'i izliyoruz. **CyberLeakGTA6.net** yer imi."),
         ('S: Build modlanabilir mi?', "**C:** EVET! 3GB+ kaynak koduyla modder'lar mod/script yapabilir."),
         ('S: Çok oyunculu / GTA Online var mı?',
          '**C:** HAYIR. Tek oyunculu. Erken GTA Online 2 kodu ama işlevsel MP yok.'),
         ("S: Antivirüs launcher'ı işaretliyor — güvenli mi?",
          '**C:** %100 güvenli, 15+ AV. Heuristik yanlış pozitif olabilir. VirusTotal.com veya istisna.'),
         ('S: Çöküyor veya başlamıyor?',
          '**C:** \\n1. Yönetici olarak çalıştır\\n2. Visual C++\\n3. NVIDIA/AMD sürücü\\n4. DirectX 12\\n5. Q2 2022 '
          'dene\\n6. Min 16GB RAM\\n7. Overclock kapat'),
         ('S: Yayın/YouTube yapabilir miyim?',
          '**C:** Teknik olarak evet, Rockstar sızıntı için DMCA gönderir. Kendi riskiniz.')],
 'lang_section_title': '🌍 Diğer diller | Other Languages | Другие языки',
 'lang_section_intro': 'Bu README 12 dilde mevcut:',
 'lang_table_header': ('Dil', 'Dosya', 'Bağlantı'),
 'lang_here': 'Buradasınız!',
 'sec_seo_title': '🔍 SEO Keywords',
 'sec_seo_keywords': 'GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, GTA 6 playable build, '
                     'download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, GTA 6 launcher, GTA 6 CyberLeak download, '
                     'play GTA 6 now, GTA 6 alpha build, GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, '
                     'Grand Theft Auto 6 download, GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked '
                     'version, CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, how to '
                     'download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, safe GTA 6 download, '
                     'GTA 6 full game download',
 'footer_cta': "⬇️ GTA 6 CYBERLEEK BUILD'İ ŞİMDİ İNDİR →",
 'footer_h3': '🎮 **RESMİ ÇIKIŞTAN ÖNCE GTA 6 OYNA!**',
 'footer_archive': 'Resmi CyberLeak GTA 6 Arşivi',
 'footer_updated': 'Güncellendi: August 28, 2026 | İndirmeler: 3.000.000+',
 'footer_disclaimer1': 'Rockstar Games veya Take-Two Interactive ile bağlantılı değil',
 'footer_disclaimer2': "19 Kasım 2026'da GTA 6 satın alarak Rockstar'ı destekleyin",
 'footer_made': 'GTA topluluğu tarafından ❤️ ile | Oyun tarihi için korundu'}

TRANSLATIONS: dict[str, dict] = {
    "en": _en(),
    "ru": _ru(),
    "es": _es(),
    "de": _de(),
    "fr": _fr(),
    "it": _it(),
    "pt": _pt(),
    "pl": _pl(),
    "zh": _zh(),
    "ja": _ja(),
    "ko": _ko(),
    "tr": _tr(),
}


def main() -> None:
    for lang, t in TRANSLATIONS.items():
        path = OUTPUT_DIR / LANG_FILES[lang]
        content = build_readme(lang, t)
        path.write_text(content, encoding="utf-8")
        print(f"{lang}: {path.name} -> {len(content.splitlines())} lines")


if __name__ == "__main__":
    main()

