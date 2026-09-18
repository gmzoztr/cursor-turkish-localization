@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================================
echo   CURSOR ORİJİNAL DOSYALARINA DÖNÜŞ (Acil Durum Kurtarma)
echo ============================================================
echo.
echo Bu işlem yamaları kaldırır ve Cursor'ı orijinal haline çevirir.
echo Devam etmek için herhangi bir tuşa basın...
pause >nul

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0ORIJINALE_DON.ps1"
echo.
pause
