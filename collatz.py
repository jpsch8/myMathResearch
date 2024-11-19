import time
from time import sleep

# sets variable
n = 1
def collatz(n):
    # the loop terminates at n = 1 because this is goes to 4,2,1 loop
    while n !=1:
        # checks if n is even
        if n % 2 == 0:
            n = n / 2
            print(n)

        checks if n i odd
        elif n % 2 == 1:
            n = n * 3 + 1
            print(n)
    return True






while True:
    # prints n and the steps to get there
    print(n,collatz(n))
    # increments n by 1
    n = n+1
    # allows for delay (just to see what is going on)
    sleep(1)







