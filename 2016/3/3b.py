#!/usr/bin/python3
import sys

def goffa():

    l1 = sys.stdin.readline().strip().split()
    l2 = sys.stdin.readline().strip().split()
    l3 = sys.stdin.readline().strip().split()

    if not l1 or not l2 or not l3:
        raise errorfail
    
    return [[l1[0],l2[0],l3[0]],
            [l1[1],l2[1],l3[1]],
            [l1[2],l2[2],l3[2]]]

f=[]
            
while True:

    try:
        a=goffa()
        f=f+a
    except:
        break

n = []
for t in f:
    print(t)
    n.append([int(x) for x in t])

def f(t):
    v = ((t[0]+t[1])>t[2]) and ((t[0]+t[2])>t[1]) and ((t[1]+t[2])>t[0])
    return v
    
n = filter(f,n)

print("Answer 2: ",len(list(n)))
