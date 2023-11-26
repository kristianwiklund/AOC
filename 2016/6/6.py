import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
import numpy as np

def decodeme(arr):
    arr = np.matrix(arr)
    arr = arr.transpose()
    s = "".join([list(reversed(sortdictbykey(dict((x, data.count(x)) for x in data))))[0][0] for data in arr.tolist()])
    return (s)

arr = readarray("input.short",split="",convert=lambda x:x)
assert(decodeme(arr)=="easter")

arr = readarray("input.long",split="",convert=lambda x:x)
print("Password:",decodeme(arr))
