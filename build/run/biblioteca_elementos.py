#!/usr/bin/env python3
"""
Biblioteca de Elementos Prontos para Apple Newsroom
Sistema para puxar/adicionar elementos pré-definidos em artigos
"""

import yaml
import json
from typing import Dict, Any, List, Optional
from pathlib import Path


class BibliotecaElementos:
    """
    Gerenciador de biblioteca de elementos prontos para artigos
    """

    def __init__(self):
        """Inicializa a biblioteca com elementos pré-definidos"""
        self.elementos = self._carregar_elementos_padrao()

    def _carregar_elementos_padrao(self) -> Dict[str, Any]:
        """Carrega elementos pré-definidos da biblioteca"""
        return {
            # === COMPONENTES DE NAVEGAÇÃO ===
            "navegacao": {
                "header_completo": {
                    "description": "Cabeçalho completo com navegação global e local",
                    "includes": {
                        "header_global": {
                            "file": "globalheader.html",
                            "position": "after_body_open",
                            "priority": 1
                        },
                        "local_nav": {
                            "file": "localnav.html",
                            "position": "after_globalheader",
                            "priority": 2
                        }
                    },
                    "components": {
                        "globalnav": {
                            "enabled": True,
                            "analytics_region": "global nav",
                            "store_api": "/[storefront]/shop/bag/status"
                        }
                    }
                },
                "header_simples": {
                    "description": "Cabeçalho simplificado sem navegação local",
                    "includes": {
                        "header_global": {
                            "file": "globalheader.html",
                            "position": "after_body_open",
                            "priority": 1
                        }
                    }
                }
            },

            # === COMPONENTES DE ANALYTICS ===
            "analytics": {
                "newsroom_padrao": {
                    "description": "Analytics padrão para artigos de newsroom",
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_0": "applestoreww",
                        "s_bucket_1": "applestoreww",
                        "s_bucket_2": "applestoreww",
                        "track": "Redação - Estatística"
                    }
                },
                "produto_lancamento": {
                    "description": "Analytics para lançamentos de produtos",
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_0": "applestoreww",
                        "s_bucket_1": "product_launch",
                        "s_bucket_2": "product_launch",
                        "track": "Redação - Estatística - Lançamento",
                        "s_products": "produto-lancamento",
                        "s_events": "event15=o"
                    }
                },
                "comunicado_imprensa": {
                    "description": "Analytics para comunicados de imprensa",
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_0": "applestoreww",
                        "s_bucket_1": "press_release",
                        "s_bucket_2": "press_release",
                        "track": "Redação - Estatística - Comunicado",
                        "s_events": "event20=o"
                    }
                }
            },

            # === COMPONENTES DE MÍDIA SOCIAL ===
            "social": {
                "twitter_completo": {
                    "description": "Twitter Cards completo com imagem grande",
                    "twitter": {
                        "card": "summary_large_image",
                        "site": "@estatisticabr",
                        "creator": "@estatisticabr",
                        "domain": "estatistica.pro"
                    }
                },
                "twitter_simples": {
                    "description": "Twitter Cards simples",
                    "twitter": {
                        "card": "summary",
                        "site": "@estatisticabr",
                        "domain": "estatistica.pro"
                    }
                },
                "og_artigo": {
                    "description": "Open Graph otimizado para artigos",
                    "og": {
                        "type": "article",
                        "site_name": "Redação - Estatística",
                        "locale": "pt_BR",
                        "image": "https://www.estatistica.pro/newsroom/images/default/tile/default.jpg.og.jpg",
                        "image:width": "1200",
                        "image:height": "630",
                        "image:alt": "Redação - Estatística"
                    }
                },
                "og_produto": {
                    "description": "Open Graph otimizado para páginas de produto",
                    "og": {
                        "type": "product",
                        "site_name": "Redação - Estatística",
                        "locale": "pt_BR",
                        "image": "https://www.estatistica.pro/newsroom/images/default/tile/product.jpg.og.jpg",
                        "image:width": "1200",
                        "image:height": "630"
                    }
                }
            },

            # === COMPONENTES DE LAYOUT ===
            "layout": {
                "artigo_padrao": {
                    "description": "Layout padrão para artigos de newsroom",
                    "components": {
                        "globalmessage": {
                            "enabled": True,
                            "lang": "pt-BR",
                            "dir": "ltr"
                        },
                        "article_hero": {
                            "enabled": True,
                            "style": "default"
                        },
                        "article_content": {
                            "enabled": True,
                            "typography": "newsroom"
                        }
                    },
                    "stylesheets": [
                        "www.estatistica.pro/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3",
                        "/newsroom/styles/newsroom-article.css"
                    ]
                },
                "landing_page": {
                    "description": "Layout para páginas de destino/landing",
                    "components": {
                        "hero_banner": {
                            "enabled": True,
                            "style": "full_width",
                            "animation": "fade_in"
                        },
                        "feature_grid": {
                            "enabled": True,
                            "columns": 3,
                            "style": "card"
                        }
                    },
                    "stylesheets": [
                        "www.estatistica.pro/wss/fonts?families=SF+Pro,v3|SF+Pro+Icons,v3",
                        "/newsroom/styles/landing-page.css"
                    ]
                }
            },

            # === TEMPLATES DE CATEGORIAS ===
            "categorias": {
                "comunicado_imprensa": {
                    "description": "Template completo para comunicados de imprensa",
                    "meta_basico": {
                        "category": "COMUNICADO DE IMPRENSA",
                        "category_class": "category_release",
                        "type": "article"
                    },
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_1": "press_release",
                        "s_bucket_2": "press_release",
                        "track": "Redação - Estatística - Comunicado"
                    },
                    "og": {
                        "type": "article",
                        "image": "https://www.estatistica.pro/newsroom/images/press/tile/default.jpg.og.jpg"
                    }
                },
                "lancamento_produto": {
                    "description": "Template para lançamentos de produtos",
                    "meta_basico": {
                        "category": "LANÇAMENTO DE PRODUTO",
                        "category_class": "category_product",
                        "type": "product"
                    },
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_1": "product_launch",
                        "s_bucket_2": "product_launch",
                        "track": "Redação - Estatística - Lançamento"
                    },
                    "components": {
                        "product_showcase": {
                            "enabled": True,
                            "style": "hero"
                        }
                    }
                },
                "evento": {
                    "description": "Template para eventos e keynotes",
                    "meta_basico": {
                        "category": "EVENTO",
                        "category_class": "category_event",
                        "type": "event"
                    },
                    "analytics": {
                        "s_channel": "newsroom",
                        "s_bucket_1": "event",
                        "s_bucket_2": "event",
                        "track": "Redação - Estatística - Evento"
                    },
                    "components": {
                        "event_info": {
                            "enabled": True,
                            "show_date": True,
                            "show_location": True
                        }
                    }
                }
            },

            # === SNIPPETS DE CONTEÚDO ===
            "snippets": {
                "disclaimer_padrao": {
                    "description": "Disclaimer padrão para artigos",
                    "content": """
---

**Sobre a Redação - Estatística**

A Redação - Estatística é dedicada a fornecer análises precisas e insights valiosos sobre tecnologia, dados e inovação. Nossos comunicados refletem nosso compromisso com a transparência e qualidade informativa.

**Contato para Imprensa:**
- Email: press@estatistica.pro
- Telefone: +55 (11) 1234-5678
"""
                },
                "cta_newsletter": {
                    "description": "Call-to-action para newsletter",
                    "content": """
## Mantenha-se Atualizado

Inscreva-se em nossa newsletter para receber as últimas análises e insights diretamente em seu email.

[**Inscrever-se →**](https://www.estatistica.pro/newsletter)
"""
                },
                "rodape_social": {
                    "description": "Links de redes sociais para rodapé",
                    "content": """
### Siga-nos nas Redes Sociais

- [Twitter](https://twitter.com/estatisticabr)
- [LinkedIn](https://linkedin.com/company/estatistica-pro)
- [YouTube](https://youtube.com/c/estatisticapro)
"""
                }
            }
        }

    def listar_elementos(self, categoria: Optional[str] = None) -> Dict[str, Any]:
        """
        Lista elementos disponíveis, opcionalmente filtrados por categoria
        
        Args:
            categoria: Categoria específica para filtrar (opcional)
            
        Returns:
            Dicionário com elementos disponíveis
        """
        if categoria:
            return self.elementos.get(categoria, {})
        return self.elementos

    def obter_elemento(self, categoria: str, nome: str) -> Optional[Dict[str, Any]]:
        """
        Obtém um elemento específico da biblioteca
        
        Args:
            categoria: Categoria do elemento
            nome: Nome do elemento
            
        Returns:
            Dados do elemento ou None se não encontrado
        """
        return self.elementos.get(categoria, {}).get(nome)

    def aplicar_elemento(self, frontmatter: Dict[str, Any], categoria: str, nome: str, sobrescrever: bool = False) -> Dict[str, Any]:
        """
        Aplica um elemento da biblioteca ao frontmatter
        
        Args:
            frontmatter: Frontmatter atual do artigo
            categoria: Categoria do elemento
            nome: Nome do elemento
            sobrescrever: Se deve sobrescrever valores existentes
            
        Returns:
            Frontmatter atualizado
        """
        elemento = self.obter_elemento(categoria, nome)
        if not elemento:
            print(f"⚠️  Elemento '{categoria}/{nome}' não encontrado na biblioteca")
            return frontmatter

        # Cria uma cópia do frontmatter para não modificar o original
        resultado = frontmatter.copy()

        # Aplica cada seção do elemento
        for secao, dados in elemento.items():
            if secao == "description":
                continue  # Pula a descrição

            if secao == "content":
                # Para snippets de conteúdo, adiciona no final
                if "content_snippets" not in resultado:
                    resultado["content_snippets"] = []
                resultado["content_snippets"].append({
                    "name": f"{categoria}_{nome}",
                    "content": dados
                })
            else:
                # Para outras seções, faz merge
                if secao not in resultado:
                    resultado[secao] = {}

                if isinstance(dados, dict):
                    for chave, valor in dados.items():
                        if sobrescrever or chave not in resultado[secao]:
                            resultado[secao][chave] = valor
                else:
                    if sobrescrever or secao not in resultado:
                        resultado[secao] = dados

        print(f"✅ Elemento '{categoria}/{nome}' aplicado com sucesso")
        return resultado

    def criar_preset(self, nome: str, elementos: List[tuple], descricao: str = "") -> Dict[str, Any]:
        """
        Cria um preset combinando múltiplos elementos
        
        Args:
            nome: Nome do preset
            elementos: Lista de tuplas (categoria, nome) dos elementos
            descricao: Descrição do preset
            
        Returns:
            Configuração combinada do preset
        """
        preset: Dict[str, Any] = {"description": descricao}
        
        for categoria, nome_elemento in elementos:
            elemento = self.obter_elemento(categoria, nome_elemento)
            if elemento:
                for secao, dados in elemento.items():
                    if secao == "description":
                        continue
                    
                    if secao not in preset:
                        preset[secao] = {}
                    
                    if isinstance(dados, dict) and isinstance(preset[secao], dict):
                        preset[secao].update(dados)
                    else:
                        preset[secao] = dados

        return preset

    def salvar_elemento_personalizado(self, categoria: str, nome: str, elemento: Dict[str, Any], descricao: str = ""):
        """
        Salva um elemento personalizado na biblioteca
        
        Args:
            categoria: Categoria do elemento
            nome: Nome do elemento
            elemento: Dados do elemento
            descricao: Descrição do elemento
        """
        if categoria not in self.elementos:
            self.elementos[categoria] = {}
        
        self.elementos[categoria][nome] = elemento.copy()
        if descricao:
            self.elementos[categoria][nome]["description"] = descricao
        
        print(f"✅ Elemento personalizado '{categoria}/{nome}' salvo na biblioteca")

    def exportar_biblioteca(self, arquivo: str):
        """
        Exporta a biblioteca atual para um arquivo YAML
        
        Args:
            arquivo: Caminho do arquivo para salvar
        """
        with open(arquivo, 'w', encoding='utf-8') as f:
            yaml.dump(self.elementos, f, allow_unicode=True, indent=2, sort_keys=False)
        print(f"✅ Biblioteca exportada para: {arquivo}")

    def importar_biblioteca(self, arquivo: str):
        """
        Importa elementos de um arquivo YAML
        
        Args:
            arquivo: Caminho do arquivo para importar
        """
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                novos_elementos = yaml.safe_load(f)
            
            # Faz merge dos elementos
            for categoria, elementos in novos_elementos.items():
                if categoria not in self.elementos:
                    self.elementos[categoria] = {}
                self.elementos[categoria].update(elementos)
            
            print(f"✅ Biblioteca importada de: {arquivo}")
        except Exception as e:
            print(f"❌ Erro ao importar biblioteca: {e}")

    def buscar_elementos(self, termo: str) -> Dict[str, Any]:
        """
        Busca elementos que contenham o termo na descrição ou nome
        
        Args:
            termo: Termo de busca
            
        Returns:
            Elementos encontrados
        """
        resultado = {}
        termo_lower = termo.lower()
        
        for categoria, elementos in self.elementos.items():
            for nome, dados in elementos.items():
                # Busca no nome
                if termo_lower in nome.lower():
                    if categoria not in resultado:
                        resultado[categoria] = {}
                    resultado[categoria][nome] = dados
                    continue
                
                # Busca na descrição
                descricao = dados.get("description", "")
                if termo_lower in descricao.lower():
                    if categoria not in resultado:
                        resultado[categoria] = {}
                    resultado[categoria][nome] = dados
        
        return resultado


