import random
import time
from time import sleep
money = 0
while True:
    numHeads = random.randint(0, 2)
    if(numHeads == 2):
        money -= 7
    elif(numHeads == 1 or numHeads == 0):
        money += 2
    print(money)
    sleep(1)

