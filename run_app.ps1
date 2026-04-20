<#
PowerShell helper to start Streamlit inside the repo venv and open Chrome.
Run: Right-click -> Run with PowerShell, or execute from a PowerShell prompt.
#>
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

$activate = Join-Path $scriptDir ".venv\Scripts\Activate.ps1"
if (Test-Path $activate) {
    & $activate
}

Write-Host "Installing requirements (if missing)..."
pip install -r requirements.txt | Out-Null

Write-Host "Starting Streamlit..."
Start-Process -FilePath "streamlit" -ArgumentList "run","`"$scriptDir\app.py`"","--server.address","127.0.0.1","--server.port","8501"
Start-Sleep -Seconds 2
Start-Process "chrome" "http://127.0.0.1:8501"
