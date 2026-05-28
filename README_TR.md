# 🛡️ Rezonans CyberOS

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)]()
[![Araçlar](https://img.shields.io/badge/G%C3%BCvenlik%20Ara%C3%A7lar%C4%B1-155+-red.svg)]()

> 🇬🇧 [Click for English version](README.md)

**Rezonans CyberOS**, herhangi bir Linux dağıtımını profesyonel bir siber güvenlik istasyonuna dönüştüren, sıfır bağımlılıklı terminal tabanlı kurulum aracıdır. Paket yöneticinizi otomatik algılar, 155+ güvenlik aracını kurar ve kernel düzeyinde sistem sıkılaştırması uygular — tamamı şık bir CLI arayüzünden.

---

## ✨ Temel Özellikler

| Özellik | Açıklama |
|---|---|
| 🎯 **Sıfır Bağımlılık** | GUI kütüphanesi yok, pip paketi yok — saf Python standart kütüphanesi |
| 🐧 **Evrensel Linux** | `apt`, `pacman`, `dnf` otomatik algılama — Arch, Ubuntu, Fedora, CachyOS vb. |
| 📦 **155+ Güvenlik Aracı** | Saldırı ve savunma güvenlik yelpazesini kapsayan 10 kategori |
| 🚀 **Akıllı AUR Desteği** | Arch tabanlı sistemlerde `paru`/`yay` ile AUR paketlerini doğrulayıp toplu kurar |
| 🔒 **Kernel Sıkılaştırma** | sysctl tabanlı ağ güvenliği (SYN flood, ICMP, IPv6, kaynak yönlendirme) |
| 🌍 **İngilizce & Türkçe** | Başlangıçta dil seçimi ile tam i18n desteği |
| 📊 **Canlı İlerleme Çubuğu** | Paket bazında gerçek zamanlı terminal ilerleme takibi |
| ⚡ **Ön Kontrol Motoru** | Kurulu paketleri atlayarak hızlı yeniden çalıştırma |

---

## 🚀 Hızlı Başlangıç

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/mefkuz/Rezonans_cyber.git
cd Rezonans_cyber
```

### 2. Kurulumu Başlatın
```bash
sudo python3 cyber_os_cli.py
```

Veya sudo olmadan çalıştırın — gerektiğinde şifrenizi soracaktır:
```bash
python3 cyber_os_cli.py
```

> **Hepsi bu kadar!** pip kurulumu yok, sanal ortam yok, yapılandırma dosyası yok. Sadece çalıştırın.

---

## 📋 Kurulum Profilleri

| # | Profil | Dahil Olan Kategoriler |
|---|---|---|
| 1 | **Full Arsenal (Tümü)** | 10 kategorinin tamamı — eksiksiz güvenlik istasyonu |
| 2 | **Web Pentester** | Bilgi Toplama, Web Zafiyet, Parola Kırma, Araçlar |
| 3 | **Ağ Uzmanı** | Bilgi Toplama, Kablosuz, Sniffing/Spoofing, Tersine Müh., Araçlar |
| 4 | **Adli Bilişim & Zararlı Analiz** | Adli Bilişim, Zararlı Yazılım, Tersine Müh., Araçlar |
| 5 | **Özel Seçim** | Kategorileri interaktif olarak seçin |

---

## 🧰 Araç Kategorileri

### 🔍 Bilgi Toplama (17 araç)
`nmap` · `masscan` · `netdiscover` · `dnsenum` · `dnsrecon` · `fierce` · `theharvester` · `whois` · `bind-tools` · `amass` · `sublist3r` · `spiderfoot` · `dmitry` · `arp-scan` · `p0f` · `enum4linux` · `smbclient`

### 🌐 Web Zafiyet (19 araç)
`burpsuite` · `zaproxy` · `sqlmap` · `gobuster` · `nikto` · `dirb` · `dirbuster` · `wfuzz` · `wpscan` · `whatweb` · `caido` · `skipfish` · `uniscan` · `wapiti` · `commix` · `ffuf` · `xsser` · `xsstrike` · `w3af`

### 🔑 Parola Kırma (13 araç)
`hashcat` · `john` · `hydra` · `medusa` · `ncrack` · `crunch` · `cupp` · `wordlists` · `cewl` · `crowbar` · `ophcrack` · `fcrackzip` · `pdfcrack`

### 📡 Kablosuz Ağ Saldırıları (12 araç)
`aircrack-ng` · `kismet` · `reaver` · `wifite` · `bully` · `hcxdumptool` · `hcxtools` · `cowpatty` · `fern-wifi-cracker` · `macchanger` · `mdk3` · `mdk4`

### 💣 İstismar / Exploitation (9 araç)
`metasploit` · `searchsploit` · `beef` · `routersploit` · `social-engineer-toolkit` · `sqlmap` · `armitage` · `exploitdb` · `msfpc`

### 🕵️ Sniffing / Spoofing (12 araç)
`wireshark-cli` · `tcpdump` · `bettercap` · `ettercap` · `responder` · `macchanger` · `mitmproxy` · `dsniff` · `netsniff-ng` · `sslstrip` · `scapy` · `arpspoof`

### ⚙️ Tersine Mühendislik (12 araç)
`radare2` · `ghidra` · `apktool` · `ltrace` · `strace` · `gdb` · `binwalk` · `dex2jar` · `jd-cli` · `edb-debugger` · `jadx` · `objdump`

### 🔬 Adli Bilişim (11 araç)
`autopsy` · `sleuthkit` · `volatility3` · `foremost` · `scalpel` · `exiftool` · `chkrootkit` · `rkhunter` · `ddrescue` · `guymager` · `bulk_extractor`

### 🦠 Zararlı Yazılım Analizi (4 araç)
`yara` · `clamav` · `maldet` · `cuckoo-sandbox`

### 🔧 Genel Araçlar (14 araç)
`tmux` · `git` · `curl` · `wget` · `htop` · `neovim` · `netcat` · `proxychains` · `tor` · `openvpn` · `docker` · `wireguard-tools` · `zsh` · `steghide`

---

## 🛡️ Sistem Sıkılaştırma

Etkinleştirildiğinde, kernel düzeyinde güvenlik politikaları uygulanır:

| Kural | Koruma |
|---|---|
| `net.ipv4.icmp_echo_ignore_broadcasts=1` | Smurf saldırılarını engeller |
| `net.ipv4.tcp_syncookies=1` | SYN Flood koruması |
| `net.ipv4.conf.all.accept_source_route=0` | Kaynak yönlendirmeli paketleri reddeder |
| `net.ipv6.conf.all.disable_ipv6=1` | IPv6'yı devre dışı bırakır (saldırı yüzeyini daraltır) |

---

## 🏗️ Mimari

```
cyber_os_cli.py          ← Tek dosya, sıfır bağımlılık CLI kurulumcusu
├── Dil Seçimi           ← İngilizce / Türkçe
├── Profil Seçimi        ← 5 hazır profil + özel seçim
├── Paket Motoru         ← apt/pacman/dnf otomatik algılama
│   ├── Ön Kontrol       ← Kurulu paketleri atla
│   ├── AUR Doğrulama    ← Var olmayan AUR paketlerini filtrele
│   └── Toplu Kurulum    ← paru/yay ile optimize edilmiş AUR toplu kurulum
├── İlerleme Takibi      ← Gerçek zamanlı terminal ilerleme çubuğu
└── Sistem Sıkılaştırma  ← sysctl kernel politikaları
```

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.

---

<p align="center">
  <b>Rezonans Ekibi tarafından 💚 ile geliştirildi</b><br>
  <i>Herhangi bir Linux'u siber silaha dönüştür.</i>
</p>
