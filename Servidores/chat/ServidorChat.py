import socket
import threading

server_ip = "127.0.0.1"
server_port = 1000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Servidor escuchando en {server_ip}:{server_port}")


def escuchar():
    while True:
        data = client_socket.recv(1024)  # Waits for up to 1024 bytes of data
        if not data:
            print("Cliente desconectado.")
            break

        print(f"Mensaje del cliente: {data.decode()}")

        # Send response to the client
        response_message = "Mensaje recibido por el servidor"
        client_socket.send(response_message.encode())


try:
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")
        
    recibirThread = threading.Thread(target=escuchar)
    recibirThread.start()
        
except KeyboardInterrupt:
    print("\nServidor detenido.")
finally:
    client_socket.close()
    server_socket.close()
