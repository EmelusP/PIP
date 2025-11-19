from time import sleep

from wolf import wolf
from sheep import sheep

num_of_sheeps = 2

wolf = wolf()
sheeps = []
for i in range(num_of_sheeps):
    sheeps.append(sheep())

while(True):
    for i in range(num_of_sheeps):
        sheeps[i].move()
        print(sheeps[i].get_place())

        wolf.move(sheeps)
        print(wolf.get_place())
        sleep(1)