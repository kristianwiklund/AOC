import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

with open("input.short.2","r") as fd:

    arr = readblock(fd, convert=lambda x:[x for x in x])
    b = readblock(fd, convert=lambda x:[x for x in x])

    b = [x for xs in b for x in xs]

    def dooz(arr):

        w = findinarray(arr, "#",all=True)
        me = findinarray(arr,"@")
        b = findinarray(arr,"O", all=True)

        me = (me[0]*2, me[1])

        wall = []
        for i in w:
            wall.append((i[0]*2,i[1]))
            wall.append((i[0]*2+1,i[1]))

        box = {}
        for i in b:
            box[i[0]*2,i[1]]=((i[0]*2,i[1]),(i[0]*2+1,i[1]))
            box[i[0]*2+1,i[1]]=((i[0]*2,i[1]),(i[0]*2+1,i[1]))
                                                 
        return {"me":me, "box":box, "wall":wall}

            

    def printworld(w):

        mx = max([t[0] for t in [w["me"]]+list(w["box"].keys())+w["wall"]])
        my = max([t[1] for t in [w["me"]]+list(w["box"].keys())+w["wall"]])

        print(mx,my)

        for y in range(my+1):
            for x in range(mx+1):

                if (x,y) == w["me"]:
                    print("@",end="")
                elif (x,y) in w["wall"]:
                    print("#", end="")
                elif (x,y) in w["box"]:
                    if w["box"][(x,y)][0]==(x,y):
                        print("[",end="")
                    elif w["box"][(x,y)][1]==(x,y):
                        print("]",end="")
                else:
                    print(".", end="")
            print("")
        print("-"*mx)

    # horizontal movement
    def smolpotat(w, d, xx, yy):

        # similar to part 1:
        # first aggregate all boxes between the dude and a wall that are immediately connected to the dude

        ox=xx
        oy=yy
        
        lb = []
        while not (xx,yy) in w["wall"]:
            if (xx,yy) in w["box"]:
                lb.append((xx,yy))
            else:
                break
                
            xx+=dirs[d][0]
            yy+=dirs[d][1]

        # we have a list of all squares containing (half of a) box that are pushing against the dude
        # (xx,yy) is the square immediately in front of these boxes. check if it is empty. if not, don't move anything
        if (xx,yy) in w["wall"]:
            return

        print("can move", lb)

        # push the boxes one step in direction d starting with the box furthest away

        for i in lb[::-1]:
            print("push",i,"one step in",d,"-->",end="")
            x,y=i
            t = w["box"][(x,y)]
            del w["box"][(x,y)]
            x+=dirs[d][0]
            y+=dirs[d][1]
            a=(t[0][0]+dirs[d][0], t[0][1]+dirs[d][1])
            b=(t[1][0]+dirs[d][0], t[1][1]+dirs[d][1])

            print((x,y),":",(a,b))
            w["box"][(x,y)]=(a,b)
            
        w["me"]=(ox,oy)
        
    
    def storpotat(w, d):

        (x,y)=w["me"]

        xx=x+dirs[d][0]
        yy=y+dirs[d][1]
        
        # cannot move this way, do nothing
        if (xx,yy) in w["wall"]:
            return
                
        # nothing to push, move and return
        if not (xx,yy) in w["box"]:
            w["me"]=(xx,yy)
            return

        # are we moving horizontally? if so, we have the trivial case from part 1

        if d==1 or d==3:
            smolpotat(w,d,xx,yy)
            return

        # moving vertically. We need to find all the boxes the box might move and move them

               
        

    world = dooz(arr)
    printworld(world)
    
    storpotat(world, 3)
    printworld(world)
    
    

