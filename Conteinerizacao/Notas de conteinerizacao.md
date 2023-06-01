# Comandos para conteinerização

#### Deixar a flag do unbunto ativada por padrão no docker (rodar no powershell)
` wsl --set-default ubuntu `


### Caso o docker pare de funcionar (carregue e não pare de carregar nunca use esse comando no powershell)
` wsl --unregister docker-desktop `
` wsl --unregister docker-desktop-data `


## Aula do dia 27/02/23

### Imagens

### Puxando e rodando a imagem
` docker run -d -p 8080:80 --name webserver nginx `

### Listando os containers
` docker ps `

### Listando imagens
` docker images `

### Acoplar ao container
` docker container exec -it webserver bash `

### Para o container 
` docker stop webserver `

### Remover a imagem
` docker rmi nginx `

### Como baixar imagens

Exemplo de como baixar a imagem do nginx

` docker pull nginx `

### Como deletar uma imagem

Exemplo de como deletar a imagem do nginx


## Network

### Como criar uma network

` docker network create nome_da_network `

### Como listar as networks
` docker network ls `

### Como deletar uma networks
` docker network rm nome_da_network `



## Aula do dia 01/03/23

### Comando para fazer o build da aplicação no docker

` docker build -t nome_da_imagem:versao_da_imagem . `
> -t serve para dizer qual é a tag (nome do aplicativo e depois dos 2 pontos é a tag que seria a versão).

> O ponto no final serve para dizer onde esta o arquivo do dockerfile, como estamos na pasta onde o dockerfile esta, o . serve para indicar que o arquivo dockerfile esta na pasta atual


public.ecr.aws/f6e8d9s2/bootcamp:1.0



## Aula do dia 02/03/23

### Comandos do dockerfile
` WORKDIR `

> Serve para alterar o diretorio de trabalho (seria igual um cd)



## Docker compose

### Como iniciar o docker compose
docker compose -f nome_do_arquivo_compose.yaml up -d 
> -d serve para iniciar o docker compose sem estar anexada ao terminal (detached)

### Como parar os containers
` docker compose -f nome_do_arquivo_compose.yaml stop `



## Docker stack

### Como criar as maquinas
### Comando para criar a maquina

` docker-machine create -d amazonec2 --amazonec2-vpc-id vpc-0700f7815be315653 --amazonec2-subnet-id subnet-0be16d5b2365a4b68 --amazonec2-region sa-east-1 --amazonec2-zone a --amazonec2-instance-type t2.micro --amazonec2-security-group swarm-sg --amazonec2-ami ami-019e9884d49f70483 manager01 `

### Como entrar na maquina
` docker-machine ssh manager01 `

### Como iniciar o swarm (tem que ser feito na manager)
` docker swarm init `

### Após iniciado o swarm, copiar o comando do join para usar nas workers
` docker swarm join --token... `

### Como criar o arquivo stack na manager
criar arquivo no manager (tem que entrar no manager)
` touch stack.yml `

editar o arquivo:
` sudo vim stack.yml `

dentro do editor apertar a tecla "i" para entrar no modo insert
ctrl + v (pra colar o conteudo do stack.yml)
"esc" para sair do modo insert

obs:  se sair com a formatação zuada, cria o arquivo, entra nele com o vim e use ":set paste" e "crtl + v"
se não copiar a primeira linha, saia do modo insert e aperte gg

salvar e sair da edição:
digitar ` :wq `


### Comando para deletar uma stack (deve ser rodado na manager)
` sudo docker stack rm "nome_da_stack" (deleta a stack) `  

### Comando para deployar uma stack (deve ser rodado na manager)
` sudo docker stack deploy -c stack.yml vote ` (vote é o nome_da_stack) (pra criar a stack)

### Comando para listar a stack e seus serviços (rodado nas maquinas da aws manager e workers)
` sudo docker stack ps vote ` (pra ver em quais maquinas os serviços estao rodando)

### comando para pegar o ip das maquinas (deve ser rodado na maquina local)
` docker-machine ip manager01 ` (pra pegar o ip da manager)



