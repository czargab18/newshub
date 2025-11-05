# ============================================
# Atalho para Iniciar Servidor (Raiz do Projeto)
# ============================================
# Execute este script se o Node.js já estiver instalado

$ErrorActionPreference = "Stop"
$PROJECT_ROOT = $PSScriptRoot
$START_SCRIPT = Join-Path $PROJECT_ROOT "bin\start-server.ps1"

if (Test-Path $START_SCRIPT) {
    & $START_SCRIPT
}
else {
    Write-Host "Erro: Script não encontrado em bin\start-server.ps1" -ForegroundColor Red
    exit 1
}
