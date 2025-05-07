from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from base_personagem.models import Base_personagem
from tela_personagem.models import Tela_personagem
from .forms import BaseForm
from lib.utilitarios import *

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
        telap = Tela_personagem.objects.get(id=personagem_id)

        pegar_front(request, personagem, personagem, "base_p", "", True)

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