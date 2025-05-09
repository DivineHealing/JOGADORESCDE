# tela_personagens/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from habilidade.models import Habilidade
from base_personagem.models import Base_personagem
from .models import Tela_personagem, Character_attribute
from django.apps import apps
from lib.utilitarios import criar_personagem_completo
from django.db.models import Sum
from lib.utilitarios import *

def exibir_personagem(request, personagem_id=None):
    todos_personagens_tela = Tela_personagem.objects.all().order_by('personagem__personagem') # Lista para dropdown, ordenada pelo nome base
    atributos_origem = ["aces","base_p", "arma", "conj", "maestria"]
    tela_personagem = None
    base_personagem = None
    habilidades_obj = None
    habilidades_data_formatada = [] # Inicializa como lista vazia

    # --- Lógica para determinar o personagem a ser exibido ---
    if personagem_id:
        # Tenta obter o personagem com o ID especificado
        tela_personagem = get_object_or_404(Tela_personagem, pk=personagem_id)
    else:
        # Se nenhum ID for especificado, tenta exibir o primeiro personagem da lista
        tela_personagem = todos_personagens_tela.first()
        # Se tela_personagem ainda for None (nenhum personagem existe), ele permanecerá None

    # --- Lógica para buscar Base_personagem e Habilidades (SÓ SE um personagem foi selecionado/encontrado) ---
    if tela_personagem:
        # Salva o ID na sessão apenas se um personagem válido foi encontrado
        request.session['personagem_id'] = tela_personagem.id

        # Tenta obter o Base_personagem associado (assumindo que o campo em Tela_personagem se chama 'personagem')
        try:
            # IMPORTANTE: Verifique se o nome do campo é 'personagem' no seu modelo Tela_personagem
            base_personagem = tela_personagem.personagem
            print(f"--- Base_personagem encontrado via Tela_personagem: ID={base_personagem.id}, Nome={getattr(base_personagem, 'personagem', 'N/A')} ---")

            # Tenta buscar o objeto Habilidade associado ao Base_personagem
            try:
                habilidades_obj = Habilidade.objects.get(personagem=base_personagem)
                print(f"--- Objeto Habilidade encontrado: ID={habilidades_obj.id} ---")
            except Habilidade.DoesNotExist:
                print(f"!!! Objeto Habilidade não encontrado para Base_personagem ID: {base_personagem.id} !!!")
                habilidades_obj = None # Garante que é None
            except Habilidade.MultipleObjectsReturned:
                print(f"!!! ERRO: Múltiplos objetos Habilidade para Base_personagem ID: {base_personagem.id} !!!")
                habilidades_obj = Habilidade.objects.filter(personagem=base_personagem).first()
                if habilidades_obj:
                    print(f"--- Usando o primeiro objeto Habilidade encontrado: ID={habilidades_obj.id} ---")
    
        except AttributeError:
            # Se Tela_personagem não tiver o atributo 'personagem' (ou o nome que você usou)
            print(f"!!! ERRO: Não foi possível acessar Base_personagem a partir de Tela_personagem ID={tela_personagem.id}. Verifique o nome do campo ForeignKey. !!!")
            base_personagem = None # Garante que é None
            habilidades_obj = None # Garante que é None

    if base_personagem:
        dados_rolagens = Character_attribute.objects.filter(
            personagem=base_personagem, 
            variavelTipo="rolagem").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        dados_defesas = Character_attribute.objects.filter(
            personagem=base_personagem, 
            variavelTipo="defesa").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        dados_resistencias = Character_attribute.objects.filter(
            personagem=base_personagem, 
            variavelTipo="resistencia").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        dados_dano = Character_attribute.objects.filter(
            personagem=base_personagem,
            variavelTipo="dano").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        dados_penetracao = Character_attribute.objects.filter(
            personagem=base_personagem,
            variavelTipo="penetracao").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        dados_amplificacao = Character_attribute.objects.filter(
            personagem=base_personagem, 
            variavelTipo="amplificacao").values("variavelPropriedade").annotate(
            variavelValor=Sum("variavelValor")
        ).order_by("variavelPropriedade")

        # --- Lógica para formatar os dados das Habilidades (SÓ SE habilidades_obj foi encontrado) ---
        if habilidades_obj:
            print(f"--- Iniciando formatação dos dados de Habilidade ID: {habilidades_obj.id} ---")
            for i in range(1, 13): # Loop pelos slots 1 a 12
                slot_niveis = []
                nome_base_habilidade = getattr(habilidades_obj, f'hab{i}_1_nome', '')

                if nome_base_habilidade and nome_base_habilidade.strip():
                    for j in range(1, 7): # Loop pelos níveis 1 a 6
                        nivel_nome = getattr(habilidades_obj, f'hab{i}_{j}_nome', '')
                        nivel_custo = getattr(habilidades_obj, f'hab{i}_{j}_custo', '')
                        nivel_tipo = getattr(habilidades_obj, f'hab{i}_{j}_tipo', '')
                        nivel_desc = getattr(habilidades_obj, f'hab{i}_{j}_descricao', '')

                        if (nivel_nome and nivel_nome.strip()) or (nivel_desc and nivel_desc.strip()):
                            slot_niveis.append({
                                'nivel': j,
                                'nome': nivel_nome,
                                'custo': nivel_custo,
                                'tipo': nivel_tipo,
                                'descricao': nivel_desc,
                            })

                    if slot_niveis:
                        habilidades_data_formatada.append({
                            'id': i, # ID do Slot
                            'nome': nome_base_habilidade,
                            'niveis': slot_niveis
                        })
        else:
             print(f"--- Formatação de Habilidades pulada (habilidades_obj é None) ---")

    else:
        # Caso nenhum personagem tenha sido selecionado ou encontrado (ex: banco vazio)
        print("--- Nenhum personagem selecionado ou encontrado. Nenhuma habilidade será carregada. ---")
        # Mantém base_personagem=None, habilidades_obj=None, habilidades_data_formatada=[]
        request.session['personagem_id'] = None # Limpa/define como None na sessão


    rolagens_json = [
    {"fields": {"variavelPropriedade": rl["variavelPropriedade"], "variavelValor": rl["variavelValor"]}}
    for rl in dados_rolagens
    ]  
    defesas_json = [
    {"fields": {"variavelPropriedade": df["variavelPropriedade"], "variavelValor": df["variavelValor"]}}
    for df in dados_defesas
]    
    resistencias_json = [
    {"fields": {"variavelPropriedade": r["variavelPropriedade"], "variavelValor": r["variavelValor"]}}
    for r in dados_resistencias
]
    danos_json = [
    {"fields": {"variavelPropriedade": d["variavelPropriedade"], "variavelValor": d["variavelValor"]}}
    for d in dados_dano
]   
    penetracoes_json = [
    {"fields": {"variavelPropriedade": p["variavelPropriedade"], "variavelValor": p["variavelValor"]}}
    for p in dados_penetracao
]
    amplificacoes_json = [
    {"fields": {"variavelPropriedade": a["variavelPropriedade"], "variavelValor": a["variavelValor"]}}
    for a in dados_amplificacao
]
    # --- Montagem Final do Contexto ---
    print("--- DEBUG ROLAGENS ---")
    print(f"Qtd rolagens: {len(dados_rolagens)}")
    for rl in dados_rolagens:
        print(f"{rl['variavelPropriedade']} = {rl['variavelValor']}")

    print("--- DEBUG DEFESAS ---")
    print(f"Qtd defesas: {len(dados_defesas)}")
    for df in dados_defesas:
        print(f"{df['variavelPropriedade']} = {df['variavelValor']}")
    
    print("--- DEBUG RESISTENCIAS ---")
    print(f"Qtd resistências: {len(dados_resistencias)}")
    for r in dados_resistencias:
        print(f"{r['variavelPropriedade']} = {r['variavelValor']}")

    print("--- DEBUG DANOS ---")
    print(f"Qtd danos: {len(dados_dano)}")
    for d in dados_dano:
        print(f"{d['variavelPropriedade']} = {d['variavelValor']}")

    print("--- DEBUG PENETRACOES ---")
    print(f"Qtd penetrações: {len(dados_penetracao)}")
    for p in dados_penetracao:
        print(f"{p['variavelPropriedade']} = {p['variavelValor']}")
    
    print("--- DEBUG AMPLIFICACOES ---")
    print(f"Qtd amplificações: {len(dados_amplificacao)}")
    for a in dados_amplificacao:
        print(f"{a['variavelPropriedade']} = {a['variavelValor']}")
        
    context = {
        'danos_json': danos_json,
        'penetracoes_json': penetracoes_json,
        'rolagens_json': rolagens_json,
        'defesas_json': defesas_json,
        'resistencias_json': resistencias_json,
        'amplificacao_json': amplificacoes_json,

        'tela_personagem': tela_personagem,          # Objeto Tela_personagem selecionado (ou None)
        'personagens': todos_personagens_tela,       # Lista de todos para o dropdown/menu
        'base_personagem': base_personagem,          # Objeto Base_personagem (ou None)
        'habilidades_raw': habilidades_obj,          # Objeto Habilidade original (ou None)
        'lista_habilidades_data': habilidades_data_formatada, # Lista formatada para JS (ou [])
    }

    print(f"\n--- CONTEXTO FINAL PARA RENDER ---")
    # Evite imprimir o contexto inteiro se ele for muito grande ou contiver objetos complexos
    # print(context)
    print(f"  -> tela_personagem: {'Encontrado' if tela_personagem else 'None'}")
    print(f"  -> personagens count: {todos_personagens_tela.count()}")
    print(f"  -> base_personagem: {'Encontrado' if base_personagem else 'None'}")
    print(f"  -> habilidades_raw: {'Encontrado' if habilidades_obj else 'None'}")
    print(f"  -> lista_habilidades_data count: {len(habilidades_data_formatada)}")


    # Renderiza o template principal passando todo o contexto
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