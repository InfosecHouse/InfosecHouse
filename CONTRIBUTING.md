# Contributing to Infosec House

Thanks for helping keep Infosec House useful. The whole catalog is plain data in this repo, so most contributions are a small edit and a pull request, with no build tools or web development needed.

There are four common contributions:

- [Add a new tool](#add-a-new-tool)
- [Write a cheat sheet](#write-a-cheat-sheet)
- [Report or fix a broken link](#report-or-fix-a-broken-link)
- [Add a new category](#add-a-new-category)

You can do any of them entirely from the GitHub website. Every tool page and category page also has **Suggest a tool**, **Edit this entry**, and (where relevant) **Improve** / **Write the cheat sheet** buttons that open the right file for you.

## Ground rules

- **Only legitimate, documented tools and resources.** No malware droppers dressed up as tools, no "download" links to pirated software, no affiliate-spam.
- **Link to the real source.** Prefer the project's own homepage or repository over a mirror or a blog about it.
- **One topic per pull request.** A PR that adds one tool, or one cheat sheet, is faster to review than a mixed bag.
- **Be accurate.** A wrong flag in a cheat sheet or a mislabeled tool is worse than nothing.

---

## Add a new tool

Tools live in `data/categories/<category>.json`, one file per category. Each file has `sections`, each section has `groups`, and each group has a list of `tools`.

1. Pick the category file that fits, e.g. `data/categories/recon.json`.
2. Find the section and group your tool belongs in (or add a new group).
3. Add an entry to that group's `tools` list:

```json
{
  "name": "Nuclei",
  "url": "https://github.com/projectdiscovery/nuclei",
  "description": "Fast, template-based vulnerability scanner.",
  "repo": "projectdiscovery/nuclei"
}
```

### Fields

| Field | Required | What it is |
| --- | --- | --- |
| `name` | yes | The tool's name, shown in the table and as the page title |
| `url` | yes | Where the tool lives. Must start with `https://`|
| `description` | yes | One sentence, ending in a period. Say what it does, not that it's "the best" |
| `repo` | yes | `"owner/name"` (not the full URL). Turns on the **last updated** pill and star count |
| `links` | optional | Extra labeled links: `[{"label": "Android", "url": "https://..."}]` |
| `tags` | optional | Currently `["tor"]` marks onion services |

### Guidelines

- **`name`**: match the project's own capitalization (`sqlmap`, not `SQLMap`).
- **`url`**: if the project is on GitHub, point `url` there and also set `repo`. If it has a dedicated homepage, point `url` at the homepage and still set `repo`, and the page shows both.
- **`description`**: keep it to one factual sentence. Skip marketing ("powerful", "ultimate") unless it's part of the name.
- **`repo`**: copy it from the GitHub URL. `https://github.com/projectdiscovery/nuclei` → `"projectdiscovery/nuclei"`.
- **Alphabetical order** inside a group is appreciated but not enforced.

---

## Write a cheat sheet

Each tool can have a cheat sheet: a short, practical reference shown on its page at `/tools/<slug>/`. They're markdown files in `content/cheatsheets/`, named after the tool's page slug.

**The slug is the last part of the tool's URL on the site.** The cheat sheet for `https://infosec.house/tools/nmap/` is `content/cheatsheets/nmap.md`. If you're unsure of the slug, open the tool's page and look at the address bar.

### Easiest way

On any tool page without a cheat sheet, click **Write the cheat sheet**. It opens GitHub's new-file editor with the filename and the template already filled in. Write, then "Propose new file" to open a pull request.

### By hand

Copy the template and fill it in:

```bash
cp content/cheatsheets/_template.md content/cheatsheets/<slug>.md
```

A cheat sheet looks like this:

```markdown
---
author: your-github-handle
updated: 2026-10-16
---

## Overview

What the tool is for, in a sentence or two.

## Install

The official install method. Link to the upstream install docs.

## Common usage

Copyable examples, each with a one-line explanation.

## References

- Official documentation
- Source repository
```

### What makes a good cheat sheet

- **Stick to documented, upstream usage.** Pull commands from the tool's own docs, and link to them.
- **Authorized targets only.** Use the tool's own test endpoint where it has one (Nmap has `scanme.nmap.org`), or the reserved documentation ranges (`192.0.2.0/24`, `example.com`). Never put a real third-party host in an example.
- **Add a safety note where it matters.** Start destructive, scanning, or inline-blocking tools with a `> [!WARNING]` or `> [!NOTE]` about authorization. See `nmap.md` or `masscan.md` for the pattern.
- **Use fenced code blocks with a language tag** (` ```bash `). They get a language label and a Copy button automatically.
- **Tables are fine** for option references. Escape a literal pipe inside a cell as `\|`.
- **Link to related cheat sheets** with a site-relative link, e.g. `[Nmap cheat sheet](/tools/nmap/)`.

The existing network cheat sheets (`nmap.md`, `wireshark.md`, `tcpdump.md`, `zeek.md`, `suricata.md`, `masscan.md`) are the reference for tone, length, and structure.

### Frontmatter

| Field | What it is |
| --- | --- |
| `author` | Your GitHub handle (or name). Shown as a byline |
| `updated` | `YYYY-MM-DD` of your last edit. Shown next to the byline |

The build **fails** if a cheat sheet's filename doesn't match an existing tool slug, so a typo is caught in the PR check rather than shipping a dead file.

---

## Report or fix a broken link

- **Just reporting?** Open an [issue](https://github.com/InfosecHouse/InfosecHouse/issues/new) (or use **Report a problem** on the tool's page). Include the tool name and what's wrong.
- **Fixing it?** Edit the tool's entry in `data/categories/<category>.json`: update the `url`, or remove the entry if the project is gone. If a repo was renamed, update both `url` and `repo`.

The weekly GitHub job flags repos it can't reach as **Repo not found** on their pages, which is a good place to look for dead links.

---

## Add a new category

1. Create `data/categories/<slug>.json`. The `slug` is lowercase, words separated by hyphens, and must match the filename:

```json
{
  "slug": "my-category",
  "title": "My Category",
  "description": "One sentence shown under the title and on the home card.",
  "sections": [
    {
      "title": "First Section",
      "groups": [
        { "title": "A Group", "tools": [] }
      ]
    }
  ]
}
```

2. Add the slug to `data/site.json`: append it to `categories` (controls order) and to the right discipline in `groups` (Offensive / Defensive / Intel & Recon / Learning).

3. Add at least one tool so the category isn't empty.

Section and group `title` may be empty strings if a category doesn't need that level of nesting; the build handles it.

---

## How your change ships

1. You open a pull request.
2. The **Validate catalog** check rebuilds the site. If it's red, open the log; it names the problem.
3. A maintainer reviews and merges.
4. Cloudflare Pages rebuilds from `main` and the change is live within a minute or two.

No build artifacts are committed; `dist/` is generated. You only ever edit files in `data/`, or `content/`.

Thank you for contributing!
