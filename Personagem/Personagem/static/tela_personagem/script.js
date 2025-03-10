function selecionarPersonagem() {
    var select = document.getElementById("personagem_select");
    var personagem_id = select.value;
    window.location.href = "/" + personagem_id + "/";
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

    
];

let algumAtributoInvalido = false; // Flag para verificar se algum atributo é inválido

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
        // Calcula o bônus e formata
        let bonus = valor / 100;
        bonus = bonus.toFixed(2);
        bonus = Math.trunc(bonus); // Remove as casas decimais (arredonda para baixo)
        bonus = "——————— +" +bonus; // Adiciona o sinal de mais

        bonusElement.innerText = bonus; // Exibe o bônus
    }

    return valor; // Retorna o valor formatado
}

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

    if (vazio) {
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
//função passada, a função atual
window.onload = function () {
    atualizarTela();
}