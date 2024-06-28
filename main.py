from flask import Flask, jsonify, render_template, request

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

    forcae = float(data.get('forcaE')) # Pega o valor do equipamento
    forca += forcae # Soma o valor base com o Equipamento

    return jsonify(forca=forca, destreza=destreza, inteligencia=inteligencia) # AQUI VAI JOGAR O DADO PRO FRONT

# Fim do Codigo
if __name__ == '__main__': 
    main.run(debug=True)

