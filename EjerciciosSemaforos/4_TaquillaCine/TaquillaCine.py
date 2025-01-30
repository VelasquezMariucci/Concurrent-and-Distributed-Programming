# 4. Imagina una taquilla de cine que vende entradas para una película. Los clientes (hilos) llegan y desean comprar
# boletos, pero solo hay un número limitado de boletos disponibles. Utiliza un mutex (cerradura) para sincronizar la
# compra de boletos y asegurarte de que no se vendan más boletos de los disponibles.

import threading
import time
import random

boletosDisponibles = 15
clientes = []
num_clientes = 20
mutex = threading.Lock()


def comprarBoletos(nombre):
    global boletosDisponibles

    with mutex:
        if boletosDisponibles > 0:
            boletosDisponibles -= 1
            time.sleep(random.randint(1, 3))
            print(nombre + " ha comprado un boleto")
            print("Boletos restantes:" + str(boletosDisponibles))
        else:
            print(nombre + " no pudo comprar boleto")


for i in range(num_clientes):
    hilo = threading.Thread(target=comprarBoletos, args=(str(i),))
    clientes.append(hilo)
    hilo.start()


for hilo in clientes:
    hilo.join()

print("Venta de boletos finalizada")
