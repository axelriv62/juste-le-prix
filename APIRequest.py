import sqlite3

def get_random_product():
    conn = sqlite3.connect('DB/ma_db.db')
    c = conn.cursor()
    c.execute("SELECT produit_code FROM Produit ORDER BY RANDOM() LIMIT 1")
    code = c.fetchone()[0]
    conn.close()
    return code

def get_image(code):
    conn = sqlite3.connect('DB/ma_db.db')
    c = conn.cursor()
    c.execute("SELECT image FROM Produit WHERE produit_code = ?", (code,))
    image = c.fetchone()[0]
    conn.close()
    return image

def get_nom(code):
    conn = sqlite3.connect('DB/ma_db.db')
    c = conn.cursor()
    c.execute("SELECT nom FROM Produit WHERE produit_code = ?", (code,))
    nom = c.fetchone()[0]
    conn.close()
    return nom

def get_prix(code):
    conn = sqlite3.connect('DB/ma_db.db')
    c = conn.cursor()
    c.execute("SELECT prix FROM Produit WHERE produit_code = ?", (code,))
    prix = c.fetchone()[0]
    conn.close()
    return prix

# def insert_log(nom, score, code_produit):
#    conn = sqlite3.connect('DB/ma_db.db')
#    c = conn.cursor()
#    c.execute("INSERT INTO Player VALUES (?, ?, ?)", (nom, score, code_produit))
#    conn.commit()
#    conn.close()