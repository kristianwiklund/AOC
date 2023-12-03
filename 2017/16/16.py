import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np
#import scipy
from functools import cache
import time

#lines = readlines("input.short")

p = "abcde"

@cache
def run(fn, p):
    arr = readarray(fn,split=",",convert=lambda x:x)
    
    for l in arr:
        for c in l:
            v=sorted(ints(c))
            if c[0]=='s':
                #                s = v[0]%len(p) # there are no spins longer than p
                s=v[0]
                if s!=len(p):
                    p = p[-s:]+p[:-s]
            elif c[0]=='x':
                p = p[:v[0]] + p[v[1]] + p[v[0]+1:v[1]] + p[v[0]] + p[v[1]+1:]
                                
            else:
                p1 = p.index(c[1])
                p2 = p.index(c[3])
                v = sorted([p1,p2])
                p = p[:v[0]] + p[v[1]] + p[v[0]+1:v[1]] + p[v[0]] + p[v[1]+1:]

    return p

assert(run("input.short","abcde")=="baedc")
assert(run("input.short.2","abcde")=="baedc")
v = run("input.txt","abcdefghijklmnop")

assert(v!="paedcbfghijklmno")
assert(v=="lbdiomkhgcjanefp")
print("Part 1:",v)

p = "abcdefghijklmnop"
#p = "abcde"
op = p
cnt=0
a=[]

while True:
    a.append(p)
    np = run("input.txt",p)
        
    if np==op:
        break 
    p = np
    cnt+=1

b = set(a)
if len(b)!=len(a):
    print("repetition inside the list, other solution needed")
    
pprint(a)
print("cycle:",cnt)
o = 1000000000%(cnt-1)
print("offset at 1bn:",o)
#print("second iteration:",a[2%cnt])

print("part 2, not brute force:",a[o])
print("real answer, index in a:",a.index("ejkflpgnamhdcboi"))

# brute force

cnt=0
ttt=time.time()
while True:
    p = run("input.txt",p)
    cnt+=1
    if cnt>1000000000:
        print("Part 2, brute force:",p)
        break
    if not (cnt%1000000):
        print(time.time()-ttt,cnt)

assert(a[1]=="lbdiomkhgcjanefp")
assert(a[o]!="nopdabcefghijklm")
assert(a[o]!="mnodpaecbfghijkl")
assert(a[o]!="gejfkohmdabicnpl")
assert(a[o]!="mbjlkpecianhodgf")
assert(a[o]=="ejkflpgnamhdcboi")
