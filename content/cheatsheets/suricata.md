---
author: Infosec House
updated: 2026-10-16
---

> [!NOTE]
> Run Suricata on networks you own or are authorized to monitor. In IPS (inline) mode it can drop traffic, so test rules in IDS mode first and roll out blocking carefully.

## Overview

Suricata is a high-performance open-source IDS, IPS, and network security monitor. It inspects traffic against signature rules to raise alerts (IDS), can block matching traffic inline (IPS), and, like Zeek, writes structured protocol logs and extracts files. It's multi-threaded, understands many application protocols, and reads the same rule format used across the industry.

Common uses: alerting on known-bad traffic with community rulesets, blocking it inline at a gateway, and producing `eve.json` metadata for a SIEM.

## Install

```bash
# Debian / Ubuntu (official PPA has current versions)
sudo add-apt-repository ppa:oisf/suricata-stable
sudo apt update && sudo apt install suricata

# Fedora / RHEL
sudo dnf install suricata

# macOS (Homebrew)
brew install suricata

suricata --build-info | head        # confirm features (NFQ, etc.) are compiled in
```

Main config lives at `/etc/suricata/suricata.yaml`. Set your `HOME_NET` (the networks you're protecting) there before going live.

## Rules and updates

Suricata ships almost no rules; you pull them in. `suricata-update` fetches and manages rulesets (ET Open by default):

```bash
sudo suricata-update                         # fetch/update the default ruleset
sudo suricata-update list-sources            # available rule sources
sudo suricata-update enable-source et/open   # Emerging Threats open ruleset
sudo suricata-update                         # re-run to apply
```

Rules end up in `/var/lib/suricata/rules/suricata.rules`.

## Testing config and rules

Always validate before restarting a live sensor:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml -v   # test config + rules, then exit
```

## Reading a pcap offline

Great for tuning rules and checking a capture against your ruleset:

```bash
mkdir out
suricata -r capture.pcap -l out/        # run rules over a pcap, logs into out/
ls out/
# eve.json  fast.log  stats.log  suricata.log
```

## IDS mode (alerting) on live traffic

```bash
# AF_PACKET on a monitoring interface (modern default on Linux)
sudo suricata -c /etc/suricata/suricata.yaml -i eth0

# As a managed service
sudo systemctl enable --now suricata
sudo systemctl status suricata
```

## IPS mode (inline blocking)

Inline mode requires routing traffic through Suricata via NFQUEUE (iptables/nftables) or AF_PACKET bridging. NFQUEUE example:

```bash
# Send forwarded traffic to queue 0
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0

# Run Suricata reading that queue
sudo suricata -c /etc/suricata/suricata.yaml -q 0
```

Rules with a `drop` action then actually block. Validate rules in IDS mode first; a bad inline rule can take down legitimate traffic.

## Output: fast.log and eve.json

- **`fast.log`**: one-line, human-readable alerts, good for a quick look:

```bash
tail -f /var/log/suricata/fast.log
```

- **`eve.json`** is the real output: JSON events for alerts, plus flow, DNS, HTTP, TLS, and file records. This is what you ship to a SIEM.

```bash
# Alert signatures seen, most frequent first
jq -r 'select(.event_type=="alert") | .alert.signature' /var/log/suricata/eve.json \
  | sort | uniq -c | sort -rn | head

# TLS SNI values
jq -r 'select(.event_type=="tls") | .tls.sni' /var/log/suricata/eve.json | sort -u

# Alerts involving one host
jq 'select(.event_type=="alert" and .src_ip=="192.0.2.10")' /var/log/suricata/eve.json
```

## Rule syntax (reading and writing)

A rule is: **action** · **header** (proto, source, direction, destination) · **options** in parentheses.

```text
alert http $HOME_NET any -> $EXTERNAL_NET any ( \
    msg:"Example suspicious user-agent"; \
    flow:established,to_server; \
    http.user_agent; content:"BadAgent/1.0"; \
    classtype:bad-unknown; sid:1000001; rev:1; )
```

- `action`: `alert`, `drop` (IPS), `reject`, `pass`
- `flow`: direction/state, e.g. `established,to_server`
- sticky buffers like `http.user_agent`, `http.uri`, `dns.query`, `tls.sni` scope the match
- `content:"..."` is the match; `sid` must be unique; bump `rev` when you edit

Test a custom rule over a pcap:

```bash
suricata -S my.rules -r capture.pcap -l out/
grep 1000001 out/fast.log
```

## Tips

- Set `HOME_NET` correctly. Many rules fire based on direction relative to it.
- Run `suricata -T` before every restart; a syntax error otherwise leaves the sensor down.
- Keep custom rules in their own file with `sid`s from the 1,000,000+ local range.
- `eve.json` is the integration point for Elastic (the ELK/EveBox stack), Splunk, or `jq`.
- IPS mode: stage as IDS, confirm no false positives on your traffic, then switch chosen rules to `drop`.
- Run Suricata and Zeek together: signature alerts from one, full protocol logs from the other.

## References

- [Suricata documentation](https://docs.suricata.io/)
- [Rules format](https://docs.suricata.io/en/latest/rules/intro.html)
- [suricata-update](https://docs.suricata.io/en/latest/rule-management/suricata-update.html)
- [eve.json / EVE output](https://docs.suricata.io/en/latest/output/eve/eve-json-format.html)
- [Source on GitHub](https://github.com/OISF/suricata)
