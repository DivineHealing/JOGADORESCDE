function selecionarPersonagem() {
    var select = document.getElementById("personagem_select");
    var personagem_id = select.value;
    window.location.href = "/" + personagem_id + "/";
}


const deleter = document.getElementById("deleter");

function validarNome() {
    const input = document.getElementById("impDel");
    const select = document.getElementById("personagem_select");
    const personagemId = select.value; // Pega o ID do personagem do <option> selecionado
    const selectedOption = select.options[select.selectedIndex]; // Pega o elemento <option>
    const personagemNome = selectedOption.text; // Pega o nome para confirmação
    deleter.style.display = "none";
    if (personagemNome == input.value){
        deleter.style.display = "";
    }    

    //var personagem = select.value;
    console.log(personagemNome)
}

const atributos = [
    { nome: "regenVida", containerId:"regenVida_container"},
    { nome: "regenMana", containerId:"regenMana_container"},
    { nome: "regenVigor", containerId:"regenVigor_container"},

    { nome: "forca", containerId:"forca_container", bonusElementId: "forcaBonus" },
    { nome: "destreza", containerId:"destreza_container", bonusElementId: "destrezaBonus"},
    { nome: "inteligencia", containerId:"inteligencia_container", bonusElementId: "inteligenciaBonus"},
    { nome: "determinacao", containerId:"determinacao_container", bonusElementId: "determinacaoBonus"},
    { nome: "perspicacia", containerId:"perspicacia_container", bonusElementId: "perspicaciaBonus"},
    { nome: "carisma", containerId:"carisma_container", bonusElementId: "carismaBonus"},

    { nome: "danoFixo_1", containerId: "danoFixo1_container"},
    { nome: "penetracao_1", containerId: "penetracao1_container"},
    { nome: "danoFixo_2", containerId: "danoFixo2_container"},
    { nome: "penetracao_2", containerId: "penetracao2_container"},
    { nome: "danoFixo_3", containerId: "danoFixo3_container"},
    { nome: "penetracao_3", containerId: "penetracao3_container"},
    { nome: "danoFinal", containerId: "danoFinal_container"},

    { nome: "defesaFixa_1", containerId: "defesaFixa1_container" },
    { nome: "resistencia_1", containerId: "resistencia1_container"},
    { nome: "defesaFixa_2", containerId: "defesaFixa2_container" },
    { nome: "resistencia_2", containerId: "resistencia2_container"},
    { nome: "defesaFixa_3", containerId: "defesaFixa3_container" },
    { nome: "resistencia_3", containerId: "resistencia3_container"},
    { nome: "defesaFixa_4", containerId: "defesaFixa4_container" },
    { nome: "resistencia_4", containerId: "resistencia4_container"},
    { nome: "defesaFixa_5", containerId: "defesaFixa5_container" },
    { nome: "resistencia_5", containerId: "resistencia5_container"},

    { nome: "rolagem1", containerId: "rolagem1_container"},
    { nome: "rolagem2", containerId: "rolagem2_container"},
    { nome: "rolagem3", containerId: "rolagem3_container"},
    { nome: "rolagem4", containerId: "rolagem4_container"},
    { nome: "rolagem5", containerId: "rolagem5_container"},
    { nome: "rolagem6", containerId: "rolagem6_container"},
    { nome: "rolagem7", containerId: "rolagem7_container"},
    { nome: "rolagem8", containerId: "rolagem8_container"},
    { nome: "rolagem9", containerId: "rolagem9_container"},
    { nome: "rolagem10", containerId: "rolagem10_container"},
    { nome: "rolagem11", containerId: "rolagem11_container"},
    { nome: "rolagem12", containerId: "rolagem12_container"},
    { nome: "rolagem13", containerId: "rolagem13_container"},
    { nome: "rolagem14", containerId: "rolagem14_container"},
    { nome: "rolagem15", containerId: "rolagem15_container"},
    { nome: "rolagem15", containerId: "rolagem15_container"},
    { nome: "rolagem16", containerId: "rolagem16_container"},
    { nome: "rolagem17", containerId: "rolagem17_container"},
    { nome: "rolagem18", containerId: "rolagem18_container"},
    { nome: "rolagem19", containerId: "rolagem19_container"},
    { nome: "rolagem20", containerId: "rolagem20_container"},
    { nome: "rolagem21", containerId: "rolagem21_container"},
    { nome: "rolagem22", containerId: "rolagem22_container"},
    { nome: "rolagem23", containerId: "rolagem23_container"},
    { nome: "rolagem24", containerId: "rolagem24_container"},
    { nome: "rolagem25", containerId: "rolagem25_container"},

    { nome: "amplificacao1", containerId: "amplificacao1_container" },
    { nome: "amplificacao2", containerId: "amplificacao2_container"},
    { nome: "amplificacao3", containerId: "amplificacao3_container" },
    { nome: "amplificacao4", containerId: "amplificacao4_container"},
    { nome: "amplificacao5", containerId: "amplificacao5_container" },
    { nome: "amplificacao6", containerId: "amplificacao6_container"},
    { nome: "amplificacao7", containerId: "amplificacao7_container" },
    { nome: "amplificacao8", containerId: "amplificacao8_container"},
    { nome: "amplificacao9", containerId: "amplificacao9_container" },
    { nome: "amplificacao10", containerId: "amplificacao10_container"},
    { nome: "amplificacao11", containerId: "amplificacao11_container" },
    { nome: "amplificacao12", containerId: "amplificacao12_container"},
    { nome: "amplificacao13", containerId: "amplificacao13_container" },
    { nome: "amplificacao14", containerId: "amplificacao14_container"},
    { nome: "amplificacao15", containerId: "amplificacao15_container" },

    

    { nome: "outros1", containerId: "outros1_container" },
    { nome: "outros2", containerId: "outros2_container"},
    { nome: "outros3", containerId: "outros3_container" },
    { nome: "outros4", containerId: "outros4_container"},
    { nome: "outros5", containerId: "outros5_container" },
    { nome: "outros6", containerId: "outros6_container"},
    { nome: "outros7", containerId: "outros7_container" },
    { nome: "outros8", containerId: "outros8_container"},
    { nome: "outros9", containerId: "outros9_container" },
    { nome: "outros10", containerId: "outros10_container"},
    { nome: "outros11", containerId: "outros11_container" },
    { nome: "outros12", containerId: "outros12_container"},
    { nome: "outros13", containerId: "outros13_container" },
    { nome: "outros14", containerId: "outros14_container"},
    { nome: "outros15", containerId: "outros15_container" },
];

