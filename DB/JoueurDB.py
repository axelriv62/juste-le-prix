import sqlite3


# Connexion à la db
conn = sqlite3.connect('ma_db.db')
c = conn.cursor()

# Create table Player
c.execute('''
    CREATE TABLE Player (
        player_name TEXT NOT NULL,
        score INTEGER NOT NULL,
        product_code TEXT NOT NULL,
        FOREIGN KEY(product_code) REFERENCES Product(product_code)
    )
''')

# Commit les changements et fermer la connexion
conn.commit()
conn.close()