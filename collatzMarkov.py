import math
from math import *

n = int(input("Enter a number"))

while n!=1:
    if n%2 == 0:
        print("A")
        n = n/2
    else:
        print("B")
        n = (3*n)+1