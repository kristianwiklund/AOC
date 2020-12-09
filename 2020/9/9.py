#!/usr/bin/python3
import sys

preamble=25

def check(x, stack):

    p = range(0,len(stack))
    t = sum([[(stack[x]+stack[y]) for x in p if x!=y] for y in p],[])

    return (x in t)

def ingest(i, stack, mymax):

    stack.append(i)
    
    if(len(stack) > mymax):
        stack.pop(0)

    return(stack)

def readint(fd):
    l = fd.readline()
    l.strip("\n\r ")

    return(int(l))
    
# ---
fd = open('input', 'r')


stack = list()

# get the first five
for i in range(0,preamble):
    x = readint(fd)
    ingest(x, stack, preamble)

print (stack)

# then go on working

while True:

    try:
        x = readint(fd)
    except:
        sys.exit()

    if (not check(x, stack)):
        print("Wrong number: "+str(x))
        sys.exit()
    
    ingest(x, stack, preamble)
