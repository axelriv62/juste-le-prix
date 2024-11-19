import sqlite3
import requests

def creer_table():
    """
    Crée la table 'PRODUIT' dans la base de données.
    Si la table existe déjà, elle sera supprimée et recréée.
    """

    # Connexion à la base de données
    con = sqlite3.connect("database/database.db")
    cur = con.cursor()

    # Suppression de la table si elle existe
    cur.execute("DROP TABLE IF EXISTS PRODUIT")

    # Création de la table
    cur.execute("""CREATE TABLE IF NOT EXISTS PRODUIT (
        code VARCHAR(10) PRIMARY KEY,
        nom VARCHAR(255) NOT NULL,
        image VARCHAR(255) NOT NULL,
        prix FLOAT(2) NOT NULL,
        theme VARCHAR(255)
    );""")

    # Commit la création de la table
    con.commit()

    # Ferme la connexion
    con.close()

def inserer_produit(code, theme):
    """
    Insère un nouveau produit dans la table 'PRODUIT'.

    Args:
        code (str): Le code du produit qui doit être composé de 10 caractères.
        theme (str): Le thème du produit.

    Returns:
        str: Un message d'erreur si le produit existe déjà ou s'il y a un problème avec l'API.
        None: Si le produit est inséré avec succès.
    """

    if len(code) < 10:
        return "Le code du produit doit être composé de 10 caractères"

    # Connexion à la base de données
    con = sqlite3.connect("database/database.db")
    cur = con.cursor()

    # Vérifie si le produit existe déjà
    cur.execute("SELECT * FROM PRODUIT WHERE code = ?", (code,))
    produit = cur.fetchone()
    if produit:
        return "Ce produit existe déjà dans la base de données"

    # Récupère les données du produit depuis l'API
    url = "http://ws.chez-wam.info/" + code
    response = requests.get(url)

    if response.status_code == 200:
        json = response.json()

        try:
            prix = json.get("price").replace("€", "").replace(",", ".").replace(" ", "")
        except:
            return "Le produit n'existe pas ou n'a pas de prix"

        nom = json.get("title")
        image = json.get("images")[0]

        # Insère le produit dans la base de données
        cur.execute("INSERT OR IGNORE INTO PRODUIT (code, nom, image, prix, theme) VALUES (?, ?, ?, ?, ?)", (code, nom, image, prix, theme))
        con.commit()
    else:
        return "Erreur de connexion à l'API"

    # Ferme la connexion
    con.close()

    return None

def remplir_produits():
    """
    Remplit la table PRODUIT avec des produits pré-enregistrés.
    """

    # Produits Textile
    inserer_produit("B00NYZQYQM", "Textile")
    inserer_produit("B08H4BNGQ2", "Textile")
    inserer_produit("B09QBZPZCY", "Textile")
    inserer_produit("B092CXJHHK", "Textile")
    inserer_produit("B0D3QP4VJM", "Textile")
    inserer_produit("B0D4VKVTRS", "Textile")
    inserer_produit("B07581N19R", "Textile")
    inserer_produit("B00HZH71AS", "Textile")
    inserer_produit("B0DLN76F7G", "Textile")
    inserer_produit("B0DBZ12YR9", "Textile")
    inserer_produit("B0DFWFJD9K", "Textile")
    inserer_produit("B06W2LXPT5", "Textile")
    inserer_produit("B08T1QXLVJ", "Textile")
    inserer_produit("B08J7QKPL8", "Textile")


    # Produits Multimedia
    inserer_produit("B09G9HWQYT", "Multimedia")
    inserer_produit("B0CXPQKHR3", "Multimedia")
    inserer_produit("B0875VYRPB", "Multimedia")
    inserer_produit("B0CR97B5Q9", "Multimedia")
    inserer_produit("B0D6GPGZ2K", "Multimedia")
    inserer_produit("B07D7TV5J3", "Multimedia")
    inserer_produit("B0C85Z1TJ1", "Multimedia")
    inserer_produit("B01LXLFF6H", "Multimedia")
    inserer_produit("B07965NDW7", "Multimedia")
    inserer_produit("B07RK9N3WM", "Multimedia")
    inserer_produit("B098RJXBTY", "Multimedia")
    inserer_produit("B0B5PKW138", "Multimedia")

    # Produits sans thème
    inserer_produit("B07YQFZ6CJ", "")
    inserer_produit("B0C8J2Y93P", "")
    inserer_produit("B08F5834R7", "")
    inserer_produit("B0CGZYP1BS", "")
    inserer_produit("B0DKDX9PNX", "")
    inserer_produit("B09SNRM3BL", "")
    inserer_produit("B00GBYZ5BS", "")

    # inserer_produit("B08W9JJB76", "Textile") # plus de prix



def get_produit(theme):
    """
    Récupère un produit aléatoire de la table PRODUIT en fonction du thème.

    Args:
        theme (str): Le thème du produit.

    Returns:
        tuple: Un tuple contenant le code, le nom, l'image et le prix du produit.
    """

    # Connexion à la base de données
    con = sqlite3.connect("database/database.db")
    cur = con.cursor()

    # Récupère un produit aléatoire en fonction du thème
    if theme:
        cur.execute("SELECT code, nom, image, prix FROM PRODUIT WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (theme,))
    else:
        cur.execute("SELECT code, nom, image, prix FROM PRODUIT ORDER BY RANDOM() LIMIT 1")

    produit = cur.fetchone()

    # Ferme la connexion
    con.close()

    return produit

def get_prix(code):
    """
    Récupère le prix d'un produit en fonction de son code.

    Args:
        code (str): Le code du produit.

    Returns:
        float: Le prix du produit.
    """

    # Connexion à la base de données
    conn = sqlite3.connect('database/database.db')
    cur = conn.cursor()

    # Récupère le prix du produit
    cur.execute("SELECT prix FROM PRODUIT WHERE code = ?", (code,))
    prix = float(cur.fetchone()[0])

    # Ferme la connexion
    conn.close()

    return prix
