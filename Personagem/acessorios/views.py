import json
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Acessorios
from tela_personagem.models import Character_attribute
from base_personagem.models import Base_personagem
from .forms import EquipamentoForm
from lib.utilitarios import *

from tela_personagem.models import Character_effects
import json

tipoEquipamento = ""

def acessorios(request):
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    acessorios = Acessorios.objects.filter(personagem=personagem_id)

    return render(request, 'acessorios.html', {'tela_personagem': tela_personagem, 'acessorios': acessorios})

def cadastrar_equipamento_acessorios(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos_acessorios')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    acessorios = get_object_or_404(Acessorios, personagem=personagem_id, peca=tipo)

    def get_attrs(atributo):
        return list(Character_attribute.objects.filter(
            personagem=personagem_id,
            variavelTipo=atributo,
            origem="aces",
            peca=tipoEquipamento,
          ))

    regeneracoes_json = [
    {"variavelPropriedade": nome, "variavelValor": getattr(acessorios, nome)}
    for nome in ["regenVida", "regenMana", "regenVigor"]
    if getattr(acessorios, nome) is not None
]
        
    context = {
        'tela_personagem': tela_personagem,
        'acessorios': acessorios,
        'defesas_json': get_attrs("defesa"),
        'resistencias_json': get_attrs("resistencia"),
        'danos_json': get_attrs("dano"),
        'penetracoes_json': get_attrs("penetracao"),
        'rolagens_json': get_attrs("rolagem"),
        'amplificacoes_json': get_attrs("amplificacao"),
        'regeneracoes_json': regeneracoes_json,
        'form': form,
        'tipo': tipo
    }
    return render(request, 'cadastrar_atributos_acessorios.html', context)


def cadastrar_efeitos_acessorios(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo
            equipamento.save()
            return redirect('cadastrar_efeitos_acessorios')  # Ajustar se necessário
    else:
        form = EquipamentoForm(initial={'tipo': tipo})

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    acessorios = Acessorios.objects.filter(personagem=personagem_id)

    def get_all_effects():
        tipos = ["efeitoAtivo", "efeitoPassivo", "efeitoAura", "nucleo", "triunfo"]
        efeitos = []
        for tipo in tipos:
            efeitos += list(Character_effects.objects.filter(
                personagem=personagem_id,
                variavelTipo=tipo,
                origem="aces",
                peca=tipoEquipamento
            ).values("variavelTipo", "variavelNome", "variavelDescricao"))
        return efeitos

    context = {
        'tela_personagem': tela_personagem,
        'acessorios': acessorios,
        'efeitos_acessorios_json': get_all_effects(),
        'form': form,
        'tipo': tipo
    }

    return render(request, 'cadastrar_efeitos_acessorios.html', context)



def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_acessorio_atributos(request):
    if request.method == "POST":    
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')
        
        personagem = Base_personagem.objects.get(id=personagem_id) 
        pecaalvo = Acessorios.objects.get(personagem= personagem_id, peca= tipoEquipamento)
        pegar_front(request, pecaalvo, personagem, "aces", tipoEquipamento, True)
        pegar_atributos(personagem_id)
        print('acessorios')

    return redirect('acessorios')

def salvar_acessorio_efeitos(request):
    if request.method == "POST":   
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        personagem = Base_personagem.objects.get(id=personagem_id) 
        #pecaalvo = Character_effects.objects.get(personagem= personagem_id, peca= tipoEquipamento)
        pegar_efeito(request, personagem, "aces", tipoEquipamento)
        print('FUNCIONA')
        return redirect('acessorios')     

    return redirect('acessorios')