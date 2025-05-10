function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

function selecionarPersonagem() {
    var select = document.getElementById("personagem_select");
    var personagem_id = select.value;
    window.location.href = "/" + personagem_id + "/";
}

const addAtributoBtn = document.getElementById('addAtributo');
const atributosContainer = document.getElementById('atributosContainer');
let atributoCount = 0; // Counter to keep track of attribute rows

addAtributoBtn.addEventListener('click', function () {
    atributoCount++; // Increment counter for each new attribute row

    const atributoRow = document.createElement('div');
    if (atributoCount <= 7) {
        atributoRow.classList.add('atributo-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elementoDefesa${atributoCount}">Elemento</label>
                <input type="text" id="elementoDefesa${atributoCount}" name="elementoDefesa${atributoCount}" placeholder="Ex: Fogo">
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
    if (rolagemCount <= 25) {
        rolagemRow.classList.add('rolagem-row');
        rolagemRow.innerHTML = `
            <div>
                <label for="rolagemTipo${rolagemCount}">Tipo</label>
                <input type="text" id="rolagemTipo${rolagemCount}" name="rolagemTipo${rolagemCount}" placeholder="Ex: Invocação">
            </div>
            <div>
                <label for="rolagem${rolagemCount}">Valor</label>
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
    if (amplificacaoCount <= 25) {
        amplificacaoRow.classList.add('amplificacao-row');
        amplificacaoRow.innerHTML = `
            <div>
                <label for="elemento${amplificacaoCount}">Tipo</label>
                <input type="text" id="amplificacaoTipo${amplificacaoCount}" name="amplificacaoTipo${amplificacaoCount}" placeholder="Ex: Fogo">
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
    if (regeneracaoCount <= 3) {
        regeneracaoRow.classList.add('regeneracao-row');
        regeneracaoRow.innerHTML =
        `   <div>
                <label for="regeneracaoTipo${regeneracaoCount}">Tipo</label>
                <select class='personagem_select' id="regeneracaoTipo${regeneracaoCount}" name="regeneracaoTipo${regeneracaoCount}">                        
                    <option value="regenVida" selected>Vida</option>
                    <option value="regenMana">Mana</option>
                    <option value="regenVigor">Vigor</option>
                </select>
            </div>
            <div>
                <label for="regeneracao${regeneracaoCount}">Valor</label>
                <input type="number" id="regeneracao${regeneracaoCount}" name="regeneracao${regeneracaoCount}" value="0">
            </div>
        `;

        regeneracaoContainer.appendChild(regeneracaoRow);
    }
});
