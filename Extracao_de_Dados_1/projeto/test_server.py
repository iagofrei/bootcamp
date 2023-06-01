import flask

# Inicialização da aplicação Flask
app = flask.Flask(__name__)

# Definição da rota '/webhook' com suporte a requisições HTTP POST
@app.route('/', methods=["POST"])

def handle_webhook():

    # Recupera o conteúdo da requisição  como um dicionário de python
    data = flask.request.get_json()

    # Trata a requisição recebida: Nesse caso, apenas imprimimos os dados
    print(f'Received data: {data}.')
    
    # retornar uma resposta
    return_code = '200'
    return return_code

# Verifica se o script esta sendo executado como um módulo principal
if __name__ == '__main__':

    # inicia a aplicação
    app.run(host="localhost", port=5000, debug=True)