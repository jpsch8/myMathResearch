import math
from math import *

def call(N,S,K,r,t,sigma):
    d1 = (math.log(S/K)+(r+((sigma)**2)/2)*t)/(sigma*(t**0.5))
    d2 = d1-sigma*(t**0.5)
    return N*d1*S-N*d2*K*(e**(-1*r*t))




print(call(10,11,10,10,10,10))