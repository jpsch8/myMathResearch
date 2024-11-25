# find zeros of zeta function


import cmath
#establishes complex variable (a+bi)

# real part (always 1/2)
x = 0.5
# complex part
y = 0
z = complex(x,y)

sum  = 0
while 1==1:

    for i in range(1,999999):
        sum = sum + ((-1)**(i-1))/(i**z)

    
    # increments complext part
    y = y+0.000001
    #checks if z is a zero (or really close to 0)
    if abs(sum)<0.000001:
        print(z)




