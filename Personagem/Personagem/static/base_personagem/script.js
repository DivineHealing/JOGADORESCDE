function selecionarPersonagem() {
    const select = document.getElementById("personagem_select");
    const selectedOption = select.options[select.selectedIndex];
    const url = selectedOption.getAttribute("data-url");
    if (url) {
        window.location.href = url;
    }
}

// TENTATIVA DE EXIBIR OS DADOS DINAMICOS

document.addEventListener('DOMContentLoaded', function () {
    const maxPorTipo = {
        defesa: 5,
        dano: 5,
        rolagem: 15,
        amplificacao: 15,
        regeneracao: 3
    };

    function safeParse(id) {
        try {
            return JSON.parse(document.getElementById(id).textContent);
        } catch {
            return [];
        }
    }
    
    const defesas = safeParse("defesas-preexistentes-json");
    const resistencias = safeParse("resistencias-preexistentes-json");
    const danos = safeParse("danos-preexistentes-json");
    const penetracoes = safeParse("penetracoes-preexistentes-json");
    const rolagens = safeParse("rolagens-preexistentes-json");
    const amplificacoes = safeParse("amplificacoes-preexistentes-json");
    const regeneracoes = safeParse("regeneracoes-preexistentes-json");

    function criarLinha(container, index, tipo, dados = {}) {
        let linha = document.createElement('div');
        linha.className = `${tipo}-row`;

        switch (tipo) {
            case 'defesa':
                linha.innerHTML = `
                    <div>
                        <label for="elementoDefesa${index}">Elemento</label>
                        <input type="text" id="elementoDefesa${index}" name="elementoDefesa${index}" value="${dados.elemento || ''}">
                    </div>
                    <div>
                        <label for="defesa${index}">Defesa Fixa</label>
                        <input type="number" id="defesa${index}" name="defesa${index}" value="${dados.defesa || 0}">
                    </div>
                    <div>
                        <label for="resistencia${index}">Resistência</label>
                        <input type="number" id="resistencia${index}" name="resistencia${index}" value="${dados.resistencia || 0}">
                    </div>
                `;
                break;

            case 'dano':
                linha.innerHTML = `
                    <div>
                        <label for="elementoDano${index}">Elemento</label>
                        <input type="text" id="elementoDano${index}" name="elementoDano${index}" value="${dados.elemento || ''}">
                    </div>
                    <div>
                        <label for="dano${index}">Dano Fixo</label>
                        <input type="number" id="dano${index}" name="dano${index}" value="${dados.dano || 0}">
                    </div>
                    <div>
                        <label for="penetracao${index}">Penetração</label>
                        <input type="number" id="penetracao${index}" name="penetracao${index}" value="${dados.penetracao || 0}">
                    </div>
                `;
                break;

            case 'rolagem':
                linha.innerHTML = `
                    <div>
                        <label for="rolagemTipo${index}">Tipo</label>
                        <input type="text" id="rolagemTipo${index}" name="rolagemTipo${index}" value="${dados.tipo || ''}">
                    </div>
                    <div>
                        <label for="rolagem${index}">Valor</label>
                        <input type="number" id="rolagem${index}" name="rolagem${index}" value="${dados.valor || 0}">
                    </div>
                `;
                break;

            case 'amplificacao':
                linha.innerHTML = `
                    <div>
                        <label for="amplificacaoTipo${index}">Tipo</label>
                        <input style="width: 17em" type="text" id="amplificacaoTipo${index}" name="amplificacaoTipo${index}" value="${dados.tipo || ''}">
                    </div>
                    <div>
                        <label for="amplificacao${index}">Valor</label>
                        <input type="number" id="amplificacao${index}" name="amplificacao${index}" value="${dados.valor || 0}">
                    </div>
                `;
                break;

            case 'regeneracao':
                linha.innerHTML = `
                    <div>
                        <label for="regeneracaoTipo${index}">Tipo</label>
                        <select class='personagem_select' id="regeneracaoTipo${index}" name="regeneracaoTipo${index}">
                            <option value="regenVida" ${dados.tipo === 'regenVida' ? 'selected' : ''}>Vida</option>
                            <option value="regenMana" ${dados.tipo === 'regenMana' ? 'selected' : ''}>Mana</option>
                            <option value="regenVigor" ${dados.tipo === 'regenVigor' ? 'selected' : ''}>Vigor</option>
                        </select>
                    </div>
                    <div>
                        <label for="regeneracao${index}">Valor</label>
                        <input type="number" id="regeneracao${index}" name="regeneracao${index}" value="${dados.valor || 0}">
                    </div>
                `;
                break;
        }

        container.appendChild(linha);
    }

    // Mapeamento de tipo → dados → container → botão → contador
    const configuracoes = [
        {
            tipo: 'defesa',
            dados: defesas.map((d, i) => ({
                elemento: d.variavelPropriedade,
                defesa: d.variavelValor,
                resistencia: resistencias[i]?.variavelValor || 0
            })),
            container: document.getElementById('defesaContainer'),
            botao: document.getElementById('addDefesa'),
            contador: 0
        },
        {
            tipo: 'dano',
            dados: danos.map((d, i) => ({
                elemento: d.variavelPropriedade,
                dano: d.variavelValor,
                penetracao: penetracoes[i]?.variavelValor || 0
            })),
            container: document.getElementById('atributosContainer'),
            botao: document.getElementById('addAtributo'),
            contador: 0
        },
        {
            tipo: 'rolagem',
            dados: rolagens.map(d => ({
                tipo: d.variavelPropriedade,
                valor: d.variavelValor
            })),
            container: document.getElementById('rolagemContainer'),
            botao: document.getElementById('addRolagem'),
            contador: 0
        },
        {
            tipo: 'amplificacao',
            dados: amplificacoes.map(d => ({
                tipo: d.variavelPropriedade,
                valor: d.variavelValor
            })),
            container: document.getElementById('amplificacaoContainer'),
            botao: document.getElementById('addAmplificacao'),
            contador: 0
        },
        {
            tipo: 'regeneracao',
            dados: regeneracoes.map(d => ({
                tipo: d.variavelPropriedade,
                valor: d.variavelValor
            })),
            container: document.getElementById('regeneracaoContainer'),
            botao: document.getElementById('addRegeneracao'),
            contador: 0
        }
    ];

    configuracoes.forEach(config => {

        // Preenche com dados existentes
        if (config.container && config.botao) {
            config.dados.forEach(dados => {
            //const valor = dados.valor ?? dados.defesa ?? dados.resistencia ?? dados.dano ?? dados.penetracao ?? 0;

            // Só exibe se o valor for diferente de zero
            if (dados.valor !== 0 && (dados.defesa !== 0 || dados.resistencia !==0) && (dados.dano !== 0 || dados.penetracao !== 0)) {
                config.contador++;
                if (config.contador <= maxPorTipo[config.tipo]) {
                    criarLinha(config.container, config.contador, config.tipo, dados);
                    console.log(`${dados.tipo || 'tipo'}${config.contador}`);
                }
            }
        });;

            config.botao.addEventListener('click', () => {
                config.contador++;
                if (config.contador <= maxPorTipo[config.tipo]) {
                    criarLinha(config.container, config.contador, config.tipo);
                }
            });
        };
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById('efeitosAcessoriosContainer');
    const botao = document.getElementById('addEfeitoAcessorios');
    const dadosEfeitos = JSON.parse(document.getElementById('efeitos-acessorios-json').textContent || "[]");

    let count = 0;
    const MAX = 20;

    function criarLinhaEfeito(index, dados = {}) {
        const efeitoRow = document.createElement("div");
        efeitoRow.classList.add("efeito-row");

        const tipo = dados.variavelTipo || "efeitoPassivo";
        const nome = dados.variavelNome || "";
        const descricao = dados.variavelDescricao || "";


        efeitoRow.innerHTML = `
        <div class="parent">
            <div class="div1">
                <label for="efeitoTipo${index}">Tipo do Efeito</label>        
            </div>
            <div class="div2">
                <select class='personagem_select' id="efeitoTipo${index}" name="efeitoTipo${index}">
                    <option value="efeitoPassivo" ${tipo === 'efeitoPassivo' ? 'selected' : ''}>Efeito Passivo</option>
                    <option value="efeitoAtivo" ${tipo === 'efeitoAtivo' ? 'selected' : ''}>Efeito Ativo</option>
                    <option value="efeitoAura" ${tipo === 'efeitoAura' ? 'selected' : ''}>Efeito Aura</option>
                    <option value="nucleo" ${tipo === 'nucleo' ? 'selected' : ''}>Núcleo</option>
                    <option value="triunfo" ${tipo === 'triunfo' ? 'selected' : ''}>Triunfo</option>        
                </select>
            </div>
            <div class="div3">
                <label for="efeitoNome${index}">Nome do Efeito:</label>
            </div>
            <div class="div4">
                <input style="width: 100%;" type="text" id="efeitoNome${index}" name="efeitoNome${index}" placeholder="Nome do efeito" value="${nome}">
            </div>
            <div class="div5">
                <label for="efeitoDesc${index}">Descrição do Efeito:</label>
            </div>
            <div class="div6">
                <textarea style="width: 100%; height: 10em;" id="efeitoDesc${index}" name="efeitoDesc${index}" placeholder="Descrição do Efeito">${descricao}</textarea>
            </div>
        </div>
    `;
        return efeitoRow;
    }
    console.log('Efeitos carregados:', dadosEfeitos);
    // Carrega efeitos existentes
    if (Array.isArray(dadosEfeitos)) {
        dadosEfeitos.forEach(dado => {
            count++;
            const linha = criarLinhaEfeito(count, dado);
            container.appendChild(linha);
        });
    }

    // Botão para adicionar novos
    botao.addEventListener('click', () => {
        if (count >= MAX) return;
        count++;
        const novaLinha = criarLinhaEfeito(count);
        container.appendChild(novaLinha);
    });
});
