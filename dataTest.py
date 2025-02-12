import math
from math import *

def centre(S): # passes in an array of arrays ((x,y) coordinates of data)
    # sets a each component to 0
    x_coord = 0 
    y_coord = 0
    for i in range(0,len(S)):
        x_coord = x_coord + S[i][0] # adds up all the x components

    for j in range(0, len(S)):
        y_coord = y_coord + S[j][1] # adds up all the y components


    return [x_coord/len(S),y_coord/len(S)] # returns an array that represents a singal point, the average of the x and y componenets respectively


S = [[1,2],[2,3],[3,2],[4,6],[5,17]]
print(centre(S))


def move(S,p): # changes the data to centre around the origin
    new_S = [] # establishes a new set to recentre the data

    for i in range(0,len(S)): # iterates through each coordinate in the original data set
        new_S.append([float(S[i][0]-p[0]),float(S[i][1]-p[1])]) # subtracts the origin direction component from the direction component and adds that to a new set

    return new_S # returns the new set


def Rsquared(S,a,b): # this is not done yet
    return 0
print("ax + b")

a = float(input("a ="))
b = float(input("b ="))
