function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

const deleter = document.getElementById("deleter");

function validarNome() {
    const input = document.getElementById("impDel");
    const select = document.getElementById("personagem_select");
    const personagemId = select.value; // Pega o ID do personagem do <option> selecionado
    const selectedOption = select.options[select.selectedIndex]; // Pega o elemento <option>
    const personagemNome = selectedOption.text; // Pega o nome para confirmação
    deleter.style.display = "none";
    if (personagemNome == input.value){
        deleter.style.display = "";
    }    

    //var personagem = select.value;
    console.log(personagemNome)
}

const atributos = [
    { nome: "vida", containerId:"vida"},
    { nome: "mana", containerId:"mana"},
    { nome: "vigor", containerId:"vigor"},
    { nome: "regenVida", containerId:"regenVida_container"},
    { nome: "regenMana", containerId:"regenMana_container"},
    { nome: "regenVigor", containerId:"regenVigor_container"},

    { nome: "forca", containerId:"forca_container", bonusElementId: "forcaBonus" },
    { nome: "destreza", containerId:"destreza_container", bonusElementId: "destrezaBonus"},
    { nome: "inteligencia", containerId:"inteligencia_container", bonusElementId: "inteligenciaBonus"},
    { nome: "determinacao", containerId:"determinacao_container", bonusElementId: "determinacaoBonus"},
    { nome: "perspicacia", containerId:"perspicacia_container", bonusElementId: "perspicaciaBonus"},
    { nome: "carisma", containerId:"carisma_container", bonusElementId: "carismaBonus"},

    { nome: "esmagamento", containerId: "esmagamento_container"},
    { nome: "penExtra", containerId: "penExtra_container"},
    { nome: "danoFinal", containerId: "danoFinal_container"},
    { nome: "espiritualFixo", containerId: "espiritualFixo_container"},
    { nome: "espiritualPerc", containerId: "espiritualPerc_container"},

    { nome: "defesaFixaEspiritual", containerId: "defesaFixaEspiritual_container"},
    { nome: "reducaoEspiritual", containerId: "reducaoEspiritual_container" },
    { nome: "reducao", containerId: "reducao_container"},
];

let algumAtributoInvalido = false; // Flag para verificar se algum atributo é inválido

function atualizarTela() {
    for (const atributo of atributos) {
        // Só continua se o container realmente existe
        if (document.getElementById(atributo.containerId)) {
            const valor = formatarAtributo(atributo);
            exibirOuOcultarAtributo(atributo, valor);
        }
    }
}

// FUNÇÃO PARA FORMATAR OS NUMEROS MILHARES
function formatarAtributo(atributo) {
    const element = document.getElementById(atributo.nome);
    const bonusElement = document.getElementById(atributo.bonusElementId);

    if (!element) {
        console.warn(`Elemento '${atributo.nome}' não encontrado.`);
        return null; // Retorna null se o elemento não for encontrado
    }

    let valorTexto = element.innerText; // Obtém o texto do elemento
    
    valorTexto = valorTexto.replace(/\./g, ''); // Remove todos os pontos (separadores de milhar)
    let valor = parseFloat(valorTexto);

    if (isNaN(valor) || valor < 0) {
        console.warn(`Valor inválido para '${atributo.nome}'. Definindo como 0.`);
        console.log(valor)
        return null; // Retorna null se o valor for inválido
    }

    if (bonusElement) {
        let maior = 0
        if (bonusElement > maior) { maior == bonusElement.length };
        // Calcula o bônus e formata
        let bonus = valor / 100;
        bonus = bonus.toFixed(2);
        bonus = Math.trunc(bonus); // Remove as casas decimais (arredonda para baixo)
        bonus = "— "+' +'+bonus; // Adiciona o sinal de mais

        bonusElement.innerText = bonus; // Exibe o bônus
    }

    return valor; // Retorna o valor formatado
}

