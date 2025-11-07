# Como funcionará este projeto???

Este projeto utilizará o Decap-CMS para gerenciar e publicar artigos de noticias. As que forem publicadas serão
processadas por um script Python que organizará o conteudo em uma estrutura de pastas específica, facilitando a navegação e o arquivamento. 


## Python Script
O python irá pegar o conteúdo do arquivo formato pelo decap, json, e colocará essas informações
em um template de noticias em HTML. 

## Action Workflow
O workflow do GitHub Actions será configurado para ser acionado sempre que um novo artigo for publicado no Decap-CMS. 
A branch news é onde o decap cms publica as noticias. O workflow irá executar o script Python para processar o novo artigo e organizar o conteúdo na estrutura de pastas desejada.

## Estrutura de Pastas
A estrutura de pastas será organizada da seguinte forma:

```
./  
│   /newshub/
│   ├── admin/
│   │   ├── config.yml          # Configuração do Decap CMS para editar as notícias.
│   │   └── index.html          # Interface do Decap CMS.
│   ├── article/
│   │   └── noticias/
│   │       ├── 2025-11-07-titulo-noticia-1.json
│   │       └── 2025-11-08-titulo-noticia-2.json
│   /newsroom/
│   ├── archive/
│   │   └── pt_BR/
│   │   │   └── 2025/
│   │   │   │   └── 03/
│   │   │   │   │   ├── xxxxxxxx/      # (código) Diretório do artigo
│   │   │   │   │   │   ├── index.html
│   │   │   │   │   │   └── src/
│   │   │   │   │   │   │   ├── img.png
│   ├── assets/                       # Recursos estáticos (CSS, JS)
│   │   └── pt_BR/
│   │   │   └── 1/
│   │   │   │   ├── archive/
│   │   │   │   └── newsroom/         # articles ( /newsroom/index.html )
│   │   │   │   └── imagens/          # Imagens gerais: logos, marcas, backgrounds etc.
│   ├── index.html                    # Página principal da newsroom
```
