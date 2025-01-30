from multiprocessing import freeze_support
import threading
import socket

ip_servidor = "127.0.0.1"
port_servidor = 1000

clientes = []
lock = threading.Lock()  # Create a lock for thread-safe access to the clientes list

def manejar_cliente(conn, addr):
    try:
        while True:
            mensaje = conn.recv(1024)
            if not mensaje:
                print(f"Cliente desconectado: {addr}")
                break  # Exit the loop if the client disconnects
            
            mensaje_decoded = mensaje.decode()
            print(f"Mensaje recibido de {addr}: {mensaje_decoded}")
            
            # Broadcast the message to all other clients
            with lock:  # Ensure thread-safe access to the clientes list
                for cliente in clientes:
                    if cliente != conn:
                        try:
                            cliente.send(mensaje)
                        except Exception as e:
                            print(f"Error enviando mensaje a {cliente.getpeername()}: {e}")
    except Exception as e:
        print(f"Error manejando el cliente {addr}: {e}")
    finally:
        with lock:
            if conn in clientes:
                clientes.remove(conn)  # Remove the client from the list
        conn.close()  # Close the connection

def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((ip_servidor, port_servidor))
    socket_servidor.listen(2)
    print(f"Servidor escuchando en {ip_servidor}:{port_servidor}")
    
    while True:
        conn, addr = socket_servidor.accept()
        print(f"Cliente conectado: {addr}")
        
        with lock:  # Ensure thread-safe access to the clientes list
            clientes.append(conn)
        
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo_cliente.start()

if __name__ == "__main__":
    freeze_support()
    
    servidor()