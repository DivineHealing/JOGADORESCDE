from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Conjunto
from .forms import EquipamentoForm
from lib.utilitarios import *

def conjunto(request):
    return render(request, 'conjunto.html')

def cadastrar_equipamento(request, tipo):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('cadastrar_atributos')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    return render(request, 'cadastrar_atributos_conj.html', {'form': form, 'tipo': tipo})


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

    return render(request, 'cadastrar_efeitos_conj.html', {'form': form, 'tipo': tipo})


def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_conjunto_atributo(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('conjunto')

def salvar_conjunto_efeitos(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('conjunto')