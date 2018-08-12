FROM golang:onbuild
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go build -o poetbio .
EXPOSE 8888
ENTRYPOINT ["./poetbio"]