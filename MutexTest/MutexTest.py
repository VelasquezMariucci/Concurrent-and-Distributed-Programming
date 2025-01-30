import random
import threading

# variabel compartida
contador = 0

# mutex
mutex = threading.Lock()


# funcion para aumentar el tamaÑo del contador de forma segura
def auementar_contador():
    global contador
    with mutex:
        contador += 1


# crear hilos para aumetnad el contador
threads = []
for _ in range(100):
    t = threading.Thread(target=auementar_contador)
    threads.append(t)

# iniciar los hilos
for t in threads:
    t.start()

# Esperar a que todos los hilos terminen
for t in threads:
    t.join()

# imprimir el resultado
print("El resultado es:", contador)


