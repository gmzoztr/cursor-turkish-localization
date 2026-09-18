@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================================
echo   CURSOR TURKCE YAMASI - Tek Tikla Uygula
echo ============================================================
echo.
echo   Once Cursor'in TAMAMEN kapali oldugundan emin olun
echo   (Ajanlar Penceresi dahil).
echo.
pause

where python >nul 2>nul
if errorlevel 1 (
    echo HATA: python bulunamadi. Python yuklu ve PATH'te olmali.
    pause
    exit /b 1
)

python -X utf8 apply_all.py
set RC=%ERRORLEVEL%

echo.
echo ============================================================
if %RC%==0 (
    echo   TAMAMLANDI. Cursor'i acabilirsiniz.
) else (
    echo   HATA OLUSTU. Yukaridaki mesajlara ve apply_report.txt'ye bakin.
)
echo   Rapor            : apply_report.txt
echo   Yeni/eksik metin  : YENI-EKLENENLER.txt
echo ============================================================
echo.
pause
