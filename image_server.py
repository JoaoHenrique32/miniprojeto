from flask import Flask, request, jsonify
import grpc
import redis
import notification_pb2 as pb2
import notification_pb2_grpc
import threading
import time

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def notify_completion(client_id, message):
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = notification_pb2_grpc.NotificationServiceStub(channel)
        response = stub.NotifyCompletion(pb2.CompletionRequest(client_id=client_id, message=message))
        print(response.status)

@app.route('/upload', methods=['POST'])
def upload_image():
    client_id = request.form['client_id']
    image = request.files['image']

    # Armazena na fila do Redis
    redis_client.lpush('image_queue', (client_id, image.read()))
    return jsonify({"status": "Imagem recebida", "client_id": client_id})

def process_images():
    while True:
        if redis_client.llen('image_queue') > 0:
            client_id, image_data = redis_client.rpop('image_queue')
            print(f"Processando imagem para cliente {client_id}")
            time.sleep(5)  # Simula o tempo de processamento

            # Notifica o cliente via gRPC
            notify_completion(client_id, "Sua imagem foi processada!")
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=process_images).start()
    app.run(host='0.0.0.0', port=5000)
