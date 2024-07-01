from flask import Flask, jsonify, render_template, request
from lib.atributos import Atributos
from lib.equipamentos import Equipamento
from lib.conjarmadura import ConjArmadura
from lib.utilitarios import somaTodosAtt

info = [] #lista de controle

main = Flask(__name__)

@main.route("/")
def home():
    return render_template('home.html')

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
    eclasse = Atributos(efor, edes, eint, edet, eper, ecar)
    elmo = Equipamento(eclasse)

    pfor = float(data['forcaP'])
    pdes = float(data['destrezaP'])
    pint = float(data['inteligenciaP'])
    pdet = float(data['determinacaoP'])
    pper = float(data['percepcaoP'])
    pcar = float(data['carismaP'])
    pclasse = Atributos(pfor, pdes, pint, pdet, pper, pcar)
    peitoral = Equipamento(pclasse)

    lfor = float(data['forcaL'])
    ldes = float(data['destrezaL'])
    lint = float(data['inteligenciaL'])
    ldet = float(data['determinacaoL'])
    lper = float(data['percepcaoL'])
    lcar = float(data['carismaL'])
    lclasse = Atributos(lfor, ldes, lint, ldet, lper, lcar)
    luva = Equipamento(lclasse)

    cfor = float(data['forcaC'])
    cdes = float(data['destrezaC'])
    cint = float(data['inteligenciaC'])
    cdet = float(data['determinacaoC'])
    cper = float(data['percepcaoC'])
    ccar = float(data['carismaC'])
    cclasse = Atributos(cfor, cdes, cint, cdet, cper, ccar)
    calca = Equipamento(cclasse)

    bfor = float(data['forcaB'])
    bdes = float(data['destrezaB'])
    bint = float(data['inteligenciaB'])
    bdet = float(data['determinacaoB'])
    bper = float(data['percepcaoB'])
    bcar = float(data['carismaB'])
    bclasse = Atributos(bfor, bdes, bint, bdet, bper, bcar)
    bota = Equipamento(bclasse)

    conja = ConjArmadura(elmo, peitoral, luva, calca, bota)
    info.extend([attbase, conja]) #retirar provavelmente quando tiver o banco de dedos
    forcaCJ = conja.somarEquip('forca') #funcao da classe para somar os atributos equipamentos
    destrezaCJ = conja.somarEquip('destreza')
    inteligenciaCJ = conja.somarEquip('inteligencia')
    determinacaoCJ = conja.somarEquip('determinacao')
    percepcaoCJ = conja.somarEquip('percepcao')
    carismaCJ = conja.somarEquip('carisma')
    forcaT = somaTodosAtt('forca', attbase, conja) #funcao para pegar a soma total de todos atributos
    destrezaT = somaTodosAtt('destreza', attbase, conja)
    inteligenciaT = somaTodosAtt('inteligencia', attbase, conja)
    determinacaoT = somaTodosAtt('determinacao', attbase, conja)
    percepcaoT = somaTodosAtt('percepcao', attbase, conja)
    carismaT = somaTodosAtt('carisma', attbase, conja)


    return jsonify(forca=forca, destreza=destreza, inteligencia=inteligencia, determinacao=determinacao, percepcao=percepcao,
                   carisma=carisma, forcaT=forcaT, destrezaT=destrezaT, inteligenciaT=inteligenciaT, determinacaoT=determinacaoT,
                   percepcaoT=percepcaoT, carismaT=carismaT, forcaCJ=forcaCJ, destrezaCJ=destrezaCJ, inteligenciaCJ=inteligenciaCJ,
                   determinacaoCJ=determinacaoCJ, percepcaoCJ=percepcaoCJ, carismaCJ=carismaCJ) # AQUI VAI JOGAR O DADO PRO FRONT

@main.route("/redvida", methods=['POST'])
def redvida():
    data = request.get_json()
    vida = float(data.get('vida'))
    mana = float(data.get('mana'))
    vigor = float(data.get('vigor'))
    vidap = float(data.get('vidaP'))
    manap = float(data.get('manaP'))
    vigorp = float(data.get('vigorP'))
    vidap -= vida
    manap -= mana
    vigorp -= vigor

    if vida >= (vidap*1.33):
        vidap = "Morreu"

    return jsonify(vidab=vidap, manab=manap, vigorb=vigorp)


# Fim do Codigo
if __name__ == '__main__': 
    main.run(debug=True)

