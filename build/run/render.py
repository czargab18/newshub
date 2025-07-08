#!/usr/bin/env python3
"""
Script Python para renderização de Markdown - Apple Newsroom
Versão: 2.0 com pypandoc e processamento avançado de componentes
"""

import os
import sys
import yaml
import re
import json
import argparse
import webbrowser
from pathlib import Path
from typing import Optional
from datetime import datetime

try:
    import pypandoc
except ImportError:
    print("❌ ERRO: pypandoc não está instalado")
    print("Execute: pip install pypandoc")
    print("Ou execute: python config.py")
    sys.exit(1)

# Importa a biblioteca de elementos
try:
    from biblioteca_elementos import BibliotecaElementos
except ImportError:
    print("⚠️  Biblioteca de elementos não encontrada. Algumas funcionalidades podem estar limitadas.")
    BibliotecaElementos = None


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
                "image": "https://www.estatistica.pro/newsroom/images/default/tile/default.jpg.og.jpg"
            },

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

    def verificar_se_deve_incluir_twitter(self, metadados_md):
        """
        Verifica se deve incluir meta tags do Twitter baseado nos dados disponíveis
        
        Args:
            metadados_md (dict): Metadados extraídos do arquivo .md
            
        Returns:
            bool: True se deve incluir Twitter, False caso contrário
        """
        # Verifica se existe configuração explícita do Twitter no frontmatter
        if metadados_md and isinstance(metadados_md.get('twitter'), dict):
            return True

        # Verifica se existe algum campo específico do Twitter no frontmatter
        twitter_fields = ['twitter_site', 'twitter_card',
                          'twitter_image', 'twitter_creator']
        if metadados_md:
            for field in twitter_fields:
                if field in metadados_md and metadados_md[field] is not None:
                    return True

        return False

    def criar_config_atualizada(self, metadados_md):
        """
        Cria configuração atualizada baseada nos metadados do arquivo .md
        
        Args:
            metadados_md (dict): Metadados extraídos do arquivo .md
            
        Returns:
            dict: Configuração atualizada
        """
        config = self.config_padrao.copy()

        # Aplica metadados extraídos
        if metadados_md:
            # Atualiza metadados básicos
            for campo in ['title', 'description', 'canonical', 'date', 'location', 'category', 'author']:
                if campo in metadados_md and metadados_md[campo] is not None:
                    config['meta_basico'][campo] = metadados_md[campo]

            # Aplica herança automática para Open Graph
            if metadados_md.get('title'):
                config['og']['title'] = metadados_md['title']
            if metadados_md.get('description'):
                config['og']['description'] = metadados_md['description']
            if metadados_md.get('canonical'):
                config['og']['url'] = metadados_md['canonical']

            # Inclui Twitter se existir
            if self.verificar_se_deve_incluir_twitter(metadados_md):
                config['twitter'] = metadados_md.get('twitter', {
                    "site": "@Apple",
                    "card": "summary_large_image",
                    "image": "https://www.estatistica.pro/newsroom/images/default/tile/default.jpg.og.jpg"
                })

                # Aplica herança para Twitter
                if metadados_md.get('title'):
                    config['twitter']['title'] = metadados_md['title']
                if metadados_md.get('description'):
                    config['twitter']['description'] = metadados_md['description']

            # Atualiza analytics com título
            if metadados_md.get('title'):
                config['analytics']['track'] = f"Newsroom - {metadados_md['title']}"

            # Preserva configurações específicas do frontmatter
            for campo in ['html_config', 'includes', 'components', 'featured_image', 'meta', 'stylesheets', 'scripts', 'body_scripts']:
                if campo in metadados_md:
                    config[campo] = metadados_md[campo]

        return config

    def gerar_frontmatter_atualizado(self, metadados_originais, input_file):
        """
        Gera frontmatter atualizado com automações aplicadas
        
        Args:
            metadados_originais (dict): Metadados originais do arquivo
            input_file (str): Caminho do arquivo de entrada
            
        Returns:
            dict: Metadados atualizados para renderização
        """
        # Extrai metadados do arquivo
        metadados_extraidos = self.extrair_metadados_do_md(input_file)

        # Cria configuração atualizada
        config_atualizada = self.criar_config_atualizada(metadados_extraidos)

        # Flatten da configuração para o formato esperado pelo render
        resultado = {}

        # Meta básico no nível raiz
        resultado.update(config_atualizada.get('meta_basico', {}))

        # Outras seções
        for key in ['html_config', 'includes', 'components', 'meta', 'analytics', 'og', 'twitter', 'featured_image', 'stylesheets', 'scripts', 'body_scripts']:
            if key in config_atualizada and config_atualizada[key] is not None:
                resultado[key] = config_atualizada[key]

        return resultado

