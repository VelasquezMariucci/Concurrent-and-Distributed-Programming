from multiprocessing.dummy import freeze_support
import threading
import multiprocessing
import socket
import random
import time

ip_servidor = "127.0.0.1"
port_servidor = 1000

def servidor():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind((ip_servidor, port_servidor))
    socket_servidor.listen()
    
    while True:
        conn, addr = socket_servidor.accept()
        
        mensaje = conn.recv(1024).decode()
        
        # logica de mensaje
        
        conn.send(mensaje.encode())
        
        conn.close()
        

def cliente():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip_servidor, port_servidor))
    
    mensaje = "".encode()
    
    socket_cliente.send(mensaje)
    
    respuesta = socket_cliente.recv(1024).decode()
    
    socket_cliente.close()
    

if __name__ == "__main__":
    freeze_support()
    
    thread_servidor = threading.Thread(target=servidor)
    thread_servidor.start()
    
    for i in range(0,5):
        m = multiprocessing.Process(target=cliente)
    