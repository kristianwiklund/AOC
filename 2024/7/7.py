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

arr = readarray("input",split=" ",convert=lambda x:int(x.strip(":")))
#lines = readlines("input.short")
#print(arr)

def doit(l):

    def helper(e, ack, target):

        if ack>target:
            return False
        
        if ack==target and len(e)==0:
            return True

        if len(e)==0:
            return False

        xp = helper(e[1:],ack+e[0],target)
        xm = helper(e[1:],ack*e[0],target)

        if not xp and not xm:
            return False

        else:
            return True
        
        
    c = len(l)-2
    v = l[0]
    e = l[1:]
#    print(v)
    return helper(e[1:], e[0], v)
    
         
    
su=0
for i in arr:
    c=doit(i)
    su+=i[0] if c else 0

print("A:",su)
