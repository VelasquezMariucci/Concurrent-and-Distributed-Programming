import random
import threading
import time

threads = []

mutex = threading.Lock()

path = r"C:\Users\esvel\OneDrive\Desktop\Code\Python\MutexTest\output.txt"


def escritor(nombre):
    global path

    print("El path es", path, "y soy ", nombre)

    with mutex:
        for a in range(10):
            arch = open(path, "+a")
            arch.writelines(
                "Soy" + str(nombre) + " -> " + "estoy escribiendo " + str(a) + "\n"
            )
            segs = random.randint(1, 5)
            arch.close()
            time.sleep(0.01)


print("vamos a escribir con varios hilos")

for i in range(30):
    nombre = f"Hilo-{i+1}"
    thread = threading.Thread(target=escritor, args=(nombre,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Todos los hilos han terminado de escribir.")

