# -*- coding: utf-8 -*-
# Glass/desktop bundle'larindaki ayar sayfasi ve Ajanlar Penceresi metinleri.
import io

# Uzun/benzersiz cumleler: dogrudan tam-string degisimi (tirnak dahil)
full = {
 "Choose which source configures this MCP server.": "Bu MCP sunucusunu hangi kaynağın yapılandıracağını seçin.",
 "Enable or disable individual tools.": "Araçları tek tek etkinleştirin veya devre dışı bırakın.",
 "Add plugins to this marketplace so your team can install them.": "Ekibinizin yükleyebilmesi için bu markete eklentiler ekleyin.",
 "This marketplace will be removed from your account. The source repository won't be affected.": "Bu market hesabınızdan kaldırılacak. Kaynak depo etkilenmeyecek.",
 "Plugins bundle rules, skills, subagents, commands, MCP servers, and hooks into one installable package.": "Eklentiler; kuralları, becerileri, alt ajanları, komutları, MCP sunucularını ve kancaları tek bir yüklenebilir pakette toplar.",
 "Model Context Protocol servers connect Cursor to external tools and data sources like Linear, Figma, and Notion.": "Model Context Protocol sunucuları Cursor'ı Linear, Figma ve Notion gibi dış araçlara ve veri kaynaklarına bağlar.",
 "Skills package domain-specific knowledge and workflows that Agent applies automatically when relevant.": "Beceriler, Ajan'ın ilgili olduğunda otomatik uyguladığı alana özgü bilgi ve iş akışlarını paketler.",
 "Subagents are specialized assistants that run in their own context window so Agent can parallelize and stay focused.": "Alt ajanlar, Ajan'ın işleri paralelleştirip odaklanabilmesi için kendi bağlam pencerelerinde çalışan uzmanlaşmış yardımcılardır.",
 "Rules give Agent persistent, system-level instructions for your coding standards and workflows.": "Kurallar, kodlama standartlarınız ve iş akışlarınız için Ajan'a kalıcı, sistem düzeyinde yönergeler verir.",
 "Commands are reusable prompts you invoke with /name to standardize common workflows across your team.": "Komutlar, ekibinizde ortak iş akışlarını standartlaştırmak için /ad ile çağırdığınız yeniden kullanılabilir istemlerdir.",
 "Hooks run custom scripts at lifecycle events to observe, control, and extend the agent loop.": "Kancalar, ajan döngüsünü gözlemlemek, denetlemek ve genişletmek için yaşam döngüsü olaylarında özel betikler çalıştırır.",
 "This will remove all browsing history entries.": "Bu, tüm gezinme geçmişi girdilerini kaldıracak.",
 "This will remove all cookies. You may be signed out of websites.": "Bu, tüm tanımlama bilgilerini kaldıracak. Web sitelerindeki oturumlarınız kapanabilir.",
 "This will clear the browser cache.": "Bu, tarayıcı önbelleğini temizleyecek.",
 "This will remove all manually accepted certificates.": "Bu, el ile kabul edilmiş tüm sertifikaları kaldıracak.",
 "Create an agent to start working on tasks": "Görevler üzerinde çalışmaya başlamak için bir ajan oluşturun",
 "Disable HTTP/1.1 SSE for agent chat. This increases resource utilization and latency, but is useful if you're behind a corporate proxy that does not support HTTP/1.1 SSE streaming responses.": "Ajan sohbeti için HTTP/1.1 SSE'yi devre dışı bırakır. Bu, kaynak kullanımını ve gecikmeyi artırır ancak HTTP/1.1 SSE akış yanıtlarını desteklemeyen bir kurumsal proxy arkasındaysanız yararlıdır.",
 "Loading Cloud Agents settings...": "Bulut Ajanları ayarları yükleniyor...",
 "Cloud Agents Unavailable": "Bulut Ajanları Kullanılamıyor",
 "Cloud Agents require data storage to function.": "Bulut Ajanları çalışmak için veri depolaması gerektirir.",
 "Privacy Mode Enabled": "Gizlilik Modu Etkin",
 "Cloud Agents are not available when your privacy mode is set to disable data storage. To use Cloud Agents, please update your privacy settings to allow data storage.": "Gizlilik modunuz veri depolamayı devre dışı bırakacak şekilde ayarlandığında Bulut Ajanları kullanılamaz. Bulut Ajanlarını kullanmak için lütfen gizlilik ayarlarınızı veri depolamaya izin verecek şekilde güncelleyin.",
 "Cloud Agents require a Git repository in an open folder.": "Bulut Ajanları, açık bir klasörde Git deposu gerektirir.",
 "Hooks let you run custom scripts at specific points during the agent's execution to modify behavior, enforce policies, or add custom logging.": "Kancalar; davranışı değiştirmek, ilkeleri uygulamak veya özel günlükleme eklemek için ajanın yürütmesi sırasında belirli noktalarda özel betikler çalıştırmanıza olanak tanır.",
 "No hooks configured": "Yapılandırılmış kanca yok",
 "Add a hooks.json file to your user, project, or enterprise config to start running custom scripts.": "Özel betikler çalıştırmaya başlamak için kullanıcı, proje veya kurum yapılandırmanıza bir hooks.json dosyası ekleyin.",
 "Crawl and index custom resources and developer docs": "Özel kaynakları ve geliştirici belgelerini tara ve dizinle",
 "No Docs Added": "Belge Eklenmedi",
 "Add documentation to use as context. You can also use @Add in Chat or while editing to add a doc.": "Bağlam olarak kullanılacak belgeler ekleyin. Sohbette veya düzenleme sırasında @Add ile de belge ekleyebilirsiniz.",
 "Cloud MCP Servers": "Bulut MCP Sunucuları",
 "Servers available to cloud agents.": "Bulut ajanlarının kullanabildiği sunucular.",
 "Sign In to View Cloud MCP Servers": "Bulut MCP Sunucularını Görmek İçin Oturum Açın",
 "Sign in to load cloud user and team MCP servers from the dashboard and manage which servers are enabled for cloud agents.": "Panodan bulut kullanıcı ve ekip MCP sunucularını yüklemek ve bulut ajanları için hangi sunucuların etkin olduğunu yönetmek için oturum açın.",
 "User MCP Servers": "Kullanıcı MCP Sunucuları",
 "Your personal cloud MCP servers.": "Kişisel bulut MCP sunucularınız.",
 "No User MCP Servers": "Kullanıcı MCP Sunucusu Yok",
 "Add a personal cloud MCP server to make it available to your cloud agents.": "Bulut ajanlarınızın kullanabilmesi için kişisel bir bulut MCP sunucusu ekleyin.",
 "Team MCP Servers": "Ekip MCP Sunucuları",
 "Cloud MCP servers shared by your team.": "Ekibinizin paylaştığı bulut MCP sunucuları.",
 "No Team MCP Servers": "Ekip MCP Sunucusu Yok",
 "Team admins can configure shared MCP servers in the dashboard.": "Ekip yöneticileri panoda paylaşılan MCP sunucularını yapılandırabilir.",
 "Home MCP Servers": "Ana Sayfa MCP Sunucuları",
 "Servers available from Home.": "Ana Sayfa üzerinden kullanılabilen sunucular.",
 "No Home MCP Tools": "Ana Sayfa MCP Aracı Yok",
 "Add a custom MCP tool in your Home MCP config.": "Ana Sayfa MCP yapılandırmanıza özel bir MCP aracı ekleyin.",
 "Configured in the dashboard": "Panoda yapılandırılır",
 "Configure MCP servers in the dashboard to make them available in Cursor on desktop and in the cloud.": "Masaüstünde ve bulutta Cursor'da kullanılabilmeleri için MCP sunucularını panoda yapılandırın.",
 "Personal usage for your primary enterprise team.": "Birincil kurumsal ekibiniz için kişisel kullanım.",
 "Use Rules to guide agent behavior, like enforcing best practices or coding standards. Rules can be applied always, by file path, or manually.": "En iyi uygulamaları veya kodlama standartlarını uygulamak gibi ajan davranışını yönlendirmek için Kuralları kullanın. Kurallar her zaman, dosya yoluna göre veya el ile uygulanabilir.",
 "No Rules Yet": "Henüz Kural Yok",
 "Create rules to guide Agent behavior": "Ajan davranışını yönlendirmek için kurallar oluşturun",
 "Skills are specialized capabilities that help the agent accomplish specific tasks. Skills will be invoked by the agent when relevant or can be triggered manually with / in chat.": "Beceriler, ajanın belirli görevleri başarmasına yardımcı olan uzmanlaşmış yeteneklerdir. Beceriler ilgili olduğunda ajan tarafından çağrılır veya sohbette / ile el ile tetiklenebilir.",
 "No Skills Yet": "Henüz Beceri Yok",
 "Skills help the agent accomplish specific tasks": "Beceriler, ajanın belirli görevleri başarmasına yardımcı olur",
 "No Subagents Yet": "Henüz Alt Ajan Yok",
 "Create specialized agents to handle focused tasks": "Odaklı görevleri üstlenecek uzmanlaşmış ajanlar oluşturun",
 "No Commands Yet": "Henüz Komut Yok",
 "Create commands to build reusable workflows": "Yeniden kullanılabilir iş akışları için komutlar oluşturun",
 "Feature request": "Özellik isteği",
 "Something is off": "Bir şeyler ters",
 "Can't use Cursor": "Cursor kullanılamıyor",
 "The main agent received the accept request, but marking this suggestion as completed failed. Refresh the FSD tray or try again.": "Ana ajan kabul isteğini aldı ancak bu öneri tamamlandı olarak işaretlenemedi. FSD tepsisini yenileyin veya tekrar deneyin.",
 "The main agent received the undo request, but reopening this suggestion failed. Refresh the FSD tray or try again.": "Ana ajan geri alma isteğini aldı ancak bu öneri yeniden açılamadı. FSD tepsisini yenileyin veya tekrar deneyin.",
 "Cannot Apply This Suggestion": "Bu Öneri Uygulanamıyor",
 "This finding is not ready to apply yet. Check that the suggestion is still open and has the required metadata.": "Bu bulgu henüz uygulanmaya hazır değil. Önerinin hâlâ açık olduğundan ve gerekli meta verilere sahip olduğundan emin olun.",
 "No Active Agent Conversation": "Etkin Ajan Konuşması Yok",
 "Create or select an agent first, then retry this action.": "Önce bir ajan oluşturun veya seçin, ardından bu eylemi tekrar deneyin.",
 "Cannot Reject This Suggestion": "Bu Öneri Reddedilemiyor",
 "This finding is missing its pull request URL. Try reopening the FSD tray from the PR or re-running /fsd.": "Bu bulgunun pull request URL'si eksik. FSD tepsisini PR'dan yeniden açmayı veya /fsd komutunu yeniden çalıştırmayı deneyin.",
 "This finding is missing run metadata. Wait for the FSD run to finish recording outputs, then try again.": "Bu bulgunun çalıştırma meta verileri eksik. FSD çalıştırmasının çıktıları kaydetmeyi bitirmesini bekleyin, sonra tekrar deneyin.",
 "Save changes not supported yet": "Değişiklikleri kaydetme henüz desteklenmiyor",
 "Saving changes to existing multi-root workspaces is not supported yet.": "Mevcut çok köklü çalışma alanlarına değişiklik kaydetme henüz desteklenmiyor.",
 "No Agent For This Task": "Bu Görev İçin Ajan Yok",
 "This task does not have an active agent run yet. Start self-driving on the pull request or wait for triage to finish.": "Bu görevin henüz etkin bir ajan çalıştırması yok. Pull request üzerinde otomatik sürüşü başlatın veya önceliklendirmenin bitmesini bekleyin.",
 "Cannot Move To Local": "Yerele Taşınamıyor",
 "This task is missing its pull request URL.": "Bu görevin pull request URL'si eksik.",
 "This pull request tab does not have a branch name yet.": "Bu pull request sekmesinin henüz bir dal adı yok.",
 "Could Not Move To Local": "Yerele Taşınamadı",
 "Local self-driving could not be started for this task. Try again from the agent panel.": "Bu görev için yerel otomatik sürüş başlatılamadı. Ajan panelinden tekrar deneyin.",
 "You'll be logged out of your Cursor account on this device.": "Bu cihazda Cursor hesabınızın oturumu kapatılacak.",
 "This will quit Cursor and close all windows. Are you sure you want to quit?": "Bu, Cursor'dan çıkacak ve tüm pencereleri kapatacak. Çıkmak istediğinizden emin misiniz?",
 "With Privacy Mode enabled, none of your questions or code will ever be stored or learned from by us or any third-party.": "Gizlilik Modu etkinken sorularınız veya kodunuz asla bizim ya da üçüncü tarafların tarafından depolanmaz veya öğrenim için kullanılmaz.",
 "If you enable Privacy Mode, none of your questions or code will ever be stored by us or any third-party.": "Gizlilik Modunu etkinleştirirseniz sorularınız veya kodunuz asla bizim ya da üçüncü taraflarca depolanmaz.",
 "Create your public profile": "Herkese açık profilinizi oluşturun",
 "Claim a handle to get a profile page showing your token, model, and agent usage.": "Jeton, model ve ajan kullanımınızı gösteren bir profil sayfası için bir kullanıcı adı alın.",
 "Claim handle": "Kullanıcı adı al",
 "Choose between light, dark, or high contrast themes": "Açık, koyu veya yüksek karşıtlıklı temalar arasında seçim yapın",
 "Adjust how much detail is shown for tool calls": "Araç çağrıları için ne kadar ayrıntı gösterileceğini ayarlayın",
 "Use themed background colors for inline code diffs": "Satır içi kod farkları için temalı arka plan renkleri kullan",
 "Choose a tint color": "Bir renk tonu seçin",
 "Control how strongly the tint is applied": "Renk tonunun ne kadar güçlü uygulanacağını denetleyin",
 "Reduce Transparency": "Saydamlığı Azalt",
 "Replace translucent surfaces with opaque backgrounds": "Yarı saydam yüzeyleri mat arka planlarla değiştir",
 "UI Font Size": "Arayüz Yazı Tipi Boyutu",
 "Font size for the Cursor user interface": "Cursor kullanıcı arayüzü için yazı tipi boyutu",
 "Code Font Size": "Kod Yazı Tipi Boyutu",
 "Font size for code editors and diffs": "Kod düzenleyicileri ve farklar için yazı tipi boyutu",
 "Cursor periodically removes old worktrees to free disk space. Tune how aggressively cleanup runs.": "Cursor, disk alanı boşaltmak için eski çalışma ağaçlarını düzenli olarak kaldırır. Temizliğin ne kadar agresif çalışacağını ayarlayın.",
 "Max Worktrees": "En Fazla Çalışma Ağacı",
 "Maximum number of Cursor-managed worktrees to retain across all workspaces. Older worktrees are removed first.": "Tüm çalışma alanlarında tutulacak Cursor yönetimindeki en fazla çalışma ağacı sayısı. Önce eski çalışma ağaçları kaldırılır.",
 "Max Total Size (GB)": "En Fazla Toplam Boyut (GB)",
 "Maximum total size in GB across all Cursor-managed worktrees. Set to 0 to disable the size limit.": "Cursor yönetimindeki tüm çalışma ağaçlarının GB cinsinden en fazla toplam boyutu. Boyut sınırını devre dışı bırakmak için 0 yapın.",
 "Cursor-Managed Worktrees": "Cursor Yönetimindeki Çalışma Ağaçları",
 "No Cursor-managed worktrees on this machine.": "Bu makinede Cursor yönetiminde çalışma ağacı yok.",
 "Search MCP servers...": "MCP sunucularında ara...",
 "Open MCP Settings": "MCP Ayarlarını Aç",
 "No MCP servers": "MCP sunucusu yok",
 "Modes, skills, MCPs and more": "Modlar, beceriler, MCP'ler ve daha fazlası",
 "Extend Cursor with Plugins": "Cursor'ı Eklentilerle Genişletin",
 "Connect External Tools with MCP": "MCP ile Dış Araçları Bağlayın",
 "Teach Cursor New Skills": "Cursor'a Yeni Beceriler Öğretin",
 "Delegate Work to Subagents": "İşleri Alt Ajanlara Devredin",
 "Guide Agent with Rules": "Ajanı Kurallarla Yönlendirin",
 "Create Reusable Commands": "Yeniden Kullanılabilir Komutlar Oluşturun",
 "Automate with Hooks": "Kancalarla Otomatikleştirin",
 "No plugins yet": "Henüz eklenti yok",
 "Remove marketplace?": "Market kaldırılsın mı?",
 "No agents yet": "Henüz ajan yok",
 "Agent Stores": "Ajan Mağazaları",
 "Search models": "Modellerde ara",
 "Plugin Settings": "Eklenti Ayarları",
 "Search the marketplace": "Markette ara",
 "Log out?": "Oturum kapatılsın mı?",
 "Quit Cursor?": "Cursor'dan çıkılsın mı?",
}

