from django.apps import apps
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BaseForm
from lib.utilitarios import *
from tela_personagem.models import Tela_personagem

def base_personagem(request, personagem_id):
    if not personagem_id:
        return redirect('exibir_personagem')  # ou qualquer outra tela de seleção
    
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    context = {
        'tela_personagem': tela_personagem,
    }
    return render(request, 'base_personagem.html', context)

def salvar_base_personagem(request, personagem_id):
    if request.method == "POST":
        personagem_id = request.POST.get('personagem_id')  # Pega do form
        pegar_atributos(2, 'forca')  # <- Essa parte é sua função
        print('FUNCIONA')
        return redirect('base_personagem', personagem_id=personagem_id)

    return redirect('exibir_personagem')