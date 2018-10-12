This application is for demonstrating kubernetes and istio application and validate deployment and security pattern

# poetryapp
The application is the combination of 4 microservices:
1. poetrypage: a Python microservice that feeds itself off poetrywebapp
2. poetrywebapp: a Java application that aggregates information from poemprovider and poetbio applications
3. poemprovider: a Java application that sends a poem
4. poetbio: a Go application that sends a poet biography

# Docker
Once all dockers are build/pushed and are running see container images with the following command
``` console
docker container ls -a
```

Whenever you're done you can delete all installed docker container by killing them ```docker kill $(docker ps -q) ``` and deleting them ```docker rm $(docker ps -a -q)```

# Minikube
Follow minikube documentation for installation

Start minikube: ``` minikube start --vm-driver docker-machine-driver-hyperkit --cpus 4 --memory 8192``` and validate it's running fine: ``` kubectl get nodes ```


Whenever you're done you can stop minikube: ```minikube stop```

On osx if cpu starts peaking try shutting down minikube dashboard:
```
k get pods -n kube-system -o name
and kill the dashboard
k delete pods -n kube-system kubernetes-dashboard-5498ccf677-9rg8v
```

# Run in kubernetes

We are using a deployment spec that can be installed for each application using the following command: ```k apply -f deployment-poetrywebapp.yaml ```