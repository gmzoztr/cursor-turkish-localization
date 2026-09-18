# -*- coding: utf-8 -*-
"""Cursor ayarlarinda dogrudan koda yazilmis gorunur Ingilizce metinleri cevirir."""
import io
import re


REPLACEMENTS = {
    'title:"Choose Custom Sound..."': 'title:"Özel Ses Seç..."',
    'title:"Preview",type:"tertiary"': 'title:"Önizle",type:"tertiary"',
    ':"Default Sound"': ':"Varsayılan Ses"',
    'title="Reset to default sound"': 'title="Varsayılan sese sıfırla"',
    'name:"Audio Files"': 'name:"Ses Dosyaları"',
    'name:"All Files"': 'name:"Tüm Dosyalar"',
    'label:"Email"': 'label:"E-posta"',
    'label:"Profile Image"': 'label:"Profil Resmi"',
    'label:"Handle"': 'label:"Kullanıcı Adı"',
    'accessibleLabel:"Profile Details"': 'accessibleLabel:"Profil Ayrıntıları"',
    'children:u?"Herkese açık profilinizi oluşturun":"Create your profile"': 'children:u?"Herkese açık profilinizi oluşturun":"Profilinizi oluşturun"',
    'label:`Link ${': 'label:`Bağlantı ${',
    '"aria-label":`Link ${': '"aria-label":`Bağlantı ${',
    'title:"Third-Party Imports"': 'title:"Üçüncü Taraf İçe Aktarımları"',
    'label:"Import Claude Code Conversations"': 'label:"Claude Code Konuşmalarını İçe Aktar"',
    'title:"OpenAI API Key"': 'title:"OpenAI API Anahtarı"',
    'title:"Anthropic API Key"': 'title:"Anthropic API Anahtarı"',
    'title:"Google API Key"': 'title:"Google API Anahtarı"',
    'Eky=Oe("<span>your OpenAI key")': 'Eky=Oe("<span>OpenAI API anahtarınızı")',
    '<span>your Anthropic key': '<span>Anthropic API anahtarınızı',
    '<span>your Google AI Studio key': '<span>Google AI Studio anahtarınızı',
    '"You can put in"': '"Kullanmak için"',
    '"to use OpenAI models at cost."': '"girin; OpenAI modelleri maliyetine kullanılır."',
    "'to use Claude at cost. When enabled, this key will be used for all models beginning with \"claude-\".'": "'girin; Claude maliyetine kullanılır. Etkinleştirildiğinde bu anahtar, adı \"claude-\" ile başlayan tüm modellerde kullanılır.'",
    '"to use Google models at-cost."': '"girin; Google modelleri maliyetine kullanılır."',
    '<div>Secret saved': '<div>Gizli anahtar kaydedildi',
    '"Secret saved. Enter a new key to replace it"': '"Gizli anahtar kaydedildi. Değiştirmek için yeni bir anahtar girin"',
    '"Enter your OpenAI API Key"': '"OpenAI API anahtarınızı girin"',
    '"Enter your Anthropic API Key"': '"Anthropic API anahtarınızı girin"',
    '"Enter your Google AI Studio API Key"': '"Google AI Studio API anahtarınızı girin"',
    'description(){return"Configure Azure OpenAI to use OpenAI models through your Azure account."}': 'description(){return"Azure hesabınız üzerinden OpenAI modellerini kullanmak için Azure OpenAI\'ı yapılandırın."}',
    'label:"Base URL"': 'label:"Temel URL"',
    'label:"API Key"': 'label:"API Anahtarı"',
    'placeholder:"e.g. my-resource.openai.azure.com"': 'placeholder:"örn. my-resource.openai.azure.com"',
    'placeholder:"e.g. gpt-35-turbo"': 'placeholder:"örn. gpt-35-turbo"',
    '"Configure AWS Bedrock to use Anthropic Claude models through your AWS account."': '"Anthropic Claude modellerini AWS hesabınız üzerinden kullanmak için AWS Bedrock\'u yapılandırın."',
    '"Cursor Enterprise teams can configure IAM roles to access Bedrock without any Access Keys."': '"Cursor Enterprise ekipleri, erişim anahtarı olmadan Bedrock\'a erişmek için IAM rollerini yapılandırabilir."',
    'label:"Access Key ID"': 'label:"Erişim Anahtarı Kimliği"',
    'label:"Secret Access Key"': 'label:"Gizli Erişim Anahtarı"',
    'label:"Region"': 'label:"Bölge"',
    'label:"Test Model"': 'label:"Test Modeli"',
    'placeholder:"AWS Access Key ID"': 'placeholder:"AWS Erişim Anahtarı Kimliği"',
    'placeholder:"AWS Secret Access Key"': 'placeholder:"AWS Gizli Erişim Anahtarı"',
    'placeholder:"e.g. us-east-1"': 'placeholder:"örn. us-east-1"',
    '"Data Sharing Enabled"': '"Veri Paylaşımı Etkin"',
    '"Privacy Mode"': '"Gizlilik Modu"',
    '"Privacy Mode (Legacy)"': '"Gizlilik Modu (Eski)"',
    '"Your codebase, prompts, edits and other usage data will be stored and trained on by Cursor to improve the product."': '"Kod tabanınız, istemleriniz, düzenlemeleriniz ve diğer kullanım verileriniz Cursor tarafından ürünü geliştirmek amacıyla saklanacak ve eğitilecektir."',
    '"Your prompts, edits and other usage data will be stored and trained on by Cursor to improve the product."': '"İstemleriniz, düzenlemeleriniz ve diğer kullanım verileriniz Cursor tarafından ürünü geliştirmek amacıyla saklanacak ve eğitilecektir."',
    '" Prompts and limited telemetry may also be shared with model providers when you explicitly select their models."': '" Açıkça modellerini seçtiğinizde istemler ve sınırlı telemetri verileri model sağlayıcılarıyla da paylaşılabilir."',
    '". Prompts and limited telemetry may also be shared with model providers when you explicitly select their models"': '". Açıkça modellerini seçtiğinizde istemler ve sınırlı telemetri verileri model sağlayıcılarıyla da paylaşılabilir"',
    '"Improve Cursor for everyone"': '"Cursor\'ı herkes için iyileştirin"',
    '"No training. Code may be stored for Background Agent and other features."': '"Eğitim yapılmaz. Kod, Arka Plan Ajanı ve diğer özellikler için saklanabilir."',
    '"No training and no storage. Background Agent and other features that require code storage will be disabled."': '"Eğitim ve depolama yapılmaz. Arka Plan Ajanı ve kod depolaması gerektiren diğer özellikler devre dışı bırakılır."',
}


