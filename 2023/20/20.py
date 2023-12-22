import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

q=[]

arr = readarray("input",split="->",convert=lambda x:x.strip())
arr = [(x[0][1:],x[0][0],[i.strip() for i in x[1].split(",")]) for x in arr]
ff = {x[0]:"low" for x in arr if x[1]=="%"}
cm = {x[0]:{} for x in arr if x[1]=="&"}
bc = [x[2] for x in arr if x[1]=="b"][0]
#print (bc)
net = {x[0]:x[2] for x in arr}
#print(net)
G=nx.DiGraph()
for x in net:
    for i in net[x]:
        G.add_edge(x,i)

p=nx.all_simple_paths(G,"roadcaster","vf")
p=list(p)
p=[item for sublist in p for item in sublist]
print(p)
H = nx.subgraph(G,p)

import pygraphviz
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot
#print(G.edges(data=True))
#print(G.nodes)

#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=labels)

cnt=0
cache=dict()
#write_dot(H, "maze.dot")

#nx.draw_spring(H,  with_labels=True)
#plt.savefig("maze_nwx.png")


#import sys
#sys.exit()

cmm={}

for x in net:
#    print(x,net[x])
    for y in net[x]:
        if y in cm:
#            print (y,cm[y])
            cm[y][x]="low"

def press(bc, q):
    for i in bc:
        q.append((i,"low","roadcaster"))
    

def tick(ff,cm, net, q, bp):
    global cnth, cntl
    global cmm
    
    while True:

        try:
            e = q.pop(0)
#            print(e)
        except:
            break

        if e[0]=="rx" and e[1]=="low":
            print("Part 2:",e[0],e,bp)
            break

#        if e[0]=="rx":
#            print(bp, e)
        
        if e[1]=="low":
            cntl+=1
        elif e[1]=="high":
            cnth+=1
        else:
            print("dafuq",e)
        
 #       print(e[2],"-",e[1],"->",e[0])
        
        if e[0] in ff and e[1]=="low":
            ff[e[0]]="low" if ff[e[0]]=="high" else "high"
            for i in net[e[0]]:
                q.append((i, ff[e[0]], e[0]))
        elif e[0] in ff and e[1]=="high":
            pass #nothing happens
        elif e[0] in cm:
            cm[e[0]][e[2]]=e[1]
            o=False
            a=True
  #          print("  [con] ->",e[0],"<-", cm[e[0]],end="")

            for i in cm[e[0]]:
                 if cm[e[0]][i]=="high":
                    o=True
                 else:
                    a=False
                
            if a:
                cmm[e[0]]="low"
                for i in net[e[0]]:
                    q.append((i, "low", e[0]))
   #                 print("--> low")
            else:
                cmm[e[0]]="high"
                for i in net[e[0]]:
                    q.append((i, "high", e[0]))
    #                print("--> high")
        else:
            pass
            #if e[0]!="output":
            #    print("************ dafuq2",e)
            #    print("cm",cm)
            #    print("ff",ff)
            
    #print("---")
    #print("ff:",ff)
    #print("cm:",cm)
    #print("---")

cnth=0
cntl=1000

for i in range(1000):
    press(bc, q)
    tick(ff,cm,net, q,i)


print(cnth, cntl, cnth*cntl)
assert(cnth*cntl>86325428)

goff=[]


while True:
    press(bc, q)
    tick(ff,cm,net, q,i)
    s=""
    for ii in ff:
        if ff[ii]=="high":
            s+="1"
        else:
            s+="0"
            
    for ii in cmm:
        if cmm[ii]=="high":
            s+="1"
        else:
            s+="0"
            
#    print(s)
    goff.append(s)
    i+=1
    if len(goff)>2000000:
        break

cnt={i:0 for i in range(len(ff)+len(cm))}
for x in range(1,len(goff)):
    g=goff[x]
    gg=goff[x-1]
    for i in range(len(g)):
        if g[i]!=gg[i]:
            cnt[i]+=1

print(cnt)

from scipy.fft import fft

bo = sorted(range(len(ff)+len(cm)),key=lambda x:cnt[x])

print(bo)

cnt={i:0 for i in range(len(ff)+len(cm))}

xo = ["rx","vf","hf","pm","mk","pk"]
while True:
    press(bc, q)
    tick(ff,cm,net, q,i)
    s=""
    for ii in ff:
        if ff[ii]=="high":
            s+="1"
        else:
            s+="0"

    for ii in cmm:
        if cmm[ii]=="high":
            s+="1"
        else:
            s+="0"
            
    #    for i in range(len(ff)):
    #        if s[i]=="1":
    #            cnt[i]+=1
    #        else:
    #            cnt[i]-=1
    
    #        print(f'{cnt[i]:>5}',end="")

    for ii in bo:
        print(s[ii],end="")
    print("")
    
    i+=1
