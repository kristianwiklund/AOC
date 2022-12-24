#!/usr/bin/python3.9

import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
import numpy as np
from functools import cache

arr = readarray("input.txt",split="",convert=lambda x:x)
b=arr2sparse(arr,ignore="#.")
#print(b)

# start and stop points

startx=arr[0].index(".")
starty=0

stopx=arr[-1].index(".")
stopy=len(arr)-1


bliz=dict()
c=0
for i in b:
    bliz[c]=(i,b[i])
    c+=1

#print(bliz)
    
bm = {
    ">":(1,0),
    "^":(0,-1),
    "v":(0,1),
    "<":(-1,0)
    }

# moves the things
def tick(bliz):

    for ii in bliz:
        #        print("moving",ii,bliz[ii])
        i,dd = bliz[ii]
        d = bm[dd]
        x,y =i
        
        nx=x+d[0]
        ny=y+d[1]
        # check wrap
        if nx>=len(arr[0])-1:
            nx=1
        if ny>=len(arr)-1:
            ny=1
        if nx<=0:
            nx=len(arr[0])-2
        if ny<=0:
            ny=len(arr)-2
            #        print("new bliz pos:",(nx,ny))
#        arr[y][x]="."
#        arr[ny][nx]=dd
        bliz[ii]=((nx,ny),dd)
    
    return bliz


def checkbang(x,y,bliz):
    b = [x for x,d in bliz.values()]
    return (x,y) in b

assert(checkbang(1,1,{1:((1,1),">")}))
assert(not checkbang(1,0,{1:((1,1),">")}))

def pp(arr,bliz,me=(-1,-1)):

    if bliz:
        p = [bliz[i][0] for i in bliz]
    else:
        p=[]
        
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if (x,y)==me:
                print("O",end="")
            elif (x,y) in p:
                print("☁",end="")
            else:
                print(arr[y][x],end="")
        print("")
    print("-"*(1+len(arr)))    

for y in range(len(arr)):
    for x in range(len(arr[0])):
        if arr[y][x]!="#":
            arr[y][x]="."

pp(arr,[])

def kodde(arr,bliz,me=(-1,-1)):
    p = [bliz[i][0] for i in bliz]

    n=list()
    for y in range(len(arr)):
        n.append([])
        for x in range(len(arr[0])):
            if me==(x,y):
                n[y].append("O")
            elif (x,y) in p:
                n[y].append("☁")
            else:
                n[y].append(arr[y][x])
    return n

cnt=0
rows=set()
dim=list()

class Getout(Exception):
    pass

t = kodde(arr,bliz)
u = "".join(["".join(x) for x in t])            
print(u)

rows.add(u)
print(len(rows))
dim.append(t)

try:
    while True:
        bliz=tick(bliz)
        cnt+=1
        t = kodde(arr,bliz)
        u = str(bliz)
        if not u in rows:
            rows.add(u)
            print(len(rows))
            dim.append(t)
        else:
            raise Getout
except:
#    print(dim)
    print("the cycle is",cnt,"long")

# it is quite possible that the above is broken - it looks at the maze, not at the blizzards which is the real criteria

# idea
# we simulate the blizzards to create a 3D cube containing a maze
# then we solve the maze
# z is always forward
# xy are changeable, so we can reach 5 locations from the current one
# (0,0,1), (-1,0,1), (0,-1,1), (1,0,1), (0,1,1)

startz=0
import sys
sys.setrecursionlimit(3500)

@cache
def solve(x,y,zz):
    # z always have to increase and will wrap around once the cycle is complete

    # recursion error...
    if zz>3000:
        return None
    
    z=zz%len(maze)

    if maze[z][y][x]!=".":
        return None
    
    maze[z][y][x]="O"
    #print(maze[z][y][x])

    
    #    print("trying",(x,y,z))
 #   pp(maze[z],None,me=(x,y))
 #   print(zz)
            
    if (x,y)==(stopx,stopy):
        print("Found the end after",zz,"minutes!")
        maze[z][y][x]="."
        return (zz,[(x,y)])


    # down, left, right, up, wait
    ds=[(0,-1,1), (-1,0,1), (1,0,1), (0,1,1), (0,0,1)] # last resort is to wait one step

    mi=-1
    mp=None
    
    for d in ds:
        try:
            v = solve(x+d[0],y+d[1],zz+d[2])
        except:
            continue
            
        if v:
            i,p=v
            if i<mi or mi==-1:
                mp=[d]+p
                mi=i
    if mp:
        maze[z][y][x]="."
        return (mi,mp)
    else:
        maze[z][y][x]="."
        return None

maze=dim
print(solve(startx,starty,0))

