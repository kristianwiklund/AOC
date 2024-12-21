import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#import matplotlib.pyplot as plt
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache


lines = readlines("input.short")

G = nx.DiGraph()

snumpad = ["789","456","123","X0A"]
sdirpad = ["X^A","<v>"]

bop="^>v<"

for y,l in enumerate(snumpad):
    for x,v in enumerate(l):
        if v=="X":
            continue
        
        G.add_node(v)
        a = checkallpos(snumpad,x,y,fun = lambda x:x!="X", outofbounds=False)
        for i,w in enumerate(a):
            if w:
                n = snumpad[y+dirs[i][1]][x+dirs[i][0]]
                if n!=v:
                    #print(v,"->",n)
                    G.add_edge(v, n, d=bop[i])
                
numpad={}        
for i in "".join(snumpad):
    for j in "".join(snumpad):
        if i=="X" or j=="X":
            continue
        if i==j:
            continue
        
        pths = list(nx.all_shortest_paths(G,i,j))
        print(i,"->",j,":",len(pths))
        numpad[i,j]=[]
        for pth in pths:                        
            eal = "".join([G[pth[i]][pth[i+1]]['d'] for i in range(len(pth[:-1]))])+"A"
            numpad[i,j].append(eal)
        
print(numpad)
G = nx.DiGraph()

for y,l in enumerate(sdirpad):
    for x,v in enumerate(l):
        if v=="X":
            continue
        
        G.add_node(v)
        a = checkallpos(sdirpad,x,y,fun = lambda x:x!="X", outofbounds=False)
        for i,w in enumerate(a):
            if w:
                n = sdirpad[y+dirs[i][1]][x+dirs[i][0]]
                if n!=v:
                    #print(v,"->",n)
                    G.add_edge(v, n, d=bop[i])
                
dirpad={}        
for i in "".join(sdirpad):
    for j in "".join(sdirpad):
        if i=="X" or j=="X":
            continue
        if i==j:
            continue
        
        pths = list(nx.all_shortest_paths(G,i,j))
        print(i,"->",j,":",len(pths))
        dirpad[i,j]=[]
        for pth in pths:                        
            eal = "".join([G[pth[i]][pth[i+1]]['d'] for i in range(len(pth[:-1]))])+"A"
            dirpad[i,j].append(eal)
        

numprev = "A"
        
def numpush(s):
    global numpad
    global numprev
    m=[]
    
    for i in s:
        m.append(numpad[numprev,i])
        numprev=i
        
    return m

print("NP",numpush("029A"))
dirprev=["A","A"]

def dirpush(s,n):
    global dirpad
    global dirprev
    m=[]
    
    for i in s:
        if dirprev[n]==i:
            m.append("A")
        else:
            m.append(dirpad[dirprev[n],i])

    return m

#print("DP",dirpush("<>^A",0))

# rnumpad={}
# for i in numpad:
#     rnumpad[i[0],"".join(sorted(numpad[i]))]=i[1]

# #print(rnumpad)

# rdirpad={}
# for i in dirpad:
#     rdirpad[i[0],"".join(sorted(dirpad[i]))]=i[1]
#     if dirpad[i]!="".join(sorted(dirpad[i])):
#         print ("boop", dirpad[i], "".join(sorted(dirpad[i])))
    
    
# print("rdirpad",rdirpad)

# s=dirpush(dirpush(numpush("029A"),0),1)

# def decodedir(st):
    
#     st = st.split("A")[:-1]
    
# #    print("st",st)
#     pos="A"

#     n=""
#     for i in st:
#         i="".join(sorted(i))
#         x=rdirpad[pos,i]
#         pos=x
#         n+=x
#     return (n)

# def decodenum(st):
    
#     st = st.split("A")[:-1]
# #    print("st",st)
#     pos="A"

#     n=""
#     for i in st:
#         i="".join(sorted(i))
#         x=rnumpad[pos,i]
#         pos=x
#         n+=x
#     return (n)

# s=dirpush(dirpush(numpush("029A"),0),1)
# print(len(s))
# print(s)
# print("s",s)
# a = decodedir(s)
# print("a",a)
# b = decodedir(a)
# print("b",b)
# c = decodenum(b)
# print("c",c)
# assert(c=="029A")

def genbobb(a):
    
    if len(a)==1:
        #print("<-genbobb:",a[0][0])
        return [a[0][0]]

    #print("genbobb:",a)
    
    ax = a[1:]
    a = a[0]
    #print(a,"|",ax)

    m=[]

    for i in a:
        #print("a=",i)
        v = genbobb(ax)
        for t in v:
            m.append(i+t)

    return m
    
    

def encode(s):
    numprev="A"
    posprev=["A","A"]

#    print("NP  ----")
    a = numpush(s)
    a = genbobb(a)
    print("genbobbarob",a)

    n = []

    for z in a:
        n.append(dirpush(z,0))

    print("nnnn:",n)
    for i in n:
        nn=genbobb(i)
        print("genbobbabob",nn)
    sys.exit()
    
    nn = {}
    for z in n.values():
        print("dp z",z)
        for x in z:
            print("dp x",x)
            b = dirpush(x,0)
            nn[x]=b
    print(nn)

    print("DP2:")
#    pprint(nn)
    
    return(a,n,nn)

a,n,nn=encode("029A")
print("vvv")
pprint(a)
print(".")
pprint(n)
print(".")
pprint(nn)
print("---")
sys.exit()

def ptbobb(v):

    for i,a in enumerate(v):
        print(i,a)
        for j,b in enumerate(a):
            print(i,j,b)
            for k,c in enumerate(b):
                print(i,j,k,c)
                for l,d in enumerate(c):
                    print(i,j,k,l,d)


def mkbobb(v,m=[]):
    pass
#    for i,a in enumerate(v):
#        m.append(

#ptbobb(v)
sys.exit()

sc=0
for i in lines:

    
    s=dirpush(dirpush(numpush(i),0),1)
    c=decodenum(decodedir(decodedir(s)))
    assert(c==i)
    
    v=ints(i)[0]
    print(len(s),"*",v)
    sc+=len(s)*v

print(sc)
#assert(sc>211720)

# s = dirpush(dirpush(numpush("379A"),0),1)
# print(s,decodenum(decodedir(decodedir(s))))
# print("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",decodenum(decodedir(decodedir("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))))

# s = dirpush(dirpush(numpush("179A"),0),1)
# t = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
# print("--")
# s=decodedir(s)
# t=decodedir(t)
# print(s)
# print(t)
# print("...")
# s=decodedir(s)
# t=decodedir(t)
# print(s)
# print(t)
# print("...")
# s=decodenum(s)
# t=decodenum(t)
# print(s)
# print(t)

# print(len([i for i,v in enumerate(s) if v=="A"]))
# print(len([i for i,v in enumerate(t) if v=="A"]))

