import random
import threading
import time
import datetime

threads = []

mydDate = datetime.datetime.now()

mutex = threading.Lock()

path = r"C:\Users\esvel\OneDrive\Desktop\Code\Python\MutexTest\AquireReleaseTest\output.txt"


def escritor(nombre):
    global path

    # print("El path es", path, "y soy ", nombre)

    mutex.acquire()
    try:
        print(nombre + ": Lock open" + "\n" + str(mydDate))
        for a in range(5):
            with open(path, "+a") as arch:
                arch.writelines(
                    "Thread "
                    + str(nombre)
                    + " -> "
                    + "estoy escribiendo "
                    + str(a)
                    + "\n"
                )
            time.sleep(1.0)
    finally:
        mutex.release()
        print(nombre + ": Lock released \n")


print("Vamos a escribir con varios hilos")

for i in range(100):
    nombre = f"Hilo-{i+1}"
    thread = threading.Thread(target=escritor, args=(nombre,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todos los hilos han terminado de escribir.")
