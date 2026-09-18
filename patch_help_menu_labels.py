# -*- coding: utf-8 -*-
"""Yeni Cursor Yardim menusu etiketlerini Turkcelestirir."""
import io

REPLACEMENTS = {
    'title:{value:"File",original:"File"': 'title:{value:"Dosya",original:"File"',
    'title:{value:"Edit",original:"Edit"': 'title:{value:"Düzen",original:"Edit"',
    'title:{value:"Selection",original:"Selection"': 'title:{value:"Seçim",original:"Selection"',
    'title:{value:"View",original:"View"': 'title:{value:"Görünüm",original:"View"',
    'title:{value:"Go",original:"Go"': 'title:{value:"Git",original:"Go"',
    'title:{value:"Terminal",original:"Terminal"': 'title:{value:"Terminal",original:"Terminal"',
    'title:{value:"Help",original:"Help"': 'title:{value:"Yardım",original:"Help"',
    'title:{value:"Preferences",original:"Preferences"': 'title:{value:"Tercihler",original:"Preferences"',
    '"Report Issue"': '"Sorun Bildir"',
    '"Give Feedback"': '"Geri Bildirim Gönder"',
    '"Give Feedback..."': '"Geri Bildirim Gönder..."',
    '"Toggle Developer Tools"': '"Geliştirici Araçlarını Aç/Kapat"',
    '"Open Process Explorer"': '"İşlem Gezginini Aç"',
}

if __name__ == '__main__':
    for filename in ['workbench.desktop.main.js', 'workbench.glass.main.js']:
        source = io.open(filename, encoding='utf-8').read()
        changes = 0
        for english, turkish in REPLACEMENTS.items():
            count = source.count(english)
            if count:
                source = source.replace(english, turkish)
                changes += count
        io.open(filename, 'w', encoding='utf-8', newline='').write(source)
        print('%s: %d Yardim menusu etiketi cevrildi' % (filename, changes))
