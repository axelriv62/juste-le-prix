from flask import Flask, request, render_template, redirect, url_for, flash
import APIRequest
import sqlite3
from DB import ProduitDB

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        if not pseudo:
            return redirect(url_for('index'))
        return redirect(url_for('jeu', pseudo=pseudo))
    return render_template('index.html')

@app.route('/jeu', methods=['GET', 'POST'])
def jeu():
    if request.method == 'GET':
        pseudo = request.args.get('pseudo')
        theme = request.args.get('theme', '')
        if not pseudo:
            return redirect(url_for('index'))

        product_data = ProduitDB.get_produit(theme)
        conn = sqlite3.connect('DB/database.db')
        c = conn.cursor()
        try:
            c.execute("SELECT score FROM JOUEUR WHERE nom = ?", (pseudo,))
            player_data = c.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return render_template('jeu.html', pseudo=pseudo, theme=theme, error="Erreur de base de données.")
        finally:
            conn.close()

        if product_data:
            product_code, nom, image, prix = product_data
            if player_data:
                score = player_data[0]
            else:
                score = 0
            return render_template('jeu.html', pseudo=pseudo, theme=theme, score=score, image=image, nom=nom, prix=prix, code=product_code)
        else:
            return render_template('jeu.html', pseudo=pseudo, theme=theme, error="Aucun produit trouvé pour le thème sélectionné.")
    else:
        pseudo = request.form['nom']
        theme = request.form.get('theme', '')  # Ensure theme is passed in POST request
        guess = float(request.form['prix'])
        code_produit = request.form['code_produit']
        actual_prix = APIRequest.get_prix(code_produit)

        if guess < actual_prix:
            result = "C'est plus !"
        elif guess > actual_prix:
            result = "C'est moins !"
        else:
            result = "Félicitations! Vous avez trouvé le juste prix!"

        image = APIRequest.get_image(code_produit)
        nom = APIRequest.get_nom(code_produit)
        return render_template('jeu.html', pseudo=pseudo, theme=theme, image=image, nom=nom, prix=actual_prix, code=code_produit, result=result)

if __name__ == '__main__':
    app.run(debug=True)