#!/usr/bin/python3
import sys

def input():
    return     [15,12,0,14,3,1]


def input2():
    return     [3,1,2]

def mkim(l):

    return {l[x]:[x+1] for x in range(0,len(l))}

def sayh(number, mydict, turn):

    if number in mydict:
        mylist = [turn,mydict[number][0]]
    else: 
        mylist = [turn,turn]
        
    mydict[number] = mylist

    thesum = mylist[0]-mylist[1]
    return thesum
    

def say2(number, mydict, turns):

    for i in range(turns,2020):
        number = sayh(number, mydict, i)
        
    return(number)
        
def ta2():
    x= mkim(input2())

    return say2(0, x,4)

print (ta2())