def demo_biblioteca():
    """Demonstração de uso da biblioteca de elementos"""
    print("=== DEMO: Biblioteca de Elementos ===\n")
    
    # Inicializa a biblioteca
    biblioteca = BibliotecaElementos()
    
    # Lista categorias disponíveis
    print("📚 Categorias disponíveis:")
    for categoria in biblioteca.elementos.keys():
        print(f"  • {categoria}")
    
    print(f"\n🔍 Elementos na categoria 'social':")
    elementos_social = biblioteca.listar_elementos("social")
    for nome, dados in elementos_social.items():
        descricao = dados.get("description", "Sem descrição")
        print(f"  • {nome}: {descricao}")
    
    # Simula frontmatter base
    frontmatter_base = {
        "meta_basico": {
            "title": "Meu Artigo",
            "description": "Descrição do artigo"
        }
    }
    
    print(f"\n🛠️  Aplicando elemento 'social/twitter_completo':")
    frontmatter_atualizado = biblioteca.aplicar_elemento(
        frontmatter_base, 
        "social", 
        "twitter_completo"
    )
    
    print(f"\n📄 Resultado:")
    print(yaml.dump(frontmatter_atualizado, allow_unicode=True, indent=2))
    
    # Busca elementos
    print(f"\n🔍 Buscando elementos com 'twitter':")
    resultados = biblioteca.buscar_elementos("twitter")
    for categoria, elementos in resultados.items():
        print(f"  {categoria}:")
        for nome in elementos.keys():
            print(f"    • {nome}")


if __name__ == "__main__":
    demo_biblioteca()
