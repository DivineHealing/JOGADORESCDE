# tela_personagens/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from base_personagem.models import Base_personagem
from .models import Tela_personagem, Elementos_personagem
from django.apps import apps
from lib.utilitarios import criar_personagem_completo

def exibir_personagem(request, personagem_id=None):
    personagens = Tela_personagem.objects.all()  # Obtém todos os personagens
    elementos = Elementos_personagem.objects.all() # Obtem todos os elementos

    if personagem_id:
        # Obtém o personagem com o ID especificado ou retorna um erro 404 se não encontrado
        tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
        elementos_personagem = get_object_or_404(Elementos_personagem, pk=personagem_id)
    else:
        # Se nenhum ID for especificado, exibe o primeiro personagem (ou None)
        tela_personagem = Tela_personagem.objects.first()
        elementos_personagem = Elementos_personagem.objects.first()
        if not tela_personagem:
            tela_personagem = None #Define como none para tratar no HTML

    # Salvar o ID do personagem na sessão
    request.session['personagem_id'] = personagem_id

    context = {'tela_personagem': tela_personagem, 'personagens': personagens, 'elementos': elementos, 'elementos_personagem': elementos_personagem} #troca na variavel pessoa para tela_personagem
    return render(request, 'tela_personagem.html', context)

def cadastrar_personagem(request):
    if request.method == "POST":
        nome_personagem = request.POST.get("novoPersonagem")  # pega nome do input

        if nome_personagem:  # se o nome não estiver vazio
            if not Base_personagem.objects.filter(personagem= nome_personagem).exists(): # verificando se o personagem ja existe
                criar_personagem_completo(nome_personagem)
            return redirect('/')

    return redirect('/')

def deletar_personagem(request):
    if request.method == "POST":
        nome_personagem = request.POST.get("deletarPersonagem")  # pega nome do input

        if nome_personagem is not None:  # se o nome não estiver vazio
        #    deletar_personagem_completo(nome_personagem)
            Base_personagem.objects.filter(personagem=nome_personagem).delete()
            return redirect('/')
        
    return redirect('/')