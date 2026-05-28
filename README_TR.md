<div align="center">
  <h1>⚡ Rezonans CyberOS Kurulum Merkezi</h1>
  <p><i>Sıradan Bir Linux Dağıtımını Siber Güvenlik İstasyonuna Dönüştürün</i></p>

  [![Language: Python](https://img.shields.io/badge/Dil-Python3-blue.svg?style=for-the-badge&logo=python)](#)
  [![OS: Linux](https://img.shields.io/badge/İS-Linux-green.svg?style=for-the-badge&logo=linux)](#)
  [![License: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg?style=for-the-badge)](#)
  
  <br>
  <i>Bu dokümanı farklı dillerde okuyun:</i><br>
  <b><a href="README.md">🇬🇧 English</a></b>
</div>

<hr>

**Rezonans CyberOS**, standart bir Linux dağıtımını (Arch/CachyOS, Debian/Ubuntu, Fedora) tek tıkla profesyonel bir siber güvenlik ve sızma testi (pentest) laboratuvarına dönüştüren gelişmiş bir otomasyon aracıdır.

Güvenlik araçlarını terminalden tek tek indirmek yerine, Rezonans OS'un sunduğu modern arayüz (GUI) sayesinde kendi siber güvenlik arşivinizi saniyeler içinde inşa edebilirsiniz.

## ✨ Öne Çıkan Özellikler

* 🛡️ **120+ Siber Güvenlik Aracı**: Bilgi Toplama, Web Zafiyetleri, Parola Kırma, İstismar, Zararlı Yazılım Analizi gibi 9 farklı kategoride sektör standardı araçlar.
* 🎛️ **Modern Arayüz (GUI)**: CustomTkinter ile hazırlanmış koyu temalı, ferah ve kullanımı kolay, sekmeli "Cyberpunk" tasarımı.
* 🚀 **Tek Tıkla Kurulum Profilleri**: 
  * `Web Pentester`: Sadece web odaklı çalışmak isteyenlere özel (BurpSuite, ZAP, SQLMap).
  * `Ağ Uzmanı`: Ağ analizi ve kablosuz ağ sızma testleri için (Wireshark, Aircrack-ng).
  * `Full Arsenal`: 120+ aracın tamamını kurarak bilgisayarınızı tam donanımlı bir istasyona çevirir.
* 🧠 **Akıllı Paket Yönetimi**: Sisteminizin `pacman`, `apt` veya `dnf` kullandığını otomatik algılar, komutları buna göre uyarlar.
* 🔒 **Sistem Sıkılaştırma (Hardening)**: Bilgisayarınızı ağ saldırılarına karşı korumak için Kernel düzeyinde (Sysctl) SYN Flood ve Smurf Attack korumalarını aktif eder.

## 📥 Kurulum ve Kullanım

Sistem paketlerine ve Kernel ayarlarına müdahale ettiği için bu aracın **root (`sudo`) yetkisiyle** çalıştırılması zorunludur.

### 1. Depoyu İndirin
```bash
git clone https://github.com/mefkuz/Rezonans_cyber.git
cd Rezonans_cyber
```

### 2. Arayüzü Başlatın
```bash
sudo python3 cyber_os_gui.py
```
> **Arch/CachyOS Kullanıcıları İçin Not**: Script, arayüzün açılması için gereken Python kütüphanelerini (PEP 668 engeline takılmadan) arka planda otomatik olarak sizin yerinize kuracaktır.

### ⚠️ Sorun Giderme (Wayland / Segmentation Fault Hatası)
Eğer arayüzü başlatırken anında `Segmentation fault` hatası alıp çöküyorsa, bu durum Wayland görüntü sunucusunun root (sudo) yetkisiyle grafik arayüz açılmasını engellemesinden kaynaklanır. Çözüm için şu iki yöntemden birini kullanın:

**Yöntem A (Önerilen):** Ortam değişkenlerini koruyarak çalıştırın
```bash
sudo -E python3 cyber_os_gui.py
```

**Yöntem B:** Ekran yetkilerini kök kullanıcıya da atayın
```bash
xhost +si:localuser:root
sudo python3 cyber_os_gui.py
```

## 🧰 İçerdiği Başlıca Araç Kategorileri
- **Bilgi Toplama (Recon)**: `nmap`, `masscan`, `recon-ng`, `spiderfoot`...
- **Web Zafiyet (Web Pentest)**: `burpsuite`, `zaproxy`, `caido`, `sqlmap`...
- **Parola Kırma (Cracking)**: `hashcat`, `john`, `hydra`, `wordlists`...
- **Kablosuz Ağ (Wireless)**: `aircrack-ng`, `kismet`, `wifite`...
- **İstismar (Exploiting)**: `metasploit`, `searchsploit`, `beef`...
- **Ağ Koklama (Sniffing)**: `wireshark`, `bettercap`, `responder`...
- **Tersine Mühendislik (Reverse Eng)**: `ghidra`, `radare2`, `apktool`...
- **Adli Bilişim & Zararlı Yazılım**: `volatility3`, `autopsy`, `yara`, `clamav`...
- **Genel Araçlar**: `tmux`, `docker`, `tor`, `proxychains`...

## 🤝 Katkıda Bulunun
Bu repoyu çatallayabilir (fork), kendi geliştirmelerinizi Pull Request olarak gönderebilir veya araç veritabanına yeni toolların eklenmesini talep edebilirsiniz!
