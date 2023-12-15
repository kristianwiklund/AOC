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

arr = [[x[0],ints(x[1])] for x in readarray("input",split=" ",convert=lambda x:x)]
#lines = readlines("input.short")
#print (arr)


# test if a goes into b
@cache
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
@cache
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

@cache
def scnt(s):
    return [len(x) for x in s.split(".") if x!='']

@cache
def krfsm(s):

    s=s.replace(".","0").replace("#","1")
    return (int("1"+s,2))

# eat a string and decorate it with v
@cache
def consume(s,v):
    global xyz

    v=ints(v)
    if len(v)==0:
        if not "#" in s:
            return 1

        return 0
            
    if len(s)==0:
        return 0

    n = v[0]
    
    # take care of any dots in the beginning of the string
    while len(s) and s[0]==".":
        sx = s[0]
        s= s[1:]

    # then identify the next block of things

    b=""
    while len(s) and s[0]!=".":
        sx = s[0]
        s= s[1:]
        b+=sx

    w = gs(n,b)

    acc=0
    if len(w)==0:
        if not "#" in b:
            acc+=(consume(s,str(v)))
    else:
        for i in w:
            acc+=(consume(b[len(i):]+s,str(v[1:])))

        if not "#" in b:
            acc+=(consume(s,str(v)))
        
    return(acc)

def c(s):
    s1,s2=s.split(" ")
    xyz=consume(s1,s2)
    print(xyz)
    return xyz

#assert(consume(".??..??...?##.",[1,1,3])==4)
#assert(consume("?###????????",[3,2,1])==10)
assert(c("???.### 1,1,3")==1)
assert(c("?#?#?.#?#???????..? 5,1,1,3,2,1")==1)
#assert(consume("??????????",[1])==10)
#assert(consume("??????????",[])==0)
#assert(consume("??.?......",[2,1,3])==0)
#assert(consume("??.???.?..",[3,1])==1)
#assert(consume("",[1,2,3])==0)
#assert(consume("???.###.???",[3])==1)

s=0
for i in arr:
    xyz=    consume(i[0],str(i[1]))
    s+=(xyz)

print("Part 1:",s)

if len(arr)>900:
    assert(s<8202)
    assert(s>6564)
    assert(s==7260)
    


assert(c("???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3")==1)
#assert(c("?#?#?#?#?#?#?#? 1,3,1,6")==1)
#assert(c("????.#...#...????.#...#...????.#...#...????.#...#...????.#...#... 4,1,1,4,1,1,4,1,1,4,1,1,4,1,1")==16)
#assert(c(".??..??...?##..??..??...?##..??..??...?##..??..??...?##..??..??...?##. 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3")==16384)


#for i in range(len(arr)):
#    arr[i][0]=(arr[i][0]+"?")*4+arr[i][0]
#    arr[i][1]=arr[i][1] + arr[i][1] + arr[i][1] + arr[i][1] + arr[i][1]

s=0
for i in arr:
    if True:
        a=(i[0]+"?")*4+i[0]
        a = a[::-1]
        b=i[1] + i[1] + i[1] + i[1] + i[1]
        b=list(reversed(b))
#        xyz=    consume(a,str(b),"",str(b))
        xyz=    consume(a,str(b))
#        xyz=    consume(a,str(b),"")
#        print(consume.cache_info())
#        s+=len(xyz)
        s+=(xyz)
#        print("A", a,b,(xyz))
#        print("A", a,b,len(xyz))


print("Part 2:",s)
