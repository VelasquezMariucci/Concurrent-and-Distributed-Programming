#You are tasked with simulating a multi-stage data pipeline using threads and barriers. The pipeline has three stages:
#Data Loading: Threads load data chunks from a shared list.
#Data Processing: Threads perform a computation (e.g., squaring the data).
#Data Saving: Threads write the processed data to an output list.

import threading
import time
import random

hilos = []

barrier = threading.Barrier(5)

def pipeline(nombre):
    print("El hilo " + nombre + " Comienza Data Loading.")
    time.sleep(random.randint(1,3))
    barrier.wait()
    print("El hilo " + nombre + " Continua Data Processing.")
    time.sleep(random.randint(1,3))
    barrier.wait()
    print("El hilo " + nombre + " Finaliza Data Saving.")
    time.sleep(random.randint(1,3))
    

for i in range(0,5):
    thread = threading.Thread(target=pipeline, args=(str(i)))
    hilos.append(thread)
    thread.start()    