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
from cachetools import *

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

@cached(cache={}, key=lambda pile:pile[1])
def make(pile):
    global pat
    o,c,l = pile

    v = match(c)
    if not len(v):
        return None

    newp = [(o,y,l+[x]) for x,y in v if len(y)]
    nawp = [(o,y,l+[x]) for x,y in v if not len(y)]
    return (newp, nawp)

# idea:
# move along the track. find spots that have a manhattan distance of <=20 and check if those are connectable
# without touching other track parts along the way



   
    
@cache
def makemake(l):

    X=[(l,l,[])]
    while len(X):
       x = X.pop()
       t = make(x)
       # returns: a list of (original name, remaining text, match list)
       if t:
           if t[1]:
               return True
           X+=t[0]
    
       
    return False

    
s=set()
c=0
a=0
for l in lines:
    v = makemake(l)
    if v:
        print(l)
        a+=1
    c+=1
    print(a,"/",c,"ok")

print("track length",len(p))
