import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#import numpy as np

arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.short")