let algumAtributoInvalido = false; // Flag para verificar se algum atributo é inválido

// FUNÇÃO PARA FORMATAR OS NUMEROS MILHARES
function formatarAtributo(atributo) {
    const element = document.getElementById(atributo.nome);
    const bonusElement = document.getElementById(atributo.bonusElementId);

    if (!element) {
        console.warn(`Elemento '${atributo.nome}' não encontrado.`);
        return null; // Retorna null se o elemento não for encontrado
    }

    let valorTexto = element.innerText; // Obtém o texto do elemento
    valorTexto = valorTexto.replace(/\./g, ''); // Remove todos os pontos (separadores de milhar)
    let valor = parseFloat(valorTexto);

    if (isNaN(valor) || valor < 0) {
        console.warn(`Valor inválido para '${atributo.nome}'. Definindo como 0.`);
        return null; // Retorna null se o valor for inválido
    }

    if (bonusElement) {
        let maior = 0
        if (bonusElement > maior) { maior == bonusElement.length };
        // Calcula o bônus e formata
        let bonus = valor / 100;
        bonus = bonus.toFixed(2);
        bonus = Math.trunc(bonus); // Remove as casas decimais (arredonda para baixo)
        bonus = "— "+' +'+bonus; // Adiciona o sinal de mais

        bonusElement.innerText = bonus; // Exibe o bônus
    }

    return valor; // Retorna o valor formatado
}

// FUNÇÃO PARA OCULTAR OS DADOS ZERADOS
function exibirOuOcultarAtributo(atributo) {
    const element = document.getElementById(atributo.nome);
    const containerElement = document.getElementById(atributo.containerId);
    

    if (!element) {
        console.warn(`Elemento '${atributo.nome}' não encontrado.`);
        return;
    }

    let valorTexto = element.innerText;

    // Remove separadores de milhar e espaços em branco
    valorTexto = valorTexto.replace(/\./g, '').trim();

    // Converte para número se for um número, senão mantém como string
    let valor;
    if (!isNaN(parseFloat(valorTexto)) && isFinite(valorTexto)) {
        valor = parseFloat(valorTexto); // Converte para número
    } else {
        valor = valorTexto; // Mantém como string
    }

    // Verifica se o valor é "vazio" (zero para números, string vazia ou null)
    let vazio = (typeof valor === 'number' && valor === 0) || (typeof valor === 'string' && valor.trim() === "") || valor === null;

    if (!containerElement) {
        console.error(`Container '${atributo.containerId}' não encontrado.`);
        return;
    }
    if (vazio && atributo.nome != "forca" && atributo.nome != "destreza" && atributo.nome != "inteligencia" && atributo.nome != "determinacao" && atributo.nome != "perspicacia" && atributo.nome != "carisma") {
        containerElement.style.display = 'none';
    } else {
        containerElement.style.display = 'block';
    }
}

