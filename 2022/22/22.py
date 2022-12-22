import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
import re

dd = {0:[1,0],  #e >
     1:[0,1],  #s v
     2:[-1,0], #w < 
     3:[0,-1], #n ^
    }

def checkstep(mymap,x,y,facing):
    global d

        
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

def wrapmove(mymap,x,y,facing):
    global d

    print("checking for wrapmove")
    ox=x
    oy=y
    
    x+=dd[facing][0]
    y+=dd[facing][1]

    while True:
    
        # wraparound
        if y<0:
            y = len(mymap)-1
        if x<0:
            x = len(mymap[y])-1

        if y>=len(mymap):
            y=0

        if x>=len(mymap[y]):
            x=0

        if mymap[y][x]=="#":
            print("Hit something",mymap[y][x])
            return None

        if mymap[y][x]==".":
            print("Done wrapping")
            return (x,y)

        ox=x
        oy=y

        x+=dd[facing][0]
        y+=dd[facing][1]
        print("+1 in the wrap",(x,y))
        
    return (x,y)
            
        

#arr = readarray("input.short",split="",convert=lambda x:x)
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

    
    # "begin the path in the leftmost open tile of the top row of tiles"
    # "initially you are facing right"
    
    x = mymap[0].index(".")
    y = 0
    
    facing = 0
    mypath = [(x,y,facing,None)]
    
    steps=re.split(r"[A-Z]",cmd)
    dirs=re.split(r"[0-9][0-9]|[0-9]",cmd)[1:]
    walk= zip(steps,dirs)

    for s,d in walk:
        print("facing",facing,"moving",(s,d))
        
        for i in range(int(s)):

            if checkstep(mymap, x,y,facing):
                x+=dd[facing][0]
                y+=dd[facing][1]
#                print("moved to",(x,y))
                mypath.append((x,y,facing,(s,d)))
            else:
                v=wrapmove(mymap,x,y,facing)
                if v:
                    x=v[0]
                    y=v[1]
                    
#                    print("moved to",(x,y))
                    mypath.append((x,y,facing,(s,d)))

                
        if d=="L":
            facing-=1
            if facing<0:
                facing=3
 #           print("Turned left")
            
        if d=="R":
            facing+=1
            facing=facing%4
 #           print("Turned right")

            
    path = [(x,y) for x,y,z,v in mypath]
#    print (path)
    printpath(path,background=mymap,bgin=".# ",end="|")
                
    print("row",y+1,"col",x+1,"facing",facing)
    print("Part 1:",1000*(y+1)+4*(x+1)+facing)
    # 164074 not right
    
