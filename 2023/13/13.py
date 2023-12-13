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

with open("input.short") as fd:
    
    while True:
        a = readblock(fd)
        if a:
            arr.append(a)
        else:
            break

#print (arr)


# find symmetry along the y axis in a even sized matrix
def findit(a):

    if not len(a):
        return None

    print("---")
    print(a)
    
    f = np.vectorize(lambda x:1 if x=='#' else 0)
    
    l = len(a)

    a = f(np.array(a))

    # the middle of the matrix
    l = int(l/2)

    
    a1 = a[0:l]
    a2 = a[l:]
    a1 = np.flipud(a1)

    print(a1)
    print(a2)
    print(a1-a2)
    # if all are zero, we have a mirror at l
    if not np.any(a1-a2):
        return l+1
    else:
        return None

    
def finditx(a):
    if (int(len(a[0])/2)*2 == len(a[0])):
        print("even x")    

    a = np.fliplr(np.matrix(a))
    x = np.matrix.transpose(a)
#    print(x)
    
    # all x are uneven, split in two to check with the same code as y

    x1 = x[0:-1]
    x2 = x[1:]

    p = findity(x1)
    if p:
        print(x1)
        return p
    q = findity(x2)
    if p:
        print(x2)
        return p+1
    return None

def findity(a):

    a = np.array(a)

    v = []
    # slice the matrix until we find something
    l = int(len(a)/2)
    
    for i in range(l-1):
        print("Checking", i*2)
        p = findit(a[0:i*2])
        q = findit(a[i*2:])
        if q:
            print((i,"1",len(a),(0,i*2),q+i*2))
            return q

        else:
            if p:
                print((i,"2",len(a),(i*2,l),p))

                return p

    return None
#    print("ve=",v)
#    return (v[0])
        

y =[findity([list(i) for i in x]) for x in arr]
print("y",y)

x =[finditx([list(i) for i in x]) for x in arr]
print("x",x)   

y = [i for i in y if i]
x = [i for i in x if i]

#s = sum(y)*100+sum(x)
#assert(s>1748)
