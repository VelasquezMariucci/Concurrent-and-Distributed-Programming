# 3. Implementa un problema de productor-consumidor donde los productores generan elementos con características
# específicas y los consumidores solo pueden tomar elementos que cumplan con ciertos criterios. Utiliza una cola
# bloqueante para gestionar la comunicación entre productores y consumidores.

import threading
import time
import random
from queue import Queue

queue = Queue(5)

items = ["pantalones", "camisas", "medias", "clavos", "tornillos"]

itemsConsumibles = {"pantalones", "camisas", "medias"}

itemsConsumidos = []


def productor():
    while True:
        item = random.choice(items)
        queue.put(item)
        print("Productor creo: " + item)
        time.sleep(random.randint(3, 10))


def consumidor():
    while True:
        item = queue.get()
        if item in itemsConsumibles:
            print("Consumidor consumio: " + item)
            itemsConsumidos.append(item)
        else:
            print("Consumidor ignoro: " + item)
        queue.task_done()
        time.sleep(random.randint(3, 10))


def imprimirEstado():
    while True:
        time.sleep(3)
        print("---------------------------------------------------------")
        current_queue = list(queue.queue)
        print("\n" + "Estado actual de la cola:", current_queue)
        print("Elementos consumidos:", itemsConsumidos)
        print("---------------------------------------------------------")


numProductores = 15
numConsumidores = 10

for _ in range(numProductores):
    p = threading.Thread(target=productor, args=())
    p.start()

for _ in range(numConsumidores):
    c = threading.Thread(target=consumidor, args=())
    c.start()

imprimirEstado = threading.Thread(target=imprimirEstado, args=())
imprimirEstado.start()

queue.join()
