---
author: hack-ita
updated: 2026-11-05
---

> [!WARNING]
> Use NetExec only against systems and networks you own or are explicitly authorized to assess. The `192.0.2.0/24` range is reserved for documentation; replace it only with an in-scope lab or assessment target.

## Overview

[NetExec](https://github.com/Pennyw0rth/NetExec) (`nxc`) is a network service enumeration and assessment tool commonly used during internal penetration tests and Active Directory security assessments. It supports protocols including SMB, LDAP, WinRM, SSH, FTP, RDP, MSSQL, VNC, and NFS.

## Install

On Kali and other Debian-based systems, install the prerequisites and use the upstream pipx installation method:

```bash
sudo apt update
sudo apt install pipx git
pipx ensurepath
pipx install git+https://github.com/Pennyw0rth/NetExec
```

Open a new shell if needed, then verify the installation:

```bash
nxc --help
nxc smb --help
```

For other installation methods and troubleshooting, see the [official installation guide](https://www.netexec.wiki/getting-started/installation).

## Common usage

### SMB

Identify SMB information exposed by an authorized host:

```bash
nxc smb 192.0.2.10
```

Authenticate with an account explicitly provided for the assessment:

```bash
nxc smb 192.0.2.10 -d CONTOSO -u alice -p 'PasswordHere'
```

List accessible shares with the same authorized account:

```bash
nxc smb 192.0.2.10 -d CONTOSO -u alice -p 'PasswordHere' --shares
```

### LDAP

Query LDAP using an authorized domain account:

```bash
nxc ldap 192.0.2.10 -d CONTOSO -u alice -p 'PasswordHere'
```

List domain users when permitted by the account and assessment scope:

```bash
nxc ldap 192.0.2.10 -d CONTOSO -u alice -p 'PasswordHere' --users
```

### WinRM

Check WinRM authentication against an in-scope host:

```bash
nxc winrm 192.0.2.10 -d CONTOSO -u alice -p 'PasswordHere'
```

### Protocol help

Each protocol has its own help output and options:

```bash
nxc smb --help
nxc ldap --help
nxc winrm --help
```

## Modules

List the modules available for a protocol:

```bash
nxc smb -L
```

Display the options for a specific module before using it:

```bash
nxc smb -M MODULE_NAME --options
```

Run a module only after reviewing its behavior and confirming that it is appropriate for the authorized scope:

```bash
nxc smb 192.0.2.10 -M MODULE_NAME
```

See the [official module documentation](https://www.netexec.wiki/getting-started/using-modules).

## Tips

- Start with `nxc <protocol> --help`; options differ between protocols.
- Use the protocol selector explicitly, such as `nxc smb`, `nxc ldap`, or `nxc winrm`.
- Review module options before execution. Some modules can change remote systems or expose sensitive data.
- Avoid placing real passwords directly in shell commands on shared systems, since they may be stored in shell history or visible in process listings. Prefer an approved secret-handling method.
- Keep targets, credentials, and modules within the written scope of the engagement.

## References

- [NetExec source repository](https://github.com/Pennyw0rth/NetExec)
- [Official NetExec wiki](https://www.netexec.wiki/)
- [Selecting and using a protocol](https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol)
- [Using modules](https://www.netexec.wiki/getting-started/using-modules)
- [EN.HackITA](https://en.hackita.it/articoli/netexec/)
