$ErrorActionPreference = 'Stop'
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$app = 'C:\Program Files\cursor\resources\app'

Write-Host "Cursor süreçleri kontrol ediliyor..."
$cursor = Get-Process Cursor -ErrorAction SilentlyContinue
if ($cursor) {
    Write-Host "Cursor kapatılıyor..."
    $cursor | Stop-Process -Force
    Start-Sleep -Seconds 1
}

$pkg = Join-Path $app 'package.json'
if (-not (Test-Path $pkg)) {
    Write-Host "HATA: Cursor kurulu bulunamadı: $app" -ForegroundColor Red
    exit 1
}

$ver = (Get-Content $pkg -Raw | ConvertFrom-Json).version
Write-Host "Tespit edilen sürüm: $ver"

$origDir = Join-Path $base "orijinal-$ver"
if (-not (Test-Path $origDir)) {
    # Eğer bu sürümün orijinali henüz oluşmadıysa en son orijinal yedeğe bak
    $candidates = Get-ChildItem $base -Directory -Filter "orijinal-*" | Sort-Object LastWriteTime -Descending
    if ($candidates.Count -gt 0) {
        $origDir = $candidates[0].FullName
        Write-Host "Uyarı: Bu sürümün tam klasörü bulunamadı, en yakın orijinal yedek kullanılıyor: $($candidates[0].Name)" -ForegroundColor Yellow
    } else {
        Write-Host "HATA: Orijinal yedek klasörü bulunamadı!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "Orijinal dosyalar geri yükleniyor ($origDir)..."

$targets = @{
    'nls.messages.json' = Join-Path $app 'out\nls.messages.json'
    'workbench.desktop.main.js' = Join-Path $app 'out\vs\workbench\workbench.desktop.main.js'
    'workbench.glass.main.js' = Join-Path $app 'out\vs\workbench\workbench.glass.main.js'
    'cursor-agent-exec-main.js' = Join-Path $app 'extensions\cursor-agent-exec\dist\main.js'
    'cursor-local-agent-runtime-main.js' = Join-Path $app 'extensions\cursor-local-agent-runtime\dist\main.js'
    'product.json' = Join-Path $app 'product.json'
}

foreach ($item in $targets.GetEnumerator()) {
    $src = Join-Path $origDir $item.Key
    if (Test-Path $src) {
        Copy-Item -LiteralPath $src -Destination $item.Value -Force
        Write-Host "  [OK] $($item.Key)" -ForegroundColor Green
    }
}

Write-Host "`nBAŞARILI: Cursor orijinal fabrika ayarlarına geri döndürüldü." -ForegroundColor Green
Write-Host "Cursor'ı şimdi açabilirsiniz."
