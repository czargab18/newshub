#!/usr/bin/env python3
"""
Script Python para renderização de Markdown - Estatística Newsroom
Versão: 2.0 com quarto e processamento avançado de componentes
"""
from bs4 import BeautifulSoup
import argparse
import shutil
import os
import sys
import yaml
import re
import json
import webbrowser
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

    def header(self):
        header = self.soup.find('header', {'id': 'title-block-header'})
        if header:
            title_meta = header.find(
                'div', {'class': 'quarto-title-meta'})  # type: ignore
            title = header.find(
                'div', {'class': 'quarto-title'})  # type: ignore
            if title_meta and title:
                title_meta.extract()  # type: ignore
                title.insert_before(title_meta)  # type: ignore

    def modificar(self):
        self.limparHead()
        self.header()
        return str(self.soup)

    def salvarArtigo(self, output_path):
        novo_html = self.modificar()
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

    def gerar_caminho_saida(self, frontmatter):
        data = frontmatter.get('date', '')
        partes = data.split('de')
        if len(partes) >= 3:
            ano = partes[-1].strip()
            mes_nome = partes[1].strip().lower()
            meses = {
                'janeiro': 1, 'fevereiro': 2, 'março': 3, 'marco': 3, 'abril': 4,
                'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9,
                'outubro': 10, 'novembro': 11, 'dezembro': 12
            }
            mes = str(meses.get(mes_nome, 0))
        else:
            ano = '0000'
            mes = '00'
        base_dir = Path('newsroom') / 'archive' / ano / mes
        base_dir.mkdir(parents=True, exist_ok=True)
        # Busca próxima subpasta livre
        for i in range(10000):
            codigo = f"{i:04d}"
            pasta_artigo = base_dir / codigo
            if not pasta_artigo.exists():
                pasta_artigo.mkdir(parents=True, exist_ok=True)
                (pasta_artigo / 'imagens').mkdir(exist_ok=True)
                return pasta_artigo / 'index.html', pasta_artigo / 'imagens'
        raise Exception("Limite de 9999 artigos por mês atingido!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Processa e move artigo HTML.")
    parser.add_argument('--basedir', type=str, required=True,
                        help='Caminho do arquivo HTML de entrada')
    parser.add_argument('--outputdir', type=str, required=True,
                        help='Caminho do arquivo HTML de saída')
    args = parser.parse_args()

    # Usa a função lerArtigo
    artigo = Article(Article('').lerArtigo(args.basedir))
    artigo.salvarArtigo(args.outputdir)

    # Calcula o destino da pasta de imagens automaticamente
    pasta_img_destino = os.path.join(os.path.dirname(args.outputdir), 'img')
    # Calcula a pasta de imagens de origem dinamicamente
    pasta_img_origem = os.path.join(os.path.dirname(args.basedir), 'img')
    artigo.moverArtigo(args.outputdir, pasta_img_origem, pasta_img_destino)
