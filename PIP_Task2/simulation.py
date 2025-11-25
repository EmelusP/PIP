import csv
import json
from time import sleep

from sheep import Sheep
from wolf import Wolf


def collect_round_data(round_no, wolf, sheeps):
    wolf_pos = (wolf.place[0], wolf.place[1])
    sheep_pos = []

    for sheep in sheeps:
        if sheep is not None:
            sheep_pos.append((sheep.place[0], sheep.place[1]))
        else:
            sheep_pos.append(None)

    return {
        'round_no': round_no,
        'wolf_pos': wolf_pos,
        'sheep_pos': sheep_pos
    }


def save_to_json(data_list):
    with open("pos.json", 'w') as file:
        json.dump(data_list, file, indent=4)
    print("Animal positions have been saved to pos.json.")


def save_to_csv(data_list):
    with open("alive.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
    print("The number of alive sheep has been saved to alive.csv.")


def num_sheeps_alive(sheeps):
    sum_of_alive_sheeps = 0
    for i in range(len(sheeps)):
        if sheeps[i] is not None:
            sum_of_alive_sheeps += 1
    return sum_of_alive_sheeps
#return sum(1 for sheep in sheeps if sheep is not None)


def run_simulation():
    num_of_sheeps = 15
    max_num_of_rounds = 50

    wolf = Wolf()
    sheeps = []
    json_data = []
    csv_data = []

    for i in range(num_of_sheeps):
        sheeps.append(Sheep())

    for j in range(max_num_of_rounds):
        for i in range(num_of_sheeps):
            if sheeps[i] is not None:
                sheeps[i].move()

        ch_sheep = wolf.move(sheeps)

        round_data = collect_round_data(j + 1, wolf, sheeps)
        json_data.append(round_data)

        csv_data.append([j + 1, num_sheeps_alive(sheeps)])

        print(f"Round number: {j + 1}")
        print(wolf.get_place())
        print(f"Number of alive sheeps: {num_sheeps_alive(sheeps)}")
        if ch_sheep == -1:
            print("The wolf has eaten last sheep!")
        elif ch_sheep % 1 != 0:
            print(f"Wolf is chasing sheep nr: {int(ch_sheep)} ")
            print(f"Wolf has eaten sheep nr: {int(ch_sheep)}")
            if num_sheeps_alive(sheeps) == 0:
                print(f"The wolf has eaten all the sheep!!\n  End of the simulation")
                break
        else:
            print(f"The Wolf is chasing sheep nr: {int(ch_sheep)} ")
        print(".\n.\n")

        #sleep(5)

    save_to_json(json_data)
    save_to_csv(csv_data)


run_simulation()
