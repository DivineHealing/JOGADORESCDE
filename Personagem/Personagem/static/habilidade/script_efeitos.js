function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

const addHab1Btn = document.getElementById('addHab1');
const addHab2Btn = document.getElementById('addHab2');
const addHab3Btn = document.getElementById('addHab3');
const addHab4Btn = document.getElementById('addHab4');
const addHab5Btn = document.getElementById('addHab5');
const addHab6Btn = document.getElementById('addHab6');
const addHab7Btn = document.getElementById('addHab7');
const addHab8Btn = document.getElementById('addHab8');
const addHab9Btn = document.getElementById('addHab9');
const addHab10Btn = document.getElementById('addHab10');
const addHab11Btn = document.getElementById('addHab11');
const addHab12Btn = document.getElementById('addHab12');
const hab1Container = document.getElementById('hab1Container');
const hab2Container = document.getElementById('hab2Container');
const hab3Container = document.getElementById('hab3Container');
const hab4Container = document.getElementById('hab4Container');
const hab5Container = document.getElementById('hab5Container');
const hab6Container = document.getElementById('hab6Container');
const hab7Container = document.getElementById('hab7Container');
const hab8Container = document.getElementById('hab8Container');
const hab9Container = document.getElementById('hab9Container');
const hab10Container = document.getElementById('hab10Container');
const hab11Container = document.getElementById('hab11Container');
const hab12Container = document.getElementById('hab12Container');
let hab1Count = 1; // Counter to keep track of attribute rows
let hab2Count = 1; // Counter to keep track of attribute rows
let hab3Count = 1; // Counter to keep track of attribute rows
let hab4Count = 1; // Counter to keep track of attribute rows
let hab5Count = 1; // Counter to keep track of attribute rows
let hab6Count = 1; // Counter to keep track of attribute rows
let hab7Count = 1; // Counter to keep track of attribute rows
let hab8Count = 1; // Counter to keep track of attribute rows
let hab9Count = 1; // Counter to keep track of attribute rows
let hab10Count = 1; // Counter to keep track of attribute rows
let hab11Count = 1; // Counter to keep track of attribute rows
let hab12Count = 1; // Counter to keep track of attribute rows

