# Kubernets


### Iniciar o minikube
`  minikube start `

### Como listar os contextos
` kubectl config get-contexts `

### Como trocar o contexto
` kubectl config use-context nome_do_contexto `

### Como dar um apply
` kubectl apply -f nome_arquivo `
` kubectl delete -f nome_arquivo `

### Como listar o nome dos services ou pods ou deployments
` kubectl get resource_name `


### Comando para rodar o loadbalancer para pegar as urls
` minikube service mongo-express-service `

### Para habilitar o ingress no minikube
` minikube addons enable ingress `

### Comando para pegar as infos do ingress e deixar apresentando na tela até o ip carregar
` kubectl get ingress --watch `

### Listar os services accouts
` kubectl get pod -n kube-system ` 

### Mostar tudo o que envolve o service accounts

` kubectl get sa -n kube-system `

# EKS AWS


### Criando o cluster
` eksctl create cluster --name my-cluster-3 --version 1.25 --region sa-east-1 --nodegroup-name my-linux-nodes --node-type t2.micro --nodes 2 `

### Parar o cluster
` eksctl scale nodegroup --cluster my-cluster-3 --name my-linux-nodes --nodes 0 --nodes-max 1 --nodes-min 0 `

### Iniciar o cluster
` eksctl scale nodegroup --cluster my-cluster-3 --name my-linux-nodes --nodes 3 --nodes-max 4 --nodes-min 0 `

### Deletar cluster
` eksctl delete cluster --region=sa-east-1 --name=my-cluster `



### IAM Policy

` aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy_latest.json `

```json
{
    "Policy": {
        "PolicyName": "AWSLoadBalancerControllerIAMPolicy",
        "PolicyId": "ANPAQKQ3IVJGI4JW3B32V",
        "Arn": "arn:aws:iam::022605769292:policy/AWSLoadBalancerControllerIAMPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2023-03-22T19:35:36+00:00",
        "UpdateDate": "2023-03-22T19:35:36+00:00"
    }
}
```


` eksctl utils associate-iam-oidc-provider --region sa-east-1 --cluster my-cluster-3 --approve `


` eksctl create iamserviceaccount --cluster=my-cluster-3 --namespace=kube-system --name=aws-load-balancer-controller --attach-policy-arn=arn:aws:iam::022605769292:policy/AWSLoadBalancerControllerIAMPolicy --override-existing-serviceaccounts --approve `


` eksctl get iamserviceaccount --cluster=my-cluster-3 `



` helm repo add eks https://aws.github.io/eks-charts `

` helm repo update `


` helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system --set clusterName=my-cluster --set serviceAccount.create=false --set serviceAccount.name=aws-load-balancer-controller --set region=sa-east-1 --set vpcId=vpc-067279c4375a95c5b --set image.repository=602401143452.dkr.ecr.sa-east-1.amazonaws.com/amazon/aws-load-balancer-controller `





` kubectl get svc -n kube-system `

` helm uninstall aws-load-balancer-controller -n kube-system `



` kubectl -n kube-system describe configmap aws-auth `

` kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master" `


` aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy_volumes.json `

