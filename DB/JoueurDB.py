import sqlite3


# Insere un joueur avec toutes les infos
def inserer_joueur(nom, score, code_produit):
    conn = sqlite3.connect('ma_db.db')
    c = conn.cursor()
    c.execute("INSERT INTO Player VALUES (?, ?, ?)", (nom, score, code_produit))
    conn.commit()
    conn.close()


# Retourne le joueur en fonction de son nom
def get_joueurs(nom):
    conn = sqlite3.connect('ma_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Player WHERE player_name = ?", (nom,))
    joueurs = c.fetchall()
    conn.close()
    return joueurs


# Supprime un joueur en cas de besoin avec son nom et le code du produit
def delete_player(nom, code_produit):
    conn = sqlite3.connect('ma_db.db')
    c = conn.cursor()
    c.execute("DELETE FROM Player WHERE player_name = ? AND product_code = ?", (nom, code_produit))
    conn.commit()
    conn.close()


# Connexion à la db
conn = sqlite3.connect('ma_db.db')
c = conn.cursor()

# Suppression de la table Player si elle existe !TEST UNIQUEMENT!
#Drop if exist
#c.execute('''
#   DROP TABLE IF EXISTS Player
#''')


# Create table Player
c.execute('''
    CREATE TABLE Player (
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        product_code TEXT NOT NULL,
        FOREIGN KEY(product_code) REFERENCES Product(product_code)
    )
''')
#inserer_joueur('Joueur1', 100, 'PADS1')
#inserer_joueur('Joueur2', 200, 'P2HSG')
#inserer_joueur('Joueur3', 300, 'PCDF3')
#print(get_joueurs('Joueur1'))
#delete_player('Joueur1', 'PADS1')
#print(get_joueurs('Joueur1'))
# Insertion de données !TEST UNIQUEMENT!
# c.execute("INSERT INTO Player VALUES ('Joueur1', 100, 'PADS1')")
# c.execute("INSERT INTO Player VALUES ('Joueur2', 200, 'P2HSG')")
# c.execute("INSERT INTO Player VALUES ('Joueur3', 300, 'PCDF3')")
# c.execute("SELECT * FROM Player")
# print(c.fetchall())

# Commit les changements et fermer la connexion
conn.commit()
conn.close()

