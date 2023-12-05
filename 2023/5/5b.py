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
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

them = dict()
with open("input.txt") as fd:
    while fd:
        v = readblock(fd)
        if not v:
            break
        what = v[0].split(":")[0].split(" ")[0]
        if v[0].split(":")[1] =="":
            s = v[1:]
        else:
            s = [(v[0].split(":")[1]).strip()]+v[1:]

        them[what] = [ints(x) for x in s]
        
print(them)

def link(them, frm, to, n):
    what = frm+"-to-"+to

    for x in them[what]:
        dr = x[0]
        sr = x[1]
        l = x[2]
#        print(what, "n=",n, "source range=",(sr, sr+l), "dest=",dr)
        i = range(sr, sr+l).index(n) if n in range(sr, sr+l) else -1
        if i>-1:
#            print (i, dr, i+dr)
            return i+dr

    # any.. not mapped... same number
    return n

# test data
if len(them["seed-to-soil"])==2:
    assert(link(them, "seed", "soil", 98)==50)
    assert(link(them, "seed", "soil", 99)==51)
    assert(link(them, "seed", "soil", 53)==55)
    assert(link(them, "fertilizer", "water", 20)==9)


def doit(them):

    lowloc=None
    for i in them["seeds"][0]:
#        print ("seed", i)
        a = link(them, "seed","soil",i)
        b = link(them, "soil", "fertilizer", a)
        c = link(them, "fertilizer", "water", b)
        d = link(them, "water", "light", c)
        e = link(them, "light", "temperature", d)
        f = link(them, "temperature", "humidity", e)
        g = link(them, "humidity", "location", f)
        
#        print(i,a,b,c,d,e,f,g)

        if not lowloc or g<lowloc:
            lowloc = g

    print (lowloc)

doit(them)

