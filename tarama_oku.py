#!/usr/bin/env python3
"""
tarama_oku.py - cursor-tr-tarama.json dosyasını okur ve
patch_menu_gaps.py için çeviri satırları önerir.

Kullanım:
  python tarama_oku.py                    # varsayılan: ~/cursor-tr-tarama.json
  python tarama_oku.py C:\baska\yol.json  # özel yol
"""

import json, sys, os, re

SKIP_PATTERNS = [
    r'^https?://',           # URL
    r'^[\w./-]+\.(js|ts|py|json|md|css|html|png|svg|woff)$',  # dosya adı
    r'^[A-Z0-9_]{4,}$',     # sabit / enum (ALL_CAPS)
    r'^\$\{',                # template literal
    r'^--',                  # CSS değişkeni
    r'^[a-z][a-zA-Z0-9]*\(',  # fonksiyon çağrısı
    r'cursor\.com',          # domain
    r'^v\d+\.\d+',           # sürüm numarası
    r'^\w+\.\w+',            # obje/property erişimi
]

def should_skip(text):
    for pat in SKIP_PATTERNS:
        if re.search(pat, text):
            return True
    return False

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/cursor-tr-tarama.json")
    if not os.path.exists(path):
        print(f"HATA: {path} bulunamadı.")
        print("Önce Cursor açıkken Alt+T tuşlarına basın.")
        return

    with open(path, encoding="utf-8") as f:
        items = json.load(f)

    print(f"Toplam: {len(items)} string tarandı.\n")
    
    filtered = [x for x in items if not should_skip(x["text"])]
    print(f"Filtrelendikten sonra: {len(filtered)} muhtemel UI string.\n")
    print("=" * 60)
    print("patch_menu_gaps.py için önerilen çeviri satırları:")
    print("(CTRL+C ile kopyala, translations Map'e yapıştır)")
    print("=" * 60)
    print()

    for item in filtered:
        t = item["text"].replace('"', '\\"')
        ctx = item.get("ctx", "")
        print(f'    ["{t}", "???"],  # ctx: {ctx[:50]}')

    print()
    print(f"Toplam {len(filtered)} satır. '???' yerine Türkçe karşılıkları yaz.")

if __name__ == "__main__":
    main()
