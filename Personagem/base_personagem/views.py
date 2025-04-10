from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from base_personagem.models import Base_personagem
from .forms import BaseForm
from lib.utilitarios import *

def base_personagem(request):
    resultado = 0  # Inicializa a variável resultado
    lvlup(185187)
    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            pegar_atributos(1, 'forca')
            for i in range(1, 7):  # Itera de 1 a 6 (incluindo 6)
                numero = form.cleaned_data.get(f'numero{i}', 0)  # Obtém o valor do campo
                if numero is not None:  # Verifica se o valor é válido
                    resultado += numero
    else:
        form = BaseForm()
    return render(request, 'base_personagem.html', {'form': form, 'resultado': resultado})


def editar_base_personagem(request):
    print('funcionou')
    personagem_id = request.GET.get(2, None)
    if personagem_id:
        personagem = get_object_or_404(Base_personagem, id=personagem_id)
    else:
        personagem = Base_personagem.objects.first()  # ou trate de outra forma

    return render(request, 'base_personagem/base_personagem.html', {
        'personagem': personagem,
    })


def salvar_base_personagem(request):
    if request.method == "POST":
        # personagem_id = request.POST.get("personagem_id")  
        personagem = Base_personagem.objects.get(id=2)  # substitua isso depois pelo ID real

        # ATRIBUTOS BASE
        personagem.forca = int(request.POST.get("forca", 0) or 0)
        personagem.destreza = int(request.POST.get("destreza", 0) or 0)
        personagem.inteligencia = int(request.POST.get("inteligencia", 0) or 0)
        personagem.determinacao = int(request.POST.get("determinacao", 0) or 0)
        personagem.perspicacia = int(request.POST.get("perspicacia", 0) or 0)
        personagem.carisma = int(request.POST.get("carisma", 0) or 0)

        # ROLAGENS
        for i in range(1, 6):
            tipo = request.POST.get(f'rolagemTipo{i}', '')
            valor = int(request.POST.get(f'rolagem{i}', 0) or 0)

            setattr(personagem, f'tipoRolagem_{i}', tipo)
            setattr(personagem, f'rolagem_{i}', valor)

        # DEFESAS
        for i in range(1, 4):
            elemento = request.POST.get(f'elemento{i}', '')
            defesa = int(request.POST.get(f'defesa{i}', 0) or 0)
            resistencia = float(request.POST.get(f'resistencia{i}', 0) or 0)

            setattr(personagem, f'elementoDefesa_{i}', elemento)
            setattr(personagem, f'defesaFixa_{i}', defesa)
            setattr(personagem, f'resistencia_{i}', resistencia)

        # DANO
        for i in range(1, 4):
            elemento = request.POST.get(f'elemento{i}', '')
            dano = int(request.POST.get(f'dano{i}', 0) or 0)
            penetracao = float(request.POST.get(f'penetracao{i}', 0) or 0)

            setattr(personagem, f'elementoDano_{i}', elemento)
            setattr(personagem, f'danoFixo_{i}', dano)
            setattr(personagem, f'penetracao_{i}', penetracao)

        # AMPLIFICAÇÃO
        for i in range(1, 6):
            tipo = request.POST.get(f'amplificacaoTipo{i}', '')
            valor = float(request.POST.get(f'amplificacao{i}', 0) or 0)

            setattr(personagem, f'elementoAmplificacao_{i}', tipo)
            setattr(personagem, f'amplificacao_{i}', valor)

        # REGENERAÇÃO
        for i in range(1, 4):
            tipo = request.POST.get(f'regeneracaoTipo{i}', '')
            valor = float(request.POST.get(f'regeneracao{i}', 0) or 0)

            if tipo == "regenVida":
                personagem.regenVida = valor
            elif tipo == "regenMana":
                personagem.regenMana = valor
            elif tipo == "regenVigor":
                personagem.regenVigor = valor

        personagem.save()
        pegar_atributos(2, 'forca')  # <- esse 2 ainda é fixo
        print('FUNCIONA')
        return redirect('base_personagem')

    return redirect('base_personagem')