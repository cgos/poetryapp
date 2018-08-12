#H1 Build
mvn package

#H1 Run locally
java -jar poetrywebapp-0.1.0.jar --poemprovider.api.url=http://127.0.0.1:8181/poem --poetbio.api.url=http://127.0.0.1:8888/poetbio

Test by opening browser to: http://127.0.0.1:8080/poetry

#H1 Creating/Pushing/Running/Stopping the docker image/container 
* start poetbio and poemprovider docker container
* find IP for those 2 container with 
''' console
docker inspect <container name> | grep "IPAddress"
'''

* docker build -f Dockerfile -t cgos/
* docker push cgos/
* docker run -d -p 8080:8181 $DOCKER_USER_ID/