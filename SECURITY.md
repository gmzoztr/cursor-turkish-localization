# Güvenlik Politikası (Security Policy)

Bu proje doğrudan Cursor Desktop kurulum dosyalarını ve Electron NLS önbelleğini yerelleştirir. Kullanıcı güvenliği ve sistem bütünlüğü en temel önceliğimizdir.

---

## 🛡️ Bütünlük & Güvenlik İlkeleri
* **Açık Kaynak Kod:** Projedeki tüm Python ve toplu iş betikleri tamamen şeffaftır, harici hiçbir yabancı ikili (binary) indirmez veya çalıştırmaz.
* **IntegrityService Uyumlu:** `product.json` içerisindeki Base64 SHA-256 bütünlük imzaları matematiksel olarak hesaplanır ve doğrulanır.
* **Orijinal Yedekleme:** Her kurulum öncesinde orijinal dosyalar `orijinal-<sürüm>/` klasörüne yedeklenir. İstendiğinde `ORIJINALE_DON.bat` ile anında fabrika ayarlarına dönülebilir.

## 🚨 Güvenlik Açığı Bildirimi
Herhangi bir güvenlik veya kararlılık sorunu tespit ederseniz lütfen GitHub Issues üzerinden genel bildirim yapmak yerine doğrudan `abdurrahmanavci@gmail.com` adresine e-posta gönderin.
