#!/usr/bin/python3.10

from copy import copy
import random
import sys
import functools

rolls = 0

def ph(x):
    while x>10:
        x-=10
    return x

wins=0
hits=0
hitss=0

@functools.cache
def dive(who, mypos, theirpos, myscore, theirscore, roll, rec):
    global wins
    global hits
    global hitss
    
    mypos=ph(mypos+roll)

    if rec==3:
        
        myscore+=mypos
        
        if myscore >= 21:
            win = [0,0]
            win[who] = 1
            wins+=1
            return win

        rec=0
        who = 1 - who
        mp=mypos
        ms=myscore
        mypos=theirpos
        myscore=theirscore
        theirpos=mp
        theirscore=ms

    # do the rolls.

    A = dive(who, mypos,theirpos, myscore,theirscore, 1, rec+1)
    B = dive(who, mypos,theirpos, myscore,theirscore, 2, rec+1)
    C = dive(who, mypos,theirpos, myscore,theirscore, 3, rec+1)

    return [A[0]+B[0]+C[0],A[1]+B[1]+C[1]]

# --

#pos = [4,8]
pos = [9,3]
myscore=0
theirscore=0

mypos=pos[0]
theirpos=pos[1]

who=0
# dive(who, pos, score, roll, rec,deep):
A = dive(who, mypos,theirpos, myscore,theirscore, 1, 1)
B = dive(who, mypos,theirpos, myscore,theirscore, 2, 1)
C = dive(who, mypos,theirpos, myscore,theirscore, 3, 1)

print ("Answer 2:",max([A[0]+B[0]+C[0],A[1]+B[1]+C[1]]))

            
            
