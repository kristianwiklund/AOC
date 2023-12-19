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

arr = readarray("input",split="{",convert=lambda x:x.strip("}"))
#lines = readlines("input")
print(arr)

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

        else:
            print("  return",j+"(x,m,a,s)")

    print("")

print ("___ss=0")
print("def A(x,m,a,s):")
print("  global ___ss")
print("  ___ss+=x+m+a+s")
print("  return \"\"")
#print("  return (\"A\",x,m,a,s,x+m+a+s)")
print("")

print("def R(x,m,a,s):")
print("  return ''")
#print("  return (\"R\",x,m,a,s,)")
print("")

for j in range(i+1,len(arr)):
#    print (arr[j])
    j=arr[j][1]
    print ("print(_in(",j,"))")
    
print("print(\"part 1:\",___ss)")
