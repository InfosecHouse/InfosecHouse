#!/usr/bin/env python3
"""Fetch last-updated dates (and, with a token, stars / archived status) for every GitHub repo in the catalog.

    GITHUB_TOKEN=ghp_xxx python3 scripts/enrich_github.py   # GraphQL: last push, stars, archived
    python3 scripts/enrich_github.py                         # no token: last commit date from public commit feeds

Writes data/github.json, which build.py uses to render "updated 3mo ago" and star counts
instead of hot-linking a shields.io badge per row. Runs daily in .github/workflows/enrich.yml;
to avoid a commit + rebuild every day, a repo's stored star count only changes when its push
date or archived status also changed, so quiet days leave the file untouched.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "github.json"
BATCH = 50


def repos():
    found = set()
    for f in (ROOT / "data" / "categories").glob("*.json"):
        cat = json.loads(f.read_text(encoding="utf-8"))
        for s in cat["sections"]:
            for g in s["groups"]:
                found.update(t["repo"] for t in g["tools"] if t.get("repo"))
    return sorted(found)


def graphql(token, query):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "infosec-house-enrich"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def from_feed(full):
    """Last commit date on the default branch via the public Atom feed (no API rate limit)."""
    req = urllib.request.Request(f"https://github.com/{full}/commits.atom", headers={"User-Agent": "infosec-house-enrich"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                m = re.search(r"<updated>(\d{4}-\d{2}-\d{2})", r.read().decode("utf-8", "replace"))
                return full, ({"pushed": m.group(1)} if m else None)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return full, {"missing": True}
            if err.code != 429:
                return full, None
            time.sleep(int(err.headers.get("Retry-After") or 0) or 10 * (attempt + 1))  # throttled: back off
        except OSError:
            return full, None
    return full, None


def enrich_without_token(all_repos, out):
    missing, failed = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for n, (full, info) in enumerate(pool.map(from_feed, all_repos), 1):
            if info is None:
                failed.append(full)  # keep whatever we had before
                continue
            # Keep stars/archived from an earlier token run; only refresh the date
            out[full] = {**{k: v for k, v in out.get(full, {}).items() if k != "missing"}, **info} \
                if not info.get("missing") else info
            if info.get("missing"):
                missing.append(full)
            if n % 100 == 0:
                print(f"{n}/{len(all_repos)}")
    if failed:
        print(f"{len(failed)} repos could not be fetched this run (kept previous data)")
    return missing


def main():
    token = os.environ.get("GITHUB_TOKEN")
    all_repos = repos()
    out = json.loads(OUT.read_text()) if OUT.exists() else {}
    if not token:
        print("GITHUB_TOKEN not set: fetching last-commit dates from public feeds (no stars/archived)")
        missing = enrich_without_token(all_repos, out)
        save(out, missing)
        return
    missing = []
    for i in range(0, len(all_repos), BATCH):
        chunk = all_repos[i:i + BATCH]
        fields = []
        for n, full in enumerate(chunk):
            owner, name = full.split("/", 1)
            fields.append(f'r{n}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) '
                          '{ nameWithOwner stargazerCount pushedAt isArchived }')
        res = graphql(token, "query {" + " ".join(fields) + "}")
        data = res.get("data") or {}
        for n, full in enumerate(chunk):
            node = data.get(f"r{n}")
            if node:
                prev = out.get(full, {})
                pushed = node["pushedAt"][:10]
                archived = node["isArchived"]
                # Hold the previous star count steady unless something meaningful changed
                # (push date, archived flag, or first time we've seen this repo). Routine
                # star wiggle alone then leaves github.json byte-identical, so the daily
                # run produces no commit and no needless Cloudflare rebuild.
                meaningful = prev.get("pushed") != pushed or prev.get("archived") != archived or "stars" not in prev
                entry = {"stars": node["stargazerCount"] if meaningful else prev["stars"],
                         "pushed": pushed, "archived": archived}
                if node["nameWithOwner"].lower() != full.lower():
                    entry["moved_to"] = node["nameWithOwner"]
                out[full] = entry
            else:
                out[full] = {"missing": True}
                missing.append(full)
        print(f"{min(i + BATCH, len(all_repos))}/{len(all_repos)}")
    save(out, missing)


def save(out, missing):
    OUT.write_text(json.dumps(dict(sorted(out.items())), indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}; {len(missing)} repos not found (deleted, renamed, or private):")
    for m in missing:
        print("  ", m)


if __name__ == "__main__":
    main()
