#!/usr/bin/python3
import sys,numpy

lines = [t.replace(" -> ",",").strip() for t in sys.stdin]
points = [{"x1":int(t[0]),"y1":int(t[1]),"x2":int(t[2]),"y2":int(t[3])} for t in [t.split(",") for t in lines]]

# --

def pr(W):
    W = numpy.transpose(W)
    for x in W:
        for y in x:
            if y==0:
                print(".",end='')
            else:
                print(int(y),end='')
        print("")
        
W = numpy.zeros(shape=(1000,1000))

vertic = list(filter(lambda p: (p["x1"] == p["x2"]), points))
horiz = list(filter(lambda p: (p["y1"] == p["y2"]), points))
#print (horiz)
#print (vertic)

for v in vertic:
    maxy = max(v["y1"],v["y2"])
    miny = min(v["y1"],v["y2"])

    for i in range(miny, maxy+1):
        W[v["x1"]][i] = W[v["x1"]][i] + 1

for h in horiz:
    maxx = max(h["x1"],h["x2"])
    minx = min(h["x1"],h["x2"])

    for i in range(minx,maxx+1):
        W[i][h["y1"]] = W[i][h["y1"]] +1


print("Answer 1:",sum(sum(W>1)))

# -- also lines with 45 degree angle

dg = [item for item in points if item not in vertic]
dg = [item for item in dg if item not in horiz]


for l in dg:

    y = l["y1"]
    dy = 1 if l["y2"]-l["y1"] > 0 else -1
    dx = 1 if l["x2"]-l["x1"] > 0 else -1
    
    for x in range(l["x1"],l["x2"]+dx,dx):
        W[x][y] = W[x][y] +1
        y = y + dy

        
print("Answer 2:",sum(sum(W>1)))



