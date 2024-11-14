from flask import Flask, request, render_template
import APIRequest
from APIRequest import get_random_product

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jeu', methods=['GET'])
def jeu():
    code = get_random_product()
    image = APIRequest.get_image(code)
    nom = APIRequest.get_nom(code)
    prix = APIRequest.get_prix(code)
    return render_template('jeu.html', image=image, nom=nom, prix=prix)

@app.route('/jeu', methods=['POST'])
def jeu_post():
    nom = request.form['nom']
    score = request.form['score']
    code_produit = request.form['code_produit']
    APIRequest.insert_log(nom, score, code_produit)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)