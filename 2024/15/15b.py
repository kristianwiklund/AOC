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

import clear_screen 

with open("input.short","r") as fd:

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

#        clear_screen.clear()

        from py100 import py100

        py100.move_cursor_upper_left()
        
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

#        print("can move", lb)

        # push the boxes one step in direction d starting with the box furthest away

        for i in lb[::-1]:
#            print("push",i,"one step in",d,"-->",end="")
            x,y=i
            t = w["box"][(x,y)]
            del w["box"][(x,y)]
            x+=dirs[d][0]
            y+=dirs[d][1]
            a=(t[0][0]+dirs[d][0], t[0][1]+dirs[d][1])
            b=(t[1][0]+dirs[d][0], t[1][1]+dirs[d][1])

 #           print((x,y),":",(a,b))
            w["box"][(x,y)]=(a,b)
            
        w["me"]=(ox,oy)

    # recursive box finder
    def findlbv(w,p,d,lb):

#        print("findlbv checking",p,"in dir",d)
        xx,yy=p
        xx+=dirs[d][0]
        yy+=dirs[d][1]
        
        if (xx,yy) in w["wall"]:
            return lb

        if (xx,yy) in w["box"]:

            m = w["box"][(xx,yy)]
            lb+=m

            # fan out the boxes
            return findlbv(w, m[0], d, lb)+findlbv(w, m[1], d, lb)

        return lb
            
            
        
    def storpotat(w, d):

        (x,y)=w["me"]
        ox=x
        oy=y
        
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

        # moving vertically.
        # the trivial case is that nothing is in front of us - we have already checked for that and for a wall,
        # so now we need to find all the boxes the box might move and move them. done the same way as in smolpotat

      #  print(list(w["box"][(xx,yy)]))
        lb = list(set(list(w["box"][(xx,yy)])+findlbv(w, w["box"][(xx, yy)][0], d, [])+findlbv(w, w["box"][(xx, yy)][1], d, [])))
      #  print(lb)

        # lb contains all boxes that potentially move when we move. now figure out if we can move or not
        # start by sorting the boxes in "furthest away from dude first" order
        dd = [abs(w["me"][1]-t[1]) for t in lb]
#        print(dd)

        lb = [x for _, x in sorted(zip(dd, lb))][::-1]
#        print(lb)

        for x in lb:
            # if any of the boxes in the cone have a wall next to them in the movement dir, we cannot move
            if (x[0]+dirs[d][0],x[1]+dirs[d][1]) in w["wall"]:
                return

        # yay move.

        for i in lb:
 #           print("push",i,"one step in",d,"-->",end="")
            x,y=i
            t = w["box"][(x,y)]
            del w["box"][(x,y)]
            x+=dirs[d][0]
            y+=dirs[d][1]
            a=(t[0][0]+dirs[d][0], t[0][1]+dirs[d][1])
            b=(t[1][0]+dirs[d][0], t[1][1]+dirs[d][1])

  #          print((x,y),":",(a,b))
            w["box"][(x,y)]=(a,b)
            
        w["me"]=(xx,yy)
        
        
        
    t = {'^':0,'>':1,'v':2,'<':3}
    world = dooz(arr)
    #printworld(world)
    
    #storpotat(world, 3)
    #printworld(world)

    #world["me"]=(7,5)
    #printworld(world)

    #storpotat(world,0)
    #printworld(world)

    def gps(world):

        s = set()
        for i in world["box"]:
            s.add(world["box"][i][0])
#        print(s)

        return sum([i[1]*100+i[0] for i in s])

    clear_screen.clear()
    
    for dd in b:
        d=t[dd]
        
        storpotat(world, d)
        #       print(".",end="")
        printworld(world)

    print(gps(world))

