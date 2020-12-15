#!/usr/bin/python3
import sys

def input():
    return     [15,12,0,14,3,1]


def input2():
    return     [0,3,6]

def mkim(l):

    return {l[x]:[x+1] for x in range(0,len(l))}

def sayh(number, mydict, turn):

    if number in mydict:
        mylist = [turn]+mydict[number]
    else: 
        mylist = [turn,turn]

    thesum = mylist[0]-mylist[1]
    mydict[number] = mylist[0:2]
#    print(mylist)
    return thesum
    

def say2(number, mydict, turns):

    for i in range(turns,30000000):
        number = sayh(number, mydict, i)
    return(number)
        
def ta2():
    x= mkim(input())

    return say2(0, x,7)

print (ta2())
