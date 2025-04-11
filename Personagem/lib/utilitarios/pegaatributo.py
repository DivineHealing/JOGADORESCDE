from django.apps import apps
from django.shortcuts import render
from django.core.exceptions import FieldDoesNotExist
from acessorios.models import Acessorios
from arma.models import Arma
from base_personagem.models import Base_personagem
from conjunto.models import Conjunto
from tela_personagem.models import Tela_personagem
from cadastro.models import Maestria


def pegar_atributos(idescolha: int, attescolhido: str):
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
    attpego = {}
    soma_total = 0

    for model in MODELOS_RELEVANTES:
        if attescolhido in [field.name for field in model._meta.fields]:  # achara o campo especificado
            valores = model.objects.filter(personagem=base_instance).values_list(attescolhido, flat=True)  # pegara todos os vallores do campo especificado
            attpego[model.__name__] = sum(valores)  # somara e guardara a informação
            soma_total += sum(valores)

  
    # atualizando a tabela tela personagem
    try:
        Tela_personagem.objects.filter(id=idescolha).update(**{attescolhido:soma_total})  # modifica o valor da tabela tela de personagem
    except Exception as e:
        print(f"Erro ao atualizar a 'Tela_personagem:{attescolhido} do personagem {idescolha}': {e}")  # apontando qual erro ocorreu

    print(attpego)  # depois retirar esse debug


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
