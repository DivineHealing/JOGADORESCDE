from flask import Flask, jsonify, render_template, request
from math import trunc
from lib.atributos import Atributos
from lib.equipamentos import Equipamento
from lib.conjarmadura import ConjArmadura
from lib.acessorio import Acessorio
from lib.conjacessorio import ConjAcessorio
from lib.utilitarios import somaTodosAtt
from lib.arma import Arma
from lib.armasemmaos import ArmasEmMaos
from lib.maestrias import Maestrias
from lib.conjmaestria import Conjmaestria
from lib.missoes import Missoes
from lib.bencaodiv import BencaoDiv
from lib.bonusex import BonusEx
from lib.grimorio import Grimorio
from lib.habilidade import Habilidade
from lib.raca import Raca
from lib.cla import Cla
from lib.elementos import Elementos

info = [] #lista de controle

main = Flask(__name__)

@main.route("/")
def home():
    return render_template('home.html')

@main.route("/visual")
def visual():
    return render_template('teste/visual.html')

# CODIGO AQUI
@main.route("/atrstatus", methods=['POST'])
def atrstatus():
    data = request.get_json() # AQUI PEGA O DADO

    attbase = Atributos(  # criando o objeto atributos base do persongem
        float(data['forca']),
        float(data['destreza']),
        float(data['inteligencia']),
        float(data['determinacao']),
        float(data['percepcao']),
        float(data['carisma'])
    )
    
    # Criando atributos e equipamentos
    fclassatt = Atributos(
        float(data['forcaE']),
        float(data['destrezaE']),
        float(data['inteligenciaE']),
        float(data['determinacaoE']),
        float(data['percepcaoE']),
        float(data['carismaE'])
    )
    elmo = Equipamento(fclassatt)  # criando objeto elmo

    fclassatt = Atributos(
        float(data['forcaP']),
        float(data['destrezaP']),
        float(data['inteligenciaP']),
        float(data['determinacaoP']),
        float(data['percepcaoP']),
        float(data['carismaP'])
    )
    peitoral = Equipamento(fclassatt)  # criando objeto peitoral

    fclassatt = Atributos(
        float(data['forcaL']),
        float(data['destrezaL']),
        float(data['inteligenciaL']),
        float(data['determinacaoL']),
        float(data['percepcaoL']),
        float(data['carismaL'])
    )
    luva = Equipamento(fclassatt)  # criando objeto luva

    fclassatt = Atributos(
        float(data['forcaC']),
        float(data['destrezaC']),
        float(data['inteligenciaC']),
        float(data['determinacaoC']),
        float(data['percepcaoC']),
        float(data['carismaC'])
    )
    calca = Equipamento(fclassatt)  # criando objeto calca

    fclassatt = Atributos(
        float(data['forcaB']),
        float(data['destrezaB']),
        float(data['inteligenciaB']),
        float(data['determinacaoB']),
        float(data['percepcaoB']),
        float(data['carismaB'])
    )
    bota = Equipamento(fclassatt)  # criando objeto bota

    conja = ConjArmadura(elmo, peitoral, luva, calca, bota)  # criando objeto de conjunto de armadura

    # Criando acessórios
    fclassatt = Atributos(
        float(data['forcaAn1']),
        float(data['destrezaAn1']),
        float(data['inteligenciaAn1']),
        float(data['determinacaoAn1']),
        float(data['percepcaoAn1']),
        float(data['carismaAn1'])
    )
    anel1 = Acessorio(fclassatt)  # criando o objeto anel1

    fclassatt = Atributos(
        float(data['forcaAn2']),
        float(data['destrezaAn2']),
        float(data['inteligenciaAn2']),
        float(data['determinacaoAn2']),
        float(data['percepcaoAn2']),
        float(data['carismaAn2'])
    )
    anel2 = Acessorio(fclassatt)  # criando o objeto anel2

    fclassatt = Atributos(
        float(data['forcaAn3']),
        float(data['destrezaAn3']),
        float(data['inteligenciaAn3']),
        float(data['determinacaoAn3']),
        float(data['percepcaoAn3']),
        float(data['carismaAn3'])
    )
    anel3 = Acessorio(fclassatt)  # criando o objeto anel3

    fclassatt = Atributos(
        float(data['forcaAn4']),
        float(data['destrezaAn4']),
        float(data['inteligenciaAn4']),
        float(data['determinacaoAn4']),
        float(data['percepcaoAn4']),
        float(data['carismaAn4'])
    )
    anel4 = Acessorio(fclassatt)  # criando o objeto anel4

    fclassatt = Atributos(
        float(data['forcaBc1']),
        float(data['destrezaBc1']),
        float(data['inteligenciaBc1']),
        float(data['determinacaoBc1']),
        float(data['percepcaoBc1']),
        float(data['carismaBc1'])
    )
    brac1 = Acessorio(fclassatt)  # criando o objeto bracelete1

    fclassatt = Atributos(
        float(data['forcaBc2']),
        float(data['destrezaBc2']),
        float(data['inteligenciaBc2']),
        float(data['determinacaoBc2']),
        float(data['percepcaoBc2']),
        float(data['carismaBc2'])
    )
    brac2 = Acessorio(fclassatt)  # criando o objeto bracelete2

    fclassatt = Atributos(
        float(data['forcaBr1']),
        float(data['destrezaBr1']),
        float(data['inteligenciaBr1']),
        float(data['determinacaoBr1']),
        float(data['percepcaoBr1']),
        float(data['carismaBr1'])
    )
    brinc1 = Acessorio(fclassatt)  # criando o objeto brinco 1

    fclassatt = Atributos(
        float(data['forcaBr2']),
        float(data['destrezaBr2']),
        float(data['inteligenciaBr2']),
        float(data['determinacaoBr2']),
        float(data['percepcaoBr2']),
        float(data['carismaBr2'])
    )
    brinc2 = Acessorio(fclassatt)  # criando o objeto brinco 2

    fclassatt = Atributos(
        float(data['forcaCo']),
        float(data['destrezaCo']),
        float(data['inteligenciaCo']),
        float(data['determinacaoCo']),
        float(data['percepcaoCo']),
        float(data['carismaCo'])
    )
    colar = Acessorio(fclassatt)  # criando o objeto colar  

    fclassatt = Atributos(
        float(data['forcaCa']),
        float(data['destrezaCa']),
        float(data['inteligenciaCa']),
        float(data['determinacaoCa']),
        float(data['percepcaoCa']),
        float(data['carismaCa'])
    )
    capa = Acessorio(fclassatt)  # criando o objeto capa  

    fclassatt = Atributos(
        float(data['forcaCi']),
        float(data['destrezaCi']),
        float(data['inteligenciaCi']),
        float(data['determinacaoCi']),
        float(data['percepcaoCi']),
        float(data['carismaCi'])
    )
    cinto = Acessorio(fclassatt)  # criando o objeto cinto  
        
    conjac = ConjAcessorio(anel1, anel2, anel3, anel4, brac1, brac2, brinc1, brinc2, colar, capa, cinto)  # criando o objeto do conjunto de acessórios

    # Criando armas
    fclassatt = Atributos(
        float(data['forcaAp']),
        float(data['destrezaAp']),
        float(data['inteligenciaAp']),
        float(data['determinacaoAp']),
        float(data['percepcaoAp']),
        float(data['carismaAp'])
    )
    armaprincipal = Arma(fclassatt)  # criando o objeto da arma principal

    fclassatt = Atributos(
        float(data['forcaAs']),
        float(data['destrezaAs']),
        float(data['inteligenciaAs']),
        float(data['determinacaoAs']),
        float(data['percepcaoAs']),
        float(data['carismaAs'])
    )
    armasecundaria = Arma(fclassatt, False)  # criando o objeto arma secundaria

    armasequip = ArmasEmMaos(armaprincipal, armasecundaria) # criando objeto das armas em mãos 

    # Criando maestrias
    fclassatt = Atributos(
        float(data['forcaMPR']),
        float(data['destrezaMPR']),
        float(data['inteligenciaMPR']),
        float(data['determinacaoMPR']),
        float(data['percepcaoMPR']),
        float(data['carismaMPR'])
    )

    pclassatt = Atributos(
        float(data['forcaMPB']),
        float(data['destrezaMPB']),
        float(data['inteligenciaMPB']),
        float(data['determinacaoMPB']),
        float(data['percepcaoMPB']),
        float(data['carismaMPB'])
    )
    maesp = Maestrias(fclassatt, pclassatt)  # criando objeto da maestrias principal

    fclassatt = Atributos(
        float(data['forcaMSR']),
        float(data['destrezaMSR']),
        float(data['inteligenciaMSR']),
        float(data['determinacaoMSR']),
        float(data['percepcaoMSR']),
        float(data['carismaMSR'])
    )

    pclassatt = Atributos(
        float(data['forcaMSB']),
        float(data['destrezaMSB']),
        float(data['inteligenciaMSB']),
        float(data['determinacaoMSB']),
        float(data['percepcaoMSB']),
        float(data['carismaMSB'])
    )
    maess = Maestrias(fclassatt, pclassatt)  # criando objeto da maestrias Secundaria

    fclassatt = Atributos(
        float(data['forcaMUR']),
        float(data['destrezaMUR']),
        float(data['inteligenciaMUR']),
        float(data['determinacaoMUR']),
        float(data['percepcaoMUR']),
        float(data['carismaMUR'])
    )

    pclassatt = Atributos(
        float(data['forcaMUB']),
        float(data['destrezaMUB']),
        float(data['inteligenciaMUB']),
        float(data['determinacaoMUB']),
        float(data['percepcaoMUB']),
        float(data['carismaMUB'])
    )
    maesu = Maestrias(fclassatt, pclassatt)  # criando objeto da maestrias utilitaria

    conjmaes = Conjmaestria(maesp, maess, maesu)  # criando o objeto do conjunto de maestrias

    # Criando missões
    fclassatt = Atributos(
        float(data['forcaMS']),
        float(data['destrezaMS']),
        float(data['inteligenciaMS']),
        float(data['determinacaoMS']),
        float(data['percepcaoMS']),
        float(data['carismaMS'])
    )
    mis = Missoes(fclassatt)  # criando objeto das missões


    pclassatt = Atributos(
        float(data['forcaBD']), 
        float(data['destrezaBD']), 
        float(data['inteligenciaBD']), 
        float(data['determinacaoBD']), 
        float(data['percepcaoBD']),
        float(data['carismaBD'])
    )  # Criando atributos da Benção Divina (apenas percentual)
    bd = BencaoDiv(pclassatt)  # criando o objeto das Bençãos divinas

    fclassatt = Atributos(
        float(data['forcaDCF']), 
        float(data['destrezaDCF']), 
        float(data['inteligenciaDCF']), 
        float(data['determinacaoDCF']), 
        float(data['percepcaoDCF']),
        float(data['carismaDCF'])
    )  # Criando atributos da dadiva do clã fixo
    pclassatt = Atributos(
        float(data['forcaDCP']), 
        float(data['destrezaDCP']), 
        float(data['inteligenciaDCP']), 
        float(data['determinacaoDCP']), 
        float(data['percepcaoDCP']),
        float(data['carismaDCP'])
    )  # Criando atributos da dadiva do clã percentual
    cla = Cla(fclassatt, pclassatt)  # criando o objeto da dadiva doc clã

    pclassatt = Atributos(
        float(data['forcaG']),
        float(data['destrezaG']), 
        float(data['inteligenciaG']), 
        float(data['determinacaoG']), 
        float(data['percepcaoG']),
        float(data['carismaG'])
    )  # Criando atributos do grimorio (apenas percentual)
    grim = Grimorio(pclassatt)  # criando o objeto do grimorio

    pclassatt = Atributos(
        float(data['forcaraca']), 
        float(data['destrezaraca']), 
        float(data['inteligenciaraca']), 
        float(data['determinacaoraca']), 
        float(data['percepcaoraca']),
        float(data['carismaraca'])
    )  # Criando atributos da Raça (apenas percentual)
    raca = Raca(pclassatt)  # criando o objeto da raça

    fclassatt = Atributos(
        float(data['forcaBF']), 
        float(data['destrezaBF']), 
        float(data['inteligenciaBF']), 
        float(data['determinacaoBF']), 
        float(data['percepcaoBF']),
        float(data['carismaBF'])
    )  # Criando atributos do bonus percentual fixo
    pclassatt = Atributos(
        float(data['forcaBP']), 
        float(data['destrezaBP']), 
        float(data['inteligenciaBP']), 
        float(data['determinacaoBP']), 
        float(data['percepcaoBP']),
        float(data['carismaBP'])
    )  # Criando atributos do bonus externo percentual
    be = BonusEx(fclassatt, pclassatt)  # criando o objeto dos bonus externos

    fclassatt = Atributos(
        float(data['forcaHF']), 
        float(data['destrezaHF']), 
        float(data['inteligenciaHF']), 
        float(data['determinacaoHF']), 
        float(data['percepcaoHF']),
        float(data['carismaHF'])
    )  # Criando atributos da habilidade fixo
    pclassatt = Atributos(
        float(data['forcaHP']), 
        float(data['destrezaHP']), 
        float(data['inteligenciaHP']), 
        float(data['determinacaoHP']), 
        float(data['percepcaoHP']),
        float(data['carismaHP'])
    )  # Criando atributos do habilidade percentual
    habilidadesp = Habilidade(fclassatt, pclassatt)  # criando o objeto das habilidades

    info.extend([attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp]) #futuramente ira para a classe personagem/ retirar provavelmente quando tiver o banco de dedos

    forcaCJ = conja.somarEquip('forca') #funcao da classe para somar os atributos equipamentos
    destrezaCJ = conja.somarEquip('destreza')
    inteligenciaCJ = conja.somarEquip('inteligencia')
    determinacaoCJ = conja.somarEquip('determinacao')
    percepcaoCJ = conja.somarEquip('percepcao')
    carismaCJ = conja.somarEquip('carisma')

    forcaAr = armasequip.somarArmaAtt('forca')  # função que ira somar os atributos das armas
    destrezaAr = armasequip.somarArmaAtt('destreza')
    inteligenciaAr = armasequip.somarArmaAtt('inteligencia')
    determinacaoAr = armasequip.somarArmaAtt('determinacao')
    percepcaoAr = armasequip.somarArmaAtt('percepcao')
    carismaAr = armasequip.somarArmaAtt('carisma')

    forcaAc = conjac.somarAces('forca') #funcao da classe para somar os atributos dos acessorios
    destrezaAc = conjac.somarAces('destreza')
    inteligenciaAc = conjac.somarAces('inteligencia')
    determinacaoAc = conjac.somarAces('determinacao')
    percepcaoAc = conjac.somarAces('percepcao')
    carismaAc = conjac.somarAces('carisma')

    forcat = attbase.forca + conjmaes.somarMaes('f','forca') + mis.att.forca #ira somar todos os atributos base
    destrezat = attbase.destreza + conjmaes.somarMaes('f', 'destreza') + mis.att.destreza
    inteligenciat = attbase.inteligencia + conjmaes.somarMaes('f', 'inteligencia') + mis.att.inteligencia
    determinacaot = attbase.determinacao + conjmaes.somarMaes('f', 'determinacao') + mis.att.determinacao
    percepcaot = attbase.percepcao + conjmaes.somarMaes('f', 'percepcao') + mis.att.percepcao
    carismat = attbase.carisma + conjmaes.somarMaes('f', 'carisma') + mis.att.carisma

    forcaT = somaTodosAtt('forca', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp) #funcao para pegar a soma total de todos atributos(personagem, equipamento, acessorio)
    destrezaT = somaTodosAtt('destreza', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp)
    inteligenciaT = somaTodosAtt('inteligencia', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp)
    determinacaoT = somaTodosAtt('determinacao', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp)
    percepcaoT = somaTodosAtt('percepcao', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp)
    carismaT = somaTodosAtt('carisma', attbase, conja, conjac, armasequip, conjmaes, mis, bd, cla, grim, raca, be, habilidadesp)

    return jsonify(forcaT=forcaT, destrezaT=destrezaT, inteligenciaT=inteligenciaT, determinacaoT=determinacaoT,
                   percepcaoT=percepcaoT, carismaT=carismaT, forcaCJ=forcaCJ, destrezaCJ=destrezaCJ, inteligenciaCJ=inteligenciaCJ,
                   determinacaoCJ=determinacaoCJ, percepcaoCJ=percepcaoCJ, carismaCJ=carismaCJ, forcaAc=forcaAc, destrezaAc=destrezaAc,
                   inteligenciaAc=inteligenciaAc, determinacaoAc=determinacaoAc, percepcaoAc=percepcaoAc, carismaAc=carismaAc,
                   forcaAr=forcaAr, destrezaAr=destrezaAr, inteligenciaAr=inteligenciaAr, determinacaoAr=determinacaoAr, percepcaoAr=percepcaoAr,
                   carismaAr=carismaAr, forcat=forcat, destrezat=destrezat, inteligenciat=inteligenciat, determinacaot=determinacaot, percepcaot=percepcaot, carismat=carismat) # AQUI VAI JOGAR O DADO PRO FRONT

