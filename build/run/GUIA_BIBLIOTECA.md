# 📚 Sistema de Biblioteca de Elementos - Guia de Uso

## 🚀 Visão Geral

O sistema de biblioteca de elementos permite puxar/adicionar elementos prontos (componentes, configurações, analytics, etc.) aos seus artigos Markdown de forma automática e reutilizável.

## 🎯 Funcionalidades Principais

### 1. **Elementos Pré-definidos**
- 🧭 **Navegação**: Headers, menus, componentes de navegação
- 📊 **Analytics**: Configurações de tracking para diferentes tipos de conteúdo
- 📱 **Social**: Twitter Cards, Open Graph, configurações de mídia social
- 🎨 **Layout**: Templates de layout para diferentes tipos de página
- 📋 **Categorias**: Templates completos por tipo de conteúdo
- 📝 **Snippets**: Trechos de conteúdo reutilizáveis

### 2. **Comandos de Linha**
```bash
# Listar todos os elementos disponíveis
python render.py --list-elements

# Listar elementos de uma categoria específica
python render.py --list-elements social

# Buscar elementos por termo
python render.py --search twitter

# Aplicar elementos durante a renderização
python render.py artigo.md --elements social/twitter_completo,analytics/newsroom_padrao
```

## 📖 Exemplos Práticos

### 🆕 Artigo Básico com Twitter e Analytics
```bash
python render.py meu-artigo.md --elements social/twitter_completo,analytics/newsroom_padrao
```

### 🚀 Lançamento de Produto Completo
```bash
python render.py lancamento.md --elements navegacao/header_completo,analytics/produto_lancamento,social/twitter_completo,social/og_produto
```

### 📢 Comunicado de Imprensa
```bash
python render.py comunicado.md --elements categorias/comunicado_imprensa,social/og_artigo
```

### 🎤 Evento/Keynote
```bash
python render.py evento.md --elements categorias/evento,analytics/newsroom_padrao,social/twitter_completo
```

## 🎨 Elementos Disponíveis

### 📁 **navegacao**
- `header_completo` - Cabeçalho completo com navegação global e local
- `header_simples` - Cabeçalho simplificado sem navegação local

### 📁 **analytics**
- `newsroom_padrao` - Analytics padrão para artigos de newsroom
- `produto_lancamento` - Analytics para lançamentos de produtos
- `comunicado_imprensa` - Analytics para comunicados de imprensa

### 📁 **social**
- `twitter_completo` - Twitter Cards completo com imagem grande
- `twitter_simples` - Twitter Cards simples
- `og_artigo` - Open Graph otimizado para artigos
- `og_produto` - Open Graph otimizado para páginas de produto

### 📁 **layout**
- `artigo_padrao` - Layout padrão para artigos de newsroom
- `landing_page` - Layout para páginas de destino/landing

### 📁 **categorias**
- `comunicado_imprensa` - Template completo para comunicados de imprensa
- `lancamento_produto` - Template para lançamentos de produtos
- `evento` - Template para eventos e keynotes

### 📁 **snippets**
- `disclaimer_padrao` - Disclaimer padrão para artigos
- `cta_newsletter` - Call-to-action para newsletter
- `rodape_social` - Links de redes sociais para rodapé

## 💡 Como Funciona

### 1. **Aplicação Automática**
O sistema automaticamente:
- Detecta o frontmatter existente
- Aplica os elementos especificados
- Faz merge inteligente das configurações
- Preserva dados já existentes

### 2. **Merge Inteligente**
```yaml
# Frontmatter original
title: "Meu Artigo"
description: "Descrição do artigo"

# Após aplicar social/twitter_completo
title: "Meu Artigo"           # ← Preservado
description: "Descrição do artigo"  # ← Preservado
twitter:                      # ← Adicionado
  card: "summary_large_image"
  site: "@estatisticabr"
  creator: "@estatisticabr"
```

### 3. **Presets Prontos**
Combine múltiplos elementos para cenários comuns:

```bash
# Artigo completo de newsroom
--elements navegacao/header_completo,analytics/newsroom_padrao,social/twitter_completo,social/og_artigo

# Lançamento de produto
--elements navegacao/header_completo,analytics/produto_lancamento,social/og_produto,categorias/lancamento_produto
```

## 🛠️ Personalização

### Criar Elementos Personalizados
Edite o arquivo `biblioteca_config.yaml` para adicionar seus próprios elementos:

```yaml
elementos_personalizados:
  social:
    meu_twitter:
      description: "Meu Twitter Cards personalizado"
      twitter:
        card: "summary"
        site: "@meusite"
```

### Criar Presets
Combine elementos em presets reutilizáveis:

```python
from biblioteca_elementos import BibliotecaElementos

biblioteca = BibliotecaElementos()
preset = biblioteca.criar_preset(
    "meu_preset",
    [("social", "twitter_completo"), ("analytics", "newsroom_padrao")],
    "Meu preset personalizado"
)
```

## 🔧 Integração com Workflow Existente

### Uso com Automações Existentes
O sistema trabalha **junto** com as automações do `render.py`:

1. Elementos são aplicados **primeiro**
2. Automações são executadas **depois**
3. Dados existentes são sempre preservados

### Compatibilidade
- ✅ Compatible com frontmatter existente
- ✅ Preserva configurações manuais
- ✅ Funciona com automações existentes
- ✅ Não quebra arquivos existentes

## 📋 Workflow Recomendado

### Para Novos Artigos
```bash
# 1. Criar artigo com frontmatter mínimo
echo "---
title: \"Meu Novo Artigo\"
description: \"Descrição do artigo\"
---

# Conteúdo do artigo..." > novo-artigo.md

# 2. Aplicar elementos e renderizar
python render.py novo-artigo.md --elements social/twitter_completo,analytics/newsroom_padrao --open
```

### Para Artigos Existentes
```bash
# Adicionar elementos sem perder configurações existentes
python render.py artigo-existente.md --elements social/og_artigo --verbose
```

## 🚨 Dicas Importantes

### ✅ Boas Práticas
- Use `--verbose` para ver o que está sendo aplicado
- Combine elementos relacionados (ex: `social/twitter_completo` + `social/og_artigo`)
- Teste com `--list-elements` antes de aplicar
- Use presets para cenários recorrentes

### ⚠️ Cuidados
- Elementos **não sobrescrevem** dados existentes (apenas adicionam)
- Use nomes corretos: `categoria/nome` (ex: `social/twitter_completo`)
- Verifique dependências com `python render.py --help`

## 🆘 Solução de Problemas

### Elemento não encontrado
```bash
# Verificar se o elemento existe
python render.py --list-elements categoria_desejada
python render.py --search nome_elemento
```

### Erro ao aplicar elementos
```bash
# Usar modo verboso para ver detalhes
python render.py arquivo.md --elements categoria/nome --verbose
```

### Biblioteca não carrega
```bash
# Verificar se os arquivos estão no lugar correto
python -c "from biblioteca_elementos import BibliotecaElementos; print('OK')"
```

## 🎉 Próximos Passos

1. **Teste os comandos básicos** listados acima
2. **Experimente com seus artigos** usando `--elements`
3. **Personalize a biblioteca** editando `biblioteca_config.yaml`
4. **Crie seus próprios presets** para workflows específicos
5. **Integre ao seu processo** de criação de conteúdo

---

**💬 Dúvidas?** Execute `python render.py --help` para ver todas as opções disponíveis!