function atualizarTela() {
    for (const atributo of atributos) {
        const valor = formatarAtributo(atributo); // Formata o atributo
        exibirOuOcultarAtributo(atributo, valor); // Exibe ou oculta o container
    }
}
// FUNÇÃO DE ATUALIZAR A TELA - ATUALIZAR DADOS PUXADOS DO BANCO
window.onload = function () {
    atualizarTela();
}

// FUNÇÃO DE BUFF
document.addEventListener('DOMContentLoaded', function () {
    const buffButtons = document.querySelectorAll('.buff-button');

    buffButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const fieldName = this.dataset.field;
            const buffInput = document.getElementById(`${fieldName}BuffInput`);
            const buffedValueSpan = document.getElementById(`${fieldName}Buffed`);
            const originalValueSpan = document.getElementById(fieldName);

            originalValueSpan.classList.add('hidden');  // Esconde o valor original
            buffInput.classList.remove('hidden');       // Mostra o input
            buffInput.focus();

            // Remove os listeners existentes (se houver)
            buffInput.removeEventListener('blur', handleBuff);
            buffInput.removeEventListener('keydown', handleEnter);
            buffInput.removeEventListener('keypress', handleF);

            // Adiciona os novos listeners
            buffInput.addEventListener('blur', handleBuff);
            buffInput.addEventListener('keydown', handleEnter);
            buffInput.addEventListener('keypress', handleF);

            function handleBuff() {
                buffInput.removeEventListener('blur', handleBuff);
                buffInput.removeEventListener('keydown', handleEnter); // Remove também o listener de Enter
                buffInput.removeEventListener('keypress', handleF); // Remove também o listener de Enter

                const buffValue = parseInt(buffInput.value, 10) || 0;
                const originalValue = parseInt(originalValueSpan.textContent.replace(/\./g, ''), 10) || 0;

                const totalValue = Math.trunc(originalValue * ((buffValue / 100) + 1));

                buffedValueSpan.textContent = totalValue.toLocaleString('pt-BR');
                buffedValueSpan.classList.remove('hidden');

                buffInput.classList.add('hidden');
                originalValueSpan.classList.remove('hidden');

                buffInput.value = '';
            }

            function handleBuffFixo() {
                buffInput.removeEventListener('blur', handleBuff);
                buffInput.removeEventListener('keypress', handleF); // Remove também o listener de Enter
                buffInput.removeEventListener('keydown', handleEnter); // Remove também o listener de Enter

                const buffValue = parseInt(buffInput.value, 10) || 0;
                const originalValue = parseInt(originalValueSpan.textContent.replace(/\./g, ''), 10) || 0;

                const totalValue = Math.trunc(originalValue + buffValue);

                buffedValueSpan.textContent = totalValue.toLocaleString('pt-BR');
                buffedValueSpan.classList.remove('hidden');

                buffInput.classList.add('hidden');
                originalValueSpan.classList.remove('hidden');

                buffInput.value = '';
            }

            function handleEnter(event) {
                if (event.key === 'Enter') {
                    handleBuff();
                    event.preventDefault();
                }            
            }
            function handleF(event) {
                if (event.key === 'F') {
                    handleBuffFixo();
                    event.preventDefault();
                }
            }
        });
    });
});


const cadastroNovo = document.getElementById("cadastrarNovo");
const deletar = document.getElementById("deletar");
const selecao = document.getElementById("personagem_select");
const selecaoLb = document.getElementById("selectLabel");

const novoPersonagem = document.getElementById("novoPersonagem")

const btnCad = document.getElementById("btnCad")
const btnDel = document.getElementById("btnDel")
const btnSalvar = document.getElementById("btnSalvar")

btnCad.addEventListener('click', function(){
    cadastroNovo.style.display = "block";
    selecao.style.display = "none";
    btnCad.style.display = "none";
    btnDel.style.display = "none";
    selecaoLb.style.display = "none";
});

btnDel.addEventListener('click', function(){
    deletar.style.display = "block";
    selecao.style.display = "none";
    btnCad.style.display = "none";
    selecaoLb.style.display = "none";
    btnDel.style.display = "none";
});

/* Layout para botão

const btnCad = document.getElementById("btnCad")
btnCad.addEventListener('click', function(){
    console.log("Teste")
});

*/