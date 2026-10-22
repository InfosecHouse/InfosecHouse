---
author: Infosec House
updated: 2026-10-16
---

> [!WARNING]
> masscan is built for speed and can send an enormous number of packets very quickly. Only scan address ranges you own or have explicit written authorization to test. Scan your own systems first to learn its behavior, keep the rate sane, and never point it at infrastructure you don't control. The `192.0.2.0/24` range below is reserved for documentation, so replace it with your authorized scope.

## Overview

masscan is an internet-scale TCP port scanner. It's asynchronous: it transmits probes and processes replies on separate threads, which lets it cover huge address ranges far faster than a traditional scanner. It uses an Nmap-like command line, so flags such as `-p` and `-oX` feel familiar, but it only does fast port discovery. It does not do Nmap's service/version detection or scripting. The usual workflow is: find open ports with masscan, then run Nmap against just those.

## Install

```bash
# Debian / Ubuntu / Kali
sudo apt install masscan

# Fedora / RHEL
sudo dnf install masscan

# macOS (Homebrew)
brew install masscan

masscan --version
```

Scanning needs raw socket access, so run it with `sudo`.

## Basic scans

```bash
# One port across a subnet
sudo masscan 192.0.2.0/24 -p80

# Several ports / ranges
sudo masscan 192.0.2.0/24 -p80,443,8000-8100

# UDP ports (prefix with U:)
sudo masscan 192.0.2.0/24 -pU:53,161

# A target list from a file
sudo masscan -iL targets.txt -p443

# Exclude addresses you must not touch (do this before scanning)
sudo masscan 192.0.2.0/24 -p80 --excludefile exclude.txt
```

## Controlling the rate (important)

The default rate is intentionally low. You set packets-per-second explicitly with `--rate`. Higher rates can saturate links and trip monitoring, so raise it only on networks you control and understand.

```bash
sudo masscan 192.0.2.0/24 -p80 --rate 1000        # 1,000 pps (gentle)
sudo masscan 192.0.2.0/24 -p80 --rate 10000       # 10,000 pps (only on networks you control)
```

Start low. Confirm the target and your own uplink can handle the traffic before increasing it.

## Output formats

```bash
sudo masscan 192.0.2.0/24 -p80,443 -oX scan.xml    # XML
sudo masscan 192.0.2.0/24 -p80,443 -oJ scan.json   # JSON
sudo masscan 192.0.2.0/24 -p80,443 -oG scan.gnmap  # grepable
sudo masscan 192.0.2.0/24 -p80,443 -oL scan.list   # simple list
sudo masscan 192.0.2.0/24 -p80,443 -oX scan.xml --interactive   # also print to screen
```

Pull just the open host:port pairs out of a list-format file:

```bash
grep '^open' scan.list | awk '{print $4":"$3}'
```

## Resuming and configuration

A long scan writes a `paused.conf` on Ctrl+C so you can resume it:

```bash
sudo masscan 192.0.2.0/24 -p1-65535 --rate 1000   # Ctrl+C writes paused.conf
sudo masscan --resume paused.conf
```

Save the equivalent flags as a config file and reuse it:

```bash
sudo masscan 192.0.2.0/24 -p80,443 --rate 1000 --echo > scan.conf
sudo masscan -c scan.conf
```

## Handing results to Nmap

masscan finds the open ports; Nmap identifies what's behind them.

```bash
# 1) Fast port discovery with masscan
sudo masscan 192.0.2.0/24 -p1-65535 --rate 1000 -oL ports.list

# 2) Build a host list and a port list from the results
ips=$(grep '^open' ports.list | awk '{print $4}' | sort -u | paste -sd, -)
ports=$(grep '^open' ports.list | awk '{print $3}' | sort -un | paste -sd, -)

# 3) Targeted service/version scan with Nmap (see the Nmap cheat sheet)
sudo nmap -sV -p "$ports" $(echo "$ips" | tr ',' ' ') -oA detail
```

## Tips

- Always set `--rate` deliberately. The flag exists precisely so you choose the speed instead of flooding by accident.
- Use `--excludefile` for addresses that must never be probed, and keep it current.
- masscan has its own TCP/IP stack. On some systems you'll see it warn about the OS also sending RST packets; the docs cover firewalling masscan's source port to avoid that.
- Scanning all 65,535 ports on a large range is a lot of traffic, so scope the ports and the range to what you actually need.
- It reports open ports only; it won't tell you the service. That's Nmap's job.
- Keep the authorization paperwork for the exact ranges and the time window with your scan output.

## References

- [masscan README and usage](https://github.com/robertdavidgraham/masscan#readme)
- [Nmap cheat sheet](/tools/nmap/) for the follow-up service scan
- [Source on GitHub](https://github.com/robertdavidgraham/masscan)
