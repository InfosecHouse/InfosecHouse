#!/usr/bin/env python3
"""Infosec House 3.0 static site generator. Standard library only.

    python3 scripts/build.py          build the site into dist/
    python3 scripts/build.py --serve  build, then serve dist/ on http://localhost:8788
"""
import collections
import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
SRC = ROOT / "src"
DIST = ROOT / "dist"

SITE = json.loads((DATA / "site.json").read_text(encoding="utf-8"))
TODAY = dt.date.today()
JSON_LD = __import__("json").dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/",
         "name": SITE["name"], "description": SITE["description"],
         "publisher": {"@id": SITE["url"] + "/#org"},
         "potentialAction": {"@type": "SearchAction",
             "target": {"@type": "EntryPoint", "urlTemplate": SITE["url"] + "/?q={search_term_string}"},
             "query-input": "required name=search_term_string"}},
        {"@type": "Organization", "@id": SITE["url"] + "/#org", "name": SITE["name"],
         "url": SITE["url"] + "/", "logo": SITE["url"] + "/assets/headers/hero-wordmark.svg",
         "sameAs": [x["href"] for x in SITE.get("social", [])]},
    ],
}, separators=(",", ":"))

LOGO_PATHS = (
    '<path d="M210 1937 l0 -142 143 -143 142 -142 170 0 170 0 -93 -93 -92 -92 0 -200 0 -200 -220 -220 -220 -220 0 -147 0 -148 138 0 137 0 283 283 282 282 0 382 0 383 -277 280 -277 280 -143 0 -143 0 0 -143z"/>'
    '<path d="M890 1943 l0 -138 317 -317 317 -318 -192 0 -192 0 0 -225 0 -225 -125 -125 -125 -125 0 -140 0 -140 143 0 142 0 178 178 178 178 -1 295 c0 162 2 298 6 302 4 4 55 -43 114 -103 l107 -109 79 -3 79 -3 5 -87 5 -87 278 -280 278 -281 140 0 139 0 0 138 0 137 -143 143 -142 142 -180 0 -180 0 103 103 102 102 0 200 0 200 220 220 220 220 0 142 0 143 -143 0 -143 0 -277 -278 -277 -279 0 -96 0 -97 -190 0 -190 0 -2 168 c0 92 -2 180 -3 195 -2 23 -40 67 -181 208 l-179 179 -142 0 -143 0 0 -137z"/>'
)
LOGO = ('<svg class="logo-mark" viewBox="0 0 300 232" aria-hidden="true"><g transform="translate(0,232) scale(0.1,-0.1)" '
        f'fill="currentColor">{LOGO_PATHS}</g></svg>')

ICONS = {
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "tools": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    "code": '<path d="m8 6-6 6 6 6M16 6l6 6-6 6"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    "github": '<path d="M9 19c-4 1.5-4-2-6-2.5m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12 12 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "arrow": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "onion": '<circle cx="12" cy="13" r="7"/><circle cx="12" cy="13" r="4"/><path d="M12 6V3"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "sheet": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
    "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    "alert": '<path d="M12 3 2 20h20z"/><path d="M12 10v4m0 3v.01"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5m0-8v.01"/>',
}

SOCIAL_ICONS = {
    "GitHub": ICONS["github"],
    "X": '<path d="M4 4l16 16M20 4 4 20"/>',
    "Telegram": '<path d="m21 4-18 7 6 2 2 6 3-4 5 4z"/><path d="m9 13 8-6"/>',
    "Instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/>',
    "YouTube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3z"/>',
}


def icon(name, cls="icon", paths=None):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths or ICONS[name]}</svg>')


def e(s):
    return html.escape(str(s or ""), quote=True)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fmt(n):
    return f"{n:,}"


# --------------------------------------------------------------------------- markdown

def safe_href(url):
    """Allow only http(s), mailto, anchors, and site-relative URLs. Blocks javascript:, data:, etc."""
    u = (url or "").strip()
    if re.match(r"^(https?:|mailto:|#)", u, re.I):
        return u
    if u.startswith("/") and not u.startswith("//"):
        return u
    if u.startswith(("./", "../")):
        return u
    return None


def md_inline(text):
    """Render a safe subset of inline markdown. All text is HTML-escaped; only links,
    images, bold, em and code become tags, and link/image URLs are scheme-checked. This
    runs on contributor-supplied catalog data, so it must never emit raw HTML."""
    slots = []

    def put(s):
        slots.append(s)
        return f"\x00{len(slots) - 1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: put(f"<code>{e(m.group(1))}</code>"), text)

    def img(m):
        src = safe_href(m.group(2))
        return put(f'<img src="{e(src)}" alt="{e(m.group(1))}" loading="lazy">') if src else e(m.group(1))

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, text)

    def link(m):
        label = html.escape(m.group(1), quote=False)  # label text escaped; image slots (\x00) preserved
        href = re.sub(r"^/?([\w-]+)\.md$", r"/\1/", m.group(2))
        safe = safe_href(href)
        if not safe:
            return label
        ext = safe.startswith("http") and "infosec.house" not in safe
        attrs = ' target="_blank" rel="noopener noreferrer nofollow"' if ext else ""
        return put(f'<a href="{e(safe)}"{attrs}>{label}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = html.escape(text, quote=False)  # escape everything that is not a slot marker
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?!\w)", r"<em>\1</em>", text)
    text = re.sub(r"\\([\[\]_*])", r"\1", text)

    def restore(s):
        return re.sub(r"\x00(\d+)\x00", lambda m: restore(slots[int(m.group(1))]), s)

    return restore(text)


def markdown(src, allow_html=False):
    lines = src.splitlines()
    out, i = [], 0
    para = []

    def flush():
        if para:
            out.append(f"<p>{md_inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
            i += 1
            continue
        if s.startswith("```"):
            flush()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            lang = s[3:].strip()
            head = f'<div class="code-head"><span>{e(lang)}</span><button type="button" class="copy" data-copy>Copy</button></div>'
            out.append(f'<div class="code">{head}<pre><code>{e(chr(10).join(buf))}</code></pre></div>')
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush()
            lvl = len(m.group(1))
            out.append(f'<h{lvl} id="{slugify(m.group(2))}">{md_inline(m.group(2))}</h{lvl}>')
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,})$", s):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if s.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            m = re.match(r"^\[!(\w+)\]$", buf[0]) if buf else None
            if m:
                kind = m.group(1).lower()
                out.append(callout(kind, md_inline(" ".join(buf[1:]))))
            else:
                out.append(f"<blockquote>{markdown(chr(10).join(buf))}</blockquote>")
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-+", lines[i + 1].strip()):
            flush()
            rows = []
            while i < len(lines) and "|" in lines[i]:
                cells = re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))
                rows.append([c.strip().replace("\\|", "|") for c in cells])
                i += 1
            head, body = rows[0], rows[2:]
            t = "<div class=\"table-wrap\"><table><thead><tr>" + "".join(f"<th>{md_inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>")
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush()
            ordered = bool(re.match(r"^\s*\d+\.", line))
            items = []
            while i < len(lines) and (re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) or
                                      (lines[i].startswith("  ") and lines[i].strip())):
                indent = len(lines[i]) - len(lines[i].lstrip())
                txt = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", lines[i])
                items.append((indent, txt))
                i += 1
            out.append(render_list(items, ordered))
            continue
        if s.startswith("<") and allow_html:  # raw HTML only on trusted maintainer pages
            flush()
            out.append(line)
            i += 1
            continue
        para.append(s)
        i += 1
    flush()
    return "\n".join(out)


