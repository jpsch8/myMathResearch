import math
from math import *

def call(N,S,K,r,t,sigma):
    d1 = (math.log(S/K)+(r+((sigma)**2)/2)*t)/(sigma*(t**0.5))
    d2 = d1-sigma*(t**0.5)
    return N*d1*S-N*d2*K*(e**(-1*r*t))

N = float(input("CDF of the normal distribution")
S = float(input("spot price of an asset")
K = float(input("strike price")
r = float(input("risk-free interest rate")
t = float(input("time to maturity")
sigma = float(input("volatility of the asset")
          

print("Call price is ",end="")
print(call(10,11,10,10,10,10))