class NewsroomRenderer:
    def __init__(self, base_dir=None):
        """Inicializa o renderizador"""
        # Inicializa automação
        self.automacao = Automacao()

        # Inicializa biblioteca de elementos se disponível
        self.biblioteca = None
        if BibliotecaElementos:
            try:
                self.biblioteca = BibliotecaElementos()
                self.log("✓ Biblioteca de elementos carregada", "SUCCESS")
            except Exception as e:
                self.log(
                    f"⚠️  Erro ao carregar biblioteca de elementos: {e}", "WARNING")

        if base_dir is None:
            # Padrão: usar diretório run como base
            script_dir = Path(__file__).parent
            self.template_file = script_dir / ".." / "modelos" / "template.html"
            self.components_dir = script_dir / ".." / "components"
            self.output_dir = script_dir / ".." / "article" / "output"
        else:
            # Quando base_dir é especificado, usar como output_dir diretamente
            self.output_dir = Path(base_dir)
            # Manter referências relativas ao script para templates e components
            script_dir = Path(__file__).parent
            self.template_file = script_dir / ".." / "modelos" / "template.html"
            self.components_dir = script_dir / ".." / "components"
        
        # Criar diretório de saída
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def log(self, message, level="INFO"):
        """Sistema de log com timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        color_codes = {
            "INFO": "\033[96m",     # Cyan
            "SUCCESS": "\033[92m",  # Green
            "WARNING": "\033[93m",  # Yellow
            "ERROR": "\033[91m",    # Red
            "RESET": "\033[0m"      # Reset
        }
        
        color = color_codes.get(level, color_codes["RESET"])
        reset = color_codes["RESET"]
        print(f"{color}[{timestamp}] {level}: {message}{reset}")
    
    def check_dependencies(self):
        """Verifica se todas as dependências estão disponíveis"""
        self.log("Verificando dependências...")
        
        # Verificar pypandoc
        try:
            version = pypandoc.get_pandoc_version()
            self.log(f"✓ Pandoc via pypandoc: {version}", "SUCCESS")
        except Exception as e:
            self.log(f"✗ Erro no pypandoc: {e}", "ERROR")
            return False
        
        # Verificar template
        if not self.template_file.exists():
            self.log(f"✗ Template não encontrado: {self.template_file}", "ERROR")
            self.log("Certifique-se de que template.html está na pasta modelos/", "ERROR")
            return False
        else:
            self.log(f"✓ Template encontrado: {self.template_file}", "SUCCESS")
        
        return True
    
    def extract_frontmatter(self, content, input_file=None):
        """Extrai frontmatter YAML do conteúdo markdown e aplica automações"""
        try:
            # Regex para frontmatter
            pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
            match = re.match(pattern, content, re.DOTALL)
            
            if match:
                yaml_content = match.group(1)
                markdown_body = match.group(2)
                
                # Parse YAML
                try:
                    metadata = yaml.safe_load(yaml_content)
                    if metadata is None:
                        metadata = {}

                    # Aplica automações se input_file foi fornecido
                    if input_file:
                        self.log("🤖 Aplicando automações...", "INFO")
                        metadata_atualizado = self.automacao.gerar_frontmatter_atualizado(
                            metadata, input_file)

                        # Log das automações aplicadas
                        metadados_extraidos = self.automacao.extrair_metadados_do_md(
                            input_file)
                        if metadados_extraidos.get('title') and not metadata.get('title'):
                            self.log(
                                f"✓ Título extraído: {metadados_extraidos['title']}", "SUCCESS")
                        if metadados_extraidos.get('date') and not metadata.get('date'):
                            self.log(
                                f"✓ Data extraída: {metadados_extraidos['date']}", "SUCCESS")
                        if metadados_extraidos.get('location') and not metadata.get('location'):
                            self.log(
                                f"✓ Localização extraída: {metadados_extraidos['location']}", "SUCCESS")
                        if metadados_extraidos.get('canonical') and not metadata.get('canonical'):
                            self.log(
                                f"✓ URL canônica gerada: {metadados_extraidos['canonical']}", "SUCCESS")

                        # Verifica Twitter
                        tem_twitter = self.automacao.verificar_se_deve_incluir_twitter(
                            metadados_extraidos)
                        if tem_twitter:
                            self.log(
                                "✓ Twitter Cards incluídas (detectadas no arquivo)", "SUCCESS")
                        else:
                            self.log(
                                "ℹ Twitter Cards omitidas (não detectadas)", "INFO")

                        return metadata_atualizado, markdown_body
                    else:
                        return metadata, markdown_body

                except yaml.YAMLError as e:
                    self.log(f"Erro ao processar YAML: {e}", "WARNING")
                    return {}, content
            else:
                # Sem frontmatter - aplica automações se input_file fornecido
                if input_file:
                    self.log(
                        "⚠ Nenhum frontmatter encontrado - aplicando automações", "WARNING")
                    metadata_gerado = self.automacao.gerar_frontmatter_atualizado(
                        {}, input_file)

                    metadados_extraidos = self.automacao.extrair_metadados_do_md(
                        input_file)
                    if metadados_extraidos.get('title'):
                        self.log(
                            f"✓ Título extraído do conteúdo: {metadados_extraidos['title']}", "SUCCESS")
                    if metadados_extraidos.get('date'):
                        self.log(
                            f"✓ Data extraída: {metadados_extraidos['date']}", "SUCCESS")

                    return metadata_gerado, content
                else:
                    self.log("Nenhum frontmatter YAML encontrado", "WARNING")
                    return {}, content
                
        except Exception as e:
            self.log(f"Erro ao extrair frontmatter: {e}", "ERROR")
            return {}, content
    
    def load_component(self, component_name):
        """Carrega um componente HTML"""
        try:
            component_path = self.components_dir / f"{component_name}.html"
            if component_path.exists():
                with open(component_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.log(f"✓ Componente carregado: {component_name}")
                return content
            else:
                self.log(f"⚠ Componente não encontrado: {component_name}", "WARNING")
                return f"<!-- Componente {component_name} não encontrado -->"
        except Exception as e:
            self.log(f"Erro ao carregar componente {component_name}: {e}", "ERROR")
            return f"<!-- Erro ao carregar {component_name} -->"
    
    def process_includes(self, html_content, metadata):
        """Processa includes/componentes no HTML"""
        try:
            includes = metadata.get('includes', {})
            
            if not includes:
                self.log("Nenhum include definido no frontmatter")
                return html_content
            
            self.log(f"Processando {len(includes)} includes...")
            
            # Processar includes simples (true/false)
            for include_name, include_value in includes.items():
                if include_value is True:
                    component_html = self.load_component(include_name)
                    
                    # Mapear posições de inserção
                    replacements = {
                        'header_global': (
                            r'(<div id="globalheader">)(.*?)(</div>)',
                            r'\1' + component_html + r'\3'
                        ),
                        'footer_global': (
                            r'(<footer id="globalfooter"[^>]*>)(.*?)(</footer>)',
                            r'\1' + component_html + r'\3'
                        ),
                        'local_nav': (
                            r'(<nav class="localnav"[^>]*>)(.*?)(</nav>)',
                            r'\1' + component_html + r'\3'
                        ),
                        'article_header': (
                            r'(<div class="article-header-extended">)(.*?)(</div>)',
                            r'\1' + component_html + r'\3'
                        )
                    }
                    
                    if include_name in replacements:
                        pattern, replacement = replacements[include_name]
                        html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
                        self.log(f"✓ Include processado: {include_name}")
                    else:
                        self.log(f"⚠ Posição de include desconhecida: {include_name}", "WARNING")
            
            return html_content
            
        except Exception as e:
            self.log(f"Erro ao processar includes: {e}", "ERROR")
            return html_content
    
    def process_images(self, html_content, input_path, output_file):
        """Processa imagens no HTML e ajusta caminhos"""
        try:
            import shutil
            
            # Diretório de origem das imagens (mesmo diretório do markdown)
            source_dir = input_path.parent
            
            # Diretório de destino das imagens
            output_dir = output_file.parent
            src_dir = output_dir / "src"
            src_dir.mkdir(exist_ok=True)
            
            # Encontrar todas as imagens no HTML
            import re
            img_pattern = r'<img[^>]+src="([^"]+)"[^>]*>'
            img_matches = re.findall(img_pattern, html_content)
            
            if not img_matches:
                self.log("Nenhuma imagem encontrada no HTML")
                return html_content
            
            self.log(f"Processando {len(img_matches)} imagens...")
            
            for img_src in img_matches:
                # Ignorar URLs absolutas
                if img_src.startswith(('http://', 'https://', '//')):
                    continue
                
                # Arquivo de origem
                source_file = source_dir / img_src
                
                if source_file.exists():
                    # Arquivo de destino
                    dest_file = src_dir / source_file.name
                    
                    # Copiar arquivo
                    shutil.copy2(source_file, dest_file)
                    self.log(f"✓ Imagem copiada: {source_file.name} → src/{source_file.name}")
                    
                    # Atualizar caminho no HTML
                    old_src = f'src="{img_src}"'
                    new_src = f'src="src/{source_file.name}"'
                    html_content = html_content.replace(old_src, new_src)
                    
                else:
                    self.log(f"⚠ Imagem não encontrada: {source_file}", "WARNING")
            
            return html_content
            
        except Exception as e:
            self.log(f"Erro ao processar imagens: {e}", "ERROR")
            return html_content
    
    def render(self, input_file, output_file=None, verbose=False):
        """Renderiza arquivo markdown para HTML"""
        try:
            input_path = Path(input_file)
            
            if not input_path.exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {input_file}")
            
            # Determinar arquivo de saída
            if output_file is None:
                # Verificar se o arquivo de entrada é artigo.md e definir como index.html
                if input_path.stem == "artigo":
                    filename = "index"
                else:
                    filename = input_path.stem

                # Verificar se existe pasta output local junto com o arquivo de entrada
                local_output_dir = input_path.parent / "output"
                if local_output_dir.exists():
                    output_file = local_output_dir / (filename + ".html")
                    self.log(
                        f"Usando diretório de output local: {local_output_dir}")
                else:
                    output_file = self.output_dir / (filename + ".html")
            else:
                # Se output_file foi especificado, criar dentro do output_dir
                output_file = self.output_dir / Path(output_file).name
            
            self.log("=" * 60, "INFO")
            self.log("RENDERIZAÇÃO MARKDOWN - APPLE NEWSROOM (Python)", "INFO")
            self.log("=" * 60, "INFO")
            self.log(f"Entrada: {input_path}", "INFO")
            self.log(f"Saída: {output_file}", "INFO")
            self.log(f"Template: {self.template_file}", "INFO")
            self.log("=" * 60, "INFO")
            
            # Ler arquivo markdown
            with open(input_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            self.log("Arquivo markdown carregado")
            
            # Extrair frontmatter com automações
            metadata, markdown_body = self.extract_frontmatter(
                markdown_content, input_path)
            
            if metadata:
                self.log(f"Frontmatter processado: {len(metadata)} campos")
                if verbose:
                    # Mostra apenas campos principais para não poluir o log
                    campos_principais = {k: v for k, v in metadata.items(
                    ) if k in ['title', 'description', 'date', 'location', 'canonical']}
                    self.log(
                        f"Metadados principais: {json.dumps(campos_principais, indent=2, ensure_ascii=False)}")
            
            # Preparar variáveis para pypandoc
            extra_args = [
                '--standalone',
                f'--template={self.template_file}',
                '--from=markdown+yaml_metadata_block',
                '--to=html5',
                '--section-divs',
                '--wrap=none'
            ]
            
            # Adicionar metadados como variáveis
            for key, value in metadata.items():
                if key != 'includes':  # Includes são processados separadamente
                    if isinstance(value, (str, int, float, bool)):
                        extra_args.extend(['-V', f'{key}:{value}'])
                    elif isinstance(value, list):
                        # Converter listas para string
                        extra_args.extend(['-V', f'{key}:{",".join(map(str, value))}'])
            
            if verbose:
                self.log(f"Argumentos pandoc: {' '.join(extra_args)}")
            
            # Executar pypandoc
            self.log("Executando pypandoc...")
            
            # Recriar markdown com frontmatter para pypandoc
            full_markdown = f"---\n{yaml.dump(metadata, allow_unicode=True)}---\n{markdown_body}" if metadata else markdown_body
            
            html_output = pypandoc.convert_text(
                full_markdown,
                'html5',
                format='markdown+yaml_metadata_block',
                extra_args=extra_args
            )
            
            self.log("HTML básico gerado pelo pypandoc")
            
            # Processar includes
            if metadata:
                html_output = self.process_includes(html_output, metadata)
            
            # Processar imagens
            html_output = self.process_images(html_output, input_path, output_file)
            
            # Salvar arquivo final
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_output)
            
            # Estatísticas
            input_size = input_path.stat().st_size
            output_size = output_file.stat().st_size
            
            self.log("=" * 60, "SUCCESS")
            self.log("SUCESSO: Arquivo HTML gerado!", "SUCCESS")
            self.log("=" * 60, "SUCCESS")
            self.log(f"Arquivo: {output_file}", "SUCCESS")
            self.log(f"Tamanho: Input {input_size} bytes → Output {output_size} bytes", "SUCCESS")
            
            return True, str(output_file)
            
        except Exception as e:
            self.log(f"Erro durante renderização: {e}", "ERROR")
            return False, str(e)
    
    def batch_render(self, input_dir, pattern="*.md", verbose=False):
        """Renderiza múltiplos arquivos"""
        try:
            input_path = Path(input_dir)
            if not input_path.exists():
                raise FileNotFoundError(f"Diretório não encontrado: {input_dir}")
            
            markdown_files = list(input_path.glob(pattern))
            
            if not markdown_files:
                self.log(f"Nenhum arquivo {pattern} encontrado em {input_dir}", "WARNING")
                return []
            
            self.log(f"Renderizando {len(markdown_files)} arquivos...")
            
            results = []
            for i, md_file in enumerate(markdown_files, 1):
                self.log(f"Processando arquivo {i}/{len(markdown_files)}: {md_file.name}")
                success, output = self.render(md_file, verbose=verbose)
                results.append({
                    'input': str(md_file),
                    'output': output,
                    'success': success
                })
            
            # Resumo
            success_count = sum(1 for r in results if r['success'])
            self.log(f"Processamento em lote concluído: {success_count}/{len(results)} sucessos")
            
            return results
            
        except Exception as e:
            self.log(f"Erro no processamento em lote: {e}", "ERROR")
            return []

    def aplicar_elementos_biblioteca(self, frontmatter: dict, elementos_desejados: list) -> dict:
        """
        Aplica elementos da biblioteca ao frontmatter
        
        Args:
            frontmatter: Frontmatter atual
            elementos_desejados: Lista de elementos no formato ['categoria/nome', ...]
            
        Returns:
            Frontmatter atualizado com elementos aplicados
        """
        if not self.biblioteca:
            self.log("⚠️  Biblioteca de elementos não disponível", "WARNING")
            return frontmatter

        resultado = frontmatter.copy()

        for elemento_path in elementos_desejados:
            try:
                if '/' not in elemento_path:
                    self.log(
                        f"⚠️  Formato inválido para elemento: {elemento_path}. Use 'categoria/nome'", "WARNING")
                    continue

                categoria, nome = elemento_path.split('/', 1)

                self.log(f"📦 Aplicando elemento: {categoria}/{nome}")
                resultado = self.biblioteca.aplicar_elemento(
                    resultado, categoria, nome)

            except Exception as e:
                self.log(
                    f"❌ Erro ao aplicar elemento {elemento_path}: {e}", "ERROR")

        return resultado

    def listar_elementos_disponiveis(self, categoria: Optional[str] = None) -> None:
        """
        Lista elementos disponíveis na biblioteca
        
        Args:
            categoria: Categoria específica (opcional)
        """
        if not self.biblioteca:
            self.log("⚠️  Biblioteca de elementos não disponível", "WARNING")
            return

        elementos = self.biblioteca.listar_elementos(categoria)

        if categoria:
            self.log(f"📚 Elementos da categoria '{categoria}':")
            for nome, dados in elementos.items():
                descricao = dados.get('description', 'Sem descrição')
                self.log(f"  • {nome}: {descricao}")
        else:
            self.log("📚 Categorias e elementos disponíveis:")
            for cat, elems in elementos.items():
                self.log(f"  📁 {cat}:")
                for nome, dados in elems.items():
                    descricao = dados.get('description', 'Sem descrição')
                    self.log(f"    • {nome}: {descricao}")

    def buscar_elementos(self, termo: str) -> None:
        """
        Busca elementos na biblioteca por termo
        
        Args:
            termo: Termo de busca
        """
        if not self.biblioteca:
            self.log("⚠️  Biblioteca de elementos não disponível", "WARNING")
            return

        resultados = self.biblioteca.buscar_elementos(termo)

        if resultados:
            self.log(f"🔍 Elementos encontrados para '{termo}':")
            for categoria, elementos in resultados.items():
                self.log(f"  📁 {categoria}:")
                for nome, dados in elementos.items():
                    descricao = dados.get('description', 'Sem descrição')
                    self.log(f"    • {nome}: {descricao}")
        else:
            self.log(f"❌ Nenhum elemento encontrado para '{termo}'")

    def criar_preset_personalizado(self, nome: str, elementos: list, descricao: str = "") -> dict:
        """
        Cria um preset personalizado combinando elementos
        
        Args:
            nome: Nome do preset
            elementos: Lista de elementos no formato ['categoria/nome', ...]
            descricao: Descrição do preset
            
        Returns:
            Configuração do preset criado
        """
        if not self.biblioteca:
            self.log("⚠️  Biblioteca de elementos não disponível", "WARNING")
            return {}

        # Converte elementos para o formato esperado
        elementos_tuplas = []
        for elemento_path in elementos:
            if '/' in elemento_path:
                categoria, nome_elem = elemento_path.split('/', 1)
                elementos_tuplas.append((categoria, nome_elem))
            else:
                self.log(
                    f"⚠️  Formato inválido: {elemento_path}. Use 'categoria/nome'", "WARNING")

        if elementos_tuplas:
            preset = self.biblioteca.criar_preset(
                nome, elementos_tuplas, descricao)
            self.log(
                f"✅ Preset '{nome}' criado com {len(elementos_tuplas)} elementos")
            return preset
        else:
            self.log("❌ Nenhum elemento válido fornecido para o preset", "ERROR")
            return {}

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(
        description='Renderizador Apple Newsroom - Versão Python',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  python render.py artigo.md
  python render.py artigo.md -o meu_artigo.html
  python render.py . --batch
  python render.py artigo.md --open --verbose
  python render.py --list-elements social
  python render.py --search twitter
  python render.py artigo.md --elements social/twitter_completo,analytics/newsroom_padrao
        '''
    )
    
    parser.add_argument('input', nargs='?',
                        help='Arquivo markdown ou diretório para processar')
    parser.add_argument('-o', '--output', help='Arquivo de saída (opcional)')
    parser.add_argument('-b', '--batch', action='store_true', help='Modo lote para processar diretório')
    parser.add_argument('-v', '--verbose', action='store_true', help='Saída detalhada')
    parser.add_argument('--open', action='store_true', help='Abrir resultado no navegador')
    parser.add_argument('--base-dir', help='Diretório base do projeto')
    
    # Opções da biblioteca de elementos
    parser.add_argument('--list-elements', metavar='CATEGORIA', nargs='?', const='',
                        help='Listar elementos disponíveis (opcionalmente de uma categoria específica)')
    parser.add_argument('--search', metavar='TERMO',
                        help='Buscar elementos por termo')
    parser.add_argument('--elements', metavar='LISTA',
                        help='Lista de elementos para aplicar (formato: categoria/nome,categoria/nome,...)')

    args = parser.parse_args()
    
    # Inicializar renderizador
    renderer = NewsroomRenderer(args.base_dir)
    
    # Comandos da biblioteca de elementos
    if args.list_elements is not None:
        categoria = args.list_elements if args.list_elements else None
        renderer.listar_elementos_disponiveis(categoria)
        return

    if args.search:
        renderer.buscar_elementos(args.search)
        return

    # Verificar se input é necessário
    if not args.input:
        parser.error(
            "Arquivo/diretório de entrada é obrigatório para renderização")

    # Verificar dependências
    if not renderer.check_dependencies():
        sys.exit(1)
    
    if args.batch:
        # Modo lote
        results = renderer.batch_render(args.input, verbose=args.verbose)
        
        # Mostrar resultados
        for result in results:
            status = "✓" if result['success'] else "✗"
            renderer.log(f"{status} {Path(result['input']).name} → {result['output']}")
        
        success_count = sum(1 for r in results if r['success'])
        if success_count == len(results):
            renderer.log("🎉 Todos os arquivos processados com sucesso!", "SUCCESS")
        elif success_count > 0:
            renderer.log(f"⚠ {success_count}/{len(results)} arquivos processados", "WARNING")
        else:
            renderer.log("❌ Nenhum arquivo foi processado com sucesso", "ERROR")
            sys.exit(1)
    
    else:
        # Aplicar elementos da biblioteca se especificados
        if args.elements:
            elementos_lista = [e.strip()
                               for e in args.elements.split(',') if e.strip()]
            renderer.log(f"📦 Elementos a aplicar: {elementos_lista}")

            # Lê o arquivo original para aplicar elementos
            try:
                with open(args.input, 'r', encoding='utf-8') as f:
                    conteudo_original = f.read()

                # Extrai frontmatter existente
                frontmatter_atual, markdown_body = renderer.extract_frontmatter(
                    conteudo_original)

                # Aplica elementos
                frontmatter_atualizado = renderer.aplicar_elementos_biblioteca(
                    frontmatter_atual, elementos_lista)

                # Reconstrói o arquivo
                yaml_atualizado = yaml.dump(
                    frontmatter_atualizado, allow_unicode=True, sort_keys=False, indent=2)
                conteudo_atualizado = f"---\n{yaml_atualizado}---\n\n{markdown_body}"

                # Salva arquivo temporário ou sobrescreve original
                arquivo_temp = Path(args.input).with_suffix('.temp.md')
                with open(arquivo_temp, 'w', encoding='utf-8') as f:
                    f.write(conteudo_atualizado)

                renderer.log(
                    f"✅ Elementos aplicados. Arquivo atualizado: {arquivo_temp}")

                # Usa arquivo temporário para renderização
                success, output = renderer.render(
                    str(arquivo_temp), args.output, args.verbose)

                # Remove arquivo temporário
                arquivo_temp.unlink()

            except Exception as e:
                renderer.log(f"❌ Erro ao aplicar elementos: {e}", "ERROR")
                sys.exit(1)
        else:
            # Renderização normal
            success, output = renderer.render(
                args.input, args.output, args.verbose)
        
        if success:
            renderer.log("🎉 Renderização concluída com sucesso!", "SUCCESS")
            
            # Abrir no navegador se solicitado
            if args.open:
                renderer.log("Abrindo no navegador...", "INFO")
                webbrowser.open(f"file://{Path(output).absolute()}")
        else:
            renderer.log(f"❌ Falha na renderização: {output}", "ERROR")
            sys.exit(1)

if __name__ == "__main__":
    main()
