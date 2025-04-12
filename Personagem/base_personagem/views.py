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
    base_personagem = get_object_or_404(Base_personagem, pk=personagem_id)   
     
    context = {
        'tela_personagem': tela_personagem,
        'base_personagem': base_personagem,
    }
    return render(request, 'base_personagem.html', context)


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
        #telap = Tela_personagem.objects.get(id=personagem_id)

        # ATRIBUTOS BASE
        personagem.vida = int(request.POST.get("vidaMax", 0) or 0)

        personagem.forca = int(request.POST.get("forca", 0) or 0)
        personagem.destreza = int(request.POST.get("destreza", 0) or 0)
        personagem.inteligencia = int(request.POST.get("inteligencia", 0) or 0)
        personagem.determinacao = int(request.POST.get("determinacao", 0) or 0)
        personagem.perspicacia = int(request.POST.get("perspicacia", 0) or 0)
        personagem.carisma = int(request.POST.get("carisma", 0) or 0)

        # ROLAGENS
        for i in range(1, 26):
            tipo = request.POST.get(f'rolagemTipo{i}', '')
            valor = int(request.POST.get(f'rolagem{i}', 0) or 0)

            setattr(personagem, f'tipoRolagem_{i}', tipo)
            setattr(personagem, f'rolagem_{i}', valor)
            #setattr(telap, f"tipoRolagem_{i}", tipo)

        # DEFESAS
        for i in range(1, 8):
            elemento = request.POST.get(f'elemento{i}', '')
            defesa = int(request.POST.get(f'defesa{i}', 0) or 0)
            resistencia = float(request.POST.get(f'resistencia{i}', 0) or 0)

            setattr(personagem, f'elementoDefesa_{i}', elemento)
            setattr(personagem, f'elementoResistencia_{i}', elemento)
            setattr(personagem, f'defesaFixa_{i}', defesa)
            setattr(personagem, f'resistencia_{i}', resistencia)
            #setattr(telap, f"elementoDefesa_{i}", elemento)
            #setattr(telap, f"elementoResistencia_{i}", elemento)

        # DANO
        for i in range(1, 8):
            elemento = request.POST.get(f'elemento{i}', '')
            dano = int(request.POST.get(f'dano{i}', 0) or 0)
            penetracao = float(request.POST.get(f'penetracao{i}', 0) or 0)

            setattr(personagem, f'elementoDano_{i}', elemento)
            setattr(personagem, f'elementoPenetracao_{i}', elemento)
            setattr(personagem, f'danoFixo_{i}', dano)
            setattr(personagem, f'penetracao_{i}', penetracao)
            #setattr(telap, f"elementoDano_{i}", elemento)
            #setattr(telap, f"elementoPenetracao_{i}", elemento)
        personagem.danoFinal = int(request.POST.get("dmgFinal", 0) or 0)

        # AMPLIFICAÇÃO
        for i in range(1, 26):
            tipo = request.POST.get(f'amplificacaoTipo{i}', '')
            valor = float(request.POST.get(f'amplificacao{i}', 0) or 0)

            setattr(personagem, f'elementoAmplificacao_{i}', tipo)
            setattr(personagem, f'amplificacao_{i}', valor)
            #setattr(telap, f"elementoAmplificacao_{i}", tipo)

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
        #telap.save()
        pegar_atributos(personagem_id)
        #pegar_atributos(personagem_id, 'vida')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'forca')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'destreza')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'inteligencia')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'determinacao')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'perspicacia')  # <- esse 2 ainda é fixo
        #pegar_atributos(personagem_id, 'carisma')  # <- esse 2 ainda é fixo
        print('FUNCIONA')
        return redirect('base_personagem', personagem_id=personagem_id)

    return redirect('exibir_personagem')