@main.route("/redvida", methods=['POST'])
def redvida():
    data = request.get_json()
    vidaB = float(data['vidaB'])
    vidaE = float(data['vidaE'])
    vidaA = float(data['vidaA'])/100+1
    vidaT = float(data['vidaT'])/100+1
    dano = float(data['dano'])
    
    vidaTo = trunc((vidaB + vidaE)*vidaA*vidaT)
    vidaAt = vidaTo - dano
    if vidaAt >= (vidaTo*1.33):
        vidaTo = ""
        vidaAt = "Morreu"
        
    elif vidaAt <= (vidaTo*1.33) and vidaAt <= 0:
        vidaTo = ""
        vidaAt = "Desacordado"
        
    manaB = float(data['manaB'])
    manaE = float(data['manaE'])
    gastoM = float(data['gastoM'])
    
    manaTo = manaB + manaE
    manaAt = manaTo - gastoM
    
    vigorB = float(data['vigorB'])
    vigorE = float(data['vigorE'])
    gastoV = float(data['gastoV'])
    
    vigorTo = vigorB + vigorE
    vigorAt = vigorTo - gastoV
    
    return jsonify(vidaTo=vidaTo, vidaAt=vidaAt, 
                   manaTo=manaTo, manaAt=manaAt, 
                   vigorTo=vigorTo, vigorAt=vigorAt)

# Fim do Codigo
if __name__ == '__main__': 
    main.run(debug=True)

