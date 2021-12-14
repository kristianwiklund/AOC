#!/usr/bin/python3

import sys
import re

rules={}
pairs={}
for l in sys.stdin:
    t = l.strip().split(" -> ")
    if len(t)==1 and len(t[0])>3:
        # template
        template=l.strip()
    elif len(t)==2:
        rules[t[0]]=t[1]
        pairs[t[0]]=0

for i in range(len(template)-1):
    q=template[i]+template[i+1]
    print (q,pairs)
    if q in pairs:
        pairs[q]+=1
    else:
        pairs[q]=1

def kroppkaka(pairs, rules):
    np={}
    #print("p",pairs)
    for x in pairs:
        if x in rules:
            if pairs[x]>0:
                p1=x[0]+rules[x]
                p2=rules[x]+x[1]
                if not p1 in np:
                    np[p1]=pairs[x]
                else:
                    np[p1]+=1
                if not p2 in np:
                    np[p2]=pairs[x]
                else:
                    np[p2]+=1
        else:
            np[x]=pairs[x]
    #print("np",np)
    return np
                
#print(pairs)
for i in range(1):
    pairs=kroppkaka(pairs,rules)
print(pairs)
