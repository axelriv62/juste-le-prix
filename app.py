from flask import Flask, request, render_template
import APIRequest

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jeu', methods=['GET'])
def jeu():
    code = "B07YQFZ6CJ"
    image = APIRequest.get_image(code)
    nom = APIRequest.get_nom(code)
    prix = APIRequest.get_prix(code)
    return render_template('jeu.html', image=image, nom=nom, prix=prix)

if __name__ == '__main__':
    app.run(debug=True)