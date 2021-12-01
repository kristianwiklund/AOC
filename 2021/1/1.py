#!/usr/bin/python3

import fileinput

t=None
c=0
for line in fileinput.input():
    if t and int(line)>t:
        c+=1
    t = int(line)
print(c)
