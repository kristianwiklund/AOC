import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
from parsemap import *

import re

dd = {0:[1,0],  #e >
     1:[0,1],  #s v
     2:[-1,0], #w < 
     3:[0,-1], #n ^
    }

# how we turn when we move to a new world
w2wt = {(1,4):0,
       (1,2):-2,
       (1,3):1,
       (1,6):-2,
       (2,3):0,
       (2,5):-2,
       (2,6):-1,
       (3,4):0,
       (3,5):1,
       (4,5):0,
       (4,6):-1,
       (5,6):0
       }
w2wc = {1:[6,4,3,2],
        2:[3,5,6,1],
        3:[4,5,2,1],
        4:[6,5,3,1],
        5:[6,2,3,4],
        6:[1,2,6,4]}
       
def checkstep(fullmap, world,x,y,facing):
    global d

    mymap = fullmap[world]
    
    x+=dd[facing][0]
    y+=dd[facing][1]

    if x<0 or y<0:
        return False

    if y>=len(mymap):
        return False

    if x>=len(mymap[y]):
        return False

    if mymap[y][x]==".":
        return True

    return False

# rewrite wrapmove to move to a new world when we wrap

def wrapmove(fullmap, world,x,y,facing):
    global d

    mymap = fullmap[world]
    
    print("checking for wrapmove")
    ox=x
    oy=y
    
    x+=dd[facing][0]
    y+=dd[facing][1]

    while True:
    
        # wraparound, this is where we need to swap worlds and rotate the movement
        # there are two steps to this change - one is to change the direction, the other
        # is to change the coordinates
        
        if y<0:
            # we move to the world in [3] in the list
            #y = len(mymap)-1
            newworld = w2wc[world][3]
            
        if x<0:
            # we move to the world in [2]
            #x = len(mymap[y])-1
            newworld = w2wc[world][2]

        if y>=len(mymap):
            # we move to the world in [1]
            #y=0
            newworld = w2wc[world][1]

        if x>=len(mymap[y]):
            # we move to the world in [0]
            #x=0
            newworld = w2wc[world][0]

            
        # rotate things
        if world!=newworld:
            
            try:
                fd = w2wt[(world, newworld)]
                facing = (facing+fd)%4
            except:
                fd = w2wt[(newworld,world)]
                facing = (facing-fd)
                if facing<0:
                    facing=facing+4

            world = newworld
            mymap = fullmap[world]

            # rotate the coordinates
            if fd==1:
                print ("rotate world right, coord left")
                nx = y
                ny = len(mymap)-x
            elif fd==2 or fd==-2:
                print ("rotate world 180 degrees")
                print ("(x,y)",(x,y))
                print("map dim",len(mymap))
                nx = len(mymap)-x
                ny = len(mymap)-y
                print ("(nx,ny)",(nx,ny))
            elif fd==-1:
                print("rotate world left, coord right")
                nx = len(mymap)-y
                ny = nx
            else:
                # do nothing
                pass

            x=nx
            y=ny

        try:
            if mymap[y][x]=="#":
                print("Hit something",mymap[ny][nx])
                return None
        except:
            print("bad range for mymap",(x,y))
            import sys
            sys.exit()

        if mymap[y][x]==".":
            print("Done wrapping")
            return ((x,y),newworld)

        ox=x
        oy=y

        x+=dd[facing][0]
        y+=dd[facing][1]
        print("+1 in the wrap",(x,y))
        
    return ((x,y), world)
            

        
#arr = readarray("input.short",split="",convert=lambda x:x)
with open("input.short","r") as fd:
    mymap = [x.rstrip() for x in readblock(fd,strip=False)]
    mypath= list()
 #   print(mymap)
    cmd = fd.readline().strip()

    tmap=list()
    ml=max([len(x) for x in mymap])
    for i in mymap:
        if len(i)<ml:
            tmap.append(i+" "*(ml-len(i)))
        else:
            tmap.append(i)

    mymap=tmap
    #   print(mymap)

    fullmap=splitmap(mymap)
    
    
    # "begin the path in the leftmost open tile of the top row of tiles"
    # "initially you are facing right"
    
    x = mymap[0].index(".")
    y = 0
    
    facing = 0
    mypath = [(x,y,facing,None)]
    
    steps=re.split(r"[A-Z]",cmd)
    dirs=re.split(r"[0-9][0-9]|[0-9]",cmd)[1:]
    walk= zip(steps,dirs)
    world=1
    
    for s,d in walk:
        print("facing",facing,"moving",(s,d))
        
        for i in range(int(s)):

            if checkstep(fullmap, world, x,y,facing):
                x+=dd[facing][0]
                y+=dd[facing][1]
#                print("moved to",(x,y))
                mypath.append((x,y,facing,world))
            else:
                v=wrapmove(fullmap,world,x,y,facing)
                if v:
                    x=v[0][0]
                    y=v[0][1]
                    world=v[1]
                    
#                    print("moved to",(x,y))
                    mypath.append((x,y,facing,world))

                
        if d=="L":
            facing-=1
            if facing<0:
                facing=3
 #           print("Turned left")
            
        if d=="R":
            facing+=1
            facing=facing%4
            #           print("Turned right")


    # need updating to plot right
    path = [(x,y) for x,y,z,v in mypath]
#    print (path)
    printpath(path,background=mymap,bgin=".# ",end="|")
                
    print("row",y+1,"col",x+1,"facing",facing)
    print("Part 1:",1000*(y+1)+4*(x+1)+facing)
    # 164074 not right
    
