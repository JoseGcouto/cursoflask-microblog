from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "José Augusto"
    dados = {'profissao':'Desenvolvedor','canal':'BugaDev'}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contatos')
def contatos():
    contatos = {'email':'teste.bugacodar@outlook.com','github':'jose.bugapd@gmial.com','linkedin':'contato.Josegcouto@gmail.com'}
    return render_template('contatos.html', contatos=contatos)