// FUNÇÃO PARA OCULTAR OS DADOS ZERADOS
function exibirOuOcultarAtributo(atributo) {
    const element = document.getElementById(atributo.nome);
    const containerElement = document.getElementById(atributo.containerId);
    

    if (!element) {
        console.warn(`Elemento '${atributo.nome}' não encontrado.`);
        return;
    }

    let valorTexto = element.innerText;

    // Remove separadores de milhar e espaços em branco
    valorTexto = valorTexto.replace(/\./g, '')  // Remove pontos (ex: 1.000 -> 1000)
                       .replace(/,/g, '.')   // Troca vírgula por ponto (ex: "0,00" -> "0.00")
                       .trim();

    // Converte para número se for um número, senão mantém como string
    let valor;
    if (!isNaN(parseFloat(valorTexto)) && isFinite(valorTexto)) {
        valor = parseFloat(valorTexto); // Converte para número
    } else {
        valor = valorTexto; // Mantém como string
    }
    // Verifica se o valor é "vazio" (zero para números, string vazia ou null)
    let vazio = (valor === null || valor === undefined) || // Checa null/undefined primeiro
                (typeof valor === 'number' && (valor === 0 || isNaN(valor))) || // Checa 0 ou NaN
                (typeof valor === 'string' && valor.trim() === "");

    if (!containerElement) {
        console.error(`Container '${atributo.containerId}' não encontrado.`);
        return;
    }
    if (vazio && atributo.nome != "forca" && atributo.nome != "destreza" && atributo.nome != "inteligencia" && atributo.nome != "determinacao" && atributo.nome != "perspicacia" && atributo.nome != "carisma") {
        containerElement.style.display = 'none';
    } else {
        containerElement.style.display = 'block';
    }
}

function atualizarTela() {
    for (const atributo of atributos) {
        const valor = formatarAtributo(atributo); // Formata o atributo
        exibirOuOcultarAtributo(atributo, valor); // Exibe ou oculta o container
    }
}
// FUNÇÃO DE ATUALIZAR A TELA - ATUALIZAR DADOS PUXADOS DO BANCO
document.addEventListener("DOMContentLoaded", function () {
    atualizarTela();
});

    // FUNÇÃO DE BUFF
document.addEventListener('click', function (event) {
    if (!event.target.matches('.buff-button')) return;

    event.preventDefault();

    const field = event.target.dataset.field;
    const baseSpan = document.getElementById(field);
    const autoBuffInput = document.getElementById(`${field}BuffInput`);
    const externalBuffInput = document.getElementById(`${field}ExternalBuffInput`);
    const finalBuffSpan = document.getElementById(`${field}FinalBuffed`);

    if (!baseSpan || !autoBuffInput || !externalBuffInput || !finalBuffSpan) return;

    const baseValue = parseInt(baseSpan.textContent.replace(/\./g, '')) || 0;

    baseSpan.classList.add('hidden');
    autoBuffInput.classList.remove('hidden');
    externalBuffInput.classList.remove('hidden');
    finalBuffSpan.classList.add('hidden');
    autoBuffInput.focus();

    function calcularFinalBuff() {
        const autoPercent = parseFloat(autoBuffInput.value) || 0;
        const externalPercent = parseFloat(externalBuffInput.value) || 0;

        let total = baseValue;

        if (autoPercent && externalPercent) {
            if (autoPercent > 0 || externalPercent > 0) {
                total += Math.floor(baseValue * (autoPercent / 100));
                total += Math.floor(baseValue * (externalPercent / 200));
            } else {
                total += Math.floor(baseValue * (autoPercent / 100));
                total += Math.floor(baseValue * (externalPercent / 100));
            }
        } else if (autoPercent) {
            total += Math.floor(baseValue * (autoPercent / 100));
        } else if (externalPercent) {
            total += Math.floor(baseValue * (externalPercent / 100));
        }

        finalBuffSpan.textContent = total.toLocaleString('pt-BR');
        finalBuffSpan.classList.remove('hidden');
        autoBuffInput.classList.add('hidden');
        externalBuffInput.classList.add('hidden');
        baseSpan.classList.remove('hidden');
    }

    function calcularFinalBuffFixo() {
        const autoPercent = parseInt(autoBuffInput.value) || 0;
        const externalPercent = parseInt(externalBuffInput.value) || 0;

        let total = baseValue;

        if (autoPercent && externalPercent) {
            if (autoPercent > 0 || externalPercent > 0) {
                total += autoPercent;
                total += Math.floor(externalPercent/2);
            }
        } else if (autoPercent) {
            total += autoPercent; 
        } else if (externalPercent) {
            total += externalPercent;
        }

        finalBuffSpan.textContent = total.toLocaleString('pt-BR');
        finalBuffSpan.classList.remove('hidden');
        autoBuffInput.classList.add('hidden');
        externalBuffInput.classList.add('hidden');
        baseSpan.classList.remove('hidden');
    }

    function calcularFinalBuffAryah() {
        const autoPercent = parseFloat(autoBuffInput.value) || 0;
        const externalPercent = parseInt(externalBuffInput.value) || 0;
        console.log(autoPercent)
        console.log(externalPercent)
        console.log(baseValue)

        let total = baseValue;

        if (autoPercent && externalPercent) {
            if (autoPercent > 0 || externalPercent > 0) {
                total += Math.floor(baseValue * (autoPercent / 100));
                total += Math.floor(externalPercent / 2);
            } else {
                total += Math.floor(baseValue * (autoPercent / 100));
                total += Math.floor(externalPercent / 2);
            }
        } else if (autoPercent) {
            total += Math.floor(baseValue * (autoPercent / 100));
        } else if (externalPercent) {
            total += externalPercent;
        }

        finalBuffSpan.textContent = total.toLocaleString('pt-BR');
        finalBuffSpan.classList.remove('hidden');
        autoBuffInput.classList.add('hidden');
        externalBuffInput.classList.add('hidden');
        baseSpan.classList.remove('hidden');
    }

    // Limpa handlers antigos (para evitar múltiplos)
    autoBuffInput.onkeydown = null;
    externalBuffInput.onkeydown = null;

    autoBuffInput.onkeydown = function (e) {
    if (e.key === 'Enter') {
        calcularFinalBuff();
        console.log("Percentual")
    } else if (e.key === 'F') {
        calcularFinalBuffFixo();
        console.log('Fixo')        
    } else if (e.key === 'A') {
            calcularFinalBuffAryah();
    }
};

    externalBuffInput.onkeydown = function (e) {
        if (e.key === 'Enter') {
            calcularFinalBuff();
        } else if (e.key === 'F') {
            calcularFinalBuffFixo();
        } else if (e.key === 'A') {
            calcularFinalBuffAryah();
        }
};

});




