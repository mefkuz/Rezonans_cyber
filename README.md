# Rezonans CyberOS Setup

**Rezonans CyberOS**, herhangi bir Linux dağıtımını (Arch/CachyOS, Debian/Ubuntu, Fedora) tek tıkla profesyonel bir siber güvenlik ve sızma testi (pentest) laboratuvarına dönüştüren gelişmiş bir otomasyon ve kurulum aracıdır.

## 🚀 Özellikler

- **120+ Siber Güvenlik Aracı:** Bilgi Toplama, Web Zafiyet Analizi, Parola Kırma, İstismar (Exploiting), Tersine Mühendislik ve Adli Bilişim gibi 9 farklı kategoride sektör standardı araçlar (BurpSuite, Metasploit, Ghidra, Wireshark vb.).
- **Hazır Profiller:** 
  - `Web Pentester`: Sadece web odaklı araçlar.
  - `Ağ Uzmanı`: Ağ analizi ve kablosuz ağ kırma araçları.
  - `Full Arsenal`: Sisteme devasa bir hack arşivi kurar.
- **Akıllı Paket Yöneticisi Algılama:** Sisteminizin `pacman`, `apt` veya `dnf` kullandığını otomatik algılar.
- **Sistem Sıkılaştırma (Hardening):** Kernel düzeyinde Sysctl ayarlarıyla ağ güvenlik sıkılaştırması yapar (SYN Flood koruması, Smurf Attack engeli vb.).
- **Modern Arayüz (GUI):** CustomTkinter ile hazırlanmış koyu temalı, neon yeşil detaylı "Cyberpunk" tarzı kullanıcı arayüzü.

## 📥 Kurulum & Kullanım

Arayüzün paketleri yükleyebilmesi ve sistem ayarlarına müdahale edebilmesi için `root` yetkisiyle çalıştırılması zorunludur.

```bash
git clone https://github.com/KULLANICI_ADIN/RezonansOS.git
cd RezonansOS
sudo python3 cyber_os_gui.py
```

*Not: Sisteminizde arayüz için gerekli kütüphaneler yoksa, araç kendi kendine indirecek ve kurulum ekranını otomatik olarak başlatacaktır.*
