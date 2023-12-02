import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy

#arr = readarray("input.short",split=";",convert=lambda x:x)
lines = readlines("input.txt")

c=0
cnt=1
for l in lines:
    l = l.split(":")[1]
    l = l.split(";")

    # start a game
    r = None
    g = None
    b = None

    for x in l:
        x = x.split(";")
        for i in x:
            for j in i.split(","):
                p = ints(j)[0]
                if "red" in j:
                    if not r or r<p:
                        r = p
                if "green" in j:
                    if not g or g<p:
                        g = p
                if "blue" in j:
                    if not b or b<p:
                        b = p
                        
    c+=r*g*b
    

print("1:",c)
