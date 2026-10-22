---
author: Infosec House
updated: 2026-10-16
---

> [!WARNING]
> Packet captures can contain passwords, cookies, and personal data. Only capture on networks and hosts you own or are authorized to monitor, and treat `.pcap` files as sensitive.

## Overview

tcpdump is the classic command-line packet capture tool. It's on nearly every Linux and BSD system and in most network appliances, so it works where Wireshark can't, such as on a headless server over SSH or inside a container. It uses the same BPF filter language as Wireshark's capture filters, and its `.pcap` files open directly in Wireshark for deeper analysis.

The usual workflow: capture on the server with tcpdump, copy the file back, and analyze it in Wireshark.

## Install

```bash
# Debian / Ubuntu
sudo apt install tcpdump

# Fedora / RHEL
sudo dnf install tcpdump

# Alpine (containers)
apk add tcpdump

# macOS: preinstalled. Check the version:
tcpdump --version
```

Capturing needs root (or `CAP_NET_RAW` and `CAP_NET_ADMIN`), so most commands below use `sudo`. Reading a saved file with `-r` doesn't.

## Basic capture

```bash
sudo tcpdump -D                       # list interfaces
sudo tcpdump -i eth0                  # capture on one interface
sudo tcpdump -i any                   # all interfaces (Linux)
sudo tcpdump -i eth0 -c 100           # stop after 100 packets
sudo tcpdump -i eth0 -n               # don't resolve hostnames (faster, clearer)
sudo tcpdump -i eth0 -nn              # don't resolve hostnames or port names
```

Start with `-nn`. Name resolution slows output and can generate DNS traffic of its own that ends up in your capture.

## Output detail

```bash
sudo tcpdump -i eth0 -nn -v           # more header detail (TTL, IP ID, length)
sudo tcpdump -i eth0 -nn -vvv         # maximum protocol decoding
sudo tcpdump -i eth0 -nn -e           # include MAC addresses (link-layer header)
sudo tcpdump -i eth0 -nn -A           # print payload as ASCII (good for HTTP)
sudo tcpdump -i eth0 -nn -X           # payload as hex + ASCII
sudo tcpdump -i eth0 -nn -tttt        # human-readable timestamps with dates
sudo tcpdump -i eth0 -nn -q           # quiet: less protocol detail per line
```

## Writing and reading files

```bash
sudo tcpdump -i eth0 -nn -w capture.pcap            # save raw packets (no screen output)
sudo tcpdump -i eth0 -nn -w capture.pcap -c 10000   # stop after 10,000 packets
tcpdump -nn -r capture.pcap                         # read back (no sudo needed)
tcpdump -nn -r capture.pcap 'port 53'               # read back with a filter
tcpdump -nn -r capture.pcap -w dns.pcap 'port 53'   # save a filtered subset
```

Watch live and save at the same time:

```bash
sudo tcpdump -i eth0 -nn -U -w - | tee capture.pcap | tcpdump -nn -r -
```

Rotating files for long captures:

```bash
# New file every 100 MB, keep the last 10 (ring buffer)
sudo tcpdump -i eth0 -nn -C 100 -W 10 -w ring.pcap

# New file every hour, timestamped names
sudo tcpdump -i eth0 -nn -G 3600 -w 'capture-%Y%m%d-%H%M.pcap'
```

Snapshot length (how much of each packet to keep):

```bash
sudo tcpdump -i eth0 -s 96 -w headers.pcap     # headers only: smaller files, less sensitive data
sudo tcpdump -i eth0 -s 0 -w full.pcap         # whole packet (the default on modern versions)
```

## Filters (BPF)

Hosts and networks:

```text
host 192.0.2.10
src host 192.0.2.10
dst host 192.0.2.10
net 192.0.2.0/24
ether host 00:11:22:33:44:55
```

Ports and protocols:

```text
port 443
src port 53
portrange 8000-8100
tcp
udp
icmp
arp
ip6
```

