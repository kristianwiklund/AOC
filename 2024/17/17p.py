import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#import matplotlib.pyplot as plt
from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input")

ABC = [ints(lines[0])[0], ints(lines[1])[0], ints(lines[2])[0]]
P = ints(lines[4])
PC=0

def combo(o):
    if o<4:
        return o
    else:
        return "ABC"[o-4]

print("A=",ABC[0])
print("B=",ABC[1])
print("C=",ABC[2])
print("P=","\""+"".join([str(x) for x in P])+"\"")

print("def run(A):")

while True:

    if PC >= len(P):
        break
    
    i = P[PC]
    o = P[PC+1]
    PC+=2


    match i:
        case 0:
            print("  A=A // (2**",combo(o),")")
        case 1:
            print("  B=B ^",o)
        case 2:
            print("  B=",combo(o),"% 8")
        case 3:
            print ("  # goto ",o)
        case 4:
            print("  B=B^C")
        case 5:
            print("  P=",combo(o)," % 8")
            #print("  print (",combo(o)," % 8)")
        case 6:
            print("  B=A // (2**",combo(o),")")
        case 7:
            print("  B=A // (2**",combo(o),")")
            
print("  return (A,P)")
print("")
print("def d(A):")
print(" S=\"\"")
print(" while True:")
print("  (A,P) = run (A)")
print("  S+=str(P)")
print("  if not A:")
print("    break")
#print(" print(S)")
print(" return(S)")
print("")
print("c=10000000000000")
print("while True:")

print(" s = d(c)")
print(" if s==P:")
print("   print(c,P)")
print("   break")
print(" c+=1")
print(" if not c%100000:")
print("   print(c,s,len(s))")
print(" if len(s)>len(P):")
print("  print(s,P)")
