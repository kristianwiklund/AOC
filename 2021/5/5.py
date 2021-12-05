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

# --
def draw(W,l):
    dy = 1 if l["y2"]-l["y1"] > 0 else (-1 if l["y2"]-l["y1"] < 0 else 0)
    dx = 1 if l["x2"]-l["x1"] > 0 else (-1 if l["x2"]-l["x1"] < 0 else 0)

    x = l["x1"]
    y = l["y1"]
    
    for i in range(max(abs(l["y2"]-l["y1"]),abs(l["x2"]-l["x1"]))+1):
        W[x][y] = W[x][y] +1
        y = y + dy
        x = x + dx

# --
W = numpy.zeros(shape=(1000,1000))

st = list(filter(lambda p: (p["x1"] == p["x2"]) or (p["y1"] == p["y2"]), points))

for p in st:
    draw(W,p)

print("Answer 1:",sum(sum(W>1)))

# -- also lines with 45 degree angle

dg = [item for item in points if item not in st]

for l in dg:
    draw(W,l)
        
print("Answer 2:",sum(sum(W>1)))



