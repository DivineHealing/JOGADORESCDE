from django.apps import apps
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from acessorios.models import Acessorios
from arma.models import Arma
from base_personagem.models import Base_personagem
from conjunto.models import Conjunto
from tela_personagem.models import Tela_personagem, Character_attribute, Character_effects
from cadastro.models import Maestria
from math import floor

campos_personagem = [
    "regenVida", "regenMana", "regenVigor", "vida", "vidaBase", "vidaTotal", "mana", "vigor",
    "forca", "destreza", "inteligencia", "determinacao", "perspicacia", "carisma",
    "forcaPer", "destrezaPer", "inteligenciaPer", "determinacaoPer", "perspicaciaPer", "carismaPer",
    # DEFESA
    "reducao", "defesaFixaEspiritual", "reducaoEspiritual",
    # DANO
    "esmagamento", "penExtra", "danoFinal", "espiritualPerc", "espiritualFixo",
    #OUTROS
    "dreno", "exaustao", "murchamento"]
 

def pegar_atributos(idescolha: int):
    """
    Obtém e soma os valores de um atributo específico de vários modelos relacionados a um personagem,
    filtrando pelos registros que possuem uma ForeignKey para a instância de Base_personagem identificada por `idescolha`,
    e atualiza o campo correspondente na tabela Tela_personagem com essa soma.

    Parâmetros:
    -----------
    idescolha : int
        O ID da instância de Base_personagem utilizada para filtrar os registros relacionados.
    
    attescolhido : str
        O nome do atributo (campo) que deve ser buscado e somado nos modelos relevantes.

    Funcionalidade:
    ---------------
    1. Define uma lista de modelos (MODELOS_RELEVANTES) que estão relacionados ao personagem através de uma ForeignKey.
       - Nesse caso, os modelos são: Base_personagem, Acessorios, Arma, Conjunto.
    2. Busca a instância de Base_personagem com o ID fornecido e a utiliza para filtrar os registros 
       dos modelos que tenham um campo 'personagem' referenciando essa instância.
    3. Para cada modelo em MODELOS_RELEVANTES:
       - Verifica se o campo `attescolhido` existe no modelo.
       - Se existir, filtra os registros cujo campo ForeignKey `personagem` é igual à instância encontrada,
         obtém os valores do campo `attescolhido` (usando values_list),
         converte esses valores em uma lista e os soma.
       - Armazena a soma para cada modelo no dicionário `attpego` e acumula a soma total em `soma_total`.
    4. Atualiza a instância de Tela_personagem (filtrada pelo mesmo id de Base_personagem) 
       atribuindo ao campo `attescolhido` o valor de `soma_total`.
    5. Imprime o dicionário `attpego` (para depuração).

    Tratamento de Erros:
    --------------------
    - Modelos que não possuem o campo `attescolhido` são ignorados.
    - Erros na atualização da instância de Tela_personagem são capturados e impressos.

    Retorno:
    --------
    A função não retorna nenhum valor explícito, mas atualiza a instância de Tela_personagem no banco com a soma total
    e imprime em debug o dicionário contendo a soma dos valores obtidos para cada modelo.
    """
    MODELOS_RELEVANTES = [Base_personagem, Acessorios, Arma, Conjunto, Maestria]  # colocando os modelos que sera usado na lista
    base_instance = MODELOS_RELEVANTES[0].objects.filter(id=idescolha).first()
    # se der errado tirar a iteração,e colocar att escolhido como parametro na função e substituir todos os "campo" por att escolhido
    for campo in campos_personagem:
        attpego = {}
        soma_total = 0 # zerando a soma total toda vez que pega um campo nome(para nao interferir entre outros campos)

        for model in MODELOS_RELEVANTES:
            # Cria um dicionário com os nomes dos campos do modelo como chave e o próprio campo como valor
            model_fields = {f.name: f for f in model._meta.concrete_fields}

            if campo in model_fields: # verifica se o campo existe no modelo atual
                field = model_fields[campo] # Obtém o objeto de campo (field) correspondente ao nome

                # Pega todos os valores desse campo para registros que pertencem ao personagem selecionado
                valores = model.objects.filter(personagem=base_instance).values_list(campo, flat=True)

                # Escolhe o tipo de conversão baseado no tipo do campo
                if isinstance(field, models.IntegerField): # se for um campo inteiro
                    casted = list(map(to_int, valores)) # converte todos os valores para int
                elif isinstance(field, (models.DecimalField, models.FloatField)): # se for um campo decimal ou float
                    casted = list(map(to_float, valores)) # converte os valores para float
                else:
                    continue # Se não for um campo numérico, pula para o próximo modelo

                # Guarda a soma individual dos valores convertidos no dicionário (para debug)
                attpego[model.__name__] = sum(casted)
                # Acumula a soma total de todos os modelos
                soma_total += sum(casted)

        # atualizando a tabela tela personagem
        try:
            Tela_personagem.objects.filter(personagem=base_instance).update(**{campo:soma_total})  # modifica o valor da tabela tela de personagem
        except Exception as e:
            print(f"Erro ao atualizar a 'Tela_personagem:{campo} do personagem {idescolha}': {e}")  # apontando qual erro ocorreu

        #print(attpego)  # depois retirar esse debug


