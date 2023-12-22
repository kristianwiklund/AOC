import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

arr = readarray("input.short",split="{",convert=lambda x:x.strip("}"))
#lines = readlines("input")
#print(arr)

G = nx.DiGraph()

for i in range(len(arr)):
    if len(arr[i][0])==0:
        break
    
    a=arr[i]
    if a[0]=="in":
        a[0]="_in"

    print ("def",a[0]+"(x,m,a,s):")

    for j in a[1].split(","):

        if ">" in j or "<" in j:
            t = j.split(":")
            print ("  if",t[0],":")
            print ("    return "+t[1]+"(x,m,a,s)")
            G.add_edge(a[0],t[1],rule=t[0])

        else:
            print("  return",j+"(x,m,a,s)")
            G.add_edge(a[0],j,rule=True)
    print("")

print ("___ss=0")
print("def A(x,m,a,s):")
print("  global ___ss")
print("  ___ss+=x+m+a+s")
#print("  return \"\"")
print("  return (\"A\",x,m,a,s,x+m+a+s)")
print("")

print("def R(x,m,a,s):")
print("  return ''")
#print("  return (\"R\",x,m,a,s,)")
print("")

for j in range(i+1,len(arr)):
#    print (arr[j])
    j=arr[j][1]
    print ("v=(_in(",j,"))")
    
print("print(\"part 1:\",___ss)")
#rint(len(G))
v=list(nx.all_simple_paths(G,"_in","A"))
#rint(v)
#v=set([i for x in v for i in x])
#G = G.subgraph(v)
#print(len(G))

#for x in G:
#    for e in (G.edges([x])):
#        if G.get_edge_data(e[0],e[1]):
#            print (e,G.get_edge_data(e[0],e[1])["rule"])

zz=[]
az=[]
from sympy import symbols, reduce_inequalities, solveset, solve, simplify
x = symbols("x")
m = symbols("m")
a = symbols("a")
s = symbols("s")

for xxx in v:
    z=["x>=1,m>=1,a>=1,s>=1,x<=4000,m<=4000,a<=4000,s<=4000"]
    for y in range(len(xxx)-1):
        p = G.get_edge_data(xxx[y],xxx[y+1])["rule"]
        if p!= True:
            z.append(p)
        
    #    zz.append(reduce_inequalities(z,[x,m,a,s]))
    zz.append(",".join(z))
#    az.append(z)
#print(zz)

for xxx in zz:
    print(reduce_inequalities(eval(xxx)))
