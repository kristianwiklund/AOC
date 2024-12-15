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

#arr = readarray("input.short",split="",convert=lambda x:x)
#lines = readlines("input.short")

with open("input","r") as fd:

    arr = readblock(fd, convert=lambda x:[x for x in x])
    b = readblock(fd, convert=lambda x:[x for x in x])

    b = [x for xs in b for x in xs]
    print(b)

    print(arr)


    # bump everything
    def storpotat(arr, x,y, d):

        s=[]
        xx=x
        yy=y

        # collect items between @ and the first #
        while arr[yy][xx]!="#":
            s.append(arr[yy][xx])
            yy+=dirs[d][1]
            xx+=dirs[d][0]

        if len(s)==0:
            return

#        print("a:",s)

        # move @ and all O immediately in front of it one step in d if there is a .
        if not "." in s:
            return

        m=[]
        for i in range(len(s)):

            if s[i]==".":
                break

            m.append(s[i])

#        print("m",m)
            
        s = ["."]+m+s[1+len(m):]
#        print("s",s)

        xx=x
        yy=y
        
        for i in s:
            arr[yy][xx]=i
            yy+=dirs[d][1]
            xx+=dirs[d][0]
        

    def gps(arr):
        v = findinarray(arr,"O", all=True)
        s = [100*y+x for (x,y) in v]
        print(s)
        print(sum(s))
            
    t = {'^':0,'>':1,'v':2,'<':3}
#    printpath(p=[], background=arr)
    print("--")
    for dd in b:
        #print(dd)
        d=t[dd]
        
        (x,y)=findinarray(arr,"@")

        storpotat(arr, x, y, d)
        print(".",end="")
        #        printpath(p=[], background=arr)
        #        print("--")
            

    print("")
    gps(arr)