def obter_personagem_sessao(request):
    personagem_id = request.session.get('personagem_id')
    if not personagem_id: # se não conseguiu achar nenhum personagem
        primeiro_personagem =  Base_personagem.objects.first()  # obtém o primeiro personagem
        if primeiro_personagem:  # se existir um personagem
            personagem_id = primeiro_personagem.id
            request.session['personagem_id'] = personagem_id  # ja salva para sessões futuras
            return personagem_id
        return None  # se não existir nenhum personagem
    return personagem_id


def pegar_front(request, escolha, personagem, origem, peca= "", percent=False):
    # ATRIBUTOS BASE
    campos = { # guardando os campos em um dicionario(esquerda é onde salvara no banco|direita é o que vai pegar no request)
        "vida": "vida",
        "vidaBase": "vidaBase",
        "vidaTotal": "vidaTotal",
        "vigor": "vigor",
        "mana": "mana",
        "forca": "forca",
        "destreza": "destreza",
        "inteligencia": "inteligencia",
        "determinacao": "determinacao",
        "perspicacia": "perspicacia",
        "carisma": "carisma",
        "reducao": "reducao",
        "danoFinal": "dmgFinal",
        # definir se a parte de baixo vai ficar junto ou em outro
        "bloqueio": "bloqueio",
        "aumentoDA": "aumentoDA",
        "defesaFixaEspiritual":"defEspiritual",
        "reducaoEspiritual": "redEspiritual",
        "esmagamento": "esmagamento",
        "penExtra": "penExtra",
        "espiritualFixo": "",
        "espiritualPerc": "dmgEspiritual"
    }
    for attr, campo in campos.items():
        if campo in request.POST:  # se o campo existe
            setattr(escolha, attr, request.POST.get(campo, 0)or 0) # adicionara o valor

    if percent:
        # ATRIBUTOS BASE
        camposp = { # guardando os camposem um dicionario(esquerda é onde salvara no banco|direita é o que via pegar no request)
            "forcaPer": "forcaPer",
            "destrezaPer": "destrezaPer",
            "inteligenciaPer": "inteligenciaPer",
            "determinacaoPer": "determinacaoPer",
            "perspicaciaPer": "perspicaciaPer",
            "carismaPer": "carismaPer",
        }
        for attr, campo in camposp.items():
            if campo in request.POST:  # se o campo existe
                setattr(escolha, attr, request.POST.get(campo, 0)or 0) # adicionara o valor

    i = 1
    # REGENERAÇÃO
    while True:
        tipo = request.POST.get(f'regeneracaoTipo{i}')
        valor = request.POST.get(f'regeneracao{i}')

        if not any([tipo, valor]):
            break
        
        if tipo == "regenVida":
            escolha.regenVida = valor
        elif tipo == "regenMana":
            escolha.regenMana = valor
        elif tipo == "regenVigor":
            escolha.regenVigor = valor
        i += 1

    i = 1
    # Outros
    while True:
        tipo = request.POST.get(f'statusEffectTipo{i}')
        valor = request.POST.get(f'statusEffect{i}')

        if not any([tipo, valor]):
            break
        
        if tipo == "dreno":
            escolha.dreno = valor
        elif tipo == "exaustao":
            escolha.exaustao = valor
        elif tipo == "murchamento":
            escolha.murchamento = valor
        i += 1
    escolha.save()

    i = 1
    # ROLAGENS
    while True:
        tipo = request.POST.get(f'rolagemTipo{i}') # tentando pegar os valores no front
        valor = request.POST.get(f'rolagem{i}')

        if not any([tipo, valor]): # se nenhum dos dois campos tem valores
            #  ira pegar os itens sobressalentes e colocar numa variavel
            extras = Character_attribute.objects.filter(
                models.Q(personagem= personagem) &
                models.Q(posicao__gte=i) &
                models.Q(variavelTipo= "rolagem") &
                models.Q(origem= origem)
            )
            for c in extras: # para cada um nos sobressalentes
                setattr(c, "variavelValor", 0)
                c.save()
            break  # sai do loop
        
        #  verificando se existe o objeto especifico na tabela, se nao existir, cria
        roll, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "rolagem", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "rolagem",
                "variavelPropriedade": tipo.strip().capitalize(),
                "variavelValor": valor,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        roll.save()
        i += 1

    i = 1
    # DEFESAS
    while True:
        elemento = request.POST.get(f'elementoDefesa{i}')
        defesa = request.POST.get(f'defesa{i}')
        resistencia = request.POST.get(f'resistencia{i}')

        if not any([elemento, defesa, resistencia]):  # se nenhum tiver valor para
            #  ira pegar os itens sobressalentes e colocar numa variavel
            extras = Character_attribute.objects.filter(
                models.Q(personagem= personagem) &
                models.Q(posicao__gte=i) &
                (models.Q(variavelTipo= "defesa") | models.Q(variavelTipo= "resistencia")) &
                models.Q(origem= origem)
            )
            for c in extras: # para cada um nos sobressalentes
                setattr(c, "variavelValor", 0)
                c.save()
            break  # nao tem mais campos entao para
        
        defesa_obj, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "defesa", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "defesa",
                "variavelPropriedade": elemento.strip().capitalize(),
                "variavelValor": defesa,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        resistencia_obj, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "resistencia", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "resistencia",
                "variavelPropriedade": elemento.strip().capitalize(),
                "variavelValor": resistencia,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        #setattr(telap, f"elementoDefesa_{i}", elemento)
        #setattr(telap, f"elementoResistencia_{i}", elemento)
        defesa_obj.save()
        resistencia_obj.save()
        i += 1
    
    i = 1
    # DANO
    while True:
        elemento = request.POST.get(f'elementoDano{i}')
        dano = request.POST.get(f'dano{i}')
        penetracao = request.POST.get(f'penetracao{i}')

        if not any([elemento, dano, penetracao]):
            #  ira pegar os itens sobressalentes e colocar numa variavel
            extras = Character_attribute.objects.filter(
                models.Q(personagem= personagem) &
                models.Q(posicao__gte=i) &
                (models.Q(variavelTipo= "dano") | models.Q(variavelTipo= "penetracao")) &
                models.Q(origem= origem)
            )
            for c in extras: # para cada um nos sobressalentes
                setattr(c, "variavelValor", 0)
                c.save()
            break
        
        dano_obj, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "dano", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "dano",
                "variavelPropriedade": elemento.strip().capitalize(),
                "variavelValor": dano,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        penetracao_obj, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "penetracao", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "penetracao",
                "variavelPropriedade": elemento.strip().capitalize(),
                "variavelValor": penetracao,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        dano_obj.save()
        penetracao_obj.save()
        i += 1

    i = 1
    # AMPLIFICAÇÃO
    while True:
        tipo = request.POST.get(f'amplificacaoTipo{i}')
        valor = request.POST.get(f'amplificacao{i}')

        if not any([tipo, valor]):
            #  ira pegar os itens sobressalentes e colocar numa variavel
            extras = Character_attribute.objects.filter(
                models.Q(personagem= personagem) &
                models.Q(posicao__gte=i) &
                models.Q(variavelTipo= "amplificacao") &
                models.Q(origem= origem)
            )
            for c in extras: # para cada um nos sobressalentes
                setattr(c, "variavelValor", 0)
                c.save()
            break
        
        amplificacao, _ = Character_attribute.objects.update_or_create(personagem= personagem, 
            posicao= i, 
            variavelTipo= "amplificacao", 
            origem= origem,
            defaults={
                "personagem": personagem,
                "variavelTipo": "amplificacao",
                "variavelPropriedade": tipo.strip().capitalize(),
                "variavelValor": valor,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        amplificacao.save()
        i += 1


def pegar_efeito(request, personagem, origem, peca):
    i = 1
    #Tipo do efeito
    while True:
        tipo = request.POST.get(f"efeitoTipo{i}")
        nome = request.POST.get(f"efeitoNome{i}")
        descricao = request.POST.get(f"efeitoDesc{i}")

        if not any([tipo, nome, descricao]):  # se não houver nenhum dos tipos
            extras = Character_effects.objects.filter(
                models.Q(personagem= personagem) &
                models.Q(posicao__gte=i) &
                models.Q(peca= peca)
            )
            for c in extras:  # para cada peça sobressalent
                setattr(c, "variavelTipo", "")
                setattr(c, "variavelNome", "")
                setattr(c, "variavelDescricao", "")
                c.save()
            break

        #  verificando se existe o objeto especifico na tabela, se nao existir, ele ira criar
        efeito, _ = Character_effects.objects.update_or_create(
            personagem= personagem,
            posicao= i,
            peca= peca,
            defaults={
                "personagem": personagem,
                "variavelTipo": tipo,
                "variavelNome": nome,
                "variavelDescricao": descricao,
                "posicao": i,
                "peca": peca,
                "origem": origem
            }
        )
        efeito.save()
        i += 1


def status_perc(personagem_id):
    status = ['forca', 'destreza', 'inteligencia', 'determinacao', 'perspicacia', 'carisma']
    statusper = ['forcaPer', 'destrezaPer', 'inteligenciaPer', 'determinacaoPer', 'perspicaciaPer', 'carismaPer']

    personagem = Tela_personagem.objects.get(id=personagem_id) 

    for i in range(6):
        flat = getattr(personagem, status[i])  # pegando atributoflat
        perc = getattr(personagem, statusper[i])  # pegando atributo porcentual

        
        calc = floor(flat + flat * perc / 100)  # fazendo o calculo
        setattr(personagem, f'{status[i]}Total', calc)  # salvando no campo apropriado
        personagem.save()


def to_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
 
    
def to_float(value, default=0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default
