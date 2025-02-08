import math
from math import *

def centre(S):
    x_coord = 0
    y_coord = 0
    for i in range(0,len(S)):
        x_coord = x_coord + S[i][0]

    for j in range(0, len(S)):
        y_coord = y_coord + S[j][1]


    return [x_coord/len(S),y_coord/len(S)]


S = [[1,2],[2,3],[3,2],[4,6],[5,17]]
print(centre(S))


def move(S,p):
    new_S = []

    for i in range(0,len(S)):
        new_S.append([float(S[i][0]-p[0]),float(S[i][1]-p[1])])

    return new_S
