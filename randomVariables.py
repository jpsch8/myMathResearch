import time
from time import sleep
import random
from random import *
import math
from math import *
avgCase1 = 0
avgCase2 = 0
i = 1
print("MAX    SQRT   DIF")
while True:
    a = random()
    b = random()
    c = random()


    sleep(1)
    avgCase1 = avgCase1 + max(a,b)
    avgCase2 = avgCase2 + sqrt(c)
    print("{0:.3f}".format(avgCase1 / i), end=" ")
    print("{0:.3f}".format(avgCase2 / i), end=" ")
    print("{0:.3f}".format(abs((avgCase1 / i) - (avgCase2 / i))))

    i = i+1


