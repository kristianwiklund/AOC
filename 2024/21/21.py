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
        #        print(i,"->",j,":",len(pths))
        numpad[i,j]=[]
        for pth in pths:                        
            eal = "".join([G[pth[i]][pth[i+1]]['d'] for i in range(len(pth[:-1]))])+"A"
            numpad[i,j].append(eal)
        
#print(numpad)
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
        #        print(i,"->",j,":",len(pths))
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

#
#print("NP",numpush("029A"))
dirprev=["A","A"]

def dph(s,n):
    global dirpad
    global dirprev
    m=[]
    #    print(s)

    for i in s:
        if dirprev[n]==i:
            m.append("A")
        else:
            pprint(dirpad)
            print("s:",s)
            print("i:",i)
            print(dirpad[dirprev[n],i])
            m.append(dirpad[dirprev[n],i])
            
        dirprev[n]=i

    return m

def dirpush(s,n):
 #   print(s)
    m=[]
    for j in s:
        for i in j:
  #          print(i)
            m.append(dph(i,n))

    return m

    
    
    
def encode(s):
    numprev="A"
    posprev=["A","A"]

#    print("NP  ----")
    a = numpush(s)
    a = flattenwithbranches(a)
    print("a",a)
    n = dirpush(a,0)
    n = flattenwithbranches(n)
#    print(n)
    n = dirpush(n,1)
#    n = flattenwithbranches(n)
    
    return(a,n)

a,n=encode("379A")
print("----->>>",a)

n=flattenwithbranches(n)
#print("-----<<<",n)
pprint(min([len (i) for i in n]))
sys.exit()

sc=0
for i in lines:    
    s=dirpush(dirpush(numpush(i),0),1)
    c=decodenum(decodedir(decodedir(s)))
    assert(c==i)
    
    v=ints(i)[0]
#    print(len(s),"*",v)
    sc+=len(s)*v

#print(sc)
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

