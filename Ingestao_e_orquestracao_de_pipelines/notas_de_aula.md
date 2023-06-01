### 1- Instalar o python
` sudo apt-get install python3 `

### 2- Instalar os pacotes do pip
` sudo apt-get install python3-pip `

### 3- Instalar o pacote do pika
` pip install pika --upgrade `

### 4- Instalar o rabbitmq-server
` sudo apt-get install rabbitmq-server `

### 5- Executar o rabbitmq-server
` sudo service rabbitmq-server start `

### 6- Rodar o 01_producer.py 
` python3 01_producer.py `


### Executar o rabbitmq-server
` sudo service rabbitmq-server start `

### Parar o rabbitmq-server
` sudo service rabbitmq-server stop `

### Listar as filas na maquina
` sudo rabbitmqctl list_queues `