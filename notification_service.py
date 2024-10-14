import grpc
from concurrent import futures
import notification_pb2 as pb2
import notification_pb2_grpc as pb2_grpc

class NotificationService(pb2_grpc.NotificationServiceServicer):
    def NotifyCompletion(self, request, context):
        print(f"Notificação recebida: {request.message} para cliente {request.client_id}")
        return pb2.CompletionResponse(status="Notificação enviada com sucesso")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    print("Serviço de Notificação iniciado.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