# Kisa/riskli metinler: yalnizca belirli anahtar baglaminda degistir
ctx = {}
for key in ["label", "title", "aria-label", "placeholder", "sectionTitle", "heading", "emptyMessage", "tooltip"]:
    for a, b in [
        ("Split Down", "Aşağıya Böl"),
        ("Split Right", "Sağa Böl"),
        ("Theme", "Tema"),
        ("Agent Conversations", "Ajan Konuşmaları"),
        ("Tool Call Density", "Araç Çağrısı Yoğunluğu"),
        ("Colors", "Renkler"),
        ("Typography", "Tipografi"),
        ("Hue", "Renk Tonu"),
        ("Intensity", "Yoğunluk"),
        ("Cleanup", "Temizlik"),
        ("New Worktree", "Yeni Çalışma Ağacı"),
        ("Loading", "Yükleniyor"),
        ("Hooks", "Kancalar"),
        ("Docs", "Belgeler"),
        ("Rules", "Kurallar"),
        ("Skills", "Beceriler"),
        ("Idea", "Fikir"),
        ("Bug", "Hata"),
        ("Urgent", "Acil"),
        ("Get Started", "Başlayın"),
        ("Privacy Mode", "Gizlilik Modu"),
        ("Plan & Usage", "Plan ve Kullanım"),
        ("All Plugins", "Tüm Eklentiler"),
        ("Up to date", "Güncel"),
        ("MCP Servers", "MCP Sunucuları"),
        ("Source", "Kaynak"),
        ("Tools", "Araçlar"),
    ]:
        q = '"' if key != "aria-label" else '"'
        ctx['%s:"%s"' % (json_key(key) if False else (('"%s"' % key) if key == "aria-label" else key), a)] = None  # placeholder, asagida kurulacak

