from lib.conjarmadura import ConjArmadura
from lib.conjacessorio import ConjAcessorio


def somaTodosAtt(escolha, atributo, conjuntoarmadura, conjuntoacessorio): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    ace = conjuntoacessorio.somarAces(escolha)
    soma1 = att + equip + ace
    return soma1
    