def render_list(items, ordered):
    tag = "ol" if ordered else "ul"
    base = items[0][0]
    html_out, j = [f"<{tag}>"], 0
    while j < len(items):
        indent, txt = items[j]
        children = []
        j += 1
        while j < len(items) and items[j][0] > base:
            children.append(items[j])
            j += 1
        li = md_inline(txt)
        if children:
            li += render_list(children, False)
        html_out.append(f"<li>{li}</li>")
    html_out.append(f"</{tag}>")
    return "".join(html_out)


def callout(kind, body_html):
    kind = {"note": "info", "tip": "info", "important": "info", "caution": "danger"}.get(kind, kind)
    name = "alert" if kind in ("danger", "warning") else "info"
    return f'<div class="callout callout-{e(kind)}">{icon(name)}<div>{body_html}</div></div>'


def frontmatter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        for line in text[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[end + 4:]
    return meta, text.lstrip()


# --------------------------------------------------------------------------- data

def host_of(url):
    try:
        h = urlparse(url).netloc
    except ValueError:
        return url
    return h[4:] if h.startswith("www.") else h


def validate(cat, path):
    """Fail the build on malformed entries so a bad pull request never deploys."""
    errors = []
    for key in ("slug", "title", "description", "sections"):
        if not cat.get(key):
            errors.append(f"missing '{key}'")
    if cat.get("slug") != path.stem:
        errors.append(f"slug '{cat.get('slug')}' must match file name '{path.stem}'")
    for sec in cat.get("sections", []):
        for grp in sec.get("groups", []):
            urls = set()
            for t in grp.get("tools", []):
                where = f"{sec.get('title') or '-'} > {grp.get('title') or '-'} > {t.get('name', '?')}"
                if not t.get("name") or not t.get("url"):
                    errors.append(f"{where}: every tool needs 'name' and 'url'")
                elif not re.match(r"^(https?|mailto):", t["url"]):
                    errors.append(f"{where}: url must start with http(s):// or mailto:")
                elif t["url"] in urls:
                    print(f"  warning: {path.name}: {where} is listed twice in the same group")
                urls.add(t.get("url"))
                for lk in t.get("links", []):
                    if not isinstance(lk, dict) or not re.match(r"^(https?|mailto):", lk.get("url", "")):
                        errors.append(f"{where}: each link needs a url starting with http(s):// or mailto:")
    if errors:
        sys.exit(f"{path.relative_to(ROOT)}:\n  " + "\n  ".join(errors))


def load_categories():
    cats = []
    for slug in SITE["categories"]:
        path = DATA / "categories" / f"{slug}.json"
        cat = json.loads(path.read_text(encoding="utf-8"))
        validate(cat, path)
        seen = set()
        tools = []
        for sec in cat["sections"]:
            for grp in sec["groups"]:
                for t in grp["tools"]:
                    anchor = slugify(t["name"]) or "tool"
                    while anchor in seen:
                        anchor += "-2"
                    seen.add(anchor)
                    t["_anchor"] = anchor
                    t["_section"] = sec["title"]
                    t["_group"] = grp["title"]
                    tools.append(t)
        tools.sort(key=lambda t: (t["name"].lower(), t["name"]))

        # Tab membership. A tab is a named section, or a group when sections are unnamed.
        # A tool belongs to its own tab plus any extra tabs named in its optional "also" list.
        named = any(s["title"] for s in cat["sections"])
        title_to_tab = {}  # section OR group title -> (tab slug, tab title)
        for sec in cat["sections"]:
            for grp in sec["groups"]:
                tab_title = sec["title"] if named else grp["title"]
                pair = (slugify(tab_title), tab_title)
                if grp["title"]:
                    title_to_tab[grp["title"]] = pair
                if sec["title"]:
                    title_to_tab[sec["title"]] = pair
        for t in tools:
            primary = t["_section"] if named else t["_group"]
            tabs = dict([title_to_tab.get(primary, (slugify(primary), primary))])
            for extra in t.get("also", []):
                if extra in title_to_tab:
                    s2, t2 = title_to_tab[extra]
                    tabs.setdefault(s2, t2)
                else:
                    print(f"  warning: {slug}.json: {t['name']!r} 'also' entry {extra!r} is not a section or group here")
            t["_tabs"] = list(tabs.keys())
            t["_tab_titles"] = list(tabs.values())

        cat["_tools"] = tools
        cat["_named"] = named
        cat["_repos"] = sum(1 for t in tools if t.get("repo"))
        cat["_group"] = next((g for g, slugs in SITE.get("groups", {}).items() if slug in slugs), "")
        cats.append(cat)
    return cats


MONO = {
    "ai": "AI", "api": "API", "assets-management": "AM", "blogs": "BLG", "bug-bounty": "$$", "c2": "C2",
    "cheat-sheets": "CS", "cloud-containers": "CLD", "collab": "CO", "cracking": "#!", "cryptography": "KEY",
    "ctf": "CTF", "data-exfiltration": "EXF", "e-mail": "@", "editor-viewer": "HEX",
    "education": "EDU", "emulation": "EMU", "endpoint-protection": "EDR", "evasion": "EVA", "exploits": "0D",
    "firewalls": "FW", "forensics": "DF", "hardware": "HW", "honeypot": "HP", "ids-ips": "IDS", "ir": "IR",
    "linux": "LNX", "malware": "MAL", "mobile": "MOB", "music": "MU", "network": "NET",
    "operating-systems": "OS", "opsec": "OPS", "osint": "OSI", "privilege-escalation": "PE",
    "re": "RE", "recon": "RCN", "shells": "$_", "social-engineering": "SE", "threat-intel": "TI",
    "videos": "VID", "vuln-scanners": "VS", "web-app": "WEB", "windows": "WIN", "wireless": "RF",
}


def mono(slug, title):
    return MONO.get(slug) or "".join(w[0] for w in title.split()[:3]).upper()


# --------------------------------------------------------------------------- layout

def breadcrumb_ld(trail):
    """BreadcrumbList JSON-LD from a list of (name, path) tuples."""
    items = [{"@type": "ListItem", "position": i + 1, "name": name,
              "item": SITE["url"] + path} for i, (name, path) in enumerate(trail)]
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList",
                       "itemListElement": items}, separators=(",", ":"))


