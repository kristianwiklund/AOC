#!/usr/bin/python3
import sys

f = [t.split(",") for t in sys.stdin]
f = sorted([int(x) for x in f[0]])

fish = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for i in f:
    fish[i] = fish[i] + 1

#print(fish)

for d in range(256):

    fn = fish[0]

    for i in range(8):
        fish[i]=fish[i+1]

    fish[8] = fn
    fish[6] = fish[6] + fn

print(fish)
s=0
for i in fish:
   s=s+fish[i]

print(s)
