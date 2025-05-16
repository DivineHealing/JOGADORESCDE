function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}


const habilidadeCounters = {
    habilidade1: 1, // Começa do 1 porque o primeiro já existe no HTML
    habilidade2: 1,
    habilidade3: 1,
    habilidade4: 1,
    habilidade5: 1,
    habilidade6: 1,
    habilidade7: 1,
    habilidade8: 1,
    habilidade9: 1,
    habilidade10: 1,
    habilidade11: 1,
    habilidade12: 1,
    // Adicione mais grupos conforme necessário
};

function createHabilidadeRow(grupo, nivel, dados = {}) {
    if (!grupo || !nivel) {
        console.error("❌ Erro: Grupo ou Nível não fornecido corretamente!", { grupo, nivel, dados });
        return;
    }

    const container = document.getElementById(`${grupo}Container`);

    const tipo = dados.tipo || 'habilidadePassivo';
    const nome = dados.nome || '';
    const custo = dados.custo || '';
    const descricao = dados.descricao || '';

    const row = document.createElement('div');
    row.classList.add('habilidade-row');

    row.innerHTML = `
        <div class='habilidade-row-container'>        
            <div class='habilidade-row-miniContainer'>
                <span style="margin-bottom: 1.2em; font-size:1.5em" name="${grupo}Nome${nivel}"><strong>Nível ${nivel}</strong></span>
                <label for="${grupo}Tipo${nivel}">Tipo da Habilidade</label>
                <select class='personagem_select' id="${grupo}Tipo${nivel}" name="${grupo}Tipo${nivel}">
                    <option value="Passivo" ${tipo === 'habilidadePassivo' ? 'selected' : ''}>Habilidade Passivo</option>
                    <option value="Ativo" ${tipo === 'habilidadeAtivo' ? 'selected' : ''}>Habilidade Ativo</option>
                    <option value="Aura" ${tipo === 'habilidadeAura' ? 'selected' : ''}>Habilidade Aura</option>
                </select>
            </div>

            <div class='habilidade-row-miniContainer'>
                <label for="${grupo}Nome${nivel}">Nome da Habilidade:</label>
                <input style="width: 100%;" type="text" id="${grupo}Nome${nivel}" name="${grupo}Nome${nivel}" value="${nome}">

                <label for="${grupo}Custo${nivel}">Custo da Habilidade:</label>
                <input style="width: 50%;" type="text" id="${grupo}Custo${nivel}" name="${grupo}Custo${nivel}" value="${custo}">
            </div>

            <div class='habilidade-row-miniContainer'>
                <label for="${grupo}Desc${nivel}">Descrição da Habilidade:</label>
                <textarea style="width: 100%; height: 10em;" id="${grupo}Desc${nivel}" name="${grupo}Desc${nivel}" wrap="hard">${descricao}</textarea>
            </div>
        </div>
    `;

    container.appendChild(row);
}


document.addEventListener("DOMContentLoaded", function () {
    const habilidadesElement = document.getElementById('all-habilidades-data');
    const habilidadesArray = JSON.parse(habilidadesElement.textContent);

    habilidadesArray.forEach(dado => {
        const id = dado.id; // Ex: 1
        dado.niveis.forEach(nivelData => {
            const nivelNumero = nivelData.nivel;
            createHabilidadeRow(`habilidade${id}`, nivelNumero, nivelData);
            habilidadeCounters[`habilidade${id}`] = nivelNumero; // Atualiza o contador
        });
    });

    document.querySelectorAll('.add-atributo-btn').forEach(button => {
        button.addEventListener('click', () => {
            const grupo = button.dataset.group;
            habilidadeCounters[grupo]++; // agora será só uma vez
            const count = habilidadeCounters[grupo];

            console.log(`Grupo: ${grupo}, Contador: ${count}`);

            if (count <= 6) {
                createHabilidadeRow(grupo, count);
            } else {
                alert("Você já adicionou todas as habilidades até o nível 6.");
            }
        });
    });
});
