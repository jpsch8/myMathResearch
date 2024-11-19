import time
from time import sleep

n = 1
def collatz(n):
    while n !=1:
        if n % 2 == 0:
            n = n / 2
            print(n)

        elif n % 2 == 1:
            n = n * 3 + 1
            print(n)
    return True






while True:
    print(n,collatz(n))
    n = n+1
    sleep(1)







