# =============================================================================
# Cursor Türkçe Yama — Otomatik Test Makinası (test_auto.ps1)
# =============================================================================
# Ne yapar:
#   1. Cursor setup'ını indirir (cursor.sh'dan en son sürüm)
#   2. Sessiz (silent) kurar
#   3. Yamayı uygular (patch_menu_gaps.py + deploy_all.ps1)
#   4. SHA-256 doğrular (verify_all.py)
#   5. Cursor'ı başlatır, 45 sn bekler, ayakta mı kontrol eder
#   6. Pass/Fail raporu verir
# =============================================================================
param(
    [string]$SetupUrl   = "",          # Boş bırakılırsa cursor.sh'dan en son sürümü indirir
    [string]$SetupFile  = "$env:TEMP\CursorSetup.exe",
    [switch]$SkipDownload,             # Zaten indirildiyse atla
    [switch]$SkipInstall,              # Zaten kurulduysa atla
    [switch]$KeepCursor                # Test sonunda Cursor'ı kapatma
)

$ErrorActionPreference = "Stop"
$REPO = $PSScriptRoot
$LOG  = "$REPO\test_auto_result.txt"

function Log($msg, $color="Cyan") {
    $ts = Get-Date -Format "HH:mm:ss"
    $line = "[$ts] $msg"
    Write-Host $line -ForegroundColor $color
    Add-Content $LOG $line
}

function Fail($msg) {
    Log "FAIL: $msg" "Red"
    Add-Content $LOG "=== TEST SONUCU: BASARISIZ ==="
    exit 1
}

function Pass($msg) {
    Log "PASS: $msg" "Green"
}

# Temiz log
Set-Content $LOG "=== Cursor TR Otomatik Test === $(Get-Date) ==="

# ─── ADIM 0: Yönetici kontrolü ───────────────────────────────────────────────
Log "Adım 0: Yönetici yetkisi kontrol ediliyor..."
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Log "Yönetici yetkisi gerekiyor. UAC ile yeniden başlatılıyor..." "Yellow"
    $extraArgs = ($PSBoundParameters.Keys | ForEach-Object { "-$_" }) -join " "
    Start-Process pwsh "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" $extraArgs" -Verb RunAs
    exit 0
}
Pass "Yönetici yetkisi var"

# ─── ADIM 1: İndir ───────────────────────────────────────────────────────────
if (-not $SkipDownload) {
    Log "Adım 1: Cursor indiriliyor..."

    if (-not $SetupUrl) {
        # cursor.sh/api/download?platform=win32&arch=x64&releaseTrack=stable
        try {
            $apiResp = Invoke-RestMethod "https://www.cursor.com/api/download?platform=win32&arch=x64&releaseTrack=stable" -TimeoutSec 15
            $SetupUrl = $apiResp.downloadUrl
            Log "İndir URL: $SetupUrl" "DarkCyan"
        } catch {
            # Fallback: bilinen son sürüm
            $SetupUrl = "https://downloader.cursor.sh/windows/nsis/x64/CursorSetup-x64-latest.exe"
            Log "API erişilemedi, fallback URL kullanılıyor" "Yellow"
        }
    }

    try {
        $wc = New-Object System.Net.WebClient
        $wc.DownloadFile($SetupUrl, $SetupFile)
        $size = (Get-Item $SetupFile).Length / 1MB
        Pass "İndirildi: $([Math]::Round($size,1)) MB → $SetupFile"
    } catch {
        Fail "İndirme başarısız: $_"
    }
} else {
    Log "Adım 1: İndirme atlandı (SkipDownload)" "Yellow"
    if (-not $SkipInstall -and -not (Test-Path $SetupFile)) { Fail "Setup dosyası bulunamadı: $SetupFile" }
}

# ─── ADIM 2: Kur ─────────────────────────────────────────────────────────────
if (-not $SkipInstall) {
    Log "Adım 2: Cursor kuruluyor (sessiz)..."
    # Önceki kurulumu kaldırmak için (varsa)
    $uninst = "C:\Program Files\cursor\Uninstall Cursor.exe"
    if (Test-Path $uninst) {
        Log "Mevcut Cursor kaldırılıyor..." "Yellow"
        Start-Process $uninst "/S" -Wait
        Start-Sleep 3
    }

    $proc = Start-Process $SetupFile "/VERYSILENT /SUPPRESSMSGBOXES /NORESTART" -Wait -PassThru
    if ($proc.ExitCode -ne 0) { Fail "Kurulum hata kodu: $($proc.ExitCode)" }
    Start-Sleep 5

    if (-not (Test-Path "C:\Program Files\cursor\resources\app")) {
        Fail "Cursor kurulumu tamamlandı ama app dizini bulunamadı"
    }
    Pass "Cursor kuruldu"
} else {
    Log "Adım 2: Kurulum atlandı (SkipInstall)" "Yellow"
    if (-not (Test-Path "C:\Program Files\cursor\resources\app")) {
        Fail "Cursor kurulu değil: C:\Program Files\cursor\resources\app"
    }
}

