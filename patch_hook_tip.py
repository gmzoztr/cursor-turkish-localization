# -*- coding: utf-8 -*-
"""
patch_hook_tip.py
"Kancalar let you control and extend the agent loop - use /create-hook to get started"
parçalı ve bozuk metnini tam Türkçe olarak düzeltir.
"""
import io, os, json

# apply_all.py PATCH_SCRIPTS akışında çalışma klasöründeki kopyalar üzerinde çalışır.
BASE = os.path.dirname(os.path.abspath(__file__))
GLASS_PATH = os.path.join(BASE, "workbench.glass.main.js")
DESK_PATH = os.path.join(BASE, "workbench.desktop.main.js")

with io.open(GLASS_PATH, "r", encoding="utf-8") as f:
    glass = f.read()

with io.open(DESK_PATH, "r", encoding="utf-8") as f:
    desk = f.read()

def safe_replace(source, target, replacement, name=""):
    if target in source:
        source = source.replace(target, replacement)
        print(f"  [OK] {name}")
        return source, True
    else:
        print(f"  [ATLANDI] {name} (hedef bulunamadı)")
        return source, False

print("\n--- 1. GLASS MAIN: KANCALAR / HOOKS TIP FRAGMENT & LOOKUP ---")

# markVisibleRotatingTip içindeki lookupValue'ya Kancalar normalizasyonu ve fallback ekle
old_lookup = 'const lookupValue = value.replace(/\\bveya\\b/gi, "or");'
new_lookup = (
    'const lookupValue = value.replace(/\\bveya\\b/gi, "or")'
    '.replace(/^Kancalar\\b/gi, "Hooks")'
    '.replace(/^Yapılandır\\b/gi, "Configure");'
)
glass, _ = safe_replace(glass, old_lookup, new_lookup, "Glass lookupValue normalizasyonu")

old_tip_check = 'if (!translated && /^Kullan\\s+\\/[a-z-]+/i.test(value)) {'
new_tip_check = (
    'if (!translated && (value.includes("extend the agent loop") || value.includes("control and extend"))) {\n'
    '        translated = "Kancalar, ajan döngüsünü kontrol edip genişletmenizi sağlar — başlamak için /create-hook kullanın";\n'
    '      }\n'
    '      if (!translated && /^Kullan\\s+\\/[a-z-]+/i.test(value)) {'
)
glass, _ = safe_replace(glass, old_tip_check, new_tip_check, "Glass hook tip fallback")

# commandTipFragments içine parça eşleme ekle
old_frag = '["/create-hook", "to get started", " ile başlamak için kullanın"],'
new_frag = (
    '["/create-hook", "to get started", " — başlamak için /create-hook kullanın"],\n'
    '    ["/create-hook", "let you control and extend the agent loop", "Kancalar, ajan döngüsünü kontrol edip genişletmenizi sağlar"],\n'
    '    ["/create-hook", "Kancalar let you control and extend the agent loop", "Kancalar, ajan döngüsünü kontrol edip genişletmenizi sağlar"],'
)
glass, _ = safe_replace(glass, old_frag, new_frag, "Glass commandTipFragments hook entries")

# DOM observer sözlüğüne eklemeler
old_obs = '["File", "Dosya"],'
new_obs = (
    '["File", "Dosya"],\n'
    '    ["Kancalar let you control and extend the agent loop - use /create-hook to get started", "Kancalar, ajan döngüsünü kontrol edip genişletmenizi sağlar — başlamak için /create-hook kullanın"],\n'
    '    ["Hooks let you control and extend the agent loop - use /create-hook to get started", "Kancalar, ajan döngüsünü kontrol edip genişletmenizi sağlar — başlamak için /create-hook kullanın"],\n'
    '    ["let you control and extend the agent loop - use", "ajan döngüsünü kontrol edip genişletmenizi sağlar — başlamak için"],\n'
    '    ["to get started", "başlamak için /create-hook kullanın"],'
)
glass, _ = safe_replace(glass, old_obs, new_obs, "Glass observer dictionary hook entries")
desk, _ = safe_replace(desk, old_obs, new_obs, "Desk observer dictionary hook entries")

print("\nDosyalar diske yazılıyor...")
with io.open(GLASS_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(glass)

with io.open(DESK_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(desk)

print("JS dosyaları kaydedildi!")

print("\nHook ipucu yaması başarıyla uygulandı!")
