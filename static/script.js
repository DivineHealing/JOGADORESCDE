function alterar() { // função que ativa quando aperta o botão
    const forca = parseFloat(document.getElementById('forca').value) || 0; // Declaração das variaveis que serão processadas, caso nao tiver, o valor sera zero.
    const destreza = parseFloat(document.getElementById('destreza').value) || 0;
    const inteligencia = parseFloat(document.getElementById('inteligencia').value) || 0;
    const determinacao =  parseFloat(document.getElementById('determinacao').value) || 0;
    const percepcao = parseFloat(document.getElementById('percepcao').value) || 0;
    const carisma = parseFloat(document.getElementById('carisma').value) || 0;

    //MAESTRIAS
    const forcaMT = parseFloat(document.getElementById('forcaMT').value) || 0
    const destrezaMT = parseFloat(document.getElementById('destrezaMT').value) || 0
    const inteligenciaMT = parseFloat(document.getElementById('inteligenciaMT').value) || 0
    const determinacaoMT =  parseFloat(document.getElementById('determinacaoMT').value) || 0
    const percepcaoMT = parseFloat(document.getElementById('percepcaoMT').value) || 0
    const carismaMT = parseFloat(document.getElementById('carismaMT').value) || 0

    //MISSÕES
    const forcaMS = parseFloat(document.getElementById('forcaMS').value) || 0
    const destrezaMS = parseFloat(document.getElementById('destrezaMS').value) || 0
    const inteligenciaMS = parseFloat(document.getElementById('inteligenciaMS').value) || 0
    const determinacaoMS =  parseFloat(document.getElementById('determinacaoMS').value) || 0
    const percepcaoMS = parseFloat(document.getElementById('percepcaoMS').value) || 0
    const carismaMS = parseFloat(document.getElementById('carismaMS').value) || 0

    // ARMA
    const forcaAp = parseFloat(document.getElementById('forcaAp').value) || 0;
    const forcaAs = parseFloat(document.getElementById('forcaAs').value) || 0;

    const destrezaAp = parseFloat(document.getElementById('destrezaAp').value) || 0;
    const destrezaAs = parseFloat(document.getElementById('destrezaAs').value) || 0;

    const inteligenciaAp = parseFloat(document.getElementById('inteligenciaAp').value) || 0;
    const inteligenciaAs = parseFloat(document.getElementById('inteligenciaAs').value) || 0;

    const determinacaoAp = parseFloat(document.getElementById('determinacaoAp').value) || 0;
    const determinacaoAs = parseFloat(document.getElementById('determinacaoAs').value) || 0;

    const percepcaoAp = parseFloat(document.getElementById('percepcaoAp').value) || 0;
    const percepcaoAs = parseFloat(document.getElementById('percepcaoAs').value) || 0;

    const carismaAp = parseFloat(document.getElementById('carismaAp').value) || 0;
    const carismaAs = parseFloat(document.getElementById('carismaAs').value) || 0;

    // CONJUNTO
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

    // ACESSORIOS
    const forcaAn1 = parseFloat(document.getElementById('forcaAn1').value) || 0;
    const forcaAn2 = parseFloat(document.getElementById('forcaAn2').value) || 0;
    const forcaAn3 = parseFloat(document.getElementById('forcaAn3').value) || 0;
    const forcaAn4 = parseFloat(document.getElementById('forcaAn4').value) || 0;
    const forcaBc1 = parseFloat(document.getElementById('forcaBc1').value) || 0;
    const forcaBc2 = parseFloat(document.getElementById('forcaBc2').value) || 0;
    const forcaBr1 = parseFloat(document.getElementById('forcaBr1').value) || 0;
    const forcaBr2 = parseFloat(document.getElementById('forcaBr2').value) || 0;
    const forcaCo = parseFloat(document.getElementById('forcaCo').value) || 0;
    const forcaCa = parseFloat(document.getElementById('forcaCa').value) || 0;
    const forcaCi = parseFloat(document.getElementById('forcaCi').value) || 0;

    const destrezaAn1 = parseFloat(document.getElementById('destrezaAn1').value) || 0;
    const destrezaAn2 = parseFloat(document.getElementById('destrezaAn2').value) || 0;
    const destrezaAn3 = parseFloat(document.getElementById('destrezaAn3').value) || 0;
    const destrezaAn4 = parseFloat(document.getElementById('destrezaAn4').value) || 0;
    const destrezaBc1 = parseFloat(document.getElementById('destrezaBc1').value) || 0;
    const destrezaBc2 = parseFloat(document.getElementById('destrezaBc2').value) || 0;
    const destrezaBr1 = parseFloat(document.getElementById('destrezaBr1').value) || 0;
    const destrezaBr2 = parseFloat(document.getElementById('destrezaBr2').value) || 0;
    const destrezaCo = parseFloat(document.getElementById('destrezaCo').value) || 0;
    const destrezaCa = parseFloat(document.getElementById('destrezaCa').value) || 0;
    const destrezaCi = parseFloat(document.getElementById('destrezaCi').value) || 0;

    const inteligenciaAn1 = parseFloat(document.getElementById('inteligenciaAn1').value) || 0;
    const inteligenciaAn2 = parseFloat(document.getElementById('inteligenciaAn2').value) || 0;
    const inteligenciaAn3 = parseFloat(document.getElementById('inteligenciaAn3').value) || 0;
    const inteligenciaAn4 = parseFloat(document.getElementById('inteligenciaAn4').value) || 0;
    const inteligenciaBc1 = parseFloat(document.getElementById('inteligenciaBc1').value) || 0;
    const inteligenciaBc2 = parseFloat(document.getElementById('inteligenciaBc2').value) || 0;
    const inteligenciaBr1 = parseFloat(document.getElementById('inteligenciaBr1').value) || 0;
    const inteligenciaBr2 = parseFloat(document.getElementById('inteligenciaBr2').value) || 0;
    const inteligenciaCo = parseFloat(document.getElementById('inteligenciaCo').value) || 0;
    const inteligenciaCa = parseFloat(document.getElementById('inteligenciaCa').value) || 0;
    const inteligenciaCi = parseFloat(document.getElementById('inteligenciaCi').value) || 0;

    const determinacaoAn1 = parseFloat(document.getElementById('determinacaoAn1').value) || 0;
    const determinacaoAn2 = parseFloat(document.getElementById('determinacaoAn2').value) || 0;
    const determinacaoAn3 = parseFloat(document.getElementById('determinacaoAn3').value) || 0;
    const determinacaoAn4 = parseFloat(document.getElementById('determinacaoAn4').value) || 0;
    const determinacaoBc1 = parseFloat(document.getElementById('determinacaoBc1').value) || 0;
    const determinacaoBc2 = parseFloat(document.getElementById('determinacaoBc2').value) || 0;
    const determinacaoBr1 = parseFloat(document.getElementById('determinacaoBr1').value) || 0;
    const determinacaoBr2 = parseFloat(document.getElementById('determinacaoBr2').value) || 0;
    const determinacaoCo = parseFloat(document.getElementById('determinacaoCo').value) || 0;
    const determinacaoCa = parseFloat(document.getElementById('determinacaoCa').value) || 0;
    const determinacaoCi = parseFloat(document.getElementById('determinacaoCi').value) || 0;

    const percepcaoAn1 = parseFloat(document.getElementById('percepcaoAn1').value) || 0;
    const percepcaoAn2 = parseFloat(document.getElementById('percepcaoAn2').value) || 0;
    const percepcaoAn3 = parseFloat(document.getElementById('percepcaoAn3').value) || 0;
    const percepcaoAn4 = parseFloat(document.getElementById('percepcaoAn4').value) || 0;
    const percepcaoBc1 = parseFloat(document.getElementById('percepcaoBc1').value) || 0;
    const percepcaoBc2 = parseFloat(document.getElementById('percepcaoBc2').value) || 0;
    const percepcaoBr1 = parseFloat(document.getElementById('percepcaoBr1').value) || 0;
    const percepcaoBr2 = parseFloat(document.getElementById('percepcaoBr2').value) || 0;
    const percepcaoCo = parseFloat(document.getElementById('percepcaoCo').value) || 0;
    const percepcaoCa = parseFloat(document.getElementById('percepcaoCa').value) || 0;
    const percepcaoCi = parseFloat(document.getElementById('percepcaoCi').value) || 0;

    const carismaAn1 = parseFloat(document.getElementById('carismaAn1').value) || 0;
    const carismaAn2 = parseFloat(document.getElementById('carismaAn2').value) || 0;
    const carismaAn3 = parseFloat(document.getElementById('carismaAn3').value) || 0;
    const carismaAn4 = parseFloat(document.getElementById('carismaAn4').value) || 0;
    const carismaBc1 = parseFloat(document.getElementById('carismaBc1').value) || 0;
    const carismaBc2 = parseFloat(document.getElementById('carismaBc2').value) || 0;
    const carismaBr1 = parseFloat(document.getElementById('carismaBr1').value) || 0;
    const carismaBr2 = parseFloat(document.getElementById('carismaBr2').value) || 0;
    const carismaCo = parseFloat(document.getElementById('carismaCo').value) || 0;
    const carismaCi = parseFloat(document.getElementById('carismaCi').value) || 0;
    const carismaCa = parseFloat(document.getElementById('carismaCa').value) || 0;

    
    fetch('/atrstatus', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            forca: forca, destreza: destreza, inteligencia: inteligencia, determinacao: determinacao, percepcao: percepcao, carisma: carisma,

            forcaMT:forcaMT, destrezaMT:destrezaMT, inteligenciaMT:inteligenciaMT, determinacaoMT:determinacaoMT, percepcaoMT:percepcaoMT, carismaMT:carismaMT,
            
            forcaMS:forcaMS, destrezaMS:destrezaMS, inteligenciaMS:inteligenciaMS, determinacaoMS:determinacaoMS, percepcaoMS:percepcaoMS, carismaMS:carismaMS,

            forcaAp:forcaAp, forcaAs:forcaAs, destrezaAp:destrezaAp, destrezaAs:destrezaAs, inteligenciaAp:inteligenciaAp, inteligenciaAs:inteligenciaAs,
            determinacaoAp:determinacaoAp, determinacaoAs:determinacaoAs, percepcaoAp:percepcaoAp, percepcaoAs:percepcaoAs, carismaAp:carismaAp, carismaAs:carismaAs,

            forcaE:forcaE, forcaP:forcaP, forcaL:forcaL, forcaC:forcaC, forcaB:forcaB, 
            destrezaE:destrezaE, destrezaP:destrezaP, destrezaL:destrezaL, destrezaC:destrezaC, destrezaB:destrezaB,
            inteligenciaE:inteligenciaE, inteligenciaP:inteligenciaP, inteligenciaL:inteligenciaL, inteligenciaC:inteligenciaC, inteligenciaB:inteligenciaB,
            determinacaoE:determinacaoE, determinacaoP:determinacaoP, determinacaoL:determinacaoL, determinacaoC:determinacaoC, determinacaoB:determinacaoB,
            percepcaoE:percepcaoE, percepcaoP:percepcaoP, percepcaoL:percepcaoL, percepcaoC:percepcaoC, percepcaoB:percepcaoB,
            carismaE:carismaE, carismaP:carismaP, carismaL:carismaL, carismaC:carismaC, carismaB:carismaB,

            forcaAn1:forcaAn1, forcaAn2:forcaAn2, forcaAn3:forcaAn3, forcaAn4:forcaAn4, forcaBc1:forcaBc1, forcaBc2:forcaBc2, forcaBr1:forcaBr1, forcaBr2:forcaBr2, forcaCo:forcaCo, forcaCa:forcaCa, forcaCi:forcaCi,
            destrezaAn1:destrezaAn1, destrezaAn2:destrezaAn2, destrezaAn3:destrezaAn3, destrezaAn4:destrezaAn4, destrezaBc1:destrezaBc1, destrezaBc2:destrezaBc2, destrezaBr1:destrezaBr1, destrezaBr2:destrezaBr2, destrezaCo:destrezaCo, destrezaCa:destrezaCa, destrezaCi:destrezaCi,
            inteligenciaAn1:inteligenciaAn1, inteligenciaAn2:inteligenciaAn2, inteligenciaAn3:inteligenciaAn3, inteligenciaAn4:inteligenciaAn4, inteligenciaBc1:inteligenciaBc1, inteligenciaBc2:inteligenciaBc2, inteligenciaBr1:inteligenciaBr1, inteligenciaBr2:inteligenciaBr2, inteligenciaCo:inteligenciaCo, inteligenciaCa:inteligenciaCa, inteligenciaCi:inteligenciaCi,
            determinacaoAn1:determinacaoAn1, determinacaoAn2:determinacaoAn2, determinacaoAn3:determinacaoAn3, determinacaoAn4:determinacaoAn4, determinacaoBc1:determinacaoBc1, determinacaoBc2:determinacaoBc2, determinacaoBr1:determinacaoBr1, determinacaoBr2:determinacaoBr2, determinacaoCo:determinacaoCo, determinacaoCa:determinacaoCa, determinacaoCi:determinacaoCi,
            percepcaoAn1:percepcaoAn1, percepcaoAn2:percepcaoAn2, percepcaoAn3:percepcaoAn3, percepcaoAn4:percepcaoAn4, percepcaoBc1:percepcaoBc1, percepcaoBc2:percepcaoBc2, percepcaoBr1:percepcaoBr1, percepcaoBr2:percepcaoBr2, percepcaoCo:percepcaoCo, percepcaoCa:percepcaoCa, percepcaoCi:percepcaoCi,
            carismaAn1:carismaAn1, carismaAn2:carismaAn2, carismaAn3:carismaAn3, carismaAn4:carismaAn4, carismaBc1:carismaBc1, carismaBc2:carismaBc2, carismaBr1:carismaBr1, carismaBr2:carismaBr2, carismaCo:carismaCo, carismaCi:carismaCi, carismaCa:carismaCa


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

        


    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

function redvida(){
    const vidaB = parseFloat(document.getElementById('vidaB').value) || 0; // Declaração da Vida Base
    const manaB = parseFloat(document.getElementById('manaB').value) || 0;
    const vigorB = parseFloat(document.getElementById('vigorB').value) || 0;
    const vidaE = parseFloat(document.getElementById('vidaE').value) || 0; // Declaração da Vida Extra
    const manaE = parseFloat(document.getElementById('manaE').value) || 0;
    const vigorE = parseFloat(document.getElementById('vigorE').value) || 0;
    const vidaM = parseFloat(document.getElementById('vidaE').value)/100 || 0; // Declaração da Vida Extra
    const manaM = parseFloat(document.getElementById('manaE').value)/100 || 0;
    const vigorM = parseFloat(document.getElementById('vigorE').value)/100 || 0;
    const vidaTo = parseFloat(document.getElementById('vidaTo')) || 0;
    const manaTo = parseFloat(document.getElementById('vidaTo')) || 0;
    const vigorTo = parseFloat(document.getElementById('vidaTo')) || 0;
    const dano = parseFloat(document.getElementById('dano')) || 0;
    const gastoM = parseFloat(document.getElementById('gastoM')) || 0;
    const gastoV = parseFloat(document.getElementById('gastoV')) || 0;


    fetch('/redvida', { // Comunicação com o python
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },  
        body: JSON.stringify({ 
            vidaE: vidaE, manaE: manaE, vigorE: vigorE,
            vidaB: vidaB, manaB: manaB, vigorB: vigorB,  
            vidaM: vidaM, manaM: manaM, vigorM: vigorM,  
            vidaTo: vidaTo, manaTo: manaTo, vigorTo: vigorTo,  
            dano: dano, gastoM: gastoM, gastoV:gastoV
        }) // Variaveis que serão jogadas para o Python 
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vidaTo').textContent = `${data.vidaTo.toLocaleString('pt-BR')}`; // Esses aqui são o que joga para o Front, na tela do HTML
        document.getElementById('vidaAt').textContent = `${data.vidaTo.toLocaleString('pt-BR')}`;
        document.getElementById('manaTo').textContent = `${data.manaTo.toLocaleString('pt-BR')}`;
        document.getElementById('manaAt').textContent = `${data.manaTo.toLocaleString('pt-BR')}`;
        document.getElementById('vigorTo').textContent = `${data.vigorTo.toLocaleString('pt-BR')}`;
        document.getElementById('vigorAt').textContent = `${data.vigorTo.toLocaleString('pt-BR')}`;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}