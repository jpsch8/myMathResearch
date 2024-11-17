# find zeros of zeta function
import time
from time import sleep
import cmath
#establishes complex variable (a+bi)

# real part (always 1/2)
x = 0.5
# compley part
y = 0
z = complex(x,y)

sum  = 0
while 1==1:

    for i in range(1,999999):
        sum = sum+(1/(i**z))

    print(sum)
    #increments complext part
    y = y+0.000001
    sleep(1)




