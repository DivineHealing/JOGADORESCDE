function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}


const addDefesaBtn = document.getElementById('addDefesa');
const defesaContainer = document.getElementById('defesaContainer');
let defesaCount = 0; // Counter to keep track of attribute rows

addDefesaBtn.addEventListener('click', function () {
    defesaCount++; // Increment counter for each new attribute row

    const atributoRow = document.createElement('div');
    if (defesaCount <= 7) {
        atributoRow.classList.add('defesa-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elementoDefesa${defesaCount}">Elemento</label>
                <input type="text" id="elementoDefesa${defesaCount}" name="elementoDefesa${defesaCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="defesa${defesaCount}">Defesa Fixa</label>
                <input type="number" id="defesa${defesaCount}" name="defesa${defesaCount}" value="0">
            </div>
            <div>
                <label for="resistencia${defesaCount}">Resistência</label>
                <input type="number" id="resistencia${defesaCount}" name="resistencia${defesaCount}" value="0">
            </div>
        `;

        defesaContainer.appendChild(atributoRow);
    }
});

const addAtributoBtn = document.getElementById('addAtributo');
const atributosContainer = document.getElementById('atributosContainer');
let danoCount = 0; // Counter to keep track of attribute rows

addAtributoBtn.addEventListener('click', function () {
    danoCount++; // Increment counter for each new attribute row

    const atributoRow = document.createElement('div');
    if (danoCount <= 7) {
        atributoRow.classList.add('dano-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elementoDano${danoCount}">Elemento</label>
                <input type="text" id="elementoDano${danoCount}" name="elementoDano${danoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="dano${danoCount}">Dano Fixo</label>
                <input type="number" id="dano${danoCount}" name="dano${danoCount}" value="0">
            </div>
            <div>
                <label for="penetracao${danoCount}">Penetração</label>
                <input type="number" id="penetracao${danoCount}" name="penetracao${danoCount}" value="0">
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
                <label for="amplificacaoTipo${amplificacaoCount}">Tipo</label>
                <input style="width: 17em" type="text" id="amplificacaoTipo${amplificacaoCount}" name="amplificacaoTipo${amplificacaoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="amplificacao${amplificacaoCount}">Valor</label>
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

const atrOfensivo = document.getElementById("atributosOfensivo");
const atrDefensivo = document.getElementById("atributosDefensivo");

function definirAtr(alterarAtr) {
    atrOfensivo.style.display = alterarAtr.checked ? "block" : "none";
    atrDefensivo.style.display = alterarAtr.checked ? "none" : "block";
};