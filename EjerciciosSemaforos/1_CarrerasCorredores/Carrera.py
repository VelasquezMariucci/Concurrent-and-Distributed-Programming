# 1. Simula una carrera de hilos en Python. Crea varios hilos que representan corredores en una pista y haz que
# compitan para llegar a la línea de meta. Utiliza mecanismos de sincronización para asegurarte de que los hilos
# compitan de manera justa y que solo uno pueda ganar la carrera (hecho en clase).

import threading
import random
import time

from Corredor import Corredor

class Main:
    listaCorredores = []

    def __init__(self):
        numeroDeCorredores = int(input("¿Cuantos corredores quieres?: "))

        for i in range(numeroDeCorredores):
            self.listaCorredores.append(Corredor())

        for corredor in self.listaCorredores:
            print(corredor)

        self.comenzarCarrera()

    def comenzarCarrera(self):
        print("Race started")
        threads = []
        winner = threading.Event()

        def race(corredor):
            while not corredor.finished: 
                corredor.correr()
                print("Corredor " + str(self.listaCorredores.index(corredor) + 1) + ": " + str(corredor.getPosition()))

                if corredor.getPosition() >= 100:
                    corredor.finished = True
                    print("Corredor " + str(self.listaCorredores.index(corredor) + 1) + ": ha terminado con una posicion de "  + str(corredor.getPosition()))

                time.sleep(0.5)  


        for corredor in self.listaCorredores:
            thread = threading.Thread(target=race, args=(corredor,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("Todos los corredores terminaron")


if __name__ == "__main__":
    main = Main()
