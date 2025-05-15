from django.apps import apps
from django.shortcuts import redirect, render, get_object_or_404
from base_personagem.models import Base_personagem
from tela_personagem.models import Tela_personagem
from .forms import BaseForm
from tela_personagem.models import Character_attribute
from lib.utilitarios import *

def base_personagem(request, personagem_id):
    if not personagem_id:
        return redirect('exibir_personagem')

    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            personagem = form.save(commit=True)
            personagem.save()
            return redirect('base_personagem', personagem_id=personagem_id)
        
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
    base_personagem = get_object_or_404(Base_personagem, pk=personagem_id)

    # Coletando todos os atributos
    def get_attrs(atributo):
        return list(Character_attribute.objects.filter(
            personagem=base_personagem,
            variavelTipo=atributo,
            origem="base_p"
          ).order_by('-variavelValor').values("variavelPropriedade", "variavelValor"))
    
    regeneracoes_json = [
        {"variavelPropriedade": nome, "variavelValor": getattr(base_personagem, nome)}
        for nome in ["regenVida", "regenMana", "regenVigor"]
        if getattr(base_personagem, nome) is not None
    ]
    context = {
        'tela_personagem': tela_personagem,
        'base_personagem': base_personagem,
        'defesas_json': get_attrs("defesa"),
        'resistencias_json': get_attrs("resistencia"),
        'danos_json': get_attrs("dano"),
        'penetracoes_json': get_attrs("penetracao"),
        'rolagens_json': get_attrs("rolagem"),
        'amplificacoes_json': get_attrs("amplificacao"),
        'regeneracoes_json': regeneracoes_json,
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
        pegar_atributos(personagem_id)
        print('FUNCIONA')
        return redirect('base_personagem', personagem_id=personagem_id)

    return redirect('exibir_personagem')