addHab1Btn.addEventListener('click', function () {
    hab1Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab1Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
            <div class='habilidade-row-container'>
                <div class='habilidade-row-miniContainer'>
                    <label for="habilidadeTipo${hab1Count}">Tipo do habilidade</label>
                    <select class='personagem_select' id="habilidadeTipo${hab1Count}" name="habilidadeTipo${hab1Count}">
                        <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                        <option value="habilidadeAtivo"> Habilidade Ativo</option>
                        <option value="habilidadeAura"> Habilidade Aura</option>
                    </select>
                    <label for="habilidadeNivel${hab1Count}">Nível do habilidade</label>
                    <select class='personagem_select' id="habilidadeNivel${hab1Count}" name="habilidadeNivel${hab1Count}">                        
                        <option value="nivel2" selected>Nível 2</option>
                        <option value="nivel3">Nível 3</option>
                        <option value="nivel4">Nível 4</option>
                        <option value="nivel5">Nível 5</option>
                        <option value="nivel6">Nível 6</option>
                    </select>
                </div>
                <div>
                    <label for="habilidadeNome${hab1Count}">Nome do habilidade:</label>
                    <input style="width: 100%"; type="text" id="habilidadeNome${hab1Count}" name="habilidadeNome${hab1Count}" placeholder="Nome do habilidade">
                    <label for="habilidadeCusto${hab1Count}">Custo do habilidade:</label>
                    <input style="width: 50%"; type="text" id="habilidadeCusto${hab1Count}" name="habilidadeCusto${hab1Count}" placeholder="Custo do habilidade">
                </div class='habilidade-row-miniContainer'>
                <div class='habilidade-row-miniContainer'>
                    <label for="habilidadeDesc${hab1Count}">Descrição do habilidade:</label>
                    <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab1Count}" name="habilidadeDesc${hab1Count}" placeholder="Descrição do habilidade"></textarea>
                </div>
            </div>
        `;

        hab1Container.appendChild(habilidadeRow);
    }
});

addHab2Btn.addEventListener('click', function () {
    hab2Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab2Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab2Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab2Count}" name="habilidadeTipo${hab2Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab2Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab2Count}" name="habilidadeNivel${hab2Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab2Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab2Count}" name="habilidadeNome${hab2Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab2Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab2Count}" name="habilidadeCusto${hab2Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab2Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab2Count}" name="habilidadeDesc${hab2Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab2Container.appendChild(habilidadeRow);
    }
});

addHab3Btn.addEventListener('click', function () {
    hab3Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab3Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab3Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab3Count}" name="habilidadeTipo${hab3Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab3Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab3Count}" name="habilidadeNivel${hab3Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab3Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab3Count}" name="habilidadeNome${hab3Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab3Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab3Count}" name="habilidadeCusto${hab3Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab3Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab3Count}" name="habilidadeDesc${hab3Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab3Container.appendChild(habilidadeRow);
    }
});

addHab4Btn.addEventListener('click', function () {
    hab4Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab4Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab4Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab4Count}" name="habilidadeTipo${hab4Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab4Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab4Count}" name="habilidadeNivel${hab4Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab4Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab4Count}" name="habilidadeNome${hab4Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab4Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab4Count}" name="habilidadeCusto${hab4Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab4Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab4Count}" name="habilidadeDesc${hab4Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab4Container.appendChild(habilidadeRow);
    }
});

addHab5Btn.addEventListener('click', function () {
    hab5Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab5Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab5Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab5Count}" name="habilidadeTipo${hab5Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab5Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab5Count}" name="habilidadeNivel${hab5Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab5Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab5Count}" name="habilidadeNome${hab5Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab5Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab5Count}" name="habilidadeCusto${hab5Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab5Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab5Count}" name="habilidadeDesc${hab5Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab5Container.appendChild(habilidadeRow);
    }
});

addHab6Btn.addEventListener('click', function () {
    hab6Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab6Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab6Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab6Count}" name="habilidadeTipo${hab6Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab6Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab6Count}" name="habilidadeNivel${hab6Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab6Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab6Count}" name="habilidadeNome${hab6Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab6Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab6Count}" name="habilidadeCusto${hab6Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab6Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab6Count}" name="habilidadeDesc${hab6Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab6Container.appendChild(habilidadeRow);
    }
});

addHab7Btn.addEventListener('click', function () {
    hab7Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab7Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab7Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab7Count}" name="habilidadeTipo${hab7Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab7Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab7Count}" name="habilidadeNivel${hab7Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab7Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab7Count}" name="habilidadeNome${hab7Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab7Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab7Count}" name="habilidadeCusto${hab7Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab7Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab7Count}" name="habilidadeDesc${hab7Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab7Container.appendChild(habilidadeRow);
    }
});

addHab8Btn.addEventListener('click', function () {
    hab8Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab8Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab8Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab8Count}" name="habilidadeTipo${hab8Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab8Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab8Count}" name="habilidadeNivel${hab8Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab8Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab8Count}" name="habilidadeNome${hab8Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab8Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab8Count}" name="habilidadeCusto${hab8Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab8Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab8Count}" name="habilidadeDesc${hab8Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab8Container.appendChild(habilidadeRow);
    }
});

addHab9Btn.addEventListener('click', function () {
    hab9Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab9Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab9Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab9Count}" name="habilidadeTipo${hab9Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab9Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab9Count}" name="habilidadeNivel${hab9Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab9Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab9Count}" name="habilidadeNome${hab9Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab9Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab9Count}" name="habilidadeCusto${hab9Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab9Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab9Count}" name="habilidadeDesc${hab9Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab9Container.appendChild(habilidadeRow);
    }
});

addHab10Btn.addEventListener('click', function () {
    hab10Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab10Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab10Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab10Count}" name="habilidadeTipo${hab10Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab10Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab10Count}" name="habilidadeNivel${hab10Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab10Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab10Count}" name="habilidadeNome${hab10Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab10Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab10Count}" name="habilidadeCusto${hab10Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab10Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab10Count}" name="habilidadeDesc${hab10Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab10Container.appendChild(habilidadeRow);
    }
});

addHab11Btn.addEventListener('click', function () {
    hab11Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab11Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab11Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab11Count}" name="habilidadeTipo${hab11Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab11Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab11Count}" name="habilidadeNivel${hab11Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab11Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab11Count}" name="habilidadeNome${hab11Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab11Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab11Count}" name="habilidadeCusto${hab11Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab11Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab11Count}" name="habilidadeDesc${hab11Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab11Container.appendChild(habilidadeRow);
    }
});

addHab12Btn.addEventListener('click', function () {
    hab12Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab12Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
    <div class='habilidade-row-container'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeTipo${hab12Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidadeTipo${hab12Count}" name="habilidadeTipo${hab12Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidadeNivel${hab12Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidadeNivel${hab12Count}" name="habilidadeNivel${hab12Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidadeNome${hab12Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab12Count}" name="habilidadeNome${hab12Count}" placeholder="Nome do habilidade">
            <label for="habilidadeCusto${hab12Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidadeCusto${hab12Count}" name="habilidadeCusto${hab12Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidadeDesc${hab12Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidadeDesc${hab12Count}" name="habilidadeDesc${hab12Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab12Container.appendChild(habilidadeRow);
    }
});
