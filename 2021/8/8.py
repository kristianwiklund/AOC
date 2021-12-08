#!/usr/bin/python3

import sys,numpy

symbols = {2:1,4:4,3:7,7:8}
cnt = [0,0,0,0,0,0,0,0,0,0]

f = [t.strip() for t in sys.stdin]

for t in f:
#    print(t)
    b = t.split(" | ")[1]

    for i in b.split(" "):
        if len(i) in symbols:
            cnt[len(i)] = cnt[len(i)] + 1

print ("Answer 1:",sum(cnt))

#---

thesum=0

for t in f:
    dec = dict()

    keys = [set(i) for i in sorted(t.split(" | ")[0].split(),key=len)]
    disps = [set(i) for i in t.split(" | ")[1].split()]
    dec[8] = keys.pop(9) # abcdefg
    dec[4] = keys.pop(2) # bcdf
    dec[7] = keys.pop(1) # acf
    dec[1] = keys.pop(0) # cf

    abcdefg = dec[8]
    cf = dec[1]
    acf = dec[7]
    bdeg = abcdefg - acf
    bcdf = dec[4]
    a = acf - cf
    bd = bcdf - cf
    eg = abcdefg - acf - bcdf

    abd = a | bd
    abcdf = abd | cf

    abdeg = a | bdeg
    abcdf = a | bcdf

    
    # we can easily find 5,2,3 with what we know
    for i in range(len(keys)):
        if len(keys[i]) == 5:
            if len(abd & keys[i]) == 3:
                abdfg = keys[i]
                dec[5] = keys[i]
            elif len(abdeg & keys[i]) == 4:
                acdeg = keys[i]
                dec[2] = keys[i]
            elif len(abcdf & keys[i]) == 4:
                acdfg = keys[i]
                dec[3] = keys[i]

    keys = filter(lambda x:len(x)!=5, keys)

    b = abdfg - acdfg
    e = acdeg - acdfg
    f = acdfg - acdeg

    dec[0] = a | b | cf | eg
    dec[6] = dec[5] | e
    dec[9] = dec[3] | b

    goff=""
#    print ("---",disps)
    for i in disps:
        for j in dec:
            if dec[j] == i:
                #print(j,"[",dec[j],i,"]",end='\n')
                goff=goff+str(j)
                break
    #print(goff)
    thesum=thesum+int(goff)

print("Answer 2:",thesum)
