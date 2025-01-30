# 2. Imagina un restaurante con un número limitado de mesas disponibles. Los clientes (hilos) llegan al restaurante y
# desean sentarse en una mesa. Crea un programa que utilice semáforos para coordinar el acceso de los clientes a
# las mesas y asegurarte de que el restaurante no exceda su capacidad (lo haremos en clase)

# 5 mesas = 0 1 2 3 4.
# Queue de gente
# lista de mesas
# El mesero tiene una lista.
# Semaphore <-- lista que controla los que entran a las mesas y los que salen.

import threading
import time
import random
import queue

mesas = []
hilos = []
clientes = []

hilosTerminados = threading.Event()

numMesas = 5

mesero = threading.Semaphore(numMesas)


def aComer(nombre):
    global mesas
    hemosComido = False
    while not hemosComido:
        if mesero.acquire(timeout=2):
            miMesa = None
            for i in range(numMesas):
                if mesas[i] == "libre" and miMesa is None:
                    miMesa = i
                    mesas[miMesa] = nombre
                    print(nombre + ": empezamos a comer")
                    hemosComido = True

            if miMesa is not None:
                time.sleep(random.randint(20, 50))

                mesas[miMesa] = "libre"
                print(nombre + ": terminó de comer en mesa " + str(i))
                mesero.release()

        else:
            print(nombre + ": No hay mesas libres")
            time.sleep(random.randint(5, 10))
    print(nombre + ": Me voy")
    
    hilos.remove(threading.current_thread())  
    if len(hilos) == 0:  
        hilosTerminados.set()



def imprimirMesas():
    while not hilosTerminados.is_set():
        print(mesas)
        time.sleep(2)


for _ in range(numMesas):
    mesas.append("libre")


hilo = threading.Thread(target=imprimirMesas, args=())
hilo.start()


for h in range(1, 15):
    hilo = threading.Thread(target=aComer, args=("Cliente_" + str(h),))
    hilos.append(hilo)
    hilo.start()
    time.sleep(random.randint(2, 5))


for j in hilos:
    j.join()
