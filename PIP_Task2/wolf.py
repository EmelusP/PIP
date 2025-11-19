import math


class wolf:
    place = [0, 0]
    speed = 1

    def __init__(self):
        self.place = [0, 0]
        self.speed = 1

    def move(self, sheeps):
        closest_dist = float("inf")
        closest_sheep = -1

        for i in range(len(sheeps)):
            if sheeps[i] == None:
                continue
            else:
                dx = self.place[0] - sheeps[i].place[0]
                dy = self.place[1] - sheeps[i].place[1]

                distance = math.sqrt(dx ** 2 + dy ** 2)
                if distance < closest_dist:
                    closest_dist = distance
                    closest_sheep = i

        if closest_sheep == -1:
            return 0

        dir_x = sheeps[closest_sheep].place[0] - self.place[0]
        dir_y = sheeps[closest_sheep].place[1] - self.place[1]

        if (closest_dist < 1):
            self.place = sheeps[closest_sheep].place
            sheeps[closest_sheep] = None

        elif closest_dist > 0:
            self.place[0] += dir_x / closest_dist * self.speed
            self.place[1] += dir_y / closest_dist * self.speed


    def get_place(self):
        return f"Wolf is heeeereeee!!! {self.place} "
