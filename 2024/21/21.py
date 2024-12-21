import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
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

numpad={}

arr = readarray("numpad",split="",convert=lambda x:x)

for i in [str(x) for x in range(0,10)]+["A"]:
    for j in [str(x) for x in range(0,10)]+["A"]:
        x1,y1 = findinarray(arr,i)
        x2,y2 = findinarray(arr,j)
        
        dx = (x2-x1)//4
        dy = (y2-y1)//2

        if sign(dx)<0:
            sx=("<"*-dx)
        elif sign(dx)>0:
            sx=(">"*dx)
        else:
            sx=""

        if sign(dy)<0:
            sy=("^"*-dy)
        elif sign(dy)>0:
            sy=("v"*dy)
        else:
            sy=""

        if j=="A" or j=="0":
            s = sx+sy
        else:
            s = sy+sx

        
            
        
        numpad[i,j] = s

numprev = "A"
        
def numpush(s):
    global numpad
    global numprev
    m=""
    
    for i in s:
        m+=numpad[numprev,i]+"A"
        numprev=i
        
    return m

dirpad={}

arr = readarray("dirpad",split="",convert=lambda x:x)

for i in "<>^vA":
    for j in "<>^vA":
        x1,y1 = findinarray(arr,i)
        x2,y2 = findinarray(arr,j)
        
        dx = (x2-x1)//4
        dy = (y2-y1)//2

        if sign(dx)<0:
            sx=("<"*-dx)
        elif sign(dx)>0:
            sx=(">"*dx)
        else:
            sx=""

        if sign(dy)<0:
            sy=("^"*-dy)
        elif sign(dy)>0:
            sy=("v"*dy)
        else:
            sy=""

        if j=="<":
            s=sy+sx
            print(i,"to <",s,sx,sy,(x1,y1),(x2,y2))
        else:
            s=sx+sy
            
        dirpad[i,j] = s


dirprev = ["A","A","A"]

print("da",dirpad["A","<"])

def dirpush(s,n):
    global dirpad
    global dirprev
    m=""
    
    for i in s:
        m+=dirpad[dirprev[n],i]+"A"
        dirprev[n]=i
        
    return m


rnumpad={}
for i in numpad:
    rnumpad[i[0],"".join(sorted(numpad[i]))]=i[1]

#print(rnumpad)

rdirpad={}
for i in dirpad:
    rdirpad[i[0],"".join(sorted(dirpad[i]))]=i[1]
    if dirpad[i]!="".join(sorted(dirpad[i])):
        print ("boop", dirpad[i], "".join(sorted(dirpad[i])))

    
print("rdirpad",rdirpad)

s=dirpush(dirpush(numpush("029A"),0),1)

def decodedir(st):
    
    st = st.split("A")[:-1]
    
#    print("st",st)
    pos="A"

    n=""
    for i in st:
        i="".join(sorted(i))
        x=rdirpad[pos,i]
        pos=x
        n+=x
    return (n)

def decodenum(st):
    
    st = st.split("A")[:-1]
#    print("st",st)
    pos="A"

    n=""
    for i in st:
        i="".join(sorted(i))
        x=rnumpad[pos,i]
        pos=x
        n+=x
    return (n)

s=dirpush(dirpush(numpush("029A"),0),1)
print(len(s))
print(s)
print("s",s)
a = decodedir(s)
print("a",a)
b = decodedir(a)
print("b",b)
c = decodenum(b)
print("c",c)
assert(c=="029A")



sc=0
for i in lines:
    numprev="A"
    posprev=["A","A","A"]
    
    s=dirpush(dirpush(numpush(i),0),1)
    c=decodenum(decodedir(decodedir(s)))
    assert(c==i)
    
    v=ints(i)[0]
    print(len(s),"*",v)
    sc+=len(s)*v

print(sc)
assert(sc>211720)
assert(sc<224204)


#s = dirpush(dirpush(numpush("379A"),0),1)
#print(s,decodenum(decodedir(decodedir(s))))
#print("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",decodenum(decodedir(decodedir("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))))
print("----------------------")
print("       379A           ")
s = dirpush(dirpush(numpush("379A"),0),1)
t = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
print(s)
print(t)
print("--")
s=decodedir(s)
t=decodedir(t)
print(s)
print(t)
print("...")
s=decodedir(s)
t=decodedir(t)
print(s)
print(t)
print("...")
s=decodenum(s)
t=decodenum(t)
print(s)
print(t)

print(len([i for i,v in enumerate(s) if v=="A"]))
print(len([i for i,v in enumerate(t) if v=="A"]))

posprev=["A","A","A"]
print(dirpush("<",0))
