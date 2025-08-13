import random
import time
# this simulation sets up a 1X1 square and a quarter circle with radius 1 and centre at the origin

hit = 0 # tracks when randomly selected point is inside the quarter circle
sum = 0 # tracks how many time we run the experiment 

while True:
    # chooses a random point in the unit square
    x = random.random()
    y = random.random()
    if ((x**2 + y**2) <= 1): # checks to see if the norm of the point is less than or equal to 1
        # increments the hit and sum value
        hit = hit + 1
        sum = sum + 1
    else:
        # only increments the sum value because randomly selected point is now within circle
        sum = sum + 1
    print((hit/sum)*4) # we multiply the ratio by 4 because if we do not, the sum approaches pi/4
    time.sleep(0.1) # the sleep call is just to see the raitio approach pi