Combine with `and`, `or`, `not`, and group with parentheses. Quote the whole filter so the shell doesn't interpret the parentheses:

```bash
sudo tcpdump -i eth0 -nn 'host 192.0.2.10 and (port 80 or port 443)'
sudo tcpdump -i eth0 -nn 'net 192.0.2.0/24 and not port 22'
sudo tcpdump -i eth0 -nn 'udp and not port 53'
```

TCP flags (handy for troubleshooting connections):

```bash
sudo tcpdump -i eth0 -nn 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0'   # new connection attempts
sudo tcpdump -i eth0 -nn 'tcp[tcpflags] & tcp-rst != 0'                                    # resets
sudo tcpdump -i eth0 -nn 'tcp[tcpflags] & tcp-fin != 0'                                    # connection closes
```

Packet size:

```bash
sudo tcpdump -i eth0 -nn 'greater 1000'     # packets over 1000 bytes
sudo tcpdump -i eth0 -nn 'less 64'
```

## Common recipes

```bash
# DNS queries and answers
sudo tcpdump -i any -nn port 53

# Is traffic from a host reaching this server at all?
sudo tcpdump -i eth0 -nn host 192.0.2.10

# HTTP requests in plain text (unencrypted traffic only)
sudo tcpdump -i eth0 -nn -A -s 0 'tcp port 80'

# DHCP traffic (clients getting addresses)
sudo tcpdump -i eth0 -nn -e 'port 67 or port 68'

# ICMP: ping, unreachables, TTL exceeded
sudo tcpdump -i eth0 -nn icmp

# ARP: who's claiming which IP
sudo tcpdump -i eth0 -nn -e arp

# Everything except your own SSH session
sudo tcpdump -i eth0 -nn 'not port 22'
```

## Capturing remotely and analyzing in Wireshark

Capture on the server, then copy the file:

```bash
ssh admin@server 'sudo tcpdump -i eth0 -nn -c 5000 -w /tmp/cap.pcap not port 22'
scp admin@server:/tmp/cap.pcap .
wireshark cap.pcap
```

Or stream straight into Wireshark (the remote user needs passwordless sudo for tcpdump, or capture capabilities):

```bash
ssh admin@server 'sudo tcpdump -i eth0 -nn -U -s 0 -w - not port 22' | wireshark -k -i -
```

Always exclude port 22 when capturing over SSH. Otherwise you capture your own session, which generates more traffic, which gets captured, and so on.

## Containers and Kubernetes

```bash
# Capture inside a container's network namespace from the host
PID=$(docker inspect -f '{{.State.Pid}}' my-container)
sudo nsenter -t "$PID" -n tcpdump -i any -nn -w container.pcap

# Kubernetes: run tcpdump in an ephemeral debug container next to the pod
kubectl debug -it my-pod --image=nicolaka/netshoot --target=my-container -- tcpdump -i any -nn
```

## Tips

- Use `-nn` by default. Resolution is slow and adds its own DNS traffic.
- Use `-w` to save, and analyze later. Printing to the screen drops packets on busy links, and writing raw packets doesn't.
- When writing to a pipe or watching a file grow, add `-U` (packet-buffered output) so packets show up immediately.
- The `packets dropped by kernel` count at the end tells you whether the capture is complete. If it's not zero, narrow the filter or use a smaller `-s`.
- Use `-i any` on Linux when you're not sure which interface carries the traffic. Note that it records a "cooked" link header instead of Ethernet.
- Ctrl+C stops the capture and prints the summary counts.
- With `-A`, encrypted traffic (HTTPS, SSH) shows only noise. That's expected.

## References

- [tcpdump man page](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [pcap-filter man page](https://www.tcpdump.org/manpages/pcap-filter.7.html) (full BPF syntax)
- [tcpdump.org](https://www.tcpdump.org/)
- [Wireshark cheat sheet](/tools/wireshark/) for analyzing your captures
- [Source on GitHub](https://github.com/the-tcpdump-group/tcpdump)
