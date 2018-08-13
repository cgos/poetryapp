# Build
```
mvn package
```

# Run locally
```
java -jar poetrywebapp-0.1.0.jar --poemprovider.api.url=http://127.0.0.1:8181/poem --poetbio.api.url=http://127.0.0.1:8888/poetbio
```

Test by opening browser to: http://127.0.0.1:8080/poetry

# Running the docker image/container 
start poetbio and poemprovider docker container
## Update poetrywebapp docker deployment
find IP for those 2 container with:
``` 
docker inspect <container name> | grep "IPAddress"
docker inspect poetbio | grep "IPAddress"
docker inspect poemprovider | grep "IPAddress"
```

Update Dockerfile ENV variables

## build docker
```
docker build -f Dockerfile -t cgos/
```
## push to repo
```
docker push cgos/
```

## run docker
```
docker run -d -p 8080:8181 $DOCKER_USER_ID/
```