import random
import time
from time import *

price = 50
money = 10000
shares = 0
for i in range(0,365):
    change = random.randint(-3,3)
    price = price + change
    print('money: $' + str(money))
    print("shares: " + str(shares))
    print("price of stock:" + str(price))
    print(" " )

    sleep(0)
    if money == 15000:
        break
    if price <= 0:
        break
    elif change > 0 and shares >=1:
        shares = shares - 1
        money = money + price

    elif change < 0 and money >= price:
        money = money - price
        shares = shares + 1
print(money-10000)


