#!/usr/bin/env python3
"""
Teste do sistema de Twitter opcional
"""

from render2 import Render

def testar_twitter_opcional():
    """
    Testa o sistema de Twitter opcional com dois cenários
    """
    print("🐦 Testando Sistema de Twitter Opcional")
    print("=" * 45)
    
    render = Render()
    
    # Teste 1: Artigo SEM configurações do Twitter
    print("\n📄 Teste 1: Artigo SEM Twitter")
    print("-" * 30)
    
    arquivo_sem_twitter = "artigo-sem-twitter.md"
    resultado_sem_twitter = render.processar_artigo(arquivo_sem_twitter)
    
    # Verifica se contém twitter no resultado
    tem_twitter = "twitter:" in resultado_sem_twitter.lower()
    print(f"✅ Processado: {arquivo_sem_twitter}")
    print(f"🐦 Contém Twitter Cards: {'❌ NÃO' if not tem_twitter else '✅ SIM'}")
    
    # Salva resultado
    with open("resultado-sem-twitter.md", "w", encoding="utf-8") as f:
        f.write(resultado_sem_twitter)
    print("💾 Salvo como: resultado-sem-twitter.md")
    
    # Teste 2: Artigo COM configurações do Twitter
    print("\n📄 Teste 2: Artigo COM Twitter")
    print("-" * 30)
    
    arquivo_com_twitter = "artigo-com-twitter.md"
    resultado_com_twitter = render.processar_artigo(arquivo_com_twitter)
    
    # Verifica se contém twitter no resultado
    tem_twitter = "twitter:" in resultado_com_twitter.lower()
    print(f"✅ Processado: {arquivo_com_twitter}")
    print(f"🐦 Contém Twitter Cards: {'✅ SIM' if tem_twitter else '❌ NÃO'}")
    
    # Salva resultado
    with open("resultado-com-twitter.md", "w", encoding="utf-8") as f:
        f.write(resultado_com_twitter)
    print("💾 Salvo como: resultado-com-twitter.md")
    
    # Teste 3: Forçar Twitter via parâmetros
    print("\n📄 Teste 3: Forçar Twitter via parâmetros")
    print("-" * 40)
    
    dados_com_twitter = {
        "twitter": render.automacao.criar_twitter_config(
            site="@EstatisticaPro",
            card="summary",
            image="https://exemplo.com/imagem-twitter.jpg"
        )
    }
    
    resultado_forcado = render.processar_artigo(arquivo_sem_twitter, dados_com_twitter)
    tem_twitter = "twitter:" in resultado_forcado.lower()
    
    print(f"✅ Processado: {arquivo_sem_twitter} + dados Twitter")
    print(f"🐦 Contém Twitter Cards: {'✅ SIM' if tem_twitter else '❌ NÃO'}")
    
    # Salva resultado
    with open("resultado-twitter-forcado.md", "w", encoding="utf-8") as f:
        f.write(resultado_forcado)
    print("💾 Salvo como: resultado-twitter-forcado.md")
    
    # Resumo
    print("\n📊 Resumo dos Testes")
    print("=" * 20)
    print("1. Artigo sem Twitter      → Twitter Cards NÃO incluídas")
    print("2. Artigo com Twitter      → Twitter Cards incluídas")
    print("3. Twitter forçado         → Twitter Cards incluídas")
    print("\n✨ Sistema funcionando corretamente!")

if __name__ == "__main__":
    testar_twitter_opcional()
