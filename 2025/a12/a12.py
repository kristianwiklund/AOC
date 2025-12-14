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

with open("input") as fd:
    while True:
        b=readblock(fd)
        if not b:
            break
        
        if len(b)>1 and ("#" in b[1] or "." in b[1]):
            gifts.append([list(x) for x in b[1:]])
        else:
            box = b

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
        
    

# q is a list of pieces to try
count=1

def doit(board, q, depth=1):
    global count
    
    if not len(q):
        return True

    #    count+=1
#    print(" "*depth,"ava",count, len(q))

    
    for i,g in enumerate(q):

        m = trypiece(board,g)
#        print(" "*depth,"vava",count, len(m))
        
        # m is a dict
        # if it is of zero length, we haven't found a single spot to put it

        if not m or not len(m):
            return False
        
        for key in m:
            if not m[key]:
                continue
            
            bobb=m[key]
            x,y=key
            
            # bobb contains all possible flips and rotations of the piece
            # babb contains which of these fits in the location
            # x,y is where we want to drop it

            #print("***",key,"-",bobb)
            for xb in bobb:
                pdraw(board, xb, x, y,count)
                count+=1
                res = doit(board, q[1:], depth+1)
                if res:
                    return True
                perase(board, xb,x,y)
                count-=1
            return False
            
    
# fit all gifts in one region (starting empty)
def fit(region, gifts):
    global count
    
    gifts=deepcopy(gifts)
    
    t = region.split(":")
    
    box = ints(t[0])
    reqs = ints(t[1])
    q = list()
    
#    print(box, reqs)

    
    board = [list("."*box[0]) for x in range(box[1])]

    for i,req in enumerate(reqs):
        if req:
            q+=[gifts[i]]*req

    count=1
    y= doit(board, q)
#    pprint(board)
    return(y)

res=[]
#for x in gifts:
#    print(len(makeallvariants(x[1:])))
print("-----------")
for x in box:
    m=fit(x,gifts)
    if m:
        print("+1")
    else:
        print(".")
    res.append(m)

print(sum(res))
        
