
# CI/CD

#### criando o volume de persistência
` docker volume create jenkins-data `

#### subindo o controller

` docker run --name jenkins --restart always --detach --privileged --volume jenkins-data:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts ` 

` docker ps ` 

( pegar o "contaier id" do jenkins )

` docker logs id_container_jenkins ` 

```
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

ce72c118dd584ff2ad7702b2afdcbaf3

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```

( Após isso abrir o navegador na http://localhost:8080/   entra com a senha 'ce72c118dd584ff2ad7702b2afdcbaf3' instala os plugins recomendados )

#### pegando o IP do container do controller

` docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' jenkins ` 

172.17.0.2


#### subindo o agent

` docker run -d --init jenkins/inbound-agent -url http://<ip-do-controller>:8080/ <token-do-agent> agent ` 



` docker run -d --init jenkins/inbound-agent -url http://172.17.0.2:8080/ 73fc3f11be4cc082e663bdc49223e3732fba06cac5f1615f104817be0caddcc5 agent ` 




` docker ps | grep jenkins `


` docker start <container_id> `


IagoFreitas
http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/IagoFreitas/index.html

RodrigoPereira
http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/RodrigoPereira/index.html

ThiagoKinjo
http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/ThiagoKinjo/index.html

HigorCangirana
http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/HigorCangirana/index.html

LuizLopes
http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/LuizLopes/index.html








# criando o volume
` docker volume create gitlab-runner-config `

# subindo o runner
` docker run -d --name gitlab-runner --restart always -v /var/run/docker.sock:/var/run/docker.sock -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner:latest `

# registrando o runner
` docker run --rm -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner register --non-interactive --executor "docker" --docker-image ubuntu:latest --url "https://gitlab.com/" --registration-token "SEU_TOKEN" --tag-list "self-hosted" `

` docker run --rm -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner register --non-interactive --executor "docker" --docker-image ubuntu:latest --url "https://gitlab.com/" --registration-token GR1348941oM7myZsndzzpsNWrmsW6 --tag-list "self-hosted" `


# reiniciando o runner
` docker restart gitlab-runner `





http://bootcamp-itau.s3-website-us-east-1.amazonaws.com/IagoFreitas/index.html



export RUNNER_ALLOW_RUNASROOT=1