# En una cadena de montaje existe un robot encargado de colocar productos de 3 tipos diferentes 
# (1, 2 o 3) en la cadena de montaje. Otros robots, retiran los productos de la cadena de montaje 
# para realizar su empaquetado, teniendo en cuenta que están especializados en un solo tipo de producto 
# (1, 2 o 3), ignorando los que no son de su tipo. Finalmente, se quiere llevar un control del total de 
# productos empaquetados (independientemente de su tipo).
import threading
import time
import random
from queue import Queue

mutex = threading.Lock()

productosEmpaquetados = []

cadenaMontaje = Queue(10)

empacarSem = threading.Semaphore(3)

def producir():
    global cadenaMontaje
    
    while True:
        print(list(cadenaMontaje.queue))
        print(productosEmpaquetados)
        
        producto = ""
        
        num = random.randint(1, 3)
        
        if (num == 1):
            producto = "Tornillo"
        elif (num == 2):
            producto = "Clavo"
        else:
            producto = "Chazo"
        
        print("Robot productor ha producido " + producto)
        
        time.sleep(3)
        
        cadenaMontaje.put(producto)
        empacarSem.release()


def empacar(tipo_producto):
    global cadenaMontaje
    global productosEmpaquetados
    
    while True:
        global cadenaMontaje
        global productosEmpaquetados
        
        empacarSem.acquire()
        
        producto = cadenaMontaje.get()
        
        if producto == tipo_producto:
            print("El robot empaqueta " + producto)
            productosEmpaquetados.append(producto)
            cadenaMontaje.task_done()
            time.sleep(2)
        else:
            print("El robot ignoro " + producto)
            cadenaMontaje.put(producto)
            
        time.sleep(2)
            
        
        
robotProd = threading.Thread(target=producir)
        
robot1 = threading.Thread(target=empacar, args=("Tornillo",))
robot2 = threading.Thread(target=empacar, args=("Clavo",))
robot3 = threading.Thread(target=empacar, args=("Chazo",))

robotProd.start()
robot1.start()
robot2.start()
robot3.start()
    
    
robotProd.join()
robot1.join()
robot2.join()
robot3.join()