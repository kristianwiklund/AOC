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

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = [int(x) for x in readlines("input")]

def sauce(n):

    a=n
    b=((64*a)^a)%16777216
    c=((b//32)^b)%16777216
    d=((c*2048)^c)%16777216
    
    return d


assert(42^15==37)
assert(100000000%16777216==16113920)

tlist=[15887950,16495136,527345,704524,1553684,12683156,11100544,12249484,7753432,5908254]

sn=123

for i in range(10):
      sn=sauce(sn)
      assert(sn==tlist[i]) 
    

#--------------------

def bop(sn):
    for i in range(2000):
        sn=sauce(sn)

    return sn

assert(bop(1)==8685429)
assert(bop(10)==4700978)
assert(bop(100)==15273692)
assert(bop(2024)==8667524)

nums=[bop(x) for x in lines]
print("A:",sum(nums))

#-------------------

def seq(sn,cnt=2000):
    meh=[]
    p=sn%10
    
    for i in range(cnt):
        sn=sauce(sn)
        meh.append(sn%10-p)
        p=sn%10
    return meh

def prsq(sn,cnt=2000):
    meh=[]
    p=sn%10
    meh.append(p)
    
    for i in range(cnt):
        sn=sauce(sn)
        meh.append(sn%10)
    return meh

ap = seq(123,cnt=10)
assert(ap==[-3, 6, -1, -1, 0, 2, -2, 0, -2, 2])

#---------------------

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def seqtopat(seq):
    mupp = list(sliding_window_view(np.array(seq),4))
    mapp = [[str(x) for x in y] for y in mupp]
    tapp = ["|".join(x) for x in mapp]
    
    return tapp

def pattoprice(seq,pat,price):

    try:
        idx = seq.index(pat)+4
    except ValueError:
        return 0
    #print("seq",idx)
    
    #if len(price)>idx:
    return(price[idx])
    #else:
    #    return 0

apsq={}
apsw={}
appr={}
appa={}

for i,v in enumerate(lines):#[1,2,3,2024]):
#for i,v in enumerate([123,123,123,123]):#[1,2,3,2024]):
    appr[i]=prsq(v)
    apsq[i]=seq(v)
    apsw[i]=seqtopat(apsq[i])

grappa=dict()
for i in range(len(appr)):
    appa[i]={x:1 for x in apsw[i] if x}
    grappa = grappa|appa[i]
    
#tappa = {x:(appa[0].get(x,0)+appa[1].get(x,0)+appa[2].get(x,0)+appa[3].get(x,0)) for x in grappa}
#tappa = {x:tappa[x] for x in tappa if tappa[x]>0}
kappa = {x:sum([pattoprice(apsw[i],x,appr[i]) for i in range(len(apsw))]) for x in grappa}


#x="-2|1|-1|3"
x="3|-3|2|6"
#for i in range(4):
#    print(pattoprice(apsw[i],x,appr[i]))

#print(sorted(kappa.items(), key = lambda item: item[1])[-3:])
print(max(kappa.values()))
# 27==False
#print(apsw[0])
