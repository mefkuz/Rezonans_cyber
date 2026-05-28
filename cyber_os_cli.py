#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║  REZONANS CyberOS - Ultimate CLI Installer               ║
║  Zero-dependency terminal interface for any Linux distro  ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import shutil
import time

# ═══════════════════════════════════════════════════════════
# COLORS & STYLES
# ═══════════════════════════════════════════════════════════
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"
    BG_GREEN = "\033[42m"
    BG_GRAY  = "\033[100m"
    NEON    = "\033[38;5;46m"   # Bright neon green
    ORANGE  = "\033[38;5;208m"

# ═══════════════════════════════════════════════════════════
# BANNER
# ═══════════════════════════════════════════════════════════
BANNER = f"""
{C.NEON}{C.BOLD}
    ██████╗ ███████╗███████╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗███████╗
    ██╔══██╗██╔════╝╚══███╔╝██╔═══██╗████╗  ██║██╔══██╗████╗  ██║██╔════╝
    ██████╔╝█████╗    ███╔╝ ██║   ██║██╔██╗ ██║███████║██╔██╗ ██║███████╗
    ██╔══██╗██╔══╝   ███╔╝  ██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║╚════██║
    ██║  ██║███████╗███████╗╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║███████║
    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
{C.RESET}
{C.CYAN}    ╔═══════════════════════════════════════════════════════════════╗
    ║  {C.WHITE}C Y B E R   O S  —  Ultimate Security Workstation Builder{C.CYAN}  ║
    ╚═══════════════════════════════════════════════════════════════╝{C.RESET}
"""

# ═══════════════════════════════════════════════════════════
# TOOLS DATABASE
# ═══════════════════════════════════════════════════════════
TOOLS = {
    "info":      ["nmap", "masscan", "netdiscover", "dnsenum", "dnsrecon", "fierce", "theharvester", "whois", "bind-tools", "amass", "sublist3r", "spiderfoot", "dmitry", "arp-scan", "p0f", "enum4linux", "smbclient"],
    "web":       ["burpsuite", "zaproxy", "sqlmap", "gobuster", "nikto", "dirb", "dirbuster", "wfuzz", "wpscan", "whatweb", "caido", "skipfish", "uniscan", "wapiti", "commix", "ffuf", "xsser", "xsstrike", "w3af"],
    "pass":      ["hashcat", "john", "hydra", "medusa", "ncrack", "crunch", "cupp", "wordlists", "cewl", "crowbar", "ophcrack", "fcrackzip", "pdfcrack"],
    "wifi":      ["aircrack-ng", "kismet", "reaver", "wifite", "bully", "hcxdumptool", "hcxtools", "cowpatty", "fern-wifi-cracker", "macchanger", "mdk3", "mdk4"],
    "exploit":   ["metasploit", "searchsploit", "beef", "routersploit", "social-engineer-toolkit", "sqlmap", "armitage", "exploitdb", "msfpc"],
    "sniff":     ["wireshark-cli", "tcpdump", "bettercap", "ettercap", "responder", "macchanger", "mitmproxy", "dsniff", "netsniff-ng", "sslstrip", "scapy", "arpspoof"],
    "reverse":   ["radare2", "ghidra", "apktool", "ltrace", "strace", "gdb", "binwalk", "dex2jar", "jd-cli", "edb-debugger", "jadx", "objdump"],
    "forensics": ["autopsy", "sleuthkit", "volatility3", "foremost", "scalpel", "exiftool", "chkrootkit", "rkhunter", "ddrescue", "guymager", "bulk_extractor"],
    "malware":   ["yara", "clamav", "maldet", "cuckoo-sandbox"],
    "utils":     ["tmux", "git", "curl", "wget", "htop", "neovim", "netcat", "proxychains", "tor", "openvpn", "docker", "wireguard-tools", "zsh", "steghide"]
}

