from Turtle import Turtle


class Main:
    turtle_list = []

    def __init__(self):
        for i in range(4):
            self.turtle_list.append(Turtle())

        for turtle in self.turtle_list:
            print(turtle)

        self.start_Race()

    def start_Race(self):
        print("Race started")

        winner = False

        while any(not turtle.finished for turtle in self.turtle_list):
            count = 0

            for turtle in self.turtle_list:
                if not turtle.finished:
                    turtle.moveTurtle()

                print(f"{turtle}:  {turtle.getPosition()}")

                if turtle.getPosition() >= 100 and not turtle.finished:
                    turtle.finished = True

                    if not winner:

                        print(f"{turtle} is the winner! " f"{turtle.getPosition()}")
                        winner = True

        print("All turtles have finished the race.")


if __name__ == "__main__":
    main = Main()
