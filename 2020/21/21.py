#!/usr/bin/python3

import sys

allergens=dict()
foods=set([])
thelist=list()

def readone(line,foods,allergens):

    line=line.strip(")\n")
    t=line.split("(")
    a=t[0]
    b=t[1].replace(",","")
    a=set(a.strip(" ").split(" "))
    b=b.split(" ")

    foods=a|foods
    thelist.append(a)
    for i in b:
        if i in allergens:
            a=allergens[i] & a
        allergens[i]=a

    return foods,allergens
    
line=sys.stdin.readline()
while line:
    foods,allergens=readone(line,foods,allergens)
    line=sys.stdin.readline()

aa=set()

for i in allergens:
    aa=aa|allergens[i]

bb=foods-aa
print(aa)
print(bb)
print(thelist)
c=0
for i in thelist:
    print(i, len(i&bb))
    c=c+len(i&bb)

print(c)

# 2535 too high