# ctx sozlugunu duz kur (yukaridaki karmasayi birak)
ctx = {}
short_pairs = [
    ("Split Down", "Aşağıya Böl"), ("Split Right", "Sağa Böl"), ("Theme", "Tema"),
    ("Agent Conversations", "Ajan Konuşmaları"), ("Tool Call Density", "Araç Çağrısı Yoğunluğu"),
    ("Colors", "Renkler"), ("Typography", "Tipografi"), ("Hue", "Renk Tonu"),
    ("Intensity", "Yoğunluk"), ("Cleanup", "Temizlik"), ("New Worktree", "Yeni Çalışma Ağacı"),
    ("Loading", "Yükleniyor"), ("Hooks", "Kancalar"), ("Docs", "Belgeler"), ("Rules", "Kurallar"),
    ("Skills", "Beceriler"), ("Idea", "Fikir"), ("Bug", "Hata"), ("Urgent", "Acil"),
    ("Get Started", "Başlayın"), ("Privacy Mode", "Gizlilik Modu"), ("Plan & Usage", "Plan ve Kullanım"),
    ("All Plugins", "Tüm Eklentiler"), ("Up to date", "Güncel"), ("MCP Servers", "MCP Sunucuları"),
    ("Source", "Kaynak"), ("Tools", "Araçlar"),
]
for key in ['label:', 'title:', '"aria-label":', 'placeholder:', 'sectionTitle:', 'heading:', 'emptyMessage:', 'tooltip:']:
    for a, b in short_pairs:
        ctx[key + '"' + a + '"'] = key + '"' + b + '"'

for fname in ["workbench.glass.main.js", "workbench.desktop.main.js"]:
    s = io.open(fname, encoding="utf-8").read()
    total = 0
    for a in sorted(full, key=len, reverse=True):
        old = '"' + a + '"'
        new = '"' + full[a] + '"'
        c = s.count(old)
        if c:
            s = s.replace(old, new)
            total += c
    for old, new in ctx.items():
        c = s.count(old)
        if c:
            s = s.replace(old, new)
            total += c
    io.open(fname, "w", encoding="utf-8", newline="").write(s)
    print(fname, "degisim:", total)
