from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Maestria
from tela_personagem.models import Tela_personagem
from .forms import EquipamentoForm
from lib.utilitarios import *

maestriaTipo = "Tipo da Porra da Maestria"
personagemSelec = 0

def cadastro(request, personagem_id):
    global personagemSelec # DEFINE O PERSONAGEM SELECIONADO COMO GLOBAL
    personagemSelec = personagem_id # PASSA O PERSONAGEM DA SESSÃO PARA O PERSONAGEM GLOBAL
    
    # PESQUISA O PERSONAGEM, USANDO O ID COMO PARAMETRO DE BUSCA
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    context = {
        'tela_personagem': tela_personagem
    }

    return render(request, 'maestria.html', context)

def cadastrar_maestria(request, tipo, personagem_id):
    global maestriaTipo # DEFINE A VARIAVEL TIPO DA MAESTRIA ESCOLHIDA COMO GLOBAL
    maestriaTipo = tipo # PASSA O TIPO MAESTRIA DA ESCOLHIDA PARA A MAESTRIA GLOBAL

    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    try: # 
        personagem_selecionado = tela_personagem.personagem
        print(personagem_selecionado)
        maestria = Maestria.objects.get(personagem=personagem_selecionado, peca=tipo)

    except Maestria.DoesNotExist:
        raise Http404("Maestria não encontrada para este personagem.")

    context = {
        'tela_personagem': tela_personagem,
        'maestria': maestria,
        'tipo': tipo,
    }

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        try:
            equipamento = form.save(commit=False)
            equipamento.tipo = tipo
            equipamento.save()
            return redirect('atributos_maestria')
        except:
            # Se o form for inválido no POST, adicione o form com erros ao contexto
            context['form'] = form
            return render(request, 'atributos_maestria.html', context) # Renderiza com erros
    else:
        form = EquipamentoForm(initial={'tipo': tipo})
        context['form'] = form

    return render(request, 'atributos_maestria.html', context)

def perfil(request, user_id):
    messages.success(request, 'Cadastro de equipamentos realizados')
    return redirect(reverse('tela_cadastro'), kwargs={'user-id': user_id})

def salvar_maestria_atributo(request):
    if request.method == "POST":        
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')
        
        pecaalvo = Maestria.objects.get(personagem=personagem_id, peca=maestriaTipo)
        #pegar_front(request, pecaalvo)  #////////////////////////////////////////////////TIRA O COMENTARIO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        print(f'Tipo da Maestria: {maestriaTipo}\nPersonagem: {personagemSelec}')
        return redirect('cadastrar_maestria', personagem_id=personagemSelec, tipo=maestriaTipo)

    return redirect('cadastrar_maestria')