from django.shortcuts import redirect, render
from .models import Habilidade

def habilidade(request):
    habilidade = Habilidade.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'habilidade.html', {'Habilidade': habilidade})

def salvar_habilidade(request):
    if request.method == "POST":        
        print('FUNCIONA')

    return redirect('base_personagem')