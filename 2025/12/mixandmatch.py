import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")
import itertools

gifts = []

with open("input.short") as fd:
    while True:
        b=readblock(fd)
        if not b:
            break
        
        if len(b)>1 and ("#" in b[1] or "." in b[1]):
            gifts.append([list(x) for x in b[1:]])
        else:
            boxen = b

#print(gifts,box)

# fit a single piece in the box centered on xy
def amatch(t, g):

    a = flatten(g)
    b = flatten(t)

    if len(a)!=9:
        raise ValueError

    
    for i,v in enumerate(a):
        if v=="#" and b[i]!=".":
            return False

    #print(a,b)

    return True

def toint(s):
    s=flatten(s)
    return eval("0b"+"".join(s).replace("#","1").replace(".","0"))
    
def makeallvariants(g):
    bobb=[g]

    for i in range(1,4):
        d = np.rot90(g,i)
        bobb.append(d)
        
    g = np.flip(g)
    for i in range(4):
        d = np.rot90(g,i)
        bobb.append(d)
            
    bobb = ["".join(flatten(x)) for x in bobb]
    bobb = SortedSet(bobb,key = toint)
    bobb = [list(itertools.batched(x,3)) for x in bobb]

    return bobb
            
# try fitting the thing in the thing
def fliptofit(board, gift, x, y):

    t = np.array(arrslice(board,x-1,y-1,x+1,y+1))
    g = np.array(gift)
    mek = []
    bobb = makeallvariants(g)
    babb = [x for x in bobb if amatch(t,x)]
#    print("ftfava","".join(flatten(flatten(babb))),len(babb))
    if not len(babb):
        return None
    else:
        return babb
    

# insert an image in the board
def pdraw(board, gift, x, y, gid=None):

    for x1 in range(3):
        for y1 in range(3):
            if gift[y1][x1]=="#":
                if not gid:
                    board[y-1+y1][x-1+x1]="#"
                else:
                    board[y-1+y1][x-1+x1]=chr(ord('A')+gid)

def perase(board, gift, x, y):

    for x1 in range(3):
        for y1 in range(3):
            if gift[y1][x1]=="#":
                board[y-1+y1][x-1+x1]="."
                
    

# try to fit one gift into one region, optimally
def trypiece(board, gift):

    # find all areas 3x3 in the board
    # then filter them for which of them
    # - have enough empty spaces to fit the gift

    mx = len(board[0])
    my = len(board)
    cnt = {}
    
    giftreqs=sum([1 for x in flatten(gift) if x=="#"])
#    print("zubava",giftreqs)
    for x in range(1,mx-1):
        for y in range(1,my-1):
            n = checkallpos(board, x, y, lambda h:h==".", diagonals=True)
#            print("zocalo",n)
            c = sum(n)+(board[y][x]==".")
            if c>=giftreqs:
                cnt[x,y] = c

    cnt=dict(sorted(cnt.items(), key=lambda item: item[1]))
#    print(cnt)

    # c is the list of locations that at least have a theoretical chance to place the boxes at
    # now check if it really can be placed there. 

    borkum={}
#    print("ZAVAV",cnt)
#    if cnt=={}:
#        pprint(board)
        
    for x,y in cnt:
        m = fliptofit(board, gift, x, y)
        borkum[x,y] = m

    return borkum
        
    
def pwg(gift1, gift2):

    # start by creating all variants of both gifts

    g1 = makeallvariants(gift1)
    g2 = makeallvariants(gift2)

    # then match the pieces to each other.

    
    possiburu={}
    for a in g1:
#        print(a)
        ia = toint(a)
        for b in g2:
            ib = toint(b)
            box = np.full((7,7),".")
            pdraw(box,a,3,3)
            m = trypiece(box, b)
            #            for x,y in m:
            #                pdraw(box,b,x,y,1)
            #                pprint(box)
            #                perase(box,b,x,y)
            if len(m):
                for x,y in m:
                    if not (ia,ib) in possiburu:
                        possiburu[(ia,ib)]=[]
                    possiburu[(ia,ib)].append((x-3,y-3))
#                    if (x,y)==(1,1):
#                        pdraw(box, b, x, y, 2)
#                        pprint(box)
#                        perase(box,b,x,y)

    return possiburu

def mam(gifts):
    kombu={}
    bungo={}

    for i in range(len(gifts)):
        bungo[i]=[toint("".join(flatten(x))) for x in makeallvariants(gifts[i])]
        for j in range(len(gifts)):        
            kombu|=pwg(gifts[i],gifts[j])

    return (kombu, bungo)

kombu,bungo=mam(gifts)
        
#for x in kombu:
#    print("kombu=",kombu)

#print("bungo=",bungo)

# now try to pack the packages

# box - box to put things in
# gift - an item to place

def canplace(box, kombu, g, x, y):
    if box[y][x]!=0:
        return False

    dog={}
    for xx in range(-2,3):
        for yy in range(-2, 3):
            if (xx,yy)!=(0,0):
                print(xx,yy)
                # collect all positions around the proposed placement that DO NOT contain an empty space.
                if checkpos(box,xx+x,yy+y, fun=lambda x:x!=0):
                    dog[xx,yy]=box[yy+y][xx+x]

                # vacuously true
                if not len(dog):
                    return True

    print(dog)

def placeone(box, kombu, g):

    print(g)
    for x in range(len(box[0])):
        for y in range(len(box)):
#            print(x,y)

            t = canplace(box, kombu, g, x, y)
            if t:
                box[y][x]=g
                print("-")
                pprint(box)
                print("-")
                return
    

def fillerup(box, kombu, bungo):
    box = box.split(" ")
    print(box)
    x,y=ints(box[0])

    tree = np.full((x-2,y-2),0)
    t = box[1:]

    targ = []
    
    for i,v in enumerate(t):
        v=int(v)
        if not v:
            continue
        
        print(i,v,bungo[i])
        for x in range(v):
            targ.append(bungo[i])

    print(targ)

    print(bungo)
    placeone(tree, kombu, bungo[0][0])
    
    
#pprint(kombu)
fillerup(boxen[0], kombu, bungo)


    


