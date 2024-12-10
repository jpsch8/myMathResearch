import random 
import time
from time import *

price = 50 # the price of the stock starts at 50
money = 10000 # this is the intital amount of money to start with
shares = 0 # starting at 0 shares
for i in range(0,365): # the loop runs 365 times for 365 days (should probably change this)
    change = random.randint(-3,3) # this is the discrete random variable for the stock price it can change by a maximum magnitude of 3
    price = price + change # this sets the new price
    print('money: $' + str(money))
    print("shares: " + str(shares))
    print("price of stock:" + str(price))
    print(" " )

    sleep(0)
    if money == 15000: # the loop stops at 15000 or when 33% is made
        break
    if price <= 0: # the algorithm stops trading at 0 dollars (should probalby increase this bound to avoid bankruptcy)
        break
    elif change > 0 and shares >=1: # if the price increases the algorithm sells 1 share
        shares = shares - 1
        money = money + price

    elif change < 0 and money >= price: # checks if the price went down and there is enough money in the account to buy a stock then if conditions are met a share is bought
        money = money - price
        shares = shares + 1
print(money-10000) # at the end the print statement shows how much profit was made (you start 10000 in the negative)


