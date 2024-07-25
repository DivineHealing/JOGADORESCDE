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
    forca = float(data['forca'])
    destreza =  float(data['destreza'])
    inteligencia = float(data['inteligencia'])
    determinacao = float(data['determinacao'])
    percepcao = float(data['percepcao'])
    carisma = float(data['carisma'])
    attbase = Atributos(forca, destreza, inteligencia, determinacao, percepcao, carisma)
    
    efor = float(data['forcaE'])
    edes = float(data['destrezaE'])
    eint = float(data['inteligenciaE'])
    edet = float(data['determinacaoE'])
    eper = float(data['percepcaoE'])
    ecar = float(data['carismaE'])
    eclasatt = Atributos(efor, edes, eint, edet, eper, ecar) # criando classe de atributos do elmo
    elmo = Equipamento(eclasatt) # criando objeto elmo

    pfor = float(data['forcaP'])
    pdes = float(data['destrezaP'])
    pint = float(data['inteligenciaP'])
    pdet = float(data['determinacaoP'])
    pper = float(data['percepcaoP'])
    pcar = float(data['carismaP'])
    pclasatt = Atributos(pfor, pdes, pint, pdet, pper, pcar)  # criando classe de atributos do peitoral
    peitoral = Equipamento(pclasatt) # criando objeto peitoral

    lfor = float(data['forcaL'])
    ldes = float(data['destrezaL'])
    lint = float(data['inteligenciaL'])
    ldet = float(data['determinacaoL'])
    lper = float(data['percepcaoL'])
    lcar = float(data['carismaL'])
    lclasatt = Atributos(lfor, ldes, lint, ldet, lper, lcar)  # criando classe de atributos da luva
    luva = Equipamento(lclasatt) # criando objeto luva

    cfor = float(data['forcaC'])
    cdes = float(data['destrezaC'])
    cint = float(data['inteligenciaC'])
    cdet = float(data['determinacaoC'])
    cper = float(data['percepcaoC'])
    ccar = float(data['carismaC'])
    cclasatt = Atributos(cfor, cdes, cint, cdet, cper, ccar)  # criando classe de atributos da calca
    calca = Equipamento(cclasatt)  # criando objeto calca

    bfor = float(data['forcaB'])
    bdes = float(data['destrezaB'])
    bint = float(data['inteligenciaB'])
    bdet = float(data['determinacaoB'])
    bper = float(data['percepcaoB'])
    bcar = float(data['carismaB'])
    bclasatt = Atributos(bfor, bdes, bint, bdet, bper, bcar)  # criando classe de atributos da bota
    bota = Equipamento(bclasatt)  # criando objeto bota

    conja = ConjArmadura(elmo, peitoral, luva, calca, bota)  # criando objeto de conjunto de armadura
    
    anfor1 = float(data['forcaAn1'])
    andes1 = float(data['destrezaAn1'])
    anint1 = float(data['inteligenciaAn1'])
    andet1 = float(data['determinacaoAn1'])
    anper1 = float(data['percepcaoAn1'])
    ancar1 = float(data['carismaAn1'])
    anclasatt1 = Atributos(anfor1, andes1, anint1, andet1, anper1, ancar1) # criando classe de atributos do anel 1
    anel1 = Acessorio(anclasatt1)  # criando o objeto anel1

    anfor2 = float(data['forcaAn2'])
    andes2 = float(data['destrezaAn2'])
    anint2 = float(data['inteligenciaAn2'])
    andet2 = float(data['determinacaoAn2'])
    anper2 = float(data['percepcaoAn2'])
    ancar2 = float(data['carismaAn2'])
    anclasatt2 = Atributos(anfor2, andes2, anint2, andet2, anper2, ancar2) # criando classe de atributos do anel 2
    anel2 = Acessorio(anclasatt2)  # criando o objeto anel2

    anfor3 = float(data['forcaAn3'])
    andes3 = float(data['destrezaAn3'])
    anint3 = float(data['inteligenciaAn3'])
    andet3 = float(data['determinacaoAn3'])
    anper3 = float(data['percepcaoAn3'])
    ancar3 = float(data['carismaAn3'])
    anclasatt3 = Atributos(anfor3, andes3, anint3, andet3, anper3, ancar3) # criando classe de atributos do anel 3
    anel3 = Acessorio(anclasatt3)  # criando o objeto anel3

    anfor4 = float(data['forcaAn4'])
    andes4 = float(data['destrezaAn4'])
    anint4 = float(data['inteligenciaAn4'])
    andet4 = float(data['determinacaoAn4'])
    anper4 = float(data['percepcaoAn4'])
    ancar4 = float(data['carismaAn4'])
    anclasatt4 = Atributos(anfor4, andes4, anint4, andet4, anper4, ancar4) # criando classe de atributos do anel 4
    anel4 = Acessorio(anclasatt4)  # criando o objeto anel4

    bcfor1 = float(data['forcaBc1'])
    bcdes1 = float(data['destrezaBc1'])
    bcint1 = float(data['inteligenciaBc1'])
    bcdet1 = float(data['determinacaoBc1'])
    bcper1 = float(data['percepcaoBc1'])
    bccar1 = float(data['carismaBc1'])
    bcclasatt1 = Atributos(bcfor1, bcdes1, bcint1, bcdet1, bcper1, bccar1) # criando classe de atributos do bracelete 1
    brac1 = Acessorio(bcclasatt1)  # criando o objeto bracelete1

    bcfor2 = float(data['forcaBc2'])
    bcdes2 = float(data['destrezaBc2'])
    bcint2 = float(data['inteligenciaBc2'])
    bcdet2 = float(data['determinacaoBc2'])
    bcper2 = float(data['percepcaoBc2'])
    bccar2 = float(data['carismaBc2'])
    bcclasatt2 = Atributos(bcfor2, bcdes2, bcint2, bcdet2, bcper2, bccar2) # criando classe de atributos do bracelete 2
    brac2 = Acessorio(bcclasatt2)  # criando o objeto bracelete2

    brfor1 = float(data['forcaBr1'])
    brdes1 = float(data['destrezaBr1'])
    brint1 = float(data['inteligenciaBr1'])
    brdet1 = float(data['determinacaoBr1'])
    brper1 = float(data['percepcaoBr1'])
    brcar1 = float(data['carismaBr1'])
    brclasatt1 = Atributos(brfor1, brdes1, brint1, brdet1, brper1, brcar1) # criando classe de atributos do brinco 1
    brinc1 = Acessorio(brclasatt1)  # criando o objeto brinco 1

    brfor2 = float(data['forcaBr2'])
    brdes2 = float(data['destrezaBr2'])
    brint2 = float(data['inteligenciaBr2'])
    brdet2 = float(data['determinacaoBr2'])
    brper2 = float(data['percepcaoBr2'])
    brcar2 = float(data['carismaBr2'])
    brclasatt2 = Atributos(brfor2, brdes2, brint2, brdet2, brper2, brcar2) # criando classe de atributos do brinco 2
    brinc2 = Acessorio(brclasatt2)  # criando o objeto brinco 2

    cofor = float(data['forcaCo'])
    codes = float(data['destrezaCo'])
    coint = float(data['inteligenciaCo'])
    codet = float(data['determinacaoCo'])
    coper = float(data['percepcaoCo'])
    cocar = float(data['carismaCo'])
    coclasatt = Atributos(cofor, codes, coint, codet, coper, cocar) # criando classe de atributos do colar
    colar = Acessorio(coclasatt)  # criando o objeto colar  

    cafor = float(data['forcaCa'])
    cades = float(data['destrezaCa'])
    caint = float(data['inteligenciaCa'])
    cadet = float(data['determinacaoCa'])
    caper = float(data['percepcaoCa'])
    cacar = float(data['carismaCa'])
    caclasatt = Atributos(cafor, cades, caint, cadet, caper, cacar) # criando classe de atributos do colar
    capa = Acessorio(caclasatt)  # criando o objeto colar  

    cifor = float(data['forcaCi'])
    cides = float(data['destrezaCi'])
    ciint = float(data['inteligenciaCi'])
    cidet = float(data['determinacaoCi'])
    ciper = float(data['percepcaoCi'])
    cicar = float(data['carismaCi'])
    ciclasatt = Atributos(cifor, cides, ciint, cidet, ciper, cicar)  # criando classe de atributos do colar
    cinto = Acessorio(ciclasatt)  # criando o objeto colar  
    
    conjac = ConjAcessorio(anel1, anel2, anel3, anel4, brac1, brac2, brinc1, brinc2, colar, capa, cinto)

    apfor = float(data['forcaAp'])
    apdes = float(data['destrezaAp'])
    apint = float(data['inteligenciaAp'])
    apdet = float(data['determinacaoAp'])
    apper = float(data['percepcaoAp'])
    apcar = float(data['carismaAp'])
    #testepen = Elementos(12)
    apclassatt = Atributos(apfor, apdes, apint, apdet, apper, apcar)  # criando o objeto dos atributos da arma principal
    armaprincipal = Arma(apclassatt)  # criando o objeto da arma principal
    #armaprincipal = Arma(apclassatt, pen=testepen)  # para testar

    asfor = float(data['forcaAs'])
    asdes = float(data['destrezaAs'])
    asint = float(data['inteligenciaAs'])
    asdet = float(data['determinacaoAs'])
    asper = float(data['percepcaoAs'])
    ascar = float(data['carismaAs'])
    asclassatt = Atributos(asfor, asdes, asint, asdet, asper, ascar)  # criando o objeto dos atributos da arma secundaria
    armasecundaria = Arma(asclassatt, False)  # criando o objeto arma secundaria
    #armasecundaria = Arma(asclassatt, False, testepen)
    armasequip = ArmasEmMaos(armaprincipal, armasecundaria) #criando objeto das armas em mãos 
    #print(armasequip.somarEspe('pen', 'tipo1')) # para testes

    mprfor = float(data['forcaMPR'])
    mprdes = float(data['destrezaMPR'])
    mprint = float(data['inteligenciaMPR'])
    mprdet = float(data['determinacaoMPR'])
    mprper = float(data['percepcaoMPR'])
    mprcar = float(data['carismaMPR'])
    mprclassatt = Atributos(mprfor, mprdes, mprint, mprdet, mprper, mprcar)  # criando o objeto dos atributos das recompensa maestrias principal
    
    mpbfor = float(data['forcaMPB'])
    mpbdes = float(data['destrezaMPB'])
    mpbint = float(data['inteligenciaMPB'])
    mpbdet = float(data['determinacaoMPB'])
    mpbper = float(data['percepcaoMPB'])
    mpbcar = float(data['carismaMPB'])
    mpbclassatt = Atributos(mpbfor, mpbdes, mpbint, mpbdet, mpbper, mpbcar)  # criando o objeto dos atributos dos bonus de maestria principal
    maesp = Maestrias(mprclassatt, mpbclassatt)  # criando objeto da maestrias principal

    msrfor = float(data['forcaMSR'])
    msrdes = float(data['destrezaMSR'])
    msrint = float(data['inteligenciaMSR'])
    msrdet = float(data['determinacaoMSR'])
    msrper = float(data['percepcaoMSR'])
    msrcar = float(data['carismaMSR'])
    msrclassatt = Atributos(msrfor, msrdes, msrint, msrdet, msrper, msrcar)  # criando o objeto dos atributos das recompensa maestrias secundaria
    
    msbfor = float(data['forcaMSB'])
    msbdes = float(data['destrezaMSB'])
    msbint = float(data['inteligenciaMSB'])
    msbdet = float(data['determinacaoMSB'])
    msbper = float(data['percepcaoMSB'])
    msbcar = float(data['carismaMSB'])
    msbclassatt = Atributos(msbfor, msbdes, msbint, msbdet, msbper, msbcar)  # criando o objeto dos atributos dos bonus de maestria secundaria
    maess = Maestrias(msrclassatt, msbclassatt)  # criando objeto da maestrias Secundaria

    murfor = float(data['forcaMUR'])
    murdes = float(data['destrezaMUR'])
    murint = float(data['inteligenciaMUR'])
    murdet = float(data['determinacaoMUR'])
    murper = float(data['percepcaoMUR'])
    murcar = float(data['carismaMUR'])
    murclassatt = Atributos(murfor, murdes, murint, murdet, murper, murcar)  # criando o objeto dos atributos das recompensa maestrias principal
    
    mubfor = float(data['forcaMUB'])
    mubdes = float(data['destrezaMUB'])
    mubint = float(data['inteligenciaMUB'])
    mubdet = float(data['determinacaoMUB'])
    mubper = float(data['percepcaoMUB'])
    mubcar = float(data['carismaMUB'])
    mubclassatt = Atributos(mubfor, mubdes, mubint, mubdet, mubper, mubcar)  # criando o objeto dos atributos dos bonus de maestria utilitaria
    maesu = Maestrias(murclassatt, mubclassatt)  # criando objeto da maestrias utilitaria
    conjmaes = Conjmaestria(maesp, maess, maesu)  # criando o objeto do conjunto de maestrias

    msfor = float(data['forcaMS'])
    msdes = float(data['destrezaMS'])
    msint = float(data['inteligenciaMS'])
    msdet = float(data['determinacaoMS'])
    msper = float(data['percepcaoMS'])
    mscar = float(data['carismaMS'])
    msclassatt = Atributos(msfor, msdes, msint, msdet, msper, mscar)  # criando o objeto dos atributos das missões
    mis = Missoes(msclassatt)  # criando objeto das missões

    bdclassatt = Atributos(float(data['forcaBD']), float(data['destrezaBD']), float(data['inteligenciaBD']), float(data['determinacaoBD']), float(data['percepcaoBD']),
                            float(data['carismaBD']))  # Criando atributos da Benção Divina (apenas percentual)
    bd = BencaoDiv(bdclassatt)  # criando o objeto das Bençãos divinas

    clafclassatt = Atributos(float(data['forcaDCF']), float(data['destrezaDCF']), float(data['inteligenciaDCF']), float(data['determinacaoDCF']), float(data['percepcaoDCF']),
                            float(data['carismaDCF']))  # Criando atributos da dadiva do clã fixo
    clapclassatt = Atributos(float(data['forcaDCP']), float(data['destrezaDCP']), float(data['inteligenciaDCP']), float(data['determinacaoDCP']), float(data['percepcaoDCP']),
                            float(data['carismaDCP']))  # Criando atributos da dadiva do clã percentual
    cla = Cla(clafclassatt, clapclassatt)  # criando o objeto da dadiva doc clã

    grimclassatt = Atributos(float(data['forcaG']), float(data['destrezaG']), float(data['inteligenciaG']), float(data['determinacaoG']), float(data['percepcaoG']),
                            float(data['carismaG']))  # Criando atributos do grimorio (apenas percentual)
    grim = Grimorio(grimclassatt)  # criando o objeto do grimorio

    racaclassatt = Atributos(float(data['forcaraca']), float(data['destrezaraca']), float(data['inteligenciaraca']), float(data['determinacaoraca']), float(data['percepcaoraca']),
                            float(data['carismaraca']))  # Criando atributos da Raça (apenas percentual)
    raca = Raca(racaclassatt)  # criando o objeto da raça

    bfefclassatt = Atributos(float(data['forcaBF']), float(data['destrezaBF']), float(data['inteligenciaBF']), float(data['determinacaoBF']), float(data['percepcaoBF']),
                            float(data['carismaBF']))  # Criando atributos do bonus percentual fixo
    bfepclassatt = Atributos(float(data['forcaBP']), float(data['destrezaBP']), float(data['inteligenciaBP']), float(data['determinacaoBP']), float(data['percepcaoBP']),
                            float(data['carismaBP']))  # Criando atributos do bonus externo percentual
    be = BonusEx(bfefclassatt, bfepclassatt)  # criando o objeto dos bonus externos

    hfclassatt = Atributos(float(data['forcaHF']), float(data['destrezaHF']), float(data['inteligenciaHF']), float(data['determinacaoHF']), float(data['percepcaoHF']),
                            float(data['carismaHF']))  # Criando atributos da habilidade fixo
    hpclassatt = Atributos(float(data['forcaHP']), float(data['destrezaHP']), float(data['inteligenciaHP']), float(data['determinacaoHP']), float(data['percepcaoHP']),
                            float(data['carismaHP']))  # Criando atributos do habilidade percentual
    habilidadesp = Habilidade(hfclassatt, hpclassatt)  # criando o objeto das habilidades

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

    forcat = forca + conjmaes.somarMaes('f','forca') + mis.att.forca #ira somar todos os atributos base
    destrezat = destreza + conjmaes.somarMaes('f', 'destreza') + mis.att.destreza
    inteligenciat = inteligencia + conjmaes.somarMaes('f', 'inteligencia') + mis.att.inteligencia
    determinacaot = determinacao + conjmaes.somarMaes('f', 'determinacao') + mis.att.determinacao
    percepcaot = percepcao + conjmaes.somarMaes('f', 'percepcao') + mis.att.percepcao
    carismat = carisma + conjmaes.somarMaes('f', 'carisma') + mis.att.carisma

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

