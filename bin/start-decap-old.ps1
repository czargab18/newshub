# Script para iniciar o Decap CMS Server com Node.js Portable
$NODE_DIR = "c:\Users\cesar.oliveira\node-portable\node-v20.10.0-win-x64"
$env:PATH = "$NODE_DIR;$env:PATH"

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "  Decap CMS - Servidor Local" -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Node.js: " -NoNewline
& "$NODE_DIR\node.exe" --version
Write-Host "npm: " -NoNewline
& "$NODE_DIR\npm.cmd" --version
Write-Host ""

# Navegar para o diretório do newshub
Set-Location "c:\Users\cesar.oliveira\github\estatistica\newshub"

# Iniciar servidor HTTP na porta 8080 em background
Write-Host "Iniciando servidor HTTP na porta 8080..." -ForegroundColor Yellow
$httpServer = Start-Job -ScriptBlock {
    param($nodeDir, $workDir)
    Set-Location $workDir
    & "$nodeDir\npx.cmd" http-server -p 8080 -c-1
} -ArgumentList $NODE_DIR, (Get-Location).Path

Start-Sleep -Seconds 3

# Iniciar decap-server na porta 8081
Write-Host "Iniciando Decap Server na porta 8081..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Acesse o CMS em: http://localhost:8080/admin/" -ForegroundColor Green
Write-Host ""
Write-Host "Pressione Ctrl+C para parar os servidores." -ForegroundColor Yellow
Write-Host ""

# Executar o decap-server (este bloqueia até Ctrl+C)
& "$NODE_DIR\npx.cmd" decap-server

# Quando o decap-server parar, parar também o http-server
Write-Host ""
Write-Host "Parando servidor HTTP..." -ForegroundColor Yellow
Stop-Job -Job $httpServer
Remove-Job -Job $httpServer
Write-Host "Servidores encerrados." -ForegroundColor Red
