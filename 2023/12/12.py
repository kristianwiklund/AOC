import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = [[[p for p in x[0].split(".") if len(p)],ints(x[1])] for x in readarray("input.short",split=" ",convert=lambda x:x)]
print(arr)


# squeeze in as many as possible from n into v
def trytomatch(n, v):
    print("trying",n,"vs",v)

    # we cannot trivially fit the first item into v, return empty list
    if len(v)<n[0]:
        return []

    # the length of the blob to fit
    # is in n[0]

    # try to fit it

    acc = []
    for x in range(len(v)-n[0]):
        print("fitter", v[x:x+len(v)],v[x+len(v):])
        if re.match("[^.]{"+str(n[0])+"}", v):
            print ("match for",n[0])
    
    
# 0 is the string of broken springs, # is broken, . is not broken, ? is unknown
# 1 is the list of numbers of broken springs in the order they appear

def rf(x):
    n=x[1]
    s=x[0]
    y = []

#    print("---------")
    
    for v in s:
        t = n[0]        
#        print (v,s,t)

        if not "?" in v:
            if t!=len(v):
                print("bork",t,v,len(v))
                return None
            else:
                y.append(v)
                n.pop(0)
        else:
            # absolute match
            if len(v)==t:
                y.append("#"*t)
                n.pop(0)
            else:
                # generate a list of possible matches
                trytomatch(n,v)
                
#                if not "#" in v:
#                    # only ???
#                    # find how many will fit. it is the sum of the items plus (n-1) where n is the number of items
#                    l = len(v)
#                    fl=False
#                    for z in range(len(n)):
#                        if l-(sum(n[:z+1])+z)<0:
#                            fl=True
#                            break#
#
#                    if not fl:
#                        return None#
#
#                    print(z, "of the things",n," fit in",v)
#                else:
#                    # mix
#                    print("mix of items",v)
#                    pass

#    return y
            

print([rf(x) for x in arr])
