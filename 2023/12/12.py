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

arr = [[x[0],ints(x[1])] for x in readarray("input",split=" ",convert=lambda x:x)]
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


def scnt(s):
    return [len(x) for x in s.split(".") if x!='']
    
# eat a string and decorate it with v
def consume(s,v,xyz=None,a="",d=0,vo=False):

    if xyz==None:
        xyz=set()
        prt=True
        print(s)
    else:
        prt=False
        
    if len(v)==0:
        if not "#" in s:
            print(a,scnt(a),vo,s)
            if scnt(a)==vo:
                xyz.add(a+"."*len(s))

        return 0

    if len(s)==0:
        return 0

    if not vo:
        vo = v
    
#    print("  "*d,"consume",s,v,a)
    

    
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
 #   print("  "*d, " --> w=",w)

    if len(w)==0:
        if not "#" in b:
            consume(s,v,xyz,a+"."*len(b),d+1,vo)
    else:
        for i in w:
            #        print("iabs(b)=",i,a,b,s,b[len(i):]+s)
            consume(b[len(i):]+s,v[1:],xyz,a+i,d+1,vo)
        if not "#" in b:
            consume(s,v,xyz,a+"."*len(b),d+1,vo)
            
    if prt:
        print(xyz)
    return(len(xyz))

def c(s):
    s1,s2=s.split(" ")
    s2=ints(s2)
    return consume(s1,s2)

assert(consume("???.###",[1,1,3])==1)
assert(consume(".??..??...?##.",[1,1,3])==4)
assert(consume("?###????????",[3,2,1])==10)
assert(c("?#?#?.#?#???????..? 5,1,1,3,2,1")==1)
assert(consume("??????????",[1])==10)
assert(consume("??????????",[])==0)
assert(consume("??.?......",[2,1,3])==0)
assert(consume("??.???.?..",[3,1])==1)
assert(consume("",[1,2,3])==0)
x=set()
print("boll")
print(consume("???.###.???",[3],x))
print(x)


assert(consume("???.###.???",[3])==1)

s=0
for i in arr:
    xyz=set()
    consume(i[0],i[1],xyz)
    s+=len(xyz)
    pprint(xyz)

if len(arr)>900:
    assert(s<8202)
    assert(s>6564)

print(s)

