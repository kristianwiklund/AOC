#!/usr/bin/python3

import sys
from pprint import pprint

foods = dict()
allergens=dict()

def readone(line,foods,allergens):

    line=line.strip("\n)")
    t=line.split("(")
    #    print(line)
    a=t[0]
    b=t[1].replace(",","")

    a=a.strip(" ").split(" ")

    b=b.split(" ")

    # now move over all the foods and all the allergens
    # if a food tagged with allergen A appear in a list that is not tagged with A, then that food cannot have allergen A

    for i in a:
        if i in foods:
            x = foods[i] | set(b)        # then add potential allergens
            foods[i] = x
        else:
            foods[i] = set(b)


    for i in b:
        if i in allergens:
            x = allergens[i] | set(a)
            allergens[i] = x
        else:
            allergens[i] = set(a)

    return (foods,allergens)


# -- "main" --

line=sys.stdin.readline()
while line:

    (foods,allergens)=readone(line,foods,allergens)
    line=sys.stdin.readline()

pprint(foods)
pprint(allergens)

for i in foods:
    print (len(foods[i]),i)
