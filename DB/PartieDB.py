import sqlite3

# Fonction pour créer la table
def creer_table():
    """
    Crée la table 'PARTIE' dans la base de données.
    Si la table existe déjà, elle sera supprimée et recréée.

    :return: None
    """

    # Connexion à la base de données
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    # Suppression de la table si elle existe
    cur.execute("DROP TABLE IF EXISTS PARTIE")

    # Création de la table
    cur.execute("""CREATE TABLE IF NOT EXISTS PARTIE (
        id_partie INTEGER PRIMARY KEY AUTOINCREMENT,
        pseudo VARCHAR(100),
        score INTEGER NOT NULL,
        code_produit VARCHAR(10) NOT NULL,
        FOREIGN KEY(code_produit) REFERENCES PRODUIT(code)
    );""")

    # Commit la création de la table
    con.commit()

    # Fermer la connexion
    con.close()



# Fonction pour insérer une nouvelle partie
def inserer_partie(pseudo, score, code_produit):
    """
    Insère une nouvelle partie dans la table 'PARTIE'.

    :param pseudo: Le pseudo du joueur
    :type pseudo: str
    :param score: Le score du joueur
    :type score: int
    :param code_produit: Le code du produit associé
    :type code_produit: str
    :return: None
    """

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Insertion de la partie
    cur.execute("INSERT INTO PARTIE (pseudo, score, code_produit) VALUES (?, ?, ?)", (pseudo, score, code_produit))

    # Commit les changements
    con.commit()

    # Fermer la connexion
    con.close()



# Fonction pour récupérer les logs joueur avec son pseudo
def get_joueurs(pseudo):
    """
    Récupère les logs des parties d'un joueur donné par son pseudo.

    :param pseudo: Le pseudo du joueur
    :type pseudo: str
    :return: Une liste de tuples contenant les informations des parties du joueur
    :rtype: list
    """

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Récupération des logs du joueur
    cur.execute("SELECT * FROM PARTIE WHERE pseudo = ?", (pseudo,))
    joueurs = cur.fetchall()

    # Fermer la connexion
    con.close()

    return joueurs



# Supprime un joueur en cas de besoin avec son pseudo et le code du produit
def delete_joueur(pseudo, code_produit):
    """
    Supprime un joueur de la table 'PARTIE' en fonction de son pseudo et du code produit.

    :param pseudo: Le pseudo du joueur
    :type pseudo: str
    :param code_produit: Le code du produit associé
    :type code_produit: str
    :return: None
    """

    # Connexion à la base de données
    con = sqlite3.connect('DB/database.db')
    cur = con.cursor()

    # Suppression du joueur
    cur.execute("DELETE FROM PARTIE WHERE pseudo = ? AND code_produit = ?", (pseudo, code_produit))

    # Commit les changements
    con.commit()

    # Fermer la connexion
    con.close()



# creer_table()