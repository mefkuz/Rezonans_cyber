#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import threading
import shutil

# --- Root (Sudo) Yetki Kontrolü ---
if os.geteuid() != 0:
    print("\n[HATA] ERİŞİM REDDEDİLDİ!")
    print("Bu arayüz sistem paketlerine ve Kernel ayarlarına müdahale ettiği için ROOT (sudo) yetkisi gerektirir.")
    print("Lütfen terminalden şu komutla tekrar çalıştırın:\n")
    print("    sudo python3 " + os.path.abspath(__file__) + "\n")
    sys.exit(1)

# --- Tkinter Sistem Kütüphanesi (C Kütüphanesi) Kontrolü ---
def install_system_tk():
    print("Sistemde arayüz çizimi için gereken 'tk' kütüphanesi eksik. Otomatik kuruluyor...")
    managers = {"apt-get": "python3-tk", "pacman": "tk", "dnf": "python3-tkinter"}
    for mgr, pkg in managers.items():
        if shutil.which(mgr):
            cmd = f"{mgr} install -y {pkg}" if mgr != "pacman" else f"pacman -S --noconfirm {pkg}"
            try:
                subprocess.check_call(cmd.split())
                print(f"[BAŞARILI] {pkg} sisteme kuruldu!")
                return
            except subprocess.CalledProcessError:
                print(f"[HATA] {pkg} kurulamadı. Lütfen manuel kurmayı deneyin.")
                sys.exit(1)
    print("Desteklenen paket yöneticisi bulunamadı. Lütfen 'tk' paketini manuel kurun.")
    sys.exit(1)

try:
    import tkinter
except ImportError:
    install_system_tk()

# CustomTkinter kontrolü ve otomatik kurulum
try:
    import customtkinter as ctk
except ImportError:
    print("Arayüz için gerekli olan 'customtkinter' kütüphanesi bulunamadı. Kuruluyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter", "--break-system-packages"])
    import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# --- Kapsamlı Araç Veritabanı (120+ Araç) ---
TOOLS = {
    "Bilgi Toplama": ["nmap", "masscan", "netdiscover", "dnsenum", "dnsrecon", "fierce", "theharvester", "whois", "bind-tools", "amass", "sublist3r", "recon-ng", "spiderfoot", "dmitry", "arp-scan", "p0f", "enum4linux", "smbclient"],
    "Web Zafiyet": ["burpsuite", "zaproxy", "sqlmap", "gobuster", "nikto", "dirb", "dirbuster", "wfuzz", "wpscan", "whatweb", "caido", "skipfish", "uniscan", "wapiti", "commix", "ffuf", "xsser", "xsstrike", "w3af"],
    "Parola Kırma": ["hashcat", "john", "hydra", "medusa", "ncrack", "crunch", "cupp", "wordlists", "cewl", "patator", "crowbar", "ophcrack", "fcrackzip", "pdfcrack"],
    "Kablosuz Ağ": ["aircrack-ng", "kismet", "reaver", "wifite", "bully", "hcxdumptool", "hcxtools", "cowpatty", "fern-wifi-cracker", "macchanger", "mdk3", "mdk4"],
    "İstismar (Exploit)": ["metasploit", "searchsploit", "beef", "routersploit", "social-engineer-toolkit", "sqlmap", "armitage", "exploitdb", "msfpc"],
    "Sniffing/Spoofing": ["wireshark-cli", "tcpdump", "bettercap", "ettercap", "responder", "macchanger", "mitmproxy", "dsniff", "netsniff-ng", "sslstrip", "scapy", "arpspoof"],
    "Tersine Müh.": ["radare2", "ghidra", "apktool", "ltrace", "strace", "gdb", "binwalk", "dex2jar", "jd-cli", "edb-debugger", "jadx", "objdump"],
    "Adli Bilişim": ["autopsy", "sleuthkit", "volatility3", "foremost", "scalpel", "exiftool", "chkrootkit", "rkhunter", "ddrescue", "guymager", "bulk_extractor"],
    "Zararlı Yazılım": ["yara", "clamav", "maldet", "cuckoo-sandbox"],
    "Genel Araçlar": ["tmux", "git", "curl", "wget", "htop", "neovim", "netcat", "proxychains", "tor", "openvpn", "docker", "wireguard-tools", "zsh", "steghide"]
}

PACKAGE_MAPPING = {
    "apt": {
        "wireshark-cli": "tshark", "bind-tools": "dnsutils", "metasploit": "metasploit-framework", 
        "netcat": "netcat-traditional", "wordlists": "wordlists"
    },
    "pacman": {
        "wireshark-cli": "wireshark-cli", "bind-tools": "bind", "metasploit": "metasploit", 
        "netcat": "gnu-netcat", "wordlists": "seclists", "burpsuite": "burpsuite",
        "zaproxy": "zaproxy"
    },
    "dnf": {
        "wireshark-cli": "wireshark", "bind-tools": "bind-utils", "netcat": "nc"
    }
}

