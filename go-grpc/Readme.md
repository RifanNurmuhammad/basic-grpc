## Basic using GRPC on Golang

https://grpc.io/docs/languages/go/quickstart

### Requirements

- Install golang
- Instal protocol buffer (brew install protobuf)
- export GO111MODULE=on
- go mod init example.com/go-grpc
- go get google.golang.org/protobuf/cmd/protoc-gen-go
- go get google.golang.org/grpc/cmd/protoc-gen-go-grpc

### Generate Code .proto file

- Create proto file
  proto/movie.proto
- Run
  ```shell
  protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    movie/proto/movie.proto
  ```
- Run Server

  ```shell
  go run movie/server/server.go
  ```

- Run Client

  ```shell
  go run movie/client/client.go
  ```
