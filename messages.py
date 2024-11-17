# find zeros of zeta function
import time
from time import sleep
import cmath
#establishes complex variable

x = 0.5
y = 0
z = complex(x,y)

sum  = 0
while 1==1:

    for i in range(1,999999):
        sum = sum+(1/(i**z))

    print(sum)
    y = y+0.000001
    sleep(1)




