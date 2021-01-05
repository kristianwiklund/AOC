#!/usr/bin/python3

def score(s,p,f,r):

    cap = max(0,5*s-p-r)
    dur = max(0,-s+3*p-f)
    flav = 4*f
    tex = 2*r

    sc =  cap*dur*flav*tex
    
    if cap <= 0 or dur <= 0:
        return 0


    return sc

maxx = 0

for s in range(0,101):
    for p in range(0,101):
        if p+s>100:
            continue
        
        for f in range(1,101):
            if p+s+f>100:
                continue
            
            for r in range(1,101):

                if p+s+f+r!=100:
                    continue
                                
                sc = score(s,p,f,r)
                if sc>maxx:
                    print(sc,s,p,f,r)
                    maxx = sc

print ("The answer to 1 is",maxx)
