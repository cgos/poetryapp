mvn package
docker build -f Dockerfile -t cgos/poemprovider .
docker push cgos/poemprovider
docker run -d -p 8080:8181 $DOCKER_USER_ID/poemprovider