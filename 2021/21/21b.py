#!/usr/bin/python3

from copy import copy
import random
import sys
import functools

rolls = 0

def ph(x):
    while x>10:
        x-=10
    return x

def nr(x):
    global rolls
    rolls +=1
    return x if x<=100 else x-100


# how this crap works:
# - we roll the dice. this takes us down one level recursively, where we roll the dice again. once done, we go another depth to a total of three, and check the score

def updatecache(who, pos, score, roll, rec, A):

    if not (who, pos[0], pos[1], score[0], score[1], roll, rec) in cache:
        cache[who, pos[0], pos[1], score[0], score[1], roll, rec] = copy(A)

wins=0
hits=0
hitss=0

@functools.cache
def dive(who, pos, score, roll, rec, deep, kent=[]):
    global wins
    global hits
    global hitss
    
    #print("who,pos,roll,score,rec,deep")
    #print(who,pos, roll, score, rec, deep)
    
    # if we already have done the investigation for this branch, return that value
    #if (who, pos[0], pos[1], score[0], score[1], roll, rec) in cache:
    #    hits+=1
    #    hitss+=sum( cache[who, pos[0], pos[1], score[0], score[1], roll, rec])
    #    #        print(hitss+wins)

    #    if hits%100000==0:
    #        print("hits/wins",hitss//wins)
    #    return cache[who, pos[0], pos[1], score[0], score[1], roll, rec]

    # then we start by adding the roll to the position and update where we are
    pos[who]=ph(pos[who]+roll)

    # if this is our third roll, we add to our score and check if we won
    # if we did, we return the win
    # if we didn't, we let the other player continue

    if rec==3:
        score[who]+=pos[who]
        
        if score[who] >= 21:
            #print(who, "won after",deep,"rolls, positions are",pos,"scores are",score)
            
            #from pprint import pprint
            #print ("who,pos,score,roll,phase")
            #pprint (kent+[(who,pos,score,-1,rec+1)])
            #            sys.exit()
            win = [0,0]
            win[who] = 1
            wins+=1
            return win

        rec=0
        who = 1 - who

    # do the rolls.

    r1 = nr(roll+3)
    r2 = nr(roll+2)
    r3 = nr(roll+1)

    #vrom = [r3,r2,r1]
    #random.shuffle(vrom)
    #r1 = vrom[0]
    #r2 = vrom[1]
    #r3 = vrom[2]

    # 786316482957123

    # [236663445107213292343991, 219491482515848882486684]
    # [236663445107213292343991, 219491482515848882486684]
    # [236663445107213292343991, 219491482515848882486684]
    # [236663445107213292343991, 219491482515848882486684]

    assert(rec<=2 and rec >=0)
    assert(r3<=100 and r3>0)
    assert(r2<=100 and r2>0)
    assert(r1<=100 and r1>0)

    assert(pos[0]<=10 and pos[0]>0)
    assert(pos[1]<=10 and pos[1]>0)

#    assert(score[0]>=0 and score[0]<21)
#    assert(score[1]>=0 and score[1]<21)
    
    A = dive(who, copy(pos), copy(score), r3, rec+1, deep+1, kent + [(who,pos,score,r3,rec+1)])
    updatecache(who, pos, score, r3, rec+1, A)
    B = dive(who, copy(pos), copy(score), r2, rec+1, deep+1, kent + [(who,pos,score,r2,rec+1)])
    updatecache(who, pos, score, r2, rec+1, B)
    C = dive(who, copy(pos), copy(score), r1, rec+1, deep+1, kent + [(who,pos,score,r1,rec+1)])
    updatecache(who, pos, score, r1, rec+1, C)

    return [A[0]+B[0]+C[0],A[1]+B[1]+C[1]]

# --

pos = [4,8]
pos = [9,3]
score = [0,0]

who=0
# dive(who, pos, score, roll, rec,deep):
A = dive(who, copy(pos), copy(score), 1, 1, 1)
updatecache(who, pos, score, 1, 1, A)
B = dive(who, copy(pos), copy(score), 2, 1, 1)
updatecache(who, pos, score, 2, 1, B)
C = dive(who, copy(pos), copy(score), 3, 1, 1)

print ("rolls",rolls,"scores",[A[0]+B[0]+C[0],A[1]+B[1]+C[1]])

            
            
