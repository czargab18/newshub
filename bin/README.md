# Scripts de Configuração - Decap CMS

Esta pasta contém scripts para instalar o Node.js localmente e iniciar o servidor Decap CMS.

## 📁 Estrutura

```
bin/
├── start.ps1           # Script All-in-One (RECOMENDADO - faz tudo automaticamente)
├── install-node.ps1    # Instala Node.js localmente
├── start-server.ps1    # Inicia apenas o servidor Decap CMS (porta 8081)
├── start-decap.ps1     # Inicia HTTP Server + Decap Server (portas 8080 e 8081)
├── setup.ps1           # Script completo (instala + inicia)
├── node/               # Node.js será instalado aqui (criado automaticamente)
└── README.md           # Este arquivo
```

## 🚀 Como Usar

### ⭐ Opção Recomendada: Script All-in-One

**Um único comando que faz tudo:**

```powershell
.\bin\start.ps1
```

Este script:
- ✅ Verifica se Node.js está instalado
- ✅ Baixa e instala Node.js automaticamente se necessário
- ✅ Instala http-server e decap-server se necessário
- ✅ Inicia ambos os servidores
- ✅ Você só precisa executar e usar!

Acesse: `http://localhost:8080/admin/`

---

### Outras Opções (avançado)

**Opção 1: Setup Completo (primeira vez):**

```powershell
.\bin\setup.ps1
```

**Opção 2: CMS Completo (HTTP + Backend):**

```powershell
.\bin\start-decap.ps1
```

**Opção 3: Apenas Decap Server:**

```powershell
.\bin\start-server.ps1
```

**Opção 4: Instalação Manual:**

```powershell
.\bin\install-node.ps1
```

## 📋 Requisitos

- Windows PowerShell 5.1 ou superior
- Conexão com a internet (para download do Node.js)
- Aproximadamente 50 MB de espaço em disco

## ⚙️ Configurações

### Alterar Versão do Node.js

Edite o arquivo `install-node.ps1` e modifique a variável:

```powershell
$NODE_VERSION = "20.11.0"  # Altere para a versão desejada
```

### Alterar Porta do Servidor

O Decap Server usa a porta padrão `8081`. Para alterar, você precisará passar argumentos adicionais no `start-server.ps1`.

## 🔧 Solução de Problemas

### Erro: "Não é possível executar scripts neste sistema"

Execute este comando no PowerShell como Administrador:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Node.js já instalado mas não funciona

Reinstale executando:

```powershell
.\bin\install-node.ps1
```

Quando perguntado se deseja reinstalar, responda `s`.

### Servidor não inicia

1. Verifique se o Node.js está instalado:
   ```powershell
   .\bin\node\node.exe --version
   ```

2. Reinstale o Decap Server manualmente:
   ```powershell
   .\bin\node\npm.cmd install -g decap-server --prefix .\bin\node
   ```

## 📝 Notas

- O Node.js é instalado **localmente** na pasta `bin/node` e não afeta instalações globais
- Os arquivos baixados ocupam aproximadamente 45-50 MB
- O arquivo `.gitignore` deve incluir `bin/node/` e `bin/*.zip`

## 🗑️ Desinstalação

Para remover o Node.js local:

```powershell
Remove-Item -Path .\bin\node -Recurse -Force
```

## 📚 Links Úteis

- [Decap CMS](https://decapcms.org/)
- [Node.js Downloads](https://nodejs.org/dist/)
- [Documentação Decap Server](https://decapcms.org/docs/beta-features/#working-with-a-local-git-repository)
