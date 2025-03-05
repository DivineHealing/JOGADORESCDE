# personagens/views.py
from django.shortcuts import render
from .models import Tela_personagem

def exibir_personagem(request):
    # Obtém o primeiro personagem (por enquanto, assumimos que só há um)
    personagem = Tela_personagem.objects.first() #Nome correto

    if personagem is None:
        # Se não houver personagem no banco, cria um
        personagem = Tela_personagem.objects.create()  # Cria com os valores padrão do modelo

    context = {'tela_personagem': personagem} #Nome correto
    return render(request, 'tela_personagem.html', context)