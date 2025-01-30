# Ejercicio 4: Conexión UDP
# Crea un servidor UDP que reciba mensajes de texto de clientes.
# El servidor debe invertir el texto y enviarlo de vuelta al cliente.
# Introduce un manejo de errores para situaciones donde los paquetes UDP no lleguen.

from multiprocessing.dummy import freeze_support
import threading 
import socket
import multiprocessing
import random

ip_servidor = "127.0.0.1"
port_servidor = 1000

palabras = ["Hola", "Carro", "Perro", "Gato", "Moto"]

def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_servidor.bind((ip_servidor, port_servidor))
    
    while True:
        data, addr = socket_servidor.recvfrom(1024)
        
        mensaje = data.decode()
        
        print("Mensaje recivido: " + mensaje)
        
        mensaje = mensaje[::-1]
        
        print("Mensaje al revez: " + mensaje)
        
        socket_servidor.sendto(mensaje.encode(), addr)
        
        
def cliente():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    mensaje = random.choice(palabras)
    
    socket_cliente.sendto(mensaje.encode(), (ip_servidor, port_servidor))
    
    respuesta, _ = socket_cliente.recvfrom(1024)
    
    print("Respuesta: " + respuesta.decode())
    
    
    
if __name__ == "__main__":
    freeze_support()
    
    thread_servidor = threading.Thread(target=servidor)
    thread_servidor.start()
    
    for i in range(0,5):
        m = multiprocessing.Process(target=cliente)
        m.start()
    
        
        
        