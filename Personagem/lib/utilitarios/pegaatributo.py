from django.apps import apps
from django.core.exceptions import FieldDoesNotExist

def pegar_atributos(idescolha: int ,attescolhido: str):
    """
    Obtém e soma(futuramente aplicara a equação de stastus) os valores de um atributo específico de diferentes modelos, 
    filtrando pelo ID fornecido, e atualiza a tabela 'Tela_personagem' com o valor somado.

    Parâmetros:
    -----------
    idescolha : int
        O ID do personagem ou entidade a ser filtrado nos modelos.
    
    attescolhido : str
        O nome do atributo a ser buscado e somado.

    Funcionalidade:
    ---------------
    - Percorre todos os modelos registrados no Django.
    - Ignora o modelo 'Tela_personagem' (pois ele é o destino da atualização).
    - Filtra cada modelo pelo ID fornecido e busca o valor do campo 'attescolhido'.
    - Soma os valores encontrados e armazena-os no dicionário `attpego`.
    - Atualiza a tabela 'Tela_personagem' com a soma total do atributo escolhido.
    
    Tratamento de Erros:
    --------------------
    - Ignora modelos que não possuem o campo escolhido.
    - Captura e exibe erros gerais ao acessar modelos e atualizar a tabela destino.

    Retorno:
    --------
    Nenhum retorno explícito, mas imprime mensagens de erro quando aplicável.
    """
    attpego = {}
    soma_total = 0

    for model in apps.get_models():  # percorre todos os modelos registrados no django
        if model.__name__ == 'Tela_personagem': # ignorando a tela de personagem(ela e o destino, verificar ela só causaria problemas)
            continue

        try: 
            # verifica se tem o campo escolhido
            if attescolhido in [field.name for field in model._meta.fields]:
                # busca o valor do campo do personagem especificado(pelo id) e adiciona ao dicionario
                valor = model.objects.filter(id=idescolha).values_list(attescolhido, flat = True).first()
                if valor:  # adiciona somente se tiver valor
                    attpego[model.__name__] = valor # usa o nome do modelo como chave
                    soma_total += valor # Soma de teste, futuramente retirar
        except FieldDoesNotExist:
            continue # ignora se o modelo não tiver o campo do atributo escolhido
        except Exception as e: # talvez retirar futuramente, aqui só pega o tipo de erro para ele nao ter pego o valor
            print(f"Erro ao buscar '{attescolhido}' em {model.__name__}: {e}")
    
    # atualizando a tabela tela personagem
    try:
        model_destino = apps.get_model('tela_personagem.Tela_personagem') # obtém o modelo da tabela de personagem
        model_destino.objects.filter(id=idescolha).update(**{attescolhido:soma_total})  # modifica o valor
    except Exception as e:
        print(f"Erro ao atualizar a 'Tela_personagem:{attescolhido} do personagem {idescolha}': {e}")  # apontando qual erro ocorreu

    print(attpego)  # depois retirar esse debug
