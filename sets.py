
def union(A,B):
    oni = []
    for i in range(0,len(A)):
        if A[i] in B:
            oni.append(A[i])
    for i in range(0,len(A)):
        if A[i] not in oni:
            oni.append(A[i])
    for i in range(0,len(B)):
        if B[i] not in oni:
            oni.append(B[i])

    return oni

def intersect(A,B):
    antiUnion = []
    for i in range(0,len(A)):
        if A[i] in B:
            antiUnion.append(A[i])
    return antiUnion





A = [1,2,3,4,5]
B = [2,4,6,8]
print(intersect(A,B))
print(union(A,B))
