function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

const addEfeitosBtn = document.getElementById("addEfeito");
const efeitosContainer = document.getElementById("efeitosContainer");
let efeitosCount = 0; // Counter to keep track of attribute rows
let nucleo = 0; // Contador para Nucleos
let triunfo = 0; // Contador para Triunfos

addEfeitosBtn.addEventListener("click", function () {
  efeitosCount++; // Increment counter for each new attribute row

  const efeitoRow = document.createElement("div");
  efeitoRow.classList.add("efeito-row");
  efeitoRow.innerHTML = `
<div class="parent">
    <div class="div1">
        <label for="efeitoTipo${efeitosCount}">Tipo do Efeito</label>        
    </div>
    <div class="div2">
        <select class='personagem_select' id="efeitoTipo${efeitosCount}" name="efeitoTipo${efeitosCount}">
            <option value="efeitoPassivo" selected> Efeito Passivo</option>
            <option value="efeitoAtivo"> Efeito Ativo</option>
            <option value="efeitoAura"> Efeito Aura</option>
            <option value="nucleo"> Nucleo</option>
            <option value="triunfo"> Triunfo</option>        
        </select>
    </div>
    <div class="div3">
        <label for="efeitoNome${efeitosCount}">Nome do Efeito:</label>
    </div>
    <div class="div4">
        <input style="width: 100%"; type="text" id="efeitoNome${efeitosCount}" name="efeitoNome${efeitosCount}" placeholder="Nome do efeito">
    </div>
    <div class="div5">
        <label for="efeitoDesc${efeitosCount}">Descrição do Efeito:</label>
    </div>
    <div class="div6">
        <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="efeitoDesc${efeitosCount}" name="efeitoDesc${efeitosCount}" placeholder="Descrição do Efeito"></textarea>
    </div>
</div>



    
        `;
    efeitosContainer.appendChild(efeitoRow);
});
