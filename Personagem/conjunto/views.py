from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Conjunto
from .forms import EquipamentoForm
from lib.utilitarios import *

tipoEquipamento = "TIPO DO EQUIPAMENTO"

def conjunto(request):    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Conjunto, pk=personagem_id)

    context = {
        'tela_personagem': tela_personagem
    }
    return render(request, 'conjunto.html', context)

def cadastrar_equipamento(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Conjunto, pk=personagem_id)

    return render(request, 'cadastrar_atributos_conj.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem})


def cadastrar_efeitos(request, tipo):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_efeitos')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo
    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Arma, pk=personagem_id)

    return render(request, 'cadastrar_efeitos_conj.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem})


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
        print('FUNCIONA')
        return redirect('conjunto')

    return redirect('conjunto')