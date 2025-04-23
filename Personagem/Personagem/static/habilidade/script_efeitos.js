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

document.addEventListener('DOMContentLoaded', function() {

    const addHab1Btn = document.getElementById('addHab1');
    const hab1Container = document.getElementById('hab1Container');
    const maxNiveis = 6; // Máximo de níveis permitidos

    // --- 1. Obter e Processar Dados das Habilidades ---
    const habilidadesDataElement = document.getElementById('all-habilidades-data');
    let allHabilidadesData = {};
    let dataArray = [];

    if (habilidadesDataElement && habilidadesDataElement.textContent) {
        try {
            const parsedData = JSON.parse(habilidadesDataElement.textContent);
            if (Array.isArray(parsedData)) {
                dataArray = parsedData;
            } else {
                console.warn("Dados de habilidades não são um array.", parsedData);
            }
        } catch (e) {
            console.error("Erro ao parsear dados das habilidades:", e);
        }
    } else {
        console.warn("Elemento 'all-habilidades-data' não encontrado ou vazio.");
    }

    // Encontra os dados específicos da Habilidade 1 (Slot ID 1)
    const habilidade1Data = dataArray.find(hab => hab.id === 1);
    console.log("Dados encontrados para Habilidade 1:", habilidade1Data);

    // --- 2. Função Reutilizável para Criar Linha de Nível ---
    //    (Adaptada da sua função original no botão Add)
    function createHabilidadeLevelRow(slotNum, levelNum, data = {}) {
        const habilidadeRow = document.createElement('div');
        habilidadeRow.classList.add('habilidade-row', `habilidade-${slotNum}-nivel-${levelNum}`); // Adiciona classes para identificação
        habilidadeRow.dataset.level = levelNum; // Guarda o nível no dataset

        // Usamos os dados passados (data) ou valores padrão/vazios
        const tipo = data.tipo || 'habilidadePassivo'; // Valor padrão se não houver dado
        const nome = data.nome || '';
        const custo = data.custo || '';
        const descricao = data.descricao || '';

        habilidadeRow.innerHTML = `
            <div class='habilidade-row-container'>
                <h4>Nível ${levelNum}</h4> <!-- Adiciona título do Nível -->
                <div class='habilidade-row-miniContainer'>
                    <label for="habilidade${slotNum}Tipo${levelNum}">Tipo da Habilidade</label>
                    <select class='personagem_select' id="habilidade${slotNum}Tipo${levelNum}" name="habilidade${slotNum}Tipo${levelNum}">
                        <option value="habilidadePassivo" ${tipo === 'habilidadePassivo' ? 'selected' : ''}> Habilidade Passivo</option>
                        <option value="habilidadeAtivo" ${tipo === 'habilidadeAtivo' ? 'selected' : ''}> Habilidade Ativo</option>
                        <option value="habilidadeAura" ${tipo === 'habilidadeAura' ? 'selected' : ''}> Habilidade Aura</option>
                    </select>
                    <!-- Removido Select de Nível daqui, pois o nível é definido pelo loop/contador -->
                </div>
                <div>
                    <label for="habilidade${slotNum}Nome${levelNum}">Nome da Habilidade:</label>
                    <input style="width: 100%"; type="text" id="habilidade${slotNum}Nome${levelNum}" name="habilidade${slotNum}Nome${levelNum}" placeholder="Nome (Nível ${levelNum})" value="${nome}">
                    <label for="habilidade${slotNum}Custo${levelNum}">Custo da Habilidade:</label>
                    <input style="width: 50%"; type="text" id="habilidade${slotNum}Custo${levelNum}" name="habilidade${slotNum}Custo${levelNum}" placeholder="Custo (Nível ${levelNum})" value="${custo}">
                </div>
                <div class='habilidade-row-miniContainer'>
                    <label for="habilidade${slotNum}Desc${levelNum}">Descrição da Habilidade:</label>
                    <textarea style="width: 100%; height: 10em;" type="text" id="habilidade${slotNum}Desc${levelNum}" name="habilidade${slotNum}Desc${levelNum}" placeholder="Descrição (Nível ${levelNum})">${descricao}</textarea>
                </div>
                <!-- Opcional: Botão Remover -->
                <!-- <button type="button" class="remove-habilidade-nivel" data-slot="${slotNum}" data-level="${levelNum}">Remover Nível</button> -->
            </div>
        `;
        return habilidadeRow;
    }

    // --- 3. Exibir Níveis Existentes (2 a 6) ---
    let maiorNivelExistente = 1; // Começa em 1 por causa do nível estático no HTML

    if (habilidade1Data && habilidade1Data.niveis) {
        // Ordena por nível para garantir a ordem correta de exibição e cálculo
        habilidade1Data.niveis.sort((a, b) => a.nivel - b.nivel);

        habilidade1Data.niveis.forEach(nivelData => {
            if (nivelData.nivel > 1 && nivelData.nivel <= maxNiveis) { // Processa apenas níveis 2 a 6 existentes
                console.log(`Renderizando nível existente ${nivelData.nivel} para Habilidade 1`);
                const levelRow = createHabilidadeLevelRow(1, nivelData.nivel, nivelData);
                hab1Container.appendChild(levelRow);
                if (nivelData.nivel > maiorNivelExistente) {
                    maiorNivelExistente = nivelData.nivel;
                }
            } else if (nivelData.nivel === 1) {
                 // Atualiza o maior nível se o nível 1 for o único encontrado até agora
                 // (embora já comecemos com 1)
                 if (1 > maiorNivelExistente) {
                     maiorNivelExistente = 1;
                 }
            }
        });
    }

    // --- 4. Inicializar Contador e Botão Add ---
    let hab1Count = maiorNivelExistente; // Contador começa no maior nível JÁ existente

    // Desabilita o botão se todos os níveis já existem
    if (hab1Count >= maxNiveis) {
        addHab1Btn.disabled = true;
        addHab1Btn.textContent = "Máx Níveis";
    } else {
         addHab1Btn.disabled = false;
         addHab1Btn.textContent = `Add Nível ${hab1Count + 1}`; // Mostra qual nível será adicionado
    }


    // --- 5. Event Listener do Botão Add ---
    addHab1Btn.addEventListener('click', function () {
        if (hab1Count < maxNiveis) {
            hab1Count++; // Incrementa para o PRÓXIMO nível a ser adicionado

            console.log(`Adicionando Nível ${hab1Count} para Habilidade 1`);
            // Cria a linha para o novo nível (sem dados pré-preenchidos)
            const newLevelRow = createHabilidadeLevelRow(1, hab1Count, {}); // Passa objeto vazio como dados
            hab1Container.appendChild(newLevelRow);

            // Atualiza e desabilita o botão se atingir o limite
            if (hab1Count >= maxNiveis) {
                addHab1Btn.disabled = true;
                addHab1Btn.textContent = "Máx Níveis";
            } else {
                 addHab1Btn.textContent = `Add Nível ${hab1Count + 1}`; // Atualiza texto do botão
            }
        }
    });

     // --- Opcional: Lógica para Remover Níveis (Mais Complexo) ---
     // hab1Container.addEventListener('click', function(event) {
     //     if (event.target.classList.contains('remove-habilidade-nivel')) {
     //         const levelToRemove = event.target.dataset.level;
     //         const rowToRemove = event.target.closest('.habilidade-row'); // Encontra a linha pai
     //         if (rowToRemove) {
     //             rowToRemove.remove();
     //             // IMPORTANTE: Ajustar hab1Count e reabilitar botão Add é complexo
     //             // pois pode criar "buracos" na sequência de níveis.
     //             // Talvez seja melhor apenas marcar para exclusão no backend.
     //             // Para simplificar, podemos reabilitar o botão Add:
     //             addHab1Btn.disabled = false;
     //             // Atualizar o texto do botão para o próximo nível a partir do maior restante?
     //             // Calcular maiorNivelRestante = ... (iterando sobre os .habilidade-row restantes)
     //             // hab1Count = maiorNivelRestante; // Atualiza contador
     //             // addHab1Btn.textContent = `Add Nível ${hab1Count + 1}`;
     //             console.log(`Nível ${levelToRemove} removido (visualmente).`);
     //         }
     //     }
     // });


}); // Fim do DOMContentLoaded

