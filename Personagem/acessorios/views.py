from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Acessorios
from .forms import EquipamentoForm
from lib.utilitarios import *

tipoEquipamento = "TIPO DO EQUIPAMENTO"

def acessorios(request):
    return render(request, 'acessorios.html')

def cadastrar_equipamento_acessorios(request, tipo):
    global tipoEquipamento
    tipoEquipamento = tipo

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos_acessorios')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Arma, pk=personagem_id)
    acessorios = get_object_or_404(Acessorios, pk=personagem_id)   

    return render(request, 'cadastrar_atributos_acessorios.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem, 'acessorios': acessorios})


def cadastrar_efeitos_acessorios(request, tipo):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_efeitos_acessorios')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Arma, pk=personagem_id)

    return render(request, 'cadastrar_efeitos_acessorios.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem})


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
        pegar_front(request, pecaalvo, personagem, "aces", tipoEquipamento)
        pegar_atributos(personagem_id)
        print('acessorios')

    return redirect('arma')

def salvar_acessorio_efeitos(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('acessorios')