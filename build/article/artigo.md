---
# ===================================================
# 📝 FRONTMATTER MÍNIMO - APENAS O ESSENCIAL
# ===================================================
# 
# ✅ VOCÊ SÓ PRECISA ESCREVER ISSO:
# • title, description, date, location
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
# • Meta tags (viewport, charset, etc.)
# • HTML config (classes, xmlns, etc.)
# • Configurações de layout
#
# ===================================================

title: "Meu Título Exemplo"
description: "Descrição curta para SEO do meu artigo"
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