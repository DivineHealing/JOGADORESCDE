function alterar() { // função que ativa quando aperta o botão
    const forca = parseFloat(document.getElementById('forca').value) || 0; // Declaração das variaveis que serão processadas, caso nao tiver, o valor sera zero.
    const destreza = parseFloat(document.getElementById('destreza').value) || 0;
    const inteligencia = parseFloat(document.getElementById('inteligencia').value) || 0;
    const determinacao =  parseFloat(document.getElementById('determinacao').value) || 0;
    const percepcao = parseFloat(document.getElementById('percepcao').value) || 0;
    const carisma = parseFloat(document.getElementById('carisma').value) || 0;
    const forcaE =parseFloat(document.getElementById('forcaE').value) || 0;
    

    fetch('/atrstatus', { // Comunicação com o python
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ forca: forca, destreza: destreza, inteligencia: inteligencia, forcaE: forcaE, 
            determinacao: determinacao, percepcao: percepcao, carisma: carisma
        }) // Variaveis que serão jogadas para o Python 
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('forcat').textContent = `${data.forca.toLocaleString('pt-BR')}`, // Esses aqui são o que joga para o Front, na tela do HTML
        document.getElementById('destrezat').textContent = `${data.destreza.toLocaleString('pt-BR')}`,
        document.getElementById('inteligenciat').textContent = `${data.inteligencia.toLocaleString('pt-BR')}`,
        document.getElementById('determinacaot').textContent = `${data.determinacao.toLocaleString('pt-BR')}`,
        document.getElementById('percepcaot').textContent = `${data.percepcao.toLocaleString('pt-BR')}`,
        document.getElementById('carismat').textContent = `${data.percepcao.toLocaleString('pt-BR')}`
        ;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}