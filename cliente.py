import socket

def client():
    server_ip = '127.0.0.1'
    server_port = 8088
    # Criar socket e conectar ao servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Enviar mensagem ao servidor
    message = "tentativa 3"
    client_socket.send(message.encode('utf-8'))

    # Receber resposta do servidor
    response = client_socket.recv(1024).decode('utf-8')
    print(f"[SERVIDOR] {response}")

    # Fechar conexão
    client_socket.close()

if __name__ == "__main__":
    client()
