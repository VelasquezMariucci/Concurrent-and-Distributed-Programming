import time 
import threading


start = time.time()

SLEEP = 10

hilos = []

def esperar(sec):
    threadingName = threading.current_thread().name
    print("Thread name: " + threadingName + " ---> A dormir...")
    time.sleep(sec)
    print("Thread name: " + threadingName + " ---> A despertar...")
    

for i in range(0, 5):
    h = threading.Thread(target=esperar, args=(SLEEP))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

end = time.time()

print("Tiempo de total: " + str(end - start))