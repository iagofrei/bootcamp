
### Criar os arquivos do terraform
` terraform init ` (tem que ser dentro da pasta que esta o arquivo main.tf)


### Fazer o apply do terraform
` terraform apply ` (tem que ser dentro da pasta que esta o arquivo .terraform e tem que ser aplicado depois do terraform init, não precisa rodar o init quando fizer alguma alteração no main.tf)

### Fazer o apply do terraform automatico 
(Não precisa digitar yes no meio do processo do apply)
` terraform apply -auto-approve ` 

### Fazer o destroy do terraform automatico 
` terraform destroy -auto-approve ` 


### Como executar programas de terminam no linux
#### Dar permição de execução para o arquivo
` chmod +x filename.sh ` 
#### Executar o arquivo
` ./filename.sh ` 

### Aplicando no nosso script
` chmod +x deploy-website.sh ` 
` ./deploywebsite.sh ` 