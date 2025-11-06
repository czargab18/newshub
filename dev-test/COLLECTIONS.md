# Coleções do CMS - Newshub

Este documento descreve as coleções disponíveis no sistema de gerenciamento de conteúdo (DecapCMS) do Newshub.

## 📚 Visão Geral

O sistema conta com **5 coleções principais** para organização de diferentes tipos de conteúdo:

1. **Publicações** (`conteudo`) - Artigos e publicações gerais
2. **Educação** (`educacao`) - Materiais educacionais
3. **Sentindo Ribbon** (`sentindo_ribbon`) - Banners de destaque
4. **Notícias** (`noticias`) - Notícias institucionais
5. **Editais** (`editais`) - Editais e processos seletivos

---

## 1. 📰 Publicações (conteudo)

**Pasta:** `article/`
**Descrição:** Gerenciamento de artigos, notícias e conteúdos gerais do site.

### Principais Campos:
- **Título Principal** (`headline`): Título do artigo
- **Categoria**: QUICK READ, EST STATEMENT, PHOTOS, PRESS RELEASE, RELEASE, UPDATE
- **Público-Alvo**: GRADUAÇÃO, PÓS-GRADUAÇÃO, COMUNIDADE EXTERNA
- **Corpo**: Conteúdo em Markdown
- **Miniatura**: Imagem de preview
- **Tags e Keywords**: Para organização e SEO

### Filtros e Agrupamentos:
- Filtros: Por público-alvo
- Agrupamentos: Por ano, categoria, idioma

---

## 2. 🎓 Educação (educacao)

**Pasta:** `article/educacao/`
**Descrição:** Materiais educacionais, cursos, tutoriais e recursos didáticos.

### Principais Campos:
- **Título** (`titulo`): Nome do conteúdo educacional
- **Tipo de Conteúdo**: tutorial, curso, apostila, video-aula, exercicio, material-apoio, webinar
- **Nível Educacional**: educacao-basica, ensino-medio, graduacao, pos-graduacao, extensao
- **Área do Conhecimento**: estatistica, matematica, geografia, economia, demografia, computacao, ciencias-sociais
- **Duração Estimada**: Tempo necessário para o conteúdo
- **Carga Horária**: Em horas
- **Objetivos de Aprendizagem**: Lista de objetivos
- **Pré-requisitos**: Conhecimentos necessários

### Casos de Uso:
- Tutoriais de ferramentas estatísticas
- Cursos online
- Material de apoio para disciplinas
- Exercícios práticos
- Webinars gravados

### Filtros e Agrupamentos:
- Filtros: Por nível educacional
- Agrupamentos: Por ano, tipo de conteúdo, nível

---

## 3. 🎨 Sentindo Ribbon (sentindo_ribbon)

**Pasta:** `article/ribbon/`
**Descrição:** Banners e ribbons de destaque para exibição na página inicial e em locais estratégicos do site.

### Principais Campos:
- **Título** (`titulo`): Texto principal do ribbon
- **Tipo de Ribbon**: destaque, alerta, informacao, promocao, evento, urgente
- **Prioridade**: baixa, media, alta, urgente
- **Ativo** (`ativo`): Boolean para ativar/desativar
- **Data de Início/Término**: Período de exibição
- **Link de Destino**: URL para redirecionamento
- **Cor de Fundo**: azul, verde, amarelo, vermelho, laranja, roxo, cinza
- **Imagem de Fundo**: Opcional
- **Texto do Botão**: Call-to-action

### Casos de Uso:
- Avisos urgentes
- Destaques de eventos
- Promoções especiais
- Alertas importantes
- Banners informativos temporários

### Filtros e Agrupamentos:
- Filtros: Por status (ativo/inativo), prioridade
- Agrupamentos: Por tipo, prioridade, status

---

## 4. 📢 Notícias (noticias)

**Pasta:** `article/noticias/`
**Descrição:** Notícias institucionais, comunicados e informações gerais.

