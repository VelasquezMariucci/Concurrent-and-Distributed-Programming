# Cinco filósofos, que representan procesos o hilos de ejecución, están 
# sentados a una mesa circular (Figura 5). Los filósofos en silencio piensan y
# luego comen, y repiten esta rutina eternamente. Ante cada filósofo se 
# encuentra un plato, y al centro de la mesa un tazón con infinito 
# abastecimiento de espagueti. Este abastecimiento representa un recurso 
# compartido, como una cinta magnética en el problema original. dining 
# philosophers Para poder comer espagueti, en la mesa están dispuestos 
# cinco tenedores (forks) o palillos chinos en el problema original 
# (chopstiks). Tanto los filósofos como los palillos están enumerados 
# de 0 a 4 como se ve en la figura Figura 5. Para poder comer, un filósofo i
# necesita los dos palillos (get chopstick), uno a su mano izquierda 
# (i + 1) y el otro a su mano derecha (i), y no los comparte mientras está 
# comiendo. Una vez que haya terminado de comer, el filósofo lava los tenedores
# y los coloca de regreso en sus posiciones en la mesa (put chopstick). Un 
# filósofo nunca sabe cuándo otro va a comer o pensar. El reto es construir un 
# algoritmo que permita a los filósofos eternamente pensar y comer que cumpla 
# los siguientes tres requerimientos: Los filósofos no se detengan de pensar y
# comer (bloqueo mutuo o deadlock). Ningún filósofo muera de hambre esperando 
# por un palillo (inanición o starvation). Dos o más filósofos puedan comer al
# mismo tiempo (concurrency). Los filósofos ya saben cómo realizar las 
# operaciones de pensar think() y comer eat(), ninguna de las dos dura 
# eternamente, y se debe detener a un filósofo mientras las realiza.

import threading
import time
import random

filosofos = []

espaguetti = threading.Lock()

forks = [1,2,3,4,5]

forksSem = threading.Thread(5)

def pensarYComer():
    