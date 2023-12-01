import sys
import re
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np

arr = readarray("input.txt",split="",convert=lambda x:x)
v = [ints(" ".join(x)) for x in arr]
s = [int(str(x[0])+str(x[-1])) for x in v]
print(sum(s))

lines=readlines("input.txt")
arr=list()
n = ["skoltröttsomfan","one","two","three","four","five","six","seven","eight","nine"]

for l in lines:
    s=""
    a = sorted([(x,l.find(x)) for x in n if l.find(x)>-1], key=lambda x:x[1])
    while a:
        x,y = a[0]
        s+=l[0:y]
        s+=str(n.index(x))
        l = l[y+len(x):]
        a = sorted([(x,l.find(x)) for x in n if l.find(x)>-1], key=lambda x:x[1])
        
    arr.append(s+l)

v = [ints(" ".join(x)) for x in arr]
s = [int(str(x[0])+str(x[-1])) for x in v]
print(sum(s))
