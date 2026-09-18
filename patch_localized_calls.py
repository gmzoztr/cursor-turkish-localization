# -*- coding: utf-8 -*-
"""NLS Turkcesini kaynak icindeki De(index, fallback) cagrilarina da uygular."""
import io, json, os, re

FILES = ['workbench.desktop.main.js', 'workbench.glass.main.js']
CALL_RE = re.compile(r'De\((\d+),("(?:\\.|[^"\\])*")')
PLACEHOLDER_RE = re.compile(r'\{\d+\}')

CUSTOM = {
    'Build Plan': 'Plan Oluştur',
    'Copy cursor.com link': 'cursor.com bağlantısını kopyala',
    'Find': 'Bul',
    'Find Previous': 'Öncekini Bul',
    "Install '{0}' command": "'{0}' komutunu yükle",
    'Install Cursor CLI': "Cursor CLI'ı Yükle",
    'Request Completions': 'Tamamlama İste',
    'Second Opinion': 'İkinci Görüş',
    'Shell Command': 'Kabuk Komutu',
}

INTENTIONAL_ENGLISH = {
    'Cursor', 'Cursor Origin', 'Terminal', 'Test',
    'Dev Auto Login (Enterprise)', 'Dev Auto Login (Free)',
    'Dev Auto Login (Pro Plus Trial)', 'Dev Auto Login (Pro Plus)',
    'Dev Auto Login (Pro Trial)', 'Dev Auto Login (Pro)',
    'Dev Auto Login (Ultra)', 'Force Renderer OOM Crash',
    'Hang Renderer Thread (30 s)', 'Manage Dynamic Config Overrides',
    'Reload CSS',
}


def patch_file(fname, messages):
    text = io.open(fname, encoding='utf-8').read()
    changed = 0

    def replace(match):
        nonlocal changed
        index = int(match.group(1))
        try:
            fallback = json.loads(match.group(2))
        except Exception:
            return match.group(0)
        translated = None
        # Ozel Cursor terimleri NLS dizisinde Ingilizce kalabilir. Bu nedenle
        # ozel harita NLS'den once gelir ve daha once yazilmis Turkce deger
        # sonraki calismada yeniden Ingilizceye dondurulmez.
        if fallback in CUSTOM:
            translated = CUSTOM[fallback]
        elif fallback in CUSTOM.values():
            return match.group(0)
        elif index < len(messages) and isinstance(messages[index], str) and messages[index] != fallback:
            translated = messages[index]
        if not translated or PLACEHOLDER_RE.findall(fallback) != PLACEHOLDER_RE.findall(translated):
            return match.group(0)
        changed += 1
        return 'De(%d,%s' % (index, json.dumps(translated, ensure_ascii=False))

    patched = CALL_RE.sub(replace, text)
    io.open(fname, 'w', encoding='utf-8', newline='').write(patched)
    return changed


if __name__ == '__main__':
    messages = json.load(io.open('nls.messages.json', encoding='utf-8'))
    for fname in FILES:
        if os.path.exists(fname):
            print('%s degisim: %d' % (fname, patch_file(fname, messages)))