const cadastroNovo = document.getElementById("cadastrarNovo");
const deletar = document.getElementById("deletar");
const selecao = document.getElementById("personagem_select");
const selecaoLb = document.getElementById("selectLabel");

const novoPersonagem = document.getElementById("novoPersonagem")

const btnCad = document.getElementById("btnCad")
const btnDel = document.getElementById("btnDel")
const btnSalvar = document.getElementById("btnSalvar")

btnCad.addEventListener('click', function(){
    cadastroNovo.style.display = "block";
    selecao.style.display = "none";
    btnCad.style.display = "none";
    btnDel.style.display = "none";
    selecaoLb.style.display = "none";
});

btnDel.addEventListener('click', function(){
    deletar.style.display = "block";
    selecao.style.display = "none";
    btnCad.style.display = "none";
    selecaoLb.style.display = "none";
    btnDel.style.display = "none";
});

/* Layout para botão

const btnCad = document.getElementById("btnCad")
btnCad.addEventListener('click', function(){
    console.log("Teste")
});

*/

document.addEventListener('DOMContentLoaded', function() {
    // 1. Obter os dados formatados das habilidades
    const habilidadesDataElement = document.getElementById('all-habilidades-data');
    let allHabilidadesData = {};
    let dataArray = []; // INICIALIZA COMO ARRAY VAZIO POR PADRÃO

    if (habilidadesDataElement && habilidadesDataElement.textContent) {
        try {
            const parsedData = JSON.parse(habilidadesDataElement.textContent);

            // *** VERIFICAÇÃO CRÍTICA ***
            // Checa se o resultado do parse é realmente um array
            if (Array.isArray(parsedData)) {
                dataArray = parsedData; // Usa o array parseado
            } else {
                 // Se não for array (pode ser null, objeto, etc.), mantém dataArray como []
                 console.warn("Os dados parseados de 'all-habilidades-data' não são um array. Tratando como vazio.", parsedData);
            }

        } catch (e) {
            console.error("Erro ao parsear dados das habilidades:", e);
            // Mantém dataArray como [] em caso de erro de parse
        }
    } else {
        console.warn("Elemento 'all-habilidades-data' ou seu conteúdo não encontrado. Tratando como vazio.");
        // Mantém dataArray como []
    }

    // Converte o array (possivelmente vazio) em um objeto/map
    dataArray.forEach(hab => { // Agora seguro usar forEach
        allHabilidadesData[hab.id] = hab;
    });


    const titulos = document.querySelectorAll('.habilidade-titulo');
    const allDetalhesDivs = document.querySelectorAll('.habilidade-detalhes');

    // --- O resto do seu código continua aqui ---
    // (A lógica de adicionar listeners e popular os detalhes)
    // ...

     titulos.forEach(titulo => {
        const slotId = titulo.dataset.slotId;
        const detalhesDiv = document.querySelector(`.habilidade-detalhes[data-details-for="${slotId}"]`);

        if (!detalhesDiv) {
            console.warn(`Div de detalhes não encontrado para slot ID: ${slotId}`);
            return;
        }

        titulo.addEventListener('click', (event) => {
            event.stopPropagation();

            const isCurrentlyVisible = detalhesDiv.classList.contains('visible');

            allDetalhesDivs.forEach(div => {
                if (div !== detalhesDiv) {
                    div.classList.remove('visible');
                }
            });

            if (!isCurrentlyVisible) {
                const habilidadeData = allHabilidadesData[slotId];
                if (!habilidadeData || !habilidadeData.niveis) {
                    detalhesDiv.innerHTML = '<p>Detalhes não disponíveis.</p>';
                    detalhesDiv.classList.add('visible');
                    return;
                }

                detalhesDiv.innerHTML = ''; // Limpa conteúdo anterior

                habilidadeData.niveis.forEach(nivelData => {
                    const nivelWrapper = document.createElement('div');
                    nivelWrapper.classList.add('nivel-wrapper');

                    const nivelTitulo = document.createElement('div');
                    nivelTitulo.classList.add('nivel-titulo');
                    nivelTitulo.innerHTML = `<strong>Nível ${nivelData.nivel}</strong>`;

                    const nivelDetalhes = document.createElement('div');
                    nivelDetalhes.classList.add('nivel-detalhes');

                    nivelDetalhes.innerHTML = `
                        ${nivelData.custo ? `<p><strong style="color: red;">Custo:</strong> ${nivelData.custo}</p>` : ''}
                        ${nivelData.tipo ? `<p><strong style="color: red;">Tipo:</strong> ${nivelData.tipo}</p>` : ''}
                        ${nivelData.descricao ? `
                            <p><strong style="color: red;">Descrição:</strong></p>
                            <div style="font-style: italic;">${nivelData.descricao}</div>
                        ` : ''}
                    `;

                    nivelTitulo.addEventListener('click', () => {
                        nivelDetalhes.classList.toggle('visible');
                        nivelTitulo.classList.toggle('active');
                    });

                    nivelWrapper.appendChild(nivelTitulo);
                    nivelWrapper.appendChild(nivelDetalhes);
                    detalhesDiv.appendChild(nivelWrapper);
                });

                detalhesDiv.classList.add('visible');
            } else {
                detalhesDiv.classList.remove('visible');
            }
        });

         detalhesDiv.addEventListener('click', (event) => {
             event.stopPropagation();
         });
    });

    // Fecha ao clicar fora
    document.addEventListener('click', () => {
        allDetalhesDivs.forEach(div => {
            div.classList.remove('visible');
        });
    });

    // Acessibilidade com Teclado
     titulos.forEach(titulo => {
        titulo.addEventListener('keydown', (event) => {
             if (event.key === 'Enter' || event.key === ' ') {
                 event.preventDefault();
                 titulo.click();
             }
             if (event.key === 'Escape') {
                 const slotId = titulo.dataset.slotId;
                 const detalhesDiv = document.querySelector(`.habilidade-detalhes[data-details-for="${slotId}"]`);
                 if (detalhesDiv && detalhesDiv.classList.contains('visible')) {
                     detalhesDiv.classList.remove('visible');
                 }
             }
         });
     });


}); // Fim do DOMContentLoaded


