#!/usr/bin/python3

from input import input
from input import tokens
import re
import networkx as nx

G = nx.DiGraph()

sum=0
bop = list()
s = input()
t = tokens()

all = set()

for i in tokens():
    r = t[i]

    for rr in r:
        all|=set([s[:m.start()] + rr + s[m.end():] for m in re.finditer(i,s)])

print(all)
print("Answer to 1: ",len(all))
