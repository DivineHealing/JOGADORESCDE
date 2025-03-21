function selecionarPersonagem() {
    var select = document.getElementById("personagem_select");
    var personagem_id = select.value;
    window.location.href = "/" + personagem_id + "/";
}

const atributos = [
    { nome: "regenVida", containerId: "regenVida_container" },
    { nome: "regenMana", containerId: "regenMana_container" },
    { nome: "regenVigor", containerId: "regenVigor_container" },

    { nome: "forca", containerId: "forca_container", bonusElementId: "forcaBonus" },
    { nome: "destreza", containerId: "destreza_container", bonusElementId: "destrezaBonus" },
    { nome: "inteligencia", containerId: "inteligencia_container", bonusElementId: "inteligenciaBonus" },
    { nome: "determinacao", containerId: "determinacao_container", bonusElementId: "determinacaoBonus" },
    { nome: "perspicacia", containerId: "perspicacia_container", bonusElementId: "perspicaciaBonus" },
    { nome: "carisma", containerId: "carisma_container", bonusElementId: "carismaBonus" },

    { nome: "defesaFixa_1", containerId: "defesaFixa1_container" },
    { nome: "resistencia_1", containerId: "resistencia1_container" },
    { nome: "defesaFixa_2", containerId: "defesaFixa2_container" },
    { nome: "resistencia_2", containerId: "resistencia2_container" },
    { nome: "defesaFixa_3", containerId: "defesaFixa3_container" },
    { nome: "resistencia_3", containerId: "resistencia3_container" },
    { nome: "defesaFixa_4", containerId: "defesaFixa4_container" },
    { nome: "resistencia_4", containerId: "resistencia4_container" },
    { nome: "defesaFixa_5", containerId: "defesaFixa5_container" },
    { nome: "resistencia_5", containerId: "resistencia5_container" },

    { nome: "rolagem1", containerId: "rolagem1_container" },
    { nome: "rolagem2", containerId: "rolagem2_container" },
    { nome: "rolagem3", containerId: "rolagem3_container" },
    { nome: "rolagem4", containerId: "rolagem4_container" },
    { nome: "rolagem5", containerId: "rolagem5_container" },
    { nome: "rolagem6", containerId: "rolagem6_container" },
    { nome: "rolagem7", containerId: "rolagem7_container" },
    { nome: "rolagem8", containerId: "rolagem8_container" },
    { nome: "rolagem9", containerId: "rolagem9_container" },
    { nome: "rolagem10", containerId: "rolagem10_container" },
    { nome: "rolagem11", containerId: "rolagem11_container" },
    { nome: "rolagem12", containerId: "rolagem12_container" },
    { nome: "rolagem13", containerId: "rolagem13_container" },
    { nome: "rolagem14", containerId: "rolagem14_container" },
    { nome: "rolagem15", containerId: "rolagem15_container" },
    { nome: "rolagem15", containerId: "rolagem15_container" },
];

let algumAtributoInvalido = false; // Flag para verificar se algum atributo é inválido

// FUNÇÃO PARA OCULTAR OS DADOS ZERADOS
function exibirOuOcultarAtributo(atributo) {
    const element = document.getElementById(atributo.nome);
    const containerElement = document.getElementById(atributo.containerId);

    if (!element) {
        console.warn(`Elemento '${atributo.nome}' não encontrado.`);
        return;
    }

    let valorTexto = element.value;

    // Remove separadores de milhar e espaços em branco
    valorTexto = valorTexto.replace(/\./g, '').trim();

    // Converte para número se for um número, senão mantém como string
    let valor;
    if (!isNaN(parseFloat(valorTexto)) && isFinite(valorTexto)) {
        valor = parseFloat(valorTexto); // Converte para número
    } else {
        valor = valorTexto; // Mantém como string
    }

    // Verifica se o valor é "vazio" (zero para números, string vazia ou null)
    let vazio = (typeof valor === 'number' && valor === 0) || (typeof valor === 'string' && valor.trim() === "") || valor === null;

    if (!containerElement) {
        console.error(`Container '${atributo.containerId}' não encontrado.`);
        return;
    }

    if (vazio) {
        containerElement.style.display = 'none';
        element.style.display = 'none';
    } else {
        containerElement.style.display = 'block';
        element.style.display = 'block';
    }
}

