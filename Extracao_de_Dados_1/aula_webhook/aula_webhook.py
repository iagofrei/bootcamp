import flask
import json
import os
from flask import Flask, make_response
from datetime import datetime

# flask simula servidor na maquina
#inicialização da aplicação flask
app = flask.Flask(__name__)
# Definição da rota '/weebhook' com suporte a requisições HTTP POST


def valida_erro(data):
   
   print(f'Received data: {data}')
   
   msg = {}
   erro = False
   
   chaves = ["name", "title", "body", "date", "numero"]
   chaves_recebidas = data.keys()
   print(chaves_recebidas)

   i = 0
   for key in chaves:
      if key not in chaves_recebidas:
         print(f"Chave Inexistente: {key}")
         msg[i] = f"Chave Inexistente: {key}"
         erro = True
         i = i + 1
         data.update(msg)
   if erro:
      return erro

   if type(data['name']) != str:
      print(f"Campo name com datatype inconsistente: Correto=str / Recebido={type(data['name'])}")
      msg['error_name'] = f"Campo name com datatype inconsistente: Correto=str / Recebido={type(data['name'])}"
      data.update(msg)
      erro = True

   if type(data['title']) != str:
      print(f"Campo title com datatype inconsistente: Correto=str / Recebido={type(data['title'])}")
      msg['error_title'] = f"Campo title com datatype inconsistente: Correto=str / Recebido={type(data['title'])}"
      data.update(msg)
      erro = True

   if type(data['body']) != str:
      print(f"Campo body com datatype inconsistente: Correto=str / Recebido={type(data['body'])}")
      msg['error_body'] = f"Campo body com datatype inconsistente: Correto=str / Recebido={type(data['body'])}"
      data.update(msg)
      erro = True

   if type(data['numero']) != int:
      print(f"Campo numero com datatype inconsistente: Correto=int / Recebido={type(data['numero'])}")
      msg['error_numero'] = f"Campo numero com datatype inconsistente: Correto=int / Recebido={type(data['numero'])}"
      data.update(msg)
      erro = True

   try:
      bool(datetime.strptime(data['date'],"%Y-%m-%d %H:%M:%S"))
   except Exception as e:
      print(f"Formato da data esperado %Y-%m-%d %H:%M:%S, erro obtido: {e}")
      msg['error_date'] = f"Formato da data esperado %Y-%m-%d %H:%M:%S, erro obtido: {e}"
      data.update(msg)
      erro = True


   return erro
      

def criar_diretorios(directory):
   os.makedirs(directory, exist_ok=True)

def salvar_requisicoes(data, directory):
   
   criar_diretorios(directory)

   diretorio = (directory)
   file_name = f"requisicao_{datetime.now().strftime('%Y%m%d-%H%M%S-%f')}.json"
   file_payload = open(f"{diretorio}/{file_name}", "w")
   file_payload.write(json.dumps(data))
   file_payload.close()

@app.route('/webhook', methods=["POST"])

def handle_webhook():
    # Recupera o conteúdp da requisição como um dicionário de python
    data = flask.request.get_json()
    if valida_erro(data):
      name_directory = 'logs'
      salvar_requisicoes(data=data, directory=name_directory)
      myResponse = make_response('Response')
      myResponse.status_code = 413
      return myResponse       
    else:
       name_directory = '00_sor'
       salvar_requisicoes(data=data, directory=name_directory)
       return 'OK'
    
# Verifica se o script esta sendo executado como um modulo principal
if __name__ == '__main__':
    app.run()