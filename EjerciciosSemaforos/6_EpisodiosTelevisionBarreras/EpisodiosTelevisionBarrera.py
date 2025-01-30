import threading
import random
import time

personas = 5
temporadas = 9
episodios_por_temporada = 5
amigos = []
barrera = threading.Barrier(personas)
paImprimir = threading.Lock()


def imprimir(mensaje):
    with paImprimir:
        print(mensaje)


def verSerie(persona):
    for temporada in range(1, temporadas + 1):
        vistos = []
        for episodio in range(1, episodios_por_temporada + 1):
            ep_nombre = "Temporada " + str(temporada) + ", Episodio " + str(episodio)
            imprimir(persona + ": empiezo a ver " + ep_nombre)
            time.sleep(random.randint(1, 3))
            vistos.append(ep_nombre)
            imprimir(persona + ": he acabado de ver " + ep_nombre)
        imprimir(persona + " ha terminado la temporada " + str(temporada))

        barrera.wait()
        imprimir("Todos han terminado la temporada " + str(temporada) + "." + persona + " continua a la siguiente temporada.\n")


for i in range(1, personas + 1):
    amigo = threading.Thread(target=verSerie, args=(f"Persona_{i}",))
    amigos.append(amigo)
    amigo.start()


for amigo in amigos:
    amigo.join()

imprimir("Todos han terminado de ver la serie")
