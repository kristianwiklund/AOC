#!/usr/bin/python3

import sys
import numpy

def pr(W):
    W = numpy.transpose(W)
    for x in W:
        for y in x:
            if y==0:
                print(".",end='')
            else:
                print(int(y),end='')
        print("")

                                                                    

#f = [t.strip().split(",") for t in sys.stdin]

Q = list()

# coordinates
mx=0
my=0
for t in sys.stdin:
    t = t.strip().split(",")

    if len(t)>1:
        Q=Q+ [(int(t[0]),int(t[1]))]
        if int(t[0])>mx:
            mx=int(t[0])
        if int(t[1])>my:
            my=int(t[1])
    else:
        break

#print(Q)
# folds

def transform(Q,d,p):

    mmx=mx
    mmy=my
    if d=='x':
        Z=[]
        for (x,y) in Q:
            if x>p:
                x=mx-x+int((mx/2)-p)
            Z.append((x,y))

        mmx=p

    else:
        Z=[]
        for (x,y) in Q:
            if y>p:
                y=my-y+int((my/2)-p)
            Z.append((x,y))
        mmy=p
    return (Z,mmx,mmy)

for t in sys.stdin:
    t = t.strip().split(" ")

    if len(t) == 3:
        x = t[2].split("=")
        d = x[0]
        p = int(x[1])

        (Q,mx,my)=transform(Q,d,p)
 
    
#print(Q)



M = numpy.zeros(shape=(mx+1,my+1))
print(mx,my)
for (x,y) in Q:
    #print (x,y)
    M[int(x)][int(y)] = '1'

    
pr(M)
#print(sum(sum(M)))
