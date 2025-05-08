function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
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
    { nome: "vida", containerId:"vida"},
    { nome: "mana", containerId:"mana"},
    { nome: "vigor", containerId:"vigor"},
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
    { nome: "danoFixo_4", containerId: "danoFixo4_container"},
    { nome: "penetracao_4", containerId: "penetracao4_container"},
    { nome: "danoFixo_5", containerId: "danoFixo5_container"},
    { nome: "penetracao_5", containerId: "penetracao5_container"},
    { nome: "danoFixo_6", containerId: "danoFixo6_container"},
    { nome: "penetracao_6", containerId: "penetracao6_container"},
    { nome: "danoFixo_7", containerId: "danoFixo7_container"},
    { nome: "penetracao_7", containerId: "penetracao7_container"},
    { nome: "esmagamento", containerId: "esmagamento_container"},
    { nome: "penExtra", containerId: "penExtra_container"},
    { nome: "danoFinal", containerId: "danoFinal_container"},
    { nome: "espiritualFixo", containerId: "espiritualFixo_container"},
    { nome: "espiritualPerc", containerId: "espiritualPerc_container"},

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
    { nome: "defesaFixa_6", containerId: "defesaFixa6_container" },
    { nome: "resistencia_6", containerId: "resistencia6_container"},
    { nome: "defesaFixa_7", containerId: "defesaFixa7_container" },
    { nome: "resistencia_7", containerId: "resistencia7_container"},
    { nome: "defesaFixaEspiritual", containerId: "defesaFixaEspiritual_container"},
    { nome: "reducaoEspiritual", containerId: "reducaoEspiritual_container" },
    { nome: "reducao", containerId: "reducao_container"},

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

    { nome: "amplificacao1", containerId: "amplificacao1_container"},
    { nome: "amplificacao2", containerId: "amplificacao2_container"},
    { nome: "amplificacao3", containerId: "amplificacao3_container"},
    { nome: "amplificacao4", containerId: "amplificacao4_container"},
    { nome: "amplificacao5", containerId: "amplificacao5_container"},
    { nome: "amplificacao6", containerId: "amplificacao6_container"},
    { nome: "amplificacao7", containerId: "amplificacao7_container"},
    { nome: "amplificacao8", containerId: "amplificacao8_container"},
    { nome: "amplificacao9", containerId: "amplificacao9_container"},
    { nome: "amplificacao10", containerId: "amplificacao10_container"},
    { nome: "amplificacao11", containerId: "amplificacao11_container"},
    { nome: "amplificacao12", containerId: "amplificacao12_container"},
    { nome: "amplificacao13", containerId: "amplificacao13_container"},
    { nome: "amplificacao14", containerId: "amplificacao14_container"},
    { nome: "amplificacao15", containerId: "amplificacao15_container"},
    { nome: "amplificacao16", containerId: "amplificacao16_container"},
    { nome: "amplificacao17", containerId: "amplificacao17_container"},
    { nome: "amplificacao18", containerId: "amplificacao18_container"},
    { nome: "amplificacao19", containerId: "amplificacao19_container"},
    { nome: "amplificacao20", containerId: "amplificacao20_container"},
    { nome: "amplificacao21", containerId: "amplificacao21_container"},
    { nome: "amplificacao22", containerId: "amplificacao22_container"},
    { nome: "amplificacao23", containerId: "amplificacao23_container"},
    { nome: "amplificacao24", containerId: "amplificacao24_container"},
    { nome: "amplificacao25", containerId: "amplificacao25_container"},

    { nome: "outros1", containerId: "outros1_container"},
    { nome: "outros2", containerId: "outros2_container"},
    { nome: "outros3", containerId: "outros3_container"},
    { nome: "outros4", containerId: "outros4_container"},
    { nome: "outros5", containerId: "outros5_container"},
    { nome: "outros6", containerId: "outros6_container"},
    { nome: "outros7", containerId: "outros7_container"},
    { nome: "outros8", containerId: "outros8_container"},
    { nome: "outros9", containerId: "outros9_container"},
    { nome: "outros10", containerId: "outros10_container"},
    { nome: "outros11", containerId: "outros11_container"},
    { nome: "outros12", containerId: "outros12_container"},
    { nome: "outros13", containerId: "outros13_container"},
    { nome: "outros14", containerId: "outros14_container"},
    { nome: "outros15", containerId: "outros15_container"},
];

let algumAtributoInvalido = false; // Flag para verificar se algum atributo é inválido

function atualizarTela() {
    for (const atributo of atributos) {
        // Só continua se o container realmente existe
        if (document.getElementById(atributo.containerId)) {
            const valor = formatarAtributo(atributo);
            exibirOuOcultarAtributo(atributo, valor);
        }
    }
}

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
        console.log(valor)
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
    valorTexto = valorTexto.replace(/\./g, '')  // Remove pontos (ex: 1.000 -> 1000)
                       .replace(/,/g, '.')   // Troca vírgula por ponto (ex: "0,00" -> "0.00")
                       .trim();

    // Converte para número se for um número, senão mantém como string
    let valor;
    if (!isNaN(parseFloat(valorTexto)) && isFinite(valorTexto)) {
        valor = parseFloat(valorTexto); // Converte para número
    } else {
        valor = valorTexto; // Mantém como string
    }
    // Verifica se o valor é "vazio" (zero para números, string vazia ou null)
    let vazio = (valor === null || valor === undefined) || // Checa null/undefined primeiro
                (typeof valor === 'number' && (valor === 0 || isNaN(valor))) || // Checa 0 ou NaN
                (typeof valor === 'string' && valor.trim() === "");

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
document.addEventListener("DOMContentLoaded", function () {
    atualizarTela();
});

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

