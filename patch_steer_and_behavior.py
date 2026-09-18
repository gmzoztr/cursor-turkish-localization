# -*- coding: utf-8 -*-
"""
patch_steer_and_behavior.py
Settings -> Ajanlar (Agents) panelindeki Steer / Queue / Interrupt açılır menülerini
ve ilgili tüm "Steer" metinlerini regex ile değişken adlarından bağımsız olarak Türkçeleştirir.
"""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
GLASS_PATH = os.path.join(BASE, "workbench.glass.main.js")
DESK_PATH = os.path.join(BASE, "workbench.desktop.main.js")

with io.open(GLASS_PATH, "r", encoding="utf-8") as f:
    glass = f.read()

with io.open(DESK_PATH, "r", encoding="utf-8") as f:
    desk = f.read()

def regex_replace(source, pattern, replacement, name=""):
    new_src, count = re.subn(pattern, replacement, source)
    if count > 0:
        print(f"  [OK] {name} ({count} eslesme)")
        return new_src, True
    else:
        print(f"  [ATLANDI] {name} (hedef bulunamadi)")
        return source, False

def apply_steer_patches(content, label):
    print(f"\n--- {label}: STEER / QUEUE / INTERRUPT ---")
    
    # Steer definition: Ycs={label:"Steer",description:"Steer the agent without stopping it"}
    content, _ = regex_replace(
        content,
        r'(\b\w+)=\{label:"Steer",description:"Steer the agent without stopping it"\}',
        r'\1={label:"Yönlendir",description:"Ajanı durdurmadan yönlendirin"}',
        "Steer definition"
    )

    # Interrupt definition: lTi={label:"Interrupt",description:"Stop the agent and send the message"}
    content, _ = regex_replace(
        content,
        r'(\b\w+)=\{label:"Interrupt",description:"Stop the agent and send the message"\}',
        r'\1={label:"Durdur ve Gönder",description:"Ajanı durdurun ve mesajı gönderin"}',
        "Interrupt definition"
    )

    # Queue/steer/interrupt map: Vvl={queue:"Queue",steer:Ycs.label,"stop-and-send":lTi.label,interrupt:lTi.label}
    content, _ = regex_replace(
        content,
        r'(\b\w+)=\{queue:"Queue",steer:(\w+)\.label,"stop-and-send":(\w+)\.label,interrupt:(\w+)\.label\}',
        r'\1={queue:"Kuyruğa Ekle",steer:\2.label,"stop-and-send":\3.label,interrupt:\4.label}',
        "queue/steer/interrupt map"
    )

    # Option: {value:"queue",label:"Queue",description:"Send after Agent finishes"}
    content, _ = regex_replace(
        content,
        r'\{value:"queue",label:"Queue",description:"Send after Agent finishes"\}',
        r'{value:"queue",label:"Kuyruğa Ekle",description:"Ajan bitirdikten sonra gönderin"}',
        "queue option"
    )

    # Fallback Queue: children:Vvl[O]??"Queue" or children:Pgp[$]??"Queue"
    content, _ = regex_replace(
        content,
        r'children:(\w+)\[([^\]]+)\]\?\?"Queue"',
        r'children:\1[\2]??"Kuyruğa Ekle"',
        "fallback Queue"
    )

    # Cr=Ar?"Steer":"Send Now"
    content, _ = regex_replace(
        content,
        r'(\b\w+)=(\w+)\?"Steer":"Send Now"',
        r'\1=\2?"Yönlendir":"Hemen Gönder"',
        "Steer / Send Now"
    )

    # Steer from Phone
    content, _ = regex_replace(
        content,
        r'(\b\w+)="Steer from Phone"',
        r'\1="Telefondan Yönet"',
        "Steer from Phone"
    )

    # Steer without interrupting
    content, _ = regex_replace(
        content,
        r'"Steer without interrupting"',
        r'"Kesintiye uğratmadan yönlendir"',
        "Steer without interrupting"
    )

    # Steer from iOS
    content, _ = regex_replace(
        content,
        r'(\b\w+)=(\w+)\("<div>Steer from iOS"\)',
        r'\1=\2("<div>iOS\'tan Yönet")',
        "Steer from iOS"
    )

    # Steer the plan
    content, _ = regex_replace(
        content,
        r'return"Steer the plan, or add more details"',
        r'return"Planı yönlendirin veya daha fazla ayrıntı ekleyin"',
        "Steer the plan"
    )

    # DOM Observer fallback (if present in overlay)
    content, _ = regex_replace(
        content,
        r'(\["File", "Dosya"\],)',
        r'\1\n    ["Steer", "Yönlendir"],\n    ["Interrupt", "Durdur ve Gönder"],\n    ["Queue", "Kuyruğa Ekle"],\n    ["Steer the agent without stopping it", "Ajanı durdurmadan yönlendirin"],\n    ["Stop the agent and send the message", "Ajanı durdurun ve mesajı gönderin"],\n    ["Send after Agent finishes", "Ajan bitirdikten sonra gönderin"],\n    ["Steer from Phone", "Telefondan Yönet"],\n    ["Steer from iOS", "iOS\'tan Yönet"],\n    ["Steer without interrupting", "Kesintiye uğratmadan yönlendir"],\n    ["Steer the plan, or add more details", "Planı yönlendirin veya daha fazla ayrıntı ekleyin"],',
        "Observer Steer translations"
    )

    return content

glass = apply_steer_patches(glass, "GLASS MAIN")
desk = apply_steer_patches(desk, "DESKTOP MAIN")

print("\nDosyalar diske yazılıyor...")
with io.open(GLASS_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(glass)

with io.open(DESK_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(desk)

print("JS dosyaları kaydedildi!")
print("\nTAMAMLANDI!")
