from tmp import check
import fileinput

li = list()
for line in fileinput.input():
    line=line.strip("\r\n")

    keep = True
    logicz=list()
    for p in line.split(","):
        r=check(int(p))
        #print(r)
        r=[y for (x,y) in r if x]
        logicz.append(set(r))
        if not r:
            keep=False
            break
        
    if keep:
        li.append(logicz)    
        #print(logicz)

#print(li)
bork = list()
for i in range(0,len(li[1])):
    #print("-")

    s = li[0][i]
    
    for j in range(1,len(li)):
        #print (li[j][i])
        s=s&li[j][i]

    bork.append(s)


bork = [(len(x),x) for x in bork]
kork = list()
bork = sorted(bork,key=lambda x:x[0])
#print (bork)    
while len(bork):
    bork = sorted(bork,key=lambda x:x[0])
    print(bork[0])
    kork.append(bork[0])
    bork = [(x,y-bork[0][1]) for (x,y) in bork[1:]]
    #    print (bork)

print(kork)
v = [x-1 for (x,y) in kork if "departure" in list(y)[0]]
print(v)

ticket = [61,101,131,127,103,191,67,181,79,71,113,97,173,59,73,137,139,53,193,179]
p = 1
for i in v:
    p=p*ticket[i]
# 627528901543 - low
print(p)
