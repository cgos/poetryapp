#H1 Build
mvn package

#H1 Run locally
java -jar poemprovider-0.1.0.jar

Test by opening browser to: http://127.0.0.1:8181/poem

#H1 Creating/Pushing/Running/Stopping the docker image/container 
docker build -f Dockerfile -t cgos/poemprovider .
docker push cgos/poemprovider
docker run -d -p 8080:8181 $DOCKER_USER_ID/poemprovider