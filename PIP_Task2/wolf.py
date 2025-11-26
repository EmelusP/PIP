import math


class Wolf:

    def __init__(self):
        self.place = [0, 0]
        self.speed = 1

    def move(self, sheeps):
        closest_dist = float("inf")
        closest_sheep = None

        for i, sheep in enumerate(sheeps):
            if sheep is None:
                continue
            else:
                dx = self.place[0] - sheep.place[0]
                dy = self.place[1] - sheep.place[1]

                distance = dx ** 2 + dy ** 2
                if distance < closest_dist:
                    closest_dist = distance
                    closest_sheep = i

        if closest_sheep is None:
            return None, False

        closest_dist_sqrt = math.sqrt(closest_dist)

        dir_x = sheeps[closest_sheep].place[0] - self.place[0]
        dir_y = sheeps[closest_sheep].place[1] - self.place[1]

        if (closest_dist_sqrt <= self.speed):
            self.place = sheeps[closest_sheep].place
            sheeps[closest_sheep] = None
            return closest_sheep, True

        elif closest_dist > 0:
            self.place[0] += dir_x / closest_dist * self.speed
            self.place[1] += dir_y / closest_dist * self.speed

        return closest_sheep, False

    def get_place(self):
        return f"Wolf is at {round(self.place[0], 3)}, {round(self.place[1], 3)}"
    #def __str__(self):
    #    pass
    #str(wolf)