def layout(path, title, description, body, hero="", body_class="", crumbs=None):
    full_title = SITE["name"] if path == "/" else f"{title} | {SITE['name']}"
    canonical = SITE["url"] + path
    nav = "".join(
        f'<a href="{e(n["href"])}"{" aria-current=page" if path.startswith(n["href"]) and n["href"] != "/" else ""}>{e(n["label"])}</a>'
        for n in SITE["nav"])
    cta = SITE.get("cta")
    social = social_row()
    analytics = ""
    uid = SITE.get("analytics", {}).get("umami_website_id")
    if uid:
        analytics = f'<script defer src="https://cloud.umami.is/script.js" data-website-id="{e(uid)}"></script>'
    footer_cats = "".join(
        f'<a href="/{c["slug"]}/">{e(c["title"])}</a>' for c in sorted(CATS, key=lambda c: -len(c["_tools"]))[:10])
    if SPONSOR_FOOTER:
        logos = "".join(sponsor_a(sp["url"], "footer",
                        f'<img src="{e(sp["logo"])}" alt="{e(sp.get("name", "Sponsor"))}" loading="lazy">')
                        for sp in SPONSOR_FOOTER)
        footer_sponsor = f'<div class="wrap footer-sponsor"><span class="muted">Sponsored by</span>{logos}</div>'
    else:
        footer_sponsor = ('<div class="wrap footer-sponsor"><span class="muted">This spot is available.</span>'
                          '<a href="/support-us/">Sponsor Infosec House</a></div>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(canonical)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(canonical)}">
<meta property="og:image" content="{SITE['url']}/assets/headers/infosechouse-header.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#05090c">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v={BUILD_ID}">
<script defer src="/app.js?v={BUILD_ID}"></script>
<script type="application/ld+json">{JSON_LD}</script>
{f'<script type="application/ld+json">{breadcrumb_ld(crumbs)}</script>' if crumbs else ''}
{analytics}
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="wrap topbar-inner">
    <a class="brand" href="/">{LOGO}<span>infosec<b>house</b></span></a>
    <nav class="nav" id="nav">{nav}</nav>
    <div class="topbar-actions">
      <button class="search-trigger" type="button" data-open-search aria-label="Search tools">{icon("search")}<span>Search</span><kbd>/</kbd></button>
      {f'<a class="btn btn-brand btn-sm cta" href="{e(cta["href"])}">{icon("heart")}{e(cta["label"])}</a>' if cta else ""}
      <button class="icon-btn menu-btn" type="button" data-menu aria-label="Open menu" aria-controls="nav" aria-expanded="false">{icon("menu")}</button>
    </div>
  </div>
</header>
{hero}
<main id="main">
{body}
</main>
<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="/">{LOGO}<span>infosec<b>house</b></span></a>
      <p class="muted">{e(SITE['description'])}</p>
      <div class="social">{social}</div>
    </div>
    <div><h4>Popular</h4>{footer_cats}</div>
    <div><h4>Project</h4>
      <a href="/about/">About</a><a href="/blog/">Blog</a><a href="/support-us/">Support us</a><a href="/sponsors/">Sponsors</a><a href="/partnership/">Partnership</a>
      <a href="/api/tools.json">JSON API</a>
      <a href="{e(SITE['repo'])}" target="_blank" rel="noopener">Source on GitHub</a></div>
    <div><h4>Contribute</h4>
      <a href="{e(SITE['repo'])}/pulls" target="_blank" rel="noopener">Suggest a tool</a>
      <a href="{e(SITE['repo'])}/issues" target="_blank" rel="noopener">Report a broken link</a></div>
  </div>
  {footer_sponsor}
  <div class="wrap footer-base"><span>&copy; {SITE.get('since', 2021)}&ndash;{TODAY.year} {e(SITE['name'])}. All rights reserved.</span><span class="muted">For authorized security testing and education only.</span></div>
</footer>
<dialog class="palette" id="palette" aria-label="Search">
  <div class="palette-box">
    <div class="search-field">{icon("search")}<input type="search" placeholder="Search {fmt(TOTAL_TOOLS)} tools and resources…" autocomplete="off" spellcheck="false" data-search-input><kbd>esc</kbd></div>
    <div class="search-results" data-search-results></div>
  </div>
</dialog>
</body>
</html>
"""


def page_hero(crumbs, title, lede="", extra="", cls=""):
    trail = "".join(f'<a href="{e(h)}">{e(t)}</a><span>/</span>' for t, h in crumbs)
    return f"""<section class="hero hero-sub {cls}">
  <div class="hero-bg" aria-hidden="true"><span class="hero-blob b1"></span><span class="hero-blob b2"></span><span class="hero-blob b3"></span></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">{trail}<span aria-current="page">{e(title)}</span></nav>
    <h1>{e(title)}</h1>
    {f'<p class="lede">{lede}</p>' if lede else ""}
    {extra}
  </div>
</section>"""


def stat(icon_name, value, label):
    return f'<div class="stat">{icon(icon_name, "icon stat-icon")}<div><strong>{value}</strong><span>{e(label)}</span></div></div>'


# --------------------------------------------------------------------------- pages

def build_home(cats):
    total_repos = sum(c["_repos"] for c in cats)
    groups = SITE.get("groups", {})
    tabs = '<button class="tab" aria-pressed="true" data-group="">All</button>' + "".join(
        f'<button class="tab" aria-pressed="false" data-group="{e(g)}">{e(g)}</button>' for g in groups)

    cards = []
    for c in cats:
        n = len(c["_tools"])
        sections = [s["title"] for s in c["sections"] if s["title"]] or [g["title"] for s in c["sections"] for g in s["groups"] if g["title"]]
        sample = ", ".join(t["name"] for t in c["_tools"][:3])
        meta = f'<span>{icon("layers")}{len(sections)} section{"s" if len(sections) != 1 else ""}</span>' if sections else ""
        meta += f'<span>{icon("github")}{c["_repos"]} repos</span>' if c["_repos"] else ""
        cards.append(f"""<a class="card cat-card" href="/{c['slug']}/" data-group="{e(c['_group'])}" data-count="{n}" data-name="{e(c['title'].lower())}" data-search="{e((c['title'] + ' ' + c['description'] + ' ' + ' '.join(sections)).lower())}">
  <div class="cat-head"><span class="mono">{e(mono(c['slug'], c['title']))}</span><h3>{e(c['title'])}</h3><span class="count">{n}</span></div>
  <p class="cat-desc">{e(c['description'])}</p>
  <div class="cat-meta">{meta}</div>
  <p class="cat-sample">{e(sample)}</p>
</a>""")

    popular = sorted(cats, key=lambda c: -len(c["_tools"]))[:6]
    chips = "".join(f'<a class="chip" href="/{c["slug"]}/">{e(c["title"])}</a>' for c in popular)

    hero = f"""<section class="hero hero-home">
  <div class="hero-bg" aria-hidden="true"><span class="hero-blob b1"></span><span class="hero-blob b2"></span><span class="hero-blob b3"></span></div>
  <div class="wrap hero-inner">
    <p class="eyebrow"><span class="dot"></span>Updated {e(LAST_UPDATED)}</p>
    <img class="hero-art" src="/assets/headers/hero-wordmark.svg" alt="Infosec House" width="1287" height="734">
    <h1 class="hero-name">Infosec House</h1>
    <p class="lede">{e(SITE['description'])}</p>
    <div class="hero-search">
      <div class="search-field">{icon("search")}<input type="search" placeholder="Search tools, techniques, repos…" autocomplete="off" spellcheck="false" data-search-input aria-label="Search tools"><kbd>/</kbd></div>
      <div class="search-results" data-search-results></div>
    </div>
    <div class="chips"><span class="muted">Popular:</span>{chips}</div>
  </div>
</section>
<div class="wrap stats-wrap"><div class="stats">
  {stat("tools", fmt(TOTAL_TOOLS), "Tools & resources")}
  {stat("grid", len(cats), "Categories")}
  {stat("github", fmt(total_repos), "Open-source repos")}
</div></div>"""

    body = f"""<section class="wrap section" id="categories">
  <div class="section-head">
    <h2>Browse by category</h2>
    <div class="toolbar">
      <div class="tabs" role="group" aria-label="Filter by discipline">{tabs}</div>
      <div class="filter">{icon("search")}<input type="search" placeholder="Filter categories" data-card-filter aria-label="Filter categories"></div>
      <label class="select"><span class="sr-only">Sort</span><select data-card-sort><option value="name">A–Z</option><option value="count">Most tools</option></select></label>
    </div>
  </div>
  <div class="grid cat-grid" data-cards>{''.join(cards)}</div>
  <p class="empty" data-empty hidden>No categories match that filter.</p>
</section>
<section class="wrap section">
  <div class="cta-band">
    <div><h2>Know a tool that belongs here?</h2><p>Infosec House is community-maintained. Every entry is a line of JSON in the GitHub repo, so adding one is a single pull request.</p></div>
    <div class="cta-actions"><a class="btn btn-brand" href="/contribute/">{icon("plus")}Contribute</a></div>
  </div>
</section>"""
    write("/", layout("/", SITE["name"], SITE["description"], body, hero, "home"))


def short_num(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def ago(days):
    if days < 30:
        return f"{max(days, 1)}d ago"
    if days < 365:
        return f"{days // 30}mo ago"
    return f"{days // 365}y ago"


def link_pill(href, icon_name, label, cls="", title=""):
    return (f'<a class="pill pill-link {cls}" href="{e(href)}" target="_blank" rel="noopener noreferrer nofollow"'
            f'{f" title={chr(34)}{e(title)}{chr(34)}" if title else ""}>{icon(icon_name)}{e(label)}</a>')


def repo_status(repo):
    """Last-updated pill and stars from data/github.json, written by scripts/enrich_github.py."""
    gh = GITHUB.get(repo)
    if not gh:
        return ""
    if gh.get("missing"):
        return '<span class="pill pill-old" title="Repository deleted, renamed, or private">Repo not found</span>'
    days = (TODAY - dt.date.fromisoformat(gh["pushed"])).days
    if gh.get("archived"):
        state, label = "archived", "Archived"
    else:
        state = "fresh" if days < 180 else "stale" if days < 730 else "old"
        label = ago(days)
    return f'<span class="pill pill-{state}" title="Last updated {e(gh["pushed"])}">{icon("clock")}{label}</span>'


def sponsor_href(url, slot):
    """Append UTM params so sponsors can attribute the traffic in their own analytics."""
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}utm_source=infosec.house&utm_medium={slot}&utm_campaign=sponsor"


def sponsor_a(url, slot, inner, cls=""):
    """Outbound sponsor link: UTM on the href, plus a Umami event so we can count clicks."""
    c = f' class="{cls}"' if cls else ""
    return (f'<a{c} href="{e(sponsor_href(url, slot))}" target="_blank" rel="noopener sponsored" '
            f'data-umami-event="sponsor-{slot}">{inner}</a>')


def sponsor_banner(sp):
    """Silver+ category banner."""
    img = sponsor_a(sp.get("link") or sp["url"], "banner",
                    f'<img src="{e(sp["banner"])}" alt="{e(sp["name"])}" loading="lazy">',
                    cls="sponsor-banner") if sp.get("banner") else ""
    name = sponsor_a(sp["url"], "banner", f'<strong>{e(sp["name"])}</strong>')
    return (f'<aside class="sponsor"><span class="badge">Sponsor</span>'
            f'<div>{name} <span class="muted">{e(sp.get("description", ""))}</span></div>{img}</aside>')


def tool_badge(page_path):
    """Bronze 'Sponsor' badge on a tool listing, from SITE['sponsors']['badges'][<slug>]."""
    slug = page_path.rstrip("/").rsplit("/", 1)[-1]
    b = SPONSOR_BADGES.get(slug)
    if not b:
        return ""
    label = e(b.get("name", "Sponsor"))
    if b.get("url"):
        return sponsor_a(b["url"], "badge", "Sponsor", cls="pill pill-sponsor").replace(
            'class="pill pill-sponsor"', f'class="pill pill-sponsor" title="Sponsored: {label}"')
    return f'<span class="pill pill-sponsor" title="Sponsored by {label}">Sponsor</span>'


def tool_row(t, cat):
    url, repo = t["url"], t.get("repo")
    host = host_of(url)
    # Primary link: where the tool lives
    if ".onion" in url:
        pills = [link_pill(url, "onion", "TOR", "pill-tor", "Onion service, requires Tor Browser")]
    elif host == "github.com":
        pills = [link_pill(url, "github", "GitHub")]
    else:
        pills = [link_pill(url, "globe", "Website", title=host)]
    if repo and host != "github.com":
        pills.append(link_pill(f"https://github.com/{repo}", "github", "GitHub"))
    stars = GITHUB.get(repo, {}).get("stars") if repo else None
    if stars is not None:
        pills.append(f'<span class="stars" title="GitHub stars">★ {short_num(stars)}</span>')
    updated = (repo_status(repo) if repo else "") or '<span class="none" aria-label="Not applicable">—</span>'
    for l in t.get("links", []):
        if l["url"] != url:
            tor = ".onion" in l["url"]
            pills.append(link_pill(l["url"], "onion" if tor else "external", l["label"], "pill-tor" if tor else ""))
    if len(t["_tab_titles"]) > 1:
        where = " · ".join(e(x) for x in t["_tab_titles"])
    else:
        where = (f'{e(t["_group"])}<span class="sub">{e(t["_section"])}</span>' if t["_group"] and t["_section"]
                 else e(t["_group"] or t["_section"]))
    sub = repo if repo else host
    search = " ".join([t["name"], t.get("description", ""), t["_section"], t["_group"], repo or ""]).lower()
    sheet = f'<span class="pill pill-sheet pill-icon" title="Has a cheat sheet" aria-label="Has a cheat sheet">{icon("sheet")}</span>' if t["_page"] in SHEETS else ""
    badge = tool_badge(t["_page"])
    return f"""<tr id="{t['_anchor']}" data-href="{t['_page']}" data-section="{e(' '.join(t['_tabs']))}" data-search="{e(search)}">
  <td class="c-name"><a href="{t['_page']}">{e(t['name'])}</a>{badge}{sheet}<span class="sub">{e(sub)}</span></td>
  <td class="c-desc">{md_inline(t.get('description', ''))}</td>
  <td class="c-where">{where}</td>
  <td class="c-links"><div class="links">{''.join(pills)}</div></td>
  <td class="c-updated">{updated}</td>
</tr>"""


def build_category(cat, idx, cats):
    tools = cat["_tools"]
    named = cat["_named"]
    # Count tools per tab from their resolved tab membership (a tool can be in several tabs).
    tab_count = collections.Counter(sl for t in tools for sl in t["_tabs"])
    if named:
        tab_items = [(s["title"], tab_count[slugify(s["title"])], s.get("description", ""))
                     for s in cat["sections"] if s["title"]]
    else:
        tab_items = [(g["title"], tab_count[slugify(g["title"])], g.get("description", ""))
                     for s in cat["sections"] for g in s["groups"] if g["title"]]
    tabs = f'<button class="tab" aria-pressed="true" data-tab="">All <span>{len(tools)}</span></button>' + "".join(
        f'<button class="tab" aria-pressed="false" data-tab="{e(slugify(t))}" data-desc="{e(d)}">{e(t)} <span>{n}</span></button>'
        for t, n, d in tab_items)

    notices = "".join(callout(n["type"], md_inline(n["text"])) for n in cat.get("notices", []))
    for s in cat["sections"]:
        for n in s.get("notices", []):
            notices += callout(n["type"], f'<strong>{e(s["title"])}:</strong> ' + md_inline(n["text"]))

    sp = SPONSOR_BANNERS.get(cat["slug"])
    sponsor_top = sponsor_banner(sp) if sp else ""

    rows = "".join(tool_row(t, cat) for t in tools)
    tor = sum(1 for t in tools if "tor" in t.get("tags", []))
    edit = SITE["edit_base"] + cat["slug"] + ".json"
    stats = (f'<div class="hero-stats"><div><strong>{len(tools)}</strong><span>Tools & resources</span></div>'
             f'<div><strong>{len(tab_items)}</strong><span>{"Sections" if named else "Groups"}</span></div>'
             f'<div><strong>{cat["_repos"]}</strong><span>GitHub repos</span></div>'
             + (f'<div><strong>{tor}</strong><span>Onion services</span></div>' if tor else "") + "</div>")
    actions = (f'<div class="hero-actions"><a class="btn btn-brand btn-sm" href="{e(SITE["repo"])}/pulls" target="_blank" rel="noopener">{icon("plus")}Suggest a tool</a>'
               f'<a class="btn btn-ghost btn-sm" href="{e(edit)}" target="_blank" rel="noopener">{icon("edit")}Edit this page</a>'
               f'<a class="btn btn-ghost btn-sm" href="/api/categories/{cat["slug"]}.json">{icon("code")}JSON</a></div>')
    lede = e(cat["description"]) + (f' <span class="intro">{e(cat["intro"])}</span>' if cat.get("intro") and cat["intro"] not in cat["description"] else "")
    hero = page_hero([("Infosec House", "/"), ("Categories", "/#categories")], cat["title"], lede, stats + actions)

    prev_c, next_c = cats[idx - 1], cats[(idx + 1) % len(cats)]
    body = f"""<div class="wrap section">
  {sponsor_top}{notices}
  <div class="table-toolbar">
    <div class="tabs tabs-scroll" role="group" aria-label="Filter by section">{tabs}</div>
    <div class="filter">{icon("search")}<input type="search" placeholder="Filter {len(tools)} entries" data-row-filter aria-label="Filter entries"></div>
  </div>
  <p class="tab-desc" data-tab-desc hidden></p>
  <p class="result-count"><span data-row-count>{len(tools)}</span> entries</p>
  <div class="table-wrap data-table-wrap">
    <table class="data-table">
      <thead><tr><th>Tool</th><th>Description</th><th>Section</th><th>Links</th><th>Last Updated</th></tr></thead>
      <tbody data-rows>{rows}</tbody>
    </table>
  </div>
  <p class="empty" data-empty hidden>Nothing matches that filter. <a href="{e(SITE['repo'])}/pulls" target="_blank" rel="noopener">Suggest a tool?</a></p>
  <nav class="pager" aria-label="More categories">
    <a class="card" href="/{prev_c['slug']}/"><span class="muted">Previous</span><strong>{e(prev_c['title'])}</strong></a>
    <a class="card next" href="/{next_c['slug']}/"><span class="muted">Next</span><strong>{e(next_c['title'])}</strong></a>
  </nav>
</div>"""
    path = f"/{cat['slug']}/"
    desc = f"{len(tools)} {cat['title']} tools and resources: {cat['description']}"
    write(path, layout(path, cat["title"], desc, body, hero, "category",
                       crumbs=[("Infosec House", "/"), ("Categories", "/#categories"), (cat["title"], path)]))


def social_row():
    return "".join(
        f'<a href="{e(s["href"])}" target="_blank" rel="noopener" aria-label="{e(s["label"])}">'
        f'{icon("", "icon", SOCIAL_ICONS.get(s["label"], ICONS["external"]))}</a>'
        for s in SITE["social"])


def build_markdown_page(name, slug):
    meta, src = frontmatter((CONTENT / name).read_text(encoding="utf-8"))
    src = re.sub(r"^# .*\n+", "", src)
    title = meta.get("title", slug.title())
    path = f"/{slug}/"
    hero = page_hero([("Infosec House", "/")], title, e(meta.get("description", "")))
    rendered = markdown(src, allow_html=True).replace("{{social}}", social_row())
    body = f'<div class="wrap section"><article class="prose prose-{slug}">{rendered}</article></div>'
    write(path, layout(path, title, meta.get("description") or title, body, hero,
                       crumbs=[("Infosec House", "/"), (title, path)]))


def build_blog():
    posts = []
    for f in sorted((CONTENT / "blog").glob("*.md"), reverse=True):
        meta, src = frontmatter(f.read_text(encoding="utf-8"))
        slug = f.stem
        date = meta.get("date", slug[:10])
        text = re.sub(r"<[^>]+>|[#*`>\[\]]|\(http[^)]*\)", "", src)
        posts.append({"slug": slug, "title": meta.get("title", slug), "date": date,
                      "author": meta.get("author", ""), "excerpt": " ".join(text.split())[:220], "src": src})
    for p in posts:
        path = f"/blog/{p['slug']}/"
        hero = page_hero([("Infosec House", "/"), ("Blog", "/blog/")], p["title"],
                         f'<time datetime="{e(p["date"])}">{e(pretty_date(p["date"]))}</time> · {e(p["author"])}')
        body = f'<div class="wrap section"><article class="prose">{markdown(p["src"])}</article></div>'
        write(path, layout(path, p["title"], p["excerpt"], body, hero,
                           crumbs=[("Infosec House", "/"), ("Blog", "/blog/"), (p["title"], path)]))
    cards = "".join(
        f'<a class="card post-card" href="/blog/{p["slug"]}/"><time class="muted">{e(pretty_date(p["date"]))}</time>'
        f'<h3>{e(p["title"])}</h3><p>{e(p["excerpt"])}…</p><span class="more">Read post {icon("arrow")}</span></a>' for p in posts)
    hero = page_hero([("Infosec House", "/")], "Blog", "Write-ups, tutorials, and news from Infosec House.")
    write("/blog/", layout("/blog/", "Blog", "Write-ups, tutorials, and news from Infosec House.",
                           f'<div class="wrap section"><div class="grid post-grid">{cards}</div></div>', hero))
    return posts


def pretty_date(s):
    try:
        return dt.date.fromisoformat(s).strftime("%B %-d, %Y")
    except ValueError:
        return s


def build_404():
    hero = page_hero([("Infosec House", "/")], "404: Not found", "That page has moved or never existed. Try searching instead.")
    body = '<div class="wrap section"><p><a class="btn btn-brand" href="/">Back to all categories</a></p></div>'
    (DIST / "404.html").write_text(layout("/404", "Not found", "Page not found", body, hero), encoding="utf-8")


def build_sponsors(cats):
    """List current (grouped by tier) and past sponsors, derived from the tiered config."""
    s = SITE.get("sponsors", {})
    cat_titles = {c["slug"]: c["title"] for c in cats}

    def perks(sp, tier):
        """What this sponsor gets, cumulative to its tier."""
        out = []
        if sp.get("tool"):
            out.append(f'Badge on <a href="/tools/{e(sp["tool"])}/">{e(sp.get("name", sp["tool"]))}</a>')
        if TIER_RANK[tier] >= TIER_RANK["silver"] and sp.get("category"):
            out.append(f'{e(cat_titles.get(sp["category"], sp["category"].title()))} banner')
        if TIER_RANK[tier] >= TIER_RANK["gold"]:
            out.append("Social shout-out")
        if TIER_RANK[tier] >= TIER_RANK["diamond"]:
            out.append("Footer, site-wide")
        return out

    def card(sp, where, muted=False):
        logo = sp.get("logo") or sp.get("banner")
        mark = (f'<img src="{e(logo)}" alt="{e(sp["name"])}" loading="lazy">'
                if logo else f'<span class="sponsor-name">{e(sp["name"])}</span>')
        link = mark if (muted or not sp.get("url")) else sponsor_a(sp["url"], "sponsors-page", mark)
        where_html = ('<p class="cat-sample">' + " · ".join(where) + "</p>") if where else ""
        desc = f'<p class="cat-desc">{e(sp["description"])}</p>' if sp.get("description") else ""
        return (f'<div class="card sponsor-card{" is-past" if muted else ""}">'
                f'<div class="sponsor-logo">{link}</div>{desc}{where_html}</div>')

    sections = ""
    for tier in reversed(TIERS):  # diamond first
        entries = s.get(tier, [])
        if not entries:
            continue
        cards = "".join(card(sp, perks(sp, tier)) for sp in entries)
        sections += (f'<section class="wrap section"><h2>{tier.title()} sponsors</h2>'
                     f'<div class="grid sponsor-grid">{cards}</div></section>')

    past = s.get("past", [])
    past_html = "".join(card(p, [p["note"]] if p.get("note") else [], muted=True) for p in past)

    if not sections:
        sections += ('<section class="wrap section"><div class="sheet-empty">' + icon("heart", "icon stat-icon")
                     + '<div><strong>This could be you</strong><p class="muted">Infosec House is community-run and '
                     'sponsor-supported. Be the first sponsor featured here.</p>'
                     '<a class="btn btn-brand btn-sm" href="/support-us/">Become a sponsor</a></div></div></section>')
    if past_html:
        sections += f'<section class="wrap section"><h2>Past sponsors</h2><p class="muted">Thanks to those who have supported Infosec House.</p><div class="grid sponsor-grid">{past_html}</div></section>'

    cta = ('<section class="wrap section"><div class="cta-band"><div><h2>Sponsor Infosec House</h2>'
           '<p>Reach a focused audience of security practitioners and support an open, community-run project.</p></div>'
           '<div class="cta-actions"><a class="btn btn-brand" href="/support-us/">' + icon("heart") + 'View sponsorship</a></div></div></section>')

    hero = page_hero([("Infosec House", "/")], "Sponsors",
                     "The companies that help keep Infosec House free, open, and community-run.")
    write("/sponsors/", layout("/sponsors/", "Sponsors",
                               "Companies sponsoring Infosec House, a community-run catalog of security tools.",
                               sections + cta, hero))


# --------------------------------------------------------------------------- tool pages

def norm_url(url):
    return url.lower().rstrip("/").replace("://www.", "://")


def assign_tool_pages(cats):
    """One page per unique tool URL, so a tool listed in several categories shares a page."""
    by_url, used = {}, set()
    for c in cats:
        for t in c["_tools"]:
            key = ("repo:" + t["repo"].lower()) if t.get("repo") else norm_url(t["url"])
            page = by_url.get(key)
            if page is None:
                slug = slugify(t["name"]) or "tool"
                if slug in used:
                    slug = f"{slug}-{c['slug']}"
                base, n = slug, 2
                while slug in used:
                    slug, n = f"{base}-{n}", n + 1
                used.add(slug)
                page = {"slug": slug, "path": f"/tools/{slug}/", "entries": []}
                by_url[key] = page
                TOOL_PAGES.append(page)
            page["entries"].append((t, c))
            t["_page"] = page["path"]
    sheet_dir = CONTENT / "cheatsheets"
    known = {p["slug"] for p in TOOL_PAGES}
    for f in sorted(sheet_dir.glob("*.md")) if sheet_dir.exists() else []:
        if f.name.startswith("_") or f.name == "README.md":
            continue
        if f.stem not in known:
            sys.exit(f"content/cheatsheets/{f.name}: no tool with slug '{f.stem}' (see the URL /tools/<slug>/)")
        SHEETS[f"/tools/{f.stem}/"] = f


SHEET_TEMPLATE = (CONTENT / "cheatsheets" / "_template.md")


def build_tool_page(page):
    t, cat = page["entries"][0]
    url, repo, host = t["url"], t.get("repo"), host_of(t["url"])
    gh = GITHUB.get(repo, {}) if repo else {}

    # Actions: where the tool lives
    if ".onion" in url:
        actions = [f'<a class="btn btn-brand btn-sm" href="{e(url)}" target="_blank" rel="noopener noreferrer nofollow">{icon("onion")}Open onion service</a>']
    elif host == "github.com":
        actions = [f'<a class="btn btn-brand btn-sm" href="{e(url)}" target="_blank" rel="noopener noreferrer nofollow">{icon("github")}View on GitHub</a>']
    else:
        actions = [f'<a class="btn btn-brand btn-sm" href="{e(url)}" target="_blank" rel="noopener noreferrer nofollow">{icon("globe")}Visit website</a>']
    if repo and host != "github.com":
        actions.append(f'<a class="btn btn-ghost btn-sm" href="https://github.com/{e(repo)}" target="_blank" rel="noopener">{icon("github")}GitHub</a>')
    for l in t.get("links", []):
        if l["url"] != url:
            actions.append(f'<a class="btn btn-ghost btn-sm" href="{e(l["url"])}" target="_blank" rel="noopener noreferrer nofollow">'
                           f'{icon("onion" if ".onion" in l["url"] else "external")}{e(l["label"])}</a>')

    status = repo_status(repo) if repo else ""
    stats = '<div class="hero-stats">'
    if status:
        stats += f'<div><strong class="stat-pill">{status}</strong><span>Last updated</span></div>'
    if "stars" in gh:
        stats += f'<div><strong>★ {short_num(gh["stars"])}</strong><span>GitHub stars</span></div>'
    stats += f'<div><strong>{len(page["entries"])}</strong><span>{"Listing" if len(page["entries"]) == 1 else "Listings"}</span></div></div>'
    hero = page_hero([("Infosec House", "/"), (cat["title"], f"/{cat['slug']}/")], t["name"],
                     md_inline(t.get("description", "")), stats + f'<div class="hero-actions">{"".join(actions)}</div>')

    # Category safety notices carry over to the tool page
    notices = "".join(callout(n["type"], md_inline(n["text"])) for n in cat.get("notices", []))
    for sec in cat["sections"]:
        if sec["title"] == t["_section"]:
            notices += "".join(callout(n["type"], md_inline(n["text"])) for n in sec.get("notices", []))

    # Cheat sheet
    sheet_file = SHEETS.get(page["path"])
    new_url = (SITE["repo"] + f"/new/main?filename=content/cheatsheets/{page['slug']}.md&value="
               + quote(SHEET_TEMPLATE.read_text(encoding="utf-8").replace("{{name}}", t["name"]) if SHEET_TEMPLATE.exists() else ""))
    if sheet_file:
        meta, src = frontmatter(sheet_file.read_text(encoding="utf-8"))
        byline = " · ".join(x for x in (meta.get("author") and f"By {meta['author']}", meta.get("updated") and f"Updated {pretty_date(meta['updated'])}") if x)
        edit = SITE["repo"] + f"/edit/main/content/cheatsheets/{page['slug']}.md"
        sheet = (f'<div class="sheet-head"><h2 id="cheat-sheet">Cheat sheet</h2>'
                 f'<a class="btn btn-ghost btn-sm" href="{e(edit)}" target="_blank" rel="noopener">{icon("edit")}Improve</a></div>'
                 + (f'<p class="muted sheet-byline">{e(byline)}</p>' if byline else "")
                 + f'<article class="prose sheet">{markdown(src)}</article>')
    else:
        sheet = (f'<div class="sheet-head"><h2 id="cheat-sheet">Cheat sheet</h2></div>'
                 f'<div class="sheet-empty">{icon("code", "icon stat-icon")}<div><strong>No cheat sheet yet</strong>'
                 f'<p class="muted">Cheat sheets are community-written markdown: install steps, common usage, and links to official docs. '
                 f'Know {e(t["name"])} well? Add one in a single pull request.</p>'
                 f'<a class="btn btn-brand btn-sm" href="{e(new_url)}" target="_blank" rel="noopener">{icon("plus")}Write the cheat sheet</a>'
                 f'</div></div>')

    # Sidebar: details + listings + related
    rows = [("Website" if ".onion" not in url else "Address", f'<a href="{e(url)}" target="_blank" rel="noopener noreferrer nofollow">{e(host)}</a>')]
    if repo:
        rows.append(("Repository", f'<a href="https://github.com/{e(repo)}" target="_blank" rel="noopener">{e(repo)}</a>'))
    if gh.get("pushed"):
        rows.append(("Last updated", f'{e(pretty_date(gh["pushed"]))}'))
    if gh.get("archived"):
        rows.append(("Status", '<span class="pill pill-archived">Archived</span>'))
    if t.get("tags"):
        rows.append(("Tags", " ".join(f'<span class="pill">{e(x)}</span>' for x in t["tags"])))
    details = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    listings = "".join(
        f'<li><a href="/{c["slug"]}/#{x["_anchor"]}">{e(c["title"])}</a>'
        f'<span class="muted">{e(" › ".join(v for v in (x["_section"], x["_group"]) if v))}</span></li>'
        for x, c in page["entries"])
    related = [x for x in cat["_tools"] if x["_group"] == t["_group"] and x["_section"] == t["_section"] and x["_page"] != page["path"]][:8]
    related_html = "".join(
        f'<a class="related" href="{x["_page"]}"><strong>{e(x["name"])}</strong><span class="muted">{e(x.get("description", ""))}</span></a>'
        for x in related)
    edit_entry = SITE["edit_base"] + cat["slug"] + ".json"

    body = f"""<div class="wrap section tool-layout">
  <div class="tool-main">{notices}{sheet}</div>
  <aside class="tool-side">
    <div class="card side-card"><h3>Details</h3><dl class="details">{details}</dl>
      <a class="side-link" href="{e(edit_entry)}" target="_blank" rel="noopener">{icon("edit")}Edit this entry</a>
      <a class="side-link" href="{e(SITE['repo'])}/issues/new?title={quote('Broken or incorrect link: ' + t['name'])}" target="_blank" rel="noopener">{icon("alert")}Report a problem</a></div>
    <div class="card side-card"><h3>Listed in</h3><ul class="listings">{listings}</ul></div>
    {f'<div class="card side-card"><h3>Related tools</h3>{related_html}</div>' if related_html else ""}
  </aside>
</div>"""
    plain = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t.get("description", ""))
    desc = f"{t['name']}: {plain} Listed in {cat['title']} on Infosec House."
    write(page["path"], layout(page["path"], t["name"], desc, body, hero, "tool",
                               crumbs=[("Infosec House", "/"), (cat["title"], f"/{cat['slug']}/"), (t["name"], page["path"])]))


# --------------------------------------------------------------------------- api / db / seo

def tool_record(t, cat):
    return {"name": t["name"], "url": t["url"], "description": t.get("description", ""),
            "category": cat["slug"], "section": t["_section"], "group": t["_group"],
            "repo": t.get("repo"), "links": t.get("links", []), "tags": t.get("tags", []),
            "path": t["_page"], "listing": f"/{cat['slug']}/#{t['_anchor']}"}


def build_api(cats):
    api = DIST / "api"
    (api / "categories").mkdir(parents=True, exist_ok=True)
    index = []
    all_tools = []
    search = []
    for c in cats:
        recs = [tool_record(t, c) for t in c["_tools"]]
        all_tools += recs
        index.append({"slug": c["slug"], "title": c["title"], "description": c["description"],
                      "group": c["_group"], "tools": len(recs), "path": f"/{c['slug']}/"})
        (api / "categories" / f"{c['slug']}.json").write_text(
            json.dumps({**{k: v for k, v in c.items() if not k.startswith("_")}, "tools": recs}, ensure_ascii=False), encoding="utf-8")
        search.append(["c", c["title"], c["description"], c["slug"], c["title"], "", f"/{c['slug']}/"])
        for r, t in zip(recs, c["_tools"]):
            where = " › ".join(x for x in (r["section"], r["group"]) if x)
            search.append(["t", r["name"], r["description"], r["repo"] or host_of(r["url"]), c["title"], where, r["path"]])
    (api / "categories.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    (api / "tools.json").write_text(json.dumps({"generated": TODAY.isoformat(), "count": len(all_tools), "tools": all_tools}, ensure_ascii=False), encoding="utf-8")
    (api / "search.json").write_text(json.dumps(search, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return all_tools


def build_seo(paths):
    urls = "".join(f"<url><loc>{SITE['url']}{p}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>" for p in paths)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n", encoding="utf-8")



WRITTEN = []


def write(path, content):
    target = DIST / path.strip("/") / "index.html" if path != "/" else DIST / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    WRITTEN.append(path)


def last_updated():
    """The build date, shown as the home-page 'Updated' label."""
    return TODAY.strftime("%B %-d, %Y")


def main():
    global CATS, TOTAL_TOOLS, BUILD_ID, LAST_UPDATED
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(STATIC, DIST)
    for f in ("styles.css", "app.js"):
        shutil.copy(SRC / f, DIST / f)

    gh_path = DATA / "github.json"
    GITHUB.update(json.loads(gh_path.read_text(encoding="utf-8")) if gh_path.exists() else {})
    resolve_sponsors()
    CATS = load_categories()
    assign_tool_pages(CATS)
    TOTAL_TOOLS = sum(len(c["_tools"]) for c in CATS)
    BUILD_ID = dt.datetime.now().strftime("%Y%m%d%H%M")
    LAST_UPDATED = last_updated()

    build_home(CATS)
    for i, c in enumerate(CATS):
        build_category(c, i, CATS)
    for page in TOOL_PAGES:
        build_tool_page(page)
    for name, slug in (("about.md", "about"), ("support-us.md", "support-us"), ("contribute.md", "contribute"), ("partnership.md", "partnership")):
        build_markdown_page(name, slug)
    build_blog()
    build_404()
    build_sponsors(CATS)
    build_api(CATS)
    build_seo(WRITTEN)
    print(f"built {len(WRITTEN)} pages ({len(TOOL_PAGES)} tool pages, {len(SHEETS)} cheat sheets), "
          f"{TOTAL_TOOLS} tools, {len(CATS)} categories -> dist/")

    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
        print("serving http://localhost:8788")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8788), handler).serve_forever()


CATS, TOTAL_TOOLS, BUILD_ID, LAST_UPDATED = [], 0, "", ""
GITHUB = {}
TOOL_PAGES = []
SHEETS = {}

# Sponsor tiers, lowest to highest. Each tier includes every perk of the tiers below it:
#   bronze  -> "Sponsor" badge on the sponsor's own tool listing
#   silver  -> + a banner at the top of a category page
#   gold    -> + a social media shout-out (off-site)
#   diamond -> + the sponsor's logo in the site footer, on every page
TIERS = ["bronze", "silver", "gold", "diamond"]
TIER_RANK = {t: i for i, t in enumerate(TIERS)}
# Derived placements, filled by resolve_sponsors() in main().
SPONSOR_FOOTER = []       # list of diamond sponsors (logo in footer)
SPONSOR_BANNERS = {}      # category slug -> sponsor (silver+)
SPONSOR_BADGES = {}       # tool slug -> sponsor (all tiers)


def resolve_sponsors():
    """Turn the tiered sponsors config into concrete placements, granting every lower perk."""
    SPONSOR_FOOTER.clear(); SPONSOR_BANNERS.clear(); SPONSOR_BADGES.clear()
    conf = SITE.get("sponsors", {})
    for tier in TIERS:
        for s in conf.get(tier, []):
            rank = TIER_RANK[tier]
            s = {**s, "tier": tier, "rank": rank}
            if s.get("tool"):                                        # bronze and up: badge
                SPONSOR_BADGES[s["tool"]] = s
            if rank >= TIER_RANK["silver"]:                          # silver and up: banner
                if s.get("category") and s.get("banner"):
                    SPONSOR_BANNERS[s["category"]] = s
                else:
                    print(f"  warning: {tier} sponsor {s.get('name')!r} needs 'category' and 'banner' for its banner")
            if rank >= TIER_RANK["diamond"]:                         # diamond: footer logo
                if s.get("logo"):
                    SPONSOR_FOOTER.append(s)
                else:
                    print(f"  warning: diamond sponsor {s.get('name')!r} needs 'logo' for the footer")
            if s.get("tool") is None:
                print(f"  warning: {tier} sponsor {s.get('name')!r} has no 'tool' slug, so no badge/catalog link")

if __name__ == "__main__":
    main()
