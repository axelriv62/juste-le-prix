import sqlite3

import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
con=sqlite3.connect("data.db")
cur=con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS PRODUIT
(
    produit_code varchar(50) PRIMARY KEY,
    nom varchar(50),
    image varchar(200),
    prix double
);
    """)

def inserer(str):
    url = "http://ws.chez-wam.info/"+str
    response = requests.get(url)
    json = response.json()
    product_code=str
    nom=json["title"]
    prix=json["price"].replace("€", "").replace(",", ".").strip()
    image=json["images"][0]
    sql = "INSERT INTO PRODUIT (produit_code, nom, image, prix) VALUES (?, ?, ?, ?)"
    val = (product_code, nom, image, prix)
    cur.execute(sql, val)
    con.commit()

inserer("B07YQFZ6CJ")
inserer("B0C8J2Y93P")
inserer("B08F5834R7")
res=cur.execute("SELECT * FROM PRODUIT")
print(res.fetchall())


con.close()