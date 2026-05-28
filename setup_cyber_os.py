#!/usr/bin/env python3
"""
Universal CyberOS Setup Script
Bu betik, herhangi bir Linux dağıtımını (CachyOS, Ubuntu, Fedora vb.) 
otomatik olarak siber güvenlik odaklı bir ortama dönüştürür.
"""

import os
import subprocess
import sys
import shutil

BANNER = """
   _____       __               ______                       
  / ___/      / /_  ___  ____  / ____/___  _________ ____  
  \__ \      / __ \/ _ \/ __ \/ /_  / __ \/ ___/ __ `/ _ \ 
 ___/ /     / / / /  __/ /_/ / __/ / /_/ / /  / /_/ /  __/ 
/____/     /_/ /_/\___/\____/_/    \____/_/   \__, /\___/  
                                             /____/        
       Universal Cyber Security OS Setup Script
"""

# Kurulacak temel araç kategorileri
TOOLS = {
    "network": ["nmap", "tcpdump", "netcat"],
    "web": ["sqlmap", "gobuster", "nikto"],
    "passwords": ["hashcat", "john"],
    "utils": ["tmux", "git", "curl", "wget", "htop", "neovim"]
}

# Dağıtımlara göre paket adı farklılıkları varsa buraya eklenir
PACKAGE_MAPPING = {
    "apt": {
        "netcat": "netcat-traditional"
    },
    "pacman": {
        "netcat": "gnu-netcat"
    },
    "dnf": {
        "netcat": "nc"
    }
}

class CyberOSBuilder:
    def __init__(self):
        self.pkg_manager = self.detect_pkg_manager()
        
    def detect_pkg_manager(self):
        managers = ["apt-get", "pacman", "dnf", "yum", "zypper"]
        for mgr in managers:
            if shutil.which(mgr):
                return "apt" if mgr == "apt-get" else mgr
        return None

    def print_status(self, msg, status="INFO"):
        colors = {"INFO": "\033[94m", "SUCCESS": "\033[92m", "ERROR": "\033[91m", "WARN": "\033[93m", "ENDC": "\033[0m"}
        print(f"[{colors.get(status, '')}{status}{colors['ENDC']}] {msg}")

    def run_cmd(self, cmd, show_output=False):
        try:
            if show_output:
                subprocess.run(cmd, shell=True, check=True)
            else:
                subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False

    def install_packages(self):
        if not self.pkg_manager:
            self.print_status("Desteklenen paket yöneticisi bulunamadı (apt, pacman, dnf vb. gerekli)!", "ERROR")
            sys.exit(1)
            
        self.print_status(f"Paket yöneticisi algılandı: {self.pkg_manager.upper()}", "SUCCESS")
        
        self.print_status("Sistem depoları güncelleniyor...", "INFO")
        if self.pkg_manager == "apt":
            self.run_cmd("sudo apt-get update -y")
        elif self.pkg_manager == "pacman":
            self.run_cmd("sudo pacman -Sy --noconfirm")
        elif self.pkg_manager == "dnf":
            self.run_cmd("sudo dnf check-update")
            
        all_tools = []
        for category, pkgs in TOOLS.items():
            for pkg in pkgs:
                mapped_pkg = PACKAGE_MAPPING.get(self.pkg_manager, {}).get(pkg, pkg)
                all_tools.append(mapped_pkg)
                
        self.print_status(f"Siber güvenlik araçları kuruluyor ({len(all_tools)} paket)...", "INFO")
        
        install_cmd = ""
        if self.pkg_manager == "apt":
            install_cmd = f"sudo apt-get install -y {' '.join(all_tools)}"
        elif self.pkg_manager == "pacman":
            install_cmd = f"sudo pacman -S --noconfirm --needed {' '.join(all_tools)}"
        elif self.pkg_manager == "dnf":
            install_cmd = f"sudo dnf install -y {' '.join(all_tools)}"
            
        if self.run_cmd(install_cmd, show_output=True):
            self.print_status("Tüm araçlar başarıyla kuruldu!", "SUCCESS")
        else:
            self.print_status("Bazı paketlerin kurulumunda hata oluştu. Depolarınız eksik olabilir.", "WARN")

    def harden_system(self):
        self.print_status("Sistem Sıkılaştırma (Hardening) politikaları uygulanıyor...", "INFO")
        
        sysctl_conf = "/etc/sysctl.d/99-cybersecurity.conf"
        config = [
            "net.ipv4.icmp_echo_ignore_broadcasts = 1",  # Smurf ataklarını engelle
            "net.ipv4.conf.all.accept_source_route = 0", # Kaynak yönlendirmeli paketleri reddet
            "net.ipv4.tcp_syncookies = 1",               # SYN Flood ataklarına karşı koruma
            "net.ipv6.conf.all.disable_ipv6 = 1"         # Kullanılmıyorsa IPv6'yı kapat (güvenlik yüzeyi daraltma)
        ]
        
        config_str = "\\n".join(config)
        cmd = f"echo -e '{config_str}' | sudo tee {sysctl_conf}"
        
        if self.run_cmd(cmd):
            self.run_cmd("sudo sysctl -p /etc/sysctl.d/99-cybersecurity.conf")
            self.print_status("Kernel ağ güvenlik ayarları yapılandırıldı.", "SUCCESS")
        else:
            self.print_status("Sıkılaştırma yapılamadı (Root yetkisi eksik olabilir).", "WARN")

    def add_aliases(self):
        self.print_status("Terminal için Hacking kısayolları (Aliases) ekleniyor...", "INFO")
        aliases = """
# --- CyberOS Hızlı Komutlar ---
alias ports='sudo netstat -tulanp'
alias myip='curl ifconfig.me'
alias update_sys='sudo pacman -Syu || sudo apt update && sudo apt upgrade -y'
alias scan_local='nmap -sn 192.168.1.0/24'
"""
        try:
            bashrc_path = os.path.expanduser("~/.bashrc")
            with open(bashrc_path, "a") as f:
                f.write(aliases)
            self.print_status("Kısayollar ~/.bashrc dosyasına eklendi.", "SUCCESS")
        except Exception as e:
             self.print_status("Kısayollar eklenemedi.", "WARN")

    def run(self):
        print(BANNER)
        if os.geteuid() != 0:
            self.print_status("Dikkat: Betiği root olarak çalıştırmadınız. Sudo parolası istenecektir.", "WARN")
            
        self.install_packages()
        self.harden_system()
        self.add_aliases()
        
        print("\n")
        self.print_status("Kurulum Tamamlandı! İşletim sisteminiz artık bir Siber Güvenlik İstasyonu.", "SUCCESS")
        self.print_status("Değişikliklerin tamamen aktif olması için terminali yeniden başlatın.", "INFO")

if __name__ == "__main__":
    builder = CyberOSBuilder()
    builder.run()
