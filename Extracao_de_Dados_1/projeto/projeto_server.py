import flask
import json
import os
import jsonschema
from flask import Flask, make_response
from datetime import datetime


# Inicialização da aplicação Flask
app = flask.Flask(__name__)



def valida_dados(data):

    """A função recebe um json como valor, e valida se os atributos estão corretos

    Args:
        "instruction_id": int
        "entity_name": str
        "entity_id": int
        "timestamp": str('%Y-%m-%d %H:%M:%S')

    Returns:
        erro: True or False, caso não seja valido retorna True
    """    
     
    print(f'Received data: {data}.')

    msg = {}
    erro = False

    keys = ["instruction_id","entity_name","entity_id","timestamp"]
    received_keys = data.keys()
    print(f'Chaves recebidas: {received_keys}')
     
    i = 0
    for key in keys:
        if key not in received_keys:
            print(f"Chave inexistente: {key}")
            msg[i] = f"Chave inexistente: {key}"
            erro = True
            i = i + 1
            data.update(msg)
    if erro:
        return erro

    if type(data['instruction_id']) != int:
        print(f"Campo 'instruction_id' com datatype inconsistente: Correto=int / Recebido={type(data['instruction_id'])}")
        msg['error_instruction_id'] = f"Campo 'instruction_id' com datatype inconsistente: Correto=int / Recebido={type(data['instruction_id'])}"
        data.update(msg)
        erro = True
     
    if type(data['entity_name']) != str:
        print(f"Campo 'entity_name' com datatype inconsistente: Correto=int / Recebido={type(data['entity_name'])}")
        msg['error_entity_name'] = f"Campo 'entity_name' com datatype inconsistente: Correto=int / Recebido={type(data['entity_name'])}"
        data.update(msg)
        erro = True

    if type(data['entity_id']) != int:
        print(f"Campo 'entity_id' com datatype inconsistente: Correto=int / Recebido={type(data['entity_id'])}")
        msg['error_entity_id'] = f"Campo 'entity_id' com datatype inconsistente: Correto=int / Recebido={type(data['entity_id'])}"
        data.update(msg)
        erro = True
    
    try:
         bool(datetime.strptime(data['timestamp'],"%Y-%m-%d %H:%M:%S"))
    except Exception as e:
            print(f"Formato do 'timestamp' esperado str(%Y-%m-%d %H:%M:%S), erro obtido: {e}")
            msg['error_timestamp'] = f"Formato do 'timestamp' esperado str(%Y-%m-%d %H:%M:%S), erro obtido: {e}"
            data.update(msg)
            erro = True

    return erro

def criar_diretorio(directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

def salvar_log_erro(data):

    criar_diretorio('logs/sent/intructions')
    dt = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    file_name = f'id_{dt}.json'
    file_payload = open(f"logs/sent/intructions/{file_name}", "w")
    file_payload.write(json.dumps(data))
    file_payload.close()


def salvar_instrucoes(data):
    criar_diretorio('logs/received/instructions')
    dt = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    file_name = f'id_{dt}.json'
    file_payload = open(f"logs/received/instructions/{file_name}", "w")
    file_payload.write(json.dumps(data))
    file_payload.close()


# def write_file(data, path, instruction_id)

# Definição da rota '/webhook' com suporte a requisições HTTP POST
@app.route('/', methods=["POST"])


def handle_webhook():

    # Recupera o conteúdo da requisição  como um dicionário de python
    # Trata a requisição recebida: Nesse caso, apenas imprimimos os dados
    data = flask.request.get_json()
    if valida_dados(data['body']):
        salvar_log_erro(data)
        myResponse = make_response('Response')
        myResponse.status_code = 847
        return myResponse
    else:
        salvar_instrucoes(data)
        return 'OK'

    
    
    # retornar uma resposta
    # return_code = '200'
    # return return_code

# Verifica se o script esta sendo executado como um módulo principal
if __name__ == '__main__':

    # inicia a aplicação
    app.run(host="localhost", port=5001, debug=True)
