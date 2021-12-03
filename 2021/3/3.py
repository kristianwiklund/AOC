#!/usr/bin/python3
import sys,re

X = [t.strip() for t in sys.stdin]

def tp(X):

    l = [[int(X[j][i]) for j in range(len(X))] for i in range(len(X[0]))]
    m = ['1' if (sum(x)/len(X))>=0.5 else '0' for x in l]
    return m

g = int("".join(tp(X)),2)
e= (2**(len(X[0]))-1)-g

print ("A:",g*e)

def fp(V,T):
    
    p = ""
    c=0
    for i in range(len(V)):
        m = T[tp(V)[c]]
        V=list(filter(lambda x: re.match(p+m,x),V))
        p=p+"."
        c=c+1
        if len(V) == 1:
            return (V[0])

oxgr = int(fp(X,{"1":"1","0":"0"}),2)
cosr = int(fp(X,{"1":"0","0":"1"}),2)
print ("B:", cosr*oxgr)
