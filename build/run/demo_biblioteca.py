#!/usr/bin/env python3
"""
Demonstração do Sistema de Biblioteca de Elementos
Mostra como puxar/adicionar elementos prontos para artigos
"""

import sys
import yaml
from pathlib import Path

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(str(Path(__file__).parent))

from biblioteca_elementos import BibliotecaElementos
from render import NewsroomRenderer


def demo_completa():
    """Demonstração completa do sistema de biblioteca de elementos"""
    
    print("=" * 80)
    print("🚀 DEMONSTRAÇÃO: Sistema de Biblioteca de Elementos")
    print("=" * 80)
    print()
    
    # 1. Inicializar sistema
    print("📚 1. Inicializando biblioteca de elementos...")
    biblioteca = BibliotecaElementos()
    renderer = NewsroomRenderer()
    
    # 2. Listar categorias disponíveis
    print("\n📁 2. Categorias disponíveis:")
    for categoria in biblioteca.elementos.keys():
        count = len(biblioteca.elementos[categoria])
        print(f"   • {categoria} ({count} elementos)")
    
    # 3. Mostrar elementos de uma categoria específica
    print("\n🔍 3. Elementos da categoria 'social':")
    elementos_social = biblioteca.listar_elementos("social")
    for nome, dados in elementos_social.items():
        descricao = dados.get("description", "Sem descrição")
        print(f"   • {nome}: {descricao}")
    
    # 4. Buscar elementos por termo
    print("\n🔎 4. Buscando elementos com 'twitter':")
    resultados = biblioteca.buscar_elementos("twitter")
    for categoria, elementos in resultados.items():
        print(f"   📁 {categoria}:")
        for nome in elementos.keys():
            print(f"     • {nome}")
    
    # 5. Demonstrar aplicação de elementos
    print("\n🛠️  5. Aplicando elementos a um frontmatter base:")
    
    # Frontmatter base simples
    frontmatter_base = {
        "meta_basico": {
            "title": "Novo Produto da Apple",
            "description": "Anúncio oficial do mais novo produto revolucionário"
        }
    }
    
    print("Frontmatter original:")
    print(yaml.dump(frontmatter_base, allow_unicode=True, indent=2))
    
    # Aplicar elemento Twitter
    print("Aplicando 'social/twitter_completo'...")
    frontmatter_com_twitter = biblioteca.aplicar_elemento(
        frontmatter_base.copy(), 
        "social", 
        "twitter_completo"
    )
    
    print("Resultado com Twitter:")
    print(yaml.dump(frontmatter_com_twitter, allow_unicode=True, indent=2, sort_keys=False))
    
    # 6. Criar preset personalizado
    print("\n🎯 6. Criando preset personalizado 'lancamento_completo':")
    elementos_preset = [
        ("navegacao", "header_completo"),
        ("analytics", "produto_lancamento"),
        ("social", "twitter_completo"),
        ("social", "og_produto"),
        ("layout", "artigo_padrao")
    ]
    
    preset_lancamento = biblioteca.criar_preset(
        "lancamento_completo",
        elementos_preset,
        "Preset completo para lançamentos de produtos"
    )
    
    print("Preset criado:")
    print(yaml.dump(preset_lancamento, allow_unicode=True, indent=2, sort_keys=False))
    
    # 7. Aplicar múltiplos elementos via renderer
    print("\n🚀 7. Aplicando múltiplos elementos via renderer:")
    elementos_lista = [
        "social/twitter_completo",
        "analytics/produto_lancamento",
        "navegacao/header_completo"
    ]
    
    frontmatter_final = renderer.aplicar_elementos_biblioteca(
        frontmatter_base.copy(), 
        elementos_lista
    )
    
    print("Resultado final com múltiplos elementos:")
    print(yaml.dump(frontmatter_final, allow_unicode=True, indent=2, sort_keys=False))
    
    # 8. Demonstrar templates por categoria
    print("\n📋 8. Templates prontos por categoria:")
    categorias_template = biblioteca.listar_elementos("categorias")
    for nome, template in categorias_template.items():
        descricao = template.get("description", "Sem descrição")
        print(f"   • {nome}: {descricao}")
    
    # 9. Aplicar template de categoria
    print("\n📄 9. Aplicando template 'categorias/lancamento_produto':")
    frontmatter_com_template = biblioteca.aplicar_elemento(
        frontmatter_base.copy(),
        "categorias",
        "lancamento_produto"
    )
    
    print("Resultado com template de lançamento:")
    print(yaml.dump(frontmatter_com_template, allow_unicode=True, indent=2, sort_keys=False))
    
    print("\n" + "=" * 80)
    print("✅ Demonstração concluída!")
    print("💡 Use os comandos abaixo para trabalhar com a biblioteca:")
    print("   python render.py --list-elements")
    print("   python render.py --list-elements social")
    print("   python render.py --search twitter")
    print("   python render.py artigo.md --elements social/twitter_completo,analytics/newsroom_padrao")
    print("=" * 80)