CAT_NAMES = {
    "en": {"info": "Info Gathering", "web": "Web Vulnerabilities", "pass": "Password Cracking",
           "wifi": "Wireless Attacks", "exploit": "Exploitation", "sniff": "Sniffing/Spoofing",
           "reverse": "Reverse Engineering", "forensics": "Digital Forensics", "malware": "Malware Analysis", "utils": "General Utilities"},
    "tr": {"info": "Bilgi Toplama", "web": "Web Zafiyet", "pass": "Parola Kırma",
           "wifi": "Kablosuz Ağ Saldırıları", "exploit": "İstismar (Exploit)", "sniff": "Sniffing/Spoofing",
           "reverse": "Tersine Mühendislik", "forensics": "Adli Bilişim", "malware": "Zararlı Yazılım Analizi", "utils": "Genel Araçlar"}
}

PACKAGE_MAPPING = {
    "apt":    {"wireshark-cli": "tshark", "bind-tools": "dnsutils", "metasploit": "metasploit-framework", "netcat": "netcat-traditional", "wordlists": "wordlists"},
    "pacman": {"wireshark-cli": "wireshark-cli", "bind-tools": "bind", "metasploit": "metasploit", "netcat": "gnu-netcat", "wordlists": "seclists", "burpsuite": "burpsuite", "zaproxy": "zaproxy", "amass": "amass-bin", "caido": "caido-bin"},
    "dnf":    {"wireshark-cli": "wireshark", "bind-tools": "bind-utils", "netcat": "nc"}
}

PROFILES = {
    "en": {
        "1": ("Full Arsenal (ALL Tools)", list(TOOLS.keys())),
        "2": ("Web Pentester", ["info", "web", "pass", "utils"]),
        "3": ("Network Specialist", ["info", "wifi", "sniff", "utils", "reverse"]),
        "4": ("Forensics & Malware Analyst", ["forensics", "malware", "reverse", "utils"]),
        "5": ("Custom Selection (choose categories)", None),
    },
    "tr": {
        "1": ("Full Arsenal (TÜM Araçlar)", list(TOOLS.keys())),
        "2": ("Web Pentester", ["info", "web", "pass", "utils"]),
        "3": ("Ağ Uzmanı", ["info", "wifi", "sniff", "utils", "reverse"]),
        "4": ("Adli Bilişim & Zararlı Analiz", ["forensics", "malware", "reverse", "utils"]),
        "5": ("Özel Seçim (kategorileri seç)", None),
    }
}

# ═══════════════════════════════════════════════════════════
# TRANSLATIONS
# ═══════════════════════════════════════════════════════════
T = {
    "en": {
        "welcome":    "Welcome to Rezonans CyberOS Installer!",
        "detected":   "Package Manager Detected",
        "lang_ask":   "Select Language / Dil Seçin",
        "prof_ask":   "Select an installation profile:",
        "cat_ask":    "Select categories (comma-separated, e.g. 1,3,5):",
        "confirm":    "The following {} tools will be installed. Continue?",
        "hardening":  "Apply kernel-level system hardening? (sysctl)",
        "phase1":     "PHASE 1 — Updating System Repositories",
        "phase2":     "PHASE 2 — Installing Security Tools",
        "phase3":     "PHASE 3 — System Hardening (Kernel Security)",
        "installed":  "Already installed",
        "installing": "Installing",
        "aur_queue":  "Queued for AUR",
        "skip":       "Not found, skipping",
        "aur_batch":  "Installing {} AUR packages via {}...",
        "complete":   "OPERATION COMPLETE — Your station is ready for duty!",
        "summary":    "Successfully processed {} / {} packages.",
        "yes_no":     "[Y/n]",
        "abort":      "Installation cancelled.",
    },
    "tr": {
        "welcome":    "Rezonans CyberOS Kurulumuna Hoş Geldiniz!",
        "detected":   "Paket Yöneticisi Algılandı",
        "lang_ask":   "Select Language / Dil Seçin",
        "prof_ask":   "Bir kurulum profili seçin:",
        "cat_ask":    "Kategorileri seçin (virgülle ayırın, ör: 1,3,5):",
        "confirm":    "Toplam {} araç kurulacak. Devam edilsin mi?",
        "hardening":  "Kernel düzeyinde sistem sıkılaştırması uygulansın mı? (sysctl)",
        "phase1":     "AŞAMA 1 — Sistem Depoları Güncelleniyor",
        "phase2":     "AŞAMA 2 — Güvenlik Araçları Kuruluyor",
        "phase3":     "AŞAMA 3 — Sistem Sıkılaştırması (Kernel Güvenliği)",
        "installed":  "Zaten kurulu",
        "installing": "Kuruluyor",
        "aur_queue":  "AUR listesine eklendi",
        "skip":       "Bulunamadı, atlanıyor",
        "aur_batch":  "{} AUR paketi {} ile kuruluyor...",
        "complete":   "İŞLEM TAMAMLANDI — İstasyonunuz göreve hazır!",
        "summary":    "{} / {} paket başarıyla işlendi.",
        "yes_no":     "[E/h]",
        "abort":      "Kurulum iptal edildi.",
    }
}

