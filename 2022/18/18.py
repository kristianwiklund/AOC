import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.short",split=",",convert=lambda x:int(x))

def sides(l):

    x,y,z=l
    
    return [(x,y,z,x+1,y+1,z),
            (x,y,z,x+1,y,z+1),
            (x,y,z,x,y+1,z+1),
            (x,y,z+1,x+1,y+1,z+1),
            (x,y+1,z,x+1,y+1,z+1),
            (x+1,y,z,x+1,y+1,z+1)]

world = set()

for i in arr:
    s = sides(i)
    for t in s:
        if not t in world:
            world.add(t)
        else:
            world.remove(t)

print("Part 1:",len(world))
print(world)

