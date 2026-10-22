---
title: Infosec House, Rebuilt
date: 2026-10-17
author: Admin
tags: release, update
---

Infosec House has been rebuilt from the ground up. Same mission, over a thousand curated offensive and defensive security tools organized by discipline, but a faster site that is easier to search, easier to read, and much easier to contribute to. Here is what changed.

## Search that actually finds things

Hit `/` or Cmd/Ctrl+K from any page and start typing. Search runs instantly across every tool, repo, and category, with the matches highlighted as you go. No page reloads, no waiting.

## A page for every tool

Every tool now has its own page. Click a tool's name, or anywhere on its row, and you get the description, where it lives, the categories it is listed in, related tools, and a cheat sheet section. It is a real landing spot you can link to and share.

## Community cheat sheets

Each tool page can hold a short, practical cheat sheet: install steps, common usage, and links to the official docs. The first batch covers the core network tools (Nmap, Wireshark, tcpdump, Zeek, Suricata, and masscan), and anyone can add more. Code blocks come with a copy button, and there is a one-click "Write the cheat sheet" button that opens a ready-to-fill template.

## See what is maintained at a glance

Repo-backed tools now show a "last updated" badge, green if the project was touched recently, red if it has gone quiet or been archived. Dead and deleted repos get flagged automatically, which keeps the catalog honest about what is still alive. Every row also shows clear Website, GitHub, and TOR links.

## Cleaner browsing

Tools are sorted alphabetically within each category, every category has section tabs you can jump straight to, and there is a filter box on every page. We also went through the whole catalog and cleaned up duplicates and dozens of broken or mislabeled links along the way.

## Open data and a public API

Under the hood, the catalog is now plain data in a public repository. That powers a read-only JSON API at `/api/` for anyone who wants to build on top of it, and it means adding or fixing a tool is a small edit instead of a chore. The whole site is static, so it loads fast and stays cheap to run.

## Easier to contribute

Because everything is open data, adding a tool, writing a cheat sheet, or fixing a link is a single pull request you can make right from GitHub. There is a new [Contribute](/contribute/) page that walks you through it, plus issue templates for suggesting a tool or reporting a broken link. If it saves you time, help us keep it current.

## Thanks

Infosec House is community-run and sponsor-supported. Thanks to everyone who has contributed tools, reported dead links, and helped out over the years, and to our sponsors for keeping the lights on. Browse around, and if something is missing, you know where the pull request button is.
