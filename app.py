from flask import Flask, request, render_template, redirect, url_for, session
from DB import ProduitDB, PartieDB

app = Flask(__name__)

"""
Clé secrète pour gérer la session de l'utilisateur
Cela permet dans notre cas de stocker le score du joueur entre jeu_get et jeu_post
"""
app.secret_key = 'ekip_abcq'


@app.route('/', methods=['GET','POST'])
def index():
    """
    Route pour la page d'accueil avec les requêtes GET et POST.
    Si la méthode de la requête est POST, redirige vers la route 'jeu_get' avec le pseudo.
    Sinon, rend le template index.html.

    :return: Le template rendu ou une réponse de redirection
    """
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        return redirect(url_for('jeu_get', pseudo=pseudo))
    return render_template('index.html')


@app.route('/jeu', methods=['GET'])
def jeu_get():
    """
    Route pour la page de jeu (requête GET).
    Initialise le score du joueur et récupère les données du produit en fonction du thème.
    Rend le template jeu.html avec les données récupérées.

    :return: Le template rendu avec les données du jeu
    """
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
    """
    Route pour la page de jeu avec la requête POST.
    Gère le guess du joueur et détermine si il est correcte.
    Rend la template jeu.html avec le résultat de la supposition.

    :return: La template rendu avec le résultat de la supposition
    """

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
        session['score'] += 1
        result_image = "plus.png"
        correct_guess = False
    elif guess > actual_prix:
        result_image = "moins.png"
        session['score'] += 1
        correct_guess = False
    else:
        result_image = "correct.png"
        session['score'] += 1
        correct_guess = True

        # Insérer la partie dans la base de données
        PartieDB.inserer_partie(pseudo, session['score'], code_produit)

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
    """
    Route pour la page d'insertion de produit avec la requête GET.
    Rend la template insertion.html.

    :return: La template rendu pour l'insertion de produit
    """
    return render_template('insertion.html')


@app.route('/insertion', methods=['POST'])
def insertion_post():
    """
    Route pour la page d'insertion de produit avec la requête POST).
    Gère l'insertion d'un nouveau produit dans la base de données.
    En cas d'erreur, rend le template insertion.html avec le message d'erreur.
    Sinon, redirige vers la route 'insertion_get'.

    :return: La template rendu avec un message d'erreur ou une réponse de redirection
    """
    code = request.form['code']
    theme = request.form['theme']

    try:
        error = ProduitDB.inserer_produit(code, theme)
        if error:
            return render_template('insertion.html', error=error)
    except Exception as e:
        return render_template('insertion.html', error=f"Erreur lors de l'insertion du produit: {str(e)}")

    return redirect(url_for('insertion_get'))


@app.route('/scores', methods=['GET'])
def afficher_scores():
    """
    Route pour la page des scores avec la requête GET.
    Récupère les scores des parties et les affiche.

    :return: La template scores.html avec les scores récupérés.
    """
    try:
        scores = PartieDB.get_scores()
        scores_enum = list(enumerate(scores, start=1))
    except Exception as e:
        scores_enum = []
        print(f"Erreur lors de la récupération des scores: {e}")

    return render_template('scores.html', scores_enum=scores_enum)


if __name__ == '__main__':
    """
    Point d'entrée principal de l'application.
    Exécute l'application Flask en mode débogage.
    """
    app.run(debug=True)
