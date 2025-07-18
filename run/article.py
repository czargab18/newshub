#!/usr/bin/env python3
"""
Script Python para renderização de Markdown - Estatística Newsroom
Versão: 2.0 com quarto e processamento avançado de componentes
"""
from bs4 import BeautifulSoup
import argparse
import shutil
import os
from pathlib import Path
from typing import Optional
from datetime import datetime


class Article:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def lerArtigo(self, basedir):
        with open(basedir, 'r', encoding='utf-8') as f:
            html = f.read()
        return html

    def limparHead(self):
        if self.soup.head:
            self.soup.head.clear()

    #def dataArtigo():
    #    data = datetime.datetime.now().strftime('%Y/%m')
    #    return data

    def headerArtigo(self, html):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        titulo = soup.find('h1', class_='title')
        titulo_texto = titulo.get_text(strip=True) if titulo else None

        subtitulo = soup.find('p', class_='subtitle lead')
        subtitulo_texto = subtitulo.get_text(strip=True) if subtitulo else None

        categoria = soup.find('div', class_='description')
        categoria_texto = categoria.get_text(
            strip=True).strip().lower() if categoria else None

        data = soup.find('p', class_='date')
        data_texto = data.get_text(strip=True) if data else None

        if categoria_texto:
            if categoria_texto == "quickread":
                categoria_texto = "QUICK READ"
            elif categoria_texto == "release":
                categoria_texto = "RELEASE"
            elif categoria_texto == "update":
                categoria_texto = "UPDATE"

        return {
            'titulo': titulo_texto,
            'data': data_texto,
            'subtitulo': subtitulo_texto,
            'categoria': categoria_texto
        }
    
    def corrigirFigcaption(html):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        for figure in soup.find_all('figure', class_='figure'):
            p_img = figure.find('p')
            figcaption = figure.find('figcaption')
            if p_img and figcaption:
                img = p_img.find('img')
                if img:
                    img.extract()
                    p_img.decompose() # type: ignore
                    figcaption.insert_before(img)
        return str(soup)

    def capturar_main_sem_header(html):
        soup = BeautifulSoup(html, 'html.parser')
        main = soup.find('main')
        if main:
            header = main.find('header')
            if header:
                header.decompose()
            # Retorna apenas elementos filhos que são tags (ignora espaços e quebras de linha)
            return ''.join(str(child) for child in main.children if getattr(child, 'name', None))
        return None

    def modificarHead(self):
        self.limparHead()
        self.header()
        return str(self.soup)

    def salvarArtigo(self, output_path):
        novo_html = self.modificarHead()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(novo_html)

    def moverArtigo(self, novo_html_path, pasta_img_origem, nova_pasta_img):
        # Move o arquivo HTML
        if not os.path.exists(os.path.dirname(novo_html_path)):
            os.makedirs(os.path.dirname(novo_html_path))
        self.salvarArtigo(novo_html_path)

        if os.path.exists(pasta_img_origem):
            shutil.copytree(pasta_img_origem, nova_pasta_img,
                            dirs_exist_ok=True)

    def gerar_caminho_saida(self, frontmatter, data=None):
        from datetime import datetime
        meses = {
            'janeiro': '01', 'fevereiro': '02', 'março': '03', 'marco': '03', 'abril': '04',
            'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09',
            'outubro': '10', 'novembro': '11', 'dezembro': '12'
        }
        if data is None:
            data = frontmatter.get('data', '')
        partes = data.split('de')
        if len(partes) >= 3:
            dia = partes[0].strip()
            mes_nome = partes[1].strip().lower()
            ano = partes[2].strip()
            mes = meses.get(mes_nome, '00')
        else:
            ano = '0000'
            mes = '00'
        base_dir = Path('newsroom/archive') / ano / mes
        base_dir.mkdir(parents=True, exist_ok=True)
        # Busca próxima subpasta livre
        for i in range(10000):
            codigo = f"{i:04d}"
            pasta_artigo = base_dir / codigo
            if not pasta_artigo.exists():
                pasta_artigo.mkdir(parents=True, exist_ok=True)
                # Não cria pasta imagens
                return pasta_artigo / 'index.html', pasta_artigo
        raise Exception("Limite de 9999 artigos por mês atingido!")

    @staticmethod
    def inserir_artigo_no_template(template_path, artigo_html, frontmatter, output_path):
        from bs4 import BeautifulSoup
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        template_soup = BeautifulSoup(template, 'html.parser')
        # Preenche header do template
        categoria = frontmatter.get('categoria', '')
        data = frontmatter.get('data', '')
        titulo = frontmatter.get('titulo', '')
        subtitulo = frontmatter.get('subtitulo', '')
        template_soup.find('span', class_='category-eyebrow-category').string = categoria
        template_soup.find('span', class_='category-eyebrow-date').string = data
        template_soup.find('h1', class_='hero-headline').string = titulo
        subhead = template_soup.find('div', class_='article-subhead component')
        if subhead:
            subhead_content = subhead.find('div', class_='component-content')
            if subhead_content:
                subhead_content.string = subtitulo
        # Conteúdo do artigo
        artigo_main = Article.capturar_main_sem_header(artigo_html)
        artigo_main_corrigido = Article.corrigirFigcaption(artigo_main)
        # Insere conteúdo no <article>
        article_tag = template_soup.find('article', class_='article')
        if article_tag:
            # Remove tudo após o header
            for el in list(article_tag.children):
                if getattr(el, 'name', None) != 'div' or 'article-header' not in el.get('class', []):
                    el.extract()
            # Adiciona conteúdo do artigo
            novo_main = BeautifulSoup(artigo_main_corrigido, 'html.parser')
            for el in novo_main.contents:
                article_tag.append(el)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(str(template_soup))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Processa e move artigo HTML.")
    parser.add_argument('--basedir', type=str, required=True,
                        help='Caminho do arquivo HTML de entrada')
    parser.add_argument('--template', type=str, required=False,
                        help='Caminho do template body.html (opcional)')
    parser.add_argument('--outputdir', type=str, required=False,
                        help='Caminho do output body.html')
    args = parser.parse_args()

    # Usa o template informado ou o padrão
    template_path = args.template if args.template else './templates/artigo/html/body.html'

    artigo_html = Article('').lerArtigo(args.basedir)
    frontmatter = Article('').headerArtigo(artigo_html)
    # Gera caminho padrão de saída ou usa o destino informado
    if args.outputdir:
        # Extrai ano e mes do frontmatter
        data = frontmatter.get('data', '')
        partes = data.split('de')
        if len(partes) >= 3:
            mes_nome = partes[1].strip().lower()
            ano = partes[2].strip()
            meses = {
                'janeiro': '01', 'fevereiro': '02', 'março': '03', 'marco': '03', 'abril': '04',
                'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09',
                'outubro': '10', 'novembro': '11', 'dezembro': '12'
            }
            mes = meses.get(mes_nome, '00')
        else:
            ano = '0000'
            mes = '00'
        # Busca próxima subpasta livre
        base_dir = Path(args.outputdir) / ano / mes
        base_dir.mkdir(parents=True, exist_ok=True)
        for i in range(10000):
            codigo = f"{i:04d}"
            pasta_destino = base_dir / codigo
            if not pasta_destino.exists():
                pasta_destino.mkdir(parents=True, exist_ok=True)
                output_path = pasta_destino / 'index.html'
                break
    else:
        output_path, pasta_destino = Article('').gerar_caminho_saida(frontmatter)
    Article.inserir_artigo_no_template(
        template_path, artigo_html, frontmatter, output_path)
    # Move pastas img/ e src/ se existirem
    pasta_img_origem = os.path.join(os.path.dirname(args.basedir), 'img')
    pasta_src_origem = os.path.join(os.path.dirname(args.basedir), 'src')
    if os.path.exists(pasta_img_origem):
        shutil.copytree(pasta_img_origem, os.path.join(pasta_destino, 'img'), dirs_exist_ok=True)
    if os.path.exists(pasta_src_origem):
        shutil.copytree(pasta_src_origem, os.path.join(pasta_destino, 'src'), dirs_exist_ok=True)
