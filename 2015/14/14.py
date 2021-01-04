#!/usr/bin/python3

import sys

def decode(line):

    l = line.split(" ")

    x = [int(l[3]) for x in range(0,int(l[6]))]
    x = x + [0 for x in range(0,int(l[13]))]
    return (l[0],x)
    
    

with open(sys.argv[1],"r") as fd:

    lines = fd.readlines()
    h = dict()
    a = dict()
    sc = dict()
    
    for line in lines:
        (hest,l) = decode(line.strip("\n\r"))
        h[hest] = l
        a[hest] = 0
        sc[hest] = 0
        
    for i in range(0, int(sys.argv[2])):

        for hest in h:
            s = h[hest].pop(0)
            h[hest].append(s)
            a[hest] += s

        m = max(list(a.values()))
        who = [x for x in a if a[x]==m]

        for i in who:
            sc[i] += 1
            
    print(sc[sorted(sc,key=sc.get).pop()])

