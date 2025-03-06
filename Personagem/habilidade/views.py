from django.shortcuts import render
from .models import Habilidade

def habilidade(request):
    habilidade = Habilidade.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'habilidade.html', {'Habilidade': habilidade})