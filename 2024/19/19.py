import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")
pat = sorted(lines[0].replace(" ","").split(","),key=lambda x:-len(x))
lines=lines[2:]

@cache
def boll(s):
    
    global pat
    hyst=set()
    #    koff = SortedList(key=len)
    #    koff.add(s)
    koff = [s]
    
    while len(koff):
#        koff=sorted(koff,key=lambda x:len(x)) 
#        print(koff)
                
        s = koff.pop()
        if s in hyst:
            continue
        hyst.add(s)
        
        x = [i for i,p in enumerate(pat) if s.startswith(p)]
        if not len(x):
            print("discard",s)
            continue
       
        for i in x:
            v = s[len(pat[i]):]
            if not v:
                return 1
            koff.append(v)

    return 0

c=0
cc=0
for i in lines:
    print(cc,c)
    cc+=1

    c+=boll(i)
       
print(c)
