from flask import Flask, jsonify, render_template, request

main = Flask(__name__)

@main.route("/")
def home():
    return render_template('home.html')

# CODIGO AQUI
@main.route("/atrstatus", methods=['POST']) #LOCALIZA DE ONDE TA VINDO
def atrstatus(javareet, att):
    data = request.get_json() # AQUI PEGA O DADO
    atributoescolhido = float(data.get(att)) #DADO

    return jsonify(javaret=atributoescolhido) # AQUI VAI JOGAR O DADO PRO FRONT

# PERA QUE FUDEU, TODOS EQUIPAMENTOS QUE DAO FORÇA, VAO TER QUE ESTAR AQUI, E VAI TER UM PRA CADA DESSE

if __name__ == '__main__': 
    main.run(debug=True)

