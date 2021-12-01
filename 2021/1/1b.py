#!/usr/bin/python3

import fileinput
import rolling

l=list()

for line in fileinput.input():
    l.append(int(line))

rl = list(rolling.Sum(l,3))

zl = list(zip(rl[:-1],rl[1:]))

def c(t):
      return 1 if t[0]<t[1] else 0

print(sum(list(map(c,zl))))

