#!/usr/bin/python3

import sys
import re
import difflib

rules={}
for l in sys.stdin:
    t = l.strip().split(" -> ")
    if len(t)==1 and len(t[0])>3:
        # template
        template=l.strip()
    elif len(t)==2:
        rules[t[0]]=t[1]

def bopp(s,p,b):
    return s[:p]+b+s[p:]

def myfind(what, where):

    katt=[]
    for i in range(len(where)-1):
        if where[i]==what[0] and where[i+1]==what[1]:
            katt.append(i)
    return katt

def subst(s,r):

    ko = []

    for x in r:
        result = myfind(x, s)
        for t in result:
            ko.append((t+1,r[x],x))

    ko = sorted(ko,key=lambda x:x[0],reverse=True)

    for x in ko:
        s = bopp(s, x[0],x[1])
    return s

s = template

if template=="NNCB":
    s=subst(s,rules)
    assert(s=="NCNBCHB")

    s=subst(s,rules)
    assert(s=="NBCCNBBBCBHCB")

    s=subst(s,rules)
    assert(s=="NBBBCNCCNBBNBNBBCHBHHBCHB")

    s=subst(s,rules)
    assert(s=="NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB")

    s=subst(s,rules)
    assert(len(s)==97)

    s=subst(s,rules)
    s=subst(s,rules)
    s=subst(s,rules)
    s=subst(s,rules)
    s=subst(s,rules)

    assert(len(s)==3073)
else:
    for i in range(10):
        s=subst(s,rules)


def calcutta(s):
    
    c={}
    for i in range(len(s)):
        if s[i] in c:
            c[s[i]]+=1
        else:
            c[s[i]]=1
    return (c)

c= calcutta(s)

if template=="NNCB":
    assert(c["B"]==1749)
    assert(c["C"]==298)
    assert(c["H"]==161)
    assert(c["N"]==865)

def kairo(c):
    d=sorted(c,key=lambda x:c[x],reverse=True)
    ans=int(c[d[0]])-int(c[d[-1]])
    return (d,ans)

(d,ans)=kairo(c)

if template=="NNCB":
    assert(ans==1588)
    
print("Answer 1:",ans)



