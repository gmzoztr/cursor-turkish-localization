# -*- coding: utf-8 -*-
# Uzanti dosyalari: Baglam Kullanimi (Context Usage) paneli satir etiketleri.
# Bu etiketler workbench bundle'larinda degil, cursor-agent-exec ve
# cursor-local-agent-runtime uzantilarinin icinde.
import io, os

REPS = [
    ('{id:"system_prompt",label:"System prompt"}', '{id:"system_prompt",label:"Sistem istemi"}'),
    ('{id:"tools",label:"Tool definitions"}', '{id:"tools",label:"Araç tanımları"}'),
    ('{id:"rules",label:"Rules"}', '{id:"rules",label:"Kurallar"}'),
    ('{id:"skills",label:"Skills"}', '{id:"skills",label:"Beceriler"}'),
    ('{id:"mcp",label:"MCP & dynamic tools"}', '{id:"mcp",label:"MCP ve dinamik araçlar"}'),
    ('{id:"subagents",label:"Subagent definitions"}', '{id:"subagents",label:"Alt ajan tanımları"}'),
    ('{id:"summarized_conversation",label:"Summarized conversation"}', '{id:"summarized_conversation",label:"Özetlenmiş konuşma"}'),
    ('{id:"conversation",label:"Conversation"}', '{id:"conversation",label:"Konuşma"}'),
    ('{id:"user_rules",label:"User rules"}', '{id:"user_rules",label:"Kullanıcı kuralları"}'),
    ('{id:"memories",label:"Memories"}', '{id:"memories",label:"Anılar"}'),
]

FILES = ['cursor-agent-exec-main.js', 'cursor-local-agent-runtime-main.js']

if __name__ == '__main__':
    for fname in FILES:
        if not os.path.exists(fname):
            print(fname, 'yok, atlandi')
            continue
        s = io.open(fname, encoding='utf-8').read()
        n = 0
        for a, b in REPS:
            c = s.count(a)
            if c:
                s = s.replace(a, b)
                n += c
        io.open(fname, 'w', encoding='utf-8', newline='').write(s)
        print(fname, 'degisim:', n)
