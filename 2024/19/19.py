import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")
#from multiprocessing import Pool

pat = sorted(lines[0].replace(" ","").split(","), key=len)
#print(pat)
lines = lines[2:]
#print(lines)

@cache
def match(line):
    global pat
    fr=[]
    for i in pat:
        if line.startswith(i):
            fr.append((i, line[len(i):]))

    return fr

def make(pile):
    global pat
    o,c,l = pile

    v = match(c)
    if not len(v):
        return([],[])

    newp = [(o,y,l+[x]) for x,y in v if len(y)]
    nawp = [(o,y,l+[x]) for x,y in v if not len(y)]
    return (newp, nawp)

s=set()
for l in lines:
    v = match(l)

    while v:
        z=[]
        for i in v:
            #print("i",i)
            if len(i[1])==0:
                s.add(l)
            ll = match(i[1])
            if ll:
                #print("bop")
                #                s.add(l)
                z+=ll
        v=z

print(s)
