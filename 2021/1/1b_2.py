#!/usr/bin/python3
import rolling,sys

rl= list(rolling.Sum([int(t) for t in sys.stdin],3)) 
print(sum([rl[x]<rl[x+1] for x in range(len(rl[:-1]))]))


