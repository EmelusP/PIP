import random


class sheep:
    place = [0, 0]
    speed = 0

    def __init__(self):
        self.speed = 0.5
        self.place = [random.randint(-10, 10), random.randint(-10, 10)]

    def move(self):
        direction = random.randint(0,3)

        match direction:
            case 0:
                self.place[1] += self.speed
            case 1:
                self.place[0] -= self.speed
            case 2:
                self.place[1] -= self.speed
            case 3:
                self.place[0] += self.speed

    def get_place(self):
        return f"Place is {self.place}"


