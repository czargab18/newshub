#!/usr/bin/env python3
"""
Teste Completo do Sistema de Biblioteca de Elementos
Demonstra todas as funcionalidades do sistema integrado
"""

import sys
import os
from pathlib import Path

# Adiciona o diretório atual ao path
sys.path.append(str(Path(__file__).parent))

def testar_linha_comando():
    """Testa os comandos da linha de comando"""
    
    print("🧪 TESTE: Comandos da Linha de Comando")
    print("=" * 60)
    
    # Diretório base
    base_dir = Path(__file__).parent
    script_render = base_dir / "render.py"
    
    if not script_render.exists():
        print("❌ Script render.py não encontrado!")
        return False
    
    # Comandos para testar
    comandos = [
        {
            "cmd": f"python {script_render} --list-elements",
            "desc": "Listar todos os elementos"
        },
        {
            "cmd": f"python {script_render} --list-elements social",
            "desc": "Listar elementos da categoria 'social'"
        },
        {
            "cmd": f"python {script_render} --search twitter",
            "desc": "Buscar elementos com 'twitter'"
        }
    ]
    
    print("📋 Comandos disponíveis para teste:")
    for i, comando in enumerate(comandos, 1):
        print(f"\n{i}. {comando['desc']}:")
        print(f"   {comando['cmd']}")
    
    print("\n✅ Para testar, execute os comandos acima no terminal.")
    return True


def criar_arquivo_teste():
    """Cria arquivo de teste para demonstração"""
    
    print("\n📝 Criando arquivo de teste...")
    
    conteudo_teste = """---
title: "Teste da Biblioteca de Elementos"
description: "Demonstração do sistema de elementos prontos"
date: "2024-01-15"
---

# Teste da Biblioteca de Elementos

Este é um arquivo de teste para demonstrar como aplicar elementos da biblioteca.

## Funcionalidades

- ✅ Aplicação automática de elementos
- ✅ Merge inteligente de configurações
- ✅ Preservação de dados existentes
- ✅ Validação de elementos

## Próximos Passos

Use este arquivo para testar:

```bash
python render.py teste_biblioteca.md --elements social/twitter_completo,analytics/newsroom_padrao
```

## Resultado Esperado

O sistema deve:
1. Carregar o frontmatter existente
2. Aplicar os elementos especificados
3. Fazer merge das configurações
4. Renderizar o HTML final
"""
    
    arquivo_teste = Path(__file__).parent.parent / "article" / "teste_biblioteca.md"
    arquivo_teste.parent.mkdir(exist_ok=True)
    
    with open(arquivo_teste, 'w', encoding='utf-8') as f:
        f.write(conteudo_teste)
    
    print(f"✅ Arquivo criado: {arquivo_teste}")
    return arquivo_teste


def testar_integracao():
    """Testa a integração completa do sistema"""
    
    print("\n🔧 TESTE: Integração Completa")
    print("=" * 60)
    
    try:
        # Importa módulos
        from biblioteca_elementos import BibliotecaElementos
        from render import NewsroomRenderer
        
        print("✅ Módulos importados com sucesso")
        
        # Inicializa sistema
        biblioteca = BibliotecaElementos()
        renderer = NewsroomRenderer()
        
        print("✅ Sistema inicializado")
        
        # Testa elementos básicos
        elementos_social = biblioteca.listar_elementos("social")
        print(f"✅ Encontrados {len(elementos_social)} elementos na categoria 'social'")
        
        # Testa busca
        resultados = biblioteca.buscar_elementos("twitter")
        count = sum(len(elems) for elems in resultados.values())
        print(f"✅ Encontrados {count} elementos com 'twitter'")
        
        # Testa aplicação
        frontmatter_base = {"meta_basico": {"title": "Teste"}}
        resultado = biblioteca.aplicar_elemento(frontmatter_base, "social", "twitter_completo")
        print(f"✅ Elemento aplicado. Resultado tem {len(resultado)} seções")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na integração: {e}")
        return False


def mostrar_exemplos():
    """Mostra exemplos práticos de uso"""
    
    print("\n📚 EXEMPLOS PRÁTICOS")
    print("=" * 60)
    
    arquivo_teste = criar_arquivo_teste()
    
    exemplos = [
        {
            "nome": "Artigo com Twitter e Analytics",
            "cmd": f"python render.py {arquivo_teste} --elements social/twitter_completo,analytics/newsroom_padrao"
        },
        {
            "nome": "Lançamento de Produto Completo",
            "cmd": f"python render.py {arquivo_teste} --elements navegacao/header_completo,analytics/produto_lancamento,social/twitter_completo,social/og_produto"
        },
        {
            "nome": "Comunicado Simples",
            "cmd": f"python render.py {arquivo_teste} --elements categorias/comunicado_imprensa,social/og_artigo"
        },
        {
            "nome": "Evento/Keynote",
            "cmd": f"python render.py {arquivo_teste} --elements categorias/evento,analytics/newsroom_padrao,social/twitter_completo"
        }
    ]
    
    print("🎯 Exemplos de uso:")
    for i, exemplo in enumerate(exemplos, 1):
        print(f"\n{i}. {exemplo['nome']}:")
        print(f"   {exemplo['cmd']}")
    
    print("\n💡 Dicas:")
    print("   • Use --verbose para ver detalhes do processamento")
    print("   • Use --open para abrir o resultado no navegador")
    print("   • Combine múltiplos elementos separando por vírgula")


def verificar_dependencias():
    """Verifica se todas as dependências estão disponíveis"""
    
    print("🔍 VERIFICAÇÃO: Dependências")
    print("=" * 60)
    
    dependencias = {
        "PyYAML": "yaml",
        "pypandoc": "pypandoc",
        "pathlib": "pathlib"
    }
    
    for nome, modulo in dependencias.items():
        try:
            __import__(modulo)
            print(f"✅ {nome}")
        except ImportError:
            print(f"❌ {nome} - FALTANDO!")
    
    # Verifica arquivos
    arquivos = [
        "render.py",
        "biblioteca_elementos.py",
        "biblioteca_config.yaml"
    ]
    
    base_dir = Path(__file__).parent
    print(f"\n📁 Arquivos em {base_dir}:")
    for arquivo in arquivos:
        caminho = base_dir / arquivo
        if caminho.exists():
            print(f"✅ {arquivo}")
        else:
            print(f"❌ {arquivo} - FALTANDO!")


def main():
    """Função principal do teste"""
    
    print("🚀 SISTEMA DE BIBLIOTECA DE ELEMENTOS - TESTE COMPLETO")
    print("=" * 80)
    
    # Verificações
    verificar_dependencias()
    
    # Testes
    if testar_integracao():
        print("\n✅ Integração funcionando corretamente!")
    else:
        print("\n❌ Problemas na integração detectados!")
        return
    
    # Demonstrações
    testar_linha_comando()
    mostrar_exemplos()
    
    print("\n" + "=" * 80)
    print("🎉 TESTE CONCLUÍDO!")
    print("\n🏃‍♂️ Próximos passos:")
    print("1. Execute os comandos de linha mostrados acima")
    print("2. Teste os exemplos práticos")
    print("3. Personalize a biblioteca editando biblioteca_config.yaml")
    print("4. Crie seus próprios elementos e presets")
    print("=" * 80)


if __name__ == "__main__":
    main()
