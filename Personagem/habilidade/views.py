from django.shortcuts import get_object_or_404, redirect, render

from tela_personagem.models import Tela_personagem
from .models import Habilidade
from lib.utilitarios import *

personagem = 0 # PERSONAGEM ATRIBUTO
def habilidade(request, personagem_id):
    global personagem
    personagem = personagem_id

    if not personagem_id:
        return redirect('exibir_personagem')  # ou qualquer outra tela de seleção
    
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)   
    habilidade = get_object_or_404(Habilidade, pk=personagem_id)   
     
    context = {
        'tela_personagem': tela_personagem,
        'habilidade': habilidade,
    }
    return render(request, 'habilidade.html', context)

def salvar_habilidade(request):
    if request.method == "POST":
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')
        
        personagem = Habilidade.objects.get(personagem=personagem_id)

        for i in range(1, 13):
            count = 1
            while True:
                prefix = f"habilidade{i}"
                nome_key = f"{prefix}Nome{count}"
                tipo_key = f"{prefix}Tipo{count}"
                nivel_key = f"{prefix}Nivel{count}"
                custo_key = f"{prefix}Custo{count}"
                desc_key = f"{prefix}Desc{count}"

                if nome_key not in request.POST:
                    break  # não há mais campos para esse grupo

                nome = request.POST.get(nome_key)
                tipo = request.POST.get(tipo_key)
                nivel = request.POST.get(nivel_key)
                custo = request.POST.get(custo_key)
                descricao = request.POST.get(desc_key)

                # distribui a habilidade associada ao personagem atual
                setattr(personagem, f"hab{i}_{count}_nome", nome)
                setattr(personagem, f"hab{i}_{count}_custo", custo)
                setattr(personagem, f"hab{i}_{count}_descricao", descricao)

                count += 1
        personagem.save()
        return redirect('base_personagem', personagem_id=personagem_id)
        print('FUNCIONA')

    return redirect('base_personagem', personagem_id=personagem_id)