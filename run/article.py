from bs4 import BeautifulSoup
import argparse
import shutil
import os


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

    def mover_quarto_title_meta(self):
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
        self.mover_quarto_title_meta()
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
