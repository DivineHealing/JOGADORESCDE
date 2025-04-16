from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Maestria
from tela_personagem.models import Tela_personagem
from .forms import EquipamentoForm
from lib.utilitarios import *
maestriaTipo = "Tipo da Porra da Maestria"
personagem = 0
def cadastro(request, personagem_id):
    global personagem
    personagem = personagem_id
    # Busca o personagem pelo ID vindo da URL
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
    # Cria o contexto com o objeto encontrado
    context = {
        'tela_personagem': tela_personagem
    }
    # Renderiza o template passando o contexto
    return render(request, 'maestria.html', context)

def cadastrar_maestria(request, tipo, personagem_id):
    global maestriaTipo # VARIAVEL DO TIPO DA MAESTRIA
    maestriaTipo = tipo # SETA O TIPO DA PEÇA

    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)

    try:
        base_personagem = tela_personagem.personagem
        maestria = Maestria.objects.get(personagem=base_personagem, peca=tipo)

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
            # Associar ao personagem/maestria aqui, se necessário
            # equipamento.personagem = tela_personagem
            # equipamento.maestria = maestria
            equipamento.save()
            # Considere redirecionar para uma página de sucesso ou de volta para a tela anterior
            return redirect('atributos_maestria')
        except:
            # Se o form for inválido no POST, adicione o form com erros ao contexto
            context['form'] = form
            return render(request, 'atributos_maestria.html', context) # Renderiza com erros
    else: # Método GET
        form = EquipamentoForm(initial={'tipo': tipo})
        context['form'] = form # Adiciona o form vazio ao contexto

    # Renderiza a página no GET ou se o POST falhou (sem redirect no POST inválido acima)
    return render(request, 'atributos_maestria.html', context) # Passa o dicionário context inteiro

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

        print(f'Tipo da Maestria: {maestriaTipo}\nPersonagem: {personagem}')
        return redirect('cadastrar_maestria', personagem_id=personagem, tipo=maestriaTipo)

    return redirect('cadastrar_maestria')