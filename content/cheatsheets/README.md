# Cheat sheets

One markdown file per tool, named after the tool's **page slug**, the last part of its URL on the site. The cheat sheet for `https://infosec.house/tools/nmap/` is `nmap.md`. If you're unsure of a tool's slug, open its page and look at the address bar.

The **Write the cheat sheet** button on each tool page opens GitHub's new-file editor with the filename and `_template.md` prefilled.

## Writing one

Copy the template and fill it in:

```bash
cp _template.md <slug>.md
```

Frontmatter:

```markdown
---
author: your-github-handle
updated: 2026-10-16
---
```

Then write sections with `##` headings. See the [full guide in CONTRIBUTING.md](../../CONTRIBUTING.md#write-a-cheat-sheet).

## Guidelines

- **Documented, upstream usage only**, with links to the official docs.
- **Authorized/test targets only** in examples: the tool's own test host (e.g. `scanme.nmap.org`), or reserved ranges like `192.0.2.0/24` and `example.com`. Never a real third-party host.
- **Add a safety note** (`> [!WARNING]` / `> [!NOTE]`) to anything that scans, deletes, or blocks. See `nmap.md` and `masscan.md`.
- **Fenced code blocks** with a language tag (` ```bash `) get a Copy button automatically.
- **Tables** are fine; escape a literal pipe inside a cell as `\|`.
- Link to related sheets with a site-relative link, e.g. `[Nmap cheat sheet](/tools/nmap/)`.

The build **fails** if a filename here doesn't match an existing tool slug, so typos are caught in the pull request check.

## Reference examples

`nmap.md`, `wireshark.md`, `tcpdump.md`, `zeek.md`, `suricata.md`, `masscan.md`. Match their tone, length, and structure.

Files starting with `_` (like `_template.md`) and this `README.md` are ignored by the build.
