import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
import numpy as np

def decodeme(arr,modified=False):
    arr = np.matrix(arr)
    arr = arr.transpose()

    if not modified:
        s = "".join([list(reversed(sortdictbykey(dict((x, data.count(x)) for x in data))))[0][0] for data in arr.tolist()])
    else:
        s = "".join([list((sortdictbykey(dict((x, data.count(x)) for x in data))))[0][0] for data in arr.tolist()])    
    return (s)

arr = readarray("input.short",split="",convert=lambda x:x)
assert(decodeme(arr)=="easter")

assert(decodeme(arr,modified=True)=="advent")

arr = readarray("input.long",split="",convert=lambda x:x)
print("Password A:",decodeme(arr))
print("Password B:",decodeme(arr,modified=True))


