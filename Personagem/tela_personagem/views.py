# tela_personagens/views.py
from collections import defaultdict
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from habilidade.models import Habilidade
from base_personagem.models import Base_personagem
from .models import Tela_personagem, Character_attribute, Character_effects
from django.apps import apps
from lib.utilitarios import criar_personagem_completo
from django.db.models import Sum
from lib.utilitarios import *
from django.core.serializers.json import DjangoJSONEncoder


def exibir_personagem(request, personagem_id=None):

    def formatar_habilidades(habilidades_obj):
        habilidades_formatadas = []

        if not habilidades_obj:
            return habilidades_formatadas

        for i in range(1, 13):  # Slots 1 a 12
            slot_niveis = []
            nome_base = getattr(habilidades_obj, f'hab{i}_1_nome', '')

            if nome_base and nome_base.strip():
                for j in range(1, 7):  # Níveis 1 a 6
                    nome = getattr(habilidades_obj, f'hab{i}_{j}_nome', '')
                    custo = getattr(habilidades_obj, f'hab{i}_{j}_custo', '')
                    tipo = getattr(habilidades_obj, f'hab{i}_{j}_tipo', '')
                    descricao = getattr(habilidades_obj, f'hab{i}_{j}_descricao', '')

                    if nome.strip() or descricao.strip():
                        slot_niveis.append({
                            'nivel': j,
                            'nome': nome,
                            'custo': custo,
                            'tipo': tipo,
                            'descricao': descricao,
                        })

                if slot_niveis:
                    habilidades_formatadas.append({
                        'id': i,
                        'nome': nome_base,
                        'niveis': slot_niveis
                    })

        return habilidades_formatadas
    
    def obter_personagem_e_base(personagem_id):
        """Retorna (tela_personagem, base_personagem, habilidades_obj)"""
        try:
            if personagem_id:
                tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
            else:
                tela_personagem = Tela_personagem.objects.all().order_by('personagem__personagem').first()

            if not tela_personagem:
                return None, None, None

            base_personagem = tela_personagem.personagem
            habilidades_obj = Habilidade.objects.filter(personagem=base_personagem).first()

            return tela_personagem, base_personagem, habilidades_obj

        except AttributeError:
            print(f"!!! ERRO: Falha ao acessar base_personagem a partir de Tela_personagem ID={personagem_id} !!!")
            return None, None, None

    todos_personagens_tela = Tela_personagem.objects.all().order_by('personagem__personagem')
    tela_personagem, base_personagem, habilidades_obj = obter_personagem_e_base(personagem_id)

    if tela_personagem:
        request.session['personagem_id'] = tela_personagem.id
        status_perc(tela_personagem.id)
        vida_perc(tela_personagem.id)
    else:
        request.session['personagem_id'] = None
    
    # SEGURANÇA PRA INICIALIZAÇÃO DO SISTEMA, SE NÃO HOUVER NENHUM PERSONAGEM CADASTRADO
    if not todos_personagens_tela:
        dados_rolagens = []
        dados_defesas = []
        dados_resistencias = []
        dados_dano = []
        dados_penetracao = []
        dados_amplificacao = []
        dados_efeitosAtivos = []
        dados_efeitosPassivos = []
        habilidades_data_formatada = []

    if base_personagem:
        def agrupar_variaveis(tipo):
            return Character_attribute.objects.filter(
                personagem=base_personagem,
                variavelTipo=tipo
            ).values("variavelPropriedade").annotate(
                variavelValor=Sum("variavelValor")
            ).order_by("variavelPropriedade")
        
        def agrupar_efeitos(efeito):
            return Character_effects.objects.filter(
            personagem=personagem_id,
            variavelTipo=efeito
            ).values("variavelNome", "variavelDescricao")        
        
        # DADOS DE EFEITOS
        try:
            dados_rolagens = agrupar_variaveis("rolagem")
            dados_defesas = agrupar_variaveis("defesa")
            dados_resistencias = agrupar_variaveis("resistencia")
            dados_dano = agrupar_variaveis("dano")
            dados_penetracao = agrupar_variaveis("penetracao")
            dados_amplificacao = agrupar_variaveis("amplificacao")
        except Character_attribute.DoesNotExist:
            dados_rolagens = []
            dados_defesas = []
            dados_resistencias = []
            dados_dano = []
            dados_penetracao = []
            dados_amplificacao = []

            # DADOS DE EFEITOS
        try:
            dados_efeitosAtivos = agrupar_efeitos("efeitoAtivo")
            dados_efeitosPassivos = agrupar_efeitos("efeitoPassivo")
        except Character_attribute.DoesNotExist:
            dados_efeitosAtivos = []
            dados_efeitosPassivos = []
            print(f"!!! ERRO: Falha ao acessar dados de efeitos para Base_personagem ID={base_personagem.id} !!!")
        

        # --- Lógica para formatar os dados das Habilidades (SÓ SE habilidades_obj foi encontrado) ---
        habilidades_data_formatada = formatar_habilidades(habilidades_obj)

    def formatar_para_json(dados):
        return [{"fields": {"variavelPropriedade": item["variavelPropriedade"], "variavelValor": item["variavelValor"]}} for item in dados]
    
    rolagens_json = formatar_para_json(dados_rolagens)
    defesas_json = formatar_para_json(dados_defesas)
    resistencias_json = formatar_para_json(dados_resistencias)
    danos_json = formatar_para_json(dados_dano)
    penetracoes_json = formatar_para_json(dados_penetracao)
    amplificacoes_json = formatar_para_json(dados_amplificacao)
    
    def formatar_efeito_json(lista):
        return json.dumps([
            {
                "nome": item["variavelNome"],
                "descricao": item.get("variavelDescricao", "")
            }
            for item in lista
        ], cls=DjangoJSONEncoder)

    efeitos_ativos_json = formatar_efeito_json(dados_efeitosAtivos)
    efeitos_passivos_json = formatar_efeito_json(dados_efeitosPassivos)

  #  print(f"--- Dados formatados para JSON ---")
  #  print(f"Efeitos Ativos JSON: {efeitos_ativos_json}")
  #  print(f"Efeitos Passivos JSON: {efeitos_passivos_json}")

    context = {
        'tela_personagem': tela_personagem,
        'personagens': todos_personagens_tela,
        'base_personagem': base_personagem,
        'habilidades_raw': habilidades_obj,
        'lista_habilidades_data': habilidades_data_formatada,
        # ATRIBUTOS
        'rolagens_json': rolagens_json,
        'defesas_json': defesas_json,
        'resistencias_json': resistencias_json,
        'danos_json': danos_json,
        'penetracoes_json': penetracoes_json,
        'amplificacoes_json': amplificacoes_json,
        # EFEITOS
        'efeitos_ativos_json': efeitos_ativos_json,
        'efeitos_passivos_json': efeitos_passivos_json,
}
    
    return render(request, 'tela_personagem.html', context)

