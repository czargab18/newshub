/* ============================================
   CUSTOM SCRIPTS - DEPARTAMENTO DE ESTATÍSTICA
   ============================================ */

// ============================================
// CUSTOMIZAR TELA DE LOGIN
// ============================================
window.addEventListener('DOMContentLoaded', () => {
  const observer = new MutationObserver(() => {
    const logos = document.querySelectorAll('[class*="Logo"], [class*="logo"]');
    logos.forEach(logo => {
      if (logo.tagName === 'IMG' || logo.tagName === 'SVG') {
        logo.style.display = 'none';
      }
    });

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
// FUNÇÕES AUXILIARES
// ============================================
const {
  h,
  createClass
} = window;

// Função para formatar datas para um formato simples
const formatDate = (dateString, options, fallback = 'Data inválida') => {
  if (!dateString) return fallback;
  const date = new Date(dateString);
  if (isNaN(date.getTime())) {
    return fallback;
  }
  return date.toLocaleString('pt-BR', options);
};

/**
 * Formata uma data para o formato "7 de Novembro de 2025, 10h30".
 * @param {string} dateString - A data em formato de string.
 * @returns {string} A data formatada.
 */
const formatarDataCustomizada = (dateString) => {
  if (!dateString) return 'Data não definida';
  const date = new Date(dateString);
  if (isNaN(date.getTime())) {
    return 'Data inválida';
  }

  const day = date.getDate();
  const month = date.toLocaleString('pt-BR', {
    month: 'long'
  });
  const year = date.getFullYear();
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');

  return `${day} de ${month} de ${year}, ${hours}h${minutes}`;
};


// ============================================
// PREVIEW TEMPLATE PARA "CONTEUDO"
// ============================================
const ArticlePreview = ({
  entry,
  widgetFor
}) => {
  const title = entry.getIn(['data', 'title']);
  const subtitle = entry.getIn(['data', 'subtitle']);
  const excerpt = entry.getIn(['data', 'excerpt']);
  const date = entry.getIn(['data', 'date_updated']); // Usando date_updated
  const author = entry.getIn(['data', 'author']) || 'Departamento de Estatística';
  const coverImage = entry.getIn(['data', 'cover_image', 'url']);
  const coverAlt = entry.getIn(['data', 'cover_image', 'alt']);
  const type = entry.getIn(['data', 'type']);

  const formattedDate = formatarDataCustomizada(date);

  return h('div', {
      className: 'cms-preview-content'
    },
    h('h1', {}, title || 'Título do Artigo'),
    subtitle ? h('h2', {}, subtitle) : null,
    h('div', {
        className: 'metadata'
      },
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
    coverImage ? h('img', {
      src: coverImage,
      alt: coverAlt || 'Imagem de capa',
      style: {
        maxWidth: '100%',
        height: 'auto'
      }
    }) : null,
    excerpt ? h('div', {
      className: 'excerpt'
    }, excerpt) : null,
    h('div', {
      className: 'body-content'
    }, widgetFor('body'))
  );
};


// ============================================
// PREVIEW TEMPLATE PARA "SENTINDO_RIBBON"
// ============================================
const RibbonPreview = createClass({
  render: function () {
    const entry = this.props.entry;
    const message = entry.getIn(['data', 'mensagem']);
    const isActive = entry.getIn(['data', 'ativo']);
    const startDate = entry.getIn(['data', 'date_start']);
    const endDate = entry.getIn(['data', 'date_end']);

    const formattedStartDate = formatarDataCustomizada(startDate);
    const formattedEndDate = formatarDataCustomizada(endDate);

    const ribbonStyle = {
      padding: '25px',
      borderRadius: '10px',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      color: 'white',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      boxShadow: '0 10px 25px rgba(0, 0, 0, 0.2)',
      margin: '20px'
    };

    const statusContainerStyle = {
      display: 'flex',
      alignItems: 'center',
      marginBottom: '15px'
    };

    const statusIndicatorStyle = {
      width: '12px',
      height: '12px',
      borderRadius: '50%',
      marginRight: '10px',
      backgroundColor: isActive ? '#28a745' : '#6c757d',
      boxShadow: isActive ? '0 0 12px #28a745' : 'none',
      flexShrink: 0
    };

    const statusTextStyle = {
      fontWeight: '600',
      fontSize: '1em',
      textTransform: 'uppercase',
      letterSpacing: '0.5px'
    };

    const messageStyle = {
      fontSize: '1.4em',
      fontWeight: 'bold',
      lineHeight: '1.4'
    };

    const dateStyle = {
      fontSize: '0.9em',
      opacity: 0.85,
      marginTop: '20px',
      borderTop: '1px solid rgba(255, 255, 255, 0.2)',
      paddingTop: '15px'
    };

    return h('div', {
        style: ribbonStyle
      },
      h('div', {
          style: statusContainerStyle
        },
        h('span', {
          style: statusIndicatorStyle
        }),
        h('span', {
          style: statusTextStyle
        }, isActive ? 'Ativo' : 'Inativo')
      ),
      h('div', {
        style: messageStyle
      }, message || 'Sua mensagem de aviso aparecerá aqui...'),
      h('div', {
          style: dateStyle
        },
        'Início: ' + formattedStartDate,
        h('br'),
        'Fim: ' + formattedEndDate
      )
    );
  }
});

// ============================================
// REGISTRO DOS PREVIEWS
// ============================================
CMS.registerPreviewTemplate('conteudo', ArticlePreview);
CMS.registerPreviewTemplate('sentindo_ribbon', RibbonPreview);