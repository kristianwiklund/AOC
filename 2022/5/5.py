from copy import deepcopy

def tjonk(s):
    t = s[0:3]
    r = s[4:]

    if t=="   ":
        t=None

    return (t,r)

torn = dict()
for i in range(1,10):
    torn[i]=list()

with open("input.torn","r") as fd:

    lines = [x.rstrip() for x in fd.readlines()]

    for line in lines:
        print("")
        i = 1
        
        while line:
            (t,line)=tjonk(line)
            if t:
                #print(t,end="")
                torn[i].append(t)
            #else:
            #    print ("...",end="")
            i+=1
#print("")
print(torn)
for i in range(1,10):
    torn[i].reverse()

tb = deepcopy(torn)
    
def move(torn,n,f,t):
    while n:
        b = torn[f].pop()
        torn[t].append(b)
        n-=1
    return torn
        

with open("input.code","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    for line in lines:
        print(line)
        line = line.split(" ")
        n = int(line[1])
        f = int(line[3])
        t = int(line[5])

        torn = move(torn,n,f,t)

print("Part 1")

for i in range(1,10):
    torn[i].reverse()
    if len(torn[i]):
        print(torn[i][0],end="")
    else:
        print("...",end="")
        
print("")

#-------

torn = tb


def move9001(torn,n,f,t):
    l = list()
    while n:
        b = torn[f].pop()
        l.append(b)
        n-=1
    l.reverse()
    torn[t] = torn[t]+l
    return torn
        

with open("input.code","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    for line in lines:
        print(line)
        line = line.split(" ")
        n = int(line[1])
        f = int(line[3])
        t = int(line[5])

        torn = move9001(torn,n,f,t)

print("Part 2")

for i in range(1,10):
    torn[i].reverse()
    if len(torn[i]):
        print(torn[i][0],end="")
    else:
        print("...",end="")
        
print("")

