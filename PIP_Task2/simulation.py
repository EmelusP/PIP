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
        if sheeps[i] != None:
            sheeps[i].move()
            print(sheeps[i].get_place())

    if wolf.move(sheeps) == 0:
        print("Wszystkie owce zostały zjedzone!!!!!!!!!!!!!!!!!!")
        break

    print(wolf.get_place())
    sleep(1)