from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from base_personagem.models import Base_personagem
from .forms import BaseForm
from lib.utilitarios import *
from tela_personagem.models import Tela_personagem

def base_personagem(request, personagem_id):
    if not personagem_id:
        return redirect('exibir_personagem')  # ou qualquer outra tela de seleção
    
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)


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
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')

        personagem = Base_personagem.objects.get(id=personagem_id) 

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
        pegar_atributos(personagem_id, 'forca')  # <- esse 2 ainda é fixo
        print('FUNCIONA')
        return redirect('base_personagem', personagem_id=personagem_id)

    return redirect('exibir_personagem')