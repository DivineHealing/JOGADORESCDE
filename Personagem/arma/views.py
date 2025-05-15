from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Arma
from .forms import EquipamentoForm
from lib.utilitarios import *

tipoEquipamento = ""

def arma(request):   
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = Arma.objects.filter(personagem=personagem_id)

    context = {
        'tela_personagem': tela_personagem
    }
    return render(request, 'arma.html', context)

def cadastrar_equipamento_armas(request, tipo):    
    global tipoEquipamento
    tipoEquipamento = tipo

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=True)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos_armas')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo
    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Tela_personagem, personagem=personagem_id)
    arma = get_object_or_404(Arma, personagem=personagem_id, peca=tipo)

    def get_attrs(atributo):
        return list(Character_attribute.objects.filter(
            personagem=personagem_id,
            variavelTipo=atributo,
            origem="arma",
            peca=tipoEquipamento,
        ).values("variavelPropriedade", "variavelValor"))
    
    regeneracoes_json = [
        {"variavelPropriedade": nome, "variavelValor": getattr(arma, nome)}
        for nome in ["regenVida", "regenMana", "regenVigor"]
        if getattr(arma, nome) is not None
]
        
    context = {
        'tela_personagem': tela_personagem,
        'arma': arma,
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
    return render(request, 'cadastrar_atributos_arma.html', context)


def cadastrar_efeitos_armas(request, tipo):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_efeitos_armas')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Conjunto, pk=personagem_id)

    return render(request, 'cadastrar_efeitos_arma.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem})


def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_arma_atributo(request):
    if request.method == "POST":     
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        print(tipoEquipamento)
        personagem = Base_personagem.objects.get(id=personagem_id)
        armalvo = Arma.objects.get(personagem= personagem_id, peca= tipoEquipamento)
        pegar_front(request, armalvo, personagem, "arma", tipoEquipamento)
        pegar_atributos(personagem_id)
        print('FUNCIONA')

    return redirect('arma')

def salvar_arma_efeitos(request):        
    if request.method == "POST":   
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        personagem = Base_personagem.objects.get(id=personagem_id) 
        #pecaalvo = Character_effects.objects.get(personagem= personagem_id, peca= tipoEquipamento)
        pegar_efeito(request, personagem, "arma", tipoEquipamento)
        print('FUNCIONA')
        return redirect('arma')     

    return redirect('arma')