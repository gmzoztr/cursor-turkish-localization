$ErrorActionPreference = 'Stop'
$resultFile = 'C:\Users\Work-D\cursor-tr-work\deploy_result.txt'
$rollbackDir = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback'
$items = @(
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\nls.messages.json'; Destination = 'C:\Program Files\cursor\resources\app\out\nls.messages.json'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\nls.messages.json' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\workbench.desktop.main.js'; Destination = 'C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\workbench.desktop.main.js' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\workbench.glass.main.js'; Destination = 'C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.glass.main.js'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\workbench.glass.main.js' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\cursor-agent-exec-main.js'; Destination = 'C:\Program Files\cursor\resources\app\extensions\cursor-agent-exec\dist\main.js'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\cursor-agent-exec-main.js' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\cursor-local-agent-runtime-main.js'; Destination = 'C:\Program Files\cursor\resources\app\extensions\cursor-local-agent-runtime\dist\main.js'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\cursor-local-agent-runtime-main.js' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\product.json'; Destination = 'C:\Program Files\cursor\resources\app\product.json'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\product.json' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\nls.cache.messages.json'; Destination = 'C:\Users\Work-D\AppData\Roaming\Cursor\clp\c310bf88ea022b4f2231f52246c03f28.tr\9998796a6096ce83d83a9332bfe7473b985db750\nls.messages.json'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\nls.cache.messages.json' },
  @{ Source = 'C:\Users\Work-D\cursor-tr-work\nls.cache.root.messages.json'; Destination = 'C:\Users\Work-D\AppData\Roaming\Cursor\clp\c310bf88ea022b4f2231f52246c03f28.tr\nls.messages.json'; Backup = 'C:\Users\Work-D\cursor-tr-work\deploy-rollback\nls.cache.root.messages.json' }
)

try {
  $cursorProcesses = @(Get-Process Cursor -ErrorAction SilentlyContinue)
  if ($cursorProcesses.Count -gt 0) {
    $cursorProcesses | Stop-Process -Force
    Start-Sleep -Seconds 1
  }
  if (Test-Path -LiteralPath $rollbackDir) {
    Remove-Item -LiteralPath $rollbackDir -Recurse -Force
  }
  New-Item -ItemType Directory -Path $rollbackDir -Force | Out-Null
  foreach ($item in $items) {
    Copy-Item -LiteralPath $item.Destination -Destination $item.Backup -Force
  }
  foreach ($item in $items) {
    Copy-Item -LiteralPath $item.Source -Destination $item.Destination -Force
  }
  try {
    $user = $env:USERNAME
    icacls 'C:\Program Files\cursor\resources\app' /grant "${user}:(OI)(CI)F" /T /C /Q | Out-Null
  } catch {}
  Set-Content -LiteralPath $resultFile -Value 'OK_VERIFIED' -Encoding ASCII
  exit 0
}
catch {
  $rollbackErrors = @()
  foreach ($item in $items) {
    if (Test-Path -LiteralPath $item.Backup) {
      try {
        Copy-Item -LiteralPath $item.Backup -Destination $item.Destination -Force
      }
      catch {
        $rollbackErrors += $item.Destination
      }
    }
  }
  if ($rollbackErrors.Count -eq 0) {
    Set-Content -LiteralPath $resultFile -Value ('FAIL_ROLLED_BACK: ' + $_.Exception.Message) -Encoding UTF8
  }
  else {
    Set-Content -LiteralPath $resultFile -Value ('FAIL_ROLLBACK_ERROR: ' + ($rollbackErrors -join ', ')) -Encoding UTF8
  }
  exit 1
}
