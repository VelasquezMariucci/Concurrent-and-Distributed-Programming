from multiprocessing.dummy import freeze_support
import threading
import socket
import time
import multiprocessing
import random

ip_servidor = "127.0.0.1"
port_servidor = 1000

def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_servidor.bind((ip_servidor,port_servidor))
    
    while True: 
        data, addr = socket_servidor.recv(1024)
        
        mensaje = data.decode()
        
        socket_servidor.send(mensaje.encode(), addr)
        
        
def cliente():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    mensaje = "".encode()
    
    socket_cliente.sendto(mensaje, (ip_servidor,port_servidor))
    
    respuesta, _ = socket_cliente.recvfrom(1024)
    
    
if __name__ == "__main__":
    freeze_support()
    
    thread_servidor = threading.Thread(target=servidor)
    thread_servidor.start()
    
    for i in range(0,5):
        m = multiprocessing.Process(target=cliente)
        m.start()