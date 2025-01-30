import threading

hilos = []

suma = 0


def sumar(nombre):
    global suma

    for i in range(10):
        print("Soy " + nombre + " y sumo 1 a " + str(suma))
        suma = suma + 1


for i in range(5):
    nombre = f"Hilo-{i+1}"
    hilo = threading.Thread(target=sumar, args=(nombre,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado de escribir.")
