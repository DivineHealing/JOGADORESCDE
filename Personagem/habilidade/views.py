from django.shortcuts import get_object_or_404, redirect, render

from tela_personagem.models import Tela_personagem
from .models import Habilidade
from lib.utilitarios import *

import json
from django.core.serializers.json import DjangoJSONEncoder

personagem = None

def habilidade(request, personagem_id):
    global personagem
    personagem = personagem_id

    if not personagem_id:
        return redirect('exibir_personagem')
        
    tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
    habilidade_obj = get_object_or_404(Habilidade, personagem_id=personagem_id)

    # FORMATAÇÃO DOS DADOS DAS HABILIDADES
    habilidades_data_formatada = []

    for i in range(1, 13):
        slot_niveis = []
        nome_base = getattr(habilidade_obj, f'hab{i}_1_nome', '')

        for j in range(2, 7):  # Somente níveis 2 a 6
            nome = getattr(habilidade_obj, f'hab{i}_{j}_nome', '')
            custo = getattr(habilidade_obj, f'hab{i}_{j}_custo', '')
            tipo = getattr(habilidade_obj, f'hab{i}_{j}_tipo', '')
            descricao = getattr(habilidade_obj, f'hab{i}_{j}_descricao', '')

            if nome.strip() or descricao.strip():
                slot_niveis.append({
                    'nivel': j,
                    'nome': nome,
                    'custo': custo,
                    'tipo': tipo,
                    'descricao': descricao,
                })

        if slot_niveis:
            habilidades_data_formatada.append({
                'id': i,
                'nome': nome_base,
                'niveis': slot_niveis
            })

    context = {
        'tela_personagem': tela_personagem,
        'habilidade': habilidade_obj,
        'range_habilidades': range(1, 13),
        'habilidades_json': habilidades_data_formatada,  # Novo dado para o JS
    }
    return render(request, 'habilidade copy.html', context)


def salvar_habilidade(request):
    if request.method == "POST":
        personagem_id = obter_personagem_sessao(request)

        # se ainda nao tiver nenhum id de personagem por não existir personagem ele volta para pagina inicial
        if not personagem_id:
            return redirect('/')
        
        personagem = Habilidade.objects.get(personagem=personagem_id)

        # itera entre as 12 slots de habilidades
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
                
                #pega os valores se só existirem
                nome = request.POST.get(nome_key)
                tipo = request.POST.get(tipo_key)
                nivel = request.POST.get(nivel_key)
                custo = request.POST.get(custo_key)
                descricao = request.POST.get(desc_key)

                # distribui a habilidade associada ao personagem atual
                setattr(personagem, f"hab{i}_{count}_nome", nome)
                setattr(personagem, f"hab{i}_{count}_tipo", tipo)
                setattr(personagem, f"hab{i}_{count}_custo", custo)
                setattr(personagem, f"hab{i}_{count}_descricao", descricao)

                count += 1
        personagem.save()
        return redirect('habilidade', personagem_id=personagem_id)

    return redirect('base_personagem', personagem_id=personagem_id)