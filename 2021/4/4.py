#!/usr/bin/python3

import csv,sys
from pprint import pprint
from bb import BB


# ------

randoms = next(sys.stdin).strip().split(",")
print(randoms)

boards = list()
try:
    while True:
        next(sys.stdin)
                
        a = BB(sys.stdin)
        boards.append(a)
        #        print(a)
                
except:
    pass



for i in randoms:
    print("Drawing ",i)
    s = [x.draw(int(i)) for x in boards]
    if sum(s):
        print (s)
        break

for t in range(len(s)):
    if s[t]:
        s = boards[t].score()
        break
print(int(i),s,int(i)*s)
