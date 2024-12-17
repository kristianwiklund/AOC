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
lines = readlines("input")

ABC = [ints(lines[0])[0], ints(lines[1])[0], ints(lines[2])[0]]
P = ints(lines[4])

print(ABC)
print(P)

IP = 0

def combo(o):
    global ABC

    if o>3:
        return ABC[o-4]
    
    return o
        

while True:

    if IP>=len(P):
        break
    
    i = P[IP]
    IP+=1
    o = P[IP]
    IP+=1

#    print(IP-2,":",i,o)
    
    match i:

        case 0:
#            print("ADV")
            ABC[0] = ABC[0] // (2**combo(o))
#            print("ADV /",2**combo(o),"->",ABC[0])
        case 1:
            ABC[1] = ABC[1] ^ o
        case 2:
#            print("BST ->",ABC[1])
            ABC[1] = combo(o) % 8
        case 3:
#            print("JNZ ?",ABC[0],"->",o)
            if ABC[0]:
                IP = o
        case 4:
            ABC[1] = ABC[1] ^ ABC[2]
        case 5:
#            print("OUT",combo(o),o, "->",end="");
            print(combo(o)%8,end=",")
#            print("")
        case 6:
            ABC[1] = ABC[0] // (2**combo(o))
        case 7:
            ABC[2] = ABC[0] // (2**combo(o))

    
    
