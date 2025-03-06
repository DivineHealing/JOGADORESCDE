from django.shortcuts import render
from .forms import BaseForm

def base_personagem(request):
    resultado = 0  # Inicializa a variável resultado

    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():

            for i in range(1, 7):  # Itera de 1 a 6 (incluindo 6)
                numero = form.cleaned_data.get(f'numero{i}', 0)  # Obtém o valor do campo
                if numero is not None:  # Verifica se o valor é válido
                    resultado += numero
    else:
        form = BaseForm()
    return render(request, 'base_personagem.html', {'form': form, 'resultado': resultado})