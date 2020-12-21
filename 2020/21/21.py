#!/usr/bin/python3

import sys
from pprint import pprint

foods = dict()

def readone(line,foods):

    line=line.strip("\n)")
    t=line.split("(")
    #    print(line)
    a=t[0]
    b=t[1].replace(",","")

    a=a.strip(" ").split(" ")

    b=b.split(" ")

    
    for i in a:
        if not i in foods:
            foods[i] = set()
        foods[i]|=set(b)
    
    return foods

# -- "main" --

line=sys.stdin.readline()
while line:

    foods=readone(line,foods)
    line=sys.stdin.readline()

print("-")
pprint(foods)
print("-")

