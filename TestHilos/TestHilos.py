import threading
import time
import random

print("esta es mi app")

def demo():
    print("este ensaje es paraun funcion")

print("esta es mi app")

thread = threading.Thread(target=demo)

thread.start()

thread.join()

print("he salido la zona donde quiero invocar a la funcion")
