# 📝 COMPARAÇÃO: Antes vs Depois

## ❌ ANTES: Você tinha que escrever TUDO manualmente (106 linhas!)

```yaml
---
title: "Meu Titulo exemplo"
description: "descrição curta para seo do meu artigo"
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
```

## ✅ AGORA: Você só escreve o ESSENCIAL (4 linhas!)

```yaml
---
title: "Meu Título Exemplo"
description: "Descrição curta para SEO do meu artigo"
date: "04 de julho de 2025"
location: "BRASÍLIA, BRASIL"
---
```

**E executa:**
```bash
python render.py artigo.md --elements preset:artigo_completo
```

## 🚀 RESULTADO AUTOMÁTICO

O sistema adiciona automaticamente:

### 📊 **Analytics** (adicionado automaticamente)
```yaml
analytics:
  s_channel: "newsroom"
  s_bucket_0: "applestoreww"
  s_bucket_1: "applestoreww"
  s_bucket_2: "applestoreww"
  track: "Redação - Estatística"
```

### 📱 **Twitter Cards** (adicionado automaticamente)
```yaml
twitter:
  card: "summary_large_image"
  site: "@estatisticabr"
  creator: "@estatisticabr"
  domain: "estatistica.pro"
  title: "Meu Título Exemplo"        # ← Herdado do seu title
  description: "Descrição curta..."   # ← Herdado do seu description
```

### 🌐 **Open Graph** (adicionado automaticamente)
```yaml
og:
  type: "article"
  site_name: "Redação - Estatística"
  locale: "pt_BR"
  image: "https://www.estatistica.pro/newsroom/images/default/tile/default.jpg.og.jpg"
  title: "Meu Título Exemplo"        # ← Herdado do seu title
  description: "Descrição curta..."   # ← Herdado do seu description
  url: "meu-título-exemplo"          # ← Gerado automaticamente
```

### 🧭 **Navegação e Headers** (adicionado automaticamente)
```yaml
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
```

### 🎨 **Layout e Recursos** (adicionado automaticamente)
```yaml
stylesheets:
  - "www.estatistica.pro/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3"

scripts:
  - "/newsroom/scripts/newsroom-head.built.js"

body_scripts:
  - "/newsroom/scripts/newsroom-body.built.js"
```

### ⚙️ **Configurações Meta** (adicionado automaticamente)
```yaml
meta:
  viewport: "width=device-width, initial-scale=1, viewport-fit=cover"
  charset: "utf-8"

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
    # ... e mais classes automáticas
```

## 📈 **ECONOMIA DE TRABALHO:**

- **Antes**: 106 linhas manuais
- **Agora**: 4 linhas manuais
- **Economia**: **96% menos trabalho!**

## 🎯 **PRESETS DISPONÍVEIS:**

```bash
# Artigo completo de newsroom
python render.py artigo.md --elements preset:artigo_completo

# Comunicado de imprensa
python render.py artigo.md --elements preset:comunicado_simples

# Lançamento de produto
python render.py artigo.md --elements preset:lancamento_produto

# Evento/Keynote
python render.py artigo.md --elements preset:keynote_evento

# Tutorial/Guia
python render.py artigo.md --elements preset:tutorial_guia
```

## 💡 **PERSONALIZAÇÃO OPCIONAL:**

Se você quiser sobrescrever algo específico, ainda pode:

```yaml
---
title: "Meu Título"
description: "Minha descrição"
date: "04 de julho de 2025"
location: "BRASÍLIA, BRASIL"

# Personalização opcional:
canonical: "url-customizada"
featured_image:
  src: "/minha-imagem-especial.png"
  alt: "Minha descrição especial"
---
```

**Agora você foca no CONTEÚDO, não na configuração!** 🎉
