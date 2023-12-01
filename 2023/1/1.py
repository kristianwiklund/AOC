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

lines=readlines("input.short.2")
arr=list()
n = ["skoltröttsomfan","one","two","three","four","five","six","seven","eight","nine"]
#54091 is too high
#46381 is too low
#46402 is too low
for l in lines:
    a = sorted([(x,l.find(x)) for x in n if l.find(x)>-1], key=lambda x:x[1])
    b = list(reversed(sorted([(x,l.rfind(x)) for x in n if l.find(x)>-1], key=lambda x:x[1])))
    
    if len(a):
        print(l)
        x,y = a[0]
        l = l.replace(x,str(n.index(x)))
        x,y = b[0]
        reverse_replacement=str(n.index(x))
        reverse_removal=x[::-1]
        l = l[::-1].replace(reverse_removal, reverse_replacement, 1)[::-1]
        print(l)
        arr.append(" ".join(list(l)))

#print(arr)
v = [ints(" ".join(x)) for x in arr]
#print(v)
s = [int(str(x[0])+str(x[-1])) for x in v]
print(sum(s))
