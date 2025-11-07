# Como funcionará este projeto???

Este projeto utilizará o Decap-CMS para gerenciar e publicar artigos de noticias. As que forem publicadas serão
processadas por um script Python que organizará o conteudo em uma estrutura de pastas específica, facilitando a navegação e o arquivamento. 


## Python Script
O python irá pegar o conteúdo do arquivo formato pelo decap, json, e colocará essas informações
em um template de noticias em HTML. 

## Action Workflow
O workflow do GitHub Actions será configurado para ser acionado sempre que um novo artigo for publicado no Decap-CMS. 
A branch news é onde o decap cms publica as noticias. O workflow irá executar o script Python para processar o novo artigo e organizar o conteúdo na estrutura de pastas desejada.
Ele pegará as noticias da pasta article/noticias e processará cada arquivo JSON, convertendo-o em HTML e salvando-o na pasta correta dentro de newsroom/archive (gerando um identificador unico para cada artigo).

## Estrutura do json
Estrutura do json criada pelo `config.yml` do decap-CMS:
```
{
  "id": "",
  "ativo": true,
  "category": "",
  "date_start": "",
  "date_end": "",
  "mensagem": "",
  "thumbnail": "",
  "title": "",
  "subtitle": "",
  "summary": "",
  "body": "",
  "paginas": [],
  "date_published": ""
}
```


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
│   │       ├── tipo_dia_mes_ano_hora_minuto_segundo.json
│   │       ├── tipo_dia_mes_ano_hora_minuto_segundo.json
│   /newsroom/
│   ├── archive/ # terá a lista de artigos HTML publicados
│   ├── index.html                    # Página principal da newsroom
```


Posteriormente, o archive terá a estrutura:
```
├── archive/
│   └── pt_BR/
│   │   └── 2025/
│   │   │   └── 03/
│   │   │   │   ├── [0000-9999]/    # (código) Diretório do artigo
│   │   │   │   │   ├── index.html
│   │   │   │   │   └── src/
│   │   │   │   │   │   ├── img.png
├── assets/                       # Recursos estáticos (CSS, JS)
│   └── pt_BR/
│   │   └── 1/
│   │   │   ├── archive/
│   │   │   └── newsroom/         # articles ( /newsroom/index.html )
│   │   │   └── imagens/          # Imagens gerais: logos, marcas, backgrounds etc.
```

## Tipos de Noticias
As noticias poderão ser de varios tipos, como por exemplo:
- PRESS RELEASE
- QUICK READ
- EST STATEMENT
- PHOTOS
- RELEASE
- UPDATE