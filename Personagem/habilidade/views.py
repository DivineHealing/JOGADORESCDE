from django.shortcuts import get_object_or_404, redirect, render

from tela_personagem.models import Tela_personagem
from .models import Habilidade

personagem = 0 # PERSONAGEM ATRIBUTO
def habilidade(request, personagem_id):
    global personagem
    personagem = personagem_id

    if not personagem_id:
        return redirect('exibir_personagem')  # ou qualquer outra tela de seleção
    
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)   
    habilidade = get_object_or_404(Habilidade, pk=personagem_id)   
     
    context = {
        'tela_personagem': tela_personagem,
        'habilidade': habilidade,
    }
    return render(request, 'habilidade.html', context)

def salvar_habilidade(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('base_personagem')