const addAtributoBtn = document.getElementById('addAtributo');
const atributosContainer = document.getElementById('atributosContainer');
let atributoCount = 0; // Counter to keep track of attribute rows

addAtributoBtn.addEventListener('click', function () {
    atributoCount++; // Increment counter for each new attribute row

    const atributoRow = document.createElement('div');
    if (atributoCount <= 7){
        atributoRow.classList.add('atributo-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elemento${atributoCount}">Elemento</label>
                <input type="text" id="elemento${atributoCount}" name="elemento${atributoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="defesa${atributoCount}">Defesa Fixa</label>
                <input type="number" id="defesa${atributoCount}" name="defesa${atributoCount}" value="0">
            </div>
            <div>
                <label for="resistencia${atributoCount}">Resistência</label>
                <input type="number" id="resistencia${atributoCount}" name="resistencia${atributoCount}" value="0">
            </div>
        `;
    
    atributosContainer.appendChild(atributoRow);
    }
});


const addRolagemBtn = document.getElementById('addRolagem');
const rolagemContainer = document.getElementById('rolagemContainer');
let rolagemCount = 0; // Counter to keep track of attribute rows

addRolagemBtn.addEventListener('click', function () {
    rolagemCount++; // Increment counter for each new attribute row

    const rolagemRow = document.createElement('div');
    if (rolagemCount <= 25){
        rolagemRow.classList.add('rolagem-row');
        rolagemRow.innerHTML = `
            <div>
                <label for="elemento${rolagemCount}">Tipo</label>
                <input type="text" id="rolagemTipo${rolagemCount}" name="rolagemTipo${rolagemCount}" placeholder="Ex: Invocação">
            </div>
            <div>
                <label for="defesa${rolagemCount}">Valor</label>
                <input type="number" id="rolagem${rolagemCount}" name="rolagem${rolagemCount}" value="0">
            </div>
        `;
    
    rolagemContainer.appendChild(rolagemRow);
    }
});


const addAmplificacaoBtn = document.getElementById('addAmplificacao');
const amplificacaoContainer = document.getElementById('amplificacaoContainer');
let amplificacaoCount = 0; // Counter to keep track of attribute rows

addAmplificacaoBtn.addEventListener('click', function () {
    amplificacaoCount++; // Increment counter for each new attribute row

    const amplificacaoRow = document.createElement('div');
    if (amplificacaoCount <= 25){
        amplificacaoRow.classList.add('amplificacao-row');
        amplificacaoRow.innerHTML = `
            <div>
                <label for="elemento${amplificacaoCount}">Tipo</label>
                <input type="text" id="amplificacaoTipo${amplificacaoCount}" name="amplificacaoElemento${amplificacaoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="defesa${amplificacaoCount}">Valor</label>
                <input type="number" id="amplificacao${amplificacaoCount}" name="amplificacao${amplificacaoCount}" value="0">
            </div>
        `;
    
    amplificacaoContainer.appendChild(amplificacaoRow);
    }
});


const addRegeneracaoBtn = document.getElementById('addRegeneracao');
const regeneracaoContainer = document.getElementById('regeneracaoContainer');
let regeneracaoCount = 0; // Counter to keep track of attribute rows

addRegeneracaoBtn.addEventListener('click', function () {
    regeneracaoCount++; // Increment counter for each new attribute row

    const regeneracaoRow = document.createElement('div');
    if (regeneracaoCount <= 3){
        regeneracaoRow.classList.add('regeneracao-row');
        regeneracaoRow.innerHTML = `
            <div>
                <label for="elemento${regeneracaoCount}">Tipo</label>
                <input type="text" id="regeneracaoTipo${regeneracaoCount}" name="regeneracaoElemento${regeneracaoCount}" placeholder="Ex: Vida">
            </div>
            <div>
                <label for="defesa${regeneracaoCount}">Valor</label>
                <input type="number" id="regeneracao${regeneracaoCount}" name="regeneracao${regeneracaoCount}" value="0">
            </div>
        `;
    
    regeneracaoContainer.appendChild(regeneracaoRow);
    }
});

