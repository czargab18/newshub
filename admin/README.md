# 📂 Admin - Estrutura de Arquivos

Sistema de gerenciamento de conteúdo personalizado para o Departamento de Estatística - UnB.

## 📋 Arquivos

```
admin/
├── index.html              # Página principal (HTML limpo)
├── config.yml              # Configuração do Decap CMS
├── custom-styles.css       # Estilos personalizados (Login + Preview)
├── custom-scripts.js       # Scripts personalizados (Login + Preview)
├── custom-login.css        # Backup completo dos estilos de login
├── CUSTOMIZACAO.md         # Guia de customização
└── README.md               # Este arquivo
```

---

## 🎯 Descrição dos Arquivos

### `index.html`
**Página principal do CMS**
- HTML limpo e minimalista
- Importa CSS e JS externos
- Contém apenas scripts do Decap CMS e Netlify Identity

### `config.yml`
**Configuração do Decap CMS**
- Define coleções e campos
- Configurações de workflow editorial
- Media folders e publish mode

### `custom-styles.css`
**Estilos personalizados**
- 🎨 Login customizado (sem logo do Decap CMS)
- 📊 Preview dos artigos formatado
- 🎭 Design institucional UnB

**Seções:**
1. Login Page (gradient roxo, logo 📊, título institucional)
2. Preview Content (estilos Markdown)
3. Responsividade

### `custom-scripts.js`
**Scripts personalizados**
- 🔧 Oculta logo do Decap CMS dinamicamente
- 📝 Customiza textos da interface
- 🎨 Renderiza preview dos artigos

**Funções:**
1. `DOMContentLoaded` → Observa mudanças no DOM
2. `ArticlePreview` → Componente React para preview
3. `CMS.registerPreviewTemplate` → Registra template

### `custom-login.css`
**Backup completo**
- Versão standalone dos estilos de login
- Incluí animações e variações de tema
- Útil para referência

### `CUSTOMIZACAO.md`
**Guia de personalização**
- Como trocar logo
- Como mudar cores
- Como alterar textos
- Exemplos de temas prontos

---

## 🚀 Como Usar

### Desenvolvimento Local

1. **Iniciar servidor Decap:**
   ```powershell
   npx decap-server
   ```

2. **Acessar CMS:**
   ```
   http://localhost:8081/admin/
   ```

3. **Editar estilos:**
   - Modifique `custom-styles.css`
   - Salve e recarregue a página

4. **Editar scripts:**
   - Modifique `custom-scripts.js`
   - Salve e faça hard refresh (Ctrl+Shift+R)

### Produção (Netlify)

Os arquivos são servidos automaticamente pelo Netlify:
```
https://seu-site.netlify.app/admin/
```

---

## 🎨 Personalização

### Trocar Logo do Emoji para Imagem

**No `custom-styles.css`, descomente:**

```css
[class*="AuthenticationPage-card"]::before {
  content: '' !important;
  background-image: url('/admin/logo.png') !important;
  background-size: contain !important;
  background-repeat: no-repeat !important;
  background-position: center !important;
  width: 120px !important;
  height: 120px !important;
  margin: 0 auto 1.5rem !important;
}
```

E adicione sua logo em: `/admin/logo.png`

### Mudar Cores do Tema

**No `custom-styles.css`, localize:**

```css
/* Gradient de fundo */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;

/* Botões */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
```

**Cores UnB (exemplo):**
```css
background: linear-gradient(135deg, #003366 0%, #0052a3 100%) !important;
```

### Alterar Textos

**No `custom-styles.css`:**

```css
/* Título institucional */
content: 'Departamento de Estatística' !important;

/* Rodapé */
content: 'Universidade de Brasília © 2025' !important;
```

**No `custom-scripts.js`:**

```javascript
heading.textContent = 'Sistema de Gerenciamento de Conteúdo';
```

---

## 🔧 Manutenção

### Adicionar Novo Campo no Preview

**No `custom-scripts.js`:**

```javascript
const ArticlePreview = ({ entry, widgetFor, getAsset }) => {
  // Adicione novo campo
  const novocampo = entry.getIn(['data', 'novocamp']);
  
  return h('div', { className: 'cms-preview-content' },
    // ...existing code...
    
    // Renderize novo campo
    novoampo ? h('div', {}, novocampo) : null
  );
};
```

### Adicionar Novo Estilo no Preview

**No `custom-styles.css`:**

```css
.cms-preview-content .novo-elemento {
  color: #333;
  font-size: 1rem;
  /* seus estilos aqui */
}
```

---

## 📦 Estrutura Recomendada

```
admin/
├── index.html              ← Importa CSS e JS
├── config.yml              ← Configuração CMS
├── custom-styles.css       ← Todos os estilos
├── custom-scripts.js       ← Todos os scripts
├── logo.png               ← Logo institucional (opcional)
└── README.md              ← Documentação
```

---

## 🐛 Troubleshooting

### Estilos não aplicados?
1. Verifique se o caminho está correto: `/admin/custom-styles.css`
2. Limpe o cache: `Ctrl+Shift+Delete`
3. Faça hard refresh: `Ctrl+Shift+R`

### Preview quebrado?
1. Abra o console (F12)
2. Verifique erros JavaScript
3. Certifique-se de que `custom-scripts.js` está carregando

### Logo ainda aparece?
1. Verifique se `custom-scripts.js` está executando
2. Teste no console: `document.querySelectorAll('[class*="Logo"]')`
3. Adicione mais seletores CSS se necessário

---

## 📞 Suporte

- **Documentação Decap CMS:** https://decapcms.org/docs/
- **Guia de Customização:** `CUSTOMIZACAO.md`
- **Issues GitHub:** [Repo do projeto]

---

**Criado com 💜 para o Departamento de Estatística - UnB**
