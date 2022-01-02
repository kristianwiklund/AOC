#!/usr/bin/python3

from copy import copy

def ph(x):
    while x>10:
        x-=10
    return x

def nr(x):
    return x if x<=100 else x-100


# how this crap works:
# - we roll the dice. this takes us down one level recursively, where we roll the dice again. once done, we go another depth to a total of three, and check the score

cache=dict()

def dive(who, pos, score, roll, rec,deep):

    pos[who]=ph(pos[who]+roll)

    if (pos[who], score[who], roll, rec) in cache:
        return cache(pos[who], score[who], roll, rec)
    
    rec+=1
    #    print("rec",rec,"who",who,"roll",roll)
    if rec==3:
        score[who]+=pos[who]
        
        if score[who] >= 21:
            #print(who, "won at depth",rec,"position",pos[who])
            win = [0,0]
            win[who] = 1
            return win
        rec=0
        who = 1-who

    # do the rolls. the highest first

    r3 = nr(roll+3)
    r2 = nr(roll+2)
    r1 = nr(roll+1)

    [s31,s32] = dive(who, copy(pos), copy(score), r3, rec, deep+1)
    [s21,s22] = dive(who, copy(pos), copy(score), r2, rec, deep+1)
    [s11,s12] = dive(who, copy(pos), copy(score), r1, rec, deep+1)

    return [s31+s21+s11,s32+s22+s12]

# --

pos = [4,8]
score = [0,0]
roll = 0

print(dive(0,pos,score,0,-1,0))

            
            
