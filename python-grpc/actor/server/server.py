from concurrent import futures

import grpc
import actor_pb2
import actor_pb2_grpc


class Actor(actor_pb2_grpc.ActorServicer):

    def FindAll(self, request, context):
        actormessage = actor_pb2.ActorMessage(
            name="thomas alfa", gender="male")
        return actor_pb2.ActorMessageList(actor=actormessage)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    actor_pb2_grpc.add_ActorServicer_to_server(
        Actorervice(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
