# we still don't know where this comes from



import math
from math import *

def lapSuc(n,m): # function for laplace succesion, takes in number of wins and losses
    return((n+1)/(n+m+1)) # simulates an extra loss and win and calculates the odds of winning the next trial

wins = int(input("wins_"))
losses = int(input("losses_"))

print(lapSuc(wins,losses)) # prints the results







# perhaps it came to me in a dream
