#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import threading
import shutil

# --- Root (Sudo) Privilege Check ---
if os.geteuid() != 0:
    print("\n[ERROR] ACCESS DENIED! / [HATA] ERİŞİM REDDEDİLDİ!")
    print("This tool requires ROOT (sudo) privileges to install packages.")
    print("Bu arayüz sistem paketlerine müdahale ettiği için ROOT (sudo) yetkisi gerektirir.")
    print("Please run it again with: / Lütfen şu komutla tekrar çalıştırın:\n")
    print("    sudo python3 " + os.path.abspath(__file__) + "\n")
    sys.exit(1)

# --- Tkinter System Library Check ---
def install_system_tk():
    print("Missing 'tk' library. Auto-installing... / 'tk' kütüphanesi eksik, kuruluyor...")
    managers = {"apt-get": "python3-tk", "pacman": "tk", "dnf": "python3-tkinter"}
    for mgr, pkg in managers.items():
        if shutil.which(mgr):
            cmd = f"{mgr} install -y {pkg}" if mgr != "pacman" else f"pacman -S --noconfirm {pkg}"
            try:
                subprocess.check_call(cmd.split())
                return
            except subprocess.CalledProcessError:
                sys.exit(1)
    sys.exit(1)

try:
    import tkinter
except ImportError:
    install_system_tk()

# CustomTkinter Auto-Install
try:
    import customtkinter as ctk
