# find zeros of zeta function


import cmath
#establishes complex variable (a+bi)

# real part (always 1/2)

# complex part
y = 0
z = complex(0.5,y)

sum  = 0
while True:

    for i in range(1,999999):
        # this is actually the Dirichlet-eta function
        sum = sum + ((-1)**(i-1))/(i**z)

    
    # increments complext part
    y = y+0.000001
    #checks if z is a zero (or really close to 0)
    if abs(sum)<0.000001:
        print(z)




