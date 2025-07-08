#!/usr/bin/env python3
"""
Script Python para renderização de Markdown - Apple Newsroom
Versão: 2.0 com pypandoc e processament            # Twitter Cards (opcional - só será incluído se existir dados específicos do Twitter)
            # Não incluído por padrão - será adicionado apenas se especificado no .md ou dados customizadosçado de componentes
"""

import os
import sys
import yaml
import re
import json
import argparse
import webbrowser
from pathlib import Path
from datetime import datetime

try:
    import pypandoc
except ImportError:
    print("❌ ERRO: pypandoc não está instalado")
    print("Execute: pip install pypandoc")
    print("Ou execute: python config.py")
    sys.exit(1)

class Automacao:
    """
    Classe base para automação de tarefas com configurações padrão para renderização
    """

    def __init__(self):
        """Inicializa as configurações padrão"""
        self.config_padrao = self._criar_config_padrao()

    def _criar_config_padrao(self):
        """Cria estrutura de configuração padrão para artigos"""
        return {
            # Metadados básicos do artigo (serão sobrescritos pelos dados do .md)
            "meta_basico": {
                "title": None,  # Será extraído do .md
                "description": None,  # Será extraído do .md
                "canonical": None,  # Será extraído do .md
                "lang": "pt-BR",
                "locale": "pt-BR",
                "author": "Apple Newsroom",
                "site_name": "Apple Newsroom",
                "type": "article",
                "date": None,  # Será extraído do .md
                "category": "COMUNICADO DE IMPRENSA",
                "category_class": "category_release",
                "location": None  # Será extraído do .md
            },

            # Configurações HTML
            "html_config": {
                "xmlns": "http://www.w3.org/1999/xhtml",
                "xml_lang": "pt-BR",
                "lang": "pt-BR",
                "dir": "ltr",
                "prefix": "og: http://ogp.me/ns#",
                "classes": [
                    "globalheader-dark",
                    "js",
                    "no-touch",
                    "svg",
                    "progressive-image",
                    "windows",
                    "no-edge",
                    "no-safari",
                    "no-mobile-os",
                    "no-reduced-motion",
                    "progressive"
                ]
            },

            # Includes de componentes
            "includes": {
                "header_global": {
                    "file": "globalheader.html",
                    "position": "after_body_open",
                    "priority": 1
                },
                "footer_global": {
                    "file": "globalfooter.html",
                    "position": "before_body_close",
                    "priority": 1
                },
                "local_nav": {
                    "file": "localnav.html",
                    "position": "after_globalheader",
                    "priority": 2
                }
            },

            # Componentes globais
            "components": {
                "globalmessage": {
                    "enabled": True,
                    "lang": "pt-BR",
                    "dir": "ltr"
                },
                "globalnav": {
                    "enabled": True,
                    "analytics_region": "global nav",
                    "store_api": "/[storefront]/shop/bag/status"
                }
            },

            # Meta tags
            "meta": {
                "viewport": "width=device-width, initial-scale=1, viewport-fit=cover",
                "charset": "utf-8"
            },

            # Analytics
            "analytics": {
                "s_channel": "newsroom",
                "s_bucket_0": "applestoreww",
                "s_bucket_1": "applestoreww",
                "s_bucket_2": "applestoreww",
                "track": "Redação - Estatística"
            },

            # Open Graph (herda automaticamente title/description dos meta_basico)
            "og": {
                "type": "article",
                "site_name": "Redação - Estatística",
                "locale": "pt_BR",
                "image": "https://www.estatistica.pro/newsroom/${path/to/images.jpg}"
            },

            # Twitter Cards (opcional - só será incluído se existir dados específicos do Twitter)
            # Não incluído por padrão - será adicionado apenas se especificado no .md ou dados customizados

            # Recursos CSS
            "stylesheets": [
                "www.estatistica.pro/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3",
            ],

            # Scripts head
            "scripts": [
                "/newsroom/scripts/newsroom-head.built.js"
            ],

            # Scripts body
            "body_scripts": [
                "/newsroom/scripts/newsroom-body.built.js"
            ]
        }

    def criar_config_artigo(self, dados_customizados=None):
        """
        Cria configuração completa para um artigo específico
        
        Args:
            dados_customizados (dict): Dados específicos do artigo para sobrescrever padrões
            
        Returns:
            dict: Configuração completa do artigo
        """
        config = self.config_padrao.copy()

        if dados_customizados:
            # Merge recursivo dos dados customizados
            config = self._merge_dicts(config, dados_customizados)

        return config

    def _merge_dicts(self, dict1, dict2):
        """
        Faz merge recursivo de dicionários
        
        Args:
            dict1 (dict): Dicionário base
            dict2 (dict): Dicionário para merge
            
        Returns:
            dict: Dicionário resultante do merge
        """
        result = dict1.copy()

        for key, value in dict2.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_dicts(result[key], value)
            else:
                result[key] = value

        return result

    def gerar_frontmatter_yaml(self, config):
        """
        Gera o frontmatter YAML a partir da configuração
        
        Args:
            config (dict): Configuração do artigo
            
        Returns:
            str: String YAML formatada para frontmatter
        """
        # Aplica herança automática de metadados
        config = self._aplicar_heranca_metadados(config)

        # Flatten da configuração para YAML
        yaml_data = {}

        # Meta básico no nível raiz
        yaml_data.update(config.get('meta_basico', {}))

        # Outras seções mantêm sua estrutura (incluindo Twitter apenas se presente)
        for key in ['html_config', 'includes', 'components', 'meta', 'analytics', 'og', 'twitter', 'stylesheets', 'scripts', 'body_scripts']:
            if key in config and config[key] is not None:
                yaml_data[key] = config[key]

        # Adiciona featured_image se existir
        if 'featured_image' in config:
            yaml_data['featured_image'] = config['featured_image']

        return yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    def criar_featured_image_config(self, src, alt, caption=None, fullbleed=True, analytics_id=None):
        """
        Cria configuração para imagem destacada
        
        Args:
            src (str): URL da imagem
            alt (str): Texto alternativo
            caption (str): Legenda da imagem
            fullbleed (bool): Se a imagem deve ocupar toda largura
            analytics_id (str): ID para analytics
            
        Returns:
            dict: Configuração da imagem destacada
        """
        config = {
            "src": src,
            "alt": alt,
            "fullbleed": fullbleed
        }

        if caption:
            config["caption"] = caption

        if analytics_id:
            config["analytics_id"] = analytics_id

        # Gera srcset automaticamente se não fornecido
        if src and not config.get("srcset"):
            # Assume convenção de nomenclatura _2x para alta resolução
            srcset_url = src.replace(
                ".jpg", "_2x.jpg") if ".jpg" in src else f"{src}_2x"
            config["srcset"] = f"{srcset_url} 2x"

        return config

    def extrair_metadados_do_md(self, arquivo_md):
        """
        Extrai metadados do arquivo Markdown (frontmatter ou conteúdo)
        
        Args:
            arquivo_md (str): Caminho para o arquivo Markdown
            
        Returns:
            dict: Metadados extraídos do arquivo
        """
        if not os.path.exists(arquivo_md):
            print(f"⚠️ Arquivo não encontrado: {arquivo_md}")
            return {}

        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        metadados = {}

        # Primeiro tenta extrair do frontmatter YAML
        frontmatter_data = self._extrair_frontmatter_yaml(conteudo)
        if frontmatter_data:
            metadados.update(frontmatter_data)

        # Se não encontrou no frontmatter, extrai do conteúdo
        if not metadados.get('title'):
            metadados['title'] = self._extrair_titulo_do_conteudo(conteudo)

        if not metadados.get('date'):
            metadados['date'] = self._extrair_data_do_conteudo(conteudo)

        if not metadados.get('location'):
            metadados['location'] = self._extrair_localizacao_do_conteudo(
                conteudo)

        # Gera canonical se não existir
        if not metadados.get('canonical') and metadados.get('title'):
            metadados['canonical'] = self._gerar_canonical_slug(
                metadados['title'])

        return metadados

    def _extrair_frontmatter_yaml(self, conteudo):
        """
        Extrai dados do frontmatter YAML se existir
        
        Args:
            conteudo (str): Conteúdo do arquivo Markdown
            
        Returns:
            dict: Dados do frontmatter ou dict vazio
        """
        if conteudo.startswith('---'):
            partes = conteudo.split('---', 2)
            if len(partes) >= 3:
                try:
                    return yaml.safe_load(partes[1])
                except yaml.YAMLError as e:
                    print(f"⚠️ Erro ao parsear frontmatter YAML: {e}")
        return {}

    def _extrair_titulo_do_conteudo(self, conteudo):
        """
        Extrai o título do primeiro cabeçalho H1 do Markdown
        
        Args:
            conteudo (str): Conteúdo do arquivo Markdown
            
        Returns:
            str: Título extraído ou None
        """
        # Remove frontmatter para buscar no conteúdo
        if conteudo.startswith('---'):
            partes = conteudo.split('---', 2)
            if len(partes) >= 3:
                conteudo = partes[2]

        # Procura por cabeçalho H1
        match = re.search(r'^#\s+(.+)$', conteudo, re.MULTILINE)
        if match:
            return match.group(1).strip()

        return None

    def _extrair_data_do_conteudo(self, conteudo):
        """
        Extrai data do conteúdo usando padrões comuns
        
        Args:
            conteudo (str): Conteúdo do arquivo Markdown
            
        Returns:
            str: Data extraída ou data atual
        """
        # Padrões de data em português
        padroes_data = [
            r'(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})',  # "04 de julho de 2025"
            r'(\d{1,2}/\d{1,2}/\d{4})',             # "04/07/2025"
            r'(\d{4}-\d{2}-\d{2})',                 # "2025-07-04"
        ]

        for padrao in padroes_data:
            match = re.search(padrao, conteudo, re.IGNORECASE)
            if match:
                return match.group(1)

        # Se não encontrou, retorna data atual
        return datetime.now().strftime("%d de %B de %Y")

    def _extrair_localizacao_do_conteudo(self, conteudo):
        """
        Extrai localização do conteúdo usando padrões comuns
        
        Args:
            conteudo (str): Conteúdo do arquivo Markdown
            
        Returns:
            str: Localização extraída ou None
        """
        # Padrões de localização
        padroes_local = [
            r'([A-Z][A-Z\s]+,\s*[A-Z][A-Z\s]+)\s*[-–—]',  # "BRASILIA, BRASIL —"
            # "BRASILIA, BRASIL" no início
            r'^([A-Z][A-Z\s]+,\s*[A-Z][A-Z\s]+)',
        ]

        for padrao in padroes_local:
            match = re.search(padrao, conteudo, re.MULTILINE)
            if match:
                return match.group(1).strip()

        return None

    def _gerar_canonical_slug(self, titulo):
        """
        Gera um slug para URL canônica a partir do título
        
        Args:
            titulo (str): Título do artigo
            
        Returns:
            str: Slug gerado
        """
        if not titulo:
            return None

        # Remove caracteres especiais e converte para minúsculo
        slug = re.sub(r'[^\w\s-]', '', titulo.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-')

        return slug

    def _aplicar_heranca_metadados(self, config):
        """
        Aplica herança automática de metadados para OG e Twitter
        Os campos title, description e url são herdados automaticamente dos meta_basico
        Twitter é opcional - só será incluído se existir na configuração
        
        Args:
            config (dict): Configuração do artigo
            
        Returns:
            dict: Configuração com herança aplicada
        """
        meta_basico = config.get('meta_basico', {})
        
        # Aplica herança para Open Graph (sempre presente)
        if 'og' in config:
            if meta_basico.get('title'):
                config['og']['title'] = meta_basico['title']
            if meta_basico.get('description'):
                config['og']['description'] = meta_basico['description']
            if meta_basico.get('canonical'):
                config['og']['url'] = meta_basico['canonical']
        
        # Aplica herança para Twitter Cards (apenas se existir)
        if 'twitter' in config:
            if meta_basico.get('title'):
                config['twitter']['title'] = meta_basico['title']
            if meta_basico.get('description'):
                config['twitter']['description'] = meta_basico['description']
        
        return config

    def criar_twitter_config(self, site="@Apple", card="summary_large_image", image=None):
        """
        Cria configuração padrão para Twitter Cards
        
        Args:
            site (str): Handle do Twitter (@site)
            card (str): Tipo de card (summary_large_image, summary, etc.)
            image (str): URL da imagem para Twitter
            
        Returns:
            dict: Configuração do Twitter Cards
        """
        config = {
            "site": site,
            "card": card
        }
        
        if image:
            config["image"] = image
        else:
            config["image"] = "https://www.estatistica.pro/newsroom/images/default/tile/default.jpg.og.jpg"
        
        return config

    def verificar_se_deve_incluir_twitter(self, metadados_md, dados_customizados=None):
        """
        Verifica se deve incluir meta tags do Twitter baseado nos dados disponíveis
        
        Args:
            metadados_md (dict): Metadados extraídos do arquivo .md
            dados_customizados (dict): Dados customizados fornecidos
            
        Returns:
            bool: True se deve incluir Twitter, False caso contrário
        """
        # Verifica se existe configuração explícita do Twitter no frontmatter
        if metadados_md and isinstance(metadados_md.get('twitter'), dict):
            return True
        
        # Verifica se existe configuração do Twitter nos dados customizados
        if dados_customizados and isinstance(dados_customizados.get('twitter'), dict):
            return True
        
        # Verifica se existe algum campo específico do Twitter no frontmatter
        twitter_fields = ['twitter_site', 'twitter_card', 'twitter_image', 'twitter_creator']
        if metadados_md:
            for field in twitter_fields:
                if field in metadados_md and metadados_md[field] is not None:
                    return True
        
        return False

class Render:
    """
    Classe para renderização de arquivos Markdown com configurações avançadas
    """

    def __init__(self):
        """Inicializa o renderizador"""
        self.automacao = Automacao()

    def processar_artigo(self, arquivo_md, dados_artigo=None):
        """
        Processa um arquivo Markdown com configurações personalizadas
        
        Args:
            arquivo_md (str): Caminho para o arquivo Markdown
            dados_artigo (dict): Dados específicos do artigo (opcionais)
            
        Returns:
            str: HTML renderizado com frontmatter
        """
        # Extrai metadados do arquivo Markdown
        metadados_md = self.automacao.extrair_metadados_do_md(arquivo_md)

        # Cria dados combinados: metadados do .md + dados customizados
        dados_combinados = {}

        # Primeiro aplica metadados extraídos do .md
        if metadados_md:
            dados_combinados["meta_basico"] = metadados_md

            # Atualiza analytics com título se disponível
            if metadados_md.get('title'):
                dados_combinados["analytics"] = {
                    "track": f"Newsroom - {metadados_md['title']}"
                }

        # Em seguida, aplica dados customizados (se fornecidos)
        if dados_artigo:
            dados_combinados = self.automacao._merge_dicts(
                dados_combinados, dados_artigo)

        # Verifica se deve incluir Twitter Cards DEPOIS do merge
        if self.automacao.verificar_se_deve_incluir_twitter(metadados_md, dados_artigo):
            # Se não há configuração específica, cria uma padrão
            if 'twitter' not in dados_combinados:
                dados_combinados["twitter"] = self.automacao.criar_twitter_config()

        # Cria configuração personalizada
        config = self.automacao.criar_config_artigo(dados_combinados)

        # Gera frontmatter (com herança automática aplicada)
        frontmatter = self.automacao.gerar_frontmatter_yaml(config)

        # Lê conteúdo do arquivo Markdown
        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo_md = f.read()

        # Remove frontmatter existente se houver
        conteudo_md = self._remover_frontmatter_existente(conteudo_md)

        # Combina novo frontmatter com conteúdo
        markdown_completo = f"---\n{frontmatter}---\n\n{conteudo_md}"

        return markdown_completo

    def _remover_frontmatter_existente(self, conteudo):
        """
        Remove frontmatter existente do conteúdo Markdown
        
        Args:
            conteudo (str): Conteúdo Markdown
            
        Returns:
            str: Conteúdo sem frontmatter
        """
        # Remove frontmatter YAML (entre --- no início)
        if conteudo.startswith('---'):
            partes = conteudo.split('---', 2)
            if len(partes) >= 3:
                return partes[2].strip()

        return conteudo

    def exemplo_uso(self):
        """
        Exemplo de como usar as configurações
        """
        # Dados específicos para um artigo
        dados_artigo = {
            "meta_basico": {
                "title": "Apple Music celebra 10 anos de inovação",
                "description": "A plataforma de streaming revolucionou a indústria musical",
                "canonical": "apple-music-celebrates-10-years",
                "date": "04 de julho de 2025",
                "category": "COMUNICADO DE IMPRENSA"
            },
            "featured_image": self.automacao.criar_featured_image_config(
                src="https://www.estatistica.pro/newsroom/images/2025/06/apple-music-celebrates-10-years/article/Apple-Music-10th-anniversary-Los-Angeles-studio_big.jpg.large.jpg",
                alt="O novo espaço de estúdio em Los Angeles",
                caption="A Apple apresenta um novo espaço de estúdio de última geração em Los Angeles dedicado ao conteúdo orientado por artistas, inovação em áudio e conexão mais profunda com os fãs.",
                analytics_id="Apple-Music-10th-anniversary-Los-Angeles-studio_big"
            ),
            "analytics": {
                "track": "Newsroom - Apple Music celebra 10 anos"
            }
        }

        # Processa artigo
        try:
            resultado = self.processar_artigo("artigo.md", dados_artigo)
            print("✅ Artigo processado com sucesso!")
            return resultado
        except Exception as e:
            print(f"❌ Erro ao processar artigo: {e}")
            return None


def main():
    """
    Função principal para demonstrar o uso do sistema de configurações
    """
    print("🚀 Sistema de Renderização - Apple Newsroom v2.0")
    print("=" * 50)

    # Inicializa renderizador
    render = Render()

    # Exemplo 1: Configuração básica (sem metadados do .md)
    print("\n📝 Exemplo 1: Configuração Básica")
    config_basica = render.automacao.criar_config_artigo()
    frontmatter_basico = render.automacao.gerar_frontmatter_yaml(config_basica)
    print("Frontmatter básico gerado:")
    print(frontmatter_basico[:200] +
          "..." if len(frontmatter_basico) > 200 else frontmatter_basico)

    # Exemplo 2: Simulando extração de metadados de um arquivo .md
    print("\n🔍 Exemplo 2: Extração de Metadados")
    print("Simulando um arquivo artigo.md com o seguinte conteúdo:")
    print("```")
    print("---")
    print("title: Apple Music celebra 10 anos")
    print("description: Uma década de inovação musical")
    print("location: CUPERTINO, CALIFORNIA")
    print("---")
    print("")
    print("# Apple Music celebra 10 anos")
    print("")
    print("CUPERTINO, CALIFORNIA — 04 de julho de 2025 — A Apple...")
    print("```")

    # Simula metadados extraídos
    metadados_simulados = {
        "title": "Apple Music celebra 10 anos",
        "description": "Uma década de inovação musical",
        "location": "CUPERTINO, CALIFORNIA",
        "date": "04 de julho de 2025",
        "canonical": "apple-music-celebra-10-anos"
    }

    dados_com_metadados = {
        "meta_basico": metadados_simulados,
        "og": {
            "title": metadados_simulados["title"],
            "description": metadados_simulados["description"],
            "url": metadados_simulados["canonical"]
        },
        "twitter": {
            "title": metadados_simulados["title"],
            "description": metadados_simulados["description"]
        }
    }

    config_com_metadados = render.automacao.criar_config_artigo(
        dados_com_metadados)
    print(f"✅ Metadados extraídos: {len(metadados_simulados)} campos")

    # Exemplo 3: Configuração personalizada adicional
    print("\n🎯 Exemplo 3: Configuração com Featured Image")
    dados_personalizados = {
        "featured_image": render.automacao.criar_featured_image_config(
            src="https://www.estatistica.pro/newsroom/images/2025/07/apple-music-10-anos/article/hero-image.jpg",
            alt="Apple Music celebrando 10 anos",
            caption="A Apple Music revolucionou a forma como consumimos música"
        )
    }

    # Combina metadados + configuração personalizada
    config_completa = render.automacao.criar_config_artigo(
        render.automacao._merge_dicts(
            dados_com_metadados, dados_personalizados)
    )

    print(f"✅ Configuração completa criada com {len(config_completa)} seções")

    # Exemplo 4: Geração de frontmatter completo
    print("\n📋 Exemplo 4: Frontmatter Completo")
    frontmatter_completo = render.automacao.gerar_frontmatter_yaml(
        config_completa)
    linhas = frontmatter_completo.split('\n')
    print(f"Frontmatter gerado com {len(linhas)} linhas")
    print("\nPrimeiras 10 linhas:")
    for i, linha in enumerate(linhas[:10], 1):
        print(f"{i:2d}: {linha}")

    print("\n✨ Sistema pronto para uso!")
    print("💡 Use render.processar_artigo('arquivo.md') para processar arquivos")
    print("💡 Os metadados (título, data, local) serão extraídos automaticamente do .md")
    print("💡 Você pode adicionar configurações extras como featured_image via parâmetros")


if __name__ == "__main__":
    main()
