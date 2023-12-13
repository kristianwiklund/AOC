import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

arr = []

with open("input") as fd:
    
    while True:
        a = readblock(fd)
        if a:
            arr.append(a)
        else:
            break

#print (arr)


# find symmetry along the y axis in a even sized matrix
def findit(a,tresh=0):

    if len(a)<2:
        return None
    

    # create numbers from the chars
    f = np.vectorize(lambda x:1 if x=='#' else 0)
    a = f(np.array(a))
    
    # the middle of the matrix
    l = len(a)
    l = int(l/2)

    
    a1 = a[0:l]
    a2 = a[l:]
    a1 = np.flipud(a1)

    if tresh==0:
        if not np.any(a1-a2):
            return l
        else:
            return None

    if tresh==1:
        p = abs(a1-a2)
        if sum(sum(p))==1:
            return l
        else:
            return None
              
def finditx(a,tresh=0):
    x = np.matrix.transpose(np.matrix(a))
    x = np.fliplr(np.matrix(x))
    return findity(x, tresh)

def findity(a, tresh=0):
    v = findityh(a, tresh)
    if v:
        return v

    # and the other way around
    v = findityh(np.flipud(a), tresh)
    if v:
        return len(a)-v
    else:
        return None

def findityh(a, tresh=0):

    a = np.array(a)

    # cut the matrix in reflectable pieces until we find something
    for i in range(int(len(a)/2)+1):
        z = findit(a[0:i*2], tresh)
        if z:
            return z

    return None
    
        
y =[findity([list(i) for i in x]) for x in arr]
#print("y",y)

x =[finditx([list(i) for i in x]) for x in arr]
#print("x",x)   

check = [(i,y[i],x[i]) for i in range(len(y)) if (y[i]!=None and x[i]!=None)]
#print("check:",check)

yy = [i for i in y if i]
xx = [i for i in x if i]

s = sum(yy)*100+sum(xx)
print("Part 1:",s)



    
y =[findity([list(i) for i in x], tresh=1) for x in arr]
x =[finditx([list(i) for i in x], tresh=1) for x in arr]

yy = [i for i in y if i]
xx = [i for i in x if i]


s = sum(yy)*100+sum(xx)
print("Part 2:",s)

