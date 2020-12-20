#!/usr/bin/python3

import copy
import math

from pprint import pprint

def readone(f):
    # parse one tile

    h = f.readline()
    h = h.strip('\n\r:')
    myid = int(h.split()[1])

    A = list()
    # then read the 10 lines
    for i in range(0,10):
        A.append(f.readline().strip('\n\r').replace("#","1").replace(".","0"))


    # process a signature for each tile

    ll = "".join([x[9] for x in A])
    lr = "".join([x[0] for x in A]) 
    
    top = int(A[0],2)
    bottom = int(A[9],2)
    left = int(ll,2)
    right = int(lr,2)

    rtop = int(A[0][::-1],2)
    rbottom = int(A[9][::-1],2)
    rleft = int(ll[::-1],2)
    rright = int(lr[::-1],2)
    
    # and discard final empty line
    f.readline()
    
    return (myid, top,bottom,left,right,rtop,rbottom,rleft,rright)

def fliphoriz(tile):

    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, rtop, rbottom, right, left, top, bottom, rright, rleft)

def flipvert(tile):

    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, top, bottom, rleft, rright, rtop, rbottom, left, right)

def rot90(tile):
    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, left, right, rtop,rbottom,rleft,rright, top ,bottom)

def rot180(tile):

    return(rot90(rot90(tile)))

def rot270(tile):

    return(rot90(rot180(tile)))

def getpix(fname):
    with open(fname,"r") as fd:
        pics = list()
        try:
            while True:
                pics.append(readone(fd))
        except:
            pass

        return pics


hl = getpix("input.short")

#print(hl[0])
#print(rot90(rot270(hl[0])))

def tlist(tile):

    return [tile, rot90(tile), rot180(tile), rot270(tile), flipvert(tile), fliphoriz(tile)]

def ismatch(ta, tb):
    #(myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile
    
    return (ta[1]==tb[2] or ta[2] == tb[1] or ta[3] == tb[4] or ta[4] == tb[3])

def matches(tile, hl):

    if len(hl) == 0:
        return []

    ml = list()
    
    for i in hl:

        ri = tlist(i)

        for j in ri:

            if ismatch(tile, j):
                ml.append(j)

    return (ml)



print(hl[0])
ml = list()

for i in hl:
    x = copy.copy(hl)
    x.remove(i)
    p = matches(i,x)
    ml.append((i,len(p),p))
    

ml = sorted(ml, key=lambda x:-x[1])
#pprint (ml)

psize = int(math.sqrt(len(ml)))
middle= psize // 2 + 1
print ("PSize: "+str(psize)+" x "+str(psize) + ", c = ("+str(middle)+", "+str(middle)+")")

print(ml[0][0])

populatematrix(middle, middle, ml[0][0])


    
