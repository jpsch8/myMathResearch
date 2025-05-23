# brute force algorithm for solving diophantine equations
# x^2 + 3x + 9 = 9y^2

def solve(x,y):
    if(x**2 + 3*x + 9 - 9 * y**2 == 0):
        print("(" + str(x) + ", " + str(y) + ")")



    return 0
for i  in range(-999,999):
    for j in range(-999, 999):
        solve(i,j)
