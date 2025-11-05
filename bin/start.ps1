# ============================================
# Script All-in-One: Decap CMS Server
# ============================================
# Este script faz tudo automaticamente:
# 1. Verifica se Node.js esta instalado
# 2. Instala Node.js se necessario
# 3. Instala dependencias (decap-server, http-server)
# 4. Inicia os servidores

$ErrorActionPreference = "Stop"

# Configuracoes
$NODE_VERSION = "20.11.0"
$ARCHITECTURE = "x64"
$BIN_DIR = $PSScriptRoot
$NODE_DIR = Join-Path $BIN_DIR "node"
$NODE_EXE = Join-Path $NODE_DIR "node.exe"
$NPM_CMD = Join-Path $NODE_DIR "npm.cmd"
$NPX_CMD = Join-Path $NODE_DIR "npx.cmd"
$NODE_ZIP = Join-Path $BIN_DIR "node.zip"
$NODE_URL = "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-win-$ARCHITECTURE.zip"
$PROJECT_ROOT = Split-Path $BIN_DIR -Parent

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Decap CMS - Servidor Local (All-in-One)" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# ============================================
# PASSO 1: Verificar/Instalar Node.js
# ============================================

if (Test-Path $NODE_EXE) {
    Write-Host "[OK] Node.js encontrado!" -ForegroundColor Green
    $nodeVersion = & $NODE_EXE --version
    $npmVersion = & $NPM_CMD --version
    Write-Host "     Node.js: $nodeVersion" -ForegroundColor Gray
    Write-Host "     npm: $npmVersion" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-Host "[!] Node.js nao encontrado. Instalando..." -ForegroundColor Yellow
    Write-Host ""
    
    # Criar diretorio bin se nao existir
    if (-not (Test-Path $BIN_DIR)) {
        New-Item -ItemType Directory -Path $BIN_DIR -Force | Out-Null
    }
    
    # Download do Node.js
    Write-Host "Baixando Node.js v$NODE_VERSION..." -ForegroundColor Yellow
    Write-Host "URL: $NODE_URL" -ForegroundColor Gray
    
    try {
        $webClient = New-Object System.Net.WebClient
        $webClient.DownloadFile($NODE_URL, $NODE_ZIP)
        Write-Host "Download concluido!" -ForegroundColor Green
        Write-Host ""
    }
    catch {
        Write-Host "Erro ao baixar Node.js: $_" -ForegroundColor Red
        exit 1
    }
    
    # Descompactar
    Write-Host "Descompactando Node.js..." -ForegroundColor Yellow
    
    try {
        Expand-Archive -Path $NODE_ZIP -DestinationPath $BIN_DIR -Force
        
        # Renomear pasta extraida
        $extractedFolder = Join-Path $BIN_DIR "node-v$NODE_VERSION-win-$ARCHITECTURE"
        if (Test-Path $extractedFolder) {
            Move-Item -Path $extractedFolder -Destination $NODE_DIR -Force
        }
        
        Write-Host "Descompactacao concluida!" -ForegroundColor Green
    }
    catch {
        Write-Host "Erro ao descompactar: $_" -ForegroundColor Red
        exit 1
    }
    finally {
        # Limpar arquivo ZIP
        if (Test-Path $NODE_ZIP) {
            Remove-Item -Path $NODE_ZIP -Force
        }
    }
    
    # Verificar instalacao
    if ((Test-Path $NODE_EXE) -and (Test-Path $NPM_CMD)) {
        $nodeVersion = & $NODE_EXE --version
        $npmVersion = & $NPM_CMD --version
        
        Write-Host ""
        Write-Host "[OK] Node.js instalado com sucesso!" -ForegroundColor Green
        Write-Host "     Node.js: $nodeVersion" -ForegroundColor Gray
        Write-Host "     npm: $npmVersion" -ForegroundColor Gray
        Write-Host ""
    }
    else {
        Write-Host "Erro: Instalacao falhou!" -ForegroundColor Red
        exit 1
    }
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

# Iniciar servidor HTTP na porta 8080 em background
Write-Host "[*] Iniciando HTTP Server (porta 8080)..." -ForegroundColor Yellow
$httpServer = Start-Job -ScriptBlock {
    param($npxCmd, $workDir)
    Set-Location $workDir
    & $npxCmd http-server -p 8080 -c-1
} -ArgumentList $NPX_CMD, $PROJECT_ROOT

Start-Sleep -Seconds 3

# Iniciar decap-server na porta 8081
Write-Host "[*] Iniciando Decap Server (porta 8081)..." -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Servidores iniciados com sucesso!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "CMS Admin: " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8080/admin/" -ForegroundColor White
Write-Host "API Local: " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8081" -ForegroundColor White
Write-Host ""
Write-Host "Pressione Ctrl+C para parar os servidores." -ForegroundColor Yellow
Write-Host ""

try {
    # Executar o decap-server (bloqueia ate Ctrl+C)
    & $NPX_CMD decap-server
}
catch {
    Write-Host ""
}
finally {
    # Quando o decap-server parar, parar tambem o http-server
    Write-Host ""
    Write-Host "Parando servidores..." -ForegroundColor Yellow
    Stop-Job -Job $httpServer -ErrorAction SilentlyContinue
    Remove-Job -Job $httpServer -ErrorAction SilentlyContinue
    Write-Host "Servidores encerrados." -ForegroundColor Red
}
