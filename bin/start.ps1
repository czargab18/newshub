# ============================================
# Script All-in-One: Decap CMS Server + Auth
# ============================================
# Este script faz tudo automaticamente:
# 1. Verifica se Node.js esta instalado
# 2. Instala Node.js se necessario
# 3. Instala dependencias (http-server + auth-server)
# 4. Configura ambiente local (config.local.yml)
# 5. Inicia os servidores (auth + http)

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
Write-Host "Este script iniciara:" -ForegroundColor Yellow
Write-Host "  1. Auth Server (porta 3000)" -ForegroundColor Gray
Write-Host "  2. HTTP Server (porta 8080)" -ForegroundColor Gray
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
$AUTH_DIR = Join-Path $PROJECT_ROOT "auth"
$AUTH_NODE_MODULES = Join-Path $AUTH_DIR "node_modules"

# Verificar http-server
if (-not (Test-Path $HTTP_SERVER_CHECK)) {
    Write-Host "[!] Instalando http-server..." -ForegroundColor Yellow
    & $NPM_CMD install -g http-server --prefix $NODE_DIR --silent
    Write-Host "[OK] http-server instalado!" -ForegroundColor Green
} else {
    Write-Host "[OK] http-server ja instalado!" -ForegroundColor Green
}

# Verificar dependencias do auth-server
if (-not (Test-Path $AUTH_NODE_MODULES)) {
    Write-Host "[!] Instalando dependencias do auth-server..." -ForegroundColor Yellow
    Push-Location $AUTH_DIR
    & $NPM_CMD install
    Pop-Location
    Write-Host "[OK] auth-server dependencias instaladas!" -ForegroundColor Green
} else {
    Write-Host "[OK] auth-server dependencias ja instaladas!" -ForegroundColor Green
}

Write-Host ""

# ============================================
# PASSO 3: Configurar Ambiente Local
# ============================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Configurando Ambiente Local" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$ADMIN_DIR = Join-Path $PROJECT_ROOT "admin"
$CONFIG_LOCAL = Join-Path $ADMIN_DIR "config.local.yml"
$CONFIG_PROD = Join-Path $ADMIN_DIR "config.yml"
$CONFIG_BACKUP = Join-Path $ADMIN_DIR "config.prod.yml"

# Backup do config.yml de producao se nao existir
if ((Test-Path $CONFIG_PROD) -and -not (Test-Path $CONFIG_BACKUP)) {
    Write-Host "[*] Criando backup do config.yml de producao..." -ForegroundColor Yellow
    Copy-Item $CONFIG_PROD $CONFIG_BACKUP -Force
    Write-Host "[OK] Backup criado: config.prod.yml" -ForegroundColor Green
}

# Copiar config.local.yml para config.yml
if (Test-Path $CONFIG_LOCAL) {
    Write-Host "[*] Aplicando configuracao local..." -ForegroundColor Yellow
    Copy-Item $CONFIG_LOCAL $CONFIG_PROD -Force
    Write-Host "[OK] config.yml agora aponta para localhost:3000" -ForegroundColor Green
} else {
    Write-Host "[!] AVISO: config.local.yml nao encontrado!" -ForegroundColor Red
    Write-Host "    Usando config.yml existente (pode apontar para producao)" -ForegroundColor Yellow
}

Write-Host ""

# ============================================
# PASSO 4: Iniciar Servidores
# ============================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Iniciando Servidores" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Navegar para o diretorio do projeto
Set-Location $PROJECT_ROOT

# Iniciar auth-server na porta 3000 em background
Write-Host "[*] Iniciando Auth Server (porta 3000)..." -ForegroundColor Yellow
$authServer = Start-Job -ScriptBlock {
    param($nodeExe, $authDir)
    Set-Location $authDir
    & $nodeExe app.js
} -ArgumentList $NODE_EXE, $AUTH_DIR

Start-Sleep -Seconds 3

# Verificar se auth-server esta rodando
$authRunning = $false
try {
    $response = Invoke-WebRequest -Uri "http://localhost:3000/" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
    if ($response.StatusCode -eq 200) {
        $authRunning = $true
        Write-Host "[OK] Auth Server iniciado!" -ForegroundColor Green
    }
} catch {
    Write-Host "[!] Auth Server pode nao ter iniciado. Verifique o log." -ForegroundColor Yellow
}

# Iniciar servidor HTTP na porta 8080
Write-Host "[*] Iniciando HTTP Server (porta 8080)..." -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Servidores iniciados com sucesso!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "CMS Admin:  " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8080/admin/" -ForegroundColor White
Write-Host "Auth Server:" -NoNewline -ForegroundColor Cyan
Write-Host " http://localhost:3000/" -ForegroundColor White
Write-Host ""
Write-Host "Para fazer login:" -ForegroundColor Yellow
Write-Host "  1. Acesse http://localhost:8080/admin/" -ForegroundColor Gray
Write-Host "  2. Clique em 'Login with GitHub'" -ForegroundColor Gray
Write-Host "  3. Autorize a aplicacao no GitHub" -ForegroundColor Gray
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
    # Quando parar, encerrar tambem o auth-server
    Write-Host ""
    Write-Host "Parando servidores..." -ForegroundColor Yellow
    Stop-Job -Job $authServer -ErrorAction SilentlyContinue
    Remove-Job -Job $authServer -ErrorAction SilentlyContinue
    
    # Restaurar config de producao
    if (Test-Path $CONFIG_BACKUP) {
        Write-Host "Restaurando config.yml de producao..." -ForegroundColor Yellow
        Copy-Item $CONFIG_BACKUP $CONFIG_PROD -Force
        Write-Host "[OK] Configuracao de producao restaurada" -ForegroundColor Green
    }
    
    Write-Host "Servidores encerrados." -ForegroundColor Red
}
