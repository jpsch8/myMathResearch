# brute force algorithm for solving diophantine equations
# x^2 + 3x + 9 = 9y^2

def solve(x,y):
    if(x**2 + 3*x + 9 - 9 * y**2 == 0): # checks to see if the integer pair satisfies the equation
        print("(" + str(x) + ", " + str(y) + ")") # if it does, we print that pair to the console



    return 0
def linear(a,b,c): # passes in 3 number a,b,c and forms the equation ax+by=c
    if((c / math.gcd(a,b)) % 1 != 0): # checks if the gcd of a and b divides c, if it does then there is no soltion
        print("no solutions")
    else: # checks every possible solution on x,y[-1000,1000]
        for i in range(-1000, 1000):
            for j in range(-1000, 1000):
                if(a*i + b*j == c):
                    print("(" + str(i) + ", " + str(j) + ")")
        # this algorithm needs to change, it is way too slow
    return 0
# this algorithm is terrible and needs adjustments
for i  in range(-999,999): # checks every x value on [-999,999]
    for j in range(-999, 999): # checks every y value on [-999,999]
        solve(i,j)
linear(1,2,3)
