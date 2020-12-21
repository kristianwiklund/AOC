#!/usr/bin/python3

import sys
from pprint import pprint

allergens=dict()
foods=set([])
thelist=list()

def readone(line,foods,allergens,thelist):

    line=line.strip("\n)")
    t=line.split("(")
    #    print(line)
    a=t[0]
    b=t[1].replace(",","")

    a=a.strip(" ").split(" ")

    a=set(a)

    b=b.split(" ")


    #print(b)

    foods=a|foods

    thelist.append(a)
    for i in b:
        if i in allergens:
            # remove previously tagged items NOT in the new list
            a=allergens[i] & a
            # then add potentially new items
            #a=allergens[i] | a
        allergens[i]=a

    return foods,allergens,thelist
    
line=sys.stdin.readline()
while line:
    foods,allergens,thelist=readone(line,foods,allergens,thelist)
    line=sys.stdin.readline()

aa=set()

# sum all with allergens in them
for i in allergens:
    aa=aa|allergens[i]

print(allergens)
    
bb=foods-aa
print("okay food:", len(bb))
print(" bad food:", len(aa))
print("     food:", len(foods))
#print(thelist)
c=0
for i in thelist:
    #    print(len(i),len(i&aa))
    c=c+len(i&bb)

print(c)
# 2535 too high
# 760 too low
# 41 too low
