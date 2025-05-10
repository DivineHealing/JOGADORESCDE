function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}


const addRolagemBtn = document.getElementById('addRolagem');
const rolagemContainer = document.getElementById('rolagemContainer');
let rolagemCount = 0; // Counter to keep track of attribute rows
let total = 0; // Contador para Validar quantia de feitos.

addRolagemBtn.addEventListener('click', function () {
    rolagemCount++; // Increment counter for each new attribute row
    total++;

    const rolagemRow = document.createElement('div');
    if (rolagemCount <= 25 && total <= 3) {
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
    total++;

    const amplificacaoRow = document.createElement('div');
    if (amplificacaoCount <= 25 && total <= 3) {
        amplificacaoRow.classList.add('amplificacao-row');
        amplificacaoRow.innerHTML = `
            <div>
                <label for="amplificacaoTipo${amplificacaoCount}">Tipo</label>
                <input type="text" id="amplificacaoTipo${amplificacaoCount}" name="amplificacaoTipo${amplificacaoCount}" placeholder="Ex: Fogo">
            </div>
            <div>
                <label for="amplificacao${amplificacaoCount}">Valor</label>
                <input type="number" id="amplificacao${amplificacaoCount}" name="amplificacao${amplificacaoCount}" value="0">
            </div>
        `;

        amplificacaoContainer.appendChild(amplificacaoRow);
        console.log(total)
    }
});


const addRegeneracaoBtn = document.getElementById('addRegeneracao');
const regeneracaoContainer = document.getElementById('regeneracaoContainer');
let regeneracaoCount = 0; // Counter to keep track of attribute rows

addRegeneracaoBtn.addEventListener('click', function () {
    regeneracaoCount++; // Increment counter for each new attribute row
    total++;

    const regeneracaoRow = document.createElement('div');
    if (regeneracaoCount <= 3 && total <= 3) {
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
