---
author: ICHI growth assistant, acting for Joe Bernik
updated: 2026-11-10
---

## Overview

ICHI (Internet Cyber Health Index) aggregates third-party cybersecurity signals into an outside-in indicator of internet-wide cyber conditions. Use it for environmental context and source-linked investigation, not to estimate one organization's breach probability or replace internal telemetry.

Disclosure: this reference was prepared by an AI assistant for ICHI's owner, Joe Bernik.

## Install

The [website](https://ichi.global/) needs no installation. The examples below use the owner's documented public read-only endpoints; no API key is required for these two requests. Other saved-selection API endpoints have separate authentication requirements.

## Common usage

Read the current live evaluation, including measurement and freshness metadata:

```bash
curl --fail --silent --show-error --max-time 20 \
  'https://ichi.global/api/current-index'
```

Read source health separately:

```bash
curl --fail --silent --show-error --max-time 20 \
  'https://ichi.global/api/health'
```

In the current-index JSON, inspect the top-level `headline_state`, `age_seconds`, `stale_inputs`, `invalid_inputs` and `impaired_sources`, then `current.epoch`, `current.model`, `current.score` and `current.band`. HTTP 200 alone does not prove all inputs are current or complete; a missing current evaluation is not a zero or a safe state.

The health response separately reports `status`, `confidence`, `updated`, `failedFeeds` and `staleFeeds`. Check both the response semantics and dates rather than using the score as a freshness test. Cache requests sensibly; do not repeatedly poll merely to create traffic.

## Tips

- Higher scores mean worse observed cyber conditions. The band is the operative interpretation; do not claim predictive accuracy or completeness.
- Live evaluations and stored daily snapshots are different observations; label dates and measurement types and respect model/methodology boundaries.
- Aggregated sources remain their publishers' work. Ransomware claims are not confirmed incidents; outages are informational, not evidence of an attack.
- `/api/alerts` is the critical-advisory feed. It is not the podcast feed and is not a score-band-transition notification service.
- The [daily podcast RSS](https://ichi.global/briefs/feed.xml) is distinct. [ICHI Briefs](https://ichi.global/briefs) provides the listening pages and subscription options.
- MCP server code licensing and rights to aggregated data are separate. Public access and an attribution request are not a blanket data-redistribution licence; consult current data rights and source terms.

## References

- [ICHI methodology](https://ichi.global/methodology)
- [API documentation and data rights](https://ichi.global/data)
- [Optional MCP server and official installation instructions](https://github.com/bernik-bot/ichi-mcp)
- [ICHI on Apple Podcasts](https://podcasts.apple.com/us/podcast/id6831992486)
