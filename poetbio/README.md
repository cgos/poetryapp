# H1 Run locally
go run poetbio.go
go build poetbio.go
./poetbio

Test by opening browser to: http://127.0.0.1:8888/poetbio


# H1 Docker
docker run -d -p 8888:8888 cgos/poetbio

