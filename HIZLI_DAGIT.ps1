$ErrorActionPreference = 'Stop'
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$cursorExe = 'C:\Program Files\cursor\Cursor.exe'
Set-Location -LiteralPath $base

$cursorProcesses = @(Get-Process Cursor -ErrorAction SilentlyContinue)
foreach ($process in ($cursorProcesses | Where-Object { $_.MainWindowHandle -ne 0 })) {
    [void]$process.CloseMainWindow()
}
$deadline = (Get-Date).AddSeconds(20)
do {
    Start-Sleep -Milliseconds 500
    $remaining = @(Get-Process Cursor -ErrorAction SilentlyContinue)
} while ($remaining.Count -gt 0 -and (Get-Date) -lt $deadline)
if ($remaining.Count -gt 0) {
    $remaining | Stop-Process -Force
    Start-Sleep -Seconds 1
}

# Son dinamik menü/ipucu katmanını her hızlı dağıtımda yeniden üret. Böylece
# patch_menu_gaps.py güncellenip çalışma dosyaları eski kaldığında eski yamanın
# yeniden kurulması engellenir.
& python (Join-Path $base 'patch_menu_gaps.py')
if ($LASTEXITCODE -ne 0) { throw 'Dinamik menü ve ipucu yaması üretilemedi.' }

& node --check (Join-Path $base 'workbench.desktop.main.js')
if ($LASTEXITCODE -ne 0) { throw 'Desktop workbench sözdizimi doğrulanamadı.' }
& node --check (Join-Path $base 'workbench.glass.main.js')
if ($LASTEXITCODE -ne 0) { throw 'Glass workbench sözdizimi doğrulanamadı.' }
& python (Join-Path $base 'refresh_staged_checksums.py')
if ($LASTEXITCODE -ne 0) { throw 'Checksum yenileme başarısız oldu.' }

$stage = Join-Path $base 'ceviri-son-hali'
$files = @(
    'cursor-agent-exec-main.js', 'cursor-local-agent-runtime-main.js',
    'nls.cache.messages.json', 'nls.cache.root.messages.json', 'nls.messages.json', 'product.json',
    'workbench.desktop.main.js', 'workbench.glass.main.js'
)
foreach ($name in $files) {
    if (Test-Path -LiteralPath (Join-Path $base $name)) {
        Copy-Item -LiteralPath (Join-Path $base $name) -Destination (Join-Path $stage $name) -Force
    }
}

$result = Join-Path $base 'deploy_result.txt'
Remove-Item -LiteralPath $result -Force -ErrorAction SilentlyContinue
$deploy = Join-Path $base 'deploy_all.ps1'
Start-Process -FilePath 'powershell.exe' -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File',$deploy -Verb RunAs -Wait
if (-not (Test-Path -LiteralPath $result)) { throw 'Yönetici dağıtım sonucu oluşmadı.' }
$status = (Get-Content -LiteralPath $result -Raw).Trim()
if ($status -ne 'OK_VERIFIED') { throw "Kurulum doğrulanamadı: $status" }

Remove-Item -LiteralPath "$env:APPDATA\Cursor\code.lock" -Force -ErrorAction SilentlyContinue
[void]([wmiclass]'Win32_Process').Create($cursorExe)
Write-Host 'HIZLI_DAGITIM=OK_VERIFIED'
