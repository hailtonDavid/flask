from app import app
from flask import render_template, url_for


@app.route("/")
def index():
    nome = "João"
    idade = 30
    interesses = ["Python", "Flask", "Desenvolvimento Web"]
    return render_template("index.html", nome=nome, idade=idade, interesses=interesses)


@app.route("/nova")
def novapagina():
    return "Sobre nós"
