from tmp import check
import fileinput

li = list()
for line in fileinput.input():
    line=line.strip("\r\n")

    keep = True
    logicz=list()
    for p in line.split(","):
        r=check(int(p))

        r=[y for (x,y) in r if x]
        logicz.append(set(r))
        if not r:
            keep=False
            break
        
    if keep:
        li.append(logicz)    


bork = list()
for i in range(0,len(li[1])):

    s = li[0][i]
    
    for j in range(1,len(li)):
        s=s&li[j][i]

    bork.append(s)


bork = [(len(x),x) for x in bork]
bork = zip(bork, range(0,len(bork)))


kork = list()
bork = sorted(bork,key=lambda x:x[0][0])

while len(bork):
    bork = sorted(bork,key=lambda x:x[0][0])
    kork.append(bork[0])
    bork = [((x[0][0],x[0][1]-bork[0][0][1]),x[1]) for x in bork[1:]]


v = [z for ((x,y),z) in kork if "departure" in list(y)[0]]


ticket = [61,101,131,127,103,191,67,181,79,71,113,97,173,59,73,137,139,53,193,179]
p = 1

for i in v:
    p=p*ticket[i]

print(p)
