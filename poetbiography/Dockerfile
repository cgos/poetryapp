FROM golang:latest 
ENV SRC_DIR=/poetryapp/poetbiography/src/poetbio
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go build -o main . 
CMD ["/app/main"]