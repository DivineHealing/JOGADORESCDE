from django.apps import apps
from django.core.exceptions import FieldDoesNotExist

def pegar_atributos(personagem: str,attescolhido: str):
    attpego = {}

    for model in apps.get_models():  # percorre todos os modelos registrados no django
        try: 
            # verifica se tem o campo escolhido
            if attescolhido in [field.name for field in model._meta.fields]:
                # busca os valores do campo e adiciona ao dicionario
                valores =  list(model.objects.filter(nome=personagem).values_list(attescolhido, flat = True)) 
                attpego[model.__name__] = valores # usa o nome do modelo como chave
        except FieldDoesNotExist:
            continue # ignora se o modelo não tiver o campo do atributo escolhido
        except Exception as e: # talvez retirar futuramente, aqui só pega o tipo de erro para ele nao ter pego o valor
            print(f"Erro ao buscar '{attescolhido}' em {model.__name__}: {e}")

    print(attpego)
