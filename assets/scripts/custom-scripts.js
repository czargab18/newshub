/* ============================================
   CUSTOM SCRIPTS - DEPARTAMENTO DE ESTATÍSTICA
   ============================================ */
function formatarDataCustomizada(dateString) {
  if (!dateString) {
    return "Data inválida";
  }

  // O formato da data no JSON é "DD de Month YYYY HH:mm" com o mês em inglês.
  // Ex: "07 de November 2025 10:21"
  // O new Date() do Javascript não consegue interpretar isso diretamente.
  // Vamos substituir o " de " por um espaço para facilitar o parse.
  const parsableDateString = dateString.replace(' de ', ' ');
  const date = new Date(parsableDateString);

  if (isNaN(date.getTime())) {
    return "Data inválida";
  }

  const dia = date.getDate();
  // Usamos toLocaleString para obter o nome do mês em português.
  const mes = date.toLocaleString('pt-BR', { month: 'long' });
  const ano = date.getFullYear();
  const hora = date.getHours();
  const minutos = date.getMinutes().toString().padStart(2, '0');

  // Colocando a primeira letra do mês em maiúscula
  const mesCapitalizado = mes.charAt(0).toUpperCase() + mes.slice(1);

  return `${dia} de ${mesCapitalizado} de ${ano}, ${hora}h${minutos}`;
}

// Exemplo de uso com a data do seu arquivo JSON
const dataDoJson = "07 de November 2025 10:21";
const dataFormatada = formatarDataCustomizada(dataDoJson);

console.log(dataFormatada); // Saída: 7 de Novembro de 2025, 10h21
// ============================================
// CUSTOMIZAR TELA DE LOGIN
// ============================================
window.addEventListener('DOMContentLoaded', () => {
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

  observer.observe(document.body, { childList: true, subtree: true });
});

// ============================================
// FUNÇÕES AUXILIARES
// ============================================
const { h, createClass } = window;

/**
 * Formata uma string de data para o padrão pt-BR.
 * Lida com o formato "dd de MMMM yyyy" vindo do Decap.
 * @param {string} dateString - A data em formato de string.
 * @param {object} options - Opções para toLocaleString.
 * @param {string} fallback - Valor de retorno se a data for inválida.
 * @returns {string} - A data formatada.
 */
const formatDate = (dateString, options, fallback = 'Data inválida') => {
  if (!dateString) return fallback;

  // Corrige o formato da data "de" para que o new Date() possa interpretar
  const correctedDateString = dateString.replace(/ de /g, ' ');
  const date = new Date(correctedDateString);

  if (isNaN(date.getTime())) {
    return fallback;
  }
  return date.toLocaleString('pt-BR', options);
};


// ============================================
// PREVIEW TEMPLATE PARA "CONTEUDO" (ARTIGOS, NOTÍCIAS, ETC.)
// ============================================
const ArticlePreview = ({ entry, widgetFor, getAsset }) => {
  const title = entry.getIn(['data', 'title']);
  const subtitle = entry.getIn(['data', 'subtitle']);
  const date = entry.getIn(['data', 'date']);
  const author = entry.getIn(['data', 'author']) || 'Departamento de Estatística';
  const coverImage = getAsset(entry.getIn(['data', 'cover_image']));
  const type = entry.getIn(['data', 'type']);

  const formattedDate = formatDate(date, {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }, 'Data não definida');

  return h('div', { className: 'article-preview', style: { fontFamily: 'sans-serif', padding: '20px' } },
    h('div', { className: 'cover-image-container', style: {
      backgroundImage: `url(${coverImage || 'dev-test/admin/image.png'})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      height: '250px',
      borderRadius: '8px',
      marginBottom: '20px',
      display: 'flex',
      alignItems: 'flex-end',
      color: 'white',
      textShadow: '0 2px 4px rgba(0,0,0,0.5)'
    }},
      h('div', { style: { padding: '20px', width: '100%', background: 'linear-gradient(to top, rgba(0,0,0,0.8), transparent)' }},
        h('h1', { style: { margin: '0', fontSize: '2.5em' } }, title || 'Título do Artigo'),
        subtitle ? h('h2', { style: { margin: '0', fontWeight: 'normal', fontSize: '1.5em' } }, subtitle) : null
      )
    ),
    h('div', { className: 'metadata', style: { color: '#555', marginBottom: '20px' } },
      h('span', {}, `${formattedDate} • ${author}`),
      type ? h('span', {
        style: {
          marginLeft: '1rem',
          background: '#e3f2fd',
          padding: '0.2rem 0.5rem',
          borderRadius: '3px',
          fontSize: '0.85rem',
          textTransform: 'uppercase',
          fontWeight: 'bold',
          color: '#0d47a1'
        }
      }, type) : null
    ),
    h('div', { className: 'body-content', style: { lineHeight: '1.6' } }, widgetFor('body'))
  );
};


// ============================================
// PREVIEW TEMPLATE PARA "SENTINDO_RIBBON" (AVISOS)
// ============================================
const RibbonPreview = createClass({
  render: function () {
    const entry = this.props.entry;
    const message = entry.getIn(['data', 'mensagem']);
    const isActive = entry.getIn(['data', 'ativo']);
    const startDate = entry.getIn(['data', 'date_start']);
    const endDate = entry.getIn(['data', 'date_end']);

    const formattedStartDate = formatDate(startDate, { dateStyle: 'short', timeStyle: 'short' }, 'Imediato');
    const formattedEndDate = formatDate(endDate, { dateStyle: 'short', timeStyle: 'short' }, 'Indefinido');

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

    return h('div', { style: ribbonStyle },
      h('div', { style: statusContainerStyle },
        h('span', { style: statusIndicatorStyle }),
        h('span', { style: statusTextStyle }, isActive ? 'Ativo' : 'Inativo')
      ),
      h('div', { style: messageStyle }, message || 'Sua mensagem de aviso aparecerá aqui...'),
      h('div', { style: dateStyle },
        'Início: ' + formattedStartDate,
        h('br'),
        'Fim: ' + formattedEndDate
      )
    );
  }
});

// ============================================
// REGISTRO DOS PREVIEWS NO DECAP CMS
// ============================================
CMS.registerPreviewTemplate('conteudo', ArticlePreview);
CMS.registerPreviewTemplate('sentindo_ribbon', RibbonPreview);