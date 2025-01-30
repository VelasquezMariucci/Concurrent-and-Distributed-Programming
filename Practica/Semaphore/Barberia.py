# El problema consiste en una barbería en la que trabaja un barbero que tiene 
# un único sillón de barbero y varias sillas para esperar. Cuando no hay 
# clientes, el barbero se sienta en una silla y se duerme. Cuando llega un 
# nuevo cliente, éste o bien despierta al barbero o —si el barbero está 
# afeitando a otro cliente— se sienta en una silla.

import threading
import time
import random
from queue import Queue

sillasLibres = 5 

clientes = []

clientesEntrados = 0

sillasEspera = threading.Semaphore(5)
sillaBarbero = threading.Semaphore(0)

mutex = threading.Lock()

def barbero():
    while True:
        print("El barbero esta dormido")
        sillaBarbero.acquire()
        print("El barbero esta cortando el pelo")
        time.sleep(2)
        print("El barbero ha terminado de cortar el pelo")
        
        
def cliente():
    global sillasLibres
    time.sleep(random.randint(2,3))
    print("El cliente llega a la barberia")
    
    mutex.acquire()
    try:
        if sillasLibres > 0:
            sillasLibres -= 1
            
            print("El cliente se sienta en una silla de espera")
                
            sillasEspera.acquire()
            
            sillaBarbero.release()
        else:
            print("El cliente se va xq no habian sillas libres")
    finally:
        mutex.release()
        
    if sillasEspera._value < 5:
        sillasEspera.release()
        mutex.acquire()
        try:
            sillasLibres+=1
        finally:
            mutex.release()
    print("El cliente termino y sale de la barberia")
    
            
barb = threading.Thread(target=barbero)
barb.start()

for i in range(0, 20):
    thread = threading.Thread(target=cliente)
    clientes.append(thread)
    thread.start()
    
for hilo in clientes:
    hilo.join()
