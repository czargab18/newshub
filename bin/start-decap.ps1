# ============================================
# Script para iniciar Decap CMS com servidores
# ============================================
# Este script inicia:
# - HTTP Server (porta 8080) para servir o admin
# - Decap Server (porta 8081) para backend local

$ErrorActionPreference = "Stop"

# Configuracoes
$BIN_DIR = $PSScriptRoot
$NODE_DIR = Join-Path $BIN_DIR "node"
$NODE_EXE = Join-Path $NODE_DIR "node.exe"
$NPM_CMD = Join-Path $NODE_DIR "npm.cmd"
$NPX_CMD = Join-Path $NODE_DIR "npx.cmd"
$PROJECT_ROOT = Split-Path $BIN_DIR -Parent

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Decap CMS - Servidor Local" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se o Node.js esta instalado
if (-not (Test-Path $NODE_EXE)) {
    Write-Host "Node.js nao encontrado em: $NODE_DIR" -ForegroundColor Red
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

# Exibir versoes
Write-Host "Node.js: " -NoNewline -ForegroundColor Green
& $NODE_EXE --version
Write-Host "npm: " -NoNewline -ForegroundColor Green
& $NPM_CMD --version
Write-Host ""

# Verificar e instalar dependencias se necessario
$HTTP_SERVER_CHECK = Join-Path $NODE_DIR "node_modules\http-server"
$DECAP_SERVER_CHECK = Join-Path $NODE_DIR "node_modules\decap-server"

if (-not (Test-Path $HTTP_SERVER_CHECK)) {
    Write-Host "Instalando http-server..." -ForegroundColor Yellow
    & $NPM_CMD install -g http-server --prefix $NODE_DIR
    Write-Host ""
}

if (-not (Test-Path $DECAP_SERVER_CHECK)) {
    Write-Host "Instalando decap-server..." -ForegroundColor Yellow
    & $NPM_CMD install -g decap-server --prefix $NODE_DIR
    Write-Host ""
}

# Navegar para o diretório do projeto
Set-Location $PROJECT_ROOT

# Iniciar servidor HTTP na porta 8080 em background
Write-Host "Iniciando servidor HTTP na porta 8080..." -ForegroundColor Yellow
$httpServer = Start-Job -ScriptBlock {
    param($npxCmd, $workDir)
    Set-Location $workDir
    & $npxCmd http-server -p 8080 -c-1
} -ArgumentList $NPX_CMD, $PROJECT_ROOT

Start-Sleep -Seconds 3

# Iniciar decap-server na porta 8081
Write-Host "Iniciando Decap Server na porta 8081..." -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "Servidores iniciados com sucesso!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Acesse o CMS em: " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8080/admin/" -ForegroundColor White
Write-Host ""
Write-Host "Pressione Ctrl+C para parar os servidores." -ForegroundColor Yellow
Write-Host ""

try {
    # Executar o decap-server (este bloqueia até Ctrl+C)
    & $NPX_CMD decap-server
}
catch {
    Write-Host ""
}
finally {
    # Quando o decap-server parar, parar tambem o http-server
    Write-Host ""
    Write-Host "Parando servidor HTTP..." -ForegroundColor Yellow
    Stop-Job -Job $httpServer -ErrorAction SilentlyContinue
    Remove-Job -Job $httpServer -ErrorAction SilentlyContinue
    Write-Host "Servidores encerrados." -ForegroundColor Red
}
