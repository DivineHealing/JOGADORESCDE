from math import floor
from lib.conjarmadura import ConjArmadura
from lib.conjacessorio import ConjAcessorio
from lib.armasemmaos import ArmasEmMaos
from lib.maestrias import Maestrias
from lib.missoes import Missoes



def somaTodosAtt(escolha, atributo, conjuntoarmadura, conjuntoacessorio, armasequipadas, maestrias, missoes): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    ace = conjuntoacessorio.somarAces(escolha)
    arma = armasequipadas.somarArmaAtt(escolha)
    maes = maestrias.att.pegaValor(escolha)
    mis = missoes.att.pegaValor(escolha)
    soma1 = att + equip + ace + arma + mis
    soma2 = soma1 + soma1 * maes / 100
    return floor(soma2)
    