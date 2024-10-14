import sqlite3


# Connexion à la db
conn = sqlite3.connect('ma_db.db')
c = conn.cursor()

# Suppression de la table Player si elle existe !TEST UNIQUEMENT!
# Drop is exist
# c.execute('''
#   DROP TABLE IF EXISTS Player
# ''')


# Create table Player
c.execute('''
    CREATE TABLE Player (
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        product_code TEXT NOT NULL,
        FOREIGN KEY(product_code) REFERENCES Product(product_code)
    )
''')

# Insertion de données !TEST UNIQUEMENT!
# c.execute("INSERT INTO Player VALUES ('Joueur1', 100, 'PADS1')")
# c.execute("INSERT INTO Player VALUES ('Joueur2', 200, 'P2HSG')")
# c.execute("INSERT INTO Player VALUES ('Joueur3', 300, 'PCDF3')")
# c.execute("SELECT * FROM Player")
# print(c.fetchall())

# Commit les changements et fermer la connexion
conn.commit()
conn.close()