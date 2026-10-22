---
author: Infosec House
updated: 2026-10-16
---

> [!NOTE]
> Zeek is a passive monitor: it reads traffic and writes logs, it never sends packets. Run it on networks you own or are authorized to monitor, and treat its logs as sensitive, since they record who talked to whom.

## Overview

Zeek (formerly Bro) is an open-source network security monitor. Instead of matching packets against signatures, it parses protocols and writes rich, structured logs of what happened on the wire: every connection, DNS query, HTTP request, TLS handshake, file transfer, and more. Those logs are the backbone of a lot of threat-hunting and incident-response work. Zeek also has its own scripting language for custom detection logic.

It analyzes live traffic from a monitoring interface (a SPAN/mirror port or tap) or reads saved `.pcap` files offline.

## Install

```bash
# Debian / Ubuntu (official package repo)
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/ /' | \
  sudo tee /etc/apt/sources.list.d/security:zeek.list
sudo apt update && sudo apt install zeek

# Fedora / RHEL
sudo dnf install zeek

# macOS (Homebrew)
brew install zeek

# Add Zeek to PATH (packages install under /opt/zeek)
export PATH=/opt/zeek/bin:$PATH
zeek --version
```

## Reading a pcap offline

This is the fastest way to get value from Zeek: point it at a capture and read the logs it produces.

```bash
mkdir analysis && cd analysis
zeek -r ../capture.pcap          # writes *.log files into the current directory
ls
# conn.log  dns.log  http.log  ssl.log  files.log  weird.log  ...
```

Load extra scripts while reading:

```bash
zeek -r capture.pcap local       # the default "local" policy: adds common detections
zeek -r capture.pcap protocols/ssl/validate-certs   # flag invalid TLS certs
```

## The log files

Zeek splits traffic into one log per protocol or activity. The most used:

| Log | What's in it |
| --- | --- |
| `conn.log` | Every connection: IPs, ports, duration, bytes each way, state |
| `dns.log` | DNS queries and answers |
| `http.log` | HTTP requests: host, URI, method, user-agent, status |
| `ssl.log` | TLS handshakes: SNI, version, cipher, cert chain |
| `files.log` | Files seen in transfers, with hashes |
| `x509.log` | Certificate details |
| `weird.log` | Protocol anomalies Zeek couldn't make sense of |
| `notice.log` | Things Zeek's scripts decided are worth flagging |
| `dhcp.log`, `smtp.log`, `ssh.log`, `smb_*.log` | Per-protocol activity |

Every log shares key fields: `ts` (timestamp) and `uid` (a connection ID). The `uid` is the magic: it's the same across logs, so you can pivot from an `http.log` entry to its `conn.log` entry to its `ssl.log` entry for the same flow.

## Reading logs on the command line

By default logs are tab-separated. `zeek-cut` extracts columns by name:

```bash
cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p service duration
cat dns.log  | zeek-cut query | sort | uniq -c | sort -rn | head    # top DNS queries
cat http.log | zeek-cut host uri | head
cat ssl.log  | zeek-cut server_name | sort -u                       # every TLS SNI seen
```

Switch output to JSON (easier for pipelines and SIEM ingestion):

```bash
zeek -r capture.pcap LogAscii::use_json=T
cat conn.log | jq 'select(.id.resp_p == 443) | .id.resp_h' | sort | uniq -c
```

## Live monitoring

Run Zeek against a monitoring interface. Put the interface in promiscuous mode and make sure it's receiving mirrored traffic.

```bash
sudo zeek -i eth0 local
```

For anything beyond a quick look, use **ZeekControl**, which manages a long-running (optionally clustered) deployment, log rotation, and restarts:

```bash
# Set the monitoring interface in /opt/zeek/etc/node.cfg, then:
sudo zeekctl deploy       # install config + start
sudo zeekctl status
sudo zeekctl stop
```

Rotated logs land in `/opt/zeek/logs/` in dated folders.

## Scripting (a taste)

Zeek's power is its event-driven scripting language. A tiny example that logs DNS queries for a watchlist of domains:

```zeek
# save as watch-dns.zeek, run: zeek -r capture.pcap watch-dns.zeek
const watchlist = set("example-c2.test", "bad-domain.test") &redef;

event dns_request(c: connection, msg: dns_msg, query: string, qtype: count, qclass: count)
    {
    if ( query in watchlist )
        print fmt("watchlist hit: %s asked for %s", c$id$orig_h, query);
    }
```

The shipped scripts under `/opt/zeek/share/zeek/` are the best reference for how detections are written.

## Tips

- Start offline with `zeek -r`. Once you understand the logs, move to live capture.
- `uid` ties everything together. When a log entry is interesting, grep that `uid` across all logs to reconstruct the full flow.
- `weird.log` and `notice.log` are where investigations often start.
- JSON output (`LogAscii::use_json=T`) plugs straight into Elastic, Splunk, or `jq`.
- Pair Zeek (what happened) with Suricata (signature alerts). Many sensor builds run both on the same traffic.
- For a packaged, searchable Zeek+pcap stack, look at Arkime or Security Onion.

## References

- [Zeek documentation](https://docs.zeek.org/)
- [Log files reference](https://docs.zeek.org/en/master/logs/index.html)
- [Scripting guide](https://docs.zeek.org/en/master/scripting/index.html)
- [Try Zeek (in-browser)](https://try.zeek.org/)
- [Source on GitHub](https://github.com/zeek/zeek)
