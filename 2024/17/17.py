import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.short")

ABC = [ints(lines[0])[0], ints(lines[1])[0], ints(lines[2])[0]]
P = ints(lines[4])

print(ABC)
print(P)


def combo(o):
    global ABC

    if o>3:
        return ABC[o-4]
    
    return o

def run(ABC,P):
#    global ABC
    IP = 0
    
    output=[]
    
    while True:

        if IP>=len(P):
            return output
    
        i = P[IP]
        IP+=1
        o = P[IP]
        IP+=1

    
        match i:

            case 0:
                ABC[0] = ABC[0] // (2**combo(o))
            case 1:
                ABC[1] = ABC[1] ^ o
            case 2:
                ABC[1] = combo(o) % 8
            case 3:
                if ABC[0]:
                    IP = o
            case 4:
                ABC[1] = ABC[1] ^ ABC[2]
            case 5:
                output.append(combo(o)%8)
            case 6:
                ABC[1] = ABC[0] // (2**combo(o))
            case 7:
                ABC[2] = ABC[0] // (2**combo(o))

    
PQI = ABC

q = 0

while True:
    q=q+1
#    print(q)
    ABC = deepcopy(PQI)
    ABC[0]=q
    r = run(ABC,P)
    if r==P:
        print ("match", q)
        print (r,P)
        break
#    print(q,r,P)
    if not q%100000:
        print(q)