def patch_runtime_text_sources(source):
    """Sunucudan gelen metinleri ekrana basan React/DOM noktalarini yamalar."""
    changes = 0

    warning_pattern = re.compile(
        r'children:\["With your Cursor"," ",(?P<plan>[A-Za-z_$][\w$]*),'
        r'"subscription, you do not need to use your own ",(?P<api>[A-Za-z_$][\w$]*)," key!"\]'
    )
    source, count = warning_pattern.subn(
        lambda match: (
            'children:["Cursor"," ",' + match.group('plan') +
            ',"aboneliğinizle kendi ",' + match.group('api') +
            '," anahtarınızı kullanmanız gerekmez!"]'
        ),
        source,
    )
    changes += count

    turn_off_pattern = re.compile(
        r'children:\["Turn Off ",(?P<api>[A-Za-z_$][\w$]*)," Key"\]'
    )
    source, count = turn_off_pattern.subn(
        lambda match: 'children:[' + match.group('api') + '," Anahtarını Kapat"]',
        source,
    )
    changes += count

    # Model bilgileri AvailableModelsResponse.tooltipData alanindan gelir.
    # Tooltip olusturucusunu genel DOM gozlemcisinden once ceviri katmanina bagla.
    markdown_pattern = re.compile(
        r'(?P<local>[A-Za-z_$][\w$]*)=(?P<obj>[A-Za-z_$][\w$]*)\.markdownContent;'
    )
    source, count = markdown_pattern.subn(
        lambda match: (
            match.group('local') + '=globalThis.__cursorTrTranslateModelTooltip?.('
            + match.group('obj') + '.markdownContent)||' + match.group('obj') + '.markdownContent;'
        ),
        source,
    )
    changes += count

    for field in ('primaryText', 'secondaryText', 'tertiaryText'):
        field_pattern = re.compile(
            r'(?P<target>[A-Za-z_$][\w$]*\.textContent=)'
            r'(?P<obj>[A-Za-z_$][\w$]*)\.' + field + r'(?P<tail>\?\?null|\?\?"")?'
        )
        source, count = field_pattern.subn(
            lambda match, field=field: (
                match.group('target') + '(globalThis.__cursorTrTranslateValue?.('
                + match.group('obj') + '.' + field + ')||' + match.group('obj') + '.' + field + ')'
                + (match.group('tail') or '')
            ),
            source,
        )
        changes += count

    return source, changes


if __name__ == '__main__':
    for fname in ['workbench.desktop.main.js', 'workbench.glass.main.js']:
        source = io.open(fname, encoding='utf-8').read()
        changes = 0
        for old, new in REPLACEMENTS.items():
            count = source.count(old)
            if count:
                source = source.replace(old, new)
                changes += count
        source, runtime_changes = patch_runtime_text_sources(source)
        changes += runtime_changes
        io.open(fname, 'w', encoding='utf-8', newline='').write(source)
        print('%s: %d ayarlar arayuzu metni cevrildi' % (fname, changes))
