from lib.conjarmadura import ConjArmadura
from lib.conjacessorio import ConjAcessorio
from lib.armasemmaos import ArmasEmMaos


def somaTodosAtt(escolha, atributo, conjuntoarmadura, conjuntoacessorio, armasequipadas): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    ace = conjuntoacessorio.somarAces(escolha)
    arma = armasequipadas.somarArmaAtt(escolha)
    soma1 = att + equip + ace + arma
    return soma1
    