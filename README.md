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
nova
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

## 🛠️ Como Usar

### 📍 Comando Principal:
```bash
# Do diretório raiz do projeto pai
python newshub/build/run/render.py newshub/build/article/artigo.md --elements preset:comunicado_simples --base-dir newsroom/archive
```

### 📋 Parâmetros Disponíveis:
- `-o, --output` - Arquivo de saída personalizado
- `-b, --batch` - Modo lote para processar diretórios
- `-v, --verbose` - Output detalhado
- `--open` - Abre no navegador automaticamente
- `--base-dir` - Diretório de saída personalizado (substitui o padrão `build/article/output/`)

### 📖 Exemplos:
```bash
# Básico
python build/run/render.py build/article/artigo.md

# Com output personalizado
python build/run/render.py build/article/artigo.md -o index.html

# Verbose + abertura automática
python build/run/render.py build/article/artigo.md --verbose --open

# Com diretório de saída personalizado
python build/run/render.py build/article/artigo.md --base-dir minha_pasta/

# Modo lote
python build/run/render.py pasta/ --batch
```

## 📊 Dependências

- **Python 3.7+**
- **pypandoc** - Para conversão Markdown → HTML
- **Pandoc** - Motor de conversão (instalado via pypandoc)

### 🔧 Instalação:
```bash
pip install pypandoc
```

## 🎯 Características Especiais

- **📁 Output Inteligente**: 
  - Padrão: `build/article/output/` (organizados junto com os artigos)
  - Se existe pasta `output/` local junto ao arquivo fonte, usa a local
- **🖼️ Gestão de Imagens**: Copia para pasta `src/` automaticamente
- **🔄 Nome Inteligente**: `artigo.md` vira `index.html`
- **🧩 Includes Dinâmicos**: Baseados no frontmatter YAML
- **📱 Design Responsivo**: Otimizado para todos os dispositivos

## 📝 Licença

Este projeto é parte do repositório `estatistica` e segue a mesma licença.

## 🤝 Contribuição

Para contribuir, faça um fork do repositório principal e submeta um Pull Request.

---

**📰 Newshub** - Transformando Markdown em experiências web de qualidade estatística/n