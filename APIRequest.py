import sqlite3

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
