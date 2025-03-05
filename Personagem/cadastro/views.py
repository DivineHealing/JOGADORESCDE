from django.shortcuts import render
from .models import Cadastro

def inicio(request):
    return render(request, 'cadastro.html')

def lista_cadastros(request):
    cadastros = Cadastro.objects.all()  # obtem todos os produtos do banco de dados
    return render(request, 'cadastro.html', {'cadastros': cadastros})

# Create your views here.
def somarteste(request):
    resultado = None
    numero1 = '0'
    numero2 = '0'
    if request.method == 'POST':
    # recupera os valores dos inputs, usando '0' como padrão
        numero1 = request.POST.get('numero1', '0')
        numero2 = request.POST.get('numero2', '0')
        soma = int(numero1) + int(numero2)
        print(soma)
    return render(request, 'cadastro.html', {'resultado': resultado})