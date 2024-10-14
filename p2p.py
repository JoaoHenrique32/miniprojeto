import socket
import threading

def handle_incoming_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[NOVA CONEXÃO] Conectado por {client_address}")

        # Receber mensagem
        message = client_socket.recv(1024).decode('utf-8')
        print(f"[RECEBIDO] {client_address}: {message}")

        # Responder ao peer
        response = "Hello from Node!"
        client_socket.send(response.encode('utf-8'))

        # Fechar conexão
        client_socket.close()

def peer_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"[PEER SERVIDOR] Escutando na porta {port}")

    # Iniciar thread para aceitar conexões
    server_thread = threading.Thread(target=handle_incoming_connections, args=(server_socket,))
    server_thread.start()

def peer_client(target_ip, target_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, target_port))

    # Enviar mensagem ao peer
    message = "Hello, Peer!"
    client_socket.send(message.encode('utf-8'))

    # Receber resposta
    response = client_socket.recv(1024).decode('utf-8')
    print(f"[PEER RESPONDEU] {response}")

    # Fechar conexão
    client_socket.close()

if __name__ == "__main__":
    # Definir portas e IPs
    my_port = 9094
    target_ip = '127.0.0.1'
    target_port = 8089

    # Iniciar o servidor P2P
    peer_server(my_port)

    # Iniciar o cliente P2P em outra thread para se conectar a outro nó
    client_thread = threading.Thread(target=peer_client, args=(target_ip, target_port))
    client_thread.start()