def criar_exemplos_markdown():
    """Cria exemplos de arquivos Markdown para demonstração"""
    
    print("\n📝 Criando arquivos de exemplo...")
    
    # Exemplo 1: Artigo básico
    exemplo_basico = """---
title: "Exemplo Básico"
description: "Um artigo simples para demonstração"
---

# Exemplo Básico

Este é um artigo básico que será enriquecido com elementos da biblioteca.

## Conteúdo

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
    
    # Exemplo 2: Artigo sem frontmatter
    exemplo_sem_frontmatter = """# Novo Produto Revolucionário

**Cupertino, Califórnia** — A Apple anunciou hoje seu mais novo produto revolucionário.

## Características Principais

- Design inovador
- Tecnologia avançada
- Experiência única

## Disponibilidade

O produto estará disponível a partir de amanhã.
"""
    
    # Salvar exemplos
    base_dir = Path(__file__).parent.parent / "article"
    base_dir.mkdir(exist_ok=True)
    
    (base_dir / "exemplo_basico.md").write_text(exemplo_basico, encoding='utf-8')
    (base_dir / "exemplo_sem_frontmatter.md").write_text(exemplo_sem_frontmatter, encoding='utf-8')
    
    print("✅ Exemplos criados:")
    print(f"   • {base_dir}/exemplo_basico.md")
    print(f"   • {base_dir}/exemplo_sem_frontmatter.md")
    
    return base_dir


def demo_linha_comando():
    """Demonstra uso via linha de comando"""
    
    print("\n🖥️  Demonstração de uso via linha de comando:")
    print()
    
    # Criar exemplos se não existirem
    base_dir = criar_exemplos_markdown()
    
    print("Comandos para testar:")
    print()
    print("1. Listar todos os elementos:")
    print("   python render.py --list-elements")
    print()
    print("2. Listar elementos de uma categoria:")
    print("   python render.py --list-elements social")
    print()
    print("3. Buscar elementos:")
    print("   python render.py --search twitter")
    print()
    print("4. Renderizar com elementos aplicados:")
    print(f"   python render.py {base_dir}/exemplo_basico.md --elements social/twitter_completo,analytics/newsroom_padrao")
    print()
    print("5. Renderizar artigo sem frontmatter com elementos:")
    print(f"   python render.py {base_dir}/exemplo_sem_frontmatter.md --elements categorias/comunicado_imprensa")
    print()
    print("6. Múltiplos elementos para lançamento de produto:")
    print(f"   python render.py {base_dir}/exemplo_basico.md --elements navegacao/header_completo,analytics/produto_lancamento,social/twitter_completo,social/og_produto")


if __name__ == "__main__":
    # Executa demonstração completa
    demo_completa()
    
    # Mostra comandos de linha de comando
    demo_linha_comando()
