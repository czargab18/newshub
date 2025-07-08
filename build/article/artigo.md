---
title: "Meu Titulo exemplo"
description: "descrição curta para seo do meu artigo"
# canonical: "https://www.estatistica.pro/newsroom/2025/06/estatistica-music-celebrates-10-years/"
# canonical: "${domin}/${diretorio}/${ano}/${mes}/${titulo}/"
canonical: "texto-para-link-canonico"
lang: "pt-BR"
locale: "pt-BR"
author: "Estatística Newsroom"
site_name: "Estatística Newsroom"
type: "article"
date: "04 de julho de 2025"
category: "COMUNICADO DE IMPRENSA"
category_class: "category_release"
location: "BRASILIA, BRASIL"

html_config:
  xmlns: "http://www.w3.org/1999/xhtml"
  xml_lang: "pt-BR"
  lang: "pt-BR"
  dir: "ltr"
  prefix: "og: http://ogp.me/ns#"
  classes: 
    - "globalheader-dark"
    - "js"
    - "no-touch" 
    - "svg"
    - "progressive-image"
    - "windows"
    - "no-edge"
    - "no-safari"
    - "no-mobile-os"
    - "no-reduced-motion"
    - "progressive"

includes:
  header_global: 
    file: "globalheader.html"
    position: "after_body_open"
    priority: 1
  footer_global: 
    file: "globalfooter.html"
    position: "before_body_close"
    priority: 1
  local_nav:
    file: "localnav.html" 
    position: "after_globalheader"
    priority: 2

components:
  globalmessage:
    enabled: true
    lang: "pt-BR"
    dir: "ltr"
  globalnav:
    enabled: true
    analytics_region: "global nav"
    store_api: "/[storefront]/shop/bag/status"

featured_image:
  src: "/image.png"
  srcset: "/image.png 2x"
  alt: "O novo espaço de estúdio em Los Angeles"
  caption: "descrição da imagem - visivel par ao usuario"
  fullbleed: true
  analytics_id: "texto-da-imagem"
  download_url: ""
  download_title: "texto-da-imagem"

meta:
  viewport: "width=device-width, initial-scale=1, viewport-fit=cover"
  charset: "utf-8"

analytics:
  s_channel: "newsroom"
  s_bucket_0: "estatisticastoreww"
  s_bucket_1: "estatisticastoreww"
  s_bucket_2: "estatisticastoreww"
  track: "Redação - Estatística"

og:
  title: "Meu Titulo exemplo"
  description: "descrição curta para seo do meu artigo"
  type: "article"
  site_name: "Estatística Newsroom"
  locale: "pt_BR"
  url: "texto-para-link-canonico"
  image: "/imgage.png"

twitter:
  title: "Meu Titulo exemplo"
  description: "descrição curta para seo do meu artigo"
  site: "@Estatística"
  card: "summary_large_image"
  image: "/imgage.png"

stylesheets:
  - "/www.estatistica.pro/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3"
  - "/newsroom/styles/articlev2.built.css"

scripts:
  - "/newsroom/scripts/newsroom-head.built.js"

body_scripts:
  - "/newsroom/scripts/newsroom-body.built.js"
---

# Lorem Ipsum - Conteúdo de Exemplo

## Introdução ao Lorem Ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit. **Sed do eiusmod tempor** incididunt ut labore et dolore magna aliqua. *Ut enim ad minim veniam*, quis nostrud exercitation ullamco laboris.

> "Lorem ipsum é simplesmente um texto fictício da indústria de impressão e composição tipográfica. Lorem ipsum tem sido o texto fictício padrão da indústria desde os anos 1500."

### Subseção com Lista Ordenada

1. **Primeiro item** - Lorem ipsum dolor sit amet
2. **Segundo item** - Consectetur adipiscing elit
3. **Terceiro item** - Sed do eiusmod tempor incididunt
   - Sub-item A
   - Sub-item B
   - Sub-item C

#### Lista Não Ordenada com Links

- [Lorem ipsum](https://lorem-ipsum.com) - Link para gerador de texto
- [Markdown Guide](https://markdownguide.org) - Guia completo de Markdown
- **Texto em negrito** com `código inline`
- *Texto em itálico* e ~~texto riscado~~

##### Tabela de Exemplo

| Nome         | Idade | Profissão     | Status     |
| ------------ | ----- | ------------- | ---------- |
| João Silva   | 32    | Desenvolvedor | ✅ Ativo    |
| Maria Santos | 28    | Designer      | ⚠️ Pendente |
| Pedro Costa  | 35    | Gerente       | ❌ Inativo  |

###### Código em Bloco

```python
def lorem_ipsum():
    """
    Função que retorna texto Lorem Ipsum
    """
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    return texto.upper()

# Exemplo de uso
resultado = lorem_ipsum()
print(resultado)
```

```javascript
// Exemplo em JavaScript
const loremIpsum = () => {
    const texto = "Lorem ipsum dolor sit amet";
    return texto.split(' ').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
};

console.log(loremIpsum());
```

## Citações e Blocos Especiais

> ### Citação Importante
> 
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
> 
> > **Citação aninhada**: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Imagens e Links

![Imagem de exemplo](image.png "Descrição da imagem de exemplo"){#exemplo-imagem .image-center .component-image data-analytics="exemplo-image"}

Para mais informações, visite [nosso site](https://exemplo.com "Site oficial") ou entre em contato através do email: exemplo@email.com

### Lista de Tarefas

- [x] Tarefa concluída
- [x] Outra tarefa finalizada
- [ ] Tarefa pendente
- [ ] Tarefa em andamento
- [ ] Tarefa futura

### Texto com Formatação Especial

Este parágrafo contém **texto em negrito**, *texto em itálico*, ***texto em negrito e itálico***, `código inline`, e ~~texto riscado~~.

Também podemos usar caracteres especiais como:
- Marca registrada: ®
- Copyright: ©
- Trademark: ™
- Setas: → ← ↑ ↓
- Símbolos: ★ ☆ ♠ ♣ ♥ ♦

### Linha Horizontal

---

### Notas de Rodapé

Este texto tem uma nota de rodapé[^1] e outra aqui[^nota-longa].

[^1]: Esta é uma nota de rodapé simples.
[^nota-longa]: Esta é uma nota de rodapé mais longa com várias linhas.
    Ela pode incluir múltiplos parágrafos e formatação.

### Definições

Termo 1
: Definição do primeiro termo lorem ipsum dolor sit amet.

Termo 2
: Definição do segundo termo consectetur adipiscing elit.
: Segunda definição para o mesmo termo.

### Quebra de Linha Manual

Primeira linha com quebra manual  
Segunda linha após quebra
Terceira linha normal

### Escape de Caracteres

Para mostrar caracteres especiais literalmente:
\*asterisco\* \#hashtag\* \[colchetes\] \`backticks\`

## Conclusão

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Recursos Adicionais

Para aprender mais sobre Markdown:

1. [Sintaxe Básica](https://markdownguide.org/basic-syntax)
2. [Sintaxe Estendida](https://markdownguide.org/extended-syntax)
3. [Cheat Sheet](https://markdownguide.org/cheat-sheet)