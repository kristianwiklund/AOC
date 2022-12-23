import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
import numpy as np

fn="input.txt"

arr = readarray(fn,split=",",convert=lambda x:int(x)+1)
maxx=max([x for x,y,z in arr])+1
maxy=max([y for x,y,z in arr])+1
maxz=max([z for x,y,z in arr])+1


w=[[[False for x in range(maxx)] for y in range(maxy)] for z in range(maxz)]

for x,y,z in arr:
#    print(x,y,z)
    w[z][y][x] = True

w=np.array(w)
#print(w)

# 1958 is too low
# 1963 is too low as well
# 1966 too low
# 2651 is wrong
# (0,0,0) is guaranteed to be in a place where the thing have free space around itself

q = list()
def bfs(pos):
    global maxx
    global maxy
    global maxz
    print(pos)
    
    while len(pos):
        t=pos.pop()
        x,y,z=t
    
        w[z][y][x] = True
        
        if z+1<maxz and not w[z+1][y][x]:
            pos.add((x,y,z+1))
        if y+1<maxy and not w[z][y+1][x]:
            pos.add((x,y+1,z))
        if x+1<maxx and not w[z][y][x+1]:
            pos.add((x+1,y,z))
        if z-1>=0 and not w[z-1][y][x]:
            pos.add((x,y,z-1))
        if y-1>=0 and not w[z][y-1][x]:
            pos.add((x,y-1,z))
        if x-1>=0 and not w[z][y][x-1]:
            pos.add((x-1,y,z))


v=set()
v.add((0,0,0))
bfs(v)
w=np.invert(w)
#print(21-sum(w))
# w is a hole.

barr=[]
for z in range(maxz):
    for y in range(maxy):
        for x in range(maxx):
            if w[z][y][x]:
                barr.append((x,y,z))

#print(arr)


def sides(l):

    x,y,z=l
    
    return [(x,y,z,x+1,y+1,z),
            (x,y,z,x+1,y,z+1),
            (x,y,z,x,y+1,z+1),
            (x,y,z+1,x+1,y+1,z+1),
            (x,y+1,z,x+1,y+1,z+1),
            (x+1,y,z,x+1,y+1,z+1)]

world = set()

arr = readarray(fn,split=",",convert=lambda x:int(x))

for i in arr:
    s = sides(i)
    for t in s:
        if not t in world:
            world.add(t)
        else:
            world.remove(t)


for i in barr:
    s = sides(i)
    for t in s:
        try:
            world.remove(t)
        except:
            pass

print("Part 2:",len(world))
#print(world)
#print(len(world))
#print(sum(w))
