# ============================================
# Script Completo: Instala Node.js e Inicia Servidor
# ============================================

$ErrorActionPreference = "Stop"

$BIN_DIR = $PSScriptRoot
$INSTALL_SCRIPT = Join-Path $BIN_DIR "install-node.ps1"
$START_SCRIPT = Join-Path $BIN_DIR "start-server.ps1"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Setup Completo - Decap CMS" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Executar instalação do Node.js
if (Test-Path $INSTALL_SCRIPT) {
    & $INSTALL_SCRIPT
}
else {
    Write-Host "Erro: Script de instalação não encontrado!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Pressione Enter para iniciar o servidor..." -ForegroundColor Yellow
Read-Host

# Executar servidor
if (Test-Path $START_SCRIPT) {
    & $START_SCRIPT
}
else {
    Write-Host "Erro: Script do servidor não encontrado!" -ForegroundColor Red
    exit 1
}
