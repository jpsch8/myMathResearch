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
    # 0.75 is the expected value of this game
    # I think that after a bunch of turns the total money should be about 0
    money += 0.75
    print(money)
    sleep(1)

