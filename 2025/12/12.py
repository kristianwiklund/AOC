import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

gifts = []

with open("input.shorter") as fd:
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

    for i,v in enumerate(a):
        if v=="#" and b[i]!=".":
            return False

    return True

# try fitting the thing in the thing
def fliptofit(board, gift, x, y):

    t = np.array(slice(board,x-1,y-1,x+1,y+1))
    g = np.array(gift)

#    print(t,g)
    
    if amatch(t,g):
        print("0G")
        return g

    np.rot90(g)
    if amatch(t,g):
        return g

    np.rot90(g)
    if amatch(t,g):
        return g

    np.rot90(g)
    if amatch(t,g):
        return g

    return None
    

# insert an image in the board
def pdraw(board, gift, x, y):

    print("drawing",gift,"in",board)
    for x1 in range(3):
        for y1 in range(3):
            if gift[y1][x1]=="#":
                print(gift[y1][x1])
                board[y-1+y1][x-1+x1]="#"

    pprint(board)
    print("----------")
    

# try to fit one gift into one region, optimally
def trypiece(board, gift):

    # find all areas 3x3 in the board
    # then filter them for which of them
    # - have enough empty spaces to fit the gift

    mx = len(board[0])
    my = len(board)
    cnt = SortedDict()
    
    giftreqs=sum([1 for x in flatten(gift) if x=="#"])
    
    for x in range(1,mx-1):
        for y in range(1,my-1):
            n = checkallpos(board, x, y, lambda x:x==".", diagonals=True)
            c = sum(n)+(board[y][x]==".")
            if c>=giftreqs:
                cnt[x,y] = c

    cnt=dict(sorted(cnt.items(), key=lambda item: item[1]))
#    print(cnt)

    # c is the list of locations that at least have a theoretical chance to place the boxes at
    # now check if it really can be placed there. 

    for x,y in cnt:

        m = fliptofit(board, gift, x, y)
        if isinstance(m, np.ndarray):
            pdraw(board, m, x, y)
            return m
            
    return False
        
    
    
# fit all gifts in one region (starting empty)
def fit(region, gifts):

    t = region.split(":")

    box = ints(t[0])
    reqs = ints(t[1])
    q = list()
    
    print(box, reqs)

    
    board = [list("."*box[0]) for x in range(box[1])]

    for i,req in enumerate(reqs):
        if req:
            q+=[gifts[i]]*req
            
    print(q)
    print(board)
    c=0
    for i,g in enumerate(q):
        m = trypiece(board,g)
        if not isinstance(m, np.ndarray):
            print("unable to place gift #",i)
            pprint(board)
            pprint(g)
            pprint(m)
            break
        else:
            c+=1

    print(c,sum(reqs)-c)
    

fit(box[0], gifts)
        
