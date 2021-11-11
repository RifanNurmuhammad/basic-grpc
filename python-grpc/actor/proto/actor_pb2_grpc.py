# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import actor_pb2 as actor__pb2


class ActorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.findAll = channel.unary_unary(
                '/actor.ActorService/findAll',
                request_serializer=actor__pb2.Empty.SerializeToString,
                response_deserializer=actor__pb2.ActorMessageList.FromString,
                )
        self.addActor = channel.unary_unary(
                '/actor.ActorService/addActor',
                request_serializer=actor__pb2.ActorMessage.SerializeToString,
                response_deserializer=actor__pb2.ActorMessage.FromString,
                )


class ActorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def findAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addActor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'findAll': grpc.unary_unary_rpc_method_handler(
                    servicer.findAll,
                    request_deserializer=actor__pb2.Empty.FromString,
                    response_serializer=actor__pb2.ActorMessageList.SerializeToString,
            ),
            'addActor': grpc.unary_unary_rpc_method_handler(
                    servicer.addActor,
                    request_deserializer=actor__pb2.ActorMessage.FromString,
                    response_serializer=actor__pb2.ActorMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'actor.ActorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ActorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def findAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/actor.ActorService/findAll',
            actor__pb2.Empty.SerializeToString,
            actor__pb2.ActorMessageList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addActor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/actor.ActorService/addActor',
            actor__pb2.ActorMessage.SerializeToString,
            actor__pb2.ActorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)