# ─── ADIM 3: Yamayı uygula ───────────────────────────────────────────────────
Log "Adım 3: Türkçe yama uygulanıyor..."

# patch_menu_gaps.py
$patchScript = "$REPO\patch_menu_gaps.py"
if (-not (Test-Path $patchScript)) { Fail "patch_menu_gaps.py bulunamadı: $patchScript" }

$patchResult = & python $patchScript 2>&1
$patchOutput = $patchResult | Out-String
Add-Content $LOG $patchOutput
if ($LASTEXITCODE -ne 0) { Fail "patch_menu_gaps.py hata verdi (kod $LASTEXITCODE)" }
if ($patchOutput -match "HATA|ERROR|Traceback") { Fail "Patch çıktısında hata var: $patchOutput" }
Pass "patch_menu_gaps.py başarılı"

# deploy_all.ps1 (dosyaları Program Files'a kopyalar)
$deployScript = "$REPO\deploy_all.ps1"
if (-not (Test-Path $deployScript)) { Fail "deploy_all.ps1 bulunamadı" }

$deployResult = & pwsh -NoProfile -ExecutionPolicy Bypass -File $deployScript 2>&1
$deployOutput = $deployResult | Out-String
Add-Content $LOG $deployOutput
if ($LASTEXITCODE -ne 0) { Fail "deploy_all.ps1 hata verdi (kod $LASTEXITCODE)" }
Pass "deploy_all.ps1 başarılı"

# ─── ADIM 4: SHA-256 doğrula ─────────────────────────────────────────────────
Log "Adım 4: SHA-256 checksumlar doğrulanıyor..."
$verifyScript = "$REPO\verify_all.py"
if (-not (Test-Path $verifyScript)) { Fail "verify_all.py bulunamadı" }

$verifyResult = & python $verifyScript 2>&1
$verifyOutput = $verifyResult | Out-String
Add-Content $LOG $verifyOutput

if ($verifyOutput -notmatch "7/7") {
    Fail "Checksum doğrulama eksik:`n$verifyOutput"
}
if ($verifyOutput -match "HATA|FAIL|ERROR") {
    Fail "Doğrulama hatası:`n$verifyOutput"
}
Pass "Tüm SHA-256 checksumlar doğrulandı (7/7)"

# ─── ADIM 5: Cursor'ı başlat ve kararlılık testi ─────────────────────────────
Log "Adım 5: Cursor başlatılıyor, 45 sn kararlılık testi..."

# code.lock temizle
$lockFile = "$env:APPDATA\Cursor\code.lock"
if (Test-Path $lockFile) { Remove-Item $lockFile -Force; Log "code.lock temizlendi" "Yellow" }

$cursorExe = "C:\Program Files\cursor\cursor.exe"
if (-not (Test-Path $cursorExe)) { Fail "cursor.exe bulunamadı: $cursorExe" }

[void]([wmiclass]'Win32_Process').Create("`"$cursorExe`"")
Log "Cursor başlatıldı, 45 sn bekleniyor..."
Start-Sleep 45

$procs = @(Get-Process -Name "cursor" -ErrorAction SilentlyContinue)
$procCount = $procs.Count
Log "Cursor process sayısı: $procCount"

if ($procCount -eq 0) {
    Fail "Cursor 45 saniye içinde çöktü veya hiç başlamadı"
}
Pass "Cursor $procCount process ile ayakta"

# ─── Kapat (isteğe bağlı) ────────────────────────────────────────────────────
if (-not $KeepCursor) {
    Log "Cursor kapatılıyor..."
    Stop-Process -Name "cursor" -Force -ErrorAction SilentlyContinue
    Start-Sleep 2
    Log "Cursor kapatıldı" "Yellow"
}

# ─── SONUÇ ───────────────────────────────────────────────────────────────────
Log ""
Log "╔══════════════════════════════════════════╗" "Green"
Log "║   TÜM TESTLER BAŞARILI — YAMA ÇALIŞIYOR ║" "Green"
Log "╚══════════════════════════════════════════╝" "Green"
Add-Content $LOG "=== TEST SONUCU: BAŞARILI ==="
Log "Rapor: $LOG" "DarkGray"
