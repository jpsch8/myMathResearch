# Thank you proffesor Swihart
import time
from time import sleep
import math
from math import *
import random
money = 100
k = 0
while money>0:
    coin = random.randint(0, 1)


    if coin == 1:
        money = money +(2**k)
        print(money)
        k = 0
        sleep(1)
    else:
        money = money - (2**k)
        k = k+1
        print(money)
        sleep(1)
print("you lost all your money")
