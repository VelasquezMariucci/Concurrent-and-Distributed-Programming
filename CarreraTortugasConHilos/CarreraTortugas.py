import threading

from Turtle import Turtle


class Main:
    turtle_list = []

    def __init__(self):
        numberOfTurtles = int(input("How many turtles do you want?: "))
        
        for i in range(numberOfTurtles):
            self.turtle_list.append(Turtle())

        for turtle in self.turtle_list:
            print(turtle)

        self.start_Race()

    def start_Race(self):
        print("Race started")
        threads = []
        winner = threading.Event()

        def race(turtle):
            while any(not turtle.finished for turtle in self.turtle_list):
                count = 0

                for turtle in self.turtle_list:
                    if not turtle.finished:
                        turtle.moveTurtle()

                    print(f"{turtle}:  {turtle.getPosition()}")

                    if turtle.getPosition() >= 100 and not turtle.finished:
                        turtle.finished = True

                        if not winner.is_set():
                            print(f"{turtle} is the winner! " f"{turtle.getPosition()}")
                            winner.set()

        for turtle in self.turtle_list:
            thread = threading.Thread(target=race, args=(turtle,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("All turtles have finished the race.")


if __name__ == "__main__":
    main = Main()
