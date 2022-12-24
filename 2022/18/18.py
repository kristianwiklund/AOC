import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint
import numpy as np
from draw import *

fn="input.txt"

arr = readarray(fn,split=",",convert=lambda x:int(x)+1)
maxx=max([x for x,y,z in arr])+2
maxy=max([y for x,y,z in arr])+2
maxz=max([z for x,y,z in arr])+2



w=[[[0 for x in range(maxx)] for y in range(maxy)] for z in range(maxz)]

for x,y,z in arr:
#    print(x,y,z)
    w[z][y][x] = 1

w=np.array(w)
#print(w)
ow=deepcopy(w)

class Bob():

    def __init__(self):
        self.list=[]
        self.set=set()

    def pop(self,x):
        t = self.list.pop(x)
        self.set.remove(t)
        return t

    def add(self,x):
        if not x in self.set:
            self.set.add(x)
            self.list.append(x)

    def __len__(self):
        return len(self.list)

q = list()
def bfs(pos,value=1):
    global maxx
    global maxy
    global maxz
    print(pos)
    cnt=0
    
    while len(pos):
        t=pos.pop(0)
        x,y,z=t
    
        w[z][y][x] = value
        
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
        #savefig(w,serial=cnt)
        cnt+=1
        print(sum(w==0))
        #print(cnt, "queue:",len(pos))


v=Bob()
v.add((0,0,0))
bfs(v)


barr=[]
for z in range(maxz):
    for y in range(maxy):
        for x in range(maxx):
            if w[z][y][x]==0:
                barr.append((x,y,z))


def sides(l):

    x,y,z=l
    
    return [(x,y,z,x+1,y+1,z),
            (x,y,z,x+1,y,z+1),
            (x,y,z,x,y+1,z+1),
            (x,y,z+1,x+1,y+1,z+1),
            (x,y+1,z,x+1,y+1,z+1),
            (x+1,y,z,x+1,y+1,z+1)]

world = set()

arr = readarray(fn,split=",",convert=lambda x:int(x)+1)

for i in arr:
    s = sides(i)
    for t in s:
        if not t in world:
            world.add(t)
        else:
            world.remove(t)

print("Part 1:",len(world))

for i in barr:
    s = sides(i)
    for t in s:
        try:
            world.remove(t)
        except:
            pass

print("Part 2:",len(world))


