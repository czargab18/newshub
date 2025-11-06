# ============================================
# Script: Decap CMS - Desenvolvimento Local
# ============================================
# Este script inicia o ambiente de desenvolvimento local:
# 1. Verifica Node.js
# 2. Inicia decap-server (backend local - porta 8081)
# 3. Inicia http-server (servindo dev-test/ - porta 8080)
# 
# IMPORTANTE: Este modo usa local_backend: true
# Não requer OAuth ou auth-server
# Edições são feitas localmente (não commitadas automaticamente)

$ErrorActionPreference = "Stop"

# Configuracoes
$BIN_DIR = $PSScriptRoot
$NODE_DIR = Join-Path $BIN_DIR "node"
$NODE_EXE = Join-Path $NODE_DIR "node.exe"
$NPM_CMD = Join-Path $NODE_DIR "npm.cmd"
$NPX_CMD = Join-Path $NODE_DIR "npx.cmd"
$PROJECT_ROOT = Split-Path $BIN_DIR -Parent

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Decap CMS - Modo Desenvolvimento Local" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Este modo usa:" -ForegroundColor Yellow
Write-Host "  - Pasta: dev-test/" -ForegroundColor Gray
Write-Host "  - Backend: Local (sem OAuth)" -ForegroundColor Gray
Write-Host "  - Decap Server: Porta 8081" -ForegroundColor Gray
Write-Host "  - HTTP Server: Porta 8080" -ForegroundColor Gray
Write-Host ""

# ============================================
# PASSO 1: Verificar Node.js
# ============================================

if (Test-Path $NODE_EXE) {
    Write-Host "[OK] Node.js encontrado!" -ForegroundColor Green
    $nodeVersion = & $NODE_EXE --version
    $npmVersion = & $NPM_CMD --version
    Write-Host "     Node.js: $nodeVersion" -ForegroundColor Gray
    Write-Host "     npm: $npmVersion" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host "[ERRO] Node.js nao encontrado em bin/node/" -ForegroundColor Red
    Write-Host "Execute primeiro: .\bin\start.ps1" -ForegroundColor Yellow
    Write-Host "Ou instale manualmente na pasta bin/node/" -ForegroundColor Yellow
    exit 1
}

# ============================================
# PASSO 2: Verificar/Instalar Dependencias
# ============================================

$HTTP_SERVER_CHECK = Join-Path $NODE_DIR "node_modules\http-server"
$DECAP_SERVER_CHECK = Join-Path $NODE_DIR "node_modules\decap-server"

# Verificar http-server
if (-not (Test-Path $HTTP_SERVER_CHECK)) {
    Write-Host "[!] Instalando http-server..." -ForegroundColor Yellow
    & $NPM_CMD install -g http-server --prefix $NODE_DIR --silent
    Write-Host "[OK] http-server instalado!" -ForegroundColor Green
} else {
    Write-Host "[OK] http-server ja instalado!" -ForegroundColor Green
}

# Verificar decap-server
if (-not (Test-Path $DECAP_SERVER_CHECK)) {
    Write-Host "[!] Instalando decap-server..." -ForegroundColor Yellow
    & $NPM_CMD install -g decap-server --prefix $NODE_DIR --silent
    Write-Host "[OK] decap-server instalado!" -ForegroundColor Green
} else {
    Write-Host "[OK] decap-server ja instalado!" -ForegroundColor Green
}

Write-Host ""

# ============================================
# PASSO 3: Iniciar Servidores
# ============================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Iniciando Servidores" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Navegar para o diretorio do projeto
Set-Location $PROJECT_ROOT

# Iniciar decap-server na porta 8081 em background
Write-Host "[*] Iniciando Decap Server (porta 8081)..." -ForegroundColor Yellow
$decapServer = Start-Job -ScriptBlock {
    param($npxCmd, $workDir)
    Set-Location $workDir
    & $npxCmd decap-server
} -ArgumentList $NPX_CMD, $PROJECT_ROOT

Start-Sleep -Seconds 3

# Verificar se decap-server esta rodando
$decapRunning = $false
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8081/api/v1" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
    if ($response.StatusCode -eq 200) {
        $decapRunning = $true
        Write-Host "[OK] Decap Server iniciado!" -ForegroundColor Green
    }
} catch {
    Write-Host "[!] Decap Server pode nao ter iniciado. Continuando..." -ForegroundColor Yellow
}

# Iniciar servidor HTTP na porta 8080
Write-Host "[*] Iniciando HTTP Server (porta 8080)..." -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Servidores iniciados com sucesso!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "CMS Admin:   " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8080/dev-test/admin/" -ForegroundColor White
Write-Host "Decap API:   " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8081/api/v1" -ForegroundColor White
Write-Host ""
Write-Host "Modo: " -NoNewline -ForegroundColor Yellow
Write-Host "LOCAL BACKEND" -ForegroundColor White
Write-Host "  - Sem login necessario" -ForegroundColor Gray
Write-Host "  - Mudancas ficam locais (nao commitadas)" -ForegroundColor Gray
Write-Host "  - Ideal para testar o CMS" -ForegroundColor Gray
Write-Host ""
Write-Host "Pressione Ctrl+C para parar os servidores." -ForegroundColor Yellow
Write-Host ""

try {
    # Executar o http-server (bloqueia ate Ctrl+C)
    & $NPX_CMD http-server -p 8080 -c-1
}
catch {
    Write-Host ""
}
finally {
    # Quando parar, encerrar tambem o decap-server
    Write-Host ""
    Write-Host "Parando servidores..." -ForegroundColor Yellow
    Stop-Job -Job $decapServer -ErrorAction SilentlyContinue
    Remove-Job -Job $decapServer -ErrorAction SilentlyContinue
    Write-Host "Servidores encerrados." -ForegroundColor Red
}
