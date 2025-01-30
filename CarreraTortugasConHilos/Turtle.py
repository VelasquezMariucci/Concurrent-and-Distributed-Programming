import random

class Turtle:
    finished = False
    
    def __init__(self):
        self.position = 0

    def moveTurtle(self):
        self.position += random.randint(1, 10)

    def getPosition(self):
        return self.position