#!/usr/bin/python3
import sys

f = [t.strip() for t in sys.stdin]

score=0
inv = {'<':'>','(':')','[':']','{':'}'}
pts = {'>':25137,')':3,']':57,'}':1197}
for l in f:
    s = []
    for x in l:
        if x in "<({[":
            s.append(x)
        else:
            t = s.pop()
            if inv[t]==x:
                pass
                #print("pop",t,x)
            else:
                print("bop",t,x)
                score = score + pts[x]

print(score)
