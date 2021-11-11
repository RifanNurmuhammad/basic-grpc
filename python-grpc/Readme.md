## Basic using GRPC on Python

https://grpc.io/docs/languages/python/quickstart/

### Requirements

- Install python
- Instal pip
  ```shell
  $ python -m pip install virtualenv
  $ virtualenv venv
  $ source venv/bin/activate
  $ python -m pip install --upgrade pip
  ```
- Install GRPC
  ```shell
  $ python -m pip install grpcio
  ```
- Install GRPC Tools
  ```shell
  $ python -m pip install grpcio-tools
  ```

### Generate Code .proto file

- Create proto file
  proto/actor.proto
- Run
  ```shell
   python -m grpc_tools.protoc -Iactor/proto --python_out=actor/proto --grpc_python_out=actor/proto actor/proto/actor.proto
  ```
- Run Server

  ```shell
  python actor/server/server.py
  ```

- Run Client

  ```shell
  python actor/client/client.py
  ```
