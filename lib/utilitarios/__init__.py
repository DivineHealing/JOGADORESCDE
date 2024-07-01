from lib.conjarmadura import ConjArmadura


def somaTodosAtt(escolha, atributo, conjuntoarmadura): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    soma1 = att + equip
    return soma1
    