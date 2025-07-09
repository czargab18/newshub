---
# ===================================================
# 📝 FRONTMATTER MÍNIMO - APENAS O ESSENCIAL
# ===================================================
# 
# ✅ VOCÊ SÓ PRECISA ESCREVER ESSAS META TAGS:
# • title (meta tag para SEO/navegador)
# • description (meta tag para SEO/redes sociais)
# • date, location (metadados do artigo)
# • O resto é ADICIONADO AUTOMATICAMENTE!
#
# 🚀 COMO USAR O SISTEMA AUTOMÁTICO:
#
# 1. COMUNICADO DE IMPRENSA (automático):
#    python render.py artigo.md --elements preset:comunicado_simples
#
# 2. LANÇAMENTO DE PRODUTO (automático):
#    python render.py artigo.md --elements preset:lancamento_produto
#
# 3. EVENTO/KEYNOTE (automático):
#    python render.py artigo.md --elements preset:keynote_evento
#
# 4. ARTIGO COMPLETO (automático):
#    python render.py artigo.md --elements preset:artigo_completo
#
# 💡 O QUE É ADICIONADO AUTOMATICAMENTE:
# • Analytics (tracking, buckets, etc.)
# • Twitter Cards (title, description, site, card, etc.)
# • Open Graph (og:title, og:description, og:image, etc.)
# • Headers e navegação (includes, components)
# • Stylesheets e scripts
# • Meta tags técnicas (viewport, charset, etc.)
# • HTML config (classes, xmlns, etc.)
# • Configurações de layout
#
# ===================================================

# 🏷️ META TAGS (para SEO, navegador, redes sociais):
title: "Meu Título Exemplo"                    # <title> tag + og:title + twitter:title
description: "Descrição curta para SEO do meu artigo"  # <meta description> + og:description + twitter:description

# 📅 METADADOS DO ARTIGO:
date: "04 de julho de 2025"
location: "BRASÍLIA, BRASIL"

# 🔧 OPCIONAL: Personalizações específicas
# canonical: "url-personalizada"  # Se não especificar, é gerado automaticamente
# category: "TIPO PERSONALIZADO"  # Se não especificar, usa padrão do preset
# featured_image:                  # Se você tem imagem específica
#   src: "/minha-imagem.png"
#   alt: "Descrição da imagem"

# ===================================================
# 📋 EXEMPLOS DE USO:
#
# Para comunicado de imprensa:
# python render.py artigo.md --elements preset:comunicado_simples
#
# Para lançamento de produto:
# python render.py artigo.md --elements preset:lancamento_produto
#
# Para evento/keynote:
# python render.py artigo.md --elements preset:keynote_evento
#
# Para artigo completo:
# python render.py artigo.md --elements preset:artigo_completo
#
# Combinando preset + elementos extras:
# python render.py artigo.md --elements preset:artigo_completo,social/twitter_video
#
# ===================================================
---

# 📝 SEU CONTEÚDO VAI AQUI (BODY DO HTML)

Este é o **conteúdo real** do artigo que aparece na página. O título acima (`title: "Meu Título Exemplo"`) é uma **meta tag** para SEO, não o título visual da página.

## Este é o H1 visual que os usuários veem

Lorem ipsum dolor sit amet, consectetur adipiscing elit. **Sed do eiusmod tempor** incididunt ut labore et dolore magna aliqua.

### Subseção com Lista

1. **Primeiro item** - Lorem ipsum dolor sit amet
2. **Segundo item** - Consectetur adipiscing elit
3. **Terceiro item** - Sed do eiusmod tempor incididunt

### Imagens e Links

![Imagem de exemplo](image.png "Descrição da imagem")

Para mais informações, visite [nosso site](https://exemplo.com) ou entre em contato através do email: exemplo@email.com

## 💡 Entenda a Diferença:

- **`title:`** no frontmatter = Meta tag `<title>` (aparece na aba do navegador, Google, Twitter, etc.)
- **`# Título`** no markdown = Conteúdo H1 visual (aparece na página para o usuário)

## Conclusão

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Este é o conteúdo que os usuários realmente leem na página.