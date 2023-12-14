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
import re

arr = [[[p for p in x[0].split(".") if len(p)],ints(x[1])] for x in readarray("input.short",split=" ",convert=lambda x:x)]
print(arr)


# test if a goes into b
def tst(a,b):

    if len(a)>len(b):
        return False

    b=list(b)
    
    for i in a:
        ii = b.pop(0)
        
        if i==ii:
            continue
        if i=="." and ii=="#":
            return False

    return True
    
# generate all variations of n long springs going into v
def gs(n, v):

    # we cannot trivially fit the number item into v, return empty list
    if len(v)<n:
        return set()

    # the length of the blob to fit
    # is in n[0]

    # try to fit it
    # fit variations of the first
    
    s = "."*(len(v)-1)+"#"*n+"."*(len(v)-1)

    acc = set()
    for i in range(len(s)-len(v)+1):
        ss = s[i:i+len(v)]
        ss = re.sub(r"\.[.]*$",".", ss)

        # remove obvious non-matches
        if "#"*n in ss:

            # check if the pattern in v is matched by the pattern in ss
            if tst(ss,v):
                acc.add(ss)

    return acc


assert(gs(1, "???")=={'.#.','#.','..#'})
assert(gs(2,"???")=={"##.",".##"})


assert(tst(".#.","???"))
assert(tst("###","???"))
assert(not tst("##.","??#"))

    
assert(gs(2,"??#")=={".##"})
assert(gs(2,"???#")=={"##.","..##"})

# push a list (nl) of numbers into the string v
def ms(nx, v, zol, acc=""):
    
  #  print("----------------")
 #   print("checking",nx,"vs",v)
    if not len(nx) or not len(v):
        zol.append((nx,acc))
        return
    
    x = gs(nx[0],v)
#    print("gs returned",x)

    if not len(x):
        return
    
#        print ("end of the way and not everything matched")
#        print ("")
    
    # check all possible matches from the first number
    for i in x:
        if len(v[len(i):]):
   #         print("for i=",i,"calling the next level")
            ms(nx[1:],v[len(i):],zol,acc+i)
        else:
            zol.append((nx[1:],acc+i))
            
def mss(nx, v,acc=""):
    zol=[]
    ms(nx,v,zol,acc)

    return zol
            
assert(gs(1,"?")=={"#"})
#print(mss([1,1],"???"))

def spnk(v,x,acc=""):

    if not len(x) or not len(v):
        return 1
    
    y = x[0]
    print("--")
    print(v,y)
    t=mss(v,y,acc)
    print(">",t,"<")
    s=0
    for i in t:
        s+=(spnk(i[0],x[1:]))
        
    return s
        

print("")
print(arr[0])
vp = spnk(arr[0][1],arr[0][0])

for v in vp:
    print(v)
            
        
    