# ═══════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def line(char="═", length=65):
    print(f"{C.CYAN}{char * length}{C.RESET}")

def header(text, color=C.CYAN):
    width = 65
    padding = (width - len(text) - 4) // 2
    print(f"\n{color}{'═' * width}")
    print(f"║{' ' * padding}  {C.WHITE}{C.BOLD}{text}{C.RESET}{color}{' ' * (width - padding - len(text) - 4)}║")
    print(f"{'═' * width}{C.RESET}\n")

def status(icon, text, color=C.GREEN):
    icons = {"ok": f"{C.GREEN}✔", "skip": f"{C.YELLOW}⏭", "fail": f"{C.RED}✘",
             "aur": f"{C.MAGENTA}◆", "info": f"{C.CYAN}ℹ", "dl": f"{C.CYAN}⬇"}
    print(f"  {icons.get(icon, '•')}{C.RESET} {color}{text}{C.RESET}")

def progress_bar(current, total, width=50):
    pct = current / total if total > 0 else 0
    filled = int(width * pct)
    bar = f"{C.NEON}{'█' * filled}{C.GRAY}{'░' * (width - filled)}{C.RESET}"
    sys.stdout.write(f"\r  {bar} {C.WHITE}{C.BOLD}{int(pct * 100):>3}%{C.RESET} ({current}/{total})")
    sys.stdout.flush()
    if current == total:
        print()

def ask(prompt, default="y"):
    try:
        answer = input(f"\n  {C.YELLOW}?{C.RESET} {prompt} ").strip().lower()
        if not answer:
            return default
        return answer
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(0)

