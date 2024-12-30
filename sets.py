
def union(A,B):
    return 0

def intersect(A,B):
    antiUnion = []
    for i in range(0,len(A)):
        if A[i] in B:
            antiUnion.append(A[i])
    return antiUnion





A = [1,2,3,4,5]
B = [2,4,6,8]
print(intersect(A,B))
