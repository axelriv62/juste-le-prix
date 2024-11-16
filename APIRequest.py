import sqlite3

def get_random_product(theme):
    conn = sqlite3.connect('DB/database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT code FROM PRODUIT WHERE theme = ? ORDER BY RANDOM() LIMIT 1", (theme,))
    code = c.fetchone()[0]
    conn.close()
    return code

def get_image(code):
    conn = sqlite3.connect('DB/database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT image FROM PRODUIT WHERE code = ?", (code,))
    image = c.fetchone()[0]
    conn.close()
    return image

def get_nom(code):
    conn = sqlite3.connect('DB/database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT nom FROM PRODUIT WHERE code = ?", (code,))
    nom = c.fetchone()[0]
    conn.close()
    return nom

def get_prix(code):
    conn = sqlite3.connect('DB/database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT prix FROM PRODUIT WHERE code = ?", (code,))
    prix = float(c.fetchone()[0])
    conn.close()
    return prix