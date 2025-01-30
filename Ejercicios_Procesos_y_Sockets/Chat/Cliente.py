from multiprocessing.dummy import freeze_support
import socket
import threading

ip_servidor = "127.0.0.1"
port_servidor = 1000

def recibir_mensaje(socket_cliente):
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode()
            if not mensaje:
                print("El servidor ha cerrado la conexión.")
                break
            print(mensaje)
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break

def cliente():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip_servidor, port_servidor))
    
    # Start the thread to receive messages
    hilo_recibir = threading.Thread(target=recibir_mensaje, args=(socket_cliente,))
    hilo_recibir.start()
    
    while True:
        mensaje = input()
        if mensaje.lower() == 'salir':
            break
        try:
            socket_cliente.send(mensaje.encode())
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
            break
    
    # Close the socket when done
    socket_cliente.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    freeze_support()
    
    cliente()