# ═══════════════════════════════════════════════════════════
# CORE ENGINE
# ═══════════════════════════════════════════════════════════
class RezonansInstaller:
    def __init__(self):
        self.pkg_manager = self.detect_pkg_manager()
        self.lang = "en"

    def detect_pkg_manager(self):
        for mgr in ["apt-get", "pacman", "dnf", "yum"]:
            if shutil.which(mgr):
                return "apt" if mgr == "apt-get" else mgr
        return None

    def is_installed(self, pkg):
        if self.pkg_manager == "apt":
            return subprocess.call(f"dpkg -s {pkg} > /dev/null 2>&1", shell=True) == 0
        elif self.pkg_manager == "pacman":
            return subprocess.call(f"pacman -Q {pkg} > /dev/null 2>&1", shell=True) == 0
        elif self.pkg_manager == "dnf":
            return subprocess.call(f"rpm -q {pkg} > /dev/null 2>&1", shell=True) == 0
        return False

    def run_cmd(self, cmd, silent=False):
        try:
            if silent:
                return subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
            else:
                return subprocess.call(cmd, shell=True) == 0
        except Exception:
            return False

    def aur_exists(self, pkg):
        """Check if a package actually exists in AUR before queuing it."""
        aur_helper = "paru" if shutil.which("paru") else ("yay" if shutil.which("yay") else None)
        if not aur_helper:
            return False
        real_user = os.environ.get("SUDO_USER", os.environ.get("USER", ""))
        cmd = f"sudo -u {real_user} {aur_helper} -Si {pkg} > /dev/null 2>&1" if os.geteuid() == 0 else f"{aur_helper} -Si {pkg} > /dev/null 2>&1"
        return subprocess.call(cmd, shell=True) == 0

    # ─── Language Selection ────────────────────────────────
    def select_language(self):
        clear()
        print(BANNER)
        line()
        print(f"  {C.WHITE}{C.BOLD}1{C.RESET} {C.GRAY}│{C.RESET} 🇬🇧  English")
        print(f"  {C.WHITE}{C.BOLD}2{C.RESET} {C.GRAY}│{C.RESET} 🇹🇷  Türkçe")
        line()
        choice = ask("Select Language / Dil Seçin [1/2]:", "1")
        self.lang = "tr" if choice == "2" else "en"

    # ─── Profile Selection ─────────────────────────────────
    def select_profile(self):
        t = T[self.lang]
        profiles = PROFILES[self.lang]
        cat_names = CAT_NAMES[self.lang]

        clear()
        print(BANNER)

        # System info
        header(t["welcome"])
        pkg_str = self.pkg_manager.upper() if self.pkg_manager else "NOT FOUND"
        total_tools = sum(len(v) for v in TOOLS.values())
        print(f"  {C.CYAN}▸{C.RESET} {t['detected']}: {C.NEON}{C.BOLD}{pkg_str}{C.RESET}")
        print(f"  {C.CYAN}▸{C.RESET} Available Tools: {C.NEON}{C.BOLD}{total_tools}{C.RESET}")
        print()

        if not self.pkg_manager:
            print(f"  {C.RED}{C.BOLD}[ERROR] No supported package manager found!{C.RESET}")
            sys.exit(1)

        # Show profiles
        line()
        print(f"  {C.WHITE}{C.BOLD}{t['prof_ask']}{C.RESET}\n")
        for num, (name, _) in profiles.items():
            print(f"  {C.NEON}{C.BOLD}{num}{C.RESET} {C.GRAY}│{C.RESET} {name}")
        line()

        choice = ask(f"[1-5]:", "1")
        if choice not in profiles:
            choice = "1"

        selected_cats = profiles[choice][1]

        # Custom category selection
        if selected_cats is None:
            print()
            cat_keys = list(TOOLS.keys())
            for i, key in enumerate(cat_keys, 1):
                count = len(TOOLS[key])
                print(f"  {C.NEON}{C.BOLD}{i:>2}{C.RESET} {C.GRAY}│{C.RESET} {cat_names[key]} {C.DIM}({count} tools){C.RESET}")
            line()
            raw = ask(t["cat_ask"], "1,2,3,4,5,6,7,8,9,10")
            try:
                indices = [int(x.strip()) - 1 for x in raw.split(",")]
                selected_cats = [cat_keys[i] for i in indices if 0 <= i < len(cat_keys)]
            except (ValueError, IndexError):
                selected_cats = list(TOOLS.keys())

        # Build package list
        selected_packages = []
        for cat in selected_cats:
            for pkg in TOOLS.get(cat, []):
                mapped = PACKAGE_MAPPING.get(self.pkg_manager, {}).get(pkg, pkg)
                if mapped not in selected_packages:
                    selected_packages.append(mapped)

        return selected_packages

    # ─── Main Installation ─────────────────────────────────
    def install(self, packages):
        t = T[self.lang]
        total = len(packages)

        # Confirmation
        print(f"\n  {C.CYAN}▸{C.RESET} {t['confirm'].format(total)} {t['yes_no']}")
        if ask("", "y") not in ("y", "e", "yes", "evet", ""):
            print(f"\n  {C.RED}{t['abort']}{C.RESET}")
            return

        # Hardening
        do_harden = ask(f"{t['hardening']} {t['yes_no']}", "y") in ("y", "e", "yes", "evet", "")

        # ── Phase 1: Update Repos ──────────────────────────
        header(t["phase1"], C.CYAN)
        if self.pkg_manager == "apt":
            self.run_cmd("sudo apt-get update -y")
        elif self.pkg_manager == "pacman":
            self.run_cmd("sudo pacman -Sy --noconfirm")
        elif self.pkg_manager == "dnf":
            self.run_cmd("sudo dnf check-update")

        # ── Phase 2: Install Tools ─────────────────────────
        header(t["phase2"], C.GREEN)

        real_user = os.environ.get("SUDO_USER", os.environ.get("USER", "root"))
        success = 0
        aur_packages = []

        for i, pkg in enumerate(packages, 1):
            progress_bar(i, total)

            # Already installed?
            if self.is_installed(pkg):
                status("ok", f"{pkg} — {t['installed']}", C.GREEN)
                success += 1
                continue

            # Arch: check main repos vs AUR
            if self.pkg_manager == "pacman":
                if subprocess.call(f"pacman -Si {pkg} > /dev/null 2>&1", shell=True) != 0:
                    if self.aur_exists(pkg):
                        status("aur", f"{pkg} — {t['aur_queue']}", C.MAGENTA)
                        aur_packages.append(pkg)
                    else:
                        status("skip", f"{pkg} — {t['skip']}", C.YELLOW)
                    continue

            # Install via main package manager
            status("dl", f"{pkg} — {t['installing']}...", C.CYAN)
            cmd = ""
            if self.pkg_manager == "apt":
                cmd = f"sudo apt-get install -y {pkg}"
            elif self.pkg_manager == "pacman":
                cmd = f"sudo pacman -S --noconfirm {pkg}"
            elif self.pkg_manager == "dnf":
                cmd = f"sudo dnf install -y {pkg}"

            if self.run_cmd(cmd, silent=True):
                success += 1
            else:
                status("fail", f"{pkg} — FAILED", C.RED)

        # ── Phase 2.5: AUR Batch ───────────────────────────
        if aur_packages and self.pkg_manager == "pacman":
            aur_helper = "paru" if shutil.which("paru") else ("yay" if shutil.which("yay") else None)
            if aur_helper:
                print()
                status("info", t["aur_batch"].format(len(aur_packages), aur_helper), C.MAGENTA)
                aur_cmd = f"sudo -u {real_user} {aur_helper} -S --noconfirm --needed {' '.join(aur_packages)}" if os.geteuid() == 0 else f"{aur_helper} -S --noconfirm --needed {' '.join(aur_packages)}"
                if self.run_cmd(aur_cmd):
                    success += len(aur_packages)
                else:
                    status("fail", "Some AUR packages failed.", C.YELLOW)

        # Summary
        print()
        line()
        status("info", t["summary"].format(success, total), C.WHITE)
        line()

        # ── Phase 3: Hardening ─────────────────────────────
        if do_harden:
            header(t["phase3"], C.ORANGE)
            sysctl = "net.ipv4.icmp_echo_ignore_broadcasts=1\nnet.ipv4.tcp_syncookies=1\nnet.ipv4.conf.all.accept_source_route=0\nnet.ipv6.conf.all.disable_ipv6=1"
            
            sysctl_cmd = f"echo '{sysctl}' | sudo tee /etc/sysctl.d/99-cybersecurity.conf > /dev/null"
            self.run_cmd(sysctl_cmd)
            self.run_cmd("sudo sysctl -p /etc/sysctl.d/99-cybersecurity.conf")

            status("ok", "SYN Flood Protection   — ENABLED", C.GREEN)
            status("ok", "ICMP Broadcast Block   — ENABLED", C.GREEN)
            status("ok", "Source Routing Block    — ENABLED", C.GREEN)
            status("ok", "IPv6 Disabled          — ENABLED", C.GREEN)

        # ── Done ───────────────────────────────────────────
        print()
        print(f"{C.NEON}{C.BOLD}")
        print("    ╔═══════════════════════════════════════════════════╗")
        print(f"    ║  ✔  {t['complete']:<47} ║")
        print("    ╚═══════════════════════════════════════════════════╝")
        print(f"{C.RESET}")

    # ─── Entry Point ───────────────────────────────────────
    def run(self):
        self.select_language()
        packages = self.select_profile()
        self.install(packages)


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        installer = RezonansInstaller()
        installer.run()
    except KeyboardInterrupt:
        print(f"\n\n  {C.YELLOW}Interrupted. Exiting...{C.RESET}\n")
        sys.exit(0)
