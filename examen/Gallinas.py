import random
import threading
import time
import queue
import math

numGallinas = 5

eficiencia = 300/365

fertilidad = 0.02
maduracion = 140

gallinas = []

huevos = []

sinHuevos = []

criadero = queue.Queue()

criadero = queue.Queue()

semHuevos = threading.Semaphore()

semSinhuevos = threading.Semaphore()

semCriadero = threading.Semaphore()

maxDia = 365

def gallina(nombre, miDia):
    global criadero
    global huevos
    global sinHuevos
    global gallinas
    
    huevos.append(0)
    sinHuevos.append(0)
    
    while (miDia != maxDia):
        porcentajeHuevo = random.randint(1, 300)/365
        
        if (porcentajeHuevo > eficiencia):
            porcentajePollo = random.randint(1, 100)/100
            
            if (porcentajePollo <= 0.2):
                print("Gallina " + str(nombre) + " ha puesto pollo.")
                criadero.put(0)
            else:
                semHuevos.acquire()
            
                print("Gallina " + str(nombre) + " ha puesto huevo.")
            
                numHuevos = huevos.pop(nombre)
                numHuevos += 1
                huevos.append(numHuevos)
            
                semHuevos.release()
                
        else: 
            semSinhuevos.acquire()
            
            print("Gallina " + str(nombre) + " no ha puesto huevo.")
            
            numSinHuevos = sinHuevos.pop(nombre)
            numSinHuevos += 1
            sinHuevos.append(numSinHuevos)
            
            semSinhuevos.release()
            
        time.sleep(random.randint(1,3))
        miDia += 1
        
        
def pollitos():
    global criadero
    global gallinas
    global numGallinas
    
    while (True):
        if criadero.empty() == False:
            for i in criadero._qsize():
                pollo = criadero.get()
                
                if pollo == 140:
                    numGallinas += 1 
                    newGallina = threading.Thread(target=gallina, args=(numGallinas+1, 140))
                    gallinas.append(newGallina)
                    newGallina.start()
                else:
                    pollo += 1
                    criadero.task_done()
                    criadero.put(pollo)
   
   
def imprimir():
    global huevos
    global sinHuevos
    global numGallinas
    
    while True:
        time.sleep(2)
        
        semHuevos.acquire()
        semSinhuevos.acquire()
        
        print(huevos)
        print(sinHuevos)
        
        total = 0
        count = 0
        for i in huevos:
            total += huevos[count]
            count = count + 1
            
        total = total/numGallinas*365
        
        print(math.ceil(total))
        print(total)
        
        semHuevos.release()
        semSinhuevos.release()
        
   
criar = threading.Thread(target=pollitos)   
criar.start()     

imprimit = threading.Thread(target=imprimir)   
imprimit.start()          

for i in range(0, numGallinas):
    g = threading.Thread(target=gallina, args=(i, 0))
    gallinas.append(g)
    g.start()
        
        
        