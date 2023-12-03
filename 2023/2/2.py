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

r = 12
g = 13
b = 14

c=0
cnt=1
for l in lines:
    l = l.split(":")[1]
    l = l.split(";")

    # start a game
    imp=False
    for x in l:
        x = x.split(";")
        for i in x:
            for j in i.split(","):
                p = ints(j)[0]
                if "red" in j and p>r:
                    imp=True
                if "green" in j and p>g:
                    imp=True
                if "blue" in j and p>b:
                    imp=True
    if not imp:
        print (cnt)
        c+=cnt
    cnt+=1
    

print("1:",c)
