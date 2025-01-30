#1. Simula la carrera de hilos en Python, pero con procesos, utilizando como 
# medio de comunicación archivos de intercambio en lugar de sockets. Crea 
# varios procesos que representan corredores en una pista y haz que compitan 
# para llegar a la línea de meta. Como mecanismos de sincronización utiliza 
# archivos de texto como intercambiadores de información, para asegurarte de 
# que los hilos compitan de manera justa y que solo uno pueda ganar la carrera.
# Cada corredor escribirá en un archivo el número de la distancia que lleva 
# recorrida. El proceso padre, leerá el archivo de cada proceso de forma 
# regular, para saber el avance de cada corredor. Cada vez que lea un dato, 
# escribirá en el archivo una nueva línea con la palabra "LEIDO". Cada corredor, 
# cuando vaya a escribir su avance, buscará la palabra "LEIDO" y, si no aparece, 
# tendrá que cerrar el archivo y esperar a que el proceso padre lea la última 
# información del archivo y pueda escribirlo. Cuando un corredor escriba en el 
# archivo, lo vaciará primero, borrando la información anterior. Cada vez que 
# un proceso (padre o hijo) quiera escribir, deberá buscar primero si existe un
# archivo con el mismo nombre, pero con el prefijo "ESCRIBIENDO_" delante del 
# nombre de archivo. Cada proceso creará ese archivo al ir a escribir en el 
# archivo y lo borrará al terminar de escribir, por lo que si el archivo existe,
# el proceso que quiera leer o escribir del archivo con la distancia, tendrá que
# esperar a que el otro proceso termine de escribir.

import multiprocessing
from multiprocessing.dummy import freeze_support
import multiprocessing.process
import os
import random
import threading
import time

# Constantes Globales
META_FINAL = 100
DIR = "Resultados_Carrera"

# Variables Globales
numCorredores = 5
procesosCorredores = []

os.makedirs(DIR, exist_ok=True) # Esto me deja crear la direccion si no existe previamente

def correr(nombre, initPos):
    pos = initPos
    
    archivoPath = os.path.join(DIR, f"{nombre}.txt")
    archivoEscribiendo = os.path.join(DIR, f"ESCRIBIENDO_{nombre}.txt")
    
    archivo = open(archivoPath, "w")
    archivo.write("0\n")
    archivo.close()

    while pos < META_FINAL:
        if not os.path.exists(archivoEscribiendo):
            
            try:
                open(archivoEscribiendo, "w").close()
                
                archivo = open(archivoPath, "r")
                lineas = archivo.readlines()
                archivo.close()

                if lineas:
                    if lineas[-1].strip() == "LEIDO":
                        pos += random.randint(1, 15)
                        
                        archivo = open(archivoPath, "w")
                        archivo.write(f"{pos}\n")
                        archivo.close()

            finally: # Asegurarme que se borre el archivo lock 
                if os.path.exists(archivoEscribiendo):
                    os.remove(archivoEscribiendo)

        else:
            time.sleep(random.randint(0.5,2))


    print(f"{nombre} llego al final.")


if __name__ == "__main__":
    freeze_support() 
    
    carrera_terminada = False
    
    ganador = ""
    
    for i in range(0, numCorredores):
        p = multiprocessing.Process(target=correr, args=(f"Corredor_{i}", 0))
        procesosCorredores.append(p)
        
        p.start()

    while not ganador:
        for i in range(0, numCorredores):
            archivo_corredor = os.path.join(DIR, f"Corredor_{i}.txt")
            archivoEscribiendo_corredor = os.path.join(DIR, f"ESCRIBIENDO_Corredor_{i}.txt")

            if not os.path.exists(archivoEscribiendo_corredor):
                if os.path.exists(archivo_corredor):
                    
                    try:
                        archivo = open(archivo_corredor, "r")
                        lineas = archivo.readlines()
                        archivo.close()

                        if lineas:
                            ultima_linea = int(lineas[-1].strip())
                            
                            if ultima_linea >= META_FINAL:
                                ganador = f"Corredor_{i}"
                            
                                print(f"el ganador es {ganador}")
                                
                                
                            archivo = open(archivo_corredor, "a")
                            archivo.write("LEIDO\n")
                            archivo.close()
                            
                    except (ValueError, IndexError):
                        pass # Excepcion para manejar si los archivos no existen en el momento justo.

        time.sleep(random.randint(0.5,2))

    
    for p in procesosCorredores:
        p.join()

    print("Carrera finalizada.")
