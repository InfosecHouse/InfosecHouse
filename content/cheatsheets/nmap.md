---
author: Infosec House
updated: 2026-10-16
---

> [!WARNING]
> Only scan networks you own or have written permission to test. The Nmap project allows test scans against `scanme.nmap.org` (be gentle with it). The `192.0.2.0/24` range in these examples is reserved for documentation, so replace it with your own target.

## Overview

Nmap ("Network Mapper") is the standard open-source tool for network discovery and security auditing. It finds live hosts, open ports, the services and versions behind them, and the likely operating system. Its scripting engine (NSE) extends it with hundreds of checks. Administrators use it for inventory and change tracking, and testers use it to map an authorized scope.

## Install

```bash
# Debian / Ubuntu / Kali
sudo apt install nmap

# Fedora / RHEL
sudo dnf install nmap

# macOS (Homebrew)
brew install nmap

# Check the installed version
nmap --version
```

Windows installers (including the Zenmap GUI) are at [nmap.org/download](https://nmap.org/download.html).

Many scan types need raw packet access, so run them with `sudo` on Linux/macOS. Without root, Nmap falls back to a slower TCP connect scan (`-sT`).

## Target specification

```bash
nmap scanme.nmap.org              # single hostname
nmap 192.0.2.10                   # single IP
nmap 192.0.2.10-20                # range
nmap 192.0.2.0/24                 # CIDR block
nmap -iL targets.txt              # read targets from a file (one per line)
nmap 192.0.2.0/24 --exclude 192.0.2.1
nmap -sL 192.0.2.0/24             # list targets only, sends nothing to them
```

`-sL` is a good sanity check that your target list matches your authorized scope before you scan.

## Host discovery

```bash
nmap -sn 192.0.2.0/24             # ping sweep: which hosts are up, no port scan
nmap -Pn scanme.nmap.org          # skip discovery, treat host as up (for hosts that ignore ping)
nmap -PR -sn 192.0.2.0/24         # ARP discovery (fastest and most reliable on a local LAN)
nmap -n -sn 192.0.2.0/24          # skip reverse DNS lookups for speed
```

## Port scanning

```bash
sudo nmap -sS scanme.nmap.org     # TCP SYN scan (default when root): fast, half-open
nmap -sT scanme.nmap.org          # TCP connect scan (default without root)
sudo nmap -sU scanme.nmap.org     # UDP scan (slow; combine with --top-ports)
```

Choosing ports:

```bash
nmap -p 22,80,443 scanme.nmap.org # specific ports
nmap -p 1-1024 scanme.nmap.org    # range
nmap -p- scanme.nmap.org          # all 65,535 TCP ports
nmap -F scanme.nmap.org           # fast: top 100 ports
nmap --top-ports 1000 scanme.nmap.org
sudo nmap -sU --top-ports 50 scanme.nmap.org
```

Port states you'll see:

| State | Meaning |
| --- | --- |
| `open` | A service is accepting connections |
| `closed` | Reachable, but nothing listening |
| `filtered` | A firewall or filter is blocking the probe, so the state is unknown |
| `open\|filtered` | No response, common with UDP |

## Service, version, and OS detection

```bash
nmap -sV scanme.nmap.org          # identify service and version on open ports
sudo nmap -O scanme.nmap.org      # OS fingerprinting
sudo nmap -A scanme.nmap.org      # aggressive: -sV -O -sC --traceroute together
nmap -sV --version-intensity 2 scanme.nmap.org   # lighter version probing (0-9)
```

`-A` is convenient but noisy. On production networks, start with `-sV` and add the rest as needed.

## Nmap Scripting Engine (NSE)

```bash
nmap -sC scanme.nmap.org                      # default script set (same as --script=default)
nmap --script safe scanme.nmap.org            # scripts categorized as non-intrusive
nmap -p 443 --script ssl-enum-ciphers example.com   # TLS versions and cipher grades
nmap -p 443 --script ssl-cert example.com     # certificate details and expiry
nmap -p 80,443 --script http-title,http-headers scanme.nmap.org
nmap --script-help ssl-enum-ciphers           # what a script does before you run it
```

Scripts are grouped into categories (`default`, `safe`, `discovery`, `version`, `intrusive`, `vuln`, and others). Read a script's help and category before running it. Categories other than `default` and `safe` can be disruptive and are for explicitly authorized tests. The full list is at [nmap.org/nsedoc](https://nmap.org/nsedoc/).

## Timing and performance

```bash
nmap -T4 scanme.nmap.org          # faster timing template (good default on reliable networks)
nmap -T2 192.0.2.0/24             # slower, gentler on fragile devices
nmap --min-rate 500 192.0.2.0/24  # send at least 500 packets/second
nmap --max-retries 1 192.0.2.0/24
nmap --host-timeout 5m 192.0.2.0/24
```

Templates run from `-T0` (paranoid) to `-T5` (insane). `-T3` is the default. Avoid `-T5` on networks with printers, OT/ICS, or older embedded devices.

## Output

```bash
nmap -oN scan.txt scanme.nmap.org   # normal, human-readable
nmap -oX scan.xml scanme.nmap.org   # XML (for tools and reports)
nmap -oG scan.gnmap scanme.nmap.org # grepable
nmap -oA scan scanme.nmap.org       # all three: scan.nmap, scan.xml, scan.gnmap
nmap -v --reason --open scanme.nmap.org   # verbose, explain each state, show only open ports
```

Turn XML into an HTML report:

```bash
xsltproc scan.xml -o scan.html
```

Resume an interrupted scan that was saved with `-oN` or `-oG`:

```bash
nmap --resume scan.txt
```

## Common recipes

```bash
# Quick inventory of a subnet: who's up and what's listening on common ports
sudo nmap -sS -sV -T4 --top-ports 100 -oA inventory 192.0.2.0/24

# Full TCP sweep of a single host, then version-scan only the open ports
sudo nmap -p- -T4 --min-rate 1000 -oN allports.txt 192.0.2.10
sudo nmap -sV -sC -p 22,80,443 -oA detail 192.0.2.10

# Check TLS configuration on web servers
nmap -p 443 --script ssl-enum-ciphers,ssl-cert -oN tls.txt 192.0.2.0/24

# Compare two scans to spot changes (ndiff ships with Nmap)
ndiff yesterday.xml today.xml
```

## Tips

- Add `--reason` when results look wrong. It shows which response led to each port state.
- `-n` (no DNS) speeds up large scans noticeably.
- Hosts that block ICMP look "down". Retry with `-Pn` if you know they're up.
- UDP is slow by design. Scan a short `--top-ports` list rather than everything.
- Save everything with `-oA`. You'll want the XML later.
- Press `v` during a scan to raise verbosity, and any key for a progress estimate.

## References

- [Nmap Reference Guide](https://nmap.org/book/man.html) (the official man page)
- [Nmap Network Scanning](https://nmap.org/book/) (free online book by Nmap's author)
- [NSE script documentation](https://nmap.org/nsedoc/)
- [Port scanning legal issues](https://nmap.org/book/legal-issues.html)
- [Source on GitHub](https://github.com/nmap/nmap)
