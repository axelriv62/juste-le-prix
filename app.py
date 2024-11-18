from flask import Flask, request, render_template, redirect, url_for, session
from DB import ProduitDB, PartieDB
import random
app = Flask(__name__)
app.secret_key = 'ekip_abcq'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        return redirect(url_for('jeu_get', pseudo=pseudo))
    return render_template('index.html')



@app.route('/jeu', methods=['GET'])
def jeu_get():
    # Récupérer le pseudo et le thème
    pseudo = request.args.get('pseudo')
    theme = request.args.get('theme', '')

    # Initialiser le score du joueur
    session['score'] = 0

    # Récupérer les données du produit
    code_produit, nom_produit, image, prix = ProduitDB.get_produit(theme)

    # Renvoyer le template avec un correct_guess explicite
    return render_template(
        'jeu.html',
        pseudo=pseudo,
        theme=theme,
        score=session['score'],
        image=image,
        nom=nom_produit,
        code=code_produit,
        result_image=None,
        correct_guess=False  # Initialisation explicite
    )


@app.route('/jeu', methods=['POST'])
def jeu_post():
    # Débogage des données reçues
    print("Form data:", request.form)

    # Récupérer les données
    pseudo = request.form['pseudo']
    theme = request.form.get('theme', '')
    guess = float(request.form['prix'])
    code_produit = request.form['code_produit']
    image = request.form['image']
    nom_produit = request.form['nom']

    # Obtenir le prix réel
    actual_prix = ProduitDB.get_prix(code_produit)

    # Déterminer le résultat
    if guess < actual_prix:
        result_image = "plus.png"
        correct_guess = False
    elif guess > actual_prix:
        result_image = "moins.png"
        correct_guess = False
    else:
        result_image = "correct.png"
        correct_guess = True

    return render_template(
        'jeu.html',
        pseudo=pseudo,
        score=session['score'],
        theme=theme,
        image=image,
        nom=nom_produit,
        code=code_produit,
        result_image=result_image,
        correct_guess=correct_guess
    )




@app.route('/insertion', methods=['GET'])
def insertion_get():
    return render_template('insertion.html')

@app.route('/insertion', methods=['POST'])
def insertion_post():
    code = request.form['code']
    theme = request.form['theme']

    try:
        error = ProduitDB.inserer_produit(code, theme)
        if error:
            return render_template('insertion.html', error=error)
    except Exception as e:
        return render_template('insertion.html', error=f"Erreur lors de l'insertion du produit: {str(e)}")

    return redirect(url_for('insertion_get'))


if __name__ == '__main__':
    app.run(debug=True)