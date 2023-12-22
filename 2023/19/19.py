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

v=list(nx.all_simple_paths(G,"_in","A"))
print(v)
#v=set([i for x in v for i in x])
#print(len(G),G.nodes())

#G = G.subgraph(v)
print(len(G),G.nodes())

def irn(G,x, vs):

    for i in G.successors(x):
        p = G.get_edge_data(x,i)["rule"]
        if p==True:
            continue
        d = ints(p)[0]

<<<<<<< HEAD
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
=======
        if p[1]==">": # <=
            vs[p[0]][1]=min(vs[p[0]][1],d+1)
        else: # >=
            vs[p[0]][0]=max(vs[p[0]][0],d-1)

    return vs
    
ss=0
for i in v:
    vs = {i:{0:1,1:4000} for i in "xmas"}
    for j in range(len(i)-1):
        p = G.get_edge_data(i[j],i[j+1])["rule"]
        if p==True:
            # this corresponds to ALL restrictions from ALL other edges, inverted
#            print("vs(pre)=",vs)
            vs=irn(G,i[j],vs)
#            print("vs=",vs)
            continue
#        print(p,vs)
        d = ints(p)[0]
#        print(d)
        if p[1]==">":
            vs[p[0]][0]=max(vs[p[0]][0],d)
        else:
            vs[p[0]][1]=min(vs[p[0]][1],d)            
            
    cc=1
    print(i)
    print(vs)
    for x in vs:
        cc*=vs[x][1]-vs[x][0]
    ss+=cc

print(ss)
>>>>>>> 4d22ed69dc76757adf0d2bf1de2f7853616c03ed
