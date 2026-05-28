<div align="center">
  <h1>⚡ Rezonans CyberOS Setup</h1>
  <p><i>The Ultimate Penetration Testing OS Converter Framework</i></p>

  [![Language: Python](https://img.shields.io/badge/Language-Python3-blue.svg?style=for-the-badge&logo=python)](#)
  [![OS: Linux](https://img.shields.io/badge/OS-Linux-green.svg?style=for-the-badge&logo=linux)](#)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](#)
  
  <br>
  <i>Read this document in other languages:</i><br>
  <b><a href="README_TR.md">🇹🇷 Türkçe (Turkish)</a></b>
</div>

<hr>

**Rezonans CyberOS** is an advanced, automated setup framework that transforms any standard Linux distribution (Arch/CachyOS, Debian/Ubuntu, Fedora) into a fully-fledged, professional cybersecurity and penetration testing environment. 

Instead of manually installing hacking tools one by one, Rezonans OS provides a sleek GUI to curate and build your custom arsenal in minutes.

## ✨ Key Features

* 🛡️ **120+ Security Tools**: Packed with industry-standard tools categorized into 9 distinct modules (Information Gathering, Web Vulnerabilities, Password Cracking, Exploitation, Forensics, Malware Analysis, and more).
* 🎛️ **Modern GUI (CustomTkinter)**: A sleek, dark-themed, cyberpunk-style graphical interface that makes tool selection effortless.
* 🚀 **One-Click Profiles**: 
  * `Web Pentester`: Focuses on Web Vulns (BurpSuite, OWASP ZAP, Caido, SQLMap).
  * `Network Admin`: Focuses on Wireshark, Aircrack-ng, Nmap, Sniffers.
  * `Full Arsenal`: Installs all 120+ tools for a complete hacker workstation.
* 🧠 **Smart Package Management**: Automatically detects your OS package manager (`pacman`, `apt`, `dnf`) and installs tools natively.
* 🔒 **Kernel Hardening**: Applies strict Sysctl security policies (SYN Flood protection, Smurf Attack blocking) to secure your own workstation.

## 📥 Installation & Usage

Since this tool directly manipulates system packages and kernel network settings, it **must be run with root (`sudo`) privileges**.

### 1. Clone the Repository
```bash
git clone https://github.com/mefkuz/Rezonans_cyber.git
cd Rezonans_cyber
```

### 2. Run the Installer
```bash
sudo python3 cyber_os_gui.py
```
> **Note for Arch/CachyOS users**: The script will automatically bypass the PEP 668 (externally-managed-environment) restriction and install necessary GUI libraries (`tk`, `customtkinter`) safely in the background before launching the application.

### ⚠️ Troubleshooting (Wayland / Segmentation Fault)
If the GUI crashes immediately with a `Segmentation fault` or display error, it is likely due to Wayland blocking GUI applications from running as root. You have two easy solutions:

**Option A (Recommended):** Preserve your environment variables
```bash
sudo -E python3 cyber_os_gui.py
```

**Option B:** Grant root access to the local display server
```bash
xhost +si:localuser:root
sudo python3 cyber_os_gui.py
```

## 🧰 Built-In Tool Categories
- **Information Gathering**: `nmap`, `masscan`, `recon-ng`, `spiderfoot`...
- **Web Vulnerability**: `burpsuite`, `zaproxy`, `caido`, `sqlmap`...
- **Password Cracking**: `hashcat`, `john`, `hydra`, `wordlists`...
- **Wireless Attacks**: `aircrack-ng`, `kismet`, `wifite`...
- **Exploitation Tools**: `metasploit`, `searchsploit`, `beef`...
- **Sniffing/Spoofing**: `wireshark`, `bettercap`, `responder`...
- **Reverse Engineering**: `ghidra`, `radare2`, `apktool`...
- **Forensics & Malware**: `volatility3`, `autopsy`, `yara`, `clamav`...
- **General Utilities**: `tmux`, `docker`, `tor`, `proxychains`...

## 🤝 Contributing
Feel free to fork this project, submit pull requests, or request new tools to be added to the internal database!