class CyberOSInstaller(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Rezonans CyberOS - Ultimate Kurulum Merkezi")
        self.geometry("1100x850")
        self.resizable(False, False)
        
        self.pkg_manager = self.detect_pkg_manager()
        self.checkboxes = {}
        
        self.setup_ui()

    def detect_pkg_manager(self):
        managers = ["apt-get", "pacman", "dnf", "yum"]
        for mgr in managers:
            if shutil.which(mgr):
                return "apt" if mgr == "apt-get" else mgr
        return None

    def setup_ui(self):
        # 1. Ana Başlık Alanı
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(title_frame, text="REZONANS CyberOS", font=ctk.CTkFont(family="Courier", size=36, weight="bold"), text_color="#00FF41").pack()
        sys_info = f"Sistem: {self.pkg_manager.upper() if self.pkg_manager else 'Bilinmiyor'} Tabanlı | 120+ Seçilebilir Siber Güvenlik Aracı"
        ctk.CTkLabel(title_frame, text=sys_info, font=ctk.CTkFont(size=14), text_color="gray").pack()

        # --- YENİ EKLENEN: PROFİL SEÇİMİ BARI ---
        profile_frame = ctk.CTkFrame(self, fg_color="transparent")
        profile_frame.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(profile_frame, text="Hızlı Kurulum Profili:", font=ctk.CTkFont(weight="bold", size=14)).pack(side="left", padx=10)
        
        self.profile_var = ctk.StringVar(value="Full Arsenal (Tümü)")
        self.profile_segmented = ctk.CTkSegmentedButton(
            profile_frame, 
            values=["Özel Seçim", "Full Arsenal (Tümü)", "Web Pentester", "Ağ Uzmanı (Network)", "Sıfırla (Hiçbiri)"],
            variable=self.profile_var,
            command=self.apply_profile,
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.profile_segmented.pack(side="left", padx=10, fill="x", expand=True)

        # 2. Orta Alan (Araç Seçimi ve Loglar - Yatay Geniş Düzen)
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # --- Üst Kısım: TABVIEW (Sekmeli Yapı) ---
        self.tabview = ctk.CTkTabview(main_frame)
        self.tabview.pack(side="top", fill="both", expand=True, pady=(0, 10))
        
        for category, packages in TOOLS.items():
            self.tabview.add(category)
            self.checkboxes[category] = {}
            
            tab_scroll = ctk.CTkScrollableFrame(self.tabview.tab(category), fg_color="transparent")
            tab_scroll.pack(fill="both", expand=True, padx=5, pady=5)
            
            row = 0
            col = 0
            for pkg in packages:
                var = ctk.IntVar(value=1) # Varsayılan: Full Arsenal modunda başlıyor
                cb = ctk.CTkCheckBox(tab_scroll, text=pkg, variable=var, font=ctk.CTkFont(size=14))
                cb.grid(row=row, column=col, padx=15, pady=8, sticky="w")
                self.checkboxes[category][pkg] = var
                
                col += 1
                if col > 3: # 4 sütunlu yapı (Geniş ekranı tam kullanmak için)
                    col = 0
                    row += 1

        # --- Alt Kısım: Kurulum Detayları (Genişletilmiş Log Ekranı) ---
        log_frame = ctk.CTkFrame(main_frame)
        log_frame.pack(side="bottom", fill="both", expand=True)
        
        ctk.CTkLabel(log_frame, text="SİSTEM ÇIKTISI (TERMINAL)", font=ctk.CTkFont(size=12, weight="bold")).pack(pady=5)
        
        self.log_textbox = ctk.CTkTextbox(log_frame, font=ctk.CTkFont(family="Courier", size=12), text_color="#00FF41", fg_color="#1E1E1E")
        self.log_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.log_textbox.insert("0.0", "Rezonans OS Ultimate Arayüzü Hazır.\nBir kurulum profili seçin veya araçları belirleyin...\n")
        self.log_textbox.configure(state="disabled")

        # 3. Alt Alan (Sıkılaştırma Seçeneği ve Kurulum Butonu)
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(pady=15, padx=20, fill="x")
        
        self.harden_var = ctk.IntVar(value=1)
        ctk.CTkCheckBox(bottom_frame, text="Kernel Düzeyinde Sistem Sıkılaştırma Uygula (Hardening)", 
                        variable=self.harden_var).pack(side="left", padx=20)

        self.install_btn = ctk.CTkButton(bottom_frame, text="SEÇİLİ PROFİLİ KUR", font=ctk.CTkFont(size=16, weight="bold"), 
                                         fg_color="#008F11", hover_color="#00FF41", text_color="black", height=45,
                                         command=self.start_installation_thread)
        self.install_btn.pack(side="right", padx=20, pady=10)

    def apply_profile(self, profile_name):
        """Seçilen profile göre checkbox'ları otomatik işaretler"""
        # Önce tüm işaretleri kaldır
        for cat in self.checkboxes.values():
            for var in cat.values():
                var.set(0)
                
        if profile_name == "Full Arsenal (Tümü)":
            for cat in self.checkboxes.values():
                for var in cat.values():
                    var.set(1)
        
        elif profile_name == "Web Pentester":
            active_cats = ["Web Zafiyet", "Bilgi Toplama", "Parola Kırma", "Genel Araçlar"]
            for cat in active_cats:
                if cat in self.checkboxes:
                    for var in self.checkboxes[cat].values():
                        var.set(1)
                        
        elif profile_name == "Ağ Uzmanı (Network)":
            active_cats = ["Bilgi Toplama", "Kablosuz Ağ", "Sniffing/Spoofing", "Genel Araçlar", "Tersine Müh."]
            for cat in active_cats:
                if cat in self.checkboxes:
                    for var in self.checkboxes[cat].values():
                        var.set(1)
                        
        # "Sıfırla" ise hepsi 0 kalır. "Özel Seçim" kullanıcının tıklarına bırakılır.

    def log(self, message):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", f"{message}\n")
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def run_cmd(self, cmd):
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.log(line.strip())
            process.wait()
            return process.returncode == 0
        except Exception as e:
            self.log(f"[HATA] {str(e)}")
            return False

    def start_installation_thread(self):
        if not self.pkg_manager:
            self.log("[HATA] Desteklenen bir paket yöneticisi bulunamadı!")
            return
            
        if os.geteuid() != 0:
            self.log("[UYARI] Arayüzü root yetkisi (sudo) olmadan çalıştırdınız.")
            self.log("[BİLGİ] İndirme işlemleri başarısız olabilir.")
            
        self.install_btn.configure(state="disabled", text="SİSTEM KURULUYOR...")
        self.profile_segmented.configure(state="disabled")
        threading.Thread(target=self.install_process, daemon=True).start()

    def install_process(self):
        self.log("\n[BİLGİ] Kurulum Süreci Başlatılıyor...")
        
        selected_packages = []
        for category, packages in self.checkboxes.items():
            for pkg, var in packages.items():
                if var.get() == 1:
                    mapped_pkg = PACKAGE_MAPPING.get(self.pkg_manager, {}).get(pkg, pkg)
                    selected_packages.append(mapped_pkg)
        
        if not selected_packages:
            self.log("[UYARI] Hiçbir araç seçilmedi. Kurulum iptal edildi.")
            self.install_btn.configure(state="normal", text="SEÇİLİ PROFİLİ KUR")
            self.profile_segmented.configure(state="normal")
            return

        self.log(f"[BİLGİ] Toplam {len(selected_packages)} adet güvenlik aracı kurulacak.")
        
        # Depo Güncelleme
        self.log("\n[AŞAMA 1] Sistem Depoları Güncelleniyor...")
        if self.pkg_manager == "apt":
            self.run_cmd("apt-get update -y")
        elif self.pkg_manager == "pacman":
            self.run_cmd("pacman -Sy --noconfirm")
        elif self.pkg_manager == "dnf":
            self.run_cmd("dnf check-update")
            
        # Paketleri Kurma
        self.log("\n[AŞAMA 2] Araçların İndirilmesi (Tek Tek Güvenli Mod)...")
        success_count = 0
        for pkg in selected_packages:
            self.log(f"\n---> Yükleniyor: {pkg}")
            cmd = ""
            if self.pkg_manager == "apt":
                cmd = f"apt-get install -y {pkg}"
            elif self.pkg_manager == "pacman":
                cmd = f"pacman -S --noconfirm --needed {pkg}"
            elif self.pkg_manager == "dnf":
                cmd = f"dnf install -y {pkg}"
                
            if self.run_cmd(cmd):
                success_count += 1
            else:
                self.log(f"[UYARI] '{pkg}' bulunamadı veya kurulamadı, atlanıyor.")

        self.log(f"\n[ÖZET] {len(selected_packages)} paketten {success_count} tanesi başarıyla kuruldu.")

        # Hardening
        if self.harden_var.get() == 1:
            self.log("\n[AŞAMA 3] Sistem Sıkılaştırması (Hardening)...")
            sysctl_config = "net.ipv4.icmp_echo_ignore_broadcasts=1\\nnet.ipv4.tcp_syncookies=1"
            self.run_cmd(f"echo -e '{sysctl_config}' > /etc/sysctl.d/99-cybersecurity.conf")
            self.run_cmd("sysctl -p /etc/sysctl.d/99-cybersecurity.conf")
            self.log("[BAŞARILI] Ağ güvenliği sıkılaştırıldı.")

        self.log("\n[BAŞARILI] İşlem Tamamlandı. İstasyonunuz Göreve Hazır!")
        self.install_btn.configure(state="normal", text="KURULUM TAMAMLANDI")
        self.profile_segmented.configure(state="normal")

if __name__ == "__main__":
    app = CyberOSInstaller()
    app.mainloop()
