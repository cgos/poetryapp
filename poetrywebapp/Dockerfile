FROM openjdk:8-jdk-alpine
ENV POEMPROVIDER_API_URL http://172.17.0.2:8181/poem
ENV POETBIO_API_URL http://172.17.0.3:8888/poetbio
ADD target/poetrywebapp-0.1.0.jar /
EXPOSE 8080
CMD ["java", "-jar", "poetrywebapp-0.1.0.jar", "--poemprovider.api.url=${POEMPROVIDER_API_URL}", "--poetbio.api.url=${POETBIO_API_URL}"]