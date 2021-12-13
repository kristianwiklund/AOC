#!/usr/bin/python3

import sys
import numpy

def pr(W):
    W = numpy.transpose(W)
    for x in W:
        for y in x:
            if y==0:
                print(" ",end='')
            else:
                print(int(y),end='')
        print("")

                                                                    

#f = [t.strip().split(",") for t in sys.stdin]

Q = set()

# coordinates
mx=0
my=0
for t in sys.stdin:
    t = t.strip().split(",")

    if len(t)>1:
        Q.add((int(t[0]),int(t[1])))
        if int(t[0])>mx:
            mx=int(t[0])
        if int(t[1])>my:
            my=int(t[1])
    else:
        break

#print(Q)
# folds

def transform(Q,d,p):
    mmx=0
    mmy=0
    if d=='x':
        Z=set()

        for (x,y) in Q:
            # if above fold then
            # new position is
            # fold position minus distance from fold position

            if x>=p:
                x = p-(x-p)
            Z.add((x,y))        
    else:
        Z=set()

        for (x,y) in Q:
            # if above fold then
            # new position is
            # fold position minus distance from fold position

            if y>=p:
                y = p-(y-p)
            Z.add((x,y))
        
    for (x,y) in Z:
        mmx = max(mmx,x)
        mmy = max(mmy,y)

        
    return (Z,mmx,mmy)

c=False
for t in sys.stdin:
    t = t.strip().split(" ")

    if len(t) == 3:
        x = t[2].split("=")
        d = x[0]
        p = int(x[1])

        (Q,mx,my)=transform(Q,d,p)
    if not c:
        print("Answer 1: ",len(Q))
        c=True
        
M = numpy.zeros(shape=(mx+2,my+2))

for (x,y) in Q:

    M[int(x)][int(y)] = '1'

print("Answer 2:\n")
pr(M)

