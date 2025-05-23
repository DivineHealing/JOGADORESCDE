from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Conjunto
from .forms import EquipamentoForm
from lib.utilitarios import *

from tela_personagem.models import Character_effects
import json

tipoEquipamento = ""

def conjunto(request):    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    pecas_conjunto = Conjunto.objects.filter(personagem=personagem_id)

    context = {
        'tela_personagem': pecas_conjunto
    }
    return render(request, 'conjunto.html', context)

def cadastrar_equipamento(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    conj = get_object_or_404(Conjunto, personagem=personagem_id, peca=tipo)

    def get_attrs(atributo):
        return list(Character_attribute.objects.filter(
            personagem=personagem_id,
            variavelTipo=atributo,
            origem="conj",
            peca=tipoEquipamento,
         ).order_by('posicao').values("variavelPropriedade", "variavelValor"))
     
    regeneracoes_json = [
        {"variavelPropriedade": nome, "variavelValor": getattr(conj, nome)}
        for nome in ["regenVida", "regenMana", "regenVigor"]
        if getattr(conj, nome) is not None
    ]
    
    context = {
        'tela_personagem': tela_personagem,
        'conjunto': conj,
        'defesas_json': get_attrs("defesa"),
        'resistencias_json': get_attrs("resistencia"),
        'rolagens_json': get_attrs("rolagem"),
        'amplificacoes_json': get_attrs("amplificacao"),
        'regeneracoes_json': regeneracoes_json,
        'form': form,
        'tipo': tipo
    }
    
    return render(request, 'cadastrar_atributos_conj.html', context)


def cadastrar_efeitos(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_efeitos')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo
    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    conjunto = Conjunto.objects.filter(personagem=personagem_id)

    def get_all_effects():
        tipos = ["efeitoAtivo", "efeitoPassivo", "efeitoAura", "nucleo", "triunfo"]
        efeitos = []
        for tipo in tipos:
            efeitos += list(Character_effects.objects.filter(
                personagem=personagem_id,
                variavelTipo=tipo,
                origem="conj",
                peca=tipoEquipamento
            ).values("variavelTipo", "variavelNome", "variavelDescricao"))
        return efeitos

    context = {
        'tela_personagem': tela_personagem,
        'conjunto': conjunto,
        'efeitos_acessorios_json': get_all_effects(),
        'form': form,
        'tipo': tipo
    }

    return render(request, 'cadastrar_efeitos_conj.html', context)


def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_conjunto_atributo(request):
    if request.method == "POST":
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        personagem = Base_personagem.objects.get(id=personagem_id)
        pecaalvo = Conjunto.objects.get(personagem= personagem_id, peca= tipoEquipamento)
        pegar_front(request, pecaalvo, personagem, "conj", tipoEquipamento)
        pegar_atributos(personagem_id)
        print(personagem_id)
        print('FUNCIONA')

    return redirect('conjunto')

def salvar_conjunto_efeitos(request):
    if request.method == "POST":
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        personagem = Base_personagem.objects.get(id=personagem_id)
        pegar_efeito(request, personagem, "conj", tipoEquipamento)
        return redirect('conjunto')

    return redirect('conjunto')