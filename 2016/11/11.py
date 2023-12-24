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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

b = [set(),
     set(["LG"]),
     set(["HG"]),
     set(["HM", "LM"])]

# LH
# generators 11
# chips 11

bg = [0,0b10,0b01,0]
bc = [0,0,0,0b11]

def bigboom(g, c):
    return ((g^c)&c)!=0

assert(not bigboom(0b0,0b0))
assert(bigboom(0b110,0b011))
assert(not bigboom(0b11,0b10))

c = [set(),
     set(["TM"]),
     set(["TG", "RG", "RM", "CG", "CM"]),
     set(["SG", "SM", "PG", "PM"])]

e = 3

cg = [0, 0, 0b11100, 0b00011]
cc = [0, 0b10000, 0b01100, 0b00011]

# TRCSP
# generators 11111
# chips      11111


     
