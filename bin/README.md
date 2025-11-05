# Scripts de Configuração - Decap CMS

Esta pasta contém o script para instalar o Node.js localmente e iniciar o servidor Decap CMS.

## 📁 Estrutura

```
bin/
├── start.ps1           # Script All-in-One (faz tudo automaticamente)
├── node/               # Node.js será instalado aqui (criado automaticamente)
└── README.md           # Este arquivo
```

## 🚀 Como Usar

### ⭐ Comando Único

**Execute este comando para fazer tudo automaticamente:**

```powershell
.\bin\start.ps1
```

**O que ele faz:**
- ✅ Verifica se Node.js está instalado
- ✅ Baixa e instala Node.js v20.11.0 automaticamente se necessário (~45MB)
- ✅ Instala http-server e decap-server se necessário
- ✅ Inicia ambos os servidores
- ✅ Pronto para usar!

**Acesse:**
- CMS Admin: `http://localhost:8080/admin/`
- API Local: `http://localhost:8081`

**Para parar os servidores:**
- Pressione `Ctrl+C` no terminal

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
