import multiprocessing
from multiprocessing.dummy import freeze_support
import os
import socket
import threading
import random
import time

# Constantes globales
LOG_DIR = "LOGS"
ip_servidor = "127.0.0.1"  

procesos = []

os.makedirs(LOG_DIR, exist_ok=True)

def consumidor(ip, puerto): 
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    archivo_consumidor = os.path.join(LOG_DIR, f"{ip}_{puerto}_pedidos.txt")
    num_peticiones = random.randint(5, 15)

    for i in range(0, num_peticiones):
        
        indice = random.randint(1,3)
        if (indice == 1):
            producto_solicitado = "Tornillos"
        elif (indice == 2):
            producto_solicitado = "Clavos"
        else:
            producto_solicitado = "Tuerca"
        
        socket_cliente.sendto(producto_solicitado.encode(), (ip, puerto))

        archivo = open(archivo_consumidor, "a")
        archivo.write(f"Solicito {producto_solicitado}\n")
        
        time.sleep(random.randint(1, 2))
        
    socket_cliente.close()
    archivo.close()
    

if __name__ == "__main__":
    freeze_support()
    
    num_consumidores = random.randint(3, 10)
    procesos = []

    for i in range(num_consumidores):
        puerto_cliente = 1000 + i
        proceso = multiprocessing.Process(target=consumidor, args=(ip_servidor, puerto_cliente))
        procesos.append(proceso)
        
        proceso.start()

    for p in procesos:
        p.join()