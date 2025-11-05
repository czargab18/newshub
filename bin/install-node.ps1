# ============================================
# Script para instalar Node.js localmente
# ============================================

$ErrorActionPreference = "Stop"

# Configurações
$NODE_VERSION = "20.11.0"  # Versão LTS do Node.js
$ARCHITECTURE = "x64"      # Arquitetura (x64 ou x86)
$BIN_DIR = $PSScriptRoot
$NODE_DIR = Join-Path $BIN_DIR "node"
$NODE_ZIP = Join-Path $BIN_DIR "node.zip"
$NODE_URL = "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-win-$ARCHITECTURE.zip"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Instalando Node.js v$NODE_VERSION localmente" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se o Node.js já está instalado
if (Test-Path (Join-Path $NODE_DIR "node.exe")) {
    Write-Host "Node.js ja esta instalado em: $NODE_DIR" -ForegroundColor Green
    
    # Verificar versao
    $installedVersion = & (Join-Path $NODE_DIR "node.exe") --version
    Write-Host "Versao instalada: $installedVersion" -ForegroundColor Green
    
    $response = Read-Host "Deseja reinstalar? (s/N)"
    if ($response -ne "s" -and $response -ne "S") {
        Write-Host "Instalacao cancelada." -ForegroundColor Yellow
        exit 0
    }
    
    Write-Host "Removendo instalacao anterior..." -ForegroundColor Yellow
    Remove-Item -Path $NODE_DIR -Recurse -Force -ErrorAction SilentlyContinue
}

# Criar diretório bin se não existir
if (-not (Test-Path $BIN_DIR)) {
    New-Item -ItemType Directory -Path $BIN_DIR -Force | Out-Null
}

# Download do Node.js
Write-Host "Baixando Node.js v$NODE_VERSION..." -ForegroundColor Yellow
Write-Host "URL: $NODE_URL" -ForegroundColor Gray
Write-Host ""

try {
    # Usar WebClient para mostrar progresso
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($NODE_URL, $NODE_ZIP)
    Write-Host "Download concluido!" -ForegroundColor Green
}
catch {
    Write-Host "Erro ao baixar Node.js: $_" -ForegroundColor Red
    exit 1
}

# Descompactar
Write-Host ""
Write-Host "Descompactando Node.js..." -ForegroundColor Yellow

try {
    # Descompactar usando Expand-Archive
    Expand-Archive -Path $NODE_ZIP -DestinationPath $BIN_DIR -Force
    
    # Renomear pasta extraida para "node"
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
        Write-Host "Arquivo ZIP removido." -ForegroundColor Gray
    }
}

# Verificar instalacao
Write-Host ""
Write-Host "Verificando instalacao..." -ForegroundColor Yellow

$nodeExe = Join-Path $NODE_DIR "node.exe"
$npmCmd = Join-Path $NODE_DIR "npm.cmd"

if ((Test-Path $nodeExe) -and (Test-Path $npmCmd)) {
    $nodeVersion = & $nodeExe --version
    $npmVersion = & $npmCmd --version
    
    Write-Host ""
    Write-Host "============================================" -ForegroundColor Green
    Write-Host "Node.js instalado com sucesso!" -ForegroundColor Green
    Write-Host "============================================" -ForegroundColor Green
    Write-Host "Node.js: $nodeVersion" -ForegroundColor Cyan
    Write-Host "npm: $npmVersion" -ForegroundColor Cyan
    Write-Host "Localizacao: $NODE_DIR" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Para usar o Node.js local, execute:" -ForegroundColor Yellow
    Write-Host "  .\bin\start-server.ps1" -ForegroundColor White
    Write-Host ""
}
else {
    Write-Host "Erro: Instalacao falhou!" -ForegroundColor Red
    exit 1
}
