# -*- coding: utf-8 -*-
# Ayar acilir listelerinin secenek etiketleri.
import io

reps = [
 # Metin Boyutu secenekleri (deger->etiket esleme fonksiyonu)
 ('case .85:return"Small";case 1:return"Default";case 1.15:return"Large";case 1.3:return"Extra Large"',
  'case .85:return"Küçük";case 1:return"Varsayılan";case 1.15:return"Büyük";case 1.3:return"Çok Büyük"'),
 # value/label ciftleri (value anahtar kalir, yalnizca label cevrilir)
 ('value:"cloud",label:"Cloud"', 'value:"cloud",label:"Bulut"'),
 ('value:"local",label:"Local"', 'value:"local",label:"Yerel"'),
 ('value:"user",label:"Local"', 'value:"user",label:"Yerel"'),
 ('value:"user",label:"User"', 'value:"user",label:"Kullanıcı"'),
 ('value:"project",label:"Workspace"', 'value:"project",label:"Çalışma Alanı"'),
 ('value:"plugin",label:"Plugin"', 'value:"plugin",label:"Eklenti"'),
 ('value:"all",label:"All"', 'value:"all",label:"Tümü"'),
 ('value:"name",label:"Name"', 'value:"name",label:"Ad"'),
 ('value:"team",label:"Team"', 'value:"team",label:"Ekip"'),
 ('value:"status",label:"Status"', 'value:"status",label:"Durum"'),
 ('value:"scope",label:"Scope"', 'value:"scope",label:"Kapsam"'),
 ('value:"author",label:"Author"', 'value:"author",label:"Yazar"'),
 ('value:"clear",label:"Clear Notification"', 'value:"clear",label:"Bildirimi Temizle"'),
]

for fname in ["workbench.desktop.main.js", "workbench.glass.main.js"]:
    s = io.open(fname, encoding="utf-8").read()
    total = 0
    for a, b in reps:
        c = s.count(a)
        if c:
            s = s.replace(a, b)
            total += c
    io.open(fname, "w", encoding="utf-8", newline="").write(s)
    print(fname, "degisim:", total)
