from math import floor
from lib.conjarmadura import ConjArmadura
from lib.conjacessorio import ConjAcessorio
from lib.armasemmaos import ArmasEmMaos
from lib.conjmaestria import Conjmaestria
from lib.missoes import Missoes



def somaTodosAtt(escolha, atributo, conjuntoarmadura, conjuntoacessorio, armasequipadas, conjmaestrias, missoes): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    ace = conjuntoacessorio.somarAces(escolha)
    arma = armasequipadas.somarArmaAtt(escolha)
    maes = conjmaestrias.somarMaes('f', escolha)
    maesb = conjmaestrias.somarMaes('p', escolha)
    mis = missoes.att.pegaValor(escolha)
    soma1 = att + equip + ace + arma + mis + maes
    soma2 = soma1 + soma1 * maesb / 100
    return floor(soma2)
    