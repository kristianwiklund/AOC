#!/usr/bin/python3
import sys

X = [t.strip() for t in sys.stdin]
l = [[int(X[j][i]) for j in range(len(X))] for i in range(len(X[0]))]
g = int("".join(['1' if (sum(x)/len(X))>0.5 else '0' for x in l]),2)
e= (2**(len(X[0]))-1)-g

print (g*e)
