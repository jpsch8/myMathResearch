import math
from math import *

def call(N,S,K,r,t,sigma): # this function will give the call price
    d1 = (math.log(S/K)+(r+((sigma)**2)/2)*t)/(sigma*(t**0.5)) # this calculates the first part of the equation
    d2 = d1-sigma*(t**0.5) # this calculates the second part of the equation
    return N*d1*S-N*d2*K*(e**(-1*r*t)) # this returns the rest of the equation finally calculating the call price


# the following allows use to input the prametres : CDF of the normal distribution, spot price, strike price, risk-free interest rate, time to maturity and volatility
N = float(input("CDF of the normal distribution")
S = float(input("spot price of an asset")
K = float(input("strike price")
r = float(input("risk-free interest rate")
t = float(input("time to maturity")
sigma = float(input("volatility of the asset")
          

print("Call price is ",end="")
print(call(N,S,K,r,t,sigma)) # this calls the function to give call price
