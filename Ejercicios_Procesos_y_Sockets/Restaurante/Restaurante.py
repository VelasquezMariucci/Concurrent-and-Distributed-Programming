# 3. Imagina un restaurante con un número limitado de mesas disponibles. Los 
# clientes (número aleatorio de procesos hijo) llegan al restaurante y desean
# sentarse en una mesa. Crea un programa que utilice sockets TCP para coordinar
# el acceso de los clientes a las mesas y asegurarte de que el restaurante no 
# exceda su capacidad. Cada cliente deberá abrir una nueva conexión que el 
# camarero utilizará para informarles cuando una mesa se libere. Cuando el 
# cliente termine de comer, informará al camarero de nuevo por la misma conexión
# para liberar la mesa y cerrará la conexión. El restaurante terminará su 
# jornada cuando todos sus procesos hayan cerrado todas sus conexiones.

from multiprocessing.dummy import freeze_support
import random
import socket
import threading
import time
import multiprocessing

# Variables
ip_servidor = "127.0.0.1"
port_servidor = 1000
num_mesas = 5

semaforo_mesas = threading.Semaphore(num_mesas)
mutex_mesero = threading.Lock()

clientes = []

def mesero():
    socket_mesero = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_mesero.bind((ip_servidor, port_servidor))
    
    socket_mesero.listen(5)

    while True:
        if mutex_mesero.acquire():
            data, addr = socket_mesero.accept()
            
            mensaje = data.recv(1024).decode()
            
            if mensaje == "sentarme":
                if semaforo_mesas.acquire(timeout=5):
                    mensaje = "asignada".encode()
                    
                    data.send(mensaje)
                    print("cliente sentado.")

                    
                    mensaje = data.recv(1024).decode()
                    
                    if mensaje == "termine":
                        print("Cliente libero la mesa.")
                        semaforo_mesas.release()
                        
                        mensaje = "libre".encode()
                        
                        data.send(mensaje)
                else:
                    mensaje = "no hay".encode()
                    
                    data.send(mensaje)
                    print("no hay mesas disponibles.")
                
                mutex_mesero.release()  
                data.close()
        

def cliente(num_cliente):
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((ip_servidor, port_servidor))

    mensaje = "sentarme".encode()

    socket_cliente.send(mensaje)
    respuesta = socket_cliente.recv(1024).decode()

    if respuesta == "asignada":
        print(f"Cliente {num_cliente} ha comenzando a comer.")
        
        time.sleep(random.randint(1, 3)) 
        
        mensaje = "termine".encode()
        
        socket_cliente.send(mensaje)
        respuesta = socket_cliente.recv(1024).decode()
        
        if respuesta == "libre":
            print(f"cliente {num_cliente} libera la mesa.")
            
    elif respuesta == "no hay":
        print(f"Cliente {num_cliente} no pudo sentarse y se fue.")

    socket_cliente.close()

if __name__ == "__main__":
    freeze_support()

    hilo_mesero = threading.Thread(target=mesero)
    hilo_mesero.start()

    for i in range(0, 15): 
        p = multiprocessing.Process(target=cliente, args=(i,))
        clientes.append(p)
        p.start()
        
        time.sleep(1) # un poco de tiempo entre clientes

    for c in clientes:
        c.join()

    print("fin jordnada restaurante")