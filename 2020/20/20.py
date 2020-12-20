#!/usr/bin/python3

import copy
import math
import sys

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
    
    return (myid, (myid, top,bottom,left,right,rtop,rbottom,rleft,rright))

def getpix(fname):
    with open(fname,"r") as fd:
        pics = dict()
        
        try:
            while True:
                t = readone(fd)
                #pprint(t)
                pics[t[0]] = t[1]
        except:
            pass

        return pics




def fliphoriz(tile):

    (picid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (picid, rtop, rbottom, right, left, top, bottom, rright, rleft)

def flipvert(tile):

    (picid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (picid, top, bottom, rleft, rright, rtop, rbottom, left, right)

def rot90(tile):
    (picid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (picid, left, right, rtop,rbottom,rleft,rright, top ,bottom)

def rot180(tile):

    return(rot90(rot90(tile)))

def rot270(tile):

    return(rot90(rot180(tile)))



def ismatch(ta, tb):
    #(myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile
    
    return (ta[1]==tb[2] or ta[2] == tb[1] or ta[3] == tb[4] or ta[4] == tb[3])

def tlist(tile):

    return [tile, rot90(tile), rot180(tile), rot270(tile), flipvert(tile), fliphoriz(tile)]

def matches(tile, hl):

    if len(hl) == 0:
        return []

    ml = list()
    
    for i in hl:

        ri = tlist(hl[i])

        for j in ri:

            if ismatch(tile, j):
                ml.append(j[0])

    return (ml)


def fit(mat, x, y, psize, ml):

    # out of bounds
    if x < 0 or y < 0 or x>=psize or y>=psize:
        return []

    # check all populated boxen around this box

    pbox = [mat[(x,y)] for x in range(0,psize) for y in range(0,psize) if (x,y) in mat]
    print ("All placed around ("+str(x)+","+str(y)+") are "+str(pbox))

    
    

    
    

def populatematrix(mat,x,y,pic, hl, ml, unused, psize):

    print("Placing "+str(pic)+" at "+str(x)+","+str(y))
    mat[(x,y)] = pic
    unused.remove(pic)
    pprint(mat)
    print ("Potential matches: "+str(ml[pic]))

    bv = 0
    bm = 0

    # for each box that isn't populated in the list below,
    # find one that might fit, and put it there. Then descend on that box. 
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        tmat = copy.copy(mat)
        # only look at unpopulated
        if not (x+dx,y+dx) in tmat:
            candidates = fit(tmat, x+dx,y+dy, psize, ml)
        
        
        
                  
# ----- "main" ------
hl = getpix("input.short")
#print (hl)

ml = dict()

# find matching tiles for all tiles
for i in hl:
    # hl is now a dict
    x = copy.copy(hl)
    del x[i]
    p = matches(hl[i],x)
    ml[i]=(len(p),p)


mlkeys=ml.keys()
mlkeys = sorted(mlkeys, key=lambda x:-ml[x][0])
#pprint (mlkeys)

psize = int(math.sqrt(len(ml)))
middle= psize // 2 + 1
print ("PSize: "+str(psize)+" x "+str(psize) + ", c = ("+str(middle)+", "+str(middle)+")")

mat = dict()

populatematrix(mat, middle, middle, mlkeys[0], hl, ml, mlkeys, psize)


    
