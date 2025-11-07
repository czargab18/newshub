
// Obtém as funções createClass e h do objeto global window para criar componentes React
const { createClass, h } = window;

/**
 * Componente de Preview para a coleção 'sentindo_ribbon'.
 * Renderiza uma prévia visual de como a faixa de aviso aparecerá.
 */
var RibbonPreview = createClass({
  render: function() {
    // Acessa os dados da entrada atual
    const entry = this.props.entry;
    const message = entry.getIn(['data', 'mensagem']);
    const isActive = entry.getIn(['data', 'ativo']);
    const startDate = entry.getIn(['data', 'date_start']);
    const endDate = entry.getIn(['data', 'date_end']);

    // Estilos para o container principal da prévia (o banner)
    const ribbonStyle = {
      padding: '25px',
      borderRadius: '10px',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      color: 'white',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      boxShadow: '0 10px 25px rgba(0, 0, 0, 0.2)',
      margin: '20px'
    };

    // Estilos para o container do status (indicador + texto)
    const statusContainerStyle = {
        display: 'flex',
        alignItems: 'center',
        marginBottom: '15px'
    };

    // Estilos para o indicador de status (círculo verde/cinza)
    const statusIndicatorStyle = {
      width: '12px',
      height: '12px',
      borderRadius: '50%',
      marginRight: '10px',
      backgroundColor: isActive ? '#28a745' : '#6c757d',
      boxShadow: isActive ? '0 0 12px #28a745' : 'none',
      flexShrink: 0
    };

    // Estilos para o texto do status ("Ativo" / "Inativo")
    const statusTextStyle = {
        fontWeight: '600',
        fontSize: '1em',
        textTransform: 'uppercase',
        letterSpacing: '0.5px'
    };

    // Estilos para a mensagem principal do aviso
    const messageStyle = {
      fontSize: '1.4em',
      fontWeight: 'bold',
      lineHeight: '1.4'
    };
    
    // Estilos para a seção de datas
    const dateStyle = {
        fontSize: '0.9em',
        opacity: 0.85,
        marginTop: '20px',
        borderTop: '1px solid rgba(255, 255, 255, 0.2)',
        paddingTop: '15px'
    };

    // Formata as datas para exibição
    const formattedStartDate = startDate ? new Date(startDate).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }) : 'Imediato';
    const formattedEndDate = endDate ? new Date(endDate).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }) : 'Indefinido';

    // Renderiza a prévia usando a função 'h' (equivalente a React.createElement)
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

// Registra o componente de preview 'RibbonPreview' para a coleção 'sentindo_ribbon'
CMS.registerPreviewTemplate("sentindo_ribbon", RibbonPreview);
