from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Maestria
from tela_personagem.models import Tela_personagem
from .forms import EquipamentoForm
from lib.utilitarios import *

maestriaTipo = "Tipo da Porra da Maestria"
personagemSelec = 0

def cadastro(request, personagem_id):
    global personagemSelec # DEFINE O PERSONAGEM SELECIONADO COMO GLOBAL
    personagemSelec = personagem_id # PASSA O PERSONAGEM DA SESSÃO PARA O PERSONAGEM GLOBAL
    
    # PESQUISA O PERSONAGEM, USANDO O ID COMO PARAMETRO DE BUSCA
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    context = {
        'tela_personagem': tela_personagem
    }

    return render(request, 'maestria.html', context)

def cadastrar_maestria(request, tipo, personagem_id):
    global maestriaTipo
    maestriaTipo = tipo

    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    try:
        personagem_selecionado = tela_personagem.personagem
        maestria = Maestria.objects.get(personagem=personagem_selecionado, peca=tipo)
    except Maestria.DoesNotExist:
        raise Http404("Maestria não encontrada para este personagem.")

    # Função auxiliar para buscar atributos por tipo
    def get_attrs(atributo):
        return list(Character_attribute.objects.filter(
            personagem=personagem_selecionado,
            variavelTipo=atributo,
            origem="maestria",
            peca=maestriaTipo,
        ).order_by('posicao').values("variavelPropriedade", "variavelValor"))

    # Coletar regenerações diretamente do modelo Maestria
    regeneracoes_json = [
        {"variavelPropriedade": nome, "variavelValor": getattr(maestria, nome)}
        for nome in ["regenVida", "regenMana", "regenVigor"]
        if getattr(maestria, nome) is not None
    ]

    # Formulário
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo
            equipamento.save()
            return redirect('atributos_maestria')
    else:
        form = EquipamentoForm(initial={'tipo': tipo})

    # Construção final do contexto (depois de garantir que tudo existe)
    context = {
        'tela_personagem': tela_personagem,
        'maestria': maestria,
        'tipo': tipo,
        'form': form,
        'defesas_json': get_attrs("defesa"),
        'resistencias_json': get_attrs("resistencia"),
        'danos_json': get_attrs("dano"),
        'penetracoes_json': get_attrs("penetracao"),
        'rolagens_json': get_attrs("rolagem"),
        'amplificacoes_json': get_attrs("amplificacao"),
        'regeneracoes_json': regeneracoes_json,
    }

    return render(request, 'atributos_maestria.html', context)


def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_maestria_atributo(request):
    if request.method == "POST":        
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')
        
        personagem = Base_personagem.objects.get(id=personagem_id) 
        pecaalvo = Maestria.objects.get(personagem=personagem_id, peca=maestriaTipo)
        pegar_front(request, pecaalvo, personagem, "maestria", maestriaTipo, True)
        pegar_atributos(personagem_id)
        print(f'Tipo da Maestria: {maestriaTipo}\nPersonagem: {personagemSelec}')
        return redirect('cadastrar_maestria', personagem_id=personagemSelec, tipo=maestriaTipo)

    return redirect('cadastrar_maestria')