import cmath
from cmath import *

# takes imputs for numbers in the matrix
# must enter in for of a+bj
row1 = int(input("how many in row 1"))
col1 = int(input("how many in column 1"))
row2 = int(input("how many in row 2"))
col2 = int(input("how many in column 1"))

if row1 == row2 and col1 == col2: # checks to see if the dimensions are the same
    ASub = [] # makes a new matrix to do operations on
    print("Matrix A")
    for i in range(0,row1):
        for j in range(0, col1):
            print(i+1,j+1)
            something = complex(input("_")) # allows user to imput complex numbers into a matrix
            ASub.append(something) # adds the input to ASub

    BSub = []
    print("Matrix B")
    for i in range(0,row2):
        for j in range(0, col2):
            print(i+1,j+1)
            another = complex(input("_")) # allows user to add complex numbers into the B matrix
            BSub.append(another) # appends those complex inputs to the B matrix
    dot = 0

    for i in range(0,len(ASub)):
        dot = dot + (ASub[i]*BSub[i]) # sums up the multiples of each element in the matrix given the dimensions are the same












else:
    print("dot product is not computable, not same dimensions")
print(dot)
# this section is for calculating cross products if applicable
cross = []
if row1 and row2 == 3 and col1 and col2 == 1:
    cross.append(ASub[1]*BSub[2]-ASub[2]*BSub[1]) # finds the magnitude of i direction
    cross.append(ASub[2]*BSub[0]-ASub[0]*BSub[2]) # finds the magnitude of j direction
    cross.append(ASub[0]*BSub[1]-ASub[1]*BSub[0]) # finds the magnitude of k direction
    print("Cross product is ",end='')
    print(cross) # outputs the vector of the corss product


def matMul(mat1,mat2): # this is the matrix multiplication function
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))] # initializes a matrix of zeroes to add numbers to


    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j] # adds the product of the matrix multiplication to the result


    

    return result



mat1 = [[1,2,3],[4,5,6]]
mat2 = [[7,8],[9,10],[11,12]]
print(matMul(mat1,mat2))