addHab2Btn.addEventListener('click', function () {
    hab2Count++; // Increment counter for each new attribute row

    const habilidadeRow = document.createElement('div');
    if (hab2Count <= 6) {
        habilidadeRow.classList.add('habilidade-row');
        habilidadeRow.innerHTML = `
        <div class='habilidade-row-container'>
            <div class='habilidade-row-miniContainer'>
                <label for="habilidade2Tipo${hab2Count}">Tipo do habilidade</label>
                <select class='personagem_select' id="habilidade2Tipo${hab2Count}" name="habilidade2Tipo${hab2Count}">
                    <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                    <option value="habilidadeAtivo"> Habilidade Ativo</option>
                    <option value="habilidadeAura"> Habilidade Aura</option>
                </select>
                <label for="habilidade2Nivel${hab2Count}">Nível do habilidade</label>
                <select class='personagem_select' id="habilidade2Nivel${hab2Count}" name="habilidade2Nivel${hab2Count}">                        
                    <option value="nivel2" selected>Nível 2</option>
                    <option value="nivel3">Nível 3</option>
                    <option value="nivel4">Nível 4</option>
                    <option value="nivel5">Nível 5</option>
                    <option value="nivel6">Nível 6</option>
                </select>
            </div>
            <div>
                <label for="habilidade2Nome${hab2Count}">Nome do habilidade:</label>
                <input style="width: 100%"; type="text" id="habilidade2Nome${hab2Count}" name="habilidade2Nome${hab2Count}" placeholder="Nome do habilidade">
                <label for="habilidade2Custo${hab2Count}">Custo do habilidade:</label>
                <input style="width: 50%"; type="text" id="habilidade2Custo${hab2Count}" name="habilidade2Custo${hab2Count}" placeholder="Custo do habilidade">
            </div class='habilidade-row-miniContainer'>
            <div class='habilidade-row-miniContainer'>
                <label for="habilidade2Desc${hab2Count}">Descrição do habilidade:</label>
                <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade2Desc${hab2Count}" name="habilidade2Desc${hab2Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade3Tipo${hab3Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade3Tipo${hab3Count}" name="habilidade3Tipo${hab3Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade3Nivel${hab3Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade3Nivel${hab3Count}" name="habilidade3Nivel${hab3Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade3Nome${hab3Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidade3Nome${hab3Count}" name="habilidade3Nome${hab3Count}" placeholder="Nome do habilidade">
            <label for="habilidade3Custo${hab3Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade3Custo${hab3Count}" name="habilidade3Custo${hab3Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade3Desc${hab3Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade3Desc${hab3Count}" name="habilidade3Desc${hab3Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade4Tipo${hab4Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade4Tipo${hab4Count}" name="habilidade4Tipo${hab4Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade4Nivel${hab4Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade4Nivel${hab4Count}" name="habilidade4Nivel${hab4Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade4Nome${hab4Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidade4Nome${hab4Count}" name="habilidadeN4ome${hab4Count}" placeholder="Nome do habilidade">
            <label for="habilidade4Custo${hab4Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade4Custo${hab4Count}" name="habilidade4Custo${hab4Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade4Desc${hab4Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade4Desc${hab4Count}" name="habilidade4Desc${hab4Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade5Tipo${hab5Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade5Tipo${hab5Count}" name="habilidade5Tipo${hab5Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade5Nivel${hab5Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade5Nivel${hab5Count}" name="habilidade5Nivel${hab5Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade5Nome${hab5Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidade5Nome${hab5Count}" name="habilidade5Nome${hab5Count}" placeholder="Nome do habilidade">
            <label for="habilidade5Custo${hab5Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade5Custo${hab5Count}" name="habilidade5Custo${hab5Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade5Desc${hab5Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade5Desc${hab5Count}" name="habilidade5Desc${hab5Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade6Tipo${hab6Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade6Tipo${hab6Count}" name="habilidade6Tipo${hab6Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade6Nivel${hab6Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade6Nivel${hab6Count}" name="habilidade6Nivel${hab6Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade6Nome${hab6Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab6Count}" name="habilidade6Nome${hab6Count}" placeholder="Nome do habilidade">
            <label for="habilidade6Custo${hab6Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade6Custo${hab6Count}" name="habilidade6Custo${hab6Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade6Desc${hab6Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade6Desc${hab6Count}" name="habilidade6Desc${hab6Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade7Tipo${hab7Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade7Tipo${hab7Count}" name="habilidade7Tipo${hab7Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade7Nivel${hab7Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade7Nivel${hab7Count}" name="habilidade7Nivel${hab7Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade7Nome${hab7Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab7Count}" name="habilidade7Nome${hab7Count}" placeholder="Nome do habilidade">
            <label for="habilidade7Custo${hab7Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade7Custo${hab7Count}" name="habilidade7Custo${hab7Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade7Desc${hab7Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade7Desc${hab7Count}" name="habilidade7Desc${hab7Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade8Tipo${hab8Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade8Tipo${hab8Count}" name="habilidade8Tipo${hab8Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade8Nivel${hab8Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade8Nivel${hab8Count}" name="habilidade8Nivel${hab8Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade8Nome${hab8Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab8Count}" name="habilidade8Nome${hab8Count}" placeholder="Nome do habilidade">
            <label for="habilidade8Custo${hab8Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade8Custo${hab8Count}" name="habilidade8Custo${hab8Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade8Desc${hab8Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade8Desc${hab8Count}" name="habilidade8Desc${hab8Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade9Tipo${hab9Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade9Tipo${hab9Count}" name="habilidade9Tipo${hab9Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade9Nivel${hab9Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade9Nivel${hab9Count}" name="habilidade9Nivel${hab9Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade9Nome${hab9Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab9Count}" name="habilidade9Nome${hab9Count}" placeholder="Nome do habilidade">
            <label for="habilidade9Custo${hab9Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade9Custo${hab9Count}" name="habilidade9Custo${hab9Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade9Desc${hab9Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade9Desc${hab9Count}" name="habilidade9Desc${hab9Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade10Tipo${hab10Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade10Tipo${hab10Count}" name="habilidade10Tipo${hab10Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade10Nivel${hab10Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade10Nivel${hab10Count}" name="habilidade10Nivel${hab10Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade10Nome${hab10Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab10Count}" name="habilidad10eNome${hab10Count}" placeholder="Nome do habilidade">
            <label for="habilidade10Custo${hab10Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade10Custo${hab10Count}" name="habilidade10Custo${hab10Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade10Desc${hab10Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade10Desc${hab10Count}" name="habilidade10Desc${hab10Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade11Tipo${hab11Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade11Tipo${hab11Count}" name="habilidade11Tipo${hab11Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade11Nivel${hab11Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade11Nivel${hab11Count}" name="habilidade11Nivel${hab11Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade11Nome${hab11Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidadeNome${hab11Count}" name="habilidad11eNome${hab11Count}" placeholder="Nome do habilidade">
            <label for="habilidade11Custo${hab11Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade11Custo${hab11Count}" name="habilidade11Custo${hab11Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade11Desc${hab11Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade11Desc${hab11Count}" name="habilidade11Desc${hab11Count}" placeholder="Descrição do habilidade"></textarea>
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
            <label for="habilidade12Tipo${hab12Count}">Tipo do habilidade</label>
            <select class='personagem_select' id="habilidade12Tipo${hab12Count}" name="habilidade12Tipo${hab12Count}">
                <option value="habilidadePassivo" selected> Habilidade Passivo</option>
                <option value="habilidadeAtivo"> Habilidade Ativo</option>
                <option value="habilidadeAura"> Habilidade Aura</option>
            </select>
            <label for="habilidade12Nivel${hab12Count}">Nível do habilidade</label>
            <select class='personagem_select' id="habilidade12Nivel${hab12Count}" name="habilidade12Nivel${hab12Count}">
                <option value="nivel2" selected>Nível 2</option>
                <option value="nivel3">Nível 3</option>
                <option value="nivel4">Nível 4</option>
                <option value="nivel5">Nível 5</option>
                <option value="nivel6">Nível 6</option>
            </select>
        </div>
        <div>
            <label for="habilidade12Nome${hab12Count}">Nome do habilidade:</label>
            <input style="width: 100%"; type="text" id="habilidade12Nome${hab12Count}" name="habilidade12Nome${hab12Count}" placeholder="Nome do habilidade">
            <label for="habilidade12Custo${hab12Count}">Custo do habilidade:</label>
            <input style="width: 50%"; type="text" id="habilidade12Custo${hab12Count}" name="habilidade12Custo${hab12Count}" placeholder="Custo do habilidade">
        </div class='habilidade-row-miniContainer'>
        <div class='habilidade-row-miniContainer'>
            <label for="habilidade12Desc${hab12Count}">Descrição do habilidade:</label>
            <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="habilidade12Desc${hab12Count}" name="habilidade12Desc${hab12Count}" placeholder="Descrição do habilidade"></textarea>
        </div>
    </div>
`;

        hab12Container.appendChild(habilidadeRow);
    }
});
