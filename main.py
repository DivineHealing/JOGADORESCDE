from flask import Flask, jsonify, render_template, request

main = Flask(__name__)

@main.route("/")
def home():
    return render_template('home.html')

# CODIGO AQUI

#teste

# NAO PASSAR DAQUI

if __name__ == '__main__':
    main.run(debug=True)

