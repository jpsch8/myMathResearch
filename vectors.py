# takes imputs for numbers in the matrix
row1 = int(input("how many in row 1"))
col1 = int(input("how many in column 1"))
row2 = int(input("how many in row 2"))
col2 = int(input("how many in column 1"))

if row1 == row2 and col1 == col2:
    ASub = []
    print("Matrix A")
    for i in range(0,row1):
        for j in range(0, col1):
            print(i+1,j+1)
            something = float(input("_"))
            ASub.append(something)

    BSub = []
    print("Matrix B")
    for i in range(0,row2):
        for j in range(0, col2):
            print(i+1,j+1)
            another = float(input("_"))
            BSub.append(another)
    dot = 0

    for i in range(0,len(ASub)):
        dot = dot + (ASub[i]*BSub[i])












else:
    print("dot product is not computable, not same dimensions")
print(dot)
cross = []
if row1 and row2 == 3 and col1 and col2 == 1:
    cross.append(ASub[1]*BSub[2]-ASub[2]*BSub[1])
    cross.append(ASub[2]*BSub[0]-ASub[0]*BSub[2])
    cross.append(ASub[0]*BSub[1]-ASub[1]*BSub[0])
    print("Cross product is ",end='')
    print(cross)

