from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Maestria
from .forms import EquipamentoForm
from lib.utilitarios import *

def cadastro(request):
    return render(request, 'maestria.html')

def cadastrar_maestria(request, tipo):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo  # Define o tipo com base na URL
            equipamento.save()
            return redirect('atributos_maestria')  # Redireciona para a lista (você ainda vai criar)
    else:
        form = EquipamentoForm(initial={'tipo': tipo})  # Pré-preenche o tipo

    return render(request, 'atributos_maestria.html', {'form': form, 'tipo': tipo})


def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_maestria_atributo(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('cadastro')