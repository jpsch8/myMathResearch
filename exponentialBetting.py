# Thank you professor Swihart
# libraries that are used
import time
from time import sleep
import math
from math import *
import random
money = 100 # sets the inital capital (you need alot of this for it to work in real life)
k = 0

while money>0: # basically this is a valid strategy while you still have some amount of money
    coin = random.randint(0, bound) # makes a coin, 1 is a win state, else is a lose state 

    # (discrete random variable)


    if coin == 1: # you win if the coin is a 1
        money = money +(2**k) # adds to money
        print(money)
        k = 0 # restarts the exponent to 0
        sleep(1)
    else: # you lose if the coin lands on any integer that is not 1
        money = money - (2**k) # subtracts from money
        k = k+1 # increases the exponent by 1 (after an infinite amount of time you are guaranteed to net gain one dollar)
        print(money)
        sleep(1)
print("you lost all your money") # this happens if your capital goes to 0 (which is why you need to have alot to start with)
