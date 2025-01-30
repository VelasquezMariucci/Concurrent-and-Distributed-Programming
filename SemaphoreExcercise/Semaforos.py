import threading

hilos = []

suma = 0

semaforo = threading.Semaphore(2)


def __init__(self):
    numberOfTurtles = int(input("How many turtles do you want?: "))
    
    for i in range(numberOfTurtles):
        self.turtle_list.append(Turtle())

    for turtle in self.turtle_list:
        print(turtle)

    self.start_Race()

def sumar(nombre):
    global suma

    for i in range(10):
        semaforo.acquire()
        try:
            print("Soy " + nombre + " y sumo 1 a " + str(suma))
            suma = suma + 1
        finally:
            semaforo.release()


for i in range(5):
    nombre = f"Hilo-{i+1}"
    hilo = threading.Thread(target=sumar, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado de escribir.")
