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

arr = [[x[0],ints(x[1])] for x in readarray("input.short",split=" ",convert=lambda x:x)]
#lines = readlines("input.short")
print (arr)


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


xyz = set()
# eat a string and decorate it with v
def consume(s,v,a="",d=0):
    global xyz
    
    print("  "*d,"consume",s,v,a)
    
    if len(v)==0:
        xyz.add(a)
        return

    if len(s)==0:
        return
    
    n = v[0]
    
    # take care of any dots in the beginning of the string
    while len(s) and s[0]==".":
        sx = s[0]
        s= s[1:]
        a+=sx
        

    # then identify the next block of things

    b=""
    while len(s) and s[0]!=".":
        sx = s[0]
        s= s[1:]
        b+=sx
        
    w = gs(n,b)
    print("  "*d, " --> w=",w)
    
    for i in w:
#        print("iabs(b)=",i,a,b,s,b[len(i):]+s)
        consume(b[len(i):]+s,v[1:],a+i,d+1)
    

s=0
for i in arr:
    xyz=set()
    consume(i[0],i[1])
    s+=len(xyz)
    print(len(xyz),xyz)

print(s)
