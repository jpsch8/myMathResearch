import math
from math import *
def phi(n):
    sum = 0
    for i in range(1,n):
        if gcd(i,n) == 1:
            sum = sum + 1
    return sum
print(phi(3))