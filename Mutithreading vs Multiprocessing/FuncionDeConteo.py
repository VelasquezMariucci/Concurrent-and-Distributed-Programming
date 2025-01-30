import time 
import threading

start = time.time()

COUNT = 200000000

hilos = []

def contar(n):
    threadName = threading.current_thread().name
    print(f"{threadName} \ ---> Empezamos a contar...")
    
    i = 0
    while i < n:
        i+=1
        
    print(f"{threadName} \ ---> Terminamos de contar...")
    

for i in range(2):
    h = threading.Thread(target=contar, args=(COUNT,))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

end = time.time()

print("Tiempo de total: " + str(end - start))