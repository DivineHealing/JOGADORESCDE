from django.shortcuts import redirect, render
from .forms import ConjuntoForm, EquipamentoForm
from lib.utilitarios import *

def conjunto(request):
    resultado = 0  # Inicializa a variável resultado

    if request.method == 'POST':
        form = ConjuntoForm(request.POST)
        if form.is_valid():
            for i in range(1, 7):  # Itera de 1 a 6 (incluindo 6)
                numero = form.cleaned_data.get(f'numero{i}', 0)  # Obtém o valor do campo
                if numero is not None:  # Verifica se o valor é válido
                    resultado += numero
    else:
        form = ConjuntoForm()

    
    return render(request, 'conjunto.html', {'form': form, 'resultado': resultado})

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

    return render(request, 'cadastrar_atributos.html', {'form': form, 'tipo': tipo})


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

    return render(request, 'cadastrar_efeitos.html', {'form': form, 'tipo': tipo})