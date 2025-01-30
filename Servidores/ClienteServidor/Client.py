import socket

server_ip = "127.0.0.1"
server_port = 12345

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    print("Conexión establecida con el servidor.")

    while True:
        message = input("Escribe un mensaje para el servidor (o 'salir' para terminar): ")
        if message.lower() == "salir":
            print("Cerrando cliente.")
            break

        client_socket.send(message.encode())

        # Receive response from the server
        response = client_socket.recv(1024)
        print(f"Respuesta del servidor: {response.decode()}")
finally:
    client_socket.close()
