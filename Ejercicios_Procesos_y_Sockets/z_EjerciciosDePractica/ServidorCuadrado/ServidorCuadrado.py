# Ejercicio 2: Servidor y Cliente TCP
# Crea un servidor TCP que pueda manejar múltiples clientes usando threading.
# Cada cliente debe enviar un número, y el servidor debe devolver el cuadrado de ese número.
# Maneja excepciones para desconexiones inesperadas de los clientes.

import multiprocessing
from multiprocessing.dummy import freeze_support
import socket
import threading

ip_servidor = "127.0.0.1"
port_servidor = 1000

def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((ip_servidor, port_servidor))
    socket_servidor.listen()
    
    while True:
        conn, addr = socket_servidor.accept()
        
        mensaje = conn.recv(1024).decode()
        print(f"Mensaje recibido: {mensaje}")
        
        numero = int(mensaje)
        resultado = numero ** 2
        
        conn.send(str(resultado).encode())
        print(f"Mensaje enviado: {resultado}")
        
        conn.close()
        


def clientes(num):
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip_servidor, port_servidor))
    
    mensaje = str(num).encode()
    
    socket_cliente.send(mensaje)
    
    respuesta = socket_cliente.recv(1024).decode()
    
    print("Respuesta: " + respuesta)
    
    socket_cliente.close()


if __name__ == "__main__":
    freeze_support()
    
    thread_servidor = threading.Thread(target=servidor)
    thread_servidor.start()
    
    for i in range(0,10):
        m = multiprocessing.Process(target=clientes, args=(i,))
        m.start()