document.addEventListener('DOMContentLoaded', function() {
    // 1. Obter os dados formatados das habilidades
    const habilidadesDataElement = document.getElementById('all-habilidades-data');
    let allHabilidadesData = {};
    let dataArray = []; // INICIALIZA COMO ARRAY VAZIO POR PADRÃO

    if (habilidadesDataElement && habilidadesDataElement.textContent) {
        try {
            const parsedData = JSON.parse(habilidadesDataElement.textContent);

            // *** VERIFICAÇÃO CRÍTICA ***
            // Checa se o resultado do parse é realmente um array
            if (Array.isArray(parsedData)) {
                dataArray = parsedData; // Usa o array parseado
            } else {
                 // Se não for array (pode ser null, objeto, etc.), mantém dataArray como []
                 console.warn("Os dados parseados de 'all-habilidades-data' não são um array. Tratando como vazio.", parsedData);
            }

        } catch (e) {
            console.error("Erro ao parsear dados das habilidades:", e);
            // Mantém dataArray como [] em caso de erro de parse
        }
    } else {
        console.warn("Elemento 'all-habilidades-data' ou seu conteúdo não encontrado. Tratando como vazio.");
        // Mantém dataArray como []
    }

    // Converte o array (possivelmente vazio) em um objeto/map
    dataArray.forEach(hab => { // Agora seguro usar forEach
        allHabilidadesData[hab.id] = hab;
    });


    const titulos = document.querySelectorAll('.habilidade-titulo');
    const allDetalhesDivs = document.querySelectorAll('.habilidade-detalhes');

    // --- O resto do seu código continua aqui ---
    // (A lógica de adicionar listeners e popular os detalhes)
    // ...

     titulos.forEach(titulo => {
        const slotId = titulo.dataset.slotId;
        const detalhesDiv = document.querySelector(`.habilidade-detalhes[data-details-for="${slotId}"]`);

        if (!detalhesDiv) {
            console.warn(`Div de detalhes não encontrado para slot ID: ${slotId}`);
            return;
        }

        titulo.addEventListener('click', (event) => {
            event.stopPropagation();

            const isCurrentlyVisible = detalhesDiv.classList.contains('visible');

            allDetalhesDivs.forEach(div => {
                if (div !== detalhesDiv) {
                    div.classList.remove('visible');
                }
            });

            if (!isCurrentlyVisible) {
                const habilidadeData = allHabilidadesData[slotId]; // Busca pelo slot ID
                // Verifica se ENCONTROU os dados para este slot específico
                if (!habilidadeData || !habilidadeData.niveis) {
                    console.error(`Dados formatados não encontrados no objeto JS para slot ID: ${slotId}`);
                    detalhesDiv.innerHTML = '<p>Detalhes não disponíveis.</p>';
                    detalhesDiv.classList.add('visible');
                    return;
                }

                // --- Restante da lógica para popular detalhes ---
                detalhesDiv.innerHTML = ''; // Limpa
                habilidadeData.niveis.forEach(nivelData => {
                    // ... (código para criar nivelDiv e nivelHTML) ...
                     const nivelDiv = document.createElement('div');
                    nivelDiv.classList.add('nivel-info');

                    let nivelHTML = `<p style="color: Orange;"><strong>Nível ${nivelData.nivel}:</strong></p>`;
                    if (nivelData.custo) { nivelHTML += `<p><strong style="color: red;">Custo:</strong> ${nivelData.custo}</p>`; }
                    if (nivelData.tipo) { nivelHTML += `<p><strong style="color: red;">Tipo:</strong> ${nivelData.tipo}</p>`; }
                    if (nivelData.descricao) {
                        const descFormatada = nivelData.descricao.replace(/\r\n|\r|\n/g, '<br>');
                        nivelHTML += `<p><strong style="color: red;">Descrição:</strong></p>`;
                        nivelHTML += `<span style="font-style: Italic">${descFormatada}</span>`;
                        nivelHTML += `<p>_______________________________________________________</p>`
                    }
                     // if (nivelData.notas) { nivelHTML += `<p><em>${nivelData.notas}</em></p>`; }

                    nivelDiv.innerHTML = nivelHTML;
                    detalhesDiv.appendChild(nivelDiv);
                });
                 // --- Fim da lógica para popular detalhes ---

                detalhesDiv.classList.add('visible');

            } else {
                detalhesDiv.classList.remove('visible');
            }
        });

         detalhesDiv.addEventListener('click', (event) => {
             event.stopPropagation();
         });
    });

    // Fecha ao clicar fora
    document.addEventListener('click', () => {
        allDetalhesDivs.forEach(div => {
            div.classList.remove('visible');
        });
    });

    // Acessibilidade com Teclado
     titulos.forEach(titulo => {
        titulo.addEventListener('keydown', (event) => {
             if (event.key === 'Enter' || event.key === ' ') {
                 event.preventDefault();
                 titulo.click();
             }
             if (event.key === 'Escape') {
                 const slotId = titulo.dataset.slotId;
                 const detalhesDiv = document.querySelector(`.habilidade-detalhes[data-details-for="${slotId}"]`);
                 if (detalhesDiv && detalhesDiv.classList.contains('visible')) {
                     detalhesDiv.classList.remove('visible');
                 }
             }
         });
     });


}); // Fim do DOMContentLoaded
