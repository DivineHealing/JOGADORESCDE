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

function createHabilidadeRow(grupo) {
    if (!(grupo in habilidadeCounters)) {
        console.warn(`Grupo "${grupo}" não está registrado.`);
        return;
    }

    const container = document.getElementById(`${grupo}Container`);
    const count = ++habilidadeCounters[grupo];

    if (count > 6) {
        alert(`Você só pode adicionar até 6 habilidades para ${grupo.toUpperCase()}.`);
        return;
    }

    const row = document.createElement('div');
    row.classList.add('habilidade-row');

    row.innerHTML = `
        <div class='habilidade-row-container'>
            <div class='habilidade-row-miniContainer'>
                <label for="${grupo}Tipo${count}">Tipo da Habilidade</label>
                <select class='personagem_select' id="${grupo}Tipo${count}" name="${grupo}tipo${count}">
                    <option value="habilidadePassivo" selected>Habilidade Passivo</option>
                    <option value="habilidadeAtivo">Habilidade Ativo</option>
                    <option value="habilidadeAura">Habilidade Aura</option>
                </select>

                <label for="${grupo}Nivel${count}">Nível da Habilidade</label>
                <select class='personagem_select' id="${grupo}Nivel${count}" name="${grupo}nivel${count}_">
                    <option value="nivel2" selected>Nível 2</option>
                    <option value="nivel3">Nível 3</option>
                    <option value="nivel4">Nível 4</option>
                    <option value="nivel5">Nível 5</option>
                    <option value="nivel6">Nível 6</option>
                </select>
            </div>

            <div class='habilidade-row-miniContainer'>
                <label for="${grupo}Nome${count}">Nome da Habilidade:</label>
                <input style="width: 100%;" type="text" id="${grupo}Nome${count}" name="${grupo}nome${count}" placeholder="Nome da Habilidade">

                <label for="${grupo}Custo${count}">Custo da Habilidade:</label>
                <input style="width: 50%;" type="text" id="${grupo}Custo${count}" name="${grupo}custo${count}" placeholder="Custo da Habilidade">
            </div>

            <div class='habilidade-row-miniContainer'>
                <label for="${grupo}Desc${count}">Descrição da Habilidade:</label>
                <textarea 
                    style="width: 100%; height: 10em;" 
                    id="${grupo}Descricao${count}" 
                    name="${grupo}Descricao${count}" 
                    placeholder="Descrição da Habilidade" 
                    wrap="hard"
                ></textarea>
            </div>
        </div>
    `;

    container.appendChild(row);
}

document.querySelectorAll('.add-atributo-btn').forEach(button => {
    button.addEventListener('click', () => {
        const grupo = button.dataset.group;
        createHabilidadeRow(grupo);
    });
});
