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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

a = 65
af = 16807
b = 8921
bf = 48271

d = 2147483647 

def gen1(x, f):

    x*=f
    x%=2147483647

    return x

def gen2(x, f):
    x = x*f
    x = (x & 0x7fffffff)  + (x >> 31)
#    x = (x & 0x7fffffff) + (x >> 31)

    return x
    
assert(gen1(a, af)==1092455)
assert(gen1(b, bf)==430625591)

assert(gen2(a, af)==1092455)
assert(gen2(b, bf)==430625591)

c=0
for i in range(40000000):
    a = gen1(a, af)
    b = gen1(b, bf)

    if a&0xffff == b&0xffff:
        c+=1

assert(c==588)

c=0
a=512
b=191

for i in range(40000000):
    a = gen1(a, af)
    b = gen1(b, bf)

    if a&0xffff == b&0xffff:
        c+=1

print("1:",c)

aa=[]
bb=[]

while True:
    a = gen1(a, af)
    b = gen1(b, bf)
    if not a&3:
        aa.append(a)

    if not b&7:
        bb.append(b)

    if len(aa)>=5000000 and len(bb)>=5000000:
        break

cnt=0
for i in range(min(len(aa), len(bb))):
    if aa[i]&0xffff == bb[i]&0xffff:
        cnt+=1

print("Part 2:", cnt)
