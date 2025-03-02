from math import floor
from lib.arsenalatt import Elementos, Atributos

def somaTodosAtt(escolha, atributo, conjuntoarmadura, conjuntoacessorio, armasequipadas, conjmaestrias, missoes, bencaodivina, cla, grim, raca, bufint, bufext, habilidade): #fara a soma de todos os atributos escolhidos
    att = atributo.pegaValor(escolha)
    equip = conjuntoarmadura.somarEquip(escolha)
    ace = conjuntoacessorio.somarAces(escolha)
    arma = armasequipadas.somarArmaAtt(escolha)
    maes = conjmaestrias.somarMaes('f', escolha)
    maesb = conjmaestrias.somarMaes('p', escolha)
    mis = missoes.att.pegaValor(escolha)
    bencdiv = bencaodivina.attp.pegaValor(escolha)
    clanf = cla.att.pegaValor(escolha)
    clanp = cla.attp.pegaValor(escolha)
    gri = grim.attp.pegaValor(escolha)
    ra = raca.attp.pegaValor(escolha) 
    bip = bufint.attp.pegaValor(escolha) 
    bef = bufext.att.pegaValor(escolha) 
    bep = bufext.attp.pegaValor(escolha)
    habf = habilidade.att.pegaValor(escolha)
    habp = habilidade.attp.pegaValor(escolha)
    resultado = []

    soma1 = att + equip + ace + arma + mis + maes + clanf + habf
    soma2 = soma1 + soma1 * (maesb + clanp + bencdiv + ra + gri + habp) / 100
    if bip > 0:  # se houver algum tipo de buff interno
        bep = floor(bep / 2)
        bef = floor(bef / 2)
    resultado.append(soma2 + soma2 * (bip + bep) / 100) 
    resultado.append(soma2 + soma2 * bip / 100 + bef) 

    return floor(max(resultado))