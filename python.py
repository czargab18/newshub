 def corrigirFigcaption(html):
      soup = BeautifulSoup(html, 'html.parser')
       for figure in soup.find_all('figure', class_='figure'):
            p_img = figure.find('p')
            figcaption = figure.find('figcaption')
            if p_img and figcaption:
                img = p_img.find('img')
                if img:
                    img.extract()
                    p_img.decompose()
                    figcaption.insert_after(img)
        return str(soup)


desejado:
<figure class="figure">
<img src="img/img1.jpg" title="Titulo da imagem" class="img-fluid figure-img" alt="Texto alternativo">
<figcaption>texto do figcaption</figcaption>
</figure>

<div class="quarto-figure quarto-figure-center">
<figure class="figure">
<p><img src="img/img1.jpg" title="Titulo da imagem" class="img-fluid figure-img" alt="Texto alternativo"></p>
<figcaption>texto do figcaption</figcaption>
</figure>
</div>

