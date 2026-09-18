# -*- coding: utf-8 -*-
"""Cursor 3.13+ AI kod izleme durum cubugu metinlerini Turkcelestirir."""
import io

REPLACEMENTS = [
    ('"AI Code Tracking Stats - Tab"', '"AI Kod İzleme İstatistikleri - Sekme"'),
    ('`$(tab) Tab Stats: ${this.todayStats.tabAcceptedLines}/${this.todayStats.tabSuggestedLines} (${t}%)`',
     '`$(tab) Sekme İstatistikleri: ${this.todayStats.tabAcceptedLines}/${this.todayStats.tabSuggestedLines} (${t}%)`'),
    ('`Tab AI Stats: ${this.todayStats.tabAcceptedLines} accepted out of ${this.todayStats.tabSuggestedLines} suggested, ${t} percent acceptance rate`',
     '`Sekme AI İstatistikleri: Önerilen ${this.todayStats.tabSuggestedLines} satırdan ${this.todayStats.tabAcceptedLines} satır kabul edildi; kabul oranı yüzde ${t}`'),
    ('`Tab AI Stats (Today): ${this.todayStats.tabAcceptedLines}/${this.todayStats.tabSuggestedLines} lines (${t}%)`',
     '`Sekme AI İstatistikleri (Bugün): ${this.todayStats.tabAcceptedLines}/${this.todayStats.tabSuggestedLines} satır (${t}%)`'),
    ('"AI Code Tracking Stats - Agent"', '"AI Kod İzleme İstatistikleri - Ajan"'),
    ('`$(comment-discussion) Agent Stats: ${this.todayStats.composerAcceptedLines}/${this.todayStats.composerSuggestedLines} (${t}%)`',
     '`$(comment-discussion) Ajan İstatistikleri: ${this.todayStats.composerAcceptedLines}/${this.todayStats.composerSuggestedLines} (${t}%)`'),
    ('`Agent AI Stats: ${this.todayStats.composerAcceptedLines} accepted out of ${this.todayStats.composerSuggestedLines} suggested, ${t} percent acceptance rate`',
     '`Ajan AI İstatistikleri: Önerilen ${this.todayStats.composerSuggestedLines} satırdan ${this.todayStats.composerAcceptedLines} satır kabul edildi; kabul oranı yüzde ${t}`'),
    ('`Agent AI Stats (Today): ${this.todayStats.composerAcceptedLines}/${this.todayStats.composerSuggestedLines} lines (${t}%)`',
     '`Ajan AI İstatistikleri (Bugün): ${this.todayStats.composerAcceptedLines}/${this.todayStats.composerSuggestedLines} satır (${t}%)`'),
    ('"AI Code Tracking - Recent Commit"', '"AI Kod İzleme - Son Commit"'),
    ('"$(git-commit) No commit scored"', '"$(git-commit) Puanlanmış değişiklik kaydı yok"'),
    ('"$(git-commit) Puanlanmış commit yok"', '"$(git-commit) Puanlanmış değişiklik kaydı yok"'),
    ('"No commit has been scored yet"', '"Henüz puanlanmış değişiklik kaydı yok"'),
    ('"Henüz puanlanmış commit yok"', '"Henüz puanlanmış değişiklik kaydı yok"'),
    ('`Repo: ${this.recentCommit.repoName}', '`Depo: ${this.recentCommit.repoName}'),
    ('`Branch: ${this.recentCommit.branchName}', '`Dal: ${this.recentCommit.branchName}'),
    ('`Most Recent Commit Scored:', '`Puanlanan En Son Commit:'),
    ('AI-Generated: ${this.recentCommit.aiPercentage}% (${n} lines)',
     'AI Tarafından Üretilen: ${this.recentCommit.aiPercentage}% (${n} satır)'),
    ('  - Tab: ${i} lines (${this.recentCommit.tabLinesAdded} added, ${this.recentCommit.tabLinesDeleted} deleted)',
     '  - Sekme: ${i} satır (${this.recentCommit.tabLinesAdded} eklendi, ${this.recentCommit.tabLinesDeleted} silindi)'),
    ('  - Composer: ${r} lines (${this.recentCommit.composerLinesAdded} added, ${this.recentCommit.composerLinesDeleted} deleted)',
     '  - Ajan: ${r} satır (${this.recentCommit.composerLinesAdded} eklendi, ${this.recentCommit.composerLinesDeleted} silindi)'),
    ('Total Changes: ${this.recentCommit.linesAdded} added, ${this.recentCommit.linesDeleted} deleted`',
     'Toplam Değişiklik: ${this.recentCommit.linesAdded} eklendi, ${this.recentCommit.linesDeleted} silindi`'),
    ('`Most recent commit scored: ${t}, ${this.recentCommit.aiPercentage} percent AI-generated`',
     '`Puanlanan en son commit: ${t}; yüzde ${this.recentCommit.aiPercentage} AI tarafından üretildi`'),
]


if __name__ == '__main__':
    for filename in ['workbench.desktop.main.js', 'workbench.glass.main.js']:
        source = io.open(filename, encoding='utf-8').read()
        changes = 0
        for english, turkish in REPLACEMENTS:
            count = source.count(english)
            if count:
                source = source.replace(english, turkish)
                changes += count
        io.open(filename, 'w', encoding='utf-8', newline='').write(source)
        print('%s: %d durum cubugu metni cevrildi' % (filename, changes))
