from bs4 import BeautifulSoup


class HtmlModifier:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def limpar_head(self):
        if self.soup.head:
            self.soup.head.clear()

    def mover_quarto_title_meta(self):
        header = self.soup.find('header', {'id': 'title-block-header'})
        if header:
            title_meta = header.find('div', {'class': 'quarto-title-meta'})
            title = header.find('div', {'class': 'quarto-title'})
            if title_meta and title:
                title_meta.extract()
                title.insert_before(title_meta)

    def modificar(self):
        self.limpar_head()
        self.mover_quarto_title_meta()
        return str(self.soup)

# Exemplo de uso:
# with open('artigo.html', 'r', encoding='utf-8') as f:
#     html = f.read()
# modifier = HtmlModifier(html)
# novo_html = modifier.modificar()
# with open('artigo_modificado.html', 'w', encoding='utf-8') as f:
#     f.write(novo_html)
