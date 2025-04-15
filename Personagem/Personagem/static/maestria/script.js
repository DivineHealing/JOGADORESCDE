const addDefesaBtn = document.getElementById('addDefesa');
const defesaContainer = document.getElementById('defesaContainer');
let defesaCount = 0; // Counter to keep track of attribute rows

addDefesaBtn.addEventListener('click', function () {
    defesaCount++; // Increment counter for each new attribute row

    const atributoRow = document.createElement('div');
    if (defesaCount <= 5) {
        atributoRow.classList.add('defesa-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elemento${defesaCount}">Elemento</label>
                <input type="text" id="elemento${defesaCount}" name="elemento${defesaCount}" placeholder="Ex: Fogo">
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
    if (danoCount <= 5) {
        atributoRow.classList.add('dano-row');
        atributoRow.innerHTML = `
            <div>
                <label for="elemento${danoCount}">Elemento</label>
                <input type="text" id="elemento${danoCount}" name="elemento${danoCount}" placeholder="Ex: Fogo">
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
    if (rolagemCount <= 5) {
        rolagemRow.classList.add('rolagem-row');
        rolagemRow.innerHTML = `
            <div>
                <label for="elemento${rolagemCount}">Tipo</label>
                <input type="text" id="rolagemTipo${rolagemCount}" name="rolagemTipo${rolagemCount}" placeholder="Ex: Invocação">
            </div>
            <div>
                <label for="dano${rolagemCount}">Valor</label>
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
    if (amplificacaoCount <= 5) {
        amplificacaoRow.classList.add('amplificacao-row');
        amplificacaoRow.innerHTML = `
            <div>
                <label for="elemento${amplificacaoCount}">Tipo</label>
                <input type="text" id="amplificacaoTipo${amplificacaoCount}" name="amplificacaoTipo${amplificacaoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="dano${amplificacaoCount}">Valor</label>
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
        regeneracaoRow.innerHTML = `
            <div>
                <label for="elemento${regeneracaoCount}">Tipo</label>
                <input type="text" id="regeneracaoTipo${regeneracaoCount}" name="regeneracaoTipo${regeneracaoCount}" placeholder="Ex: Vida">
            </div>
            <div>
                <label for="dano${regeneracaoCount}">Valor</label>
                <input type="number" id="regeneracao${regeneracaoCount}" name="regeneracao${regeneracaoCount}" value="0">
            </div>
        `;

        regeneracaoContainer.appendChild(regeneracaoRow);
    }
});