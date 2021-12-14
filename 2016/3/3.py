#!/usr/bin/python3

import sys

f = [l.strip().split() for l in sys.stdin]
n = []
for t in f:
    n.append([int(x) for x in t])

def f(t):
    
    v = ((t[0]+t[1])>t[2]) and ((t[0]+t[2])>t[1]) and ((t[1]+t[2])>t[0])
    return v
    
n = filter(f,n)

print(len(list(n)))
