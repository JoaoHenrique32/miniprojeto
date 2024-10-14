import socket
import threading

# Contador de conexões ativas
connections = 0
lock = threading.Lock()

def handle_client(client_socket, client_address):
    global connections
    with lock:
        connections += 1
    print(f"[NOVA CONEXÃO] {client_address} conectado. Conexões ativas: {connections}")
    
    # Receber mensagem do cliente
    message = client_socket.recv(1024).decode('utf-8')
    print(f"[RECEBIDO] {client_address}: {message}")

    # Enviar resposta
    response = f"Hello, Client! Você é a conexão número {connections}"
    client_socket.send(response.encode('utf-8'))

    # Fechar conexão
    client_socket.close()
    with lock:
        connections -= 1
    print(f"[CONEXÃO FECHADA] {client_address} desconectado. Conexões ativas: {connections}")

def server():
    server_ip = '0.0.0.0'
    server_port = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"[ESCUTANDO] Servidor escutando na porta {server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    server()
