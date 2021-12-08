#!/usr/bin/python3

import sys,numpy

symbols = {2:1,4:4,3:7,7:8}
cnt = [0,0,0,0,0,0,0,0,0,0]

f = [t.strip() for t in sys.stdin]

for t in f:
#    print(t)
    b = t.split(" | ")[1]

    for i in b.split(" "):
        if len(i) in symbols:
            cnt[len(i)] = cnt[len(i)] + 1

print ("Answer 1:",sum(cnt))

