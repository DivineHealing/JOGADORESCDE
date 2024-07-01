from lib.conjarmadura import ConjArmadura


def somaTodosAtt(escolha, atributo, conjuntoarmadura):
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    soma1 = att + equip
    return soma1
    