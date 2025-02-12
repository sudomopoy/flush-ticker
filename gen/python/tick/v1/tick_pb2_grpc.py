# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tick.v1 import tick_pb2 as tick_dot_v1_dot_tick__pb2


class TickerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tick = channel.unary_unary(
                '/example.Ticker/Tick',
                request_serializer=tick_dot_v1_dot_tick__pb2.TickRequest.SerializeToString,
                response_deserializer=tick_dot_v1_dot_tick__pb2.TickResponse.FromString,
                _registered_method=True)


class TickerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Tick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Tick': grpc.unary_unary_rpc_method_handler(
                    servicer.Tick,
                    request_deserializer=tick_dot_v1_dot_tick__pb2.TickRequest.FromString,
                    response_serializer=tick_dot_v1_dot_tick__pb2.TickResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'example.Ticker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('example.Ticker', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Ticker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Tick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/example.Ticker/Tick',
            tick_dot_v1_dot_tick__pb2.TickRequest.SerializeToString,
            tick_dot_v1_dot_tick__pb2.TickResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
