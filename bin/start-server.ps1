# ============================================
# Script para iniciar o servidor Decap CMS
# ============================================

$ErrorActionPreference = "Stop"

# Configurações
$BIN_DIR = $PSScriptRoot
$NODE_DIR = Join-Path $BIN_DIR "node"
$NODE_EXE = Join-Path $NODE_DIR "node.exe"
$NPM_CMD = Join-Path $NODE_DIR "npm.cmd"
$PROJECT_ROOT = Split-Path $BIN_DIR -Parent

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Iniciando Decap CMS Server" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se o Node.js está instalado
if (-not (Test-Path $NODE_EXE)) {
    Write-Host "Node.js não encontrado em: $NODE_DIR" -ForegroundColor Red
    Write-Host ""
    Write-Host "Execute primeiro:" -ForegroundColor Yellow
    Write-Host "  .\bin\install-node.ps1" -ForegroundColor White
    Write-Host ""
    
    $response = Read-Host "Deseja instalar o Node.js agora? (S/n)"
    if ($response -ne "n" -and $response -ne "N") {
        Write-Host ""
        & (Join-Path $BIN_DIR "install-node.ps1")
        Write-Host ""
    }
    else {
        exit 1
    }
}

# Exibir versões
$nodeVersion = & $NODE_EXE --version
$npmVersion = & $NPM_CMD --version

Write-Host "Node.js: $nodeVersion" -ForegroundColor Green
Write-Host "npm: $npmVersion" -ForegroundColor Green
Write-Host ""

# Verificar se o decap-server está instalado globalmente na pasta local
$NPX_CMD = Join-Path $NODE_DIR "npx.cmd"
$DECAP_SERVER_CHECK = Join-Path $NODE_DIR "node_modules\decap-server"

if (-not (Test-Path $DECAP_SERVER_CHECK)) {
    Write-Host "Decap Server não encontrado. Instalando..." -ForegroundColor Yellow
    Write-Host ""
    
    try {
        # Instalar decap-server globalmente no Node.js local
        & $NPM_CMD install -g decap-server --prefix $NODE_DIR
        Write-Host ""
        Write-Host "Decap Server instalado com sucesso!" -ForegroundColor Green
        Write-Host ""
    }
    catch {
        Write-Host "Erro ao instalar Decap Server: $_" -ForegroundColor Red
        exit 1
    }
}

# Iniciar o servidor
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Iniciando servidor local..." -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Servidor rodando em: http://localhost:8081" -ForegroundColor Green
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Yellow
Write-Host ""

try {
    # Mudar para o diretório raiz do projeto
    Set-Location $PROJECT_ROOT
    
    # Iniciar o servidor Decap CMS usando npx
    & $NPX_CMD decap-server
}
catch {
    Write-Host ""
    Write-Host "Servidor encerrado." -ForegroundColor Yellow
}
