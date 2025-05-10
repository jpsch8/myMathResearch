import time
from time import sleep
import random
from random import *
import math
from math import *
# these are the 2 cases that we compare, avgCase1 is the max of 2 variables and avgCase2 is the square root of a random variable
avgCase1 = 0
avgCase2 = 0
i = 1
print("MAX    SQRT   DIF")
# iterates an infinite number of times to show convergence
while True:
    # makes a random variable on [0,1]
    a = random()
    b = random()
    c = random()


    sleep(1)
    
    # finds the max of the 2 variables and sums that to avgCase1
    avgCase1 = avgCase1 + max(a,b)
    # finds the square root of 1 variable and sums that to avgCase2
    avgCase2 = avgCase2 + sqrt(c)
    # we make the accuracy of output to 3 decimal places for ease of reading
    # also divides the sum by i to show the averages
    print("{0:.3f}".format(avgCase1 / i), end=" ")
    print("{0:.3f}".format(avgCase2 / i), end=" ")
    # finds the differences between taking max of 2 variables and taking the square root of 1 variable
    # this should go to 0
    print("{0:.3f}".format(abs((avgCase1 / i) - (avgCase2 / i))))
    # increments the number of tests to find the average
    i = i+1
    


