#!/usr/bin/python3
import sys,re

X = [t.strip() for t in sys.stdin]

def tp(X):

    l = [[int(X[j][i]) for j in range(len(X))] for i in range(len(X[0]))]
    m = ['1' if (sum(x)/len(X))>=0.5 else '0' for x in l]
    return m

g = int("".join(tp(X)),2)
e= (2**(len(X[0]))-1)-g

print (g*e)

V = X
p = ""
c=0
for i in range(len(V)):
    m = tp(V)[c]
    V=list(filter(lambda x: re.match(p+m,x),V))
    p=p+"."
    c=c+1
    #print (V)
    if len(V) == 1:
        break

oxgr = int(V[0],2)

V = X
p = ""
c=0
for i in range(len(V)):
    m = tp(V)[c]
    m = '1' if m=='0' else '0'
    V=list(filter(lambda x: re.match(p+m,x),V))
    p=p+"."
    c=c+1
    #print (V)
    if len(V) == 1:
        break

cosr = int(V[0],2)

print (cosr*oxgr)
