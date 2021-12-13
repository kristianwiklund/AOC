#!/usr/bin/python3

import sys

def pr(W,mx,my):
    for y in range(my+1):
        for x in range(mx+1):
            if (x,y) in W:
                print("#",end='')
            else:
                print(" ",end='')
        print("")

                                                                    

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
            mmx = max(mmx,x)
            Z.add((x,y))
        mmy = my
    else:
        Z=set()

        for (x,y) in Q:
            # if above fold then
            # new position is
            # fold position minus distance from fold position

            if y>=p:
                y = p-(y-p)
            mmy = max(mmy,y)
            Z.add((x,y))
        mmx = mx
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
        
M = {}

for (x,y) in Q:

    M[x,y] = '1'

print("Answer 2:\n")
pr(M,mx,my)

