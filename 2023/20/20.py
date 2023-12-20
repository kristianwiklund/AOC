import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
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
    
    while True:

        try:
            e = q.pop(0)
#            print(e)
        except:
            break

        if e[0]=="rx" and e[1]=="low":
            print("Part 2:",e[0],e,bp)
            break

        if e[0]=="rx":
            print(bp, e)
        
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
                for i in net[e[0]]:
                    q.append((i, "low", e[0]))
   #                 print("--> low")
            else:
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

while True:
    press(bc, q)
    tick(ff,cm,net, q,i)
    i+=1
