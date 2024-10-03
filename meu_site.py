# This is a sample Python script.

from flask import Flask, render_template



#router: qual caminho da pagina a ser exibida
#funcao : o que voce quer  exibir naquela pagina
app = Flask (__name__)

@app.route ("/") #@"nome do site",route:define o link da pagina.que tem ba funcao def.


def homepage():

    return render_template("homepage.html") #render_template carrega a pagina em html
    #retorna um valor como resposta

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")#retorna o nome do usuario que eu quero
def usuarios (nome_usuario):
    return render_template ("usuarios.html", nome_usuario=nome_usuario)
#o primeiro nome_usuario é o que se refre a pagina usuarios.html o segundo é o da função









if __name__ == "__main__":
    app.run(debug=True)
    #app.run = coloca o site no ar