except ImportError:
    print("Installing customtkinter... / CustomTkinter kuruluyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "--break-system-packages"])
    import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# --- INTERNAL TOOLS DATABASE ---
TOOLS = {
    "info": ["nmap", "masscan", "netdiscover", "dnsenum", "dnsrecon", "fierce", "theharvester", "whois", "bind-tools", "amass", "sublist3r", "recon-ng", "spiderfoot", "dmitry", "arp-scan", "p0f", "enum4linux", "smbclient"],
    "web": ["burpsuite", "zaproxy", "sqlmap", "gobuster", "nikto", "dirb", "dirbuster", "wfuzz", "wpscan", "whatweb", "caido", "skipfish", "uniscan", "wapiti", "commix", "ffuf", "xsser", "xsstrike", "w3af"],
    "pass": ["hashcat", "john", "hydra", "medusa", "ncrack", "crunch", "cupp", "wordlists", "cewl", "patator", "crowbar", "ophcrack", "fcrackzip", "pdfcrack"],
    "wifi": ["aircrack-ng", "kismet", "reaver", "wifite", "bully", "hcxdumptool", "hcxtools", "cowpatty", "fern-wifi-cracker", "macchanger", "mdk3", "mdk4"],
    "exploit": ["metasploit", "searchsploit", "beef", "routersploit", "social-engineer-toolkit", "sqlmap", "armitage", "exploitdb", "msfpc"],
    "sniff": ["wireshark-cli", "tcpdump", "bettercap", "ettercap", "responder", "macchanger", "mitmproxy", "dsniff", "netsniff-ng", "sslstrip", "scapy", "arpspoof"],
    "reverse": ["radare2", "ghidra", "apktool", "ltrace", "strace", "gdb", "binwalk", "dex2jar", "jd-cli", "edb-debugger", "jadx", "objdump"],
    "forensics": ["autopsy", "sleuthkit", "volatility3", "foremost", "scalpel", "exiftool", "chkrootkit", "rkhunter", "ddrescue", "guymager", "bulk_extractor"],
    "malware": ["yara", "clamav", "maldet", "cuckoo-sandbox"],
    "utils": ["tmux", "git", "curl", "wget", "htop", "neovim", "netcat", "proxychains", "tor", "openvpn", "docker", "wireguard-tools", "zsh", "steghide"]
}

PACKAGE_MAPPING = {
    "apt": {"wireshark-cli": "tshark", "bind-tools": "dnsutils", "metasploit": "metasploit-framework", "netcat": "netcat-traditional", "wordlists": "wordlists"},
    "pacman": {"wireshark-cli": "wireshark-cli", "bind-tools": "bind", "metasploit": "metasploit", "netcat": "gnu-netcat", "wordlists": "seclists", "burpsuite": "burpsuite", "zaproxy": "zaproxy"},
    "dnf": {"wireshark-cli": "wireshark", "bind-tools": "bind-utils", "netcat": "nc"}
}

# --- TRANSLATIONS (i18n) ---
T = {
    "en": {
        "main_title": "Rezonans CyberOS - Ultimate Setup Center",
        "sys_info": "System: {} Based | 120+ Selectable Security Tools",
        "lang_lbl": "Language / Dil:",
        "prof_lbl": "Quick Install Profile:",
        "prof_opts": ["Custom Selection", "Full Arsenal", "Web Pentester", "Network Admin", "Reset (None)"],
        "term_lbl": "SYSTEM OUTPUT (TERMINAL)",
        "term_init": "Rezonans OS Ultimate Interface Ready.\nSelect a profile or choose tools from the tabs above...\n",
        "harden": "Apply Kernel Level System Hardening (Sysctl)",
        "btn_inst": "INSTALL SELECTED PROFILE",
        "btn_doing": "INSTALLING SYSTEM...",
        "btn_done": "INSTALLATION COMPLETED",
        "err_pkg": "[ERROR] No supported package manager found!",
        "log_start": "\n[INFO] Installation Process Started...",
        "warn_no_sel": "[WARNING] No tools selected. Installation cancelled.",
        "inf_tot": "[INFO] A total of {} security tools will be installed.",
        "s1": "\n[PHASE 1] Updating System Repositories...",
        "s2": "\n[PHASE 2] Downloading Tools (Safe Single-Install Mode)...",
        "s2_dl": "\n---> Installing: {}",
        "s2_err": "[WARNING] '{}' not found or failed, skipping.",
        "s2_sum": "\n[SUMMARY] Successfully installed {} out of {} packages.",
        "s3": "\n[PHASE 3] System Hardening...",
        "s3_ok": "[SUCCESS] Network security hardened.",
        "ok_all": "\n[SUCCESS] Operation Completed. Your station is ready for duty!",
        "cat_info": "Info Gathering", "cat_web": "Web Vulns", "cat_pass": "Password Cracking", 
        "cat_wifi": "Wireless", "cat_exploit": "Exploitation", "cat_sniff": "Sniffing/Spoofing", 
        "cat_reverse": "Reverse Eng.", "cat_forensics": "Forensics", "cat_malware": "Malware Analysis", "cat_utils": "General Utils"
    },
    "tr": {
        "main_title": "Rezonans CyberOS - Ultimate Kurulum Merkezi",
        "sys_info": "Sistem: {} Tabanlı | 120+ Seçilebilir Siber Güvenlik Aracı",
        "lang_lbl": "Dil / Language:",
        "prof_lbl": "Hızlı Kurulum Profili:",
        "prof_opts": ["Özel Seçim", "Full Arsenal (Tümü)", "Web Pentester", "Ağ Uzmanı (Network)", "Sıfırla (Hiçbiri)"],
        "term_lbl": "SİSTEM ÇIKTISI (TERMINAL)",
        "term_init": "Rezonans OS Ultimate Arayüzü Hazır.\nBir kurulum profili seçin veya araçları belirleyin...\n",
        "harden": "Kernel Düzeyinde Sistem Sıkılaştırma Uygula (Hardening)",
        "btn_inst": "SEÇİLİ PROFİLİ KUR",
        "btn_doing": "SİSTEM KURULUYOR...",
        "btn_done": "KURULUM TAMAMLANDI",
        "err_pkg": "[HATA] Desteklenen bir paket yöneticisi bulunamadı!",
        "log_start": "\n[BİLGİ] Kurulum Süreci Başlatılıyor...",
        "warn_no_sel": "[UYARI] Hiçbir araç seçilmedi. Kurulum iptal edildi.",
        "inf_tot": "[BİLGİ] Toplam {} adet güvenlik aracı kurulacak.",
        "s1": "\n[AŞAMA 1] Sistem Depoları Güncelleniyor...",
        "s2": "\n[AŞAMA 2] Araçların İndirilmesi (Tek Tek Güvenli Mod)...",
        "s2_dl": "\n---> Yükleniyor: {}",
        "s2_err": "[UYARI] '{}' bulunamadı veya kurulamadı, atlanıyor.",
        "s2_sum": "\n[ÖZET] {} paketten {} tanesi başarıyla kuruldu.",
        "s3": "\n[AŞAMA 3] Sistem Sıkılaştırması (Hardening)...",
        "s3_ok": "[BAŞARILI] Ağ güvenliği sıkılaştırıldı.",
        "ok_all": "\n[BAŞARILI] İşlem Tamamlandı. İstasyonunuz Göreve Hazır!",
        "cat_info": "Bilgi Toplama", "cat_web": "Web Zafiyet", "cat_pass": "Parola Kırma", 
        "cat_wifi": "Kablosuz Ağ", "cat_exploit": "İstismar (Exploit)", "cat_sniff": "Sniffing/Spoofing", 
        "cat_reverse": "Tersine Müh.", "cat_forensics": "Adli Bilişim", "cat_malware": "Zararlı Yazılım", "cat_utils": "Genel Araçlar"
    }
}

CAT_KEYS = ["info", "web", "pass", "wifi", "exploit", "sniff", "reverse", "forensics", "malware", "utils"]

class CyberOSInstaller(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.lang = "en" # Default Language
        self.pkg_manager = self.detect_pkg_manager()
        self.setup_window()
        self.build_ui()

    def setup_window(self):
        self.geometry("1100x850")
        self.resizable(False, False)

    def detect_pkg_manager(self):
        for mgr in ["apt-get", "pacman", "dnf", "yum"]:
            if shutil.which(mgr): return "apt" if mgr == "apt-get" else mgr
        return None

    def change_language(self, choice):
        self.lang = "tr" if "Türkçe" in choice else "en"
        # Destroy all widgets and rebuild
        for widget in self.winfo_children():
            widget.destroy()
        self.build_ui()

    def build_ui(self):
        self.title(T[self.lang]["main_title"])
        self.checkboxes = {}
        
        # 1. HEADER AREA
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(pady=10, padx=20, fill="x")
        
        # Left side: Titles
        title_box = ctk.CTkFrame(top_frame, fg_color="transparent")
        title_box.pack(side="left")
        ctk.CTkLabel(title_box, text="REZONANS CyberOS", font=ctk.CTkFont(family="Courier", size=36, weight="bold"), text_color="#00FF41").pack(anchor="w")
        sys_str = "Unknown" if not self.pkg_manager else self.pkg_manager.upper()
        ctk.CTkLabel(title_box, text=T[self.lang]["sys_info"].format(sys_str), font=ctk.CTkFont(size=14), text_color="gray").pack(anchor="w")

        # Right side: Language Selector
        lang_box = ctk.CTkFrame(top_frame, fg_color="transparent")
        lang_box.pack(side="right", anchor="n")
        ctk.CTkLabel(lang_box, text=T[self.lang]["lang_lbl"], font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10)
        self.lang_opt = ctk.CTkOptionMenu(lang_box, values=["🇬🇧 English", "🇹🇷 Türkçe"], command=self.change_language)
        self.lang_opt.set("🇬🇧 English" if self.lang == "en" else "🇹🇷 Türkçe")
        self.lang_opt.pack(side="left")

        # 2. PROFILE AREA
        profile_frame = ctk.CTkFrame(self, fg_color="transparent")
        profile_frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(profile_frame, text=T[self.lang]["prof_lbl"], font=ctk.CTkFont(weight="bold", size=14)).pack(side="left", padx=10)
        
        self.profile_var = ctk.StringVar(value=T[self.lang]["prof_opts"][1]) # Default: Full Arsenal
        self.profile_segmented = ctk.CTkSegmentedButton(
            profile_frame, 
            values=T[self.lang]["prof_opts"],
            variable=self.profile_var,
            command=self.apply_profile,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.profile_segmented.pack(side="left", padx=10, fill="x", expand=True)

        # 3. MIDDLE AREA (Tabs & Terminal)
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Tabs
        self.tabview = ctk.CTkTabview(main_frame)
        self.tabview.pack(side="top", fill="both", expand=True, pady=(0, 10))
        
        for key in CAT_KEYS:
            cat_name = T[self.lang][f"cat_{key}"]
            packages = TOOLS[key]
            
            self.tabview.add(cat_name)
            self.checkboxes[key] = {}
            
            tab_scroll = ctk.CTkScrollableFrame(self.tabview.tab(cat_name), fg_color="transparent")
            tab_scroll.pack(fill="both", expand=True, padx=5, pady=5)
            
            row, col = 0, 0
            for pkg in packages:
                var = ctk.IntVar(value=1) # Default selected (Full Arsenal)
                cb = ctk.CTkCheckBox(tab_scroll, text=pkg, variable=var, font=ctk.CTkFont(size=14))
                cb.grid(row=row, column=col, padx=15, pady=8, sticky="w")
                self.checkboxes[key][pkg] = var
                
                col += 1
                if col > 3: # 4 columns
                    col = 0
                    row += 1

        # Terminal
        log_frame = ctk.CTkFrame(main_frame)
        log_frame.pack(side="bottom", fill="both", expand=True)
        ctk.CTkLabel(log_frame, text=T[self.lang]["term_lbl"], font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        
        self.log_textbox = ctk.CTkTextbox(log_frame, font=ctk.CTkFont(family="Courier", size=12), text_color="#00FF41", fg_color="#1E1E1E")
        self.log_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.log_textbox.insert("0.0", T[self.lang]["term_init"])
        self.log_textbox.configure(state="disabled")

        # 4. BOTTOM AREA (Hardening & Install)
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(pady=15, padx=20, fill="x")
        
        self.harden_var = ctk.IntVar(value=1)
        ctk.CTkCheckBox(bottom_frame, text=T[self.lang]["harden"], variable=self.harden_var).pack(side="left", padx=20)

        self.install_btn = ctk.CTkButton(bottom_frame, text=T[self.lang]["btn_inst"], font=ctk.CTkFont(size=16, weight="bold"), 
                                         fg_color="#008F11", hover_color="#00FF41", text_color="black", height=45,
                                         command=self.start_installation_thread)
        self.install_btn.pack(side="right", padx=20, pady=10)

    def apply_profile(self, profile_name):
        opts = T[self.lang]["prof_opts"]
        # Clear all
        for cat in self.checkboxes.values():
            for var in cat.values(): var.set(0)
                
        if profile_name == opts[1]: # Full Arsenal
            for cat in self.checkboxes.values():
                for var in cat.values(): var.set(1)
        elif profile_name == opts[2]: # Web Pentester
            for cat in ["web", "info", "pass", "utils"]:
                for var in self.checkboxes[cat].values(): var.set(1)
        elif profile_name == opts[3]: # Network Admin
            for cat in ["info", "wifi", "sniff", "utils", "reverse"]:
                for var in self.checkboxes[cat].values(): var.set(1)

    def log(self, message):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", f"{message}\n")
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def run_cmd(self, cmd):
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout: self.log(line.strip())
            process.wait()
            return process.returncode == 0
        except Exception as e:
            self.log(f"[ERROR] {str(e)}")
            return False

    def start_installation_thread(self):
        if not self.pkg_manager:
            self.log(T[self.lang]["err_pkg"])
            return
            
        self.install_btn.configure(state="disabled", text=T[self.lang]["btn_doing"])
        self.profile_segmented.configure(state="disabled")
        threading.Thread(target=self.install_process, daemon=True).start()

    def install_process(self):
        t = T[self.lang]
        self.log(t["log_start"])
        
        selected_packages = []
        for cat_key, packages in self.checkboxes.items():
            for pkg, var in packages.items():
                if var.get() == 1:
                    mapped_pkg = PACKAGE_MAPPING.get(self.pkg_manager, {}).get(pkg, pkg)
                    selected_packages.append(mapped_pkg)
        
        if not selected_packages:
            self.log(t["warn_no_sel"])
            self.install_btn.configure(state="normal", text=t["btn_inst"])
            self.profile_segmented.configure(state="normal")
            return

        self.log(t["inf_tot"].format(len(selected_packages)))
        
        # Phase 1
        self.log(t["s1"])
        if self.pkg_manager == "apt": self.run_cmd("apt-get update -y")
        elif self.pkg_manager == "pacman": self.run_cmd("pacman -Sy --noconfirm")
        elif self.pkg_manager == "dnf": self.run_cmd("dnf check-update")
            
        # Phase 2
        self.log(t["s2"])
        success_count = 0
        for pkg in selected_packages:
            self.log(t["s2_dl"].format(pkg))
            cmd = ""
            if self.pkg_manager == "apt": cmd = f"apt-get install -y {pkg}"
            elif self.pkg_manager == "pacman": cmd = f"pacman -S --noconfirm --needed {pkg}"
            elif self.pkg_manager == "dnf": cmd = f"dnf install -y {pkg}"
                
            if self.run_cmd(cmd): success_count += 1
            else: self.log(t["s2_err"].format(pkg))

        self.log(t["s2_sum"].format(success_count, len(selected_packages)))

        # Phase 3 (Hardening)
        if self.harden_var.get() == 1:
            self.log(t["s3"])
            sysctl = "net.ipv4.icmp_echo_ignore_broadcasts=1\\nnet.ipv4.tcp_syncookies=1"
            self.run_cmd(f"echo -e '{sysctl}' > /etc/sysctl.d/99-cybersecurity.conf")
            self.run_cmd("sysctl -p /etc/sysctl.d/99-cybersecurity.conf")
            self.log(t["s3_ok"])

        self.log(t["ok_all"])
        self.install_btn.configure(state="normal", text=t["btn_done"])
        self.profile_segmented.configure(state="normal")

if __name__ == "__main__":
    app = CyberOSInstaller()
    app.mainloop()
