from flask import Flask, request, render_template, redirect, url_for, session
from DB import ProduitDB, PartieDB

app = Flask(__name__)

# Clé secrète de session (ça permet de stocker les informations de la session en cours, notamment le score du joueur)
app.secret_key = 'ekip_abcq'



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        return redirect(url_for('jeu_get', pseudo=pseudo))
    return render_template('index.html')



@app.route('/jeu', methods=['GET'])
def jeu_get():

    # Récupérer le pseudo et le thème en paramètres
    pseudo = request.args.get('pseudo')
    theme = request.args.get('theme', '')

    # Récupérer les données du produit
    code_produit, nom_produit, image, prix = ProduitDB.get_produit(theme)

    # TODO: Gérer la récupération des données du joueur une fois que le traitement des données des joueurs est implémenté
    # Récupérer les données du joueur (pas intérréssant pour le moment car on ne gère pas les données des joueurs)
    """
    conn = sqlite3.connect('DB/database.db')
    c = conn.cursor()
    try:
        c.execute("SELECT score FROM JOUEUR WHERE pseudo = ?", (pseudo,))
        player_data = c.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return render_template('jeu.html', pseudo=pseudo, theme=theme, error="Erreur de base de données.")
    finally:
        conn.close()
    
    
    # Afficher le jeu avec les données récupérées
    if player_data:
        score = player_data[0]
    else:
        score = 0
    """

    session['nb_essais'] = 0

    return render_template('jeu.html', pseudo=pseudo, theme=theme, score=0, image=image, nom=nom_produit, prix=prix, code=code_produit)



@app.route('/jeu', methods=['POST'])
def jeu_post():

    # Récupérer les données
    pseudo = request.form['pseudo']
    theme = request.form.get('theme', '')
    guess = float(request.form['prix'])
    code_produit = request.form['code_produit']
    image = request.form['image']
    nom_produit = request.form['nom']

    # Récupérer le prix du produit
    actual_prix = ProduitDB.get_prix(code_produit)

    # Récupérer le nombre d'essais restants
    nb_essais = session.get('nb_essais', 0)

    # Comparer le prix du produit avec le prix proposé par le joueur
    if guess < actual_prix:
        result = "C'est plus !"
        nb_essais += 1
    elif guess > actual_prix:
        result = "C'est moins !"
        nb_essais += 1
    else:
        result = "Félicitations! Vous avez trouvé le juste prix!"
        nb_essais += 1

        # Insérer la partie du joueur dans la base de données
        PartieDB.inserer_partie(pseudo, nb_essais, code_produit)

    # Mettre à jour le nombre d'essais restants
    session['nb_essais'] = nb_essais

    return render_template('jeu.html', pseudo=pseudo, score=nb_essais, theme=theme, image=image, nom=nom_produit, prix=actual_prix, code=code_produit, result=result)



if __name__ == '__main__':
    app.run(debug=True)