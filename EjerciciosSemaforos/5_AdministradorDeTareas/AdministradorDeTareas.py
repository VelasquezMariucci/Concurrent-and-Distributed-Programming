# 5. Desarrolla un administrador de tareas para un sistema operativo. Los procesos (tareas) se ejecutan de manera
# concurrente, y el administrador debe coordinar la ejecución de las tareas. Utiliza una cola (queue) para gestionar la
# ejecución de las tareas.
#
# En este ejercicio, debes implementar las siguientes funciones:
# agregar_tarea(nombre, duracion): Esta función agrega una nueva tarea a la cola de tareas pendientes. Debes
# especificar el nombre de la tarea y su duración estimada en segundos.
#
# ejecutar_tarea(): Esta función toma la tarea de mayor prioridad (aquella con la duración más corta) de la cola de
# tareas pendientes y la ejecuta. Debes simular la ejecución de la tarea mediante un retraso de la duración especificada.
#
# mostrar_tareas_pendientes(): Esta función muestra la lista de tareas pendientes en la cola.
#
# mostrar_tareas_completadas(): Esta función muestra la lista de tareas que han sido ejecutadas.
#
# Utiliza una cola para gestionar las tareas pendientes y asegurarte de que las tareas se ejecuten en el orden correcto,
# es decir, primero las tareas más cortas.

import time
import threading
import random
from queue import Queue

tareasPendientes = Queue()
tareasCompletadas = []

miMutex = threading.Lock()


def agregar_tarea(nombre):
    with miMutex:
        duracion = random.randint(5, 15)
        tareasPendientes.put((nombre, duracion))
        print(nombre + " agregada con duracion " + str(duracion) + " segundos")


def ejecutar_tarea():
    tarea_existe = True

    while tarea_existe:
        with miMutex:
            if tareasPendientes.empty():
                tarea_existe = False
            else:
                nombre, duracion = tareasPendientes.get()

        if tarea_existe:
            print("Ejecutando: " + nombre + ", duracion: " + str(duracion))
            time.sleep(duracion)
            with miMutex:
                tareasCompletadas.append((nombre, duracion))

            print(nombre + " completado")


def mostrar_tareas_pendientes():
    with miMutex:
        if not tareasPendientes.empty():
            print("Tareas pendientes:")
            for nombre, duracion in list(tareasPendientes.queue):
                print("\t" + nombre + ", duracion: " + str(duracion))
        else:
            print("No hay tareas pendientes")


def mostrar_tareas_completadas():
    with miMutex:
        if tareasCompletadas:
            print("Tareas completadas:")
            for nombre, duracion in tareasCompletadas:
                print("\t" + nombre + "duracion: " + str(duracion))
        else:
            print("No hay tareas completadas")


if __name__ == "__main__":
    agregar_tarea("Tarea A")
    agregar_tarea("Tarea B")
    agregar_tarea("Tarea C")

    hilo_ejecucion = threading.Thread(target=ejecutar_tarea)
    hilo_ejecucion.start()

    mostrar_tareas_pendientes()

    hilo_ejecucion.join()

    mostrar_tareas_pendientes()
    mostrar_tareas_completadas()
