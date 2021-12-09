#!/usr/bin/python3

import sys
from pprint import pprint
import numpy

f = [t.strip() for t in sys.stdin]

M=[]
for i in f:
    M.append([int(x) for x in i])

def ismin(M,x,y):

    v = M[x][y]
    c = 0

    c = c + (1 if x-1>=0 and M[x-1][y]>v else 0)
    c = c + (1 if x+1<len(M) and M[x+1][y]>v else 0)
    c = c + (1 if y-1>=0 and M[x][y-1]>v else 0)
    c = c + (1 if y+1<len(M[0]) and M[x][y+1]>v else 0)

    c = c + (1 if x == 0 else 0)
    c = c + (1 if x == len(M)-1 else 0)
    c = c + (1 if y == 0 else 0)
    c = c + (1 if y == len(M[0])-1 else 0)

    return c==4

P = []
s = 0
for x in range(len(M)):
    t = []
    for y in range(len(M[x])):
        w = ismin(M,x,y)
        t.append(w)
        if w:
            s=s+M[x][y]+1
    P.append(t)

print("Answer 1:",s)

# Where P is true, we have a low point

def bh(X, T, x, y):

    if x<0 or y<0:
        return 0
    if(x>=len(X) or y>=len(X[x])):
        return 0
    
    if(T[x][y]):
        return 0

    if(X[x][y] == 9):
        return 0
    
    T[x][y] = True
    return bh(X, T, x-1, y) + bh(X, T, x+1, y) + bh(X, T, x, y-1) + bh(X, T, x, y+1)  + 1
    
def basin(X, x, y):
    T = numpy.array(X)
    T = T > 4711

    return bh(X, T, x, y)

t = [] 
for x in range(len(M)):
    for y in range(len(M[x])):
        if P[x][y]:
            t.append(basin(M, x, y))

t = sorted(t,reverse=True)

print("Answer 2:", t[0]*t[1]*t[2])
