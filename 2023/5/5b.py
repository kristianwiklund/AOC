import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

them = dict()
with open("input.short") as fd:
    while fd:
        v = readblock(fd)
        if not v:
            break
        what = v[0].split(":")[0].split(" ")[0]
        if v[0].split(":")[1] =="":
            s = v[1:]
        else:
            s = [(v[0].split(":")[1]).strip()]+v[1:]

        them[what] = sorted([ints(x) for x in s])
        

ns=[]
for i in range(int(len(them["seeds"][0])/2)):
    ns.append(range(them["seeds"][0][i*2],them["seeds"][0][i*2]+them["seeds"][0][i*2+1]))

them["seeds"]=ns
#print(them)

def rangify(i):
    return (range(i[1],i[1]+i[2]), range(i[0],i[0]+i[2]))

for x in them:
    if x=="seeds":
        continue

    v = them[x]
    v = [rangify(y) for y in v]
    them[x] = v

def transform(them, frm, to, r):
    t = them[frm+"-to-"+to]
    print("to transform:",r)
    a= []
    for x in t:
        # check if r matches any ranges in x
        fr = x[0]
        tr = x[1]
        print(r,fr,tr)
        
        if overlap(r, fr):
            print(r,"overlaps",fr)
            print("slicing...")
            i = range_intersect(r, fr)

            print(r,fr,i,tr)
        

    print(a)

        
            
            
            
transform(them, "seed", "soil", them["seeds"][0])


    
