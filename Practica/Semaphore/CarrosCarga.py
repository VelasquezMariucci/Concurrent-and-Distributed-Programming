# Cinco autos eléctricos necesitan cargar su batería en una estación de carga, 
# pero la estación solo tiene dos enchufes disponibles. Un auto no puede cargar 
# mientras no haya un enchufe libre. Una vez que termina de cargar, libera el 
# enchufe para que otro auto lo use.

import threading
import time
import random

cargadores = threading.Semaphore(2)

carros = []

def recargar(nombre):
    time.sleep(random.randint(1, 5))
    print("Carro " + nombre + " busca cargador.")
    
    cargadores.acquire()
    print("Carro " + nombre + " empieza a cargar.")
    time.sleep(random.randint(2, 5))
    cargadores.release()
    
    print("Carro " + nombre + " termina y se va.")
    

for i in range(0, 6):
    h = threading.Thread(target=recargar, args=(str(i)))
    carros.append(h)
    h.start()
    
for c in carros:
    c.join()
    