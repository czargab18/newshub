# 📰 Newshub - Sistema de Renderização estatística/newsroom

Sistema avançado de renderização de Markdown para HTML no estilo estatística/newsroom, com suporte a componentes dinâmicos, processamento de imagens e templates customizáveis.

## 🚀 Características Principais

- **🎨 Templates estatística/newsroom**: Design autêntico e responsivo
- **🧩 Sistema de Componentes**: Headers, footers, navegação dinâmica
- **🖼️ Processamento de Imagens**: Cópia e organização automática
- **📊 Frontmatter Rico**: Metadados YAML completos
- **⚡ Multi-linguagem**: Scripts Python, PowerShell e Batch
- **🔄 Output Inteligente**: `artigo.md` → `index.html` automaticamente

## 📁 Estrutura do Projeto

```
newshub/
├── build/
│   ├── article/          # Artigos de exemplo
│   │   ├── artigo.md     # Markdown com frontmatter
│   │   ├── img1.png      # Imagens
│   │   └── output/       # 📁 Output padrão (gerado automaticamente)
│   │       ├── index.html    # HTML renderizado
│   │       └── src/          # Imagens processadas
│   ├── components/       # Componentes HTML
│   │   ├── article-header.html
│   │   ├── globalfooter.html
│   │   ├── globalheader.html
│   │   └── localnav.html
│   ├── modelos/          # Templates
│   │   └── template.html # Template principal Pandoc
│   └── run/              # Scripts de renderização
│       ├── render.py     # ✅ Script Python principal
│       ├── render.ps1    # Script PowerShell
│       ├── render.cmd    # Script Windows Batch
│       └── config/       # Configurações
└── README.md             # Esta documentação

```
nova estrutura de diretórios
```
.vscode/
run/
|  └─ artigo.py
ac/
  ├─ modelos/
  └─ components/
article/
  ├─ build/
  │   ├─ artigo.qmd
  │   ├─ img/
  │   └─ src/
  └─ _output_/
      ├─ index.html
      ├─ img/
      └─ src/
newsroom/
|  └─ archive/
|  |    └─ ano/
|  |       └─ mes/
|  |           └─ xxxx/   # onde xxxx vai de 0000 a 9999
                  ├─ index.html
                  ├─ img/
                  └─ src/
```

## 📰 Novo Script dos Artigos

```python
# Output padrão (organização por ano/mês/código)
python run/artigo.py --basedir article/_output_/artigo.html --template templates/artigo/html/body.html

# Output personalizado (mantém organização por ano/mês/código dentro da pasta escolhida)
python run/artigo.py --basedir article/_output_/artigo.html --template templates/artigo/html/body.html --outputdir output/
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