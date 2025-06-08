import math
from math import *

# this is the euler phi function
def phi(n):
    sum = 0 # starts a sum at 0
    for i in range(1,n): # checks every natural number between 1 and n inclusive
        if gcd(i,n) == 1: # checks to see if the ith natural number is mutually prime with n
            sum = sum + 1
    return sum # returns the amount of numbers between 1 and n inclusive that are mutually prime with n


print(phi(3)) # calls the phi function
