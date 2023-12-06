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


def checkseed(ns, s):
    for x in ns:
        if s in x:
            return True

    return False
    
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
ns=[]
for i in range(int(len(them["seeds"][0])/2)):
    ns.append(range(them["seeds"][0][i*2],them["seeds"][0][i*2]+them["seeds"][0][i*2+1]))

def link(them, frm, to, n):
    what = to+"-to-"+frm

    for x in them[what]:
        sr = x[0]
        dr = x[1]
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
    assert(link(them, "location", "humidity", 82)==78)
    assert(link(them, "soil", "seed", 81)==79)
    assert(link(them, "water", "fertilizer", 81)==81)


def doit(them):

    lowloc=None
    maxloc = max([x[0]+x[2] for x in them["humidity-to-location"]])
    #    print(maxloc)

    print("maxloc=",maxloc)
    import time
    tttt = time.time()
    for x in range(0,maxloc):
        if not x % 1000000:
            print (x, "time elapsed=",time.time()-tttt,"time remain=",(time.time()-tttt)*maxloc/1000000)
#        print ("seed", i)
        a = link(them, "location","humidity",x)
        b = link(them, "humidity", "temperature", a)
        c = link(them, "temperature", "light", b)
        d = link(them, "light", "water", c)
        e = link(them, "water", "fertilizer", d)
        f = link(them, "fertilizer", "soil", e)
        g = link(them, "soil", "seed", f)

        if checkseed(ns, g):
            print(x,g)
            break

    print ("lowloc:",x)

doit(them)

