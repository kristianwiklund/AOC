#!/usr/bin/python3
import sys

preamble=25

def check(x, stack):

    p = range(0,len(stack))
    t = [[(stack[x]+stack[y]) for x in p if x!=y] for y in p]
    t = [i for s in t for i in s]
    
    return (x in t)

def ingest(i, stack, mymax, helalistan):

    stack.append(i)
    helalistan.append(i)
    
    if(len(stack) > mymax):
        stack.pop(0)


def readint(fd):
    l = fd.readline()
    l.strip("\n\r ")

    return(int(l))

# find a sequence in hl that sum up to x
def fulcheck(talet, hl):
    r = range(0, len(hl))

    u = [[(x,y,sum(hl[x:y])) for x in r if x<y] for y in r]
    u = [i for s in u for i in s]

    a = [[x,y] for x,y,s in u if s==talet][0]
            
    l = hl[a[0]:a[1]]
    
    print("B:"+str(min(l)+max(l)))
    
# ---
fd = open('input', 'r')


stack = list()
hl = list() # hela listan

# get the first (twenty-)five
for i in range(0,preamble):
    x = readint(fd)
    ingest(x, stack, preamble, hl)


# then go on working

while True:

    x = readint(fd)

    if (not check(x, stack)):
        print("Wrong number: "+str(x))

        li = fulcheck(x, hl)
        sys.exit()
    
    ingest(x, stack, preamble, hl)
