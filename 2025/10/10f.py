import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from copy import copy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
import numpy as np
#import scipy
from functools import cache
from functools import lru_cache
import itertools
#import scipy
#import sympy
#from shapely.geometry.polygon import Polygon
#from shapely import contains

#arr = readarray("input.shortest",split="",convert=lambda x:x)
lines = readlines("input.short")

def tf(button,ln):

    ack=[]
    for i in range(ln):
        ack.append(1 if i in button else 0)

    return (ack)

assert(tf([0,2],4)==[1,0,1,0])

def pl(l):
    x,y=l.split("]")
    y,z=y.split("{")
    #    print(x,y,z)

    #m = [list(x.replace("[","")),eval("("+y.lstrip().rstrip().replace(" ",",")+")"),eval("["+z.strip().replace("}","]"))]
    m = [list(x.replace("[","")),eval("["+y.lstrip().rstrip().replace(" ",",").replace("(","[").replace(")","]")+"]"),eval("["+z.strip().replace("}","]"))]

    m[1] = [tf(x,len(m[2])) for x in m[1]]
    
    return m

lines=[pl(x) for x in lines]

def murkla(knappar, knapp, target, summa, tryck):
    global a
    global kossa

    if kossa and tryck>kossa:
        print(" "*knapp,kossa,">",tryck,"<",nysumma, target)                    
        return False
    
    if knapp>=len(knappar):
        return False

    if (summa>target).any():
        return False

    if (summa==target).all():
        return tryck

    if knappar==[]:
        return False


    
#    kossa=None

#    print(" "*knapp,kossa,tryck,summa)
    

    #
    nysumma = copy(summa)            
    for i in range(knappar[knapp]+1):
        for n in range(len(nysumma)):
            nysumma[n]+=a[n][knapp]
            if nysumma[n] > target[n]:
                return False

        # move one knapp upwards
        kalv = murkla(knappar,knapp+1, target, nysumma, tryck+i)
        if kalv:
            if not kossa:
                kossa=kalv
            elif kossa<kalv:
                kossa=kalv
                print("muu:",kossa)

    return kossa

#print(murkla(knappnytt, 0, b, [0]*len(b),0))



def karate(l):
        
    a = np.array(l[1])
    #    pprint(a)
    a = np.transpose(a)
    b = np.array(l[2])
    
    for i,v in enumerate(a):
        #        print (v,"=",b[i])
        
        knappnytt=[100000]*len(a[0])
        #        print(knappnytt)


        for i,v in enumerate(a):
            #            print (v,"=",b[i])
            print(".",end="")
            for x in range(len(knappnytt)):
                if v[x]:
                    knappnytt[x]=min(knappnytt[x],b[i])
                    
    return (knappnytt, a,b)

kossa=False

s=0
ttt=0
for l in lines:
#    print(l)
    print(ttt,"...",end="")
    ttt+=1
    print("calculating knappnytt...")
    knappnytt,a,b = karate(l)
    print("searching for svamp...")
    kossa = sum(b)
    x = murkla(knappnytt, 0, b, [0]*len(b), 0)
    s+=x
    print(x)

print(s)
