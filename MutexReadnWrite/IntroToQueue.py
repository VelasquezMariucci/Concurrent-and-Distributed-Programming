import threading
import time

lista = []
mutex = threading.Lock()

# more producers = 20 sec
# more consumers = 12 sec
# equal = 12 sec

numProducer = 20
numConsumer = 20

# more producers, more products = 20 sec
# more producers, less products = 30 sec
# more producers, equal products = 20 sec

producerTime = 1
consumerTime = 1


def generar():
    global lista

    for i in range(numProducer):
        if mutex.acquire(timeout=1):
            lista.append(i)
            time.sleep(producerTime)
        else:
            print("El generador no ha podido escribir " + str(i))
            mutex.release()


def leer():
    global lista

    for i in range(numConsumer):
        if mutex.acquire(timeout=1):
            if len(lista) >= 1:
                print("Leemos " + str(lista[len(lista) - 1]))
            else:
                print("No se puede leer nada, porque el indice es 0")
            time.sleep(consumerTime)
        else:
            print("El leer no ha sido posible en " + str(i))
            mutex.release()


hiloGenerador = threading.Thread(target=generar)
hiloLector = threading.Thread(target=leer)

hiloGenerador.start()
hiloLector.start()

# sin quitar los join = 20 sec
# quitar los join = 20 sec

# El hilo padre sigue ejecutando, lanza los hilos (pero continua),
# muere el padre. Los hilos hijos luego mueren. Perdemos el
# control de los hilos.

hiloGenerador.join()
hiloLector.join()

# while hiloLector.is_alive():
#   print("Lector alive")
#  time.sleep(1)

# while hiloGenerador.is_alive():
#   print("Generador alive")
#  time.sleep(1)

print("El resultado final es una lista con:\n")
print(lista)
