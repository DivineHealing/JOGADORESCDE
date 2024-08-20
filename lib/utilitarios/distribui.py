from lib.arsenalatt import Elementos, Atributos

def distribuidor(classe, data, idvar=''):  # ira distribuir os valores para a classe selecionada
    if isinstance(classe, Atributos):  # Ira checar se a classe da variavel é Atributos, para então distribuir
        classe.forca = float(data['forca' + idvar]) or 0
        classe.destreza = float(data['destreza' + idvar]) or 0
        classe.inteligencia = float(data['inteligencia' + idvar]) or 0
        classe.determinacao = float(data['determinacao' + idvar]) or 0
        classe.percepcao = float(data['percepcao' + idvar]) or 0
        classe.carisma =float(data['carisma' + idvar]) or 0
    elif isinstance(classe, Elementos):  # melhorar essa condição para distribuir os tipo e pegar melhor o identificador??
        classe.tipo1 = float(data['tipo1' + idvar]) or 0
        classe.tipo2 = float(data['tipo2' + idvar]) or 0
        classe.tipo3 = float(data['tipo3' + idvar]) or 0