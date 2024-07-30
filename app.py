from flask import Flask, render_template

app = Flask(__name__)


@app.route("/inicio")
def ola():
    lista = ["O Senhor dos Aneis","Don Casmurro","O Alquimista","Pai Pobre, Pai Rico"]
    return render_template('lista.html', titulo = "Listagem de Livros - SENAI", lista_de_livros = lista)


app.run(debug=True)