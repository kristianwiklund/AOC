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
       (3,5):-1,
       (4,5):0,
       (4,6):1,
       (5,6):0
       }
w2wc = {1:[6,4,3,2],
        2:[3,5,6,1],
        3:[4,5,2,1],
        4:[6,5,3,1],
        5:[6,2,3,4],
        6:[1,2,5,4]}


w2wtreal = {
    (1,2):0,
    (1,3):0,
    (1,6):1,
    (6,1):-1,
    (1,4):2,
    (3,2):-1,
    (2,3):1,
    (2,5):2,
    (2,6):0,
    (3,5):0,
    (3,4):-1,
    (4,3):1,
    (4,5):0,
    (4,6):0,
    (5,6):1,
    (6,5):-1
       }
w2wcreal = {1:[2,3,4,6],
        2:[5,3,1,6],
        3:[2,5,4,1],
        4:[5,6,1,3],
        5:[2,6,4,3],
        6:[5,2,1,4]}

w2wt = w2wtreal
w2wc = w2wcreal

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

 #   print("Taking a giant leap for mankind from",(x,y),"to",end="")
    x+=dd[facing][0]
    y+=dd[facing][1]
 #   print((x,y))

    while True:
        print("we are facing",facing)
        newworld=world
        # wraparound, this is where we need to swap worlds and rotate the movement
        # there are two steps to this change - one is to change the direction, the other
        # is to change the coordinates
        
        if y<0:
            # we move to the world in [3] in the list
            y = len(mymap)-1
            newworld = w2wc[world][3]
            print("a we move from",world,"to",newworld)
        
        if x<0:
            # we move to the world in [2]
            x = len(mymap[y])-1
            newworld = w2wc[world][2]
            print("b we move from",world,"to",newworld)
            
        if y>=len(mymap):
            # we move to the world in [1]
            #y=0
            newworld = w2wc[world][1]
            y=0
            print("c we move from",world,"to",newworld)

        if x>=len(mymap[y]):
            # we move to the world in [0]
            x=0

            newworld = w2wc[world][0]
            print("d we move from",world,"to",newworld)
            
        # rotate things
        if world!=newworld:
            
            try:
                fd = w2wt[(world, newworld)]
                print("add facing",facing,fd)
                facing = (facing+fd)
                if facing<0:
                    facing=facing+4
                facing=facing%4
                print("new addfacing",facing)
                assert(facing>=0 and facing<4)
            except:
                fd = w2wt[(newworld,world)]
                print("subtract facing",facing,fd)
                                
                facing = (facing-fd)
                
                if facing<0:
                    facing=facing+4
                    
                facing=facing%4
                print("new subfacing", facing)
                
                assert(facing>=0 and facing<4)


            print("from",world,"to",newworld,"facing",facing)
            oldworld=world
            world = newworld
            mymap = fullmap[world]

            # rotate the coordinates
            if fd==1:

                print ("rotate world right, coord left")
#                nx = y
                ny = x
                nx = len(mymap)-y-1
                print((x,y),"-->",(nx,ny))
                printpath([(ox,oy)],background=fullmap[oldworld],bgin="#")
                print("")
                printpath([(nx,ny)],background=fullmap[world],bgin="#")
                print("--")
            elif fd==2 or fd==-2:

                print ("rotate world 180 degrees")
                print ("(x,y)",(x,y))
                print("map dim",len(mymap))
                nx = len(mymap)-x-1
                ny = len(mymap)-y-1
#                print ("(nx,ny)",(nx,ny))
            elif fd==-1:

                print("rotate world left, coord right")
                nx = y
                ny = len(mymap)-x-1
                print("new coord are",(nx,ny))
                print("we are facing",facing)
            else:
                # do nothing
                print("No rotation, new coordinates are",(x,y))

                nx=x
                ny=y

            x=nx
            y=ny

        try:
            if mymap[y][x]=="#":
#                print("Hit something",mymap[y][x])
                return None
        except:
#            print("bad range for mymap",(x,y),"or",(nx,ny))
#            print("max range is",(len(mymap[0]),len(mymap)))
            import sys
            sys.exit()

        if mymap[y][x]==".":
#            print("Done wrapping")
            return ((x,y),newworld, facing)

        ox=x
        oy=y

#        print("Happily moving around in the world, from",(x,y),end="")

        x+=dd[facing][0]
        y+=dd[facing][1]
#        print("to +1 in the wrap",(x,y))
        
    return ((x,y), world, facing)

def pp():
    import os
    #os.system("clear")
        
    newpath=transmogrif(mypath, fullmap)
    path = [(x,y) for x,y,z,w in newpath]
    theex = [w for x,y,z,w in mypath][1:]+[0]

    printpath(path,background=mymap,bgin=".# ",end="|",thex=theex)

        
with open("input.txt","r") as fd:
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
    
    x = fullmap[1][0].index(".")
    y = 0
    
    facing = 0
    
    steps=re.split(r"[A-Z]",cmd)
    dirs=re.split(r"[0-9][0-9]|[0-9]",cmd)[1:]
    walk= zip(steps,dirs)
    world=1
    mypath = [(x,y,facing,world)] 
    print("starting at",x,y,"facing",facing,"on map ",world)
   
    for s,d in walk:
        
#        pp()
        
        for i in range(int(s)):
 #           print("facing",facing,"moving",(s,d))
        
            if checkstep(fullmap, world, x,y,facing):
                x+=dd[facing][0]
                y+=dd[facing][1]
#                printpath([(x,y)],background=fullmap[world],bgin="#")
#                print("moved to",(x,y))
                mypath.append((x,y,facing,world))
            else:
                v=wrapmove(fullmap,world,x,y,facing)
                if v:
                    x=v[0][0]
                    y=v[0][1]
                    world=v[1]
                    facing=v[2]
                    assert(world!=0)
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
#    path = [(x,y) for x,y,z,v in mypath]
#    print (path)
#    printpath(path,background=mymap,bgin=".# ",end="|")
                
    print("row",y+1,"col",x+1,"facing",facing)
    
    newpath=transmogrif(mypath, fullmap)
    path = [(x,y) for x,y,z,w in newpath]
    theex = [w for x,y,z,w in mypath][1:]+[0]
        
    pp()
    x,y,z,v=newpath[-1]

    print("Part 2:",1000*(y+1)+4*(x+1)+z)
#    print(theex)
# high: 128019
# 25309

# inte heller 103245, eller 126020
