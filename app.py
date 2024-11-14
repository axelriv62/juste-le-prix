from flask import Flask, request, render_template, redirect, url_for
import APIRequest
import sqlite3
from APIRequest import get_random_product

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jeu', methods=['GET'])
def jeu():
    pseudo = request.args.get('pseudo')
    if not pseudo:
        return redirect(url_for('index'))

    conn = sqlite3.connect('DB/ma_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Player WHERE player_name = ?", (pseudo,))
    player_data = c.fetchone()
    conn.close()

    if player_data:
        score = player_data[1]
        product_code = player_data[2]
        image = APIRequest.get_image(product_code)
        nom = APIRequest.get_nom(product_code)
        prix = APIRequest.get_prix(product_code)
        return render_template('jeu.html', pseudo=pseudo, score=score, image=image, nom=nom, prix=prix)
    else:
        code = get_random_product()
        image = APIRequest.get_image(code)
        nom = APIRequest.get_nom(code)
        prix = APIRequest.get_prix(code)
        return render_template('jeu.html', pseudo=pseudo, image=image, nom=nom, prix=prix)

if __name__ == '__main__':
    app.run(debug=True)