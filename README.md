# 🛡️ Rezonans CyberOS

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)]()
[![Tools](https://img.shields.io/badge/Security%20Tools-155+-red.svg)]()

> 🇹🇷 [Türkçe sürüm için tıklayın / Click for Turkish version](README_TR.md)

**Rezonans CyberOS** is a zero-dependency, terminal-based installer that transforms any Linux distribution into a professional cybersecurity workstation. It automatically detects your package manager, installs 155+ security tools, and applies kernel-level system hardening — all from a beautiful CLI interface.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎯 **Zero Dependencies** | No GUI libraries, no pip packages — pure Python standard library |
| 🐧 **Universal Linux** | Auto-detects `apt`, `pacman`, `dnf` — works on Arch, Ubuntu, Fedora, CachyOS, etc. |
| 📦 **120+ Security Tools** | 10 categories covering the full offensive & defensive security spectrum |
| 🚀 **Smart AUR Support** | Auto-validates and batch-installs AUR packages via `paru`/`yay` on Arch-based systems |
| 🔒 **Kernel Hardening** | Optional sysctl-based network hardening (SYN flood, ICMP, IPv6, source routing) |
| 🌍 **English & Turkish** | Full i18n with language selection at startup |
| 📊 **Live Progress Bar** | Real-time terminal progress tracking with per-package status |
| ⚡ **Pre-Check Engine** | Skips already-installed packages for blazing fast re-runs |

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/mefkuz/Rezonans_cyber.git
cd Rezonans_cyber
```

### 2. Run the Installer
```bash
sudo python3 cyber_os_cli.py
```

Or run without sudo — it will prompt for your password when needed:
```bash
python3 cyber_os_cli.py
```

> **That's it!** No pip installs, no virtual environments, no configuration files. Just run and go.

---

## 📋 Installation Profiles

| # | Profile | Categories Included |
|---|---|---|
| 1 | **Full Arsenal** | ALL 10 categories — complete security workstation |
| 2 | **Web Pentester** | Info Gathering, Web Vulns, Password Cracking, Utilities |
| 3 | **Network Specialist** | Info Gathering, Wireless, Sniffing/Spoofing, Reverse Eng., Utilities |
| 4 | **Forensics & Malware** | Forensics, Malware Analysis, Reverse Eng., Utilities |
| 5 | **Custom Selection** | Pick individual categories interactively |

---

## 🧰 Tool Categories

### 🔍 Information Gathering (17 tools)
`nmap` · `masscan` · `netdiscover` · `dnsenum` · `dnsrecon` · `fierce` · `theharvester` · `whois` · `bind-tools` · `amass` · `sublist3r` · `spiderfoot` · `dmitry` · `arp-scan` · `p0f` · `enum4linux` · `smbclient`

### 🌐 Web Vulnerabilities (19 tools)
`burpsuite` · `zaproxy` · `sqlmap` · `gobuster` · `nikto` · `dirb` · `dirbuster` · `wfuzz` · `wpscan` · `whatweb` · `caido` · `skipfish` · `uniscan` · `wapiti` · `commix` · `ffuf` · `xsser` · `xsstrike` · `w3af`

### 🔑 Password Cracking (13 tools)
`hashcat` · `john` · `hydra` · `medusa` · `ncrack` · `crunch` · `cupp` · `wordlists` · `cewl` · `crowbar` · `ophcrack` · `fcrackzip` · `pdfcrack`

### 📡 Wireless Attacks (12 tools)
`aircrack-ng` · `kismet` · `reaver` · `wifite` · `bully` · `hcxdumptool` · `hcxtools` · `cowpatty` · `fern-wifi-cracker` · `macchanger` · `mdk3` · `mdk4`

### 💣 Exploitation (9 tools)
`metasploit` · `searchsploit` · `beef` · `routersploit` · `social-engineer-toolkit` · `sqlmap` · `armitage` · `exploitdb` · `msfpc`

### 🕵️ Sniffing / Spoofing (12 tools)
`wireshark-cli` · `tcpdump` · `bettercap` · `ettercap` · `responder` · `macchanger` · `mitmproxy` · `dsniff` · `netsniff-ng` · `sslstrip` · `scapy` · `arpspoof`

### ⚙️ Reverse Engineering (12 tools)
`radare2` · `ghidra` · `apktool` · `ltrace` · `strace` · `gdb` · `binwalk` · `dex2jar` · `jd-cli` · `edb-debugger` · `jadx` · `objdump`

### 🔬 Digital Forensics (11 tools)
`autopsy` · `sleuthkit` · `volatility3` · `foremost` · `scalpel` · `exiftool` · `chkrootkit` · `rkhunter` · `ddrescue` · `guymager` · `bulk_extractor`

### 🦠 Malware Analysis (4 tools)
`yara` · `clamav` · `maldet` · `cuckoo-sandbox`

### 🔧 General Utilities (14 tools)
`tmux` · `git` · `curl` · `wget` · `htop` · `neovim` · `netcat` · `proxychains` · `tor` · `openvpn` · `docker` · `wireguard-tools` · `zsh` · `steghide`

---

## 🛡️ System Hardening

When enabled, the installer applies kernel-level security policies:

| Rule | Protection |
|---|---|
| `net.ipv4.icmp_echo_ignore_broadcasts=1` | Blocks Smurf attacks |
| `net.ipv4.tcp_syncookies=1` | SYN Flood protection |
| `net.ipv4.conf.all.accept_source_route=0` | Rejects source-routed packets |
| `net.ipv6.conf.all.disable_ipv6=1` | Disables IPv6 (reduces attack surface) |

---

## 🏗️ Architecture

```
cyber_os_cli.py          ← Single-file, zero-dependency CLI installer
├── Language Selection   ← English / Turkish
├── Profile Selection    ← 5 pre-built profiles + custom
├── Package Engine       ← Auto-detect apt/pacman/dnf
│   ├── Pre-check        ← Skip installed packages
│   ├── AUR Validation   ← Filter non-existent AUR packages
│   └── Batch Install    ← Optimized AUR batch via paru/yay
├── Progress Tracking    ← Real-time terminal progress bar
└── System Hardening     ← sysctl kernel policies
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">
  <b>Built with 💚 by the Rezonans Team</b><br>
  <i>Transform any Linux into a cyber weapon.</i>
</p>
