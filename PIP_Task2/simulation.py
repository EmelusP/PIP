from time import sleep

from wolf import Wolf
from sheep import Sheep


def num_sheeps_allive(sheeps):
    sum = 0
    for i in range(len(sheeps)):
        if sheeps[i] != None:
            sum += 1
    return sum

num_of_sheeps = 2
max_num_of_rounds = 50

wolf = Wolf()
sheeps = []
for i in range(num_of_sheeps):
    sheeps.append(Sheep())

for j in range(max_num_of_rounds):
    for i in range(num_of_sheeps):
        if sheeps[i] != None:
            sheeps[i].move()

    ch_sheep = wolf.move(sheeps)


    print(f"Round number: {j}")
    print(wolf.get_place())
    print(f"Number of allive sheeps: {num_sheeps_allive(sheeps)}")
    if ch_sheep == -1:
        print("The wolf has eaten last sheep!")
    elif ch_sheep % 1 != 0:
        print(f"Wolf is chasing sheep nr: {int(ch_sheep)} ")
        print(f"Wolf has eaten sheep nr: {int(ch_sheep)}")
        if num_sheeps_allive(sheeps) == 0:
            print(f"Wolf has eaten all the sheeps!!\n End of the simulation")
            break
    else:
        print(f"Wolf is chasing sheep nr: {int(ch_sheep)} ")
    print(".\n.\n")

    sleep(1)