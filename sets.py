
def union(A,B): # this is the function to find the union of a ses
    oni = [] # this is the set we are going to return
    for i in range(0,len(A)): # this first loop is to avoid double counting
        if A[i] in B: # checks for elements in A that are in B
            oni.append(A[i])
    for i in range(0,len(A)):
        if A[i] not in oni: # Appends elements in A that have not been counted yet
            oni.append(A[i])
    for i in range(0,len(B)):
        if B[i] not in oni: # Appends elements in B that have not been counted yet
            oni.append(B[i])

    return oni # returns the union of A and B (AUB)

def intersect(A,B):
    interRet = [] # sets up the array we are going to return
    for i in range(0,len(A)): 
        if A[i] in B: # checks if an element in A is in B
            interRet.append(A[i]) # if an element in A is in B this appends that element to the intersetcion set
    return interRet # returns the intersection set


def difference(A,B):
    diffRet = A
    for i in range(0,len(B)):
        if B[i] in A:
            diffRet.remove(B[i])


    return diffRet


A = [1,2,3,4,5]
B = [2,4,6,8]
print(intersect(A,B))
print(union(A,B))
print(difference(A,B))
