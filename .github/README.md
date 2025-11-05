# 📰 Newshub - Sistema de Renderização estatística/newsroom

Sistema avançado de renderização de Markdown para HTML no estilo estatística/newsroom, com suporte a componentes dinâmicos, processamento de imagens e templates customizáveis.

- Exemplo de uso: [artigo](https://czargab18.github.io/newshub/archive/2025/07/0000/index.html)

## 🎯 Início Rápido

### 📝 Gerenciar Conteúdo com Decap CMS

**Setup Automático (Primeira vez):**
```powershell
.\bin\setup.ps1
```

**CMS Completo (HTTP + Backend):**
```powershell
.\bin\start-decap.ps1
```
Acesse em: `http://localhost:8080/admin/`

**Apenas Backend:**
```powershell
.\bin\start-server.ps1
```
Servidor em: `http://localhost:8081`

> **Nota:** Os scripts instalam o Node.js localmente na pasta `bin/` sem afetar seu sistema.
> 
> **Documentação completa:** Veja `bin/README.md` para mais detalhes e solução de problemas.

---

## 🚀 Características Principais

- **🎨 Templates estatística/newsroom**: Design autêntico e responsivo
- **🧩 Sistema de Componentes**: Headers, footers, navegação dinâmica
- **🖼️ Processamento de Imagens**: Cópia e organização automática
- **📊 Frontmatter Rico**: Metadados YAML completos
- **⚡ Multi-linguagem**: Scripts Python, PowerShell e Batch
- **🔄 Output Inteligente**: `artigo.md` → `index.html` automaticamente

## 📁 Estrutura do Projeto

```
.vscode/                  # Configurações do VSCode
run/
│   └─ artigo.py          # Script principal de processamento/renderização
ac/
│   ├─ modelos/           # Templates HTML
│   └─ components/        # Componentes HTML reutilizáveis
article/
│   ├─ build/             # Artigos em desenvolvimento
│   │   ├─ artigo.qmd     # Fonte Quarto/Markdown do artigo
│   │   ├─ img/           # Imagens do artigo
│   │   └─ src/           # Outros recursos do artigo
│   └─ _output_/          # Output temporário/exportado do artigo
│   │    ├─ index.html     # HTML intermediário gerado
│   │    ├─ img/           # Imagens exportadas
│   │    └─ src/           # Recursos exportados
newsroom/
│   └─ archive/           # Output final organizado por data
│   │   └─ ano/
│   │   │   └─ mes/
│   │   │   │   └─ xxxx/  # xxxx vai de 0000 a 9999 (incremental por artigo)
│   │   │   │   │   ├─ index.html # artigo
│   │   │   │   │   ├─ img/
│   │   │   │   │   └─ src/
```
- O script `run/artigo.py` processa o HTML do artigo e copia as pastas `img/` e `src/` para o destino final.
- O output final é sempre organizado por ano, mês e código incremental, facilitando o arquivamento e a publicação.

---

## 📰 Renderizar Artigos

completo e único
```bash
echo "Navegando para o diretório do artigo..."
cd newshub/article/ ;

echo "Renderizando artigo com Quarto..."
quarto render article/ --output-dir ../artefatos/ ; 

echo "Automatizando a geração do HTML do artigo"
cd ../ ; 
python ./run/article.py --basedir ./artefatos/artigo.html --outputdir newsroom/archive  
```

só o script de automaçao
```python
# Output padrão (organização por ano/mês/código)
python ./run/article.py --basedir ./artefatos/artigo.html --outputdir newsroom/

# Output personalizado (mantém organização por ano/mês/código dentro da pasta escolhida)
python ./run/article.py --basedir ./artefatos/artigo.html --outputdir newsroom/ --outputdir output/
```

O arquivo gerado será salvo em:
- Padrão: `newsroom/archive/ANO/MES/XXXX/index.html`
- Personalizado: `output/ANO/MES/XXXX/index.html`

As pastas `img/` e `src/` do artigo também são copiadas para o mesmo destino.

---

## 🛠️ Como Usar

### 📍 Comando Principal:
```bash
# Do diretório raiz do projeto
python run/artigo.py --basedir article/_output_/artigo.html --template templates/artigo/html/body.html
```

### 📋 Parâmetros Disponíveis:
- `--basedir` - Caminho do arquivo HTML de entrada
- `--template` - Caminho do template HTML
- `--outputdir` - Diretório de saída personalizado (opcional)

---

**📰 Newshub** - Transformando Markdown em experiências web de qualidade estatística/newsroom