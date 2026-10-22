---
author: Infosec House
updated: 2026-10-16
---

> [!WARNING]
> Packet captures can contain passwords, cookies, and personal data. Only capture on networks you own or are authorized to monitor, and store `.pcap` files as carefully as the data in them.

## Overview

Wireshark is the standard open-source network protocol analyzer. It captures live traffic or opens saved capture files and decodes thousands of protocols field by field. It's the go-to tool for troubleshooting connectivity and performance, investigating incidents, learning how protocols work, and checking what an application actually sends over the wire.

It ships with command-line companions: `tshark` (terminal Wireshark), `dumpcap` (the capture engine), `capinfos`, `editcap`, and `mergecap`.

## Install

```bash
# Debian / Ubuntu / Kali (answer "Yes" to let non-root users capture)
sudo apt install wireshark
sudo usermod -aG wireshark "$USER"   # then log out and back in

# Fedora / RHEL
sudo dnf install wireshark

# macOS (Homebrew; also installs the ChmodBPF capture helper)
brew install --cask wireshark

# Check the version
wireshark --version
tshark --version
```

Windows installers are at [wireshark.org/download](https://www.wireshark.org/download.html). They include Npcap, which Wireshark needs to capture.

Run Wireshark as a normal user who belongs to the `wireshark` group, not as root. The privileged part is limited to `dumpcap`.

## Capture filters vs. display filters

Wireshark has two filter languages, and mixing them up is the most common stumbling block.

| | Capture filter | Display filter |
| --- | --- | --- |
| When it applies | While capturing: packets that don't match are never saved | After capture: hides packets but keeps them |
| Syntax | BPF (same as tcpdump) | Wireshark's own field syntax |
| Example | `host 192.0.2.10 and port 443` | `ip.addr == 192.0.2.10 && tcp.port == 443` |
| Where | Capture options, or `tshark -f` | The filter bar, or `tshark -Y` |

Use capture filters to keep files small on busy links. Use display filters for everything else.

## Capture filters (BPF)

```text
host 192.0.2.10                  # traffic to or from one host
net 192.0.2.0/24                 # a whole subnet
src host 192.0.2.10              # only traffic from this host
port 53                          # DNS
tcp port 443                     # HTTPS
portrange 8000-8100
not port 22                      # leave out your own SSH session
host 192.0.2.10 and not port 22
ether host 00:11:22:33:44:55     # by MAC address
icmp or arp
```

## Display filters

Basics:

```text
ip.addr == 192.0.2.10            # either source or destination
ip.src == 192.0.2.10
ip.dst == 192.0.2.0/24
tcp.port == 443                  # either direction
udp.port == 53
!(arp or icmp)                   # hide noise
frame contains "login"           # raw bytes match a string
```

Protocols:

```text
dns                              # all DNS
dns.qry.name contains "example"  # lookups for a domain
http.request                     # HTTP requests only
http.response.code >= 400        # HTTP errors
tls.handshake.type == 1          # TLS Client Hello
tls.handshake.extensions_server_name == "example.com"   # SNI
dhcp                             # DHCP (older versions: bootp)
smb2
```

Troubleshooting:

```text
tcp.analysis.flags               # anything Wireshark's TCP analysis flags
tcp.analysis.retransmission
tcp.analysis.zero_window
tcp.flags.reset == 1             # connection resets
tcp.flags.syn == 1 && tcp.flags.ack == 0   # new connection attempts
tcp.time_delta > 1               # gaps over 1 second in a TCP stream
icmp.type == 3                   # destination unreachable
```

Operators: `==`, `!=`, `>`, `<`, `contains`, `matches` (regex), `in {80 443 8080}`, `&&` / `and`, `||` / `or`, `!` / `not`.

To build a filter from a field, right-click it in the packet details pane and choose **Apply as Filter** or **Prepare as Filter**.

## Useful GUI features

| Feature | Where | What it's for |
| --- | --- | --- |
| Follow Stream | Right-click a packet → Follow → TCP/UDP/TLS/HTTP Stream | Read a whole conversation in order |
| Conversations | Statistics → Conversations | Who talks to whom, and how much |
| Endpoints | Statistics → Endpoints | Top talkers by bytes or packets |
| Protocol Hierarchy | Statistics → Protocol Hierarchy | What protocols make up the capture |
| I/O Graphs | Statistics → I/O Graphs | Traffic over time, spikes, gaps |
| Expert Information | Analyze → Expert Information | Errors and warnings Wireshark found |
| Export Objects | File → Export Objects → HTTP/SMB/… | Save files that were transferred in the capture |
| Name Resolution | View → Name Resolution | Show hostnames and vendor names instead of numbers |
| Coloring Rules | View → Coloring Rules | Highlight traffic that matters to you |
| Profiles | Edit → Configuration Profiles | Separate column and filter setups per task |

Handy columns to add (right-click a field → **Apply as Column**): `tcp.stream`, `dns.qry.name`, `http.host`, `tls.handshake.extensions_server_name`, `frame.time_delta_displayed`.

## TShark (command line)

```bash
tshark -D                                     # list capture interfaces
tshark -i eth0                                # capture live, print a summary per packet
tshark -i eth0 -f "port 53" -w dns.pcapng     # capture with a filter, write to file
tshark -i eth0 -a duration:60 -w one-min.pcapng   # stop after 60 seconds
tshark -i eth0 -b filesize:100000 -b files:10 -w ring.pcapng   # ring buffer: 10 x ~100 MB
tshark -r capture.pcapng                      # read a file
tshark -r capture.pcapng -Y "http.request"    # read with a display filter
```

Pull specific fields (great for spreadsheets and scripts):

```bash
tshark -r capture.pcapng -Y dns.flags.response==0 \
  -T fields -e frame.time -e ip.src -e dns.qry.name

tshark -r capture.pcapng -Y http.request \
  -T fields -E header=y -E separator=, \
  -e ip.src -e http.host -e http.request.uri > requests.csv
```

Built-in statistics:

```bash
tshark -r capture.pcapng -q -z io,phs              # protocol hierarchy
tshark -r capture.pcapng -q -z conv,tcp            # TCP conversations
tshark -r capture.pcapng -q -z endpoints,ip        # IP endpoints
tshark -r capture.pcapng -q -z http,tree           # HTTP request/response stats
tshark -r capture.pcapng -q -z follow,tcp,ascii,0  # follow TCP stream 0
```

## Working with capture files

```bash
capinfos capture.pcapng                       # duration, packet count, size, interfaces
editcap -c 100000 big.pcapng part.pcapng      # split into 100k-packet files
editcap -A "2026-10-16 09:00:00" -B "2026-10-16 10:00:00" big.pcapng hour.pcapng   # time slice
editcap -D 5 capture.pcapng dedup.pcapng      # remove duplicate packets
mergecap -w combined.pcapng a.pcapng b.pcapng # merge, sorted by timestamp
tshark -r capture.pcapng -Y "ip.addr==192.0.2.10" -w host-only.pcapng   # save a filtered subset
```

## Decrypting TLS you control

To inspect HTTPS from your own browser or application, have it log its session keys and point Wireshark at the file:

```bash
export SSLKEYLOGFILE="$HOME/tls-keys.log"
# then start Chrome or Firefox from this same shell
```

In Wireshark, go to **Preferences → Protocols → TLS → (Pre)-Master-Secret log filename** and select the file. Decrypted HTTP/2 and HTTP/1.1 then appear under the TLS records. This only works for sessions whose keys you have. It can't decrypt anyone else's traffic.

## Tips

- Capture first, filter later. A broad capture with a display filter beats a narrow capture that missed the problem.
- Capture as close to the problem as you can. A mirror/SPAN port or capture on the host itself sees more than the middle of the network.
- Turn off name resolution on big files. DNS lookups make large captures crawl.
- Use `tcp.stream eq N` to isolate one connection, then Follow Stream to read it.
- Save as `.pcapng` (the default). It keeps comments, interface details, and per-packet annotations.
- Before sharing a capture, cut it down to the relevant packets with `editcap` or **File → Export Specified Packets**, and scrub anything sensitive.

## References

- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Display filter reference](https://www.wireshark.org/docs/dfref/) (every field for every protocol)
- [Capture filter syntax (pcap-filter)](https://www.tcpdump.org/manpages/pcap-filter.7.html)
- [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html)
- [Sample captures](https://wiki.wireshark.org/SampleCaptures) for practice
- [Source on GitLab](https://gitlab.com/wireshark/wireshark)
