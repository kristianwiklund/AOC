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
import numpy as np
#import scipy
#from functools import cache

arr = readarray("input",split=" ",convert=lambda x:x.replace("L","-").replace("R",""))
arr = [x[0] for x in arr]

p = 50
xp = 50
pw=0
pw2=0
bep=[]

for i in arr:
    pp = xp
    xp = pp + int(i)
    p = p + int(i)

    ap = list(range(pp,xp,-1 if xp<pp else 1))
    bep+=ap
    
    p=p%100
    
    if p<0:
        p+=100

    if not p:
        pw+=1
        
mep = np.array(bep)
mep = mep % 100
pw2 = sum(mep==0)


print("pw1=",pw)
print("pw2=",pw2)
