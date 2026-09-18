# -*- coding: utf-8 -*-
# product.json'daki TUM checksum girdilerini canli dosyalarla eslesecek
# sekilde yeniden hesaplar (yalnizca tek dosyayi degil, hepsini).
import json, hashlib, base64, io, shutil, os

APP = r'C:\Program Files\cursor\resources\app'
shutil.copy2(os.path.join(APP, 'product.json'), 'product.json')
p = json.load(io.open('product.json', encoding='utf-8'))
for rel in list(p.get('checksums', {}).keys()):
    path = os.path.join(APP, 'out', *rel.split('/'))
    h = hashlib.sha256(open(path, 'rb').read()).digest()
    new_val = base64.b64encode(h).decode().rstrip('=')
    old_val = p['checksums'][rel]
    p['checksums'][rel] = new_val
    print(rel, '->', 'degisti' if old_val != new_val else 'ayni')
io.open('product.json', 'w', encoding='utf-8').write(json.dumps(p, indent='\t', ensure_ascii=False) + '\n')
print('product.json guncellendi (tum checksumlar canli dosyalarla eslesiyor)')
