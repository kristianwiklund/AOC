#!/usr/bin/python3.9

import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
import numpy as np
from functools import cache

arr = readarray("input.short",split="",convert=lambda x:x)
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
# 814 too high for part 2 (but a nice try...)
# 812 is too low
# hence, it is 813...

@cache
def solve(x,y,zz,ex,ey):
#    print("solving",x,y,zz,ex,ey)
    # z always have to increase and will wrap around once the cycle is complete
    z=zz%(len(maze))

    if maze[z][y][x]!=".":
        return None
    
    maze[z][y][x]="O"

    if (x,y)==(ex,ey):
        maze[z][y][x]="."
        return (zz,[(x,y,zz)])


    # down, up, left, right, wait
    ds=[(0,-1,1), (0,1,1), (-1,0,1), (1,0,1), (0,0,1)]

    mi=-1
    mp=None
    
    for d in ds:
        try:
            v = solve(x+d[0],y+d[1],zz+d[2],ex,ey)
        except:
            # ignore recursion, out of bounds, etc, errors
#            print("b0rk",x,y,z,d)
            continue
            
        if v:
            i,p=v
            if i<=mi or mi==-1:
                mp=[(x+d[0],y+d[1],zz+d[2])]+p
                mi=i

    maze[z][y][x]="."

    if mp:
        return (mi,mp)
    else:
        return None

maze=dim
#print("the maze is looping after",len(maze),"steps")
one=solve(startx,starty,0,stopx,stopy)
#print(one)
solve.cache_clear()
two=solve(stopx,stopy,one[0],startx,starty)
#print(two)
#pp(maze[one[0]%len(maze)],[],(startx,starty))
solve.cache_clear()
three=solve(startx,starty,two[0],stopx,stopy)
print(three)

