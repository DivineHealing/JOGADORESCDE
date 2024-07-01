function alterar() { // função que ativa quando aperta o botão
    const forca = parseFloat(document.getElementById('forca').value) || 0; // Declaração das variaveis que serão processadas, caso nao tiver, o valor sera zero.
    const destreza = parseFloat(document.getElementById('destreza').value) || 0;
    const inteligencia = parseFloat(document.getElementById('inteligencia').value) || 0;
    const determinacao =  parseFloat(document.getElementById('determinacao').value) || 0;
    const percepcao = parseFloat(document.getElementById('percepcao').value) || 0;
    const carisma = parseFloat(document.getElementById('carisma').value) || 0;

    const forcaE = parseFloat(document.getElementById('forcaE').value) || 0;
    const forcaP = parseFloat(document.getElementById('forcaP').value) || 0;
    const forcaL = parseFloat(document.getElementById('forcaL').value) || 0;
    const forcaC = parseFloat(document.getElementById('forcaC').value) || 0;
    const forcaB = parseFloat(document.getElementById('forcaB').value) || 0;

    const destrezaE = parseFloat(document.getElementById('destrezaE').value) || 0;
    const destrezaP = parseFloat(document.getElementById('destrezaP').value) || 0;
    const destrezaL = parseFloat(document.getElementById('destrezaL').value) || 0;
    const destrezaC = parseFloat(document.getElementById('destrezaC').value) || 0;
    const destrezaB = parseFloat(document.getElementById('destrezaB').value) || 0;

    const inteligenciaE = parseFloat(document.getElementById('inteligenciaE').value) || 0;
    const inteligenciaP = parseFloat(document.getElementById('inteligenciaP').value) || 0;
    const inteligenciaL = parseFloat(document.getElementById('inteligenciaL').value) || 0;
    const inteligenciaC = parseFloat(document.getElementById('inteligenciaC').value) || 0;
    const inteligenciaB = parseFloat(document.getElementById('inteligenciaB').value) || 0;

    const determinacaoE = parseFloat(document.getElementById('determinacaoE').value) || 0;
    const determinacaoP = parseFloat(document.getElementById('determinacaoP').value) || 0;
    const determinacaoL = parseFloat(document.getElementById('determinacaoL').value) || 0;
    const determinacaoC = parseFloat(document.getElementById('determinacaoC').value) || 0;
    const determinacaoB = parseFloat(document.getElementById('determinacaoB').value) || 0;

    const percepcaoE = parseFloat(document.getElementById('percepcaoE').value) || 0;
    const percepcaoP = parseFloat(document.getElementById('percepcaoP').value) || 0;
    const percepcaoL = parseFloat(document.getElementById('percepcaoL').value) || 0;
    const percepcaoC = parseFloat(document.getElementById('percepcaoC').value) || 0;
    const percepcaoB = parseFloat(document.getElementById('percepcaoB').value) || 0;

    const carismaE = parseFloat(document.getElementById('carismaE').value) || 0;
    const carismaP = parseFloat(document.getElementById('carismaP').value) || 0;
    const carismaL = parseFloat(document.getElementById('carismaL').value) || 0;
    const carismaC = parseFloat(document.getElementById('carismaC').value) || 0;
    const carismaB = parseFloat(document.getElementById('carismaB').value) || 0;
    
    fetch('/atrstatus', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            forca: forca, destreza: destreza, inteligencia: inteligencia, determinacao: determinacao, percepcao: percepcao, carisma: carisma,

            forcaE:forcaE, forcaP:forcaP, forcaL:forcaL, forcaC:forcaC, forcaB:forcaB, 
            destrezaE:destrezaE, destrezaP:destrezaP, destrezaL:destrezaL, destrezaC:destrezaC, destrezaB:destrezaB,
            inteligenciaE:inteligenciaE, inteligenciaP:inteligenciaP, inteligenciaL:inteligenciaL, inteligenciaC:inteligenciaC, inteligenciaB:inteligenciaB,
            determinacaoE:determinacaoE, determinacaoP:determinacaoP, determinacaoL:determinacaoL, determinacaoC:determinacaoC, determinacaoB:determinacaoB,
            percepcaoE:percepcaoE, percepcaoP:percepcaoP, percepcaoL:percepcaoL, percepcaoC:percepcaoC, percepcaoB:percepcaoB,
            carismaE:carismaE, carismaP:carismaP, carismaL:carismaL, carismaC:carismaC, carismaB:carismaB
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('forcat').textContent = `${data.forca.toLocaleString('pt-BR')}`;
        document.getElementById('destrezat').textContent = `${data.destreza.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciat').textContent = `${data.inteligencia.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaot').textContent = `${data.determinacao.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaot').textContent = `${data.percepcao.toLocaleString('pt-BR')}`;
        document.getElementById('carismat').textContent = `${data.carisma.toLocaleString('pt-BR')}`;

        document.getElementById('forcaT').textContent = `${data.forcaT.toLocaleString('pt-BR')}`;
        document.getElementById('destrezaT').textContent = `${data.destrezaT.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciaT').textContent = `${data.inteligenciaT.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaoT').textContent = `${data.determinacaoT.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaoT').textContent = `${data.percepcaoT.toLocaleString('pt-BR')}`;
        document.getElementById('carismaT').textContent = `${data.carismaT.toLocaleString('pt-BR')}`;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function redvida(){
    const vida = parseFloat(document.getElementById('vida').value) || 0; // Declaração da Vida
    const mana = parseFloat(document.getElementById('mana').value) || 0;
    const vigor = parseFloat(document.getElementById('vigor').value) || 0;
    const vidaP = parseFloat(document.getElementById('vidaP').value) || 0; // Declaração da Vida
    const manaP = parseFloat(document.getElementById('manaP').value) || 0;
    const vigorP = parseFloat(document.getElementById('vigorP').value) || 0;

    fetch('/redvida', { // Comunicação com o python
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ vida: vida, mana: mana, vigor: vigor,
            vidaP: vidaP, manaP: manaP, vigorP: vigorP,  
        }) // Variaveis que serão jogadas para o Python 
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vidat').textContent = `${data.vidab.toLocaleString('pt-BR')}`; // Esses aqui são o que joga para o Front, na tela do HTML
        document.getElementById('manat').textContent = `${data.manab.toLocaleString('pt-BR')}`;
        document.getElementById('vigort').textContent = `${data.vigorb.toLocaleString('pt-BR')}`;

    })
    .catch(error => {
        console.error('Erro:', error);
    });
}