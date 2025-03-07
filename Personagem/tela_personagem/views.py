# tela_personagem/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Tela_personagem
from django.shortcuts import redirect

def exibir_personagem(request, personagem_id=None):
    personagens = Tela_personagem.objects.all()  # Obtém todos os personagens

    if personagem_id:
        # Obtém o personagem com o ID especificado ou retorna um erro 404 se não encontrado
        tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
    else:
        # Se nenhum ID for especificado, exibe o primeiro personagem (ou None)
        tela_personagem = Tela_personagem.objects.first()
        if not tela_personagem:
            tela_personagem = None #Define como none para tratar no HTML

    context = {'tela_personagem': tela_personagem, 'personagens': personagens} #troca na variavel pessoa para tela_personagem
    return render(request, 'tela_personagem.html', context)

def telaCadastro(request):
    # ... sua lógica aqui ...
    return redirect('/cadastro/cadastro/')