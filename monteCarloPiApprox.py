import random
import time
hit = 0
sum = 0

while True:
    x = random.random()
    y = random.random()
    if ((x**2 + y**2) <= 1):
        hit = hit + 1
        sum = sum + 1
    else:
        sum = sum + 1
    print((hit/sum)*4)
    time.sleep(0.1)


