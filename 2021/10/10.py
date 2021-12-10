#!/usr/bin/python3
import sys

f = [t.strip() for t in sys.stdin]

score=0
inv = {'<':'>','(':')','[':']','{':'}'}
pts = {'>':25137,')':3,']':57,'}':1197}
inc=[]
for l in f:
    s = []
    borked = False
    for x in l:
        if x in "<({[":
            s.append(x)
        else:
            t = s.pop()
            if inv[t]==x:
                pass
                #print("pop",t,x)
            else:
                #print("bop",t,x)
                score = score + pts[x]
                borked = True
                break
    if not borked:
        s.reverse()
        inc.append(s)
    
print("Answer 1:",score)
#print(inc)
scorez = []
pts = {'<':4,'(':1,'[':2,'{':3}
for l in inc:
    score = 0
    for x in l:
        score = score * 5 + pts[x]
    scorez.append(score)

s = sorted(scorez)
print("Answer 2:", s[len(s)//2])
