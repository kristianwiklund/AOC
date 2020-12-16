from tmp import check
import fileinput

for line in fileinput.input():
    line=line.strip("\r\n")
    logicz=list()
    for p in line.split(","):
        r=check(int(p))
        print(r)
        r=[y for (x,y) in r if x]
        logicz.append(r)
    print(logicz)

