import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split=",",convert=lambda x:x)
#print (arr)

def h(s):
    c=0

    for i in s:
        c+=ord(i)
        c*=17
        c%=256

    return c


v = [h(x) for x in arr[0]]
#print(v)
print("Part 1:",sum(v))

box=SortedDict()
d=[]
vvv = {}

for x in arr[0]:

    if x[-1]=="-":
#        d.append(x[0:-1])
        ha = h(x[0:-1])
        try:
            box[ha].remove(x[0:-1])
        except:
            pass
    else:
        x1,x2=x.split("=")
        ha = h(x1)

        if not ha in box:
            box[ha]=[x1]            
        else:
            if not x1 in box[ha]:
                box[ha].append(x1)

        try:
            d.remove(x1)
        except:
            pass
        vvv[x1] = int(x2)

#print(d)
#print(box)
ss=0
for x in box:
    ii=0
    for i in box[x]:
        if not i in d:
 #           print(x,box[x],i)
            v = (x+1)*(ii+1)*(vvv[i])
 #           print(i,v)
            ii+=1
            ss+=v

print("Part 2:",ss)
