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

    tela_personagem = get_object_or_404(Conjunto, pk=personagem_id)

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
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos_armas')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo
    
    personagem_id = obter_personagem_sessao(request)

    if not personagem_id:
        return redirect('exibir_personagem')

    tela_personagem = get_object_or_404(Arma, pk=personagem_id)

    return render(request, 'cadastrar_atributos_arma.html', {'form': form, 'tipo': tipo, 'tela_personagem': tela_personagem})


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
        print('FUNCIONA')

    return redirect('arma')