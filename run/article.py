from bs4 import BeautifulSoup

class Article:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def limpar_head(self):
        if self.soup.head:
            self.soup.head.clear()

    def mover_quarto_title_meta(self):
        header = self.soup.find('header', {'id': 'title-block-header'})
        if header:
            title_meta = header.find('div', {'class': 'quarto-title-meta'}) # type: ignore
            title = header.find('div', {'class': 'quarto-title'}) # type: ignore
            if title_meta and title:
                title_meta.extract()  # type: ignore
                title.insert_before(title_meta)  # type: ignore

    def modificar(self):
        self.limpar_head()
        self.mover_quarto_title_meta()
        return str(self.soup)

if __name__ == "__main__":
    basedir = "build2/article/_output/artigo.html"
    outputdir = "./article/index.html"
    with open(basedir, 'r', encoding='utf-8') as f:
        html = f.read()
    modifier = Article(html)
    novo_html = modifier.modificar()
    with open(outputdir, 'w', encoding='utf-8') as f:
        f.write(novo_html)
