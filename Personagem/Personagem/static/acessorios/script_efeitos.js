function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

const addEfeitosAcessoriosBtn = document.getElementById("addEfeitoAcessorios");
const efeitosAcessoriosContainer = document.getElementById("efeitosAcessoriosContainer");
let efeitosAcessoriosCount = 0; // Counter to keep track of attribute rows
let nucleo = 0; // Contador para Nucleos
let triunfo = 0; // Contador para Triunfos

addEfeitosAcessoriosBtn.addEventListener("click", function () {
  efeitosAcessoriosCount++; // Increment counter for each new attribute row

  const efeitoAcessoriosRow = document.createElement("div");
  efeitoAcessoriosRow.classList.add("efeito-row");
  efeitoAcessoriosRow.innerHTML = `
<div class="parent">
    <div class="div1">
        <label for="efeitoTipo${efeitosAcessoriosCount}">Tipo do Efeito</label>        
    </div>
    <div class="div2">
        <select class='personagem_select' id="efeitoTipo${efeitosAcessoriosCount}" name="efeitoTipo${efeitosAcessoriosCount}">
            <option value="efeitoPassivo" selected> Efeito Passivo</option>
            <option value="efeitoAtivo"> Efeito Ativo</option>
            <option value="efeitoAura"> Efeito Aura</option>
            <option value="nucleo"> Nucleo</option>
            <option value="triunfo"> Triunfo</option>        
        </select>
    </div>
    <div class="div3">
        <label for="efeitoNome${efeitosAcessoriosCount}">Nome do Efeito:</label>
    </div>
    <div class="div4">
        <input style="width: 100%"; type="text" id="efeitoNome${efeitosAcessoriosCount}" name="efeitoNome${efeitosAcessoriosCount}" placeholder="Nome do efeito">
    </div>
    <div class="div5">
        <label for="efeitoAcessoriosDesc${efeitosAcessoriosCount}">Descrição do Efeito:</label>
    </div>
    <div class="div6">
        <textarea style="width: 100%; height: 10em; wrap: "hard""; type="text" id="efeitoDesc${efeitosAcessoriosCount}" name="efeitoDesc${efeitosAcessoriosCount}" placeholder="Descrição do Efeito"></textarea>
    </div>
</div>



    
        `;
    efeitosAcessoriosContainer.appendChild(efeitoAcessoriosRow);
});

