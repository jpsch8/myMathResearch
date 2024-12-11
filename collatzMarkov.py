# representing the collatz conjecture as a markov chain was an idea that came to me in a dream


import math
from math import *

n = int(input("Enter a number")) # this allows you to put in a number to test the collatz conjecture

while n!=1:
    if n%2 == 0:
        print("A") # prints A if even
        n = n/2 # then divides n by 2
    else:
        print("B") # prints B if odd
        n = (3*n)+1 # then multiplies n by 3 and adds 1
