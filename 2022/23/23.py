import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.txt",split="",convert=lambda x:x)
elves = arr2sparse(arr,ignore=".")




d = {
    "N":(0,-1),
    "E":(1,0),
    "S":(0,1),
    "W":(-1,0)
    }


for x in ["NE","NW","SE","SW"]:
    d[x[0]+x[1]]=addtuples(d[x[0]],d[x[1]])

#print(d)

order=["N","S","E","W"]

def haself(elves,elf,dr):
    (x,y)=elf
    return (x+d[dr][0],y+d[dr][1]) in elves

#    If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
#    If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
#    If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
#    If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

def findmove(elves, elf):
    global order
    
    for x in order:
        if x=="N":
            if not (haself(elves, elf, "N") or haself(elves,elf,"NE") or haself(elves,elf,"NW")):
                return addtuples(elf,d["N"])

        if x=="S":
            if not (haself(elves, elf, "S") or haself(elves,elf,"SE") or haself(elves,elf,"SW")):
                return addtuples(elf,d["S"])

        if x=="E":
            if not (haself(elves, elf, "W") or haself(elves,elf,"NW") or haself(elves,elf,"SW")):
                return addtuples(elf,d["W"])

        if x=="W":
            if not (haself(elves, elf, "E") or haself(elves,elf,"NE") or haself(elves,elf,"SE")):
                return addtuples(elf,d["E"])

    return None


class Deadlock(Exception):
    pass

def phase1(elves):
    
    moves=[]
    reg=dict()
    for elf in elves:

        #During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
        m=False
        for i in d:
            if haself(elves,elf,i):
                m=True

        #Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:
        if m:
            n = findmove(elves,elf)
            if n:
                moves.append((elf,n))
                if not n in reg:
                    reg[n]=1
                else:
                    reg[n]+=1

    def p2e(t):
        elf,new=t
        return (not (new in reg)) or (reg[new]==1)

#    print(moves)
#    print(reg)
    moves = filter(p2e,moves)

    return(moves)


def phase2(elves,moves):

    um=0
    for i in moves:
        um+=1
        elf,new=i
        del elves[elf]
        elves[new]="#"

    if um==0:
        raise Deadlock
    
    return(elves)

def tick(elves):
    global order

        
    moves=phase1(elves)
    elves=phase2(elves, moves)
    #print(order)
    #score(elves)
    
    order.append(order[0])
    order=order[1:]
    return(elves)

def score(elves):

    maxx = max([x for x,y in elves])
    minx = min([x for x,y in elves])
    maxy = max([y for x,y in elves])
    miny = min([y for x,y in elves])

    s=0
    #print("-"*(maxx-minx+1))
    for y in range(miny,maxy+1):
        for x in range(minx, maxx+1):
            if not (x,y) in elves:
                s+=1
                #print(".",end="")
            #else:
             #   print("#",end="")
        #print("")
    #print("")
    return s

score(elves)
r=0
for i in range(10):
    r+=1
    elves=tick(elves)

print("Part 1:",score(elves))
    
while True:
    try:
        r+=1
        elves=tick(elves)
    except:
        break


print("Part 2:",r)
    


                
            
        
    




