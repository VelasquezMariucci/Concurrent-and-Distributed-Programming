# lograr la sincronización
# de tres procesos (P1, P2 y P3) de forma que el orden de la ejecución de las sentencias S1, S2 y S3 de
# los procesos sea la siguiente: en primer lugar se debe ejecutar S1; al finalizar S1 se puede ejecutar S3 y
# cuando finaliza S3 se puede ejecutar S2. Al terminar S2 se puede volver a ejecutar S1 y así
# sucesivamente. Para lograr la sincronización se deben emplear semáforos.

import random
import threading
import time

sem1 = threading.Semaphore()
sem2 = threading.Semaphore()
sem3 = threading.Semaphore()

def p1():
    while True:
        if sem1.acquire():
            print("Se esta ejecutando el proceso 1")
            time.sleep(2)
            sem3.release()
            
def p2():
    while True:
        if sem2.acquire():
            print("Se esta ejecutando el proceso 2")
            time.sleep(2)
            sem1.release()
            
def p3():
    while True:
        if sem3.acquire():
            print("Se esta ejecutando el proceso 3")
            time.sleep(2)
            sem2.release()

hilo1 = threading.Thread(target=p1)
hilo2 = threading.Thread(target=p2)
hilo3 = threading.Thread(target=p3)

sem2.acquire()
sem3.acquire()

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()