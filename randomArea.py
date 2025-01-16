# this is a script that can find the area under some random step function

import random
import time
from time import sleep

step = random.randint(-1,1) # sets the step size
print(step)
# sets the starting point to the origin
x = 0
y = 0
# sets the initial area to 0
area = 0

while True: # runs forever (think as x approaches infinity)
    step = random.randint(-1, 1)# I don't know why this appears more than once, will fix later
    x = x+1 # constantly increments x by 1, important because it makes the system discrete
    y = y+step # increments the y coordinate by the step size
    if y!=0: # checks if y is not zer0
        area = area + (y-(step/2)) # think of adding some whole number of cubes +- a triangle, it took quite a while to derive this (I am not very good at math)
        
        print(x,y,area)# prints the coordinates and the area
    
    else: # I think zero is a special case but I could be wrong
        area = area-(step/2)
        print(x,y,area)
    sleep(1) # this is just here to see the system in more detail, things get too fast to see when it's removed






