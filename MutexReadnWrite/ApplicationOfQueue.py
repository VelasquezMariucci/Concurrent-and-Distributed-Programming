import threading
import queue
import time

lista = []
mutex = threading.Lock()
myQueue = queue.Queue(maxsize=5)

numProducts = 20


def generar():
    global lista
    global myQueue

    for i in range(numProducts):
        if mutex.acquire(timeout=0.1):
            myQueue.put(i)
            mutex.release()
        else:
            print("El generador no ha podido escribir " + str(i))


def leer():
    global lista
    global myQueue

    while not myQueue.empty():
        print_queue_content(myQueue)

        if mutex.acquire(timeout=1):
            object = myQueue.get()
            lista.append(object)
            myQueue.task_done()
        else:
            print("El leer no ha sido posible")
            mutex.release()


def print_queue_content(q):
    temp_list = list(q.queue)
    print("Queue Content:", temp_list)


# no hay perdida de datos si no se libera la escritura? Si hay un bloqueo de retirada,
# no se podran añadir nuevos objetos

hiloGenerador = threading.Thread(target=generar, args=())
hiloLector = threading.Thread(target=leer, args=())

hiloGenerador.start()
hiloLector.start()

hiloGenerador.join()
myQueue.join()
hiloLector.join()

print("El resultado final es una lista con:\n")
print(lista)
