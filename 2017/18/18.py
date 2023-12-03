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

arr = readarray("input",split=" ",convert=lambda x:x)

pc=0
reg=dict()
sound=0

def getval(reg, val):

    try:
        return int(val)
    except:
        try:
            return reg[val];
        except:
            return 0

while True:

    if pc>=len(arr):
        print ("END")
        break

    print(arr[pc])
    i =arr[pc][0]
    o1 = arr[pc][1]
    if len(arr[pc])>2:
        o2 = arr[pc][2]

    
    match i:
        case "snd":
            print ("play sound", getval(reg, o1))
            sound=getval(reg, o1)
        case "set":
            reg[o1]=getval(reg, o2)
        case "add":
            reg[o1]=getval(reg, o1) + getval(reg, o2)
        case "mul":
            reg[o1]=getval(reg, o1) * getval(reg, o2)
        case "mod":
            reg[o1]=getval(reg, o1) % getval(reg, o2)
        case "rcv":
            v = getval(reg, o1)
            if v!=0:
                print ("rcv",v,"=",sound)
                break
        case "jgz":
            v = getval(reg, o1)
            if v>0:
                pc+=getval(reg, o2)
                continue

    pc+=1
    

