import random
import time
from time import sleep

step = random.randint(-1,1)
print(step)

x = 0
y = 0
area = 0
while True:
    step = random.randint(-1, 1)
    x = x+1
    y = y+step
    if y>0:
        area = area + (y-(step/2))
        print(x,y,area)
    elif y<0:
        area = area-(y-(step/2))
        print(x,y,area)
    else:
        area = area-(step/2)
        print(x,y,area)
    sleep(1)







