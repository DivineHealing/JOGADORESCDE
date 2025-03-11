def lvlup(xp):
    lvl = 1  # lvl atual
    passo = 0  # quanto ele tem que ajustar para ir ao proximo level
    antecessor = 0  # xp necessario para chegar nesse lvl
    while True:
        if lvl == 1:
            passo = 100
        elif lvl < 10:
            passo += 50
        elif lvl < 20:
            passo += 500
        elif lvl < 30:
            if lvl == 20:
                passo -= 500
            passo += 5000
        elif lvl < 40:
            passo += 10000
        elif lvl < 55:
            passo += 25000
        elif lvl < 60:
            passo += 50000
        elif lvl < 65:
            passo += 100000
        elif lvl < 70:
            passo += 150000
        elif lvl < 75:
            passo += 200000
        elif lvl < 80:
            passo += 250000
        elif lvl < 85:
            passo += 300000
        elif lvl < 90:
            passo += 350000
        elif lvl < 95:
            passo += 400000
        else:
            passo += 450000
        nextlvl = antecessor + passo  # o proximo lvl só é alcançando apos passar o ajuste somado ao necessario do lvl atual
        if lvl == 100:  # se chegou no lvl maximo
            break  # para de iterar pq não tem mais oq adicionar de lvl
        elif xp >= nextlvl: # se o xp for o suficiente de subir de lvl
            antecessor = nextlvl  #  ajusta o xp necessario que precisou para chegar nesse lvl
            lvl += 1 # sobe de lvl
        else:
            break
    return lvl

# versão diferente
'''def lvlup(xp):
    lvl = 1  # Nível inicial
    antecessor = 0  # XP necessário para o nível inicial
    passo = 0
    # Definindo os incrementos de XP por faixa de nível
    passos = [
        (1, 100),    # Nível 1
        (10, 50),    # Níveis 2-9
        (20, 500),   # Níveis 10-19
        (30, 5000),  # Níveis 20-29
        (40, 10000), # Níveis 30-39
        (55, 25000), # Níveis 40-54
        (60, 50000), # Níveis 55-59
        (65, 100000),# Níveis 60-64
        (70, 150000),# Níveis 65-69
        (75, 200000),# Níveis 70-74
        (80, 250000),# Níveis 75-79
        (85, 300000),# Níveis 80-84
        (90, 350000),# Níveis 85-89
        (95, 400000),# Níveis 90-94
        (100, 450000),# Níveis 95-99
    ]

    # Loop para calcular o nível atual
    while lvl < 100:
        # Identifica o incremento de XP para a faixa atual
        for limit, incremento in passos:
            if lvl == 1:
                passo += 100
                break
            if lvl < limit:
                if lvl == 20:  # ajuste especifico do nvl 20
                    passo -= 500
                passo += incremento
                break

        nextlvl = antecessor + passo  # XP necessário para o próximo nível

        if xp >= nextlvl:  # Se o XP for suficiente para subir de nível
            antecessor = nextlvl  # Atualiza o XP necessário para o próximo nível
            lvl += 1  # Avança o nível
        else:
            break  # Sai do loop se o XP não for suficiente para o próximo nível
    return lvl'''