from turtledemo.penrose import inflatedart

from sheep import sheep

class wolf:
    place = [0, 0]
    speed = 1

    def __init__(self):
        self.place = [0, 0]
        self.speed = 1

    def move(self, sheeps):
        closest = float("inf")
        closest_sheep = 0
        for i in range(len(sheeps)):

            distance = (self.place[0] - sheeps[i].place[0]) + (self.place[1] - sheeps[i].place[1])
            if distance > closest:
                closest_sheep = i

        x_diff = self.place[0] - sheeps[closest_sheep].place[0]
        y_diff = self.place[1] - sheeps[closest_sheep].place[1]

        self.place[0] += 1 * (y_diff / x_diff)
        self.place[1] += 1 * (x_diff / y_diff)

    def get_place(self):
        return f"Wolf is at {self.place}"