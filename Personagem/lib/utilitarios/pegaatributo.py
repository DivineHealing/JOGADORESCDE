from django.apps import apps
from django.core.exceptions import FieldDoesNotExist

def pegar_atributos(personagem: str,attescolhido: str):
    attpego = {}
    soma_total = 0

    for model in apps.get_models():  # percorre todos os modelos registrados no django
        if model.__name__ == 'Tela_personagem': # ignorando a tela de personagem(ela e o destino, verificar ela só causaria problemas)
            continue

        try: 
            # verifica se tem o campo escolhido
            if attescolhido in [field.name for field in model._meta.fields]:
                # busca o valor do campo do personagem especificado e adiciona ao dicionario
                valor = model.objects.filter(nome=personagem).values_list(attescolhido, flat = True).first()
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
        model_destino.objects.filter(nome=personagem).update(**{attescolhido:soma_total})
    except Exception as e:
        print(f"Erro ao atualizar a 'Tela_personagem:{attescolhido} do personagem {personagem}': {e}")  # apontando qual erro ocorreu

    print(attpego)
