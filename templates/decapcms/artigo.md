# 📄 Documentação do Schema de Artigo

Este documento explica todos os campos do arquivo `artigo.build.json` e como utilizá-los corretamente.

---

## 📋 Índice

1. [Identificação e Datas](#1-identificação-e-datas)
2. [Status de Publicação](#2-status-de-publicação)
3. [Conteúdo Principal](#3-conteúdo-principal)
4. [Autoria](#4-autoria)
5. [Categorização](#5-categorização)
6. [Imagens](#6-imagens)
7. [Mídia Adicional](#7-mídia-adicional)
8. [Corpo do Artigo](#8-corpo-do-artigo)
9. [Referências e Citações](#9-referências-e-citações)
10. [Relacionamentos](#10-relacionamentos)
11. [Campos Personalizados](#11-campos-personalizados)

---

## 1. 🆔 Identificação e Datas

### `id` (string)
- **Descrição**: Identificador único do artigo
- **Formato**: Numérico com zeros à esquerda
- **Exemplo**: `"0001"`, `"0156"`, `"1234"`
- **Uso**: Referência única para o artigo no sistema

### `ano` (string)
- **Descrição**: Ano de publicação
- **Formato**: YYYY
- **Exemplo**: `"2025"`

### `month` (string)
- **Descrição**: Mês de publicação
- **Formato**: Numérico (01-12)
- **Exemplo**: `"11"` (novembro)

### `date_format` (string)
- **Descrição**: Data formatada para exibição
- **Formato**: Texto livre, legível por humanos
- **Exemplo**: `"4 de Novembro de 2025"`

### `date_updated` (string)
- **Descrição**: Data/hora da última atualização
- **Formato**: ISO 8601 com timezone
- **Exemplo**: `"2025-11-04T10:30:00.000-03:00"`

---

## 2. ✅ Status de Publicação

### `published` (boolean)
- **Descrição**: Indica se o artigo está publicado
- **Opções**:
  - `true` → Artigo publicado e visível
  - `false` → Artigo não publicado
- **Exemplo**: `true`

### `featured` (boolean)
- **Descrição**: Indica se o artigo está em destaque
- **Opções**:
  - `true` → Aparece em áreas de destaque (homepage, banners)
  - `false` → Artigo normal
- **Exemplo**: `false`

### `draft` (boolean)
- **Descrição**: Indica se o artigo está em rascunho
- **Opções**:
  - `true` → Rascunho (em edição)
  - `false` → Finalizado
- **Exemplo**: `false`

---

## 3. 📝 Conteúdo Principal

### `title` (string)
- **Descrição**: Título principal do artigo
- **Tamanho recomendado**: 40-60 caracteres
- **Exemplo**: `"Censo 2025: População brasileira cresce 2,5%"`
- **Obrigatório**: ✅ Sim

### `subtitle` (string)
- **Descrição**: Subtítulo ou linha de apoio
- **Tamanho recomendado**: 60-100 caracteres
- **Exemplo**: `"IBGE divulga primeiros resultados do Censo Demográfico"`

### `slug` (string)
- **Descrição**: URL amigável do artigo
- **Formato**: minúsculas, hífens, sem acentos
- **Exemplo**: `"censo-2025-populacao-brasileira-cresce"`
- **Uso**: URL final será `/artigo/censo-2025-populacao-brasileira-cresce`

### `excerpt` (string)
- **Descrição**: Resumo curto para listagens
- **Tamanho recomendado**: 120-160 caracteres
- **Exemplo**: `"IBGE divulga os primeiros resultados do Censo 2025, mostrando crescimento populacional de 2,5% em relação a 2022."`
- **Uso**: Cards, previews, meta description

### `summary` (string)
- **Descrição**: Resumo detalhado do conteúdo
- **Tamanho recomendado**: 200-300 caracteres
- **Exemplo**: `"O Instituto Brasileiro de Geografia e Estatística divulgou hoje os primeiros resultados do Censo Demográfico 2025. Os dados mostram um crescimento populacional de 2,5% nos últimos três anos, com destaque para as regiões Norte e Centro-Oeste."`

---

## 4. 👤 Autoria

### `author` (string)
- **Descrição**: Nome do autor principal
- **Exemplo**: `"César Oliveira"`
- **Obrigatório**: ✅ Sim

### `author_bio` (string)
- **Descrição**: Biografia curta do autor
- **Tamanho recomendado**: 100-200 caracteres
- **Exemplo**: `"Estatístico e analista de dados no IBGE, especialista em análise demográfica"`

### `author_avatar` (string)
- **Descrição**: URL da foto do autor
- **Formato**: Caminho relativo ou URL completa
- **Exemplo**: `"/assets/avatars/cesar-oliveira.jpg"`

### `contributors` (array)
- **Descrição**: Lista de colaboradores do artigo
- **Estrutura**:
  ```json
  {
    "name": "Nome completo",
    "role": "Função/papel",
    "email": "contato@email.com"
  }
  ```

#### Opções de `role`:
- `"Editor"` - Revisou e editou o texto
- `"Revisor Técnico"` - Revisão científica/técnica
- `"Co-autor"` - Escreveu parte do conteúdo
- `"Pesquisador"` - Coletou ou analisou dados
- `"Designer Gráfico"` - Criou elementos visuais
- `"Fotógrafo"` - Produziu fotografias
- `"Tradutor"` - Traduziu o conteúdo
- `"Consultor"` - Forneceu expertise

**Exemplo**:
```json
"contributors": [
  {
    "name": "Maria Silva",
    "role": "Editora",
    "email": "maria.silva@ibge.gov.br"
  },
  {
    "name": "Dr. João Santos",
    "role": "Revisor Técnico",
    "email": "joao.santos@ibge.gov.br"
  }
]
```

---

## 5. 🏷️ Categorização

### `type` (string)
- **Descrição**: Tipo de conteúdo
- **Opções disponíveis**:
  - `"news"` - Notícia
  - `"article"` - Artigo
  - `"event"` - Evento
  - `"press"` - Comunicado de imprensa
  - `"analysis"` - Análise técnica
  - `"report"` - Relatório
- **Exemplo**: `"news"`

### `category` (array)
- **Descrição**: Categorias do artigo (pode ter múltiplas)
- **Opções disponíveis**:
  - `"QUICK READ"` - Leitura rápida
  - `"EST STATEMENT"` - Declaração estatística oficial
  - `"PHOTOS"` - Galeria de fotos
  - `"PRESS RELEASE"` - Comunicado à imprensa
  - `"RELEASE"` - Lançamento/divulgação
  - `"UPDATE"` - Atualização
- **Exemplo**: `["PRESS RELEASE", "UPDATE"]`

### `subcategory` (string)
- **Descrição**: Subcategoria específica
- **Exemplos**: `"Demografia"`, `"Economia"`, `"Social"`, `"Territorial"`

### `tags` (array)
- **Descrição**: Tags/palavras-chave para busca interna
- **Formato**: Array de strings
- **Exemplo**: `["censo", "população", "demografia", "ibge", "2025"]`
- **Uso**: Filtros, busca, agrupamento

### `keywords` (array)
- **Descrição**: Palavras-chave para SEO
- **Formato**: Array de strings ou frases
- **Exemplo**: `["censo demográfico 2025", "população brasileira", "dados ibge"]`
- **Uso**: Meta keywords, otimização de busca

### `language` (string)
- **Descrição**: Idioma do conteúdo
- **Formato**: Código ISO 639-1 + ISO 3166-1
- **Opções comuns**:
  - `"pt-BR"` - Português (Brasil)
  - `"en-US"` - Inglês (Estados Unidos)
  - `"es-ES"` - Espanhol (Espanha)
- **Exemplo**: `"pt-BR"`

---

## 6. 🖼️ Imagens

### `thumbnail` (object)
**Descrição**: Miniatura para listagens e previews  
**Tamanho recomendado**: 600x400px (proporção 3:2)  
**Onde aparece**: Cards, feeds, listas de artigos

**Estrutura**:
```json
{
  "url": "/article/imgs/thumbnail.jpg",
  "alt": "Descrição da imagem para acessibilidade",
  "width": 600,
  "height": 400,
  "caption": "Legenda opcional"
}
```

**Campos**:
- `url` (string) - Caminho da imagem
- `alt` (string) - **Obrigatório** para acessibilidade e SEO
- `width` (number) - Largura em pixels
- `height` (number) - Altura em pixels
- `caption` (string) - Legenda opcional

---

### `cover_image` (object)
**Descrição**: Imagem de capa principal do artigo  
**Tamanho recomendado**: 1920x1080px (proporção 16:9)  
**Onde aparece**: Topo do artigo completo (hero/banner)

**Estrutura**:
```json
{
  "url": "/article/imgs/cover.jpg",
  "alt": "Descrição completa da imagem",
  "width": 1920,
  "height": 1080,
  "caption": "Legenda da imagem de capa",
  "credit": "Foto: João Silva/IBGE"
}
```

**Campos**:
- `url` (string) - Caminho da imagem
- `alt` (string) - **Obrigatório** para acessibilidade e SEO
- `width` (number) - Largura em pixels
- `height` (number) - Altura em pixels
- `caption` (string) - Legenda que aparece abaixo da imagem
- `credit` (string) - **Créditos do fotógrafo/fonte** (obrigatório para direitos autorais)

---

### `images` (array)
**Descrição**: Galeria de imagens do artigo  
**Tamanho recomendado**: 1000x600px (proporção 5:3)  
**Onde aparece**: Ao longo do corpo do artigo

**Estrutura**:
```json
[
  {
    "url": "/article/imgs/grafico1.jpg",
    "alt": "Gráfico de barras mostrando crescimento populacional",
    "caption": "Figura 1: População por região (2020-2025)",
    "width": 1000,
    "height": 600
  },
  {
    "url": "/article/imgs/mapa.jpg",
    "alt": "Mapa do Brasil com densidade demográfica",
    "caption": "Figura 2: Densidade populacional por estado",
    "width": 1000,
    "height": 600
  }
]
```

**Pode conter múltiplas imagens** - adicione quantas forem necessárias.

---

## 7. 🎥 Mídia Adicional

### `videos` (array)
**Descrição**: Vídeos incorporados no artigo

**Estrutura**:
```json
[
  {
    "url": "https://www.youtube.com/watch?v=abc123",
    "type": "youtube",
    "title": "Vídeo explicativo sobre o Censo 2025",
    "thumbnail": "/article/imgs/video-thumb.jpg"
  }
]
```

**Campos**:
- `url` (string) - URL do vídeo
- `type` (string) - Plataforma: `"youtube"`, `"vimeo"`, `"mp4"`
- `title` (string) - Título descritivo do vídeo
- `thumbnail` (string) - Miniatura customizada (opcional)

---

### `attachments` (array)
**Descrição**: Arquivos para download

**Estrutura**:
```json
[
  {
    "name": "Tabela completa - Censo 2025.xlsx",
    "url": "/article/files/tabela-censo-2025.xlsx",
    "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "size": "2.5MB"
  },
  {
    "name": "Relatório PDF",
    "url": "/article/files/relatorio.pdf",
    "type": "application/pdf",
    "size": "1.8MB"
  }
]
```

**Tipos MIME comuns**:
- PDF: `"application/pdf"`
- Excel: `"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"`
- CSV: `"text/csv"`
- Word: `"application/vnd.openxmlformats-officedocument.wordprocessingml.document"`
- ZIP: `"application/zip"`

---

## 8. 📄 Corpo do Artigo

### `body` (string)
- **Descrição**: Conteúdo completo do artigo em HTML
- **Formato**: HTML válido
- **Exemplo**:
```json
"body": "<h2>Introdução</h2><p>O IBGE divulgou hoje...</p><h2>Principais Resultados</h2><p>Os dados mostram...</p>"
```

**Tags HTML permitidas**:
- Títulos: `<h2>`, `<h3>`, `<h4>`
- Parágrafos: `<p>`
- Listas: `<ul>`, `<ol>`, `<li>`
- Ênfase: `<strong>`, `<em>`
- Links: `<a href="...">`
- Imagens: `<img src="..." alt="...">`
- Tabelas: `<table>`, `<tr>`, `<td>`, `<th>`

---

## 9. 📚 Referências e Citações

### `references` (array)
**Descrição**: Bibliografia / fontes consultadas

**Estrutura**:
```json
[
  {
    "title": "Censo Demográfico 2022: Primeiros Resultados",
    "authors": ["IBGE", "Diretoria de Pesquisas"],
    "year": "2023",
    "url": "https://www.ibge.gov.br/censo2022",
    "doi": "10.1234/ibge.censo.2022"
  }
]
```

**Campos**:
- `title` (string) - Título da referência
- `authors` (array) - Lista de autores
- `year` (string) - Ano de publicação
- `url` (string) - Link para a fonte
- `doi` (string) - Digital Object Identifier (opcional)

---

### `citations` (array)
**Descrição**: Citações diretas usadas no artigo

**Estrutura**:
```json
[
  {
    "text": "O Brasil possui uma das maiores biodiversidades do planeta",
    "author": "Dr. José Silva",
    "source": "Estudo sobre Biodiversidade Brasileira (2024)"
  }
]
```

**Uso**: Blocos de citação destacados no artigo

---

## 10. 🔗 Relacionamentos

### `related_articles` (array)
**Descrição**: IDs de artigos relacionados para recomendação

**Formato**: Array de strings (IDs)
**Exemplo**: `["0023", "0045", "0067", "0089"]`

**Uso**: Seção "Leia também" no final do artigo

---

### `series` (object)
**Descrição**: Informações sobre série de artigos

**Estrutura**:
```json
{
  "title_series": "Guia Completo do Censo Demográfico",
  "part": 2,
  "total_parts": 5
}
```

**Campos**:
- `title_series` (string) - Nome/título da série
- `part` (number) - Número da parte atual (este artigo)
- `total_parts` (number) - Total de artigos na série

**Exemplo de uso**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 SÉRIE: Guia Completo do Censo Demográfico
Parte 2 de 5

← Parte 1: Introdução ao Censo
→ Parte 3: Metodologia de Coleta
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 11. 🔧 Campos Personalizados

### `custom_fields` (object)
**Descrição**: Metadados institucionais e contextuais

**Estrutura**:
```json
{
  "research_project": "Pesquisa Nacional por Amostra de Domicílios (PNAD)",
  "funding_source": "Orçamento IBGE 2025",
  "institution": "IBGE - Instituto Brasileiro de Geografia e Estatística"
}
```

**Campos**:
- `research_project` (string) - Nome do projeto de pesquisa
- `funding_source` (string) - Fonte de financiamento
- `institution` (string) - Instituição responsável

**Uso**: Transparência, credibilidade, compliance acadêmico

---

## 📊 Exemplo Completo de Artigo

```json
{
  "id": "0156",
  "ano": "2025",
  "month": "11",
  "date_format": "4 de Novembro de 2025",
  "date_updated": "2025-11-04T10:30:00.000-03:00",
  "published": true,
  "featured": true,
  "draft": false,

  "title": "Censo 2025: População brasileira atinge 215 milhões",
  "subtitle": "IBGE divulga primeiros resultados do Censo Demográfico",
  "slug": "censo-2025-populacao-215-milhoes",
  "excerpt": "O Brasil alcançou 215 milhões de habitantes em 2025, segundo dados preliminares do Censo divulgados hoje pelo IBGE.",
  "summary": "O Instituto Brasileiro de Geografia e Estatística divulgou hoje os primeiros resultados do Censo Demográfico 2025. A população brasileira atingiu 215 milhões de habitantes, representando crescimento de 2,5% em relação ao Censo 2022.",

  "author": "César Oliveira",
  "author_bio": "Estatístico e analista demográfico do IBGE",
  "author_avatar": "/assets/avatars/cesar-oliveira.jpg",
  "contributors": [
    {
      "name": "Maria Silva",
      "role": "Editora",
      "email": "maria.silva@ibge.gov.br"
    }
  ],

  "type": "news",
  "category": ["PRESS RELEASE", "UPDATE"],
  "subcategory": "Demografia",
  "tags": ["censo", "população", "ibge", "2025", "demografia"],
  "keywords": ["censo demográfico 2025", "população brasileira", "ibge dados"],
  "language": "pt-BR",

  "thumbnail": {
    "url": "/article/imgs/censo-2025-thumb.jpg",
    "alt": "Mapa do Brasil com dados populacionais",
    "width": 600,
    "height": 400,
    "caption": ""
  },

  "cover_image": {
    "url": "/article/imgs/censo-2025-cover.jpg",
    "alt": "Sede do IBGE no Rio de Janeiro com banner do Censo 2025",
    "width": 1920,
    "height": 1080,
    "caption": "Divulgação dos resultados do Censo 2025",
    "credit": "Foto: Ana Costa/IBGE"
  },

  "images": [
    {
      "url": "/article/imgs/grafico-populacao.jpg",
      "alt": "Gráfico de barras mostrando crescimento populacional por região",
      "caption": "Figura 1: População por região (2022-2025)",
      "width": 1000,
      "height": 600
    }
  ],

  "videos": [
    {
      "url": "https://www.youtube.com/watch?v=abc123",
      "type": "youtube",
      "title": "Entrevista: Diretor do IBGE explica resultados do Censo",
      "thumbnail": ""
    }
  ],

  "attachments": [
    {
      "name": "Tabela completa - População por UF.xlsx",
      "url": "/article/files/populacao-uf-2025.xlsx",
      "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "size": "1.2MB"
    }
  ],

  "body": "<h2>Crescimento populacional</h2><p>Os dados mostram que a população brasileira cresceu 2,5% desde o último Censo...</p><h2>Distribuição regional</h2><p>As regiões Norte e Centro-Oeste apresentaram os maiores crescimentos...</p>",
  
  "custom_fields": {
    "research_project": "Censo Demográfico 2025",
    "funding_source": "Orçamento IBGE",
    "institution": "IBGE - Diretoria de Pesquisas"
  },
  
  "references": [
    {
      "title": "Censo Demográfico 2022",
      "authors": ["IBGE"],
      "year": "2023",
      "url": "https://www.ibge.gov.br/censo2022",
      "doi": ""
    }
  ],
  
  "citations": [],
  "related_articles": ["0155", "0154", "0150"],
  
  "series": {
    "title_series": "",
    "part": 0,
    "total_parts": 0
  }
}
```

---

## ✅ Checklist de Validação

Antes de publicar um artigo, verifique:

- [ ] `id` único está definido
- [ ] `title` está preenchido (obrigatório)
- [ ] `author` está preenchido (obrigatório)
- [ ] `slug` está no formato correto (minúsculas, hífens)
- [ ] `published` está `true` se quiser publicar
- [ ] `thumbnail` tem URL e `alt` preenchidos
- [ ] `cover_image` tem URL, `alt` e `credit` preenchidos
- [ ] Todas as imagens têm `alt` (acessibilidade)
- [ ] `category` tem pelo menos uma opção selecionada
- [ ] `language` está definido
- [ ] `body` contém o conteúdo completo
- [ ] Links externos abrem em nova aba (se aplicável)
- [ ] Arquivos em `attachments` existem e são acessíveis

---

## 🎯 Dicas de Boas Práticas

### SEO
- Título entre 50-60 caracteres
- Excerpt entre 120-160 caracteres
- Use palavras-chave em `keywords`
- Sempre preencha `alt` nas imagens

### Acessibilidade
- Texto alternativo descritivo em todas as imagens
- Use hierarquia correta de títulos (H2, H3, H4)
- Contraste adequado em imagens
- Legendas em vídeos quando possível

### Performance
- Otimize imagens (WebP, compressão)
- Thumbnail: máx 100KB
- Cover: máx 300KB
- Images: máx 200KB cada

### Conteúdo
- Parágrafos curtos (3-4 linhas)
- Use subtítulos para organizar
- Adicione imagens relevantes
- Cite fontes em `references`
- Vincule artigos relacionados

---

**Última atualização**: 4 de novembro de 2025  
**Versão**: 1.0

