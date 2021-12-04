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


theboard = None
for i in randoms:
    print("Drawing ",i)
    s = [x.draw(int(i)) for x in boards]
    if sum(s)==(len(boards)-1):
        for t in range(len(s)):
            if not s[t]:
                theboard = t
                break
    if sum(s)==len(boards):
        break
    


print ("board ",t," is the board")
s = boards[t].score()
print("Score: ",int(i)*s)
