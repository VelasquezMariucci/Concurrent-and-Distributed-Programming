# Simple problem - you have one loop that prints odd numbers ( 1,3,5... ) 
# and another one that prints even numbers ( 0,2,4... ). Use mutex in these 
# loops to "sync" them such that the program prints 0,1,2,3,4,5....

import threading
import time

mutex = threading.Lock()

par = True

def pares():
    global par
    
    count = 0
    while True:
        if par == True:
            if mutex.acquire():
                print(count) 
                count = count + 2
                time.sleep(2)
                par = False
                mutex.release()
                
            else:
                print("Par Mutex ocupado")
                time.sleep(2)
     
            
def impares():
    global par
    
    count = 1
    while True:
        if par == False:
            if mutex.acquire():
                print(count) 
                time.sleep(2)
                count = count + 2
                par = True
                mutex.release()
              
            else:
                print("Impar Mutex ocupado")
                time.sleep(2)


hiloPar = threading.Thread(target=pares)
hiloImpar = threading.Thread(target=impares)  

hiloPar.start()
hiloImpar.start()

hiloPar.join()
hiloImpar.join()