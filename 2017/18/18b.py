import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
#from copy import deepcopy
from pprint import pprint
#from sortedcontainers import SortedList
#from sortedcontainers import SortedDict
#from sortedcontainers import SortedSet
#import numpy as np
#import scipy
#from functools import cache
from threading import Thread
from queue import Queue

arr = readarray("input",split=" ",convert=lambda x:x)

def getval(reg, val):

    try:
        return int(val)
    except:
        try:
            return reg[val];
        except:
            return 0

pipe={0:Queue(),
      1:Queue()}

sc = {0:0,1:0}

def send(pipe, me, value):
    global sc
    pipe[me].put(value)
    sc[me]+=1
    print("Sent: 0=",sc[0],", 1=",sc[1])
                    

def receive(pipe, me):
    global rc
    return pipe[1-me].get()


@timer
def runprog(arr,prognum=0):
    global pipe
    pc=0
    reg=dict()
    sound=0

    reg["p"]=prognum
    
    while True:

        if pc>=len(arr):
            print ("END")
            break

        i =arr[pc][0]
        o1 = arr[pc][1]
        if len(arr[pc])>2:
            o2 = arr[pc][2]

    
        match i:
            case "snd":
                sound=getval(reg, o1)
                send(pipe, prognum, sound)
            case "set":
                reg[o1]=getval(reg, o2)
            case "add":
                reg[o1]=getval(reg, o1) + getval(reg, o2)
            case "mul":
                reg[o1]=getval(reg, o1) * getval(reg, o2)
            case "mod":
                reg[o1]=getval(reg, o1) % getval(reg, o2)
            case "rcv":
                v = receive(pipe, prognum)
                reg[o1] = v
                    
            case "jgz":
                v = getval(reg, o1)
                if v>0:
                    pc+=getval(reg, o2)
                    continue
        pc+=1


#runprog(arr, prognum=1)

a = Thread(target=runprog,args=(arr,0))
b = Thread(target=runprog,args=(arr,1))
a.start()
b.start()
