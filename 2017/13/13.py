import sys
sys.path.append("../..")
from utilities import *

a=readarray("input.txt",split=":",convert=lambda x:int(x))
a={x[0]:x[1] for x in a}
#print(a)
def tick(a):

    mp=-1
    sp={x:0 for x in a.keys()}
    dr={x:1 for x in a.keys()}
    
    #print("--")
    score=0
    #print(sp)
    while True:
        # move packet
        mp+=1
        
        # check if through
        if mp>max(sp.keys()):
            return score
        
        # check if caught

        if mp in sp and sp[mp]==0:
            score+=mp*a[mp]
           # print("* ",end="")
        #else:
        #    print("  ",end="")

        #if mp in sp:
        #    print(mp,sp)
        #else:
        #    print(mp,sp)
            
        # then move the scanners

        for d in a:
            sp[d]=(sp[d]+dr[d])
            
            if sp[d]<0 or sp[d]==a[d]:
                dr[d]=-dr[d]
                sp[d]=(sp[d]+2*dr[d])
                


print("Part 1:",tick(a))

