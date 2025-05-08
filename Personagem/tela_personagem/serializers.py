from django.core.serializers import serialize
import json

danos_json = serialize("json", dados_dano, fields=("variavelPropriedade", "variavelValor"))
penetracoes_json = serialize("json", dados_penetracao, fields=("variavelPropriedade", "variavelValor"))


context = {
    # ...
    'danos': danos_json,
    'penetracoes': penetracoes_json,
    # ...
}
