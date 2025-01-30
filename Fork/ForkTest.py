import multiprocessing
from multiprocessing.dummy import freeze_support
import threading
import time

GLOVAR = 10  

def func():
    global GLOVAR
    GLOVAR += 1  
    print(f"GLOVAR in process: {GLOVAR}")
    

if __name__ == '__main__':
    GLOVAR = 20
    
    freeze_support()
    
    P1 = multiprocessing.Process(target=func) 
    
    P1.start()
    P1.join()

    print(f"GLOVAR in main: {GLOVAR}")
