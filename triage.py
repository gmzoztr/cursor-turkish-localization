# -*- coding: utf-8 -*-
# YENI-EKLENENLER.txt icerigini "muhtemelen dev/jargon/teknik" (atla) ve
# "muhtemelen gercek UI metni" (cevir) olarak otomatik ayirir.
import io, re

SKIP_PAT = re.compile(
    r'^\d+\.\s|^\[Dev\]|^\[Debug\]|^Dev |^Debug:|debug fuzz|\bsimulat|\bSimulate\b|'
    r'development builds|production builds|\btelemetry\b|only available in development|'
    r'^Test View|^Dummy |^Option \d|^Item \d|^Action \d|Fake Dev|FAKE DEV|'
    r'\{0\}.*\{1\}|BracketPairColorization|ChildProcess|LazyReference|event-loop|'
    r'stack trace|Observatory|reactive graph|SolidJS|Async Tokenization|'
    r'^\w+$',  # tek kelime teknik terimler (Approved, Accepted haric asagida ayiklaniyor)
    re.I)

SHORT_UI_WORDS = {
    'Back', 'Close', 'Accepted', 'Approved', 'Changes requested', 'Add Marketplace',
    'Add to marketplace', 'Add MCP server', 'Close Window', 'Add plugin source',
    'Add plugins to marketplace', 'Cancel new folder', 'Cancel recording',
    'Change action', 'Clear selection', 'Close Observatory',
}


def load(path):
    lines = io.open(path, encoding='utf-8').read().split('\n')
    sections = {}
    cur = None
    for ln in lines:
        m = re.match(r'^=== (.+?) \(\d+\) ===$', ln)
        if m:
            cur = m.group(1)
            sections[cur] = []
        elif cur and ln.strip():
            sections[cur].append(ln)
    return sections


if __name__ == '__main__':
    sections = load('YENI-EKLENENLER.txt')
    likely_ui, likely_skip = [], []
    for sec, items in sections.items():
        for v in items:
            if v in SHORT_UI_WORDS or (len(v) <= 40 and not SKIP_PAT.search(v)
                                        and not v.endswith('.') and '{' not in v):
                likely_ui.append((sec, v))
            else:
                likely_skip.append((sec, v))
    print('muhtemel gercek UI metni:', len(likely_ui))
    print('muhtemel atlanacak (dev/jargon/teknik):', len(likely_skip))
    with io.open('triage_ui.txt', 'w', encoding='utf-8') as f:
        for sec, v in likely_ui:
            f.write('%s\t%s\n' % (sec, v))
    with io.open('triage_skip.txt', 'w', encoding='utf-8') as f:
        for sec, v in likely_skip:
            f.write('%s\t%s\n' % (sec, v))
