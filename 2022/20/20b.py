import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

with open("input.txt","r") as fd:
    arr = [int(x) for x in fd.readlines()]

    nein = set()
    for i in range(len(arr)):

        c=0
        while True:
            v = chr(c+ord("A"))+str(arr[i])
            c+=1

            if not v in nein:
                break
        nein.add(v)
        arr[i]=v


    def move(arr,what):

        number = int(what[1:])

        if number==0:
            return arr

        if abs(number)==len(arr)-1:
            return arr

        where = arr.index(what)

        to = (where+number)%(len(arr)-1)
        del arr[where]
        
        arp = arr[:to]+[what]+arr[to:]

        return(arp)


    print("== Running tests")
    
    assert(move(["A4", "A5", "A6", "A1", "A7", "A8", "A9"],"A1") == ["A4", "A5", "A6", "A7", "A1", "A8", "A9"])
    assert(move(["A4", "A-2", "A6", "A1", "A7", "A8", "A9"],"A-2") == ["A4", "A6", "A1", "A7", "A8", "A-2", "A9"])

    print("== Done running tests")
    
    def shuffle(arr,barr):
        for i in barr:
            arr = move(arr,i)
            
        return arr

    res = shuffle(arr,deepcopy(arr))
    i = res.index("A0")

    a = int(res[(i+1000)%len(res)][1:])
    b = int(res[(i+2000)%len(res)][1:])
    c = int(res[(i+3000)%len(res)][1:])

    print("Part 1:",a+b+c)

    