### Principais Campos:
- **Título** (`titulo`): Título da notícia
- **Chamada/Resumo** (`chamada`): Resumo breve (100-150 caracteres)
- **Categoria**: institucional, academica, pesquisa, eventos, comunicado, destaque, servico
- **Urgência**: baixa, normal, alta, urgente
- **Publicado**: Boolean para controlar visibilidade
- **Destaque na Home**: Para notícias principais
- **Autor**: Nome do autor/assessoria
- **Imagem Principal**: Com créditos e legenda
- **Fonte**: Origem da notícia

### Casos de Uso:
- Comunicados institucionais
- Notícias acadêmicas
- Divulgação de pesquisas
- Cobertura de eventos
- Avisos de serviço

### Filtros e Agrupamentos:
- Filtros: Por urgência, status de publicação, categoria
- Agrupamentos: Por ano, categoria, urgência

---

## 5. 📋 Editais (editais)

**Pasta:** `article/editais/`
**Descrição:** Editais, avisos, chamadas públicas e processos seletivos.

### Principais Campos:
- **Número do Edital** (`numero_edital`): Ex: 001/2025
- **Título** (`titulo`): Nome do edital
- **Tipo**: concurso, selecao, chamada-publica, credenciamento, licitacao, pregao, processo-seletivo
- **Status**: previsto, aberto, em-andamento, suspenso, encerrado, cancelado, homologado
- **Data de Abertura/Encerramento**: Período do edital
- **Número de Vagas**: Quantidade disponível
- **Valor/Remuneração**: Informação financeira
- **Órgão/Instituição**: Responsável pelo edital
- **Requisitos**: Lista de requisitos para participação
- **Documento do Edital**: Arquivo PDF principal
- **Link de Inscrição**: URL para inscrição online

### Casos de Uso:
- Concursos públicos
- Processos seletivos
- Chamadas públicas
- Credenciamentos
- Licitações

### Filtros e Agrupamentos:
- Filtros: Por status, tipo
- Agrupamentos: Por tipo, status, ano

---

## 🚀 Como Usar

### Acessando o CMS

1. Execute o script de inicialização:
   ```powershell
   .\bin\start.ps1
   ```

2. Acesse: `http://localhost:8080/admin/`

3. Faça login com suas credenciais do GitHub

### Criando Novo Conteúdo

1. Selecione a coleção desejada no menu lateral
2. Clique em "New [Nome da Coleção]"
3. Preencha os campos obrigatórios (marcados com *)
4. Adicione conteúdo opcional conforme necessário
5. Clique em "Save" para salvar como rascunho
6. Quando pronto, use "Publish" para publicar

### Organizando Conteúdo

- Use **Tags** para facilitar a busca e organização
- Utilize **Filtros** no painel lateral para encontrar conteúdos específicos
- Os **Agrupamentos** ajudam a visualizar conteúdos por categorias

---

## 📁 Estrutura de Arquivos

```
article/
├── [arquivos gerais de publicações]
├── educacao/
│   └── [materiais educacionais]
├── ribbon/
│   └── [banners e ribbons]
├── noticias/
│   └── [notícias]
└── editais/
    └── [editais]
```

Cada conteúdo é salvo como um arquivo JSON com timestamp no formato:
`YYYY-MM-DD_HH-MM-SS.json`

---

## 🔧 Configuração

A configuração completa das coleções está em:
- **Desenvolvimento/Teste:** `dev-test/admin/config.yml`
- **Produção:** `admin/config.yml`

Para adicionar novas coleções ou modificar as existentes, edite o arquivo `config.yml` correspondente.

---

## 📝 Notas Importantes

1. **Campos Obrigatórios**: Sempre preencha os campos marcados como `required: true`
2. **Imagens**: Use formatos web otimizados (JPG, PNG, WebP)
3. **Markdown**: O widget markdown suporta formatação rica e inclusão de imagens
4. **Datas**: Use o formato padrão DD/MM/YYYY HH:mm
5. **Slugs**: São gerados automaticamente baseados na data/hora de criação

---

## 🆘 Suporte

Para problemas ou dúvidas:
1. Consulte a [documentação do DecapCMS](https://decapcms.org/docs/)
2. Verifique o arquivo `bin/README.md` para troubleshooting
3. Entre em contato com a equipe de desenvolvimento

---

**Última atualização:** Novembro 2025
