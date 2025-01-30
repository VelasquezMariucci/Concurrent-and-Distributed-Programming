import queue
import threading
import time
import random
from carro import carro  # Assuming 'carro' is a valid class with relevant methods.

class main:
    def __init__(self):
        # Initialize queues
        self.tramoA = queue.Queue(maxsize=5)
        self.tramoB = queue.Queue(maxsize=3)
        
        # Car list and threads list
        self.carros = []
        self.threads = []
        
        # Semaphore to allow 2 cars to move at a time
        self.semaforo = threading.Semaphore(2)

        # Create 5 cars
        for i in range(5):
            car_name = "Carro#" + str(i)
            car = carro(car_name, 0, 0)  # Assumed to have (name, speed, laps)
            self.carros.append(car)
            self.tramoA.put(car)  # Add the car to tramoA initially
        print("Cars created and added to tramoA.")

        # Create and start the crossing threads
        for car in self.carros:
            print(f"Starting thread for {car.inforArray[0]}")
            thread = threading.Thread(target=self.moverCarro, args=(car,))
            self.threads.append(thread)
            thread.start()

        # Create a thread for printing the state of the roads
        print_thread = threading.Thread(target=self.imprimirCallePeriodically)
        self.threads.append(print_thread)
        print("Starting the print thread.")
        print_thread.start()

    def moverCarro(self, car):
        while True:
            # Simulate random waiting before trying to cross
            time.sleep(random.uniform(1, 4))

            # Wait for the semaphore to allow crossing
            with self.semaforo:
                if not self.tramoA.empty():
                    # Move car from tramoA to tramoB if there is space
                    try:
                        car = self.tramoA.get_nowait()
                        if not self.tramoB.full():
                            print(f"{car.inforArray[0]} is crossing...")
                            self.tramoB.put(car)
                        else:
                            print(f"{car.inforArray[0]} cannot cross, tramoB is full!")
                            self.tramoA.put(car)  # Put the car back if tramoB is full
                    except queue.Empty:
                        print("No cars to move.")
    
    def imprimirCallePeriodically(self):
        while True:
            # Pause other threads when printing
            self.semaforo.acquire()  # Acquire semaphore fully to stop crossing
            self.imprimirCalle()  # Print the state of the roads
            self.semaforo.release()  # Release semaphore so cars can move again
            time.sleep(2)  # Print every 2 seconds

    def imprimirCalle(self):
        print("------------------Tramo A------------------")
        # Print cars in tramoA
        for car in list(self.tramoA.queue):
            print(car.inforArray[0])

        print("------------------Tramo B------------------")
        # Print cars in tramoB
        for car in list(self.tramoB.queue):
            print(car.inforArray[0])

if __name__ == "__main__":
    # Start the Main class
    main_program = main()

    # Keep the main thread running so that threads don't terminate
    for thread in main_program.threads:
        thread.join()  # Wait for all threads to finish
