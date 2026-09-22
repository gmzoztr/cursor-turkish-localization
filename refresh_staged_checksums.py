# -*- coding: utf-8 -*-
"""Hazirlanmis workbench dosyasina gore product.json checksumlarini yeniler."""
import base64
import hashlib
import io
import json
import os

APP = r'C:\Program Files\cursor\resources\app'
product = json.load(io.open('product.json', encoding='utf-8'))
for relative in list(product.get('checksums', {})):
    if relative == 'vs/workbench/workbench.desktop.main.js':
        path = 'workbench.desktop.main.js'
    else:
        path = os.path.join(APP, 'out', *relative.split('/'))
    if os.path.exists(path):
        digest = hashlib.sha256(io.open(path, 'rb').read()).digest()
        product['checksums'][relative] = base64.b64encode(digest).decode().rstrip('=')
io.open('product.json', 'w', encoding='utf-8').write(
    json.dumps(product, indent='\t', ensure_ascii=False) + '\n'
)
print('product.json checksumlari yeniden hesaplandi')
