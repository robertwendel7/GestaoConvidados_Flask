from flask import *

#inicialização do flask (instanciar o servidor flask)
app = Flask(__name__)

#criando a lista de convidados
convidados = ["Ka", "Robert","Eduardo" ,"Hugo" ,"Hyago"]

#criar uma função atrelada a rota (a ser quando a rota receber uma requisição)
#a função sempre precisa retonar algo (String, pagina html, etc)
@app.route("/", methods=['GET', 'POST', 'PUT'])
def principal():
    titulo_pagina = "Gestão de convidados"
    
    return render_template("principal.html", titulo = titulo_pagina, lista_convidados = convidados)

#criar uma rota para verificar se o usuário está na lista
@app.route("/verificacao", methods=['POST'])
def verificar():
    nome = request.form.get("nomeUsuario")
    if(nome in convidados):
        mensagem = "Você está na lista"
        return render_template("resultado.html", mensagem = mensagem)
    else:
        mensagem = "Você não está na lista"
        return render_template("resultado.html", mensagem = mensagem)

    return render_template("resultado.html", titulo = titulo_pagina)

#execução do servidor (chamar a função responsavel por executar o servidor web)
#colocar no modo servidor (recarregar o srvidor web automaticamente)
app.run(debug= True)