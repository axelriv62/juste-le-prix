import sqlite3

# Fonction pour créer la table
def creer_table():

    # Connexion à la base de données
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    # Suppression de la table si elle existe
    cur.execute("DROP TABLE IF EXISTS JOUEUR")

    # Création de la table
    cur.execute("""CREATE TABLE IF NOT EXISTS JOUEUR (
        pseudo VARCHAR(100) PRIMARY KEY,
        score INTEGER NOT NULL,
        code_produit VARCHAR(10) NOT NULL,
        FOREIGN KEY(code_produit) REFERENCES PRODUIT(code)
    );""")

    # Commit la création de la table
    con.commit()

    # Fermer la connexion
    con.close()



# Fonction pour insérer un nouveau joueur
def inserer_joueur(pseudo, score, code_produit):

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Insertion du joueur
    cur.execute("INSERT INTO JOUEUR VALUES (?, ?, ?)", (pseudo, score, code_produit))

    # Commit les changements
    con.commit()

    # Fermer la connexion
    con.close()



# Fonction pour récupérer les logs joueur avec son pseudo
def get_joueurs(pseudo):

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Récupération des logs du joueur
    cur.execute("SELECT * FROM JOUEUR WHERE pseudo = ?", (pseudo,))
    joueurs = cur.fetchall()

    # Fermer la connexion
    con.close()

    return joueurs



# Supprime un joueur en cas de besoin avec son pseudo et le code du produit
def delete_joueur(pseudo, code_produit):

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Suppression du joueur
    cur.execute("DELETE FROM JOUEUR WHERE pseudo = ? AND code_produit = ?", (pseudo, code_produit))

    # Commit les changements
    con.commit()

    # Fermer la connexion
    con.close()



# creer_table()
# inserer_joueur("Joueur1", 10, "B07YQFZ6CJ")