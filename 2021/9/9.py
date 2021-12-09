#!/usr/bin/python3

import sys
from pprint import pprint

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

    print(x,y,c)


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

pprint(P)
print("Answer 1:",s)
