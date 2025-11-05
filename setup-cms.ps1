# ============================================
# Atalho para Setup Completo
# ============================================
# Este script pode ser executado da raiz do projeto

$ErrorActionPreference = "Stop"
$PROJECT_ROOT = $PSScriptRoot
$SETUP_SCRIPT = Join-Path $PROJECT_ROOT "bin\setup.ps1"

if (Test-Path $SETUP_SCRIPT) {
    & $SETUP_SCRIPT
}
else {
    Write-Host "Erro: Script de setup não encontrado em bin\setup.ps1" -ForegroundColor Red
    exit 1
}
