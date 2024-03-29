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
        i = 1
        
        while line:
            (t,line)=tjonk(line)
            if t:
                torn[i].append(t)

            i+=1

for i in range(1,10):
    torn[i].reverse()

tb = deepcopy(torn)
    
def move(torn,n,f,t):

    torn[t] = torn[t]+list(reversed(torn[f][-n:]))
    torn[f] = torn[f][:-n]
        
    return torn


def move9001(torn,n,f,t):

    torn[t] = torn[t]+torn[f][-n:]
    torn[f] = torn[f][:-n]

    return torn

with open("input.code","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    for line in lines:
        line = line.split(" ")
        n = int(line[1])
        f = int(line[3])
        t = int(line[5])

        torn = move(torn,n,f,t)
        tb = move9001(tb,n,f,t)

p1 = "".join([torn[x][-1] for x in torn]).replace("[","").replace("]","")
p2 = "".join([tb[x][-1] for x in tb]).replace("[","").replace("]","")

print ("Part 1:",p1)
print ("Part 2:",p2)

