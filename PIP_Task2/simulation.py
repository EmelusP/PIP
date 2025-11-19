import random
from time import sleep

from sheep import sheep

sh = sheep()

while(True):
    print(sh.get_place())
    sh.move()
    sleep(1)