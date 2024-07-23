function alterar() {
    // Definindo categorias de inputs em arrays
    const atributos = ['forca', 'destreza', 'inteligencia', 'determinacao', 'percepcao', 'carisma'];

    const missoes = ['forcaMS', 'destrezaMS', 'inteligenciaMS', 'determinacaoMS', 'percepcaoMS', 'carismaMS'];

    const arma = ['forcaAp', 'destrezaAp', 'inteligenciaAp', 'determinacaoAp', 'percepcaoAp', 'carismaAp',
                  'forcaAs', 'destrezaAs', 'inteligenciaAs', 'determinacaoAs', 'percepcaoAs', 'carismaAs'];

    const conjunto = ['forcaE', 'destrezaE', 'inteligenciaE', 'determinacaoE', 'percepcaoE', 'carismaE',
                      'forcaP', 'destrezaP', 'inteligenciaP', 'determinacaoP', 'percepcaoP', 'carismaP',
                      'forcaL', 'destrezaL', 'inteligenciaL', 'determinacaoL', 'percepcaoL', 'carismaL',
                      'forcaC', 'destrezaC', 'inteligenciaC', 'determinacaoC', 'percepcaoC', 'carismaC',
                      'forcaB', 'destrezaB', 'inteligenciaB', 'determinacaoB', 'percepcaoB', 'carismaB'];

    const acessorios  = ['forcaAn1', 'destrezaAn1', 'inteligenciaAn1', 'determinacaoAn1', 'percepcaoAn1', 'carismaAn1',
                         'forcaAn2', 'destrezaAn2', 'inteligenciaAn2', 'determinacaoAn2', 'percepcaoAn2', 'carismaAn2',
                         'forcaAn3', 'destrezaAn3', 'inteligenciaAn3', 'determinacaoAn3', 'percepcaoAn3', 'carismaAn3',
                         'forcaAn4', 'destrezaAn4', 'inteligenciaAn4', 'determinacaoAn4', 'percepcaoAn4', 'carismaAn4',
                         'forcaBc1', 'destrezaBc1', 'inteligenciaBc1', 'determinacaoBc1', 'percepcaoBc1', 'carismaBr1',
                         'forcaBc2', 'destrezaBc2', 'inteligenciaBc2', 'determinacaoBc2', 'percepcaoBc2', 'carismaBr2',
                         'forcaBr1', 'destrezaBr1', 'inteligenciaBr1', 'determinacaoBr1', 'percepcaoBr1', 'carismaBc1',
                         'forcaBr2', 'destrezaBr2', 'inteligenciaBr2', 'determinacaoBr2', 'percepcaoBr2', 'carismaBc2',
                         'forcaCo', 'destrezaCo', 'inteligenciaCo', 'determinacaoCo', 'percepcaoCo', 'carismaCo',
                         'forcaCa', 'destrezaCa', 'inteligenciaCa', 'determinacaoCa', 'percepcaoCa', 'carismaCa',
                         'forcaCi', 'destrezaCi', 'inteligenciaCi', 'determinacaoCi', 'percepcaoCi', 'carismaCi',];

    const maestria = ['forcaMPR', 'destrezaMPR', 'inteligenciaMPR', 'determinacaoMPR', 'percepcaoMPR', 'carismaMPR',
                      'forcaMPB', 'destrezaMPB', 'inteligenciaMPB', 'determinacaoMPB', 'percepcaoMPB', 'carismaMPB',
                      'forcaMSR', 'destrezaMSR', 'inteligenciaMSR', 'determinacaoMSR', 'percepcaoMSR', 'carismaMSR',
                      'forcaMSB', 'destrezaMSB', 'inteligenciaMSB', 'determinacaoMSB', 'percepcaoMSB', 'carismaMSB',
                      'forcaMUR', 'destrezaMUR', 'inteligenciaMUR', 'determinacaoMUR', 'percepcaoMUR', 'carismaMUR',
                      'forcaMUB', 'destrezaMUB', 'inteligenciaMUB', 'determinacaoMUB', 'percepcaoMUB', 'carismaMUB'];

                  
    const extra = ['forcaBD', 'destrezaBD', 'inteligenciaBD', 'determinacaoBD', 'percepcaoBD', 'carismaBD',
                   'forcaDCF', 'destrezaDCF', 'inteligenciaDCF', 'determinacaoDCF', 'percepcaoDCF', 'carismaDCF',
                   'forcaDCP', 'destrezaDCP', 'inteligenciaDCP', 'determinacaoDCP', 'percepcaoDCP', 'carismaDCP',
                   'forcaG', 'destrezaG', 'inteligenciaG', 'determinacaoG', 'percepcaoG', 'carismaG',
                   'forcaraca', 'destrezaraca', 'inteligenciaraca', 'determinacaoraca', 'percepcaoraca', 'carismaraca',
                   'forcaBF', 'destrezaBF', 'inteligenciaBF', 'determinacaoBF', 'percepcaoBF', 'carismaBF',
                   'forcaBP', 'destrezaBP', 'inteligenciaBP', 'determinacaoBP', 'percepcaoBP', 'carismaBP',
                   'forcaHF', 'destrezaHF', 'inteligenciaHF', 'determinacaoHF', 'percepcaoHF', 'carismaHF',
                   'forcaHP', 'destrezaHP', 'inteligenciaHP', 'determinacaoHP', 'percepcaoHP', 'carismaHP'];

    
    // Objeto para armazenar os valores dos inputs
    const valores = {};

    // Função para iterar e obter os valores dos inputs
    const obterValores = (...arrays) => {
        arrays.forEach((array) => {
            array.forEach((id) => {
                valores[id] = parseFloat(document.getElementById(id).value) || 0;
            });
        });
    };

    // Chamando a função para obter os valores de cada categoria
    obterValores(atributos, missoes, arma, conjunto, acessorios, maestria, extra);
    
    // Enviando os dados para o servidor
    fetch('/atrstatus', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(valores)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Dados recebidos:', data)
        
        document.getElementById('forcat').textContent = `${data.forcat.toLocaleString('pt-BR')}`;
        document.getElementById('destrezat').textContent = `${data.destrezat.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciat').textContent = `${data.inteligenciat.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaot').textContent = `${data.determinacaot.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaot').textContent = `${data.percepcaot.toLocaleString('pt-BR')}`;
        document.getElementById('carismat').textContent = `${data.carismat.toLocaleString('pt-BR')}`;

        document.getElementById('forcaT').textContent = `${data.forcaT.toLocaleString('pt-BR')}`;
        document.getElementById('destrezaT').textContent = `${data.destrezaT.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciaT').textContent = `${data.inteligenciaT.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaoT').textContent = `${data.determinacaoT.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaoT').textContent = `${data.percepcaoT.toLocaleString('pt-BR')}`;
        document.getElementById('carismaT').textContent = `${data.carismaT.toLocaleString('pt-BR')}`;

        document.getElementById('forcaCJ').textContent = `${data.forcaCJ.toLocaleString('pt-BR')}`;
        document.getElementById('destrezaCJ').textContent = `${data.destrezaCJ.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciaCJ').textContent = `${data.inteligenciaCJ.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaoCJ').textContent = `${data.determinacaoCJ.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaoCJ').textContent = `${data.percepcaoCJ.toLocaleString('pt-BR')}`;
        document.getElementById('carismaCJ').textContent = `${data.carismaCJ.toLocaleString('pt-BR')}`;

        document.getElementById('forcaAc').textContent = `${data.forcaAc.toLocaleString('pt-BR')}`;
        document.getElementById('destrezaAc').textContent = `${data.destrezaAc.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciaAc').textContent = `${data.inteligenciaAc.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaoAc').textContent = `${data.determinacaoAc.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaoAc').textContent = `${data.percepcaoAc.toLocaleString('pt-BR')}`;
        document.getElementById('carismaAc').textContent = `${data.carismaAc.toLocaleString('pt-BR')}`;

        document.getElementById('forcaAr').textContent = `${data.forcaAr.toLocaleString('pt-BR')}`;
        document.getElementById('destrezaAr').textContent = `${data.destrezaAr.toLocaleString('pt-BR')}`;
        document.getElementById('inteligenciaAr').textContent = `${data.inteligenciaAr.toLocaleString('pt-BR')}`;
        document.getElementById('determinacaoAr').textContent = `${data.determinacaoAr.toLocaleString('pt-BR')}`;
        document.getElementById('percepcaoAr').textContent = `${data.percepcaoAr.toLocaleString('pt-BR')}`;
        document.getElementById('carismaAr').textContent = `${data.carismaAr.toLocaleString('pt-BR')}`;

        // Constrói a URL com os parâmetros para a próxima página
        const queryString = `
        ?forcaT=${data.forcaT}
        &destrezaT=${data.destrezaT}
        &inteligenciaT=${data.inteligenciaT}
        &determinacaoT=${data.determinacaoT}
        &percepcaoT=${data.percepcaoT}
        &carismaT=${data.carismaT}`;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function redvida(){
    const vidaB = parseFloat(document.getElementById('vidaB').value) || 0; // Declaração da Vida Base
    const vidaE = parseFloat(document.getElementById('vidaE').value) || 0; // Declaração da Vida Extra
    const vidaA = parseFloat(document.getElementById('vidaA').value)/100 || 0; // Declaração da Vida Extra
    const vidaT = parseFloat(document.getElementById('vidaT').value)/100 || 0; // Declaração da Vida Extra
    const dano = parseFloat(document.getElementById('dano').value) || 0;

    const manaB = parseFloat(document.getElementById('manaB').value) || 0;
    const manaE = parseFloat(document.getElementById('manaE').value) || 0;
    const gastoM = parseFloat(document.getElementById('gastoM').value) || 0;

    const vigorB = parseFloat(document.getElementById('vigorB').value) || 0;
    const vigorE = parseFloat(document.getElementById('vigorE').value) || 0;
    const gastoV = parseFloat(document.getElementById('gastoV').value) || 0;


    fetch('/redvida', { // Comunicação com o python
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },  
        body: JSON.stringify({ 
            vidaB: vidaB, vidaE: vidaE, vidaA: vidaA, vidaT: vidaT, dano: dano,
            manaB: manaB, manaE: manaE, gastoM: gastoM,
            vigorB: vigorB, vigorE: vigorE, gastoV: gastoV
        }) // Variaveis que serão jogadas para o Python 
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vidaTo').textContent = `${data.vidaTo.toLocaleString('pt-BR')}`; // Esses aqui são o que joga para o Front, na tela do HTML
        document.getElementById('vidaAt').textContent = `${data.vidaAt.toLocaleString('pt-BR')}`;
        document.getElementById('manaTo').textContent = `${data.manaTo.toLocaleString('pt-BR')}`;
        document.getElementById('manaAt').textContent = `${data.manaAt.toLocaleString('pt-BR')}`;
        document.getElementById('vigorTo').textContent = `${data.vigorTo.toLocaleString('pt-BR')}`;
        document.getElementById('vigorAt').textContent = `${data.vigorAt.toLocaleString('pt-BR')}`;


    })
    .catch(error => {
        console.error('Erro:', error);
    });
    
}