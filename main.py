from flask import Flask, jsonify, render_template, request
from lib.atributos import atributos

info = [] #lista de controle

main = Flask(__name__)

@main.route("/")
def home():
    return render_template('home.html')

# CODIGO AQUI
@main.route("/atrstatus", methods=['POST'])
def atrstatus():
    data = request.get_json() # AQUI PEGA O DADO
    forca = float(data.get('forca'))
    destreza =  float(data.get('destreza'))
    inteligencia = float(data.get('inteligencia'))
    determinacao = float(data['determinacao'])
    percepcao = float(data['percepcao'])
    carisma = float(data['carisma'])
    criadojack = atributos(forca, destreza, inteligencia, determinacao, percepcao, carisma)
    info.append(criadojack) #retirar provavelmente quando tiver o banco de dedos
    print(criadojack.forca)

    forcae = float(data.get('forcaE')) # Pega o valor do equipamento
    forca += forcae # Soma o valor base com o Equipamento

    return jsonify(forca=forca, destreza=destreza, inteligencia=inteligencia, determinacao=determinacao, percepcao=percepcao,
                   carisma=carisma) # AQUI VAI JOGAR O DADO PRO FRONT

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

