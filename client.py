import grpc
import greeting_pb2
import greeting_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greeting_pb2_grpc.GreetingServiceStub(channel)
    response = stub.SayHello(greeting_pb2.HelloRequest(name='Alice'))
    print("Greeting from server:", response.message)

if __name__ == '__main__':
    run()
