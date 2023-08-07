import grpc
from concurrent import futures
import time

# import the generated classes
import chat_pb2
import chat_pb2_grpc

# import the original chat.py
import chat

# create a class to define the server functions, derived from chat_pb2_grpc.ChatServicer
class ChatService(chat_pb2_grpc.ChatServiceServicer):

    def GetChat(self, request, context):
        response = chat_pb2.ChatResponse()
        response.msg = chat.process_request(request.msg, request.model)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

chat_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatService(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
