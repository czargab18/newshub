/* ============================================
   CUSTOM SCRIPTS - DEPARTAMENTO DE ESTATÍSTICA
   ============================================ */

// ============================================
// CUSTOMIZAR TELA DE LOGIN
// ============================================
window.addEventListener('DOMContentLoaded', () => {
  // Observar mudanças no DOM para aplicar customizações
  const observer = new MutationObserver(() => {
    // Ocultar logo do Decap CMS
    const logos = document.querySelectorAll('[class*="Logo"], [class*="logo"]');
    logos.forEach(logo => {
      if (logo.tagName === 'IMG' || logo.tagName === 'SVG') {
        logo.style.display = 'none';
      }
    });
    
    // Customizar textos
    const heading = document.querySelector('h1');
    if (heading && heading.textContent.includes('Decap')) {
      heading.textContent = 'Sistema de Gerenciamento de Conteúdo';
    }
  });
  
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
});

// ============================================
// PREVIEW TEMPLATE CUSTOMIZADO
// ============================================
const { h } = window;

// Preview Component
const ArticlePreview = ({ entry, widgetFor, getAsset }) => {
  const title = entry.getIn(['data', 'title']);
  const subtitle = entry.getIn(['data', 'subtitle']);
  const excerpt = entry.getIn(['data', 'excerpt']);
  const date = entry.getIn(['data', 'date_format']);
  const author = entry.getIn(['data', 'author']) || 'Departamento de Estatística';
  const coverImage = entry.getIn(['data', 'cover_image', 'url']);
  const coverAlt = entry.getIn(['data', 'cover_image', 'alt']);
  const type = entry.getIn(['data', 'type']);
  
  // Formatar data
  let formattedDate = 'Data não definida';
  if (date) {
    try {
      const dateObj = new Date(date);
      formattedDate = dateObj.toLocaleDateString('pt-BR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch (e) {
      formattedDate = date;
    }
  }
  
  return h('div', { className: 'cms-preview-content' },
    // Título
    h('h1', {}, title || 'Título do Artigo'),
    
    // Subtítulo
    subtitle ? h('h2', {}, subtitle) : null,
    
    // Metadata
    h('div', { className: 'metadata' },
      h('span', {}, `${formattedDate} • ${author}`),
      type ? h('span', {
        style: {
          marginLeft: '1rem',
          background: '#e3f2fd',
          padding: '0.2rem 0.5rem',
          borderRadius: '3px',
          fontSize: '0.85rem',
          textTransform: 'uppercase'
        }
      }, type) : null
    ),
    
    // Imagem de capa
    coverImage ? h('img', {
      src: coverImage,
      alt: coverAlt || 'Imagem de capa',
      style: { maxWidth: '100%', height: 'auto' }
    }) : null,
    
    // Excerto
    excerpt ? h('div', { className: 'excerpt' }, excerpt) : null,
    
    // Corpo do artigo (Markdown renderizado)
    h('div', { className: 'body-content' }, widgetFor('body'))
  );
};

// Registrar o preview template
CMS.registerPreviewTemplate('conteudo', ArticlePreview);
