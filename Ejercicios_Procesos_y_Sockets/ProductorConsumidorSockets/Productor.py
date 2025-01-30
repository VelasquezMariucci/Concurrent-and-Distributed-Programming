# 2. Implementa un problema de productor-consumidor, con un numero aleatorio 
# sockets UDP a modo de clientes consumidores, donde los productores generan 
# aleatoriamente elementos con características específicas y los consumidores 
# solo pueden tomar elementos que cumplan un determinado criterio (aleatorio) de
# entre las características producidas (el productor será un programa servidor y 
# los clientes serán un sprograma consumidor con varios hilos que abren las 
# conexiones para consumir). El servidor creará una cola para todo lo que produzca
# y recibirá conexiones UDP de los clientes con el tipo de item a consumir. Cada 
# vez que se consume un item, se saca de la cola y, si no se puede consumir, se 
# reincorpora a la cola. Si el elemento del inicio de la cola coincide con una 
# petición, se escribirá en una linea nueva en un archivo con el producto consumido,
# o con un mensaje de error si no se puede servir por no ser del tipo adecuado. 
# Cada consumidor realizará un número aleatorio de peticiones y escribirá también en
# otro archivo las peticiones que ha realizado. El nombre de archivo del servidor para
# cada cliente, será la IP y el puerto del consumidor, y la palabra "envios". El 
# cliente escribirá su propio archivo con su IP, el puerto y la palabra "pedidos" en 
# el nombre de archivo. Los clientes terminarán su ejecución cuando terminen sus 
# peticiones. El servidor no terminará nunca su ejecución, porque estará esperando 
# conexiones, pero cuando todos los clientes hayan terminado, lo consumido en cada 
# archivo del servidor y cada archivo del cliente, debería coincidir. ¿Coincide siempre?

import os
import queue
import socket
import threading
import random
import time

# Constantes globnales
LOG_DIR = "LOGS"

# Variables globales
queue_productos = queue.Queue()
numero_sockets = random.randint(3, 10)

sockets = [] # borrar creo que no se necesita

os.makedirs(LOG_DIR, exist_ok=True)

ip_servidor = "127.0.0.1"
port_servidor = 1000

for i in range(numero_sockets):
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_servidor.bind((ip_servidor, port_servidor+i))
    
    sockets.append(socket_servidor)


def productor():
       
    producto = ""
    
    while True:
        indice = random.randint(1, 3) 
        
        if (indice == 1):
            producto = "Tornillos"
        elif (indice == 2):
            producto = "Clavos"
        else:
            producto = "Tuerca"
        
        print(f"Producto producido = {producto}")
        
        queue_productos.put(producto)
        time.sleep(random.randint(1,2))
    
    
def servidor(socket_servidor): 
    while True:
        data, addr = socket_servidor.recvfrom(1024)
        producto_solicitado = data.decode()
        
        prod_dir = os.path.join(LOG_DIR, f"{addr[0]}_{addr[1]}_envios.txt")
        
        producto = queue_productos.get()
        
        if not queue_productos.empty():
            if producto_solicitado ==  producto: 
                archivo = open(prod_dir, "a")
                archivo.write(f"{producto} cosnumdio por {addr}\n")
                
                print(f"{producto} cosnumdio por {addr}")
                archivo.close()
                
                socket_servidor.sendto(b"Producto consumido.", addr)
            else:
                queue_productos.put(producto)
                
                archivo = open(prod_dir, "a")
                archivo.write("Producto no coincide con solicitud.\n")
                
                print("Producto no coincide con solicitud.")
                archivo.close()
                
                socket_servidor.sendto(b"Producto no coincide.", addr)
                
        else:
            producto = ""
            socket_servidor.sendto(b"queue vacia.", addr)
            print("quee vacia.")
       
       
for socket_servidor in sockets:
    hilo_servidor = threading.Thread(target=servidor, args=(socket_servidor,))
    hilo_servidor.start()
       
hilo_productor = threading.Thread(target=productor)
hilo_productor.start()