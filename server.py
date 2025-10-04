import grpc
from concurrent import futures
import time

import greeting_pb2
import greeting_pb2_grpc

class GreetingService(greeting_pb2_grpc.GreetingServiceServicer):
    def SayHello(self, request, context):
        return greeting_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

