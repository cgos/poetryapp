# Run locally
1. python3 poetrypage.py 9090  http://172.17.0.3:8080 http://172.17.0.2:8888
2. python3 poetrypage.py 9090 http://127.0.0.1:8080 http://127.0.0.1:8888

Test by opening browser to: localhost:9090/poetrypage?u=normal#

# Creating/Pushing/Running/Stopping the docker image/container

find IP for poetrywebapp container with:
```
docker inspect poetbio | grep "IPAddress"
```

Update poetrypage Dockerfile


1. docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
2. docker build -f Dockerfile -t $DOCKER_USER_ID/poetrypage ./
3. docker push $DOCKER_USER_ID/poetrypage
4. docker pull $DOCKER_USER_ID/poetrypage
5. docker run -d -p 80:9090 --name poetrypage cgos/poetrypage 9090 http://172.17.0.3:8080

# Minikube installation
1. kubectl create -f
