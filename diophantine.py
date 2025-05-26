# brute force algorithm for solving diophantine equations
# x^2 + 3x + 9 = 9y^2

def solve(x,y):
    if(x**2 + 3*x + 9 - 9 * y**2 == 0): # checks to see if the integer pair satisfies the equation
        print("(" + str(x) + ", " + str(y) + ")") # if it does, we print that pair to the console



    return 0
# this algorithm is terrible and needs adjustments
for i  in range(-999,999): # checks every x value on [-999,999]
    for j in range(-999, 999): # checks every y value on [-999,999]
        solve(i,j)
