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
        #pairs[t[0]]=0

def gpairs(s):
    pairs={}
    for i in range(len(s)-1):
        q=s[i]+s[i+1]
        #print (q,pairs)
        if q in pairs:
            pairs[q]+=1
        else:
            pairs[q]=1

    return(pairs)

pairs = gpairs(template)
#print("ip", pairs)
            
def kroppkaka(pairs, rules, mydebug=False):
    np={}
    #print("p",pairs)
    for x in pairs:
        if x in rules:
            if pairs[x]>0:

                # these are the newly formed pairs
                p1=x[0]+rules[x]
                p2=rules[x]+x[1]
                # that replace the old pair
                if mydebug:
                    print(x, pairs[x], rules[x],p1,p2)
                    
                if not p1 in np:
                    np[p1]=pairs[x]
                else:
                    np[p1]+=pairs[x]
                    
                if not p2 in np:
                    np[p2]=pairs[x]
                else:
                    np[p2]+=pairs[x]
        else:
            np[x]=pairs[x]
    #print("np",np)
    return np
                
#print(pairs)

def calcutta(pairs, template):
    s={}

    for i in pairs:
        for j in i:
            if not j in s:
                s[j]=pairs[i]
            else:
                s[j]+=pairs[i]

    if not template[0] in s:
        s[template[0]]=1
    else:
        s[template[0]]=s[template[0]]+1

    if not template[-1] in s:
        s[template[-1]]=1
    else:
        s[template[-1]]=s[template[-1]]+1


    return(s)
    
if template=="NNCB":
    pairs=kroppkaka(pairs,rules)
    assert (pairs == gpairs("NCNBCHB"))
    pairs=kroppkaka(pairs,rules)
    assert (pairs == gpairs("NBCCNBBBCBHCB"))
    pairs=kroppkaka(pairs,rules,mydebug=False)
    try:
        assert (pairs == gpairs("NBBBCNCCNBBNBNBBCHBHHBCHB"))
    except:
        print(pairs)
        print(gpairs("NBBBCNCCNBBNBNBBCHBHHBCHB"))
        sys.exit()
              
    pairs=kroppkaka(pairs,rules)
    assert(pairs==gpairs("NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"))

    for x in range(36):
        pairs = kroppkaka(pairs,rules)
else:
    for x in range(40):
        pairs = kroppkaka(pairs,rules)
    
c=calcutta(pairs,template)

def kairo(c):
    d=sorted(c,key=lambda x:c[x],reverse=True)
    ans=int(c[d[0]])-int(c[d[-1]])
    return (d,ans)

(d,ans)=kairo(c)
print("Answer 2:", int(ans/2))