// FUNÇÃO DE EXIBIÇÃO DOS EFEITOS
document.addEventListener("DOMContentLoaded", function () {
    const containers = {
        ativo: document.getElementById('area-ativo'),
        passivo: document.getElementById('area-passivo'),
        aura: document.getElementById('area-aura'),
        nucleo: document.getElementById('area-nucleo'),
        triunfo: document.getElementById('area-triunfo')
    };

    const jsonIds = {
        ativo: 'ativo-json',
        passivo: 'passivo-json',
        aura: 'aura-json',
        nucleo: 'nucleo-json',
        triunfo: 'triunfo-json'
    };

    const listas = {};

    for (const tipo in jsonIds) {
        try {
            const el = document.getElementById(jsonIds[tipo]);
            if (el && el.textContent.trim() !== '') {
                listas[tipo] = JSON.parse(JSON.parse(el.textContent));
                //console.log(`✔️ Efeitos carregados para tipo "${tipo}":`, listas[tipo]);
            } else {
                //console.warn(`⚠️ Elemento JSON "${jsonIds[tipo]}" não encontrado ou vazio.`);
                listas[tipo] = [];
            }
        } catch (e) {
            //console.error(`❌ Erro ao parsear JSON para tipo "${tipo}":`, e);
            listas[tipo] = [];
        }
    }
    
    //console.log("🎯 Listas finalizadas:", listas);


function criarCardEfeito({ nome, descricao }, index) {
    const div = document.createElement('div');
    div.className = 'efeito-card';
    div.id = `efeito_${index}`;

    // Renderiza o HTML com suporte a <b>, <i>, etc.
    div.innerHTML = `
        <div class="efeito-nome">
            <strong>${nome}</strong>
            <span class="efeito-underline"></span>
        </div>
        <div class="efeito-descricao">${descricao}</div>
    `;

    const nomeDiv = div.querySelector('.efeito-nome');
    const descricaoDiv = div.querySelector('.efeito-descricao');

    nomeDiv.addEventListener('click', function () {
        const visivel = descricaoDiv.classList.contains('ativo');

        // Fecha todos os outros
        document.querySelectorAll('.efeito-descricao').forEach(el => el.classList.remove('ativo'));
        document.querySelectorAll('.efeito-card').forEach(el => el.classList.remove('ativo-card'));

        // Se não estava visível, abre este
        if (!visivel) {
            descricaoDiv.classList.add('ativo');
            div.classList.add('ativo-card');
        }
    });

    return div;
}
    // Itera sobre cada tipo (ativo, passivo, etc)
    for (const tipo in listas) {
    const lista = listas[tipo];
    const container = containers[tipo];

    //console.log(`→ Verificando tipo: ${tipo}`);
    //console.log('→ Lista:', lista);
    //console.log('→ Container:', container);

    if (!container || !Array.isArray(lista)) continue;

    lista.forEach((efeitoObj, i) => {
        const { nome, descricao } = efeitoObj;
        console.log(descricao)
        if (descricao != undefined && descricao != null && descricao != "") {
            const card = criarCardEfeito({ nome, descricao }, i + 1);
            container.appendChild(card);
            }        
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const camposBuffaveis = [
        'forca', 'destreza', 'inteligencia', 'determinacao', 'perspicacia', 'carisma',
        'vida', 'esmagamento', 'penExtra', 'danoFinal',
        'espiritualFixo', 'espiritualPerc', 'defesaFixaEspiritual', 'reducaoEspiritual', 'reducao'
    ];

    camposBuffaveis.forEach(campo => {
        const container = document.getElementById(`${campo}_container`);
        if (!container) return;

        const valorSpan = document.createElement('span');
        valorSpan.className = 'buffed-value hidden';
        valorSpan.id = `${campo}AutoBuffed`;
        container.appendChild(valorSpan);

        const valorExterno = document.createElement('span');
        valorExterno.className = 'buffed-value hidden';
        valorExterno.id = `${campo}ExternalBuffed`;
        container.appendChild(valorExterno);

        const valorFinal = document.createElement('span');
        valorFinal.className = 'buffed-value hidden';
        valorFinal.id = `${campo}FinalBuffed`;
        container.appendChild(valorFinal);

        const botao = document.createElement('button');
        botao.className = 'buff-button';
        botao.dataset.field = campo;
        botao.textContent = 'BUFF';
        container.appendChild(botao);

        const input1 = document.createElement('input');
        input1.type = 'number';
        input1.className = 'buff-input hidden';
        input1.id = `${campo}BuffInput`;
        input1.placeholder = 'Auto-buff %';
        container.appendChild(input1);

        const input2 = document.createElement('input');
        input2.type = 'number';
        input2.className = 'buff-input hidden';
        input2.id = `${campo}ExternalBuffInput`;
        input2.placeholder = 'Buff Externo %';
        container.appendChild(input2);
    });
});