def cadastrar_personagem(request):
    if request.method == "POST":
        nome_personagem = request.POST.get("novoPersonagem")  # pega nome do input

        if nome_personagem:  # se o nome não estiver vazio
            if not Base_personagem.objects.filter(personagem= nome_personagem).exists(): # verificando se o personagem ja existe
                criar_personagem_completo(nome_personagem)
            return redirect('/')

    return redirect('/')

def deletar_personagem(request):
    if request.method == "POST":
        nome_personagem = request.POST.get("deletarPersonagem")  # pega nome do input

        if nome_personagem is not None:  # se o nome não estiver vazio
        #    deletar_personagem_completo(nome_personagem)
            Base_personagem.objects.filter(personagem=nome_personagem).delete()
            return redirect('/')
        
    return redirect('/')

def exibir_ficha_personagem(request, personagem_id):

    # 1. CORRETO: Busca o Base_personagem usando o ID da URL
    base_personagem = get_object_or_404(Base_personagem, pk=personagem_id)
    print(f"--- Base_personagem encontrado: ID={base_personagem.id}, Nome={getattr(base_personagem, 'personagem', 'N/A')} ---") # Ajuste o nome do campo se necessário

    try:
        # 2. CORRETO: Busca o objeto Habilidade associado ao Base_personagem correto
        habilidades_obj = Habilidade.objects.get(personagem=base_personagem)
        print(f"--- Objeto Habilidade encontrado: ID={habilidades_obj.id} ---")
    except Habilidade.DoesNotExist:
        habilidades_obj = None
        print(f"!!! Objeto Habilidade não encontrado para Base_personagem ID: {base_personagem.id} !!!")
        # Você pode querer mostrar uma mensagem no template ou apenas não mostrar habilidades
        # raise Http404("Registro de habilidades não encontrado para este personagem.") # Alternativa
    except Habilidade.MultipleObjectsReturned:
        print(f"!!! ERRO: Múltiplos objetos Habilidade encontrados para Base_personagem ID: {base_personagem.id} !!!")
        # Pegar o primeiro é uma forma de contornar, mas indica erro nos dados
        habilidades_obj = Habilidade.objects.filter(personagem=base_personagem).first()
        if habilidades_obj:
             print(f"--- Usando o primeiro objeto Habilidade encontrado: ID={habilidades_obj.id} ---")

    # Estrutura de dados que será enviada para o template/JS
    habilidades_data_formatada = []
    print(f"--- Iniciando formatação dos dados ---")

    if habilidades_obj:
        # Loop pelos 12 "slots" de habilidade
        for i in range(1, 13): # De 1 a 12
            # print(f"\n--- Verificando Slot {i} ---") # Mantenha se quiser super detalhado
            slot_niveis = []
            nome_base_habilidade = getattr(habilidades_obj, f'hab{i}_1_nome', '')
            # print(f"  Nome Base (hab{i}_1_nome): '{nome_base_habilidade}'")

            # Se não houver nome no nível 1, consideramos o slot vazio
            if nome_base_habilidade and nome_base_habilidade.strip(): # Adicionado .strip()
                # print(f"  >> Condição Nome Base OK para Slot {i}")
                for j in range(1, 7): # De 1 a 6
                    nivel_nome = getattr(habilidades_obj, f'hab{i}_{j}_nome', '')
                    nivel_custo = getattr(habilidades_obj, f'hab{i}_{j}_custo', '')
                    nivel_tipo = getattr(habilidades_obj, f'hab{i}_{j}_tipo', '')
                    nivel_desc = getattr(habilidades_obj, f'hab{i}_{j}_descricao', '')

                    # Adiciona o nível APENAS se tiver nome OU descrição (após remover espaços)
                    if (nivel_nome and nivel_nome.strip()) or (nivel_desc and nivel_desc.strip()):
                        # print(f"    >> Condição Nível {j} OK (Nome ou Desc existe)")
                        slot_niveis.append({
                            'nivel': j,
                            'nome': nivel_nome,
                            'custo': nivel_custo,
                            'tipo': nivel_tipo,
                            'descricao': nivel_desc,
                        })

                if slot_niveis:
                    # print(f"  >> Lista slot_niveis NÃO está vazia. Adicionando Slot {i} à lista final.")
                    habilidades_data_formatada.append({
                        'id': i,
                        'nome': nome_base_habilidade,
                        'niveis': slot_niveis
                    })
            # else:
                 # print(f"  >> Condição Nome Base FALHOU para Slot {i}.")

    context = {
        'base_personagem': base_personagem, # Passa o Base_personagem para o template
        'lista_habilidades_data': habilidades_data_formatada,
        'habilidades_raw': habilidades_obj # Objeto Habilidade original
        # Adicione 'tela_personagem' se você precisar dele também
        # 'tela_personagem': get_object_or_404(Tela_personagem, personagem=base_personagem) # Exemplo
    }

    # VERIFICAÇÃO FINAL DO CONTEXTO
    # print(f"\n--- CONTEXTO FINAL ---")
    # print(context)
    # Certifique-se que está renderizando o template correto
    return render(request, 'tela_personagem.html', context) # Ou 'seu_template_ficha.html'

from